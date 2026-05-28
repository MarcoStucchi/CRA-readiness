# CRA → ETSI Standards Mapping
**Provision-level coverage analysis**
Standards: EN 303 645 V3.1.3 · TS 103 701 V2.1.1 · EN 18031-1/2/3 (2024)
Version: 0.1 — May 2026 · Status: Working draft

---

## How to read this document

Each CRA requirement has one table with a row per standard. Coverage and gaps are assessed at provision level, not topic level.

**Coverage ratings**

| Symbol | Meaning |
|--------|---------|
| ✅ FULL | The standard addresses all substantive dimensions of the CRA requirement at outcome level |
| 🟡 PARTIAL | The standard addresses some but not all dimensions, or addresses them only indirectly |
| ❌ NONE | The standard has no relevant provisions |

**Gap types** — used when coverage is FULL or PARTIAL but something is still missing

| Code | Type | Meaning |
|------|------|---------|
| \[C\] | Coverage | The requirement dimension is simply not addressed by the standard |
| \[P\] | Prescriptiveness | The requirement is addressed at outcome level but the standard leaves implementation detail to the manufacturer |
| \[T\] | Testability | The requirement is addressed but lacks a repeatable, objective test procedure |

> **Note:** \[P\] gaps are not failures of the standard — EN 303 645 is deliberately outcome-focused. They signal where a manufacturer must make and document implementation choices, and where an assessor must exercise judgement.

---

## Summary overview

| CRA Requirement | EN 303 645 V3.1.3 | TS 103 701 V2.1.1 | EN 18031-1/2/3 | Gap types |
|---|---|---|---|---|
| I·§1(1) No known exploitable vulnerabilities | 🟡 PARTIAL | 🟡 PARTIAL | 🟡 PARTIAL | \[C\] \[P\] \[T\] |
| I·§1(2) Secure by default configuration | ✅ FULL | ✅ FULL | ✅ FULL | \[P\] \[T\] |
| I·§1(3) Secure update mechanism | ✅ FULL | ✅ FULL | ✅ FULL | \[P\] \[T\] |
| I·§1(4) Data confidentiality | 🟡 PARTIAL | 🟡 PARTIAL | 🟡 PARTIAL | \[C\] \[P\] \[T\] |
| I·§1(5) Data integrity protection | 🟡 PARTIAL | 🟡 PARTIAL | ✅ FULL | \[C\] \[P\] \[T\] |
| I·§1(6) Vulnerability disclosure & handling | ✅ FULL | 🟡 PARTIAL | ❌ NONE | \[C\] \[T\] |
| I·§1(7) Availability & resilience to DoS | 🟡 PARTIAL | 🟡 PARTIAL | 🟡 PARTIAL | \[C\] \[P\] \[T\] |
| II·§2(1) Identify & document vulnerabilities / SBOM | 🟡 PARTIAL | ❌ NONE | ❌ NONE | \[C\] \[P\] |
| II·§2(2) Security support period | 🟡 PARTIAL | 🟡 PARTIAL | ❌ NONE | \[C\] \[P\] \[T\] |

---

## Annex I · Part I — Product-related security requirements

---

### CRA·I·§1(1) — No known exploitable vulnerabilities

> *Products shall be placed on the market without known exploitable vulnerabilities.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | 🟡 PARTIAL | 5.0-1 Justification record for non-applicable provisions · 5.6-1 Unused interfaces disabled · 5.6-3 Least privilege software operation · 5.7-1 Software integrity via secure boot (should) · 5.13-1 Input data validation | Provisions address structural hardening and attack-surface minimisation that reduce the likelihood of exploitable vulnerabilities, but there is no requirement for a pre-market vulnerability assessment or verification that no known CVEs exist at point of conformity | \[C\] No structured pre-market vulnerability assessment or threat modelling required (threat model only referenced as a recommendation in 5.0 rationale) · \[P\] No specification of vulnerability scanning methodology, CVE database checks, or SBOM-based analysis · \[T\] No testable criterion for "no known exploitable vulnerability" at point of conformity assessment |
| **TS 103 701 V2.1.1** | 🟡 PARTIAL | T-5.6 Test cases for attack surface minimisation and interface disablement · T-5.13 Input validation testing via network interface fuzzing | Provides repeatable test procedures for the EN provisions listed, adding testability. Does not include a CVE-check or vulnerability database test procedure | \[C\] No test procedure for verifying absence of known CVEs or SBOM completeness · \[T\] Fuzzing scope is defined per-provision; no holistic vulnerability assessment test scenario |
| **EN 18031-1/2/3** | 🟡 PARTIAL | GEC-1 Up-to-date software/hardware — products shall use components free from known vulnerabilities · GEC-4 Exposed interfaces shall be documented and minimised | GEC-1 is the closest provision to the CRA intent, explicitly requiring absence of known vulnerabilities in components. More prescriptive than EN 303 645 on this specific point. Scope limited to radio equipment | \[P\] GEC-1 does not specify the methodology for verifying "known vulnerability" status (e.g. NVD lookup, SBOM tooling) · \[T\] Test methods for GEC-1 still being finalised in companion test specification |

**Cross-standard note:** SBOM as a tool for systematic vulnerability identification is absent from all three standards. This is a genuine gap that will require new content in any CRA-specific harmonised standard.

---

### CRA·I·§1(2) — Secure by default configuration

> *Products shall be delivered with a secure by default configuration, including the possibility to reset the product to its original state.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | ✅ FULL | 5.1-1 Unique per-device passwords; no universal defaults (shall) · 5.1-2 Brute-force protection (shall) · 5.6-1 Unused logical and physical interfaces disabled (shall) · 5.6-6 Unnecessary physical interfaces not exposed in production (shall) · 5.12-3 Means to restore to factory settings; user informed of implications (should) | This is one of the strongest areas of EN 303 645 alignment with CRA. Provisions 5.1-1 and 5.1-2 directly address the no-universal-default-passwords requirement. 5.6-1/5.6-6 address secure default configuration. 5.12-3 covers the factory reset requirement. Coverage is substantive across both the "secure default" and "resettable" dimensions | \[P\] 5.12-3 uses "should" (recommendation) rather than "shall" (requirement) for factory reset — the CRA intent appears mandatory, creating a modal asymmetry |
| **TS 103 701 V2.1.1** | ✅ FULL | T-5.1-1 Verify password uniqueness; test universal default credential scenario · T-5.1-2 Brute-force protection — automated credential stuffing simulation · T-5.6-1 Enumerate and verify all logical interfaces; confirm disabled state of unused ones · T-5.12-3 Factory reset procedure verification including data erasure confirmation | Provides concrete, repeatable test cases for all relevant provisions including password uniqueness, brute-force protection, interface enumeration, and factory reset. One of the areas where the EN + TS combination is most complete | \[T\] Factory reset data erasure test does not specify cryptographic verification of erasure completeness — assessor judgement required |
| **EN 18031-1/2/3** | ✅ FULL | GEC-9 Secure startup configuration — device shall start in a secure state without user intervention · GEC-2 Limiting service exposure — only required services enabled by default | GEC-9 is more explicitly prescriptive than EN 303 645 on secure startup, directly requiring that no user action is needed to achieve a secure state. This is a stronger formulation and complementary to EN 303 645 in a combined compliance strategy | \[T\] Test methods for GEC-9 "secure startup" not yet fully standardised in a companion test specification |

---

### CRA·I·§1(3) — Secure update mechanism

> *Products shall be able to receive security updates and shall have a secure update mechanism, including the ability to receive updates automatically.*

**Note on ENISA mapping:** The ENISA CRA Standards Mapping document claims EN 303 645 "lacks detailed guidance on secure mechanisms for installing/implementing updates." This assessment is not supported by the V3.1.3 text. As the provision mapping below shows, clause 5.3 addresses updateability, the secure mechanism itself, integrity and authenticity verification, user notification, cryptographic protection, and timeliness. The ENISA claim appears to confuse the absence of prescriptive implementation detail (a deliberate design choice) with absence of coverage.

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | ✅ FULL | 5.3-1 Software shall be securely updateable; resource-constraint exception with justification · 5.3-2 Device shall have a secure update mechanism unless use-case resource constraints prevent it · 5.3-3 Update shall be verified for authenticity and integrity before being applied (shall) · 5.3-4 User shall be notified prior to automatic update installation (shall) · 5.3-5 Device shall notify user when update is available (shall) · 5.3-6 Device should continue to function during update where reasonably possible (should) · 5.3-7 Best practice cryptography shall be used for the update mechanism (shall) · 5.3-8 *(V3 new)* Security updates shall be timely; critical vulnerabilities with priority handling (shall) | Comprehensive outcome-level coverage across all CRA dimensions: updateability, secure mechanism, integrity/authenticity verification, user notification for automatic updates, update availability notification, operational continuity, cryptographic protection, and timeliness. No substantive CRA dimension is unaddressed | \[P\] 5.3-7 requires "best practice cryptography" without specifying algorithm families, key lengths, or signature schemes · \[P\] Anti-rollback protection not mandated (referenced in rationale as an example only) · \[T\] 5.3-8 timeliness has no defined timeframe (e.g. days from patch availability to deployment), making conformance assessment of "timely" dependent on assessor judgement |
| **TS 103 701 V2.1.1** | ✅ FULL | T-5.3-1 Verify device accepts and applies a valid signed update package · T-5.3-2 Verify device rejects unsigned or tampered update packages · T-5.3-3 Verify integrity check failure results in update rejection and safe fallback · T-5.3-4 Verify user notification mechanism for automatic update scenarios · T-5.3-7 Verify cryptographic algorithm and key length against current best practice reference list | Adds significant testability to the EN provisions. Notably, T-5.3-2 and T-5.3-3 provide concrete negative test cases (tampered update rejection, integrity failure handling) that directly address the CRA's intent of a verifiably secure mechanism. The EN + TS combination substantially closes the ENISA-cited gap | \[T\] No specific test case for anti-rollback enforcement · \[T\] Timeliness (5.3-8) has no corresponding test procedure — assessed via documentation review only |
| **EN 18031-1/2/3** | ✅ FULL | GEC-1 Software/firmware shall be updatable; update mechanism shall preserve integrity · RCP-1 *(EN 18031-2)* Secure update channel requirements for radio-connected devices | Complements EN 303 645 specifically for radio equipment. GEC-1 overlaps substantially with 5.3-1/5.3-2. EN 18031 adds value by specifying update channel security more explicitly for wireless interfaces | \[T\] Companion test specification for EN 18031 update requirements still in development |

---

### CRA·I·§1(4) — Data confidentiality

> *Products shall protect the confidentiality of stored, transmitted or otherwise processed data, including personal data, by appropriate technical means.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | 🟡 PARTIAL | 5.4-1 Sensitive security parameters in persistent storage shall be stored securely (shall) · 5.4-3 Hard-coded critical security parameters in source code shall not be used (shall) · 5.5-1 Best practice cryptography shall be used for communication security (shall) · 5.5-2 Device shall use reviewed/evaluated cryptographic implementations (shall) · 5.8-1 Communication of personal data shall be encrypted (shall) · 6-1 Data minimisation — only necessary personal data processed (shall) · 6-6 *(V3 new)* Data storage and processing shall be appropriately protected | Strong communication-layer and security-parameter confidentiality coverage. The V3 addition of 6-6 strengthens data-at-rest coverage. However, general user data stored at rest (beyond "sensitive security parameters") is not explicitly required to be encrypted | \[C\] No general requirement to encrypt all stored user data — 5.4-1 scope limited to "sensitive security parameters," not general application or user data · \[P\] "Best practice cryptography" (5.5-1/5.5-2) not defined — no reference to specific protocol versions (e.g. TLS 1.2+), algorithm suites, or key lengths · \[T\] Clause 6 data protection provisions assessed primarily via documentation and policy review rather than technical test |
| **TS 103 701 V2.1.1** | 🟡 PARTIAL | T-5.4-1 Verify sensitive parameter storage protection via key extraction attempt · T-5.5-1 Verify communication uses current best practice cipher suites; reject weak cipher suites · T-5.8-1 Verify personal data transmitted over network is encrypted; traffic interception and inspection | Good communication-layer test coverage. Limited test procedures for data-at-rest confidentiality beyond security parameter storage. Clause 6 provisions have minimal corresponding test cases | \[T\] No test procedure for general user data at rest encryption · \[T\] Cipher suite "best practice" reference list is informative, not normative — risk of inconsistent assessor interpretation across labs |
| **EN 18031-1/2/3** | 🟡 PARTIAL | CRP-1 Cryptographic protection of communications — specific protocol requirements for radio interfaces · CRP-2 Key management requirements for radio equipment | More prescriptive than EN 303 645 on communication-layer cryptography, particularly for wireless protocols. Adds value specifically for radio equipment but does not address general data-at-rest confidentiality | \[C\] No data-at-rest confidentiality requirement |

---

### CRA·I·§1(5) — Data integrity protection

> *Products shall protect the integrity of stored, transmitted or otherwise processed data, commands, programs and configuration against any manipulation or modification not authorised by the user.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | 🟡 PARTIAL | 5.3-3 Update authenticity and integrity verification before applying (shall) · 5.4-2 Hard-coded unique device identity used for security shall resist tampering — physical, electrical, software (shall) · 5.5-1 Best practice cryptography — implicitly covers integrity through authenticated encryption · 5.7-1 Software integrity shall be verified using secure boot (should) · 5.7-2 Device shall be able to detect and recover from unauthorised software modifications (shall) | Software and firmware integrity well addressed (5.7-1/5.7-2, 5.3-3). Data integrity in transit addressed implicitly through 5.5-1. Integrity of configuration data and commands at rest or in transit not explicitly required beyond security parameters | \[C\] No explicit requirement for integrity protection of configuration data at rest or user commands in transit · \[P\] 5.7-1 uses "should" (recommendation) for secure boot — the strongest integrity mechanism is not mandated · \[T\] 5.7-2 (recovery from unauthorised modification) difficult to test — requires inducing a controlled modification with practical lab challenges |
| **TS 103 701 V2.1.1** | 🟡 PARTIAL | T-5.7-1 Verify secure boot prevents loading of unsigned firmware · T-5.7-2 Verify detection and recovery from induced firmware modification | Test cases for 5.7 are among the more technically demanding in the specification. Both provide meaningful coverage of software integrity testability | \[T\] No test procedure for configuration data integrity · \[T\] Recovery test (T-5.7-2) methodology varies by device architecture — risk of inconsistent assessor interpretation |
| **EN 18031-1/2/3** | ✅ FULL | GEC-5 Device shall verify integrity of code, configuration and data · GEC-7 Device shall validate authenticity of commands received from associated services | GEC-5 and GEC-7 are more complete than EN 303 645 on integrity — explicitly covering configuration data and command integrity, not only software/firmware. This closes the coverage gap identified in EN 303 645 for this CRA requirement | \[T\] Companion test specification for GEC-5/GEC-7 still being finalised |

**Cross-standard note:** For integrity, EN 18031 and EN 303 645 are genuinely complementary. A combined compliance approach using both standards achieves full coverage of this CRA requirement at outcome level.

---

### CRA·I·§1(6) — Vulnerability disclosure and handling

> *Manufacturers shall address and remediate vulnerabilities without delay, provide security updates, and make available a coordinated vulnerability disclosure policy. Products shall support identification of components including a software bill of materials (SBOM).*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | ✅ FULL | 5.2-1 Vulnerability disclosure policy shall be publicly available (shall) — V3 references ETSI TR 103 838 as implementation example · 5.2-2 Disclosed vulnerabilities shall be acted on in a timely manner (shall) · 5.2-3 Manufacturer shall provide a point of contact for vulnerability reporting (shall) · 5.3-8 Security updates shall be timely; critical vulnerabilities handled with priority (shall) | Provisions 5.2-1 through 5.2-3 directly address the coordinated vulnerability disclosure requirement. The V3 addition of TR 103 838 as a reference example strengthens the guidance. Coverage is full for the disclosure policy and process dimension. The SBOM requirement is a genuine gap | \[C\] No SBOM requirement — this is a significant coverage gap; the CRA explicitly requires a machine-readable software bill of materials and EN 303 645 has no equivalent · \[T\] "Timely" handling (5.2-2, 5.3-8) has no defined timeframe — assessed via process review, not objective metric |
| **TS 103 701 V2.1.1** | 🟡 PARTIAL | T-5.2-1 Verify vulnerability disclosure policy is publicly available and contains required elements · T-5.2-3 Verify contact mechanism is functional and accessible | Workable test procedures for disclosure policy existence and accessibility. Primarily documentation/process checks rather than technical tests, which is appropriate for this requirement type | \[C\] No test procedure for SBOM completeness or format (e.g. SPDX, CycloneDX) · \[T\] Timeliness of remediation cannot be tested at point-in-time conformity assessment — requires longitudinal monitoring |
| **EN 18031-1/2/3** | ❌ NONE | — | EN 18031 focuses entirely on technical product requirements and does not address organisational/process requirements such as vulnerability disclosure policies. EN 303 645 is the sole ETSI source for this CRA requirement | \[C\] Complete gap — vulnerability disclosure is outside EN 18031 scope by design |

---

### CRA·I·§1(7) — Availability and resilience to denial-of-service

> *Products shall be resilient against denial-of-service attacks and shall maintain availability of essential functions. Network and power outage resilience shall be addressed.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | 🟡 PARTIAL | 5.9-1 Device shall remain operable and locally functional in the event of a loss of network connectivity (shall) · 5.9-2 Device shall recover from power outages without requiring user intervention (shall) · 5.6-5 Rate-limiting bypass resistance — implicitly addresses some DoS vectors · 5.13-1 Input validation — indirectly mitigates malformed-input DoS vectors | Network outage resilience (5.9-1) and power outage recovery (5.9-2) addressed effectively. No explicit provision for DoS attack resilience — the standard focuses on outage resilience, not attack-induced unavailability. This distinction matters for CRA compliance | \[C\] No explicit DoS resilience requirement — 5.9 addresses outages, not attack-induced unavailability · \[P\] No rate-limiting or connection-limiting requirement specified for network interfaces · \[T\] DoS simulation testing not included in TS 103 701 scope |
| **TS 103 701 V2.1.1** | 🟡 PARTIAL | T-5.9-1 Simulate network disconnection and verify local operation continuity · T-5.9-2 Simulate power interruption and verify automatic recovery to operational state | Clear and executable test procedures for outage scenarios. Good coverage of the outage-resilience dimension of the CRA requirement | \[C\] No DoS simulation test procedure |
| **EN 18031-1/2/3** | 🟡 PARTIAL | GEC-6 Network resilience — device shall limit negative impact on network availability from its own behaviour | GEC-6 addresses an important dimension absent from EN 303 645: the device's responsibility not to become a DoS source against the network. Meaningful contribution but addresses outbound behaviour only, not inbound attack resilience | \[C\] Addresses outbound behaviour only — inbound DoS attack resilience not covered |

---

## Annex I · Part II — Vulnerability and lifecycle management requirements

*Part II requirements are primarily organisational and lifecycle-oriented rather than product-technical. This is reflected in generally lower coverage by product technical standards (EN 303 645, EN 18031) and greater reliance on EN 303 645's organisational provisions and TS 103 701's documentation-based test procedures.*

---

### CRA·II·§2(1) — Identify and document vulnerabilities and components (SBOM)

> *Manufacturers shall identify and document vulnerabilities and components contained in their products, including by drawing up a software bill of materials (SBOM) at least in a machine-readable format.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | 🟡 PARTIAL | 5.0-1 Justification shall be recorded for each non-applicable/non-fulfilled recommendation — establishes documentation discipline · 5.2-1/2/3 Vulnerability disclosure policy, timely action, contact point — addresses vulnerability handling, not identification process | Vulnerability handling and disclosure are addressed organisationally but the SBOM requirement and structured component-level vulnerability identification process are not. Provision 5.0-1 is a weak proxy for the CRA's more rigorous component documentation intent | \[C\] No SBOM requirement — significant and genuine gap relative to CRA §2(1) · \[C\] No structured component vulnerability identification process required (e.g. per-component CVE monitoring) · \[P\] No specification of SBOM format (SPDX, CycloneDX) or minimum required content |
| **TS 103 701 V2.1.1** | ❌ NONE | — | No test procedures addressing SBOM or component vulnerability identification. Consistent with EN 303 645 having no such provisions to test | \[C\] Complete gap — no relevant test procedures |
| **EN 18031-1/2/3** | ❌ NONE | — | EN 18031 is a product technical standard and does not address manufacturer lifecycle management processes such as SBOM production | \[C\] Complete gap — SBOM is a genuine cross-standard gap requiring new content in any CRA-specific harmonised standard |

**Cross-standard note:** SBOM is the most significant single gap across all three standards relative to CRA requirements. No existing ETSI standard addresses it. New harmonised standard content will be required.

---

### CRA·II·§2(2) — Security support period

> *Manufacturers shall ensure a security support period appropriate to the expected product lifetime. Security updates shall remain available for the duration of this period and users shall be informed of the support period at point of purchase.*

| Standard | Coverage | Relevant provisions | Coverage assessment | Gaps |
|---|---|---|---|---|
| **EN 303 645 V3.1.3** | 🟡 PARTIAL | 5.3-1 Software shall be securely updateable — implies ongoing update availability but does not set a period · 5.3-9 Manufacturer shall define a minimum support period for security updates and communicate this to users (shall) | Provision 5.3-9 directly addresses the support period concept and aligns well with the CRA intent. However, no minimum floor for support period duration is set — the standard leaves the period entirely to manufacturer discretion | \[P\] No minimum support period floor — "appropriate to expected product lifetime" is an outcome without a threshold · \[T\] Support period commitment assessed via documentation review only; no testable technical criterion · \[C\] No requirement for end-of-life notification to users when support period ends |
| **TS 103 701 V2.1.1** | 🟡 PARTIAL | T-5.3-9 Verify support period is documented and communicated to users at point of sale or in product documentation | Provides a documentation-based test for support period communication. Appropriate test type for this requirement but cannot validate that the commitment will actually be honoured over time | \[T\] Cannot test actual support period fulfilment at point-in-time conformity assessment — inherently a market surveillance issue rather than a pre-market conformity issue |
| **EN 18031-1/2/3** | ❌ NONE | — | EN 18031 is a product technical standard and does not address manufacturer lifecycle commitments | \[C\] Complete gap — lifecycle commitment requirements are outside EN 18031 scope by design |

---

## Structural observations

The following observations apply across all CRA requirements mapped in this document.

**1. The ENISA coverage assessment systematically underestimates EN 303 645**
The ENISA CRA Standards Mapping (November 2024) cites EN 303 645 V2.1.1 and conflates the standard's deliberate outcome-based design with coverage gaps. In multiple cases — most clearly for secure updates (§1(3)) — the standard addresses all substantive CRA dimensions. The ENISA document does not distinguish between coverage gaps \[C\], prescriptiveness gaps \[P\], and testability gaps \[T\], causing all three to appear as equivalent deficiencies.

**2. EN 303 645 + TS 103 701 should be assessed as a system**
TS 103 701 is not a harmonised standard and cannot itself confer presumption of conformity under CRA. However, the two documents are designed as a pair: EN 303 645 sets outcome-level requirements, TS 103 701 defines how conformance is assessed. Evaluating EN 303 645 without TS 103 701 significantly understates the practical testability of its provisions.

**3. EN 18031 and EN 303 645 are complementary, not competing**
For integrity (§1(5)) and attack surface minimisation, EN 18031 provisions (GEC-5, GEC-7) fill genuine gaps left by EN 303 645. For vulnerability disclosure (§1(6)) and lifecycle requirements (Part II), EN 303 645 is the primary source and EN 18031 has no relevant provisions. A combined compliance strategy using both standards achieves better total coverage than either alone.

**4. SBOM is the most significant cross-standard gap**
No existing ETSI standard — EN 303 645, TS 103 701, or EN 18031 — addresses the SBOM requirement of CRA §2(1). This is a genuine gap requiring new content in harmonised standards developed specifically for CRA. It is one of the few areas where the ENISA gap assessment is correct.

**5. Part II requirements are structurally less well covered**
CRA Annex I Part II requirements (organisational/lifecycle) are systematically less covered than Part I (product-technical). This is structurally expected — product technical standards cannot fully address manufacturer process obligations. New harmonised standards or guides developed under the CRA standardisation request will need to address Part II requirements more directly.

---

## Document status and limitations

- **CRA harmonised standards not yet designated:** As of May 2026, no standards have been published in the Official Journal of the EU as harmonised standards under the CRA. This mapping uses EN 303 645 V3.1.3, TS 103 701 V2.1.1, and EN 18031-1/2/3 (2024) as the current best-available ETSI references.
- **This is an independent analytical document** — not an official ENISA, ETSI, or European Commission publication.
- **Coverage assessments reflect the authors' analytical judgement** and should be verified against the primary standard texts.
- **This document requires updating** as CRA harmonised standards are formally designated and as ETSI develops new ENs in response to the CRA standardisation request.
- **EN 18031 test specifications** for several GEC provisions are still in development; testability assessments for that standard are preliminary.
