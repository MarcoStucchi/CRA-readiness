# Cybersecurity Standards: Product-to-Standard Mapping Guide

> **Purpose:** Route products to the correct cybersecurity standard(s) for evaluation. Each standard has its own dedicated reference file — this document covers only scope, proof mechanism, and cross-standard relationships.  
> **How to use:** Identify the product sector, confirm scope, check the proof mechanism, then load the relevant standard file(s) for detailed evaluation criteria.

---

## Sector Quick-Reference Table

| Sector | Standard(s) | Proof Mechanism | Assessment Type |
|---|---|---|---|
| Consumer IoT | EN 303 645 | ETSI TS 103 701 test cases | Self-assessment |
| Industrial / OT | IEC 62443 (4-1, 4-2) | Certification SL1–SL4 | Third-party |
| Energy | IEC 62443 + IEC 62351 | Certification + protocol compliance evidence | Third-party |
| Automotive | ISO/SAE 21434 + UNECE R155/R156 | CSMS audit + national type approval (EU) | OEM-driven |
| Medical | IEC 81001-5-1 | MDR technical file integration | MDR notified body |
| Critical Components | Common Criteria (ISO/IEC 15408) | EAL evaluation by accredited lab | EU cybersecurity certification (CRA Annex IV) |
| Organisation | ISO/IEC 27001 | Certification or documented alignment | Third-party / self |

---

## 1. Consumer IoT → EN 303 645

**In-scope products:**
- Smart home devices (speakers, TVs, thermostats, cameras)
- Wearable health trackers
- Connected children's toys and baby monitors
- Home automation systems and gateways
- Connected appliances (washing machines, fridges)
- Retail tech with consumer-facing connectivity

**Out of scope:** Industrial, medical, and automotive devices even if network-connected.

**Proof mechanism:** ETSI TS 103 701 test cases + completed Implementation Conformance Statement (ICS)  
**Assessment:** Manufacturer self-assessment; third-party assessment possible via TS 103 701  
**Regulatory linkage:** Primary harmonised standard under EU Cyber Resilience Act (CRA) for default-category connected products; Clause 6 aligns with GDPR; maps directly to UK PSTI Act  
**Dedicated file:** `en_303_645.md`

---

## 2. Industrial / OT → IEC 62443

**In-scope products:**
- SCADA systems
- Programmable Logic Controllers (PLCs)
- Distributed Control Systems (DCS)
- Factory automation controllers
- Industrial network equipment and HMIs

**Key distinction within the standard:**
- **IEC 62443-4-1** applies to the *development organisation* (process)
- **IEC 62443-4-2** applies to the *component or product* (technical requirements)
- **IEC 62443-3-3** applies at the *system/zone level* — a product's certified Security Level (SL1–4) must match or exceed the target SL of the zone it is deployed in

**Proof mechanism:** Certification against Security Level 1–4 by an accredited body (e.g. TÜV, Exida, DNV)  
**Assessment:** Third-party  
**Dedicated file:** `iec_62443.md`

---

## 3. Energy → IEC 62443 + IEC 62351

**In-scope products:**
- Smart meters
- Grid sensors and Remote Terminal Units (RTUs)
- EV charging infrastructure
- Substation automation systems
- Distributed energy resource (DER) management systems

**Standard relationship:**
- **IEC 62443** provides the industrial security framework (see section 2 above)
- **IEC 62351** adds protocol-level security requirements specific to power systems communication (IEC 61850, DNP3, IEC 60870-5, etc.)

Both standards apply; evaluate against each independently.

**Proof mechanism:** IEC 62443 certification + IEC 62351 protocol compliance evidence  
**Assessment:** Third-party  
**Regional note:** North American grid operators may additionally require NERC CIP compliance — verify jurisdiction before evaluating  
**Dedicated files:** `iec_62443.md`, `iec_62351.md`

---

## 4. Automotive → ISO/SAE 21434 + UNECE R155/R156

**In-scope products:**
- Electronic Control Units (ECUs)
- Telematics Control Units (TCUs)
- Connectivity modules (V2X, cellular, Wi-Fi, Bluetooth)
- OBD interfaces
- Infotainment and gateway ECUs

**Standard relationship:**
- **ISO/SAE 21434** defines the cybersecurity engineering process (TARA, risk management, secure development lifecycle)
- **UNECE R155** is the regulatory requirement for a Cyber Security Management System (CSMS) — required for EU/UK type approval
- **UNECE R156** is the regulatory requirement for a Software Update Management System (SUMS) — governs OTA update governance

**Proof mechanism:** CSMS audit by OEM + national type approval authority approval (e.g. KBA in Germany, RDW in Netherlands)  
**Assessment:** OEM-driven; suppliers must demonstrate conformance to OEM cybersecurity requirements derived from ISO/SAE 21434  
**Dedicated files:** `iso_sae_21434.md`, `unece_r155_r156.md`

---

## 5. Medical → IEC 81001-5-1

**In-scope products:**
- Patient monitoring software
- Health data gateways
- Medical device firmware with network connectivity
- Clinical decision support systems
- Hospital information systems with device interfaces

**Critical regulatory note — CRA exclusion:** Medical devices already covered by EU MDR (2017/745) or IVDR (2017/746) are **explicitly excluded from the EU Cyber Resilience Act**. Cybersecurity conformity for these products is assessed through the MDR/IVDR technical file and notified body process, not through CRA.

**Proof mechanism:** IEC 81001-5-1 activities integrated into MDR technical file; assessed by MDR notified body  
**Assessment:** MDR notified body (e.g. BSI, TÜV SÜD, SGS)  
**US market note:** FDA Cybersecurity Guidance (2023) applies for US market submissions — document separately  
**Dedicated file:** `iec_81001_5_1.md`

---

## 6. Critical Components → Common Criteria (ISO/IEC 15408)

**In-scope products:**
- Hardware Security Modules (HSMs)
- Smart cards and SIM/eSIM
- Trusted Platform Modules (TPMs)
- Secure elements
- Cryptographic modules
- Trusted Execution Environments (TEEs)

**Proof mechanism:** EAL evaluation (EAL1–EAL7) by an accredited Common Criteria Testing Laboratory (CCTL); certificate issued by a national certification body (e.g. ANSSI, BSI Germany, NCSC)  
**Assessment:** Third-party accredited lab; certificates listed in the CCRA portal or SOG-IS MRA  
**CRA linkage:** CRA Annex I Class II and Annex IV products must undergo EU cybersecurity certification under the Cybersecurity Act (CSA) framework, which uses Common Criteria as its technical basis  
**Dedicated file:** `common_criteria_iso_15408.md`

---

## 7. Organisation → ISO/IEC 27001

**Applies to:** The organisation developing, operating, or supporting the product — not a product standard.

**Why it matters for product evaluation:**
- NIS2 Directive (EU 2022/2555) requires "appropriate technical and organisational measures" — ISO/IEC 27001 is the most widely accepted demonstration
- Increasingly required by enterprise customers as a procurement prerequisite
- Provides the organisational foundation from which product security programmes derive

**Proof mechanism:** ISO/IEC 27001 certification from an accredited body, or documented gap assessment against Annex A controls with remediation roadmap  
**Assessment:** Third-party certification body (UKAS, DAkkS, COFRAC, etc.) or self-assessed with documentation  
**Dedicated file:** `iso_iec_27001.md`

---

## Layered Standards: When Multiple Standards Apply

A product may fall under more than one standard. When overlap exists, always escalate to the most stringent mandatory assessment requirement — self-assessment is not acceptable where third-party certification is required by any applicable standard.

| Product Scenario | Applicable Standards |
|---|---|
| Connected EV charger (consumer-facing) | IEC 62443 + IEC 62351 + EN 303 645 |
| Wearable medical device | IEC 81001-5-1 + EN 303 645 |
| Automotive HSM / secure element | ISO/SAE 21434 + Common Criteria |
| Industrial gateway with cloud connectivity | IEC 62443 + ISO/IEC 27001 (org) |
| Smart meter | IEC 62443 + IEC 62351 |

---

## Regulatory Framework Context

| Regulation | Primary Sector | Standard Alignment |
|---|---|---|
| EU Cyber Resilience Act (CRA) | All connected products (excl. medical, automotive under type approval) | EN 303 645, IEC 62443, Common Criteria |
| EU MDR / IVDR | Medical devices | IEC 81001-5-1 |
| UNECE WP.29 R155/R156 | Automotive | ISO/SAE 21434 |
| NIS2 Directive | Critical infrastructure operators | ISO/IEC 27001 |
| GDPR | Any product processing personal data | EN 303 645 (Clause 6), ISO/IEC 27001 |

---

## Standard File Index

| File | Standard |
|---|---|
| `en_303_645.md` | ETSI EN 303 645 — Consumer IoT |
| `iec_62443.md` | IEC 62443 — Industrial / OT |
| `iec_62351.md` | IEC 62351 — Energy / Power Systems Protocols |
| `iso_sae_21434.md` | ISO/SAE 21434 — Automotive Cybersecurity Engineering |
| `unece_r155_r156.md` | UNECE R155 / R156 — Automotive CSMS and SUMS |
| `iec_81001_5_1.md` | IEC 81001-5-1 — Medical Device / Health Software |
| `common_criteria_iso_15408.md` | Common Criteria / ISO IEC 15408 — Critical Components |
| `iso_iec_27001.md` | ISO/IEC 27001 — Organisational ISMS |

---

*Guide version: 1.0 | Review annually — CRA implementing acts and harmonised standard designations are evolving through 2025–2026.*
