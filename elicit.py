"""
elicit.py — Path C elicitation engine
Cybersecurity readiness assessment system — UL

Usage:
    python elicit.py --archetype consumer-thermostat --product "Acme ThermoSmart 200" --assessor "J. Smith"
    python elicit.py --archetype iot-gateway --product "Acme GW-200" --assessor "J. Smith"
    python elicit.py --resume sessions/acme-gw-200.json

Requires:
    pip install anthropic rich pydantic python-dotenv

Setup:
    Copy .env.example to .env in the repo root and add your Anthropic API key:
        ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx
"""

import argparse
import json
import uuid
import sys
from datetime import date
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
import anthropic
from pydantic import BaseModel
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm
from rich import print as rprint

# ── Load .env from repo root ──────────────────────────────────────────────────
# Works whether elicit.py lives at repo root or in a scripts/ subfolder
_SCRIPT_DIR = Path(__file__).resolve().parent
_REPO_ROOT  = _SCRIPT_DIR.parent if _SCRIPT_DIR.name == "scripts" else _SCRIPT_DIR
load_dotenv(_REPO_ROOT / ".env")

# ── Paths (resolve relative to repo root regardless of where script lives) ───
ARCHETYPES_DIR = _REPO_ROOT / "archetypes"
SESSIONS_DIR   = _REPO_ROOT / "sessions"
OUTPUT_DIR     = _REPO_ROOT / "output"

SESSIONS_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)

console = Console()

# ── API key check ─────────────────────────────────────────────────────────────
import os
_api_key = os.getenv("ANTHROPIC_API_KEY")
if not _api_key:
    Console().print(
        "[red bold]ANTHROPIC_API_KEY not set.[/red bold]\n"
        f"Create a [cyan].env[/cyan] file at [cyan]{_REPO_ROOT}[/cyan] with:\n\n"
        "    ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxx\n\n"
        "Get your key at [cyan]https://console.anthropic.com[/cyan]"
    )
    sys.exit(1)

client = anthropic.Anthropic(api_key=_api_key)


# ── Pydantic models (mirrors DB schema) ──────────────────────────────────────

class ConfirmedComponent(BaseModel):
    id: str
    template_id: str
    actual_name: str
    notes: str = ""
    confirmed_properties: list[str] = []

class ConfirmedConnection(BaseModel):
    id: str
    template_id: str
    source_id: str
    target_id: str
    actual_protocols: list[str] = []
    notes: str = ""

class SessionState(BaseModel):
    instance_id: str
    archetype_id: str
    product_name: str
    assessor: str
    assessment_date: str
    confirmed_components: list[ConfirmedComponent] = []
    confirmed_connections: list[ConfirmedConnection] = []
    pending_component_ids: list[str] = []
    pending_connection_ids: list[str] = []
    conversation_history: list[dict] = []
    complete: bool = False


# ── Archetype loader ──────────────────────────────────────────────────────────

def load_archetype(name: str) -> dict:
    path = ARCHETYPES_DIR / f"{name}.json"
    if not path.exists():
        available = [p.stem for p in ARCHETYPES_DIR.glob("*.json")]
        console.print(f"[red]Archetype '{name}' not found.[/red]")
        console.print(f"Available: {', '.join(available)}")
        sys.exit(1)
    return json.loads(path.read_text(encoding="utf-8"))


# ── Session persistence ───────────────────────────────────────────────────────

def save_session(session: SessionState) -> Path:
    """Atomic save: write to a .tmp file then rename, so a crash never corrupts the session."""
    path     = SESSIONS_DIR / f"{session.instance_id}.json"
    tmp_path = path.with_suffix(".tmp")
    tmp_path.write_text(session.model_dump_json(indent=2), encoding="utf-8")
    tmp_path.replace(path)   # atomic on all major OS / filesystems
    return path

def load_session(path: str) -> SessionState:
    """Load session with a clear error if the file is empty or corrupted."""
    p    = Path(path)
    text = p.read_text(encoding="utf-8").strip()
    if not text:
        console.print(f"[red]Session file '{path}' is empty or corrupted and cannot be resumed.[/red]")
        console.print("Please start a new session with [cyan]--archetype[/cyan] and [cyan]--product[/cyan].")
        sys.exit(1)
    try:
        return SessionState.model_validate_json(text)
    except Exception as e:
        console.print(f"[red]Could not parse session file '{path}': {e}[/red]")
        console.print("Please start a new session with [cyan]--archetype[/cyan] and [cyan]--product[/cyan].")
        sys.exit(1)

def init_session(archetype: dict, product_name: str, assessor: str) -> SessionState:
    return SessionState(
        instance_id=str(uuid.uuid4())[:8],
        archetype_id=archetype["id"],
        product_name=product_name,
        assessor=assessor,
        assessment_date=str(date.today()),
        pending_component_ids=[c["id"] for c in archetype["component_templates"]],
        pending_connection_ids=[c["id"] for c in archetype["connection_templates"]],
    )


# ── Claude interview helpers ──────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a cybersecurity assessor conducting a structured product interview.
Your role is to ask clear, concise questions about a specific component or connection of the product
under assessment, interpret the analyst's answer, and determine whether the element is:
  - CONFIRMED (present as described or with modifications)
  - REJECTED (not present in this product)
  - NEEDS_FOLLOWUP (answer was ambiguous — ask one clarifying question)

Always respond in this JSON format:
{{
  "status": "CONFIRMED" | "REJECTED" | "NEEDS_FOLLOWUP",
  "question": "<the question to display to the analyst, or the follow-up>",
  "interpretation": "<brief summary of what was understood from the analyst's answer>",
  "confirmed_properties": ["<property1>", ...],
  "actual_protocols": ["<protocol1>", ...],
  "notes": "<any relevant detail to record>"
}}

On the first turn for a component, set status to NEEDS_FOLLOWUP and question to the first
elicitation question. Do not try to confirm or reject before the analyst has answered.
Keep questions short and non-technical where possible — the analyst may not be an engineer.
"""

def _extract_json(raw: str) -> str:
    """
    Try progressively looser strategies to extract a JSON object from a raw string.
    1. Strip markdown fences and parse directly.
    2. Find the first { ... } block in the string.
    Returns the cleaned string (may still fail json.loads if truly malformed).
    """
    # Strategy 1 — strip fences
    clean = raw.strip()
    for prefix in ("```json", "```"):
        if clean.startswith(prefix):
            clean = clean[len(prefix):]
    if clean.endswith("```"):
        clean = clean[:-3]
    clean = clean.strip()
    if clean:
        return clean

    # Strategy 2 — find first JSON object by brace matching
    start = raw.find("{")
    if start != -1:
        depth = 0
        for i, ch in enumerate(raw[start:], start):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0:
                    return raw[start:i+1]
    return clean


def ask_claude(session: SessionState, archetype: dict, element: dict, element_type: str) -> dict:
    """
    Send one turn of the interview to Claude and return its structured response.
    Retries up to 3 times on JSON parse errors, with a corrective prompt.
    Falls back to a safe NEEDS_FOLLOWUP dict if all retries fail.
    """
    context = {
        "product": session.product_name,
        "archetype": archetype["name"],
        "element_type": element_type,
        "element_name": element.get("name", f"{element.get('source_component_id','?')} -> {element.get('target_component_id','?')}"),
        "elicitation_questions": element.get("elicitation_questions", []),
        "security_properties": element.get("security_properties", []),
        "session_so_far": {
            "confirmed_components": [c.model_dump() for c in session.confirmed_components],
            "confirmed_connections": [c.model_dump() for c in session.confirmed_connections],
        }
    }

    messages = session.conversation_history + [
        {
            "role": "user",
            "content": f"Element context: {json.dumps(context, indent=2)}\n\nProceed with the interview for this element."
        }
    ]

    max_retries = 3
    last_raw = ""

    for attempt in range(max_retries):
        try:
            response = client.messages.create(
                model="claude-sonnet-4-6",
                max_tokens=1000,
                system=SYSTEM_PROMPT,
                messages=messages,
            )
            last_raw = response.content[0].text if response.content else ""
            clean = _extract_json(last_raw)
            return json.loads(clean)

        except json.JSONDecodeError:
            if attempt < max_retries - 1:
                console.print(
                    f"[yellow]⚠ JSON parse error on attempt {attempt + 1} — retrying...[/yellow]"
                )
                # Add a corrective turn asking Claude to reply in pure JSON
                messages = messages + [
                    {"role": "assistant", "content": last_raw},
                    {"role": "user",      "content":
                        "Your previous response was not valid JSON. "
                        "Reply ONLY with a valid JSON object matching the schema in the system prompt. "
                        "No prose, no markdown fences, no explanation — just the JSON object."}
                ]
            else:
                console.print(
                    f"[red]✗ Could not parse Claude response after {max_retries} attempts.[/red]\n"
                    f"[dim]Raw response: {last_raw[:300]}{'...' if len(last_raw) > 300 else ''}[/dim]"
                )

        except Exception as e:
            console.print(f"[red]✗ API error: {e}[/red]")
            break

    # Safe fallback — surface the first elicitation question manually
    fallback_question = (
        element.get("elicitation_questions", ["Can you describe this component?"])[0]
    )
    return {
        "status": "NEEDS_FOLLOWUP",
        "question": fallback_question,
        "interpretation": "Could not parse Claude response — using fallback question.",
        "confirmed_properties": [],
        "actual_protocols": [],
        "notes": f"Fallback after {max_retries} failed JSON parse attempts."
    }


# ── Interview loop for one element ───────────────────────────────────────────

def interview_element(session: SessionState, archetype: dict, element: dict, element_type: str) -> Optional[dict]:
    """
    Run the back-and-forth interview for a single component or connection.
    Returns a confirmation dict or None if rejected.
    """
    # Connections have no 'name' — build a label from source/target IDs and protocols
    if element_type == "connection":
        protocols = ", ".join(element.get("protocols", ["unknown"]))
        element_label = (
            f"{element.get('source_component_id', '?')} -> "
            f"{element.get('target_component_id', '?')} ({protocols})"
        )
    else:
        element_label = element.get("name", element.get("id", "unknown"))

    console.rule(f"[bold]{element_type.title()}: {element_label}[/bold]")

    if element.get("typical"):
        console.print("[dim]Typically present in this product category.[/dim]")
    if element.get("required"):
        console.print("[yellow]Required — assessment incomplete without an answer.[/yellow]")

    # Fallback question in case Claude returns a null/empty question field
    _fallback_q = element.get("elicitation_questions", ["Please describe this element."])[0]

    max_turns = 6
    analyst_answer = None

    for turn in range(max_turns):
        result = ask_claude(session, archetype, element, element_type)

        # Guard: ensure all expected fields exist and are non-None
        question       = result.get("question") or _fallback_q
        status         = result.get("status")   or "NEEDS_FOLLOWUP"
        interpretation = result.get("interpretation") or ""

        # Show Claude's question
        console.print(Panel(str(question), title="Question", border_style="blue"))

        if status == "REJECTED":
            if interpretation:
                console.print(f"[dim]Interpretation: {interpretation}[/dim]")
            if Confirm.ask("Mark this element as NOT present?", default=True):
                return None
            # Analyst disagrees — continue
            analyst_answer = Prompt.ask("[green]Your answer[/green]")

        elif status == "CONFIRMED":
            if interpretation:
                console.print(f"[dim]Interpretation: {interpretation}[/dim]")
            if Confirm.ask("Confirm this element as present?", default=True):
                return result
            analyst_answer = Prompt.ask("[green]Correction / additional detail[/green]")

        else:  # NEEDS_FOLLOWUP
            analyst_answer = Prompt.ask("[green]Your answer[/green]")

        # Append exchange to history (use resolved question, never None)
        session.conversation_history.append({"role": "assistant", "content": question})
        session.conversation_history.append({"role": "user",      "content": analyst_answer or ""})

    console.print("[yellow]Max turns reached — recording as needs review.[/yellow]")
    return {"status": "NEEDS_REVIEW", "notes": "Max interview turns reached", "confirmed_properties": [], "actual_protocols": []}


# ── STRIDE letter to full Threat Dragon type name ────────────────────────────
_STRIDE_NAMES = {
    "S": "Spoofing",
    "T": "Tampering",
    "R": "Repudiation",
    "I": "Information disclosure",
    "D": "Denial of service",
    "E": "Elevation of privilege",
}

# ── archetype shape -> Threat Dragon cell type ────────────────────────────────
_TD_TYPE = {
    "process":         "tm.Process",
    "datastore":       "tm.Store",
    "external-entity": "tm.Actor",
    "actor":           "tm.Actor",
    "store":           "tm.Store",
}

# ── Threat Dragon JSON builder ────────────────────────────────────────────────

def _td_threat(h: dict) -> dict:
    """Convert a threat_hint dict to the exact Threat Dragon v2 threat object."""
    return {
        "status":      "Open",
        "severity":    h["severity"].capitalize(),
        "title":       h["title"],
        "type":        _STRIDE_NAMES.get(h["stride_category"], h["stride_category"]),
        "description": h["description"],
        "mitigation":  h["mitigation"],
    }

def _td_attrs(label: str, has_threats: bool, in_scope: bool = True) -> dict:
    """Build the attrs dict Threat Dragon uses for rendering."""
    threat_cls  = "hasOpenThreats"  if has_threats else "hasNoOpenThreats"
    scope_cls   = "isInScope"       if in_scope    else "isOutOfScope"
    return {
        ".element-shape": {"class": f"element-shape {threat_cls} {scope_cls}"},
        "text":           {"text": label},
        ".element-text":  {"class": f"element-text {threat_cls} {scope_cls}"},
    }

def _td_flow_attrs(has_threats: bool) -> dict:
    threat_cls = "hasOpenThreats" if has_threats else "hasNoOpenThreats"
    return {
        ".marker-target": {"class": f"marker-target {threat_cls} isInScope"},
        ".connection":    {"class": f"connection {threat_cls} isInScope"},
    }

def build_threat_dragon_model(session: SessionState, archetype: dict) -> dict:
    """
    Build a Threat Dragon v2-compatible model JSON from confirmed session elements.
    Matches the schema of the official OWASP demo-threat-model.json exactly.
    """
    cells = []
    x_pos, y_pos = 80, 80
    z = 1

    # Map template_id -> confirmed component id for connection wiring
    comp_map = {c.template_id: c.id for c in session.confirmed_components}

    # ── Components ──
    for comp in session.confirmed_components:
        tmpl   = next(c for c in archetype["component_templates"] if c["id"] == comp.template_id)
        label  = comp.actual_name or tmpl.get("name", comp.template_id)
        td_type = _TD_TYPE.get(tmpl.get("threat_dragon_shape", "process"), "tm.Process")

        threats = [
            _td_threat(h)
            for h in archetype.get("threat_hints", [])
            if h["component_type"] == tmpl["type"]
        ]
        has_threats = bool(threats)

        # Size: Store uses 160x80, Process uses 100x100, Actor uses 160x80
        if td_type == "tm.Process":
            size = {"width": 100, "height": 100}
        else:
            size = {"width": 160, "height": 80}

        cell = {
            "type":           td_type,
            "size":           size,
            "position":       {"x": x_pos, "y": y_pos},
            "angle":          0,
            "id":             comp.id,
            "z":              z,
            "threats":        threats,
            "hasOpenThreats": has_threats,
            "outOfScope":     False,
            "attrs":          _td_attrs(label, has_threats),
        }

        # Store-specific fields
        if td_type == "tm.Store":
            cell["storesCredentials"] = any(
                "credential" in p.lower() or "key" in p.lower()
                for p in tmpl.get("security_properties", [])
            )
            cell["isALog"] = "logging" in tmpl.get("name", "").lower()

        cells.append(cell)
        z += 1
        x_pos += 240
        if x_pos > 900:
            x_pos = 80
            y_pos += 160

    # ── Flows ──
    for conn in session.confirmed_connections:
        if conn.source_id not in comp_map.values() or conn.target_id not in comp_map.values():
            continue

        protocol_label = ", ".join(conn.actual_protocols) if conn.actual_protocols else "data flow"

        conn_threats = [
            _td_threat(h)
            for h in archetype.get("threat_hints", [])
            if any(p.lower() in h.get("connection_type", "").lower() for p in conn.actual_protocols)
        ]
        has_threats = bool(conn_threats)

        cell = {
            "type":   "tm.Flow",
            "size":   {"width": 10, "height": 10},
            "smooth": True,
            "source": {"id": conn.source_id},
            "target": {"id": conn.target_id},
            "vertices": [],
            "id":     conn.id,
            "labels": [
                {
                    "position": 0.5,
                    "attrs": {
                        "text": {
                            "text": protocol_label,
                            "font-weight": "400",
                            "font-size": "small",
                        }
                    },
                }
            ],
            "z":              z,
            "threats":        conn_threats,
            "hasOpenThreats": has_threats,
            "outOfScope":     False,
            "attrs":          _td_flow_attrs(has_threats),
        }
        cells.append(cell)
        z += 1

    return {
        "summary": {
            "title":       session.product_name,
            "owner":       session.assessor,
            "description": f"Generated by elicit.py on {session.assessment_date}. Archetype: {archetype['name']}.",
            "id":          0,
        },
        "detail": {
            "contributors": [{"name": session.assessor}],
            "diagrams": [
                {
                    "title":       "System overview",
                    "thumbnail":   "./public/content/images/thumbnail.stride.jpg",
                    "diagramType": "STRIDE",
                    "id":          0,
                    "diagramJson": {
                        "cells": cells,
                    },
                    "size": {
                        "height": max(600, y_pos + 200),
                        "width":  max(900, x_pos + 200),
                    },
                }
            ],
            "reviewer": "",
        },
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Cybersecurity readiness — product elicitation")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--archetype",  help="Archetype name (e.g. iot-gateway)")
    group.add_argument("--resume",     help="Path to an existing session JSON file")
    parser.add_argument("--product",   help="Product name (required with --archetype)")
    parser.add_argument("--assessor",  help="Assessor name (required with --archetype)", default="Unknown")
    args = parser.parse_args()

    # Load or init session
    if args.resume:
        session = load_session(args.resume)
        archetype = load_archetype(session.archetype_id.replace("-001", "").replace("iot-gateway", "iot-gateway"))
        console.print(f"[green]Resuming session {session.instance_id} for {session.product_name}[/green]")
    else:
        if not args.product:
            console.print("[red]--product is required when starting a new session.[/red]")
            sys.exit(1)
        archetype = load_archetype(args.archetype)
        session   = init_session(archetype, args.product, args.assessor)
        console.print(Panel(
            f"[bold]Product:[/bold] {session.product_name}\n"
            f"[bold]Archetype:[/bold] {archetype['name']}\n"
            f"[bold]Assessor:[/bold] {session.assessor}\n"
            f"[bold]Session ID:[/bold] {session.instance_id}",
            title="New assessment session",
            border_style="green"
        ))

    # ── Component interview loop ──
    remaining_components = [
        c for c in archetype["component_templates"]
        if c["id"] in session.pending_component_ids
    ]
    # Required first, then typical, then optional
    remaining_components.sort(key=lambda c: (not c["required"], not c["typical"]))

    for template in remaining_components:
        result = interview_element(session, archetype, template, "component")

        if result:
            confirmed = ConfirmedComponent(
                id=str(uuid.uuid4())[:8],
                template_id=template["id"],
                actual_name=template["name"],
                notes=result.get("notes", ""),
                confirmed_properties=result.get("confirmed_properties", []),
            )
            session.confirmed_components.append(confirmed)
            console.print(f"[green]✓ Confirmed: {template['name']}[/green]\n")
        else:
            console.print(f"[dim]✗ Rejected: {template['name']}[/dim]\n")

        session.pending_component_ids.remove(template["id"])
        save_session(session)

    # ── Connection interview loop ──
    remaining_connections = [
        c for c in archetype["connection_templates"]
        if c["id"] in session.pending_connection_ids
    ]

    confirmed_template_ids = {c.template_id for c in session.confirmed_components}

    for template in remaining_connections:
        # Skip connections where either endpoint was rejected
        if template["source_component_id"] not in confirmed_template_ids or \
           template["target_component_id"] not in confirmed_template_ids:
            session.pending_connection_ids.remove(template["id"])
            continue

        result = interview_element(session, archetype, template, "connection")

        if result:
            src_comp = next(c for c in session.confirmed_components if c.template_id == template["source_component_id"])
            tgt_comp = next(c for c in session.confirmed_components if c.template_id == template["target_component_id"])
            confirmed = ConfirmedConnection(
                id=str(uuid.uuid4())[:8],
                template_id=template["id"],
                source_id=src_comp.id,
                target_id=tgt_comp.id,
                actual_protocols=result.get("actual_protocols", template.get("protocols", [])),
                notes=result.get("notes", ""),
            )
            session.confirmed_connections.append(confirmed)
            console.print(f"[green]✓ Confirmed connection: {template['id']}[/green]\n")
        else:
            console.print(f"[dim]✗ Rejected connection: {template['id']}[/dim]\n")

        session.pending_connection_ids.remove(template["id"])
        save_session(session)

    # ── Emit Threat Dragon JSON ──
    session.complete = True
    save_session(session)

    td_model = build_threat_dragon_model(session, archetype)
    output_path = OUTPUT_DIR / f"{session.instance_id}-{session.product_name.replace(' ', '-').lower()}.td.json"
    output_path.write_text(json.dumps(td_model, indent=2), encoding="utf-8")

    console.print(Panel(
        f"[bold green]Assessment complete![/bold green]\n\n"
        f"Session saved: [cyan]sessions/{session.instance_id}.json[/cyan]\n"
        f"Threat Dragon model: [cyan]{output_path}[/cyan]\n\n"
        f"Components confirmed: {len(session.confirmed_components)}\n"
        f"Connections confirmed: {len(session.confirmed_connections)}\n"
        f"Pre-seeded threats: {sum(len(c.get('threats', [])) for c in td_model['detail']['diagrams'][0]['diagramJson']['cells'])}",
        title="Done",
        border_style="green"
    ))


if __name__ == "__main__":
    main()
