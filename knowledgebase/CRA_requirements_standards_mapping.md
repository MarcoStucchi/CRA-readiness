# CRA Requirements → Standards Mapping
### JRC & ENISA Joint Analysis | EUR 31892 EN | 2024

> **Purpose:** For each CRA Annex I essential requirement, this file identifies the most relevant existing standards, the coverage they offer, and the remaining gaps. Use this file alongside the routing guide and individual standard files to resolve specific CRA requirements during AI-assisted evaluation.  
> **Source:** Hernandez Ramos et al., *Cyber Resilience Act Requirements Standards Mapping*, Publications Office of the EU, 2024. doi:10.2760/905934

---

## Structure of CRA Annex I Requirements

The CRA defines two groups of essential requirements:

**Section 1 — Security requirements relating to the properties of products with digital elements** (requirements 1, 2, 3a–3k)  
**Section 2 — Vulnerability handling requirements** (requirements 1–8)

---

## Top-Level Coverage Summary

### Security Property Requirements

| Standard | Req 1 | Req 2 | 3a | 3b | 3c | 3d | 3e | 3f | 3g | 3h | 3i | 3j | 3k |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ETSI EN 303 645 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| EN ISO/IEC 27002:2022 | ✓ | | ✓ | | | | | ✓ | | | ✓ | ✓ | ✓ |
| EN IEC 62443-4-2:2019 | | | | ✓ | ✓ | ✓ | | ✓ | | ✓ | | ✓ | ✓ |
| EN IEC 62443-4-1:2018 | ✓ | ✓ | | | | | | | | | | | |
| EN ISO/IEC 27005:2022 | ✓ | | | | | | | | | | | | |
| EN IEC 62443-3-2:2020 | ✓ | | | | | | | | | | ✓ | | |
| ISO/IEC 18045:2022 | | ✓ | | | | | | | | | ✓ | | |
| ISO/IEC 15408-2:2022 | | | | | | | | | | ✓ | | | |
| ISO/IEC 27001:2022 | | | | | | | | | | | ✓ | | |
| ISO/IEC 27701:2019 | | | | | | | ✓ | | | | | | |
| ITU-T X.805 | | | | | ✓ | | | ✓ | | | | | |
| ITU-T Y.4810 | | | | | | | | | ✓ | | | | |
| ISO/IEC 18031:2011 | | | ✓ | | | | | | | | | | |
| ISO/IEC 13888-1:2020 | | | | | | | | | | | | ✓ | |
| IEC 62443-2-1:2010 | | | | | | | | | | | | | ✓ |

### Vulnerability Handling Requirements

| Standard | VH1 | VH2 | VH3 | VH4 | VH5 | VH6 | VH7 | VH8 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| EN ISO/IEC 30111:2020 | | ✓ | ✓ | ✓ | ✓ | ✓ | | ✓ |
| EN ISO/IEC 29147:2020 | | | | ✓ | ✓ | ✓ | | |
| EN IEC 62443-4-1:2018 | | ✓ | | ✓ | | | ✓ | ✓ |
| ISO/IEC 27002:2022 | | ✓ | ✓ | | | | ✓ | ✓ |
| ISO/IEC 27001:2022 | | ✓ | ✓ | | | | | |
| ETSI EN 303 645 | | | | ✓ | ✓ | | | |
| ISO/IEC 27036 Parts 1–3 | ✓ | | | | | | | |
| ISO/IEC 27005:2022 | | | ✓ | | | | | |
| ISO/IEC TS 27034-5-1:2018 | | | ✓ | | | | | |

> **Key finding:** No single standard covers all CRA requirements. ETSI EN 303 645 has the broadest coverage of security property requirements but is scoped to consumer IoT and carries gaps. EN ISO/IEC 30111 is the most relevant for vulnerability handling requirements.

---

## Section 1: Security Property Requirements

---

### Requirement 1 — Risk-based design, development and production

> *Products with digital elements shall be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity based on the risks.*

**Core concepts:** cybersecurity risk analysis across the full product lifecycle; security by design; secure coding

**Lifecycle stages:** Design, Implementation, Validation, Commissioning, Surveillance/Maintenance

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 27002:2022 | Secure coding controls; information security in supplier agreements | No equivalent guidance for hardware design; analogous hardware provisions are missing |
| EN ISO/IEC 27005:2022 | Risk management process; risk analysis as the basis for "appropriate level of cybersecurity" | Generic; not specific to product development |
| EN IEC 62443-3-2:2020 | Security Risk Assessment process for system design including residual risk evaluation after countermeasures | IACS-specific; does not cover security-by-design principles |
| EN IEC 62443-4-1:2018 | Security-by-design principles in product development phases | IACS-specific; does not cover risk assessment concept |
| ETSI EN 303 645 | Promotes secure development and maintenance practices; implies need for risk analysis via secure design framework | Detailed risk analysis guidelines not provided; consumer IoT scoped |

**Overall gap:** Hardware design coverage is weaker than software; risk analysis specifically targeted at system design exists only for IACS (IEC 62443-3-2), while ISO 27005 is not specific to product design.

---

### Requirement 2 — No known exploitable vulnerabilities at delivery

> *Products with digital elements shall be delivered without any known exploitable vulnerabilities.*

**Core concepts:** vulnerability assessment; fixing known vulnerabilities before product release

**Lifecycle stages:** Validation, Surveillance/Maintenance

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 18045:2022 (Common Criteria CEM) | Minimum actions for IT security evaluation; dedicated vulnerability assessment section with penetration testing | Covers vulnerability discovery only, not fixing; single technique cited |
| ITU-T X.1214 | Vulnerability detection of ICT network elements; covers known and zero-day vulnerabilities via scanning, fuzzing, code review, binary analysis, penetration testing | Detection only, not fixing; no step-by-step procedure; ICT network element scope |
| EN IEC 62443-4-1:2018 | Security testing requirements including vulnerability testing, penetration testing; describes scope, responsibility and management of identified issues | IACS-specific |
| ETSI EN 303 645 (Provision 5.2-3) | Requires manufacturers to continually monitor, identify and rectify vulnerabilities during defined support period | No explicit requirement to conduct vulnerability assessment; no explicit requirement to fix all known exploitable vulnerabilities before release |

**Overall gap:** Standards collectively cover vulnerability detection across pre- and post-delivery phases but — with the exception of IEC 62443-4-1 (IACS only) — do not cover the patching of discovered vulnerabilities, leaving the full requirement only partially addressed.

---

### Requirement 3a — Secure by default configuration; factory reset

> *Be delivered with a secure by default configuration, including the possibility to reset the product to its original state.*

**Core concepts:** default configuration; randomised/unique password; non-erasable memory for configuration; factory reset function

**Lifecycle stages:** Design, Implementation

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 27002:2022 | Configuration management control; security configuration guidance for hardware, software, services and networks | General guidelines; does not specifically target this requirement |
| ETSI EN 303 645 | Default password provisions; secure storage of sensitive parameters; credential management (password generation, authentication, change of default values) | High-level provisions; lacks detail on a "reasonable security level" in default configuration; consumer IoT scoped |
| ISO/IEC 18031:2011 | Models for non-deterministic and deterministic random bit generators; covers random PIN and password generation | Dedicated to random bit generation models; does not target configuration management |

**Overall gap:** Aspects of random password/key generation are well covered by ISO/IEC 18031. Configuration/credential management is addressed at high level in ISO/IEC 27002 and EN 303 645 with references to NIST for details. Specific implementation aspects (e.g. use of non-erasable memories for configuration) are not covered.

---

### Requirement 3b — Protection from unauthorised access

> *Ensure protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity or access management systems.*

**Core concepts:** authentication; authorisation; identity & access management (IAM); physical and logical access control; anti-tampering

**Lifecycle stages:** Design, Implementation, Validation

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 9798 (Parts 1–6) | Entity authentication model; general requirements; variety of protocols including one-to-one and third-party authentication | Covers authentication only |
| ISO/IEC 24760 (Parts 1–3) | Identity management framework; terminology, reference architecture, requirements, and conformance guidance | Covers identity management only; does not cover access management |
| ISO/IEC 29146:2016 | Access management framework built on identity management systems; secure and accountable access to ICT resources | Covers access management only; identity management is a prerequisite not covered here |
| ITU-T X.1253 | Guidelines for secure and privacy-preserving deployment and operation of identity management systems | Generic; high-level descriptions only |
| ITU-T X.812 | General access control framework, policies and mechanisms; usable as reference for other standards | Generic; does not describe specific mechanisms or step-by-step access control |
| ETSI EN 303 645 (5.1, 5.5) | Authentication, unique passwords, cryptographic measures | Emphasises authentication and cryptography; lacks specifics on access management systems |
| EN IEC 62443-4-2:2019 | User authentication (Foundational Requirement 1); authorisation (Component Requirement 2-1) | IACS-specific |

**Overall gap:** Authentication, identity management, and access control areas are well covered but mostly by generic standards that do not specify mechanisms. No single standard combines all three areas comprehensively.

---

### Requirement 3c — Data confidentiality

> *Protect the confidentiality of stored, transmitted or otherwise processed data, personal or other, such as by encrypting relevant data at rest or in transit by state of the art mechanisms.*

**Core concepts:** symmetric/asymmetric encryption; encryption at rest and in transit; PKI; certificates; data confidentiality

**Lifecycle stages:** Design, Implementation

| Standard | Coverage | Gap |
|---|---|---|
| ITU-T X.805 | Generic security architecture for end-to-end communication security across network types | Does not cover data at rest; very generic |
| ISO/IEC 18033 (Parts 1–7) | Encryption algorithms for data confidentiality at rest and in transit; symmetric, asymmetric, homomorphic, and identity-based ciphers | Does not describe key management; some algorithms are deprecated |
| ITU-T X.814 | Basic confidentiality concepts; types of confidentiality services, mechanisms, threats and attacks | Very generic; does not describe specific protocols |
| ETSI EN 303 645 (5.5-1, 5.5-6, 5.5-7, 5.8-1, 5.8-2, 5.4-1, 5.4-4) | Secure communication and confidentiality using cryptography; cryptographic protection of personal data; secure storage and uniqueness of security parameters | Lacks specific coverage for protecting all data types at rest; does not fully address particular encryption schemes |
| EN IEC 62443-4-2:2019 (Component Req 4.1) | Confidentiality requirement for data at rest and in transit | IACS-specific; requirement is generic without technical detail |

**Overall gap:** Basic principles and algorithms for data confidentiality (at rest and in transit) are well covered. Key management is a consistent gap across the identified standards.

---

### Requirement 3d — Data integrity

> *Protect the integrity of stored, transmitted or otherwise processed data, personal or other, commands, programs and configuration against any manipulation or modification not authorised by the user, as well as report on corruptions.*

**Core concepts:** integrity; hashing; checksum; data corruption; PKI; certificates; self-test

**Lifecycle stages:** Design, Implementation

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 9796 (Parts 2–3) | Digital signature schemes with message recovery; deterministic and randomized mechanisms; key production | Does not cover digital signatures with appendix; no key management or random number generation |
| ISO/IEC 9797 (Parts 1–3) | MAC algorithms based on block ciphers, dedicated or universal hash functions; generic enough for any security architecture | Does not cover key management of block cipher mechanisms |
| ISO/IEC 14888 (Parts 1–3) | Digital signatures with appendix; multiple mechanisms including identity-based and certificate-based schemes | Does not cover signatures with message recovery; no key/certificate management or random number generation |
| ITU-T X.815 | Basic integrity concepts; types of integrity services, policies, mechanisms, threats and attacks | Generic; does not describe specific mechanisms |
| ETSI EN 303 645 (5.4, 5.7) | Secure storage; software integrity | Covers many integrity aspects; does not explicitly detail information integrity |
| EN IEC 62443-4-2:2019 | Specific integrity requirements for software, updates, configuration, communications, audit logs | IACS-specific; some requirements lack general applicability |

**Overall gap:** Basic integrity concepts and specific mechanisms (digital signatures, MACs) are well covered. The standards are a mix of generic (integrity concepts) and specific (integrity mechanisms).

---

### Requirement 3e — Data minimisation

> *Process only data, personal or other, that are adequate, relevant and limited to what is necessary in relation to the intended use of the product ('minimisation of data').*

**Core concepts:** privacy; GDPR; data minimisation; personal data; data retention

**Lifecycle stages:** Design, Implementation, Validation, Commissioning, Surveillance/Maintenance, End of Life

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 27701:2019 | Extension to ISO 27001/27002 for privacy information management; includes GDPR mapping; covers data minimisation | Organisational standard, not product-specific; implementation by an organisation will however reflect in products |
| ISO/IEC 29100:2011 | High-level privacy framework for ICT systems; explanatory sections on key privacy concepts including data minimisation | No specific requirements or controls |
| ETSI TS 103 485 V1.1.1 | Privacy assurance and verification mechanisms; references Common Criteria and GDPR | No specific requirements or controls |
| ETSI EN 303 645 (5.8, 6) | Data protection and minimisation; secure data handling; transparent processing; only necessary data processed; aligns with GDPR principles | Lacks specific guidance on deletion of unnecessary data and prevention of forced registrations; limited explicit GDPR-specific best practices |

**Overall gap:** This requirement is well covered in ISO/IEC 27701, which maps directly to GDPR. The concept of data minimisation is well addressed across the identified standards.

---

### Requirement 3f — Availability and resilience against denial of service

> *Protect the availability of essential functions, including the resilience against and mitigation of denial of service attacks.*

**Core concepts:** availability; resilience; backup; DoS/DDoS mitigation; redundancy; rate limiting; minimise offered services

**Lifecycle stages:** Design, Implementation

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 27002:2022 | DoS protection for electronic messaging; availability of services and information | High-level guidance only |
| ISO/IEC 22237-1:2021 | Availability, reliability and resilience principles for data centres | Focused on data centre facilities; does not cover generic user product design |
| ITU-T X.805 | Network security architecture covering availability dimension; explicitly mentions DoS protection | Specific to end-to-end network security; does not cover general product design |
| ETSI EN 303 645 (5.5, 5.6, 5.9) | Secure communication; attack surface minimisation; resilience to outages including DDoS mitigation | High-level provisions; consumer IoT scoped |
| EN IEC 62443-4-2:2019 (CR 7.1, CR 7.2) | DoS protection; resource usage limitation to prevent resource exhaustion | IACS-specific |

**Overall gap:** General availability principles are covered for data centre infrastructure (ISO/IEC 22237-1) and end-to-end network security (ITU-T X.805). More detailed implementation guidance for generic user products is lacking. IoT-specific coverage (EN 303 645) remains at a high level.

---

### Requirement 3g — Minimise negative impact on availability of other devices/networks

> *Minimise their own negative impact on the availability of services provided by other devices or networks.*

**Core concepts:** network saturation; connection limits; timeouts; exception handling

**Lifecycle stages:** Design, Implementation

| Standard | Coverage | Gap |
|---|---|---|
| ETSI EN 303 645 (5.6, 5.9, 5.13) | System resilience; minimising unnecessary exposure; orderly network connections; input data validation | Does not specifically focus on minimising interference with other services; provisions on network saturation, connection limits and exception handling not fully addressed |
| ITU-T Y.4810 (Section 9.5) | Limits data transfer function to explicit user permission; anti-interference capability between IoT device and network equipment | Limited to data transfer and radio interference for IoT devices only |

**Overall gap:** This requirement is covered only by IoT-focused documents, and even within those the coverage is limited to a small number of high-level provisions. Broader applicability across product types is not addressed.

---

### Requirement 3h — Limit attack surfaces

> *Be designed, developed and produced to limit attack surfaces, including external interfaces.*

**Core concepts:** hardware hardening; tamper-resistance; system and software hardening; minimising interfaces and API entry points; security by design

**Lifecycle stages:** Design, Implementation, Validation

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC TS 19249:2017 | Catalogue of security design principles including attack surface minimisation; concrete application examples | Descriptive; does not include a concrete requirements list |
| ISO/IEC 15408-2:2022 | Security functional components; "Limited capabilities and availability" section defines requirements for least privilege and attack surface minimisation | Does not list concrete requirements |
| EN IEC 62443-4-2:2019 | Physical hardening requirements including tamper resistance, detection, and use of physical diagnostic and test interfaces | No dedicated attack surface minimisation requirement; IACS-specific |
| ETSI EN 303 645 (5.6) | Disabling unused interfaces; not unnecessarily exposing physical interfaces; secure development processes | Consumer IoT scoped; more specific provisions may be needed for other product categories |

**Overall gap:** This requirement is well covered theoretically; security design principles for attack surface minimisation are well described. However, concrete implementation requirements are lacking — IEC 62443-4-2 is a partial exception, but is IACS-specific.

---

### Requirement 3i — Reduce impact of incidents (exploitation mitigation)

> *Be designed, developed and produced to reduce the impact of an incident using appropriate exploitation mitigation mechanisms and techniques.*

**Core concepts:** defence in depth; encryption at rest; data minimisation; security by design; hardening; risk assessment; secure architecture; sandboxing

**Lifecycle stages:** Design, Implementation, Validation

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 27001:2022 | Systematic information security risk management | Does not cover specific technical measures for defence in depth, encryption at rest, or sandboxing |
| ISO/IEC 27002:2022 | Best practices for selecting and implementing security controls | High-level; may lack specifics on secure software design and hardening |
| ISO/IEC 27034-1:2011 | Secure development practices for software applications; supports defence-in-depth implicitly | Does not detail hardening and sandboxing; encryption at rest not specified; data minimisation not explicitly addressed |
| EN ISO/IEC 15408-3:2022 | Security evaluation criteria for IT products and systems | Focused on evaluation criteria, not specific mitigation mechanisms; useful for providing assurance that appropriate mechanisms are assessed by a lab |
| EN ISO/IEC 18045:2022 | Methodology for IT security evaluation; attack potential calculation to assess mitigation robustness | Focused on evaluation methodology, not specific mitigation mechanisms |
| ETSI EN 303 645 (5.4-1, 5.4-2, 5.3-7, 5.5-1, 5.6, 5.7) | Encryption at rest (partial); software integrity; encrypted communication; hardening by disabling unused interfaces and minimising code; secure management and best practice cryptography | Data minimisation not explicitly covered; secure architecture, sandboxing, secure environment not explicitly defined |
| IEC 62443-3-2:2020 | Security risk assessment and secure system design; network segmentation strategies; hardening via vulnerability identification and countermeasures | IACS-relevant; does not explicitly address encryption at rest, data minimisation, or sandboxing |

**Overall gap:** Solid foundation across the identified standards for secure system design, risk assessment, security evaluation and controls. Some aspects of defence in depth, sandboxing, and certain mitigation techniques are not explicitly covered by any identified standard.

---

### Requirement 3j — Security logging and monitoring

> *Provide security related information by recording and/or monitoring relevant internal activity, including the access to or modification of data, services or functions.*

**Core concepts:** logging; event monitoring; non-repudiation; intrusion detection; tamper-detection

**Lifecycle stages:** Design, Implementation, Validation, Surveillance/Maintenance

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 27002:2022 | Logging and monitoring activities; logging of events; protection of log information; examples of events to log and unauthorised changes | Guidance at high level; some examples provided |
| ISO/IEC 13888-1:2020 | Non-repudiation mechanisms using cryptographic techniques; generation of evidence for relevant events | More general logging aspects outside non-repudiation are not in scope |
| ETSI EN 303 645 (5.9-2, 5.9-3, 5.10-1, 5.11-1–4, 5.13-1) | Resilience provisions imply behavioural monitoring; telemetry data examination; data deletion implies tracking of data access/modification; input validation implies monitoring | Recording/monitoring of internal activity not explicitly required; no specific mandates for logging cybersecurity events or log protection from unauthorised modification |
| EN IEC 62443-4-2:2019 (CR 2.8, CR 2.11, CR 2.12) | Auditable events; timestamping of audit records; non-repudiation | IACS-specific |

**Overall gap:** Non-repudiation aspects are covered by ISO/IEC 13888-1. ISO/IEC 27002 provides a general high-level overview. EN 303 645 touches on telemetry and data integrity but does not explicitly mandate logging or log protection. EN 62443-4-2 covers this well but only for IACS.

---

### Requirement 3k — Security updates and user notification

> *Ensure that vulnerabilities can be addressed through security updates, including, where applicable, through automatic updates and the notification of available updates to users.*

**Core concepts:** patching; software updates; automatic updates; user notification; secure update functionality

**Lifecycle stages:** Design, Validation

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 27002:2022 | General patch management principles | Lacks specific guidance on automatic updates and user notifications |
| ISO/IEC 30111:2019 | Vulnerability handling processes | Does not address mechanisms for delivering and installing updates |
| ETSI EN 303 645 | Security updates; automatic updates; user notifications for consumer IoT | Lacks detailed guidance on secure mechanisms for installing/implementing updates |
| IEC 62443-2-1:2010 | Patch management and updates in IACS environments | IACS-specific; does not cover automatic updates or user notifications in detail |
| IEC 62443-4-2:2019 | Patch management and security updates for IACS components | IACS-specific; does not cover user notifications |

**Overall gap:** The identified standards focus on different aspects of vulnerability management, patching and updates. None explicitly cover all three sub-requirements (secure update mechanism + automatic update capability + user notification) together.

---

## Section 2: Vulnerability Handling Requirements

---

### VH Requirement 1 — SBOM and component documentation

> *Identify and document vulnerabilities and components contained in the product, including by drawing up a software bill of materials in a commonly used and machine-readable format covering at the very least the top-level dependencies of the product.*

**Core concepts:** Software Bill of Materials (SBOM); SPDX; CycloneDX; supply chain security; machine-readable; software dependencies

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 27036 (Parts 1–3) | Information security for supplier relationships; managing risks in supply chains and with third-party developers | Does not specifically address creation, management, or exchange of SBOMs |

**Supplementary initiatives to address gaps:**
- **SPDX** (Linux Foundation) — standard format for sharing software components, licenses, copyrights, and security data
- **CycloneDX** — SBOM specification for application security and supply chain component analysis
- **NTIA Software Component Transparency Initiative** — US initiative on SBOM formats and best practices
- **IIoTSBOM** — initiative from LSEC, Flanders Make and KU Leuven COSIC

**Overall gap:** Combining ISO/IEC 27036 with SPDX or CycloneDX provides the most comprehensive approach. No single ISO/IEC/ETSI standard comprehensively addresses SBOM creation and management.

---

### VH Requirement 2 — Address and remediate vulnerabilities without delay

> *In relation to the risks posed to the products with digital elements, address and remediate vulnerabilities without delay, including by providing security updates.*

**Core concepts:** security updates; CVSS; vulnerability management; vulnerability classification; timely remediation; third-party component updates

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 27001:2022 | Framework for managing information security risks including addressing vulnerabilities | Does not cover vulnerability classification, patch management for libraries/third-party components |
| ISO/IEC 27002:2022 | Vulnerability management controls including risk assessment, classification and remediation | Does not detail patch management procedures or third-party component handling specifically |
| EN ISO/IEC 30111:2020 | Vulnerability handling process; how to identify, analyse and remediate vulnerabilities; distributing security updates | Does not cover subscribing to CERT updates or maintaining third-party component libraries |
| EN ISO/IEC 29147:2020 | Vulnerability disclosure process; receiving and processing reports from CERTs and cybersecurity organisations | Focuses on disclosure; does not cover classification, remediation and patch management comprehensively |
| EN IEC 62443-4-1:2018 (SUM-1, SUM-5) | Timely delivery of security patches; security update qualification | IACS-specific; does not cover vulnerability classification or comprehensive patch management |

**Overall gap:** No single standard comprehensively covers all aspects — classification, remediation, patch management, CERT monitoring, and third-party component maintenance. A combination of ISO/IEC 30111 + ISO/IEC 29147 + ISO/IEC 27002 provides the best coverage.

---

### VH Requirement 3 — Effective and regular security testing

> *Apply effective and regular tests and reviews of the security of the product with digital elements.*

**Core concepts:** vulnerability assessment; CI/CD; risk assessment re-evaluation; security testing procedures

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 27001:2022 | Framework for managing information security risks including regular security reviews | Does not explicitly cover security testing procedures, CI/CD, or specific testing methodologies |
| ISO/IEC 27002:2022 | Security testing and vulnerability management controls; risk assessment and periodic reviews | Does not detail specific testing procedures, CI/CD techniques, or testing frequency/scope |
| ISO/IEC TS 27034-5-1:2018 | Security embedded in the software development lifecycle; regular security testing of applications | Focuses on application security; may not cover non-software products, hardware, or infrastructure |
| ISO/IEC 27005:2022 | Risk management guidelines including risk monitoring and review | Does not cover specific testing methodologies or CI/CD |

**Overall gap:** No single standard comprehensively covers all aspects of effective security testing, including specific methodologies, CI/CD integration and frequency/scope of testing. A DevSecOps-oriented combination of these standards is recommended.

---

### VH Requirement 4 — Public disclosure of fixed vulnerabilities

> *Once a security update has been made available, publicly disclose information about fixed vulnerabilities, including description, affected products, impacts, severity and remediation guidance.*

**Core concepts:** CVE; vulnerability disclosure; vulnerability analysis; public disclosure

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 29147:2020 | Guidelines for vulnerability disclosure; recommendations on nature of vulnerabilities, affected products, impacts, severity, remediation | Does not specify timeline for public disclosure or exact format for sharing information |
| EN ISO/IEC 30111:2020 | Vulnerability handling process; steps for investigation, resolution and public disclosure | Does not address disclosure for non-software products or hardware components in detail |
| ETSI EN 303 645 (5.2) | Means to manage reports of vulnerabilities; references ISO/IEC 29147; vulnerability disclosure policy content and timelines | Remains generic; timeline guidance no more precise than ISO/IEC 29147; IoT scoped |
| EN IEC 62443-4-1:2018 (DM-5) | Disclosure of fixed vulnerability information in a timely manner | IACS-specific |

**Supplementary references:** CVE (MITRE), NIST National Vulnerability Database (NVD), FIRST VRDX SIG

**Overall gap:** Standards contribute to the process but do not comprehensively address specific disclosure timelines or exact format for sharing vulnerability information across product types. Industry best practices (CVE, NVD) fill part of the gap.

---

### VH Requirement 5 — Coordinated vulnerability disclosure (CVD) policy

> *Put in place and enforce a policy on coordinated vulnerability disclosure.*

**Core concepts:** CVD policy

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 29147:2020 | Guidelines for CVD policy; disclosure process, roles and responsibilities, communicating vulnerability information | Does not provide detailed implementation guidance for a CVD policy; not industry-specific |
| EN ISO/IEC 30111:2020 | Vulnerability handling processes; investigating, resolving and disclosing vulnerabilities in a coordinated manner | Does not specify enforcement of a particular national or EU CVD policy |
| ETSI EN 303 645 (5.2) | Vulnerability management; reference to ISO/IEC 29147; CVD in IoT context | Highlights successful CVD use in software industries but lacks IoT domain specifics; generic |

**Supplementary references:** NIST SP 800-61 Rev 2, FIRST VRDX SIG

**Overall gap:** Standards contribute to CVD policy development but do not comprehensively address enforcement or provide industry-specific guidance.

---

### VH Requirement 6 — Facilitate vulnerability information sharing; contact address

> *Take measures to facilitate the sharing of information about potential vulnerabilities in their product with digital elements as well as in third party components, including by providing a contact address for the reporting of vulnerabilities.*

**Core concepts:** PSIRT; discovered vulnerabilities; contact point; CERT/CSIRT notification

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 29147:2020 | Guidelines for establishing communication channels for vulnerability reporting; roles and responsibilities for sharing vulnerability information | Does not specifically address sharing of information about third-party component vulnerabilities |
| EN ISO/IEC 30111:2020 | Vulnerability handling; investigating, resolving and disclosing vulnerabilities | Focused on software products; does not comprehensively cover third-party components and other digital elements |

**Supplementary references:** FIRST PSIRT Services Framework, ENISA CSIRTs Network, NIST SP 800-61 Rev 2

**Overall gap:** Standards do not comprehensively address sharing information about third-party component vulnerabilities. Collaboration with national CERTs/CSIRTs and ENISA is recommended to fill the gap.

---

### VH Requirement 7 — Secure update distribution mechanisms

> *Provide for mechanisms to securely distribute updates for products with digital elements to ensure that exploitable vulnerabilities are fixed or mitigated in a timely manner.*

**Core concepts:** code signing certificate; hashing; secure software update distribution; digital signatures; official distribution channel; hash publication

| Standard | Coverage | Gap |
|---|---|---|
| ISO/IEC 27002:2022 | Secure software distribution; cryptographic controls; securing distribution channels; update management | Does not explicitly address requirement to publish update hashes and provide verification instructions |
| IEC 62443-4-1:2018 | Secure product development lifecycle; security requirements covering design, implementation, testing and maintenance; patch management aspects | IACS-specific; does not explicitly address code signing certificates or hash publication; industry specificity limits coverage |

**Supplementary references:** NIST SP 800-53, NIST SP 800-63B, OWASP SSDLC, EU Cybersecurity Certification (EUCC) patch management mechanism

**Overall gap:** The identified standards do not comprehensively cover the publication of update hashes and the provision of verification instructions. Code signing certificate requirements are not explicitly mandated.

---

### VH Requirement 8 — Free and timely security patches with advisory messages

> *Ensure that, where security patches or updates are available to address identified security issues, they are disseminated without delay and free of charge, accompanied by advisory messages providing users with relevant information, including on potential action to be taken.*

**Core concepts:** security update notice; free updates; user notification methods

| Standard | Coverage | Gap |
|---|---|---|
| EN ISO/IEC 30111:2020 | Guidelines for timely dissemination of security patches and advisories | Does not explicitly address providing updates free of charge or specific user notification methods |
| ISO/IEC 27002:2022 | Technical vulnerability management; timely application of patches | Does not provide guidance on free updates or specific notification methods |
| EN IEC 62443-4-1:2018 (DM-5, SUM-5) | Disclosing security-related issues; timely delivery of security patches | IACS-specific; does not explicitly require security updates to be free of charge |

**Overall gap:** Existing standards provide guidance on vulnerability management and patch dissemination but do not explicitly address the requirement for free-of-charge updates or specific user notification methods. Policy-level mandates are needed to cover the full requirement.

---

## Overall Findings

1. **No single standard covers all CRA requirements.** Every identified standard covers some but not all requirements. Combinations are always necessary.

2. **"Horizontal" standards** (not sector-specific) emerged as the most universally relevant — particularly EN ISO/IEC 27002, EN ISO/IEC 30111, and EN ISO/IEC 29147.

3. **ETSI EN 303 645** has the broadest coverage of security property requirements (Req 1 through 3k) but is scoped to consumer IoT. Its applicability to other product categories is not automatic.

4. **EN IEC 62443 family** offers strong coverage but is scoped to Industrial Automation and Control Systems (IACS).

5. **For vulnerability handling**, EN ISO/IEC 30111 covers 5 of 8 requirements and EN ISO/IEC 29147 covers 4 — these are the primary standards for that section.

6. **Hardware design** is consistently less well covered than software across all requirements.

7. **Gaps consistently identified:** key management; specific disclosure timelines and formats; secure update mechanisms (code signing, hash publication); CI/CD and DevSecOps testing; sandboxing and secure environment specifics; SBOM creation standards.

---

## Key Standards Referenced

| Standard | Full Title | Most Relevant For |
|---|---|---|
| ETSI EN 303 645 | Cyber Security for Consumer IoT: Baseline Requirements | Security property requirements (all) |
| EN ISO/IEC 27002:2022 | Information security controls | Req 1, 3a, 3f, 3i, 3j, 3k; VH 2, 3, 7, 8 |
| EN ISO/IEC 30111:2020 | Vulnerability handling processes | VH 2, 3, 4, 5, 6, 8 |
| EN ISO/IEC 29147:2020 | Vulnerability disclosure | VH 4, 5, 6 |
| EN IEC 62443-4-1:2018 | Secure product development lifecycle (IACS) | Req 1, 2; VH 2, 4, 7, 8 |
| EN IEC 62443-4-2:2019 | Technical security requirements for IACS components | Req 3b, 3c, 3d, 3f, 3h, 3j, 3k |
| ISO/IEC 27001:2022 | Information security management systems | Req 3i; VH 2, 3 |
| ISO/IEC 27701:2019 | Privacy information management (extension to 27001/27002) | Req 3e |
| ISO/IEC 18045:2022 | Methodology for IT security evaluation (Common Criteria CEM) | Req 2, 3i |
| ISO/IEC 15408-2:2022 | Evaluation criteria for IT security — Security functional components | Req 3h |
| ISO/IEC 27036 (Parts 1–3) | Cybersecurity — Supplier relationships | VH 1 |
| ISO/IEC 27005:2022 | Information security risk management | Req 1; VH 3 |
| EN IEC 62443-3-2:2020 | Security risk assessment for IACS system design | Req 1, 3i |

---

*Based on: JRC & ENISA, Cyber Resilience Act Requirements Standards Mapping, EUR 31892 EN, 2024. CC BY 4.0.*
