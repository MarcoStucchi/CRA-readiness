---
title: "Cyber Resilience Act – Annex I: Essential Cybersecurity Requirements"
source: "Regulation (EU) 2024/2847, OJ L 2024/2847, 20.11.2024"
official_text: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R2847"
version: "Final – adopted 23 October 2024"
document: "Regulation (EU) 2024/2847 of the European Parliament and of the Council"
section: "Annex I"
supersedes: "Annex I of COM(2022) 454 (proposal, 15.9.2022)"
keywords:
  - Cyber Resilience Act
  - CRA
  - cybersecurity
  - EU regulation
  - essential requirements
  - product security
  - vulnerability handling
  - SBOM
retrieved: "2026-05-13"
---

# Annex I – Essential Cybersecurity Requirements

> **Regulation (EU) 2024/2847 – adopted 23 October 2024, in force 10 December 2024**

> **Changes from the 2022 proposal:** Part I expanded from 11 to 13 sub-requirements under point (2); notably added: security updates by design, security logging with user opt-out, and secure data deletion. Part II substantively revised: SBOM must now be registered in a public vulnerability database (EUVD or equivalent); CVD policy now explicit; security updates must remain available for a minimum of 10 years after issue.

---

## Part I – Cybersecurity Requirements Relating to the Properties of Products with Digital Elements

(1) Products with digital elements shall be designed, developed and produced in such a way that they ensure an appropriate level of cybersecurity based on the risks, and delivered without any known exploitable vulnerabilities.

(2) On the basis of the cybersecurity risk assessment referred to in Article 13(3) and where applicable, products with digital elements shall:

(a) be delivered with a secure by default configuration, including the possibility to reset the product to its original state;

(b) ensure protection from unauthorised access by appropriate control mechanisms, including but not limited to authentication, identity or access management systems, and report on and protect against unauthorised access attempts;

(c) protect the confidentiality of stored, transmitted or otherwise processed data, personal or other, such as by encrypting relevant data at rest or in transit by state of the art mechanisms;

(d) protect the integrity of stored, transmitted or otherwise processed data, personal or other, commands, programs and configuration against any manipulation or modification not authorised by the user, as well as report on corruptions;

(e) process only data, personal or other, that are adequate, relevant and limited to what is necessary in relation to the intended use of the product ('minimisation of data');

(f) protect the availability of essential functions, including the resilience against and mitigation of denial of service attacks;

(g) minimise their own negative impact on the availability of services provided by other devices or networks;

(h) be designed, developed and produced to limit attack surfaces, including external interfaces;

(i) be designed, developed and produced to reduce the impact of an incident using appropriate exploitation mitigation mechanisms and techniques;

(j) provide security related information by recording and/or monitoring relevant internal activity, including the access to or modification of data, services or functions, with the possibility for the user to disable this recording and/or monitoring function;

(k) ensure that vulnerabilities can be addressed through security updates, including through automatic updates that are enabled by default, with a clear notification to users when updates are available and the possibility to install them easily;

(l) ensure that when a security patch or update is available, it is disseminated without delay and free of charge, accompanied by advisory messages providing users with the relevant information, including on potential action to be taken;

(m) provide users with the possibility to permanently and securely delete personal data and, where applicable, other data, including after the support period.

---

## Part II – Vulnerability Handling Requirements

Manufacturers of products with digital elements shall:

(1) identify and document vulnerabilities and components contained in the product, including by drawing up a software bill of materials in a commonly used and machine-readable format covering at the very least the top-level dependencies of the product, and register it in the European vulnerability database referred to in Article 12 of Directive (EU) 2022/2555 or another publicly accessible vulnerability database;

(2) in relation to the risks posed to the products with digital elements, address and remediate vulnerabilities without undue delay, including by providing security updates that are, where technically possible, separated from functionality updates; when a security update is available, manufacturers shall disseminate it without delay;

(3) apply effective and regular tests and reviews of the security of the product with digital elements;

(4) once a security update has been made available, publicly disclose information about fixed vulnerabilities, including a description of the vulnerabilities, information allowing users to identify the affected product, the impacts, the severity, and information helping users to remediate the vulnerabilities; where the manufacturer has decided not to address a vulnerability, it shall publicly disclose this decision together with the reasoning;

(5) put in place and enforce a policy on coordinated vulnerability disclosure;

(6) take measures to facilitate the sharing of information about potential vulnerabilities in their product with digital elements as well as in third party components contained in that product, including by providing a contact address for the reporting of the vulnerabilities discovered in the product;

(7) provide for mechanisms to securely distribute updates for products with digital elements, including through automatic updates or notifications guiding users on how to install security updates, to ensure that exploitable vulnerabilities are fixed or mitigated in a timely manner;

(8) ensure that, where security patches or updates are available to address identified security issues, they are disseminated without delay and free of charge, and that each security update made available during the support period remains available for a minimum of 10 years from its issue date or for the remainder of the support period, whichever is longer.
