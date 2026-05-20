# CRA Annex I — Reconciliation table: draft COM(2022) 454 vs final Reg. EU 2024/2847

> **Purpose:** Map every requirement identifier used in the ENISA/JRC standards mapping (EUR 31892 EN, 2024)
> to the corresponding clause in the final CRA text. Use this table in `assess_path_a.py` to translate
> ENISA coverage findings to the correct final-text clause references.
>
> **Status of ENISA mapping per clause:**
> - ✅ Direct mapping — ENISA analysis fully applies
> - ⚠️ Partial — ENISA analysis applies but clause scope was slightly different in the draft
> - ❌ Not covered — clause did not exist in the draft; no ENISA standards coverage available

---

## Part I — Security property requirements

### Top-level clauses

| ENISA ref (draft) | Final text ref | Final text content (summary) | Mapping status | Notes |
|---|---|---|---|---|
| Requirement 1 | Part I (1) — first sentence | Risk-based design, development and production | ✅ Direct | ENISA Req 1 maps cleanly |
| Requirement 2 | Part I (1) — second sentence | Delivered without any known exploitable vulnerabilities | ✅ Direct | ENISA Req 2 maps cleanly; both sentences now form a single clause (1) in the final text |

> **Structural note:** In the final text, Req 1 and Req 2 of the draft are merged into a single
> unnumbered clause (1) with two sentences. The ENISA analysis treats them as separate requirements
> and should be read accordingly when applying coverage findings.

---

### Sub-requirements (2)(a) → (2)(m)

| ENISA ref (draft) | Final text ref | Final text content (summary) | Mapping status | Notes |
|---|---|---|---|---|
| 3a | Part I (2)(a) | Secure by default configuration; factory reset | ✅ Direct | |
| 3b | Part I (2)(b) | Protection from unauthorised access; authentication; IAM; report on access attempts | ⚠️ Partial | Final text adds "report on and protect against unauthorised access attempts" — not in draft; ENISA coverage does not address the reporting sub-element |
| 3c | Part I (2)(c) | Confidentiality of stored, transmitted, processed data; encryption at rest and in transit | ✅ Direct | |
| 3d | Part I (2)(d) | Integrity of data, commands, programs, configuration; report on corruptions | ✅ Direct | |
| 3e | Part I (2)(e) | Data minimisation | ✅ Direct | |
| 3f | Part I (2)(f) | Availability of essential functions; DoS resilience | ✅ Direct | |
| 3g | Part I (2)(g) | Minimise negative impact on availability of other devices/networks | ✅ Direct | |
| 3h | Part I (2)(h) | Limit attack surfaces including external interfaces | ✅ Direct | |
| 3i | Part I (2)(i) | Reduce impact of incidents; exploitation mitigation | ✅ Direct | |
| 3j | Part I (2)(j) | Security logging and monitoring; user opt-out for logging | ⚠️ Partial | Final text adds explicit "possibility for the user to disable this recording and/or monitoring function" — not in draft; ENISA coverage does not address user opt-out |
| 3k | Part I (2)(k) | Security updates; automatic updates enabled by default; user notification | ⚠️ Partial | Final text adds "automatic updates that are enabled by default" — stronger than draft wording; ENISA coverage addresses updates and notification but not the default-on auto-update requirement |
| *(not in draft)* | Part I (2)(l) | Patch dissemination without delay and free of charge; advisory messages to users | ❌ Not covered | New in final text; no ENISA standards mapping available — must be covered manually in `assess_path_a.py` |
| *(not in draft)* | Part I (2)(m) | Permanent and secure deletion of personal data and other data; accessible after support period | ❌ Not covered | New in final text; no ENISA standards mapping available — must be covered manually in `assess_path_a.py` |

---

## Part II — Vulnerability handling requirements

| ENISA ref (draft) | Final text ref | Final text content (summary) | Mapping status | Notes |
|---|---|---|---|---|
| VH 1 | Part II (1) | SBOM in machine-readable format; register in EUVD or public vulnerability database | ⚠️ Partial | Final text adds mandatory registration in EUVD (European Vulnerability Database, Art. 12 NIS2) — stronger than draft; ENISA coverage addresses SBOM format but not the EUVD registration obligation |
| VH 2 | Part II (2) | Address and remediate vulnerabilities without delay; security updates separated from functionality updates where possible | ✅ Direct | |
| VH 3 | Part II (3) | Effective and regular security testing | ✅ Direct | |
| VH 4 | Part II (4) | Public disclosure of fixed vulnerabilities; description, affected products, severity, remediation | ✅ Direct | |
| VH 5 | Part II (5) | Coordinated vulnerability disclosure (CVD) policy | ✅ Direct | |
| VH 6 | Part II (6) | Facilitate vulnerability information sharing; contact address | ✅ Direct | |
| VH 7 | Part II (7) | Secure update distribution mechanisms | ✅ Direct | |
| VH 8 | Part II (8) | Free and timely security patches; 10-year minimum availability of each security update | ⚠️ Partial | Final text adds explicit 10-year minimum availability obligation ("security update made available during the support period remains available for a minimum of 10 years from its issue date") — not in draft; ENISA coverage does not address this retention obligation |

---

## Summary: gaps requiring manual coverage in assess_path_a.py

| Clause | Type | Gap description | Suggested interim approach |
|---|---|---|---|
| Part I (2)(b) — reporting sub-element | ⚠️ Partial | "Report on and protect against unauthorised access attempts" not covered by ENISA mapping | Map to EN 303 645 provision 5.1-3 (monitoring of authentication attempts); flag as partially addressed |
| Part I (2)(j) — user opt-out | ⚠️ Partial | User opt-out for logging not addressed in any identified standard | Flag as gap; note EN 303 645 provision 5.10-1 (telemetry opt-out) as closest analogue |
| Part I (2)(k) — auto-update default-on | ⚠️ Partial | Default-on automatic updates stronger than draft wording; ENISA coverage does not fully address | Map to EN 303 645 provisions 5.3-2, 5.3-3; flag the default-on requirement as a gap |
| Part I (2)(l) | ❌ Not covered | No ENISA standards mapping; clause entirely new in final text | Map manually to EN 303 645 provisions 5.3-7, 5.3-8 (update delivery); flag "free of charge" as policy requirement with no standard coverage |
| Part I (2)(m) | ❌ Not covered | No ENISA standards mapping; clause entirely new in final text | Map manually to EN 303 645 provision 5.11-1 (data deletion); flag "after support period" obligation as gap |
| Part II (1) — EUVD registration | ⚠️ Partial | EUVD registration obligation not in draft; no standard addresses it | Flag as regulatory obligation (Art. 12 NIS2); no standard coverage — procedural compliance only |
| Part II (8) — 10-year patch availability | ⚠️ Partial | 10-year retention obligation not in draft; no standard addresses it | Flag as regulatory obligation; no standard coverage — policy/contractual compliance only |

---

## How to use this table in assess_path_a.py

When Path A loads the ENISA mapping to assess a product against CRA Annex I:

1. For clauses with status ✅ — use ENISA coverage findings directly, substituting the final-text clause reference
2. For clauses with status ⚠️ — use ENISA coverage findings for the shared portion, then add a manual gap note for the delta between draft and final text (described in the Notes column above)
3. For clauses with status ❌ — skip ENISA mapping entirely; apply manual mapping from the "Suggested interim approach" column; flag explicitly in the gap table as "not covered by ENISA mapping — manual assessment required"

---

*Produced: 2026-05-20 | Based on: COM(2022) 454 draft structure as used in EUR 31892 EN vs Reg. EU 2024/2847 final text*
