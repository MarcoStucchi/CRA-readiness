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
    return json.loads(path.read_text())


# ── Session persistence ───────────────────────────────────────────────────────

def save_session(session: SessionState) -> Path:
    path = SESSIONS_DIR / f"{session.instance_id}.json"
    path.write_text(session.model_dump_json(indent=2))
    return path

def load_session(path: str) -> SessionState:
    return SessionState.model_validate_json(Path(path).read_text())

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

def ask_claude(session: SessionState, archetype: dict, element: dict, element_type: str) -> dict:
    """Send one turn of the interview to Claude and return its structured response."""

    context = {
        "product": session.product_name,
        "archetype": archetype["name"],
        "element_type": element_type,
        "element_name": element["name"],
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

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=messages,
    )

    raw = response.content[0].text
    # Strip possible markdown fences
    clean = raw.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return json.loads(clean)


# ── Interview loop for one element ───────────────────────────────────────────

def interview_element(session: SessionState, archetype: dict, element: dict, element_type: str) -> Optional[dict]:
    """
    Run the back-and-forth interview for a single component or connection.
    Returns a confirmation dict or None if rejected.
    """
    console.rule(f"[bold]{element_type.title()}: {element['name']}[/bold]")

    if element.get("typical"):
        console.print("[dim]Typically present in this product category.[/dim]")
    if element.get("required"):
        console.print("[yellow]Required — assessment incomplete without an answer.[/yellow]")

    max_turns = 6
    analyst_answer = None

    for turn in range(max_turns):
        result = ask_claude(session, archetype, element, element_type)

        # Show Claude's question
        console.print(Panel(result["question"], title="Question", border_style="blue"))

        if result["status"] == "REJECTED":
            console.print(f"[dim]Interpretation: {result.get('interpretation', '')}[/dim]")
            if Confirm.ask("Mark this element as NOT present?", default=True):
                return None
            # Analyst disagrees — continue
            analyst_answer = Prompt.ask("[green]Your answer[/green]")

        elif result["status"] == "CONFIRMED":
            console.print(f"[dim]Interpretation: {result.get('interpretation', '')}[/dim]")
            if Confirm.ask("Confirm this element as present?", default=True):
                return result
            analyst_answer = Prompt.ask("[green]Correction / additional detail[/green]")

        else:  # NEEDS_FOLLOWUP
            analyst_answer = Prompt.ask("[green]Your answer[/green]")

        # Append exchange to history
        session.conversation_history.append({"role": "assistant", "content": result["question"]})
        session.conversation_history.append({"role": "user",      "content": analyst_answer})

    console.print("[yellow]Max turns reached — recording as needs review.[/yellow]")
    return {"status": "NEEDS_REVIEW", "notes": "Max interview turns reached", "confirmed_properties": [], "actual_protocols": []}


# ── Threat Dragon JSON builder ────────────────────────────────────────────────

def build_threat_dragon_model(session: SessionState, archetype: dict) -> dict:
    """
    Build a minimal Threat Dragon v2 model JSON from confirmed session elements.
    """
    cells = []
    x_pos, y_pos = 100, 100

    # Map template_id -> confirmed component id for connection wiring
    comp_map = {c.template_id: c.id for c in session.confirmed_components}

    # Components → Threat Dragon cells
    for comp in session.confirmed_components:
        tmpl = next(c for c in archetype["component_templates"] if c["id"] == comp.template_id)

        # Collect applicable threat hints
        threats = [
            {
                "id": str(uuid.uuid4()),
                "title": h["title"],
                "type": h["stride_category"],
                "status": "Open",
                "severity": h["severity"].capitalize(),
                "description": h["description"],
                "mitigation": h["mitigation"],
                "modelType": "STRIDE",
            }
            for h in archetype.get("threat_hints", [])
            if h["component_type"] == tmpl["type"]
        ]

        cells.append({
            "id": comp.id,
            "type": f"tm.{tmpl['threat_dragon_shape'].capitalize()}",
            "label": comp.actual_name or tmpl["name"],
            "data": {
                "name": comp.actual_name or tmpl["name"],
                "description": comp.notes,
                "threats": threats,
            },
            "position": {"x": x_pos, "y": y_pos},
            "size": {"width": 160, "height": 60},
        })
        x_pos += 220
        if x_pos > 800:
            x_pos = 100
            y_pos += 120

    # Connections → Threat Dragon flow cells
    for conn in session.confirmed_connections:
        if conn.source_id not in comp_map.values() or conn.target_id not in comp_map.values():
            continue  # skip if either endpoint was rejected

        conn_threats = [
            {
                "id": str(uuid.uuid4()),
                "title": h["title"],
                "type": h["stride_category"],
                "status": "Open",
                "severity": h["severity"].capitalize(),
                "description": h["description"],
                "mitigation": h["mitigation"],
                "modelType": "STRIDE",
            }
            for h in archetype.get("threat_hints", [])
            if any(p.lower() in h.get("connection_type", "").lower() for p in conn.actual_protocols)
        ]

        cells.append({
            "id": conn.id,
            "type": "tm.Flow",
            "label": ", ".join(conn.actual_protocols) or "data flow",
            "source": {"id": conn.source_id},
            "target": {"id": conn.target_id},
            "data": {
                "name": ", ".join(conn.actual_protocols) or "data flow",
                "description": conn.notes,
                "threats": conn_threats,
            },
        })

    return {
        "version": "2.3.0",
        "summary": {
            "title": session.product_name,
            "owner": session.assessor,
            "description": f"Generated by elicit.py on {session.assessment_date}",
            "id": session.instance_id,
        },
        "detail": {
            "contributors": [{"name": session.assessor}],
            "diagrams": [
                {
                    "id": 0,
                    "title": "System overview",
                    "diagramType": "STRIDE",
                    "thumbnail": "",
                    "cells": cells,
                }
            ],
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
    output_path.write_text(json.dumps(td_model, indent=2))

    console.print(Panel(
        f"[bold green]Assessment complete![/bold green]\n\n"
        f"Session saved: [cyan]sessions/{session.instance_id}.json[/cyan]\n"
        f"Threat Dragon model: [cyan]{output_path}[/cyan]\n\n"
        f"Components confirmed: {len(session.confirmed_components)}\n"
        f"Connections confirmed: {len(session.confirmed_connections)}\n"
        f"Pre-seeded threats: {sum(len(c['data']['threats']) for c in td_model['detail']['diagrams'][0]['cells'] if 'data' in c)}",
        title="Done",
        border_style="green"
    ))


if __name__ == "__main__":
    main()
