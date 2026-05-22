# Cybersecurity readiness assessment system — project context

**Owner**: Principal Engineer, Cybersecurity — UL  
**Started**: May 2026  
**Status**: Architecture design phase  
**Last updated**: 2026-05-22 (session 9 — final)  
**Status**: POC complete — EN 18031 integrated — ready for Path A prototype  
**Filename**: `project-context.md` (repo root)

---

## Project goal

Build a Claude-assisted system to assess the **cybersecurity readiness level of products** against EU Cyber Resilience Act (CRA) requirements, mapping them to the most applicable technical standards and generating a structured threat model. The system is intended for use at UL in product security evaluations.

---

## Knowledge base — file inventory

All files reside in:
`knowledgebase/` (repo root) — synced from `C:\Users\ITMASTU1\OneDrive - ABB\Documents\Standards\EU commission\CRA\AI knowledgebase\`

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

> ⚠️ **Important — ENISA mapping version note**: `CRA_requirements_standards_mapping.md` is based on the
> draft CRA (COM(2022) 454), not the final Reg. EU 2024/2847. The clause structure differs: the draft had
> Req 1, Req 2, and 3a–3k; the final text has (1) and (2)(a)–(2)(m). Clauses (l) and (m) are entirely
> absent from the ENISA mapping. See `CRA_mapping_reconciliation.md` for the full translation table
> and gap list before using this file in Path A.

| File | Content | Role in the system |
|---|---|---|
| `cybersecurity_standards_evaluation_guide.md` | Product-to-standard routing guide across 7 sectors (consumer IoT, industrial/OT, energy, automotive, medical, critical components, organisational). Includes layered standards table and regulatory framework context. | **Path A routing input** — Claude uses this to select the applicable standard(s) for a product |
| `CRA_requirements_standards_mapping.md` | JRC & ENISA joint analysis (EUR 31892 EN, 2024). Based on **draft CRA COM(2022) 454** — see reconciliation note above. Coverage table across 15+ standards, gap analysis, lifecycle stages. Key finding: no single standard covers all CRA requirements; ETSI EN 303 645 has broadest coverage for consumer IoT. | **Path A gap analysis input** — use only in conjunction with `CRA_mapping_reconciliation.md` |
| `CRA_mapping_reconciliation.md` | Reconciliation table mapping every ENISA draft clause identifier to the corresponding final-text clause. Documents 2 missing clauses (❌), 5 partial mappings (⚠️), and 7 manual gap items with suggested EN 303 645 interim mappings. Produced 2026-05-20. | **Path A correction layer** — mandatory companion to `CRA_requirements_standards_mapping.md`; ensures gap analysis references final CRA text |
| `ETSI_EN_303_645_V3_1_3.md` | ETSI EN 303 645 v3.1.3 — Consumer IoT cybersecurity standard (13 provisions + 16 data protection provisions). Primary harmonised standard under CRA for default-category connected products. | **Path A evaluation criteria** — detailed requirement set for consumer IoT products |
| `en_18031.md` | EN 18031-1/2/3:2024 — Common security requirements for radio equipment. Mandatory under RED from 1 August 2025. Three parts: -1 (internet-connected), -2 (personal data processing), -3 (monetary value). Includes requirement clause tables, mapping to EN 303 645, conformity assessment routes, and product applicability matrix. | **Path A evaluation criteria** — mandatory for all wireless consumer IoT; complements EN 303 645; required for CE marking under RED |

### Key regulatory facts for Path A logic

- **Full applicability date**: 11 December 2027 (products placed on market before this date only subject to CRA if substantially modified after that date)
- **Reporting obligations start**: 11 September 2026 (all products on market, including pre-2027 ones)
- **Minimum support period**: 5 years (unless expected lifetime is shorter)
- **Patch availability**: security updates must remain available for minimum 10 years from issue date or remainder of support period, whichever is longer
- **Medical devices (MDR/IVDR) and automotive (type approval)**: explicitly excluded from CRA scope
- **EN 18031-1/2/3**: mandatory from 1 August 2025 under RED for all internet-connected radio equipment — applies NOW, before CRA full applicability (Dec 2027); compliance work directly supports future CRA conformity
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
1. Claude identifies the applicable standard(s) from the product description using `cybersecurity_standards_evaluation_guide.md`
2. For consumer wireless IoT products **both** EN 303 645 and EN 18031 apply — they come from different regulatory instruments (CRA and RED respectively) and are not interchangeable:
   - **EN 18031** is legally mandatory under RED from 1 August 2025 (CE marking requirement)
   - **EN 303 645** is the primary CRA harmonised standard candidate (full CRA applicability: Dec 2027)
   - Substantial overlap exists but EN 18031 is more prescriptive; EN 303 645 compliance does NOT automatically imply EN 18031 compliance
3. Claude cross-walks each CRA Annex I clause to coverage in EN 303 645 AND EN 18031, using:
   - `CRA_requirements_standards_mapping.md` (ENISA analysis — draft-based, use with `CRA_mapping_reconciliation.md`)
   - `ETSI_EN_303_645_V3_1_3.md` (EN 303 645 provisions)
   - `en_18031.md` (EN 18031 clause table + Annex C mapping to EN 303 645)
4. Gap analysis structure per CRA clause:
   ```
   CRA Annex I clause → EN 303 645 coverage → EN 18031-1 coverage → EN 18031-2 coverage (if personal data) → Residual gap
   ```
5. Residual gaps after both standards are largely procedural (CVD policy, SBOM in EUVD, 10-year patch availability) — no technical standard covers these

**Output**: Structured gap table with CRA clause ↔ EN 303 645 clause ↔ EN 18031 clause, compliance status per standard, and remediation notes.

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

### `archetypes/consumer-thermostat.json` — POC archetype
Connected consumer thermostat archetype (EN 303 645 scope, CRA class: default) with:
- 13 component templates (cloud backend, mobile app, local display, Wi-Fi, OTA firmware agent, secure credential store, local control logic, HVAC relay, environmental sensors, debug interfaces, local data store, BLE, telemetry service)
- 8 connection templates covering all major data flows with trust boundary flags
- 12 pre-seeded STRIDE threat hints, each cross-referenced to both EN 303 645 provision AND CRA Annex I clause
- Two new archetype fields vs iot-gateway: `en303645_provisions[]` per component and `en303645_provision` per threat hint

### `elicit.py` — bug fixes applied during POC run
The following issues were found and fixed during the first end-to-end POC run:

| Issue | Fix |
|---|---|
| `claude-sonnet-4-20250514` deprecation warning | Updated model to `claude-sonnet-4-6` |
| `JSONDecodeError` when Claude returns non-JSON | Added `_extract_json()` with brace-matching + 3-attempt retry loop with corrective prompt |
| `NotRenderableError: Unable to render None` | Added null guards on all `result` fields in `interview_element()` |
| `KeyError: 'name'` on connection templates | Connection templates have no `name` field — built label from source/target IDs and protocols |
| `UnicodeEncodeError` on Windows (cp1252) | All file read/write operations now use `encoding="utf-8"` explicitly; Unicode arrows replaced with ASCII `->` |
| `SessionState` loads empty/corrupted file | `save_session()` now writes atomically via `.tmp` → rename; `load_session()` validates before parsing |
| `KeyError: 'cells'` in summary panel | Fixed path to `diagramJson.cells` in threat count expression |
| Threat Dragon schema validation warning | Completely rewrote `build_threat_dragon_model()` to match exact v2 schema: `diagramJson.cells`, full STRIDE names, `attrs` labels, `hasOpenThreats`, `smooth`, `labels[]`, `vertices[]` |

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

## Repository structure (`cra-readiness-poc/`)

```
cra-readiness-poc/
├── archetypes/
│   ├── manifest.json              ← lists available archetypes (to build)
│   ├── iot-gateway.json           ← ✓ done (7 components, 4 connections, 6 threat hints)
│   └── consumer-thermostat.json   ← ✓ done (13 components, 8 connections, 12 threat hints)
├── knowledgebase/
│   ├── CRA_Main_Body_Summary.md
│   ├── CRA_Annex_1.md … CRA_Annex_8.md
│   ├── cybersecurity_standards_evaluation_guide.md
│   ├── CRA_requirements_standards_mapping.md
│   ├── ETSI_EN_303_645_V3_1_3.md
│   ├── standards/                 ← future: iec_62443.md, common_criteria.md…
│   └── README.md
├── sessions/                      ← gitignored — live elicitation state per run
├── output/                        ← gitignored — Threat Dragon JSON + gap tables
├── elicit.py                      ← ✓ done — Path C elicitation engine
├── assess_path_a.py               ← future — Path A gap analysis
├── requirements.txt
├── .env.example                   ← ANTHROPIC_API_KEY placeholder
├── .gitignore                     ← excludes: .env, sessions/, output/, __pycache__/
└── project-context.md             ← this file
```

---

## Open questions / next decisions

- [x] **Elicitation interface** → Claude Code Python CLI
- [x] **Archetype DB storage** → flat JSON files
- [x] **First archetype** → `iot-gateway.json` delivered
- [x] **Threat Dragon JSON generation** → implemented in `elicit.py`
- [x] **Standard KB format** → markdown files in `knowledgebase/`
- [x] **Project folder structure** → agreed (see repo structure above)
- [x] **POC product** → connected thermostat (consumer IoT, EN 303 645 + EN 18031)
- [x] **consumer-thermostat.json** → delivered (13 components, 8 connections, 12 threat hints)
- [x] **POC elicitation run** → completed end-to-end; Threat Dragon JSON generated and validated
- [x] **Threat Dragon v2 schema** → `build_threat_dragon_model()` rewritten to exact spec
- [x] **EN 18031 integration** → `en_18031.md` produced from PDFs; routing guide updated; thermostat archetype updated; dual-standard Path A structure defined
- [x] **Dual-standard Path A structure** → EN 303 645 + EN 18031 both apply to consumer wireless IoT under different regulatory instruments; gap table must cover both
- [ ] **Archetype manifest** — `archetypes/manifest.json` not yet created
- [ ] **Prompt caching** — system prompt + archetype JSON repeat every turn; 90% cost saving available
- [ ] **Path A prototype** — `assess_path_a.py` not yet started — see next steps for detailed spec
- [ ] **Cross-path synthesis** — how STRIDE output + gap table merge into report
- [ ] **Additional archetypes** — consumer IoT variants, future ICS
- [ ] **EN 18031 threat hints** — `consumer-thermostat.json` threat hints reference EN 303 645 provisions; EN 18031 clause IDs (e.g. AUM-5, GEC-2) not yet added as cross-references

---

## Proposed next steps

1. **Add `archetypes/manifest.json`** — list of available archetypes with display names; fix name resolution in `elicit.py`
2. **Add prompt caching to `elicit.py`** — system prompt + archetype JSON are repeated every API call; caching saves ~90% on input tokens per session
3. **Build `assess_path_a.py`** — Path A prototype for consumer thermostat:
   - Inputs: product description + session JSON (from elicit.py) + KB files
   - Step 1: route to applicable standards (EN 303 645 + EN 18031-1 + EN 18031-2) using routing guide
   - Step 2: for each CRA Annex I clause, query Claude with the relevant KB files and produce coverage assessment per standard
   - Step 3: use `CRA_mapping_reconciliation.md` to correct ENISA draft-based coverage findings to final-text clause IDs
   - Step 4: identify residual gaps (especially clauses (l), (m), EUVD registration, 10-year patch availability)
   - Output: markdown gap table — CRA clause | EN 303 645 | EN 18031-1 | EN 18031-2 | gap | remediation
4. **Add EN 18031 clause IDs to threat hints** in `consumer-thermostat.json` — each `threat_hint` currently has `en303645_provision`; add `en18031_clause` field (e.g. `"AUM-5"`, `"GEC-2"`) for dual-standard cross-referencing
5. **Run second clean POC** — fresh elicitation + Path A gap table for the thermostat → validate both outputs together
6. **Design cross-path synthesis** — STRIDE threats (Path B) + compliance gaps (Path A) → readiness report

---

## TODO — deferred items

These are confirmed future work items, parked deliberately and not yet scheduled.

---

### TODO-1: Trust boundaries in Threat Dragon output

**Status**: Data exists, rendering not implemented  
**Priority**: High — trust boundaries are a core DFD concept; their absence makes the Threat Dragon output incomplete for a real assessment

**Current state**: The `crosses_trust_boundary` and `trust_boundary_name` fields are correctly populated in `connection_templates` across all archetypes (e.g. `"Home network / Internet boundary"`, `"Physical proximity boundary"`). However `build_threat_dragon_model()` in `elicit.py` ignores these fields entirely — no `tm.Boundary` cells are emitted in the output `.td.json`.

**What needs to be built**:
- Change the layout algorithm in `build_threat_dragon_model()` to be boundary-aware:
  1. Collect all unique `trust_boundary_name` values from confirmed connections
  2. Assign each confirmed component to a zone (external entities = outside, processes/datastores = inside, cloud entities = far outside)
  3. Place component zones in horizontal bands with gaps between them
  4. Emit a `tm.Boundary` cell (type `"tm.Boundary"`, source/target as x/y coordinates) as a horizontal line in each gap
- `tm.Boundary` is a coordinate-based line, not connected to component IDs — placement depends on the layout algorithm knowing where components landed

**Impact**: Without trust boundaries, the Threat Dragon DFD does not meet the standard representation expected in a formal threat model review.

---

### TODO-2: Architecture evolution — Phase 2 and Phase 3

**Status**: Planned, not yet designed in detail  
**Priority**: Medium — relevant when more than one assessor uses the system or when the archetype registry grows beyond a few files

#### Context and motivation

The current Phase 1 architecture couples three concerns in a single script (`elicit.py`): archetype authoring, assessment execution, and output generation. This works for a single expert user but does not scale. Two key insights from the POC:

1. **Archetypes are synthesised, not validated** — the current `consumer-thermostat.json` and `iot-gateway.json` were generated by Claude from general knowledge, not derived from real UL assessments or validated threat libraries. An experienced professional must review and adjust them. There is currently no tooling to support that review at human level (no editor, no diff tool, no validation schema enforcement).

2. **Knowledgebase is the premium asset** — the CRA and standards markdown files are authoritative and will grow over time. The archetype registry is currently the weakest link but has the highest potential for improvement through real assessment experience.

#### Phase 2 — separated knowledge system / assessment tool

**Goal**: Decouple archetype authoring (expert work) from assessment execution (analyst work).

**New components to build**:
- `archetype-builder.py` — Claude-powered guided tool for creating and editing archetypes in plain language; validates against schema before writing; maintains a changelog per archetype file
- `registry/` folder replacing flat `archetypes/` — adds `manifest.json` with versioning (semver per archetype), so every session record references the exact archetype version used
- `archetype-validator.py` — schema validation script to run in CI on every registry change; catches missing required fields, invalid `threat_dragon_shape` values, broken component ID references in connections
- Archetype update workflow: experienced professional edits archetype → validator runs → changelog entry added → version bumped → existing sessions remain pinned to old version

**Archetype ownership principle**: archetypes are maintained by cybersecurity experts (UL engineers). Analysts run assessments against published archetype versions. The two roles are separated.

#### Phase 3 — multi-product / multi-assessor platform

**Goal**: Turn the system into a shared UL asset enabling longitudinal compliance tracking across a product portfolio.

**New components to build**:
- `product_database/` — persistent store of completed assessments (session JSON + Threat Dragon output + gap table), indexed by product, archetype version, and assessment date
- `delta_report.py` — compares two assessments of the same product across time: what changed in the product model, what changed in the applicable standard, what the new gap picture looks like
- `knowledgebase API` — versioned access to KB files so assessments can reference the CRA/standard version in force at assessment date (CRA implementing acts evolve through 2025-2027)
- Web UI or structured CLI — multi-assessor workflow, session handoff, review and sign-off

**Key capability unlocked**: CRA compliance evolution tracked across product versions and standard updates. A product assessed today against EN 303 645 v3.1.3 and CRA Annex I (2024) can be re-assessed in 2026 when implementing acts are finalised, with a diff showing exactly what changed and what new gaps appeared.

**Archetype round-trip (deferred)**: Post-assessment, an expert opens the `.td.json` in Threat Dragon, corrects the diagram visually, and a reverse-mapping script reads those corrections back into the archetype. This closes the loop between real assessment experience and the registry — parked until Phase 2 archetype tooling is stable.

---

---

## Session log

| Date | Topics covered |
|---|---|
| 2026-05-17 | Initial architecture design; three-path system; OWASP Threat Dragon selection; archetype DB schema design with ERD; variable-length array strategy |
| 2026-05-18 (s2) | Decided on Claude Code Python CLI for elicitation interface; built `elicit.py` (full interview loop, session persistence, Threat Dragon JSON builder); built `archetypes/iot-gateway.json` (first archetype — 7 components, 4 connections, 6 STRIDE threat hints with CRA clause refs); clarified API access and pricing (Sonnet 4.6 at $3/$15 per MTok; ~cents per assessment) |
| 2026-05-18 (s3) | Integrated knowledge base: 12 files uploaded (CRA Annex I–VIII, CRA main body summary, standards routing guide, JRC/ENISA requirements-to-standards mapping, ETSI EN 303 645 v3.1.3); full KB inventory documented with role of each file in Path A; identified 7 missing standard files still to be added; KB now covers full CRA Annex I requirement set with cross-standard gap analysis |
| 2026-05-18 (s4) | Agreed repo folder structure (`cra-readiness-poc/`); renamed `cybersec_readiness_project.md` → `project-context.md` at repo root; decided POC product = connected thermostat (consumer IoT, EN 303 645); next step = `consumer-thermostat.json` archetype |
| 2026-05-19 (s5) | Built `consumer-thermostat.json` (13 components, 8 connections, 12 STRIDE threat hints with dual EN 303 645 + CRA Annex I references); ran first end-to-end POC elicitation; fixed 8 bugs in `elicit.py` (model deprecation, JSON parsing, null guards, KeyError on connection name, Windows Unicode encoding, atomic session save, Threat Dragon v2 schema); POC Threat Dragon output successfully generated and loaded in Threat Dragon; elicit.py now stable |
| 2026-05-20 (s6) | Discussed architecture separation: knowledge system vs assessment tool; clarified that archetypes are Claude-synthesised (not validated) while knowledgebase is authoritative; discussed trust boundary gap in Threat Dragon output; planned Phase 2 (separated knowledge/assessment) and Phase 3 (multi-product platform) evolution; added TODO section to project context; archetype human-editing and Threat Dragon round-trip deferred to experienced professional review |
| 2026-05-20 (s7) | Identified structural discrepancy between ENISA mapping (based on draft COM(2022) 454) and final CRA text (Reg. EU 2024/2847): Req1+Req2 merged into (1), 3a-3k became (2)(a)-(2)(k), two new clauses (l) and (m) added in final text; produced `CRA_mapping_reconciliation.md` with full clause translation table, 2 missing clauses (❌), 5 partial mappings (⚠️), 7 manual gap items with EN 303 645 interim mappings; file copied to `knowledgebase/` as `CRA_mapping_reconciliation.md` |
| 2026-05-20 (s8) | Identified EN 18031 (not EN 10381) as mandatory RED standard for consumer wireless IoT from 1 Aug 2025; read STN EN 18031-1/2/3:2024 PDFs; produced `en_18031.md` KB file covering all three parts with clause tables, EN 303 645 mapping, conformity assessment routes, and product applicability matrix; updated `cybersecurity_standards_evaluation_guide.md` with EN 18031 in Consumer IoT section and layered standards table; updated `consumer-thermostat.json` applicable_standards to include EN 18031-1 and -2 |
| 2026-05-22 (s9) | Clarified dual-standard relationship: EN 303 645 (CRA candidate harmonised standard) and EN 18031 (RED mandatory from Aug 2025) both apply to consumer wireless IoT but under different regulatory instruments; EN 303 645 compliance does not imply EN 18031 compliance; Path A gap table must cover both standards per CRA clause; defined detailed spec for `assess_path_a.py`; added EN 18031 clause IDs to thermostat threat hints as next step; session ended cleanly — ready for new chat |

---

## How to resume context with Claude

**Session convention**: use `/plan` before any request that involves modifying files or writing code. Claude will describe the plan and wait for approval before acting.

Paste this document at the start of a new Claude conversation with the following prompt:

> "This is the project context document for a cybersecurity readiness assessment system I am building at UL. Please read it carefully and continue from where we left off. The open questions and next steps are at the bottom. Use /plan before making any changes to files or code."

---

*Generated with Claude Sonnet 4.6 — update this document at the end of each working session.*
