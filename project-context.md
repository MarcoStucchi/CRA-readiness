# Cybersecurity readiness assessment system — project context

**Owner**: Principal Engineer, Cybersecurity — UL  
**Started**: May 2026  
**Status**: Architecture design phase  
**Last updated**: 2026-05-18 (session 3)

---

## Project goal

Build a Claude-assisted system to assess the **cybersecurity readiness level of products** against EU Cyber Resilience Act (CRA) requirements, mapping them to the most applicable technical standards and generating a structured threat model. The system is intended for use at UL in product security evaluations.

---

## Knowledge base — file inventory

All files reside in:
`C:\Users\ITMASTU1\OneDrive - ABB\Documents\Standards\EU commission\CRA\AI knowledgebase\`

### CRA regulatory files (Regulation EU 2024/2847 — adopted 23 Oct 2024)

| File | Content | Role in the system |
|---|---|---|
| `CRA_Main_Body_Summary.md` | Full summary of the CRA main body: definitions, manufacturer obligations, reporting deadlines, conformity assessment framework, penalties, timeline | Path A — regulatory context; determines which Annex applies to the product |
| `CRA_Annex_1.md` | **Annex I** — Essential cybersecurity requirements. Part I: 13 security properties (secure by default, auth, confidentiality, integrity, data minimisation, availability, DoS resilience, attack surface, incident impact, logging, security updates, patch dissemination, data deletion). Part II: 8 vulnerability handling obligations (SBOM, CVD, testing, disclosure, update distribution, 10-year patch availability) | **Core Path A input** — the authoritative requirement set every product must be checked against |
| `CRA_Annex_2.md` | **Annex II** — Minimum user information and instructions (contact details, CVD policy pointer, product identification, support period end date, SBOM access point) | Path A — user-facing documentation checklist |
| `CRA_Annex_3.md` | **Annex III** — Important products (Class I and Class II). Class I: 24 categories (IACS, IIoT, smart meters, routers, OS, SIEM, VPN…). Class II: 14 categories (server OS, hypervisors, HSMs, PKI, industrial firewalls, secure elements…) | Path A — determines CRA risk classification of the product under assessment |
| `CRA_Annex_4.md` | **Annex IV** — Critical products (5 categories: hardware security boxes, smart meter gateways, high-trust smartcards, HSMs for national infrastructure, secure cryptoprocessors for critical infra) | Path A — determines if mandatory EU cybersecurity certification applies |
| `CRA_Annex_5.md` | **Annex V** — EU Declaration of Conformity template (9 mandatory fields including support period and notified body reference) | Path A — conformity documentation checklist |
| `CRA_Annex_6.md` | **Annex VI** — Simplified EU Declaration of Conformity (one-line declaration + URL to full Annex V text; physical affixing to product) | Path A — lightweight conformity documentation option |
| `CRA_Annex_7.md` | **Annex VII** — Technical documentation contents (8 elements: product description, design/development/production info including SBOM and CVD policy, cybersecurity risk assessment, support period rationale, harmonised standards list, test reports, DoC copy) | Path A — technical file completeness checklist |
| `CRA_Annex_8.md` | **Annex VIII** — Conformity assessment procedures. Module A (self-assessment, default products), Module B+C (EU-type examination + production control, Class I without harmonised standards / Class II), Module H (full quality assurance, Class II / Critical) | Path A — determines the conformity assessment route |

### Standards mapping and routing files

| File | Content | Role in the system |
|---|---|---|
| `cybersecurity_standards_evaluation_guide.md` | Product-to-standard routing guide across 7 sectors (consumer IoT, industrial/OT, energy, automotive, medical, critical components, organisational). Includes layered standards table and regulatory framework context. | **Path A routing input** — Claude uses this to select the applicable standard(s) for a product |
| `CRA_requirements_standards_mapping.md` | JRC & ENISA joint analysis (EUR 31892 EN, 2024). For each CRA Annex I requirement: coverage table across 15+ standards, gap analysis, lifecycle stages. Covers all 13 security property requirements and 8 vulnerability handling requirements. Key finding: no single standard covers all CRA requirements; ETSI EN 303 645 has broadest coverage for consumer IoT. | **Path A gap analysis input** — maps each CRA clause to the best-covering standard clause(s) and identifies residual gaps |
| `ETSI_EN_303_645_V3_1_3.md` | ETSI EN 303 645 v3.1.3 — Consumer IoT cybersecurity standard (13 provisions + 16 data protection provisions). Primary harmonised standard under CRA for default-category connected products. | **Path A evaluation criteria** — detailed requirement set for consumer IoT products |

### Key regulatory facts for Path A logic

- **Full applicability date**: 11 December 2027 (products placed on market before this date only subject to CRA if substantially modified after that date)
- **Reporting obligations start**: 11 September 2026 (all products on market, including pre-2027 ones)
- **Minimum support period**: 5 years (unless expected lifetime is shorter)
- **Patch availability**: security updates must remain available for minimum 10 years from issue date or remainder of support period, whichever is longer
- **Medical devices (MDR/IVDR) and automotive (type approval)**: explicitly excluded from CRA scope
- **Penalties**: up to 2.5% of global annual turnover (or €15M) for Annex I violations

### Missing standard files (referenced in routing guide, not yet in KB)

| File referenced | Standard | Priority |
|---|---|---|
| `iec_62443.md` | IEC 62443-4-1 / 4-2 / 3-3 — Industrial/OT | High — needed for IACS, IIoT, gateway assessments |
| `iec_62351.md` | IEC 62351 — Energy/power systems protocols | Medium |
| `iso_sae_21434.md` | ISO/SAE 21434 — Automotive | Low (out of CRA scope) |
| `unece_r155_r156.md` | UNECE R155/R156 — Automotive CSMS/SUMS | Low (out of CRA scope) |
| `iec_81001_5_1.md` | IEC 81001-5-1 — Medical device | Low (out of CRA scope) |
| `common_criteria_iso_15408.md` | Common Criteria / ISO 15408 — Critical components | Medium — needed for Annex IV products |
| `iso_iec_27001.md` | ISO/IEC 27001 — Organisational ISMS | Medium |

---

## System architecture — three paths

The system is organised into three parallel paths that converge into a final readiness report.

```
Product description
      |
  ----+----
  |       |
Path A  Path C
  |       |
  |    Path B
  |       |
  +---+---+
      |
 Readiness report
```

### Path A — Compliance mapping

**Purpose**: Map CRA Annex I requirements to the specific technical standard that applies to the product under assessment, then identify gaps.

**Inputs**:
- Knowledge base: CRA Annex I requirements (as structured document/KB)
- Markdown file: product category → applicable standard mapping

**Process**:
1. Claude identifies the applicable standard from the product description (e.g. IEC 62443, EN 18031, ETSI EN 303 645)
2. Claude cross-walks CRA Annex I clauses to specific standard clauses
3. Gap analysis: which requirements are not demonstrably met

**Output**: Structured gap table with CRA clause ↔ standard clause references, compliance status, and remediation notes.

---

### Path B — Threat modelling

**Purpose**: Generate a structured STRIDE threat model using OWASP Threat Dragon.

**Tool chosen**: [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)  
**Why**: Open source, machine-readable JSON format, supports DFD with trust boundaries, STRIDE per component and flow.

**Process**:
1. Receive confirmed product model JSON from Path C
2. Map components and connections to Threat Dragon cell types
3. Run STRIDE analysis per component and per data flow
4. Pre-populate threat entries from `THREAT_HINT` table (see schema)

**Output**: Threat Dragon `.json` file with populated DFD, trust boundaries, and STRIDE threat entries.

---

### Path C — Guided product elicitation (core innovation)

**Purpose**: Build the Threat Dragon-compatible product model through a structured Claude interview, guided by a database of product archetypes.

**Concept**: Claude acts as an interview engine. It draws on a reference database of known product archetypes (IoT gateway, ICS controller, medical device, consumer electronics, etc.), each containing a canonical checklist of components, interfaces, protocols, and data flows. Claude questions the analyst about the product under assessment, confirming or rejecting each candidate element. The confirmed set is emitted as a Threat Dragon JSON file.

**Key design decisions**:
- Components and connections are **separate first-class entities** (not nested arrays) — mirrors Threat Dragon's internal model
- Each archetype has `required` and `typical` flags per component/connection, shaping how Claude phrases questions
- The confirmed product model also informs Path A standard selection (e.g. Modbus present → IEC 62443-3-3 becomes relevant)
- `THREAT_HINT` records are indexed by component/connection type, reusable across archetypes

**Implementation decisions (resolved)**:
- Interface: **Claude Code CLI script** (`elicit.py`) — chosen over browser artifact for session persistence, pipeline integration, and git versionability
- Language: **Python** (over JavaScript) — more natural for data processing pipelines
- Libraries: `anthropic` SDK, `pydantic` for schema validation, `rich` for terminal UI
- Archetype storage: **flat JSON files** per archetype, one per product category — simple, versionable, no DB required at this stage
- Session state: auto-saved to `sessions/{id}.json` after each element — supports resume after interruption

**Output**: `PRODUCT_INSTANCE` record + Threat Dragon `.json` file ready for Path B.

---

## Archetype database schema

### Entities

#### `ARCHETYPE`
Template for a product category.

| Field | Type | Notes |
|---|---|---|
| `id` | string PK | |
| `name` | string | e.g. "Industrial IoT gateway" |
| `category` | string | e.g. "ICS", "IoT", "medtech", "consumer" |
| `cra_class` | string | CRA risk classification |
| `applicable_standards` | string[] | Variable-length array |
| `description` | string | |

#### `COMPONENT_TEMPLATE`
Candidate component within an archetype. Variable-length per archetype.

| Field | Type | Notes |
|---|---|---|
| `id` | string PK | |
| `archetype_id` | string FK | |
| `name` | string | e.g. "Firmware update agent" |
| `type` | string | e.g. "process", "datastore", "external entity" |
| `layer` | string | e.g. "hardware", "firmware", "OS", "application", "cloud" |
| `required` | boolean | Assessment incomplete without answer |
| `typical` | boolean | Present in most devices of this category |
| `security_properties` | string[] | e.g. ["authentication", "encryption", "integrity"] |
| `elicitation_questions` | string[] | Variable-length — Claude's interview questions |
| `threat_dragon_shape` | string | Threat Dragon cell type |

#### `CONNECTION_TEMPLATE`
Candidate data flow between two component templates. Variable-length per archetype.

| Field | Type | Notes |
|---|---|---|
| `id` | string PK | |
| `archetype_id` | string FK | |
| `source_component_id` | string FK | |
| `target_component_id` | string FK | |
| `protocols` | string[] | Variable-length — e.g. ["MQTT", "TLS 1.3"] |
| `direction` | string | "unidirectional" / "bidirectional" |
| `crosses_trust_boundary` | boolean | |
| `trust_boundary_name` | string | e.g. "OT/IT boundary" |
| `typical` | boolean | |
| `required` | boolean | |
| `elicitation_questions` | string[] | Variable-length |

#### `THREAT_HINT`
Pre-seeded STRIDE threat suggestions, indexed by component/connection type — reusable across archetypes.

| Field | Type | Notes |
|---|---|---|
| `id` | string PK | |
| `component_type` | string | Matches `COMPONENT_TEMPLATE.type` |
| `connection_type` | string | e.g. "Modbus", "MQTT over TLS" |
| `stride_category` | string | S / T / R / I / D / E |
| `title` | string | |
| `description` | string | |
| `cra_clause` | string | Cross-reference to CRA Annex I |
| `mitigation` | string | |
| `severity` | string | "high" / "medium" / "low" |

#### `PRODUCT_INSTANCE`
Actual assessment record for a specific product.

| Field | Type | Notes |
|---|---|---|
| `id` | string PK | |
| `archetype_id` | string FK | |
| `product_name` | string | |
| `manufacturer` | string | |
| `assessment_date` | date | |
| `assessor` | string | |
| `threat_dragon_file` | string | Path or blob reference |

#### `CONFIRMED_COMPONENT` / `CONFIRMED_CONNECTION`
Result of the elicitation interview — confirmed elements of the actual product, referencing their archetype templates by FK. This enables gap analysis: unconfirmed `required` templates = missing security elements.

---

## Deliverables produced so far

### `elicit.py` — Path C CLI elicitation engine
Python script implementing the full interview loop. Structure:
- `SessionState` (Pydantic) — live session model, auto-saved to `sessions/{id}.json`
- `load_archetype()` — loads archetype JSON from `archetypes/` directory
- `ask_claude()` — single interview turn via Anthropic API; returns structured JSON (CONFIRMED / REJECTED / NEEDS_FOLLOWUP)
- `interview_element()` — back-and-forth loop for one component or connection, max 6 turns
- `build_threat_dragon_model()` — walks confirmed elements and emits Threat Dragon v2 JSON with pre-seeded STRIDE threats

Usage:
```bash
pip install anthropic rich pydantic
export ANTHROPIC_API_KEY=your_key_here

# New assessment
python elicit.py --archetype iot-gateway --product "Acme GW-200" --assessor "J. Smith"

# Resume interrupted session
python elicit.py --resume sessions/abc12345.json
```

### `archetypes/iot-gateway.json` — first archetype
Industrial IoT gateway archetype with:
- 7 component templates (cloud agent, firmware update, local config UI, field device interface, data store, debug/JTAG, network mgmt)
- 4 connection templates with trust boundary flags
- 6 pre-seeded STRIDE threat hints with CRA Annex I clause references

---

## API access and pricing

The Anthropic API is a **separate product** from claude.ai — requires its own account at `console.anthropic.com` and its own API key. Billing is usage-based (tokens), independent of any claude.ai subscription.

Current rates (per million tokens, input / output):

| Model | Input | Output | Best for |
|---|---|---|---|
| Claude Haiku 4.5 | $1.00 | $5.00 | High-volume, simple tasks |
| Claude Sonnet 4.6 | $3.00 | $15.00 | Balanced — used in `elicit.py` |
| Claude Opus 4.7 | $5.00 | $25.00 | Complex reasoning |

Cost reducers: **50% off** with Batch API; **90% off** cached input with prompt caching (relevant for elicitation since system prompt + archetype JSON repeat every turn).

Estimated cost per full product assessment: **a few cents** (20–30 API calls × ~5K tokens each at Sonnet rates).

---

## Key design principles

- **Variable-length arrays** (`string[]`) are first-class in the schema — used for protocols, questions, standards, properties. In storage: JSONB (Postgres) or JSON-serialised TEXT (SQLite).
- **`typical` vs `required`** flags shape interview phrasing. `required` = must ask, assessment incomplete without answer. `typical` = Claude assumes presence and asks "does your device have X?" rather than open question.
- **Template → instance traceability**: every confirmed element references its template FK, enabling gap analysis and audit trail.
- **`THREAT_HINT` reusability**: threat hints are keyed on component/connection *type*, not specific template IDs, so they apply across archetypes automatically.

---

## Open questions / next decisions

- [x] **Elicitation interface**: ~~browser artifact vs Claude Code~~ → **resolved: Claude Code Python CLI**
- [x] **Archetype DB storage**: ~~SQLite vs Postgres~~ → **resolved: flat JSON files for now**
- [x] **Draft first archetype**: → **resolved: `archetypes/iot-gateway.json` delivered**
- [x] **Threat Dragon JSON generation**: → **resolved: implemented in `build_threat_dragon_model()` in `elicit.py`**
- [x] **Standard KB format**: → **resolved: markdown files per document, stored in OneDrive folder alongside project files**
- [ ] **Archetype manifest**: add a `manifest.json` listing all available archetypes with display names
- [ ] **Report format**: what does the final readiness report look like? Who is the audience — internal UL assessors, product manufacturers, regulators?
- [ ] **Standard KB format**: how are CRA Annex I and the applicable standards stored for Claude to reason over? Chunked markdown? Structured JSON?
- [ ] **Path A prototype**: CRA KB + standard markdown → gap table (not yet started)
- [ ] **Cross-path synthesis**: how do Path A gap table and Path B STRIDE output merge into the final readiness report?
- [ ] **Additional archetypes**: ICS controller, medical device, consumer IoT

---

## Proposed next steps

1. Add missing standard files to KB — priority: `iec_62443.md` (needed for IACS/IIoT assessments, most common at UL), then `common_criteria_iso_15408.md` (Annex IV critical products)
2. Add `archetypes/manifest.json` to list available archetypes; fix archetype name resolution in `elicit.py`
3. Run `elicit.py` against a real product to validate the interview loop and Threat Dragon JSON output
4. Add prompt caching to `elicit.py` (system prompt + archetype JSON repeated every turn — 90% cost saving)
5. Build Path A prototype: load CRA_Annex_1.md + routing guide + CRA_requirements_standards_mapping.md → Claude identifies applicable standard(s) and produces gap table
6. Design the cross-path synthesis layer: STRIDE threats (Path B) + compliance gaps (Path A) → readiness report
7. Draft additional archetypes: ICS controller, consumer IoT device

---

## Session log

| Date | Topics covered |
|---|---|
| 2026-05-17 | Initial architecture design; three-path system; OWASP Threat Dragon selection; archetype DB schema design with ERD; variable-length array strategy |
| 2026-05-18 (s2) | Decided on Claude Code Python CLI for elicitation interface; built `elicit.py` (full interview loop, session persistence, Threat Dragon JSON builder); built `archetypes/iot-gateway.json` (first archetype — 7 components, 4 connections, 6 STRIDE threat hints with CRA clause refs); clarified API access and pricing (Sonnet 4.6 at $3/$15 per MTok; ~cents per assessment) |
| 2026-05-18 (s3) | Integrated knowledge base: 12 files uploaded (CRA Annex I–VIII, CRA main body summary, standards routing guide, JRC/ENISA requirements-to-standards mapping, ETSI EN 303 645 v3.1.3); full KB inventory documented with role of each file in Path A; identified 7 missing standard files still to be added; KB now covers full CRA Annex I requirement set with cross-standard gap analysis |

---

## How to resume context with Claude

Paste this document at the start of a new Claude conversation with the following prompt:

> "This is the project context document for a cybersecurity readiness assessment system I am building at UL. Please read it carefully and continue from where we left off. The open questions and next steps are at the bottom."

---

*Generated with Claude Sonnet 4.6 — update this document at the end of each working session.*
