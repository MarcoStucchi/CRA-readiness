---
title: "Cyber Resilience Act – Main Body: Regulation (EU) 2024/2847"
source: "https://digital-strategy.ec.europa.eu/en/policies/cra-summary"
official_text: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R2847"
proposal: "COM(2022) 454 – 15.9.2022"
adopted: "23 October 2024"
published: "20 November 2024 – OJ L 2024/2847"
in_force: "10 December 2024"
fully_applicable: "11 December 2027"
document: "Regulation (EU) 2024/2847 of the European Parliament and of the Council"
amends:
  - "Regulation (EU) No 168/2013"
  - "Regulation (EU) 2019/1020 (Market Surveillance)"
  - "Directive (EU) 2020/1828"
keywords:
  - Cyber Resilience Act
  - CRA
  - cybersecurity
  - products with digital elements
  - EU regulation
  - CE marking
  - vulnerability handling
  - conformity assessment
  - market surveillance
  - ENISA
retrieved: "2026-05-13"
---

# Cyber Resilience Act – Main Body Summary

> **Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024**  
> On horizontal cybersecurity requirements for products with digital elements.  
> Legal basis: Article 114 TFEU (internal market).

> **Note on the proposal vs. the adopted text:** The Commission originally published the CRA as proposal **COM(2022) 454** on 15 September 2022, accompanied by **Annexes 1 to 6** (the document already extracted in the companion markdown files). Following trilogues between the Parliament, Council and Commission, the final adopted text — **Regulation (EU) 2024/2847** — was published on 20 November 2024. The adopted regulation contains **8 Annexes** (vs. 6 in the proposal), reflecting structural changes made during the legislative process. The relationship between the main body and the annexes is described at the end of this file.

---

## Purpose and Context

The CRA is a **horizontal regulatory framework** establishing mandatory cybersecurity requirements for all hardware and software products ("products with digital elements") placed on the EU market whose intended or foreseeable use includes a direct or indirect logical or physical data connection to a device or network. It addresses two root problems:

- widespread and insufficiently remediated **vulnerabilities** in digital products;
- **insufficient and inconsistent provision of security updates** throughout the product lifecycle.

The CRA introduces a duty of care running from product design through to end of support, placing primary responsibility on **manufacturers** and ensuring users have adequate information to make informed choices. Products that meet its requirements bear the **CE marking**.

---

## Key Definitions (Article 3)

**Product with digital elements:** A software or hardware product and its remote data processing solutions, including components placed on the market separately.

**Remote data processing:** Data processing at a distance for which the software is designed by the manufacturer, whose absence would prevent the product from performing one of its functions.

**Manufacturer:** Any natural or legal person who develops or manufactures products with digital elements and markets them under their name or trademark, whether for payment, monetisation or free of charge.

**Open-source software steward:** A legal person (not a manufacturer) that systematically and sustainably supports the development of specific free and open-source software intended for commercial activities, and ensures the viability of those products.

**Importer:** A natural or legal person established in the Union who places on the market a product with digital elements bearing the name or trademark of a person established outside the Union.

**Distributor:** A natural or legal person in the supply chain (other than the manufacturer or importer) who makes a product available on the Union market without affecting its properties.

**Conformity assessment:** The process of verifying whether the essential cybersecurity requirements set out in Annex I have been fulfilled.

**Notified body:** A conformity assessment body designated under Article 43 and authorised to carry out third-party conformity assessments.

**Support period:** The period determined by the manufacturer during which vulnerabilities of the product with digital elements will be handled effectively. Must be proportionate to the expected use of the product and at minimum 5 years (unless the expected lifetime is shorter).

---

## Chapter I – General Provisions (Articles 1–12)

The CRA applies to all products with digital elements **made available on the market** whose intended or reasonably foreseeable use includes a data connection to a device or network. Products not made available on the market (not supplied in the course of a commercial activity) are out of scope.

**Exclusions from scope** include products already covered by sector-specific Union legislation with equivalent cybersecurity requirements (e.g. medical devices, aviation, motor vehicles, certain defence and national security products). Free and open-source software not placed on the market (non-monetised) is generally excluded.

The CRA operates in conjunction with other Union legislation, in particular:
- **Regulation (EU) 2019/1020** (market surveillance) — which applies to CRA products for general enforcement machinery;
- **NIS2 Directive (EU) 2022/2555** — which governs network and information security at the entity level;
- **Cybersecurity Act (EU) 2019/881** — whose certification schemes can be used to demonstrate CRA conformity.

---

## Chapter II – Obligations of Economic Operators (Articles 13–26)

### Manufacturer Obligations (Article 13)

Manufacturers bear the primary obligations of the CRA. Before placing a product on the market they must:

- perform a **cybersecurity risk assessment** covering design, development, production, delivery and maintenance;
- ensure the product meets the **essential cybersecurity requirements** set out in Annex I (security properties) and Annex I Part II (vulnerability handling);
- draw up **technical documentation** (see Annex VII) incorporating the risk assessment and the means chosen to implement requirements;
- carry out the applicable **conformity assessment procedure** (see Chapter III and Annex VIII);
- draw up the **EU declaration of conformity** and affix the **CE marking**;
- include with the product: type/batch/serial identification, name and contact details, and **user information and instructions** as set out in Annex II;
- determine and communicate a **support period** (minimum 5 years as a rule), clearly indicating its end date (month and year) at the time of purchase.

If third-party components are integrated, the manufacturer must exercise **due diligence** to ensure those components do not compromise the product's cybersecurity.

### Reporting Obligations (Article 14)

After placing the product on the market, manufacturers must notify **actively exploited vulnerabilities** and **severe incidents** affecting product security to:
- the CSIRT of the Member State of their main establishment; and
- **ENISA**, via the CRA Single Reporting Platform.

Deadlines:

| Notification type | Deadline |
|---|---|
| Early warning | 24 hours of becoming aware |
| Main notification | 72 hours |
| Final report (actively exploited vulnerability) | No later than 14 days after a corrective/mitigating measure is available |
| Final report (severe incident) | Within 1 month of the 72-hour submission |

Reporting obligations apply from **11 September 2026** and cover all products on the Union market, including those placed before 11 December 2027.

### Authorised Representative (Article 15)

A manufacturer may appoint an **authorised representative** by written mandate to perform specified tasks, including cooperation with market surveillance authorities.

### Importer Obligations (Article 19)

Importers must verify before placing a product on the market that:
- the manufacturer has complied with the essential cybersecurity requirements;
- vulnerability handling processes are in place;
- the appropriate conformity assessment has been carried out;
- the technical documentation has been drawn up;
- the product bears the CE marking.

Importers must not place non-compliant products on the market and must cooperate with market surveillance authorities.

### Distributor Obligations (Article 20)

Distributors must verify that products bear the CE marking, that manufacturers and importers have affixed their contact details, provided user information and indicated the support period. Distributors must not make non-compliant products available and must inform manufacturers of known vulnerabilities.

### Open-Source Software Stewards (Article 24)

A new economic actor introduced by the CRA. Open-source software stewards are required to:
- maintain a **cybersecurity policy** fostering secure development and effective vulnerability handling;
- cooperate with market surveillance authorities;
- report actively exploited vulnerabilities and severe incidents affecting their infrastructure.

Open-source software stewards are **not subject to penalties** for CRA infringements.

### Support for SMEs (Article 33)

Member States shall promote measures to support microenterprises and small and medium-sized enterprises (SMEs) in complying with the CRA, including regulatory sandboxes, guidance and dedicated training. The Commission shall publish guidance with a particular focus on facilitating SME compliance.

---

## Chapter III – Conformity Assessment (Articles 27–34)

### Presumption of Conformity (Article 27)

Products compliant with relevant **harmonised European standards** or **common specifications** benefit from a presumption of conformity with the essential requirements of Annex I.

### Conformity Assessment Procedures (Article 32)

The applicable procedure depends on the product category:

**Default products (approx. 90% of products):** The manufacturer may use **self-assessment** (Module A — internal control), draw up the EU declaration of conformity and affix the CE marking.

**Important products – Class I (Annex III):** Self-assessment is permitted only if the manufacturer has applied harmonised standards or common specifications; otherwise, **third-party assessment** via a notified body (Module B+C or Module H) is required.

**Important products – Class II (Annex III) and Critical products (Annex IV):** **Mandatory third-party assessment** via a notified body, or use of a European cybersecurity certification scheme where available and specified by the Commission.

Exception: manufacturers of important products (Class I and II) that are free and open-source software may use self-assessment, provided the technical documentation is made publicly available.

### EU Declaration of Conformity (Articles 28–29)

The manufacturer draws up the EU declaration of conformity (model in Annex V, simplified version in Annex VI) attesting that the product meets the essential requirements. A simplified declaration may be affixed to the product, with the full text available online.

### CE Marking (Article 30)

The CE marking must be affixed before placing the product on the market. It must be visible, legible and indelible. Where a notified body is involved (Module H), the notified body's identification number follows the CE marking.

### Technical Documentation (Article 31 + Annex VII)

Technical documentation must be drawn up before placing the product on the market and kept available for market surveillance authorities. It must contain at minimum the elements listed in Annex VII, including the cybersecurity risk assessment and the software bill of materials.

---

## Chapter IV – Notification of Conformity Assessment Bodies (Articles 35–51)

Member States must designate **notifying authorities** responsible for assessing, designating and notifying conformity assessment bodies (by **11 June 2026**). Conformity assessment bodies wishing to act as notified bodies must meet requirements including independence, impartiality and technical competence. Notification is made via the NANDO information system.

Notified bodies must carry out conformity assessments proportionately and with due account of the size of the undertaking, in particular for SMEs (including in relation to fees).

---

## Chapter V – Market Surveillance and Enforcement (Articles 52–60)

Each Member State must designate one or more **market surveillance authorities** to enforce the CRA. Enforcement builds on the framework of **Regulation (EU) 2019/1020** (market surveillance), which is explicitly made applicable to CRA products.

Market surveillance authorities may:
- provide guidance and advice to economic operators;
- evaluate products presenting a **significant cybersecurity risk**;
- require corrective or restrictive actions;
- coordinate with other Member States' authorities and carry out **joint sweeps**.

An **Administrative Cooperation Group (ADCO)** composed of national market surveillance authority representatives is established for uniform application of the CRA. ADCO may conduct Union-wide **dependency assessments** for specific product categories, including by requesting software bills of materials from manufacturers.

**Sanctions (Article 64):** Non-compliance can result in:
- fines up to **2.5% of global annual turnover** (or €15 million, whichever is higher) for violations of essential requirements;
- fines up to **2%** for other obligations (e.g. reporting);
- fines up to **1%** for providing incorrect information.

Microenterprises and small enterprises may not be fined for failures to meet the 24-hour reporting deadline.

---

## Chapter VI – Delegated Powers and Committee Procedure (Articles 61–62)

The Commission is empowered to adopt **delegated and implementing acts** to supplement the CRA (e.g. to specify product categories, cybersecurity certification schemes applicable for conformity, or reporting formats). Two implementing acts have already been adopted:

- **Commission Delegated Regulation (EU) 2025/1535** — exclusion from CRA scope for certain products under Regulation (EU) No 168/2013.
- **Commission Implementing Regulation (EU) 2025/2392** — technical descriptions of important and critical product categories (Annexes III and IV).

---

## Chapter VII – Confidentiality and Penalties (Article 63–65)

Rules on **confidentiality** apply to all parties involved in the application of the CRA. Penalties for infringements are laid down at national level, subject to the maxima in Article 64.

---

## Chapter VIII – Transitional and Final Provisions (Articles 66–71)

| Event | Date |
|---|---|
| Entry into force | 10 December 2024 |
| Notification of conformity assessment bodies | 11 June 2026 |
| Reporting obligations (Art. 14) | 11 September 2026 |
| Full applicability | 11 December 2027 |

Products placed on the market before 11 December 2027 are subject to the CRA only if, from that date, they undergo a **substantial modification**. Reporting obligations apply from 11 September 2026 to all products on the market, including those placed before 11 December 2027.

---

## Relationship Between the Main Body and the Annexes

The CRA main body operates through a system of **cross-references to its Annexes**, which carry the substantive technical and procedural content. The main body defines the framework, actors, obligations, conformity processes and enforcement powers; the Annexes supply the specific requirements and templates. Neither is self-sufficient without the other.

| Annex | Title | Role in the main body |
|---|---|---|
| **Annex I** | Essential Cybersecurity Requirements | The core technical standard. Referenced throughout Ch. II and III. Part I: product security properties. Part II: vulnerability handling obligations. Manufacturers must meet these; conformity assessment checks compliance against them. |
| **Annex II** | Information and Instructions to the User | Defines the minimum information to accompany every product. Referenced in Art. 13 (manufacturer obligations). |
| **Annex III** | Important Products with Digital Elements | Lists Class I and Class II important product categories. Determines which conformity assessment procedure applies (Art. 32). |
| **Annex IV** | Critical Products with Digital Elements | Lists critical product categories requiring mandatory third-party assessment or EU cybersecurity certification. Referenced in Art. 32. |
| **Annex V** | EU Declaration of Conformity | Provides the model structure for the full declaration. Referenced in Art. 28. |
| **Annex VI** | Simplified EU Declaration of Conformity | Provides the model for the simplified declaration that may be affixed directly to the product. Referenced in Art. 29. |
| **Annex VII** | Content of the Technical Documentation | Lists the minimum elements of the technical file the manufacturer must draw up. Referenced in Art. 31. |
| **Annex VIII** | Conformity Assessment Procedures | Specifies Module A (internal control), Module B+C (EU-type examination + conformity to type), and Module H (full quality assurance). Referenced in Art. 32. |

### Note on the proposal (COM(2022) 454) vs. the adopted text (Regulation 2024/2847)

The **Commission proposal of September 2022** contained **6 Annexes** (I–VI), which are the files already extracted in the companion markdown series (CRA_Annex_1.md through CRA_Annex_6.md). During the legislative process the structure was revised: the adopted regulation contains **8 Annexes**, with the declaration of conformity split into a full version (Annex V) and a simplified version (Annex VI), and the technical documentation content and conformity assessment procedures renumbered as Annexes VII and VIII respectively. The substantive content of the original 6 annexes is preserved and elaborated in the 8 final annexes.
