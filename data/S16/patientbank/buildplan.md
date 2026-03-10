# Build Plan: PatientBank 2026

## Overview

The 2026 PatientBank targets personal injury law firms and insurance adjusters who need verified medical records to settle claims faster. Instead of chasing consumer fees, it operates as a B2B API layer that plugs directly into law firm case management systems and pulls structured records electronically from hospital networks via FHIR standards and interoperability networks like CommonWell.

The viability shift is regulatory: the 21st Century Cures Act's information-blocking rules now mandate electronic record sharing, meaning hospitals can no longer hide behind fax machines. The infrastructure PatientBank built in 2015 is finally legal and expected. This transforms the unit economics—no more manual labor bridging analog systems. API calls scale.

The go-to-market is vertical and immediate. Law firms lose thousands per case waiting for records. PatientBank charges per-case or monthly retainer, integrates in weeks, and wins by cutting claim resolution time from 60 days to 10. The market is ready, the regulations are enforced, and the friction is quantifiable in dollars.34:T809,

## Why Now?

The single most important change since PatientBank's 2018 failure is the enforcement of the 21st Century Cures Act's information-blocking rules (effective April 2021), which legally mandate that healthcare providers expose patient data via standardized FHIR/HL7 APIs. This regulatory shift eliminates the fax-and-mail operational bottleneck that made PatientBank's per-transaction costs structurally unsustainable. The company that needed a physical fax machine and a 2.5-million-contact database to retrieve records can now be rebuilt as a pure software integration layer over mandated infrastructure.

Three additional infrastructure shifts compound this opportunity:

**API network coverage is now substantial.** The CMS Interoperability and Patient Access Final Rule (2020) requires Medicare and Medicaid payers to expose patient data via FHIR APIs, meaning insurance claims data — a reliable proxy for complete medical history — is programmatically accessible without hospital-by-hospital outreach. CommonWell Health Alliance and Carequality now connect thousands of U.S. health systems for electronic record exchange; a rebuilt PatientBank can join these networks as a participant rather than routing fax requests.

**Consumer behavior has been validated.** Apple Health Records (launched 2018, expanded through 2023) and CommonHealth (Android) have established that patients will aggregate medical records via FHIR APIs. PatientBank assumed this behavior in 2016; it now exists at scale.

**LLM-based document processing has matured.** GPT-4 (March 2023) and Claude 3 (March 2024) can extract structured clinical data — diagnoses, medications, lab values, dates — from unstructured PDF medical records with high accuracy. Manual curation that would have required expensive human labor in 2017 is now automatable.

The U.S. telehealth market grew from approximately $2B (2019) to approximately $28B (2023), per publicly cited industry estimates, normalizing digital health record management as a patient expectation rather than a novelty.

---

## Current Market Analysis

**Market size:** The U.S. medical records retrieval and management market was nascent and difficult to size discretely when PatientBank operated. The broader health information management market is estimated at approximately $33B globally in 2024 (source: Grand View Research — specific PatientBank-era comparison figure not available in the research report). The personal injury legal market alone — one of the highest-value B2B segments for medical records retrieval — processes hundreds of thousands of cases annually, with attorneys routinely paying $50–$200+ per record retrieval. Exact aggregate spend figures are not publicly documented.

## Current competitors and their specific weaknesses:

- **PicnicHealth** (still operating as of 2024): Consumer-focused, subscription model, strong on chronic disease management. Weakness: remains consumer-oriented with limited B2B infrastructure; does not target legal or insurance verticals at scale.
- **Datavant**: Enterprise health data connectivity platform. Weakness: built for large health system and pharma clients; inaccessible price point and sales cycle for mid-market legal firms or independent adjusters.
- **Ciox Health / Datavant (merged 2021)**: Dominant in ROI (Release of Information) for hospitals. Weakness: serves the hospital side of the transaction, not the requestor side; no patient-facing product.
- **Epic MyChart**: Covers records within a single health system. Weakness: cannot aggregate across systems — the exact gap PatientBank was built to fill.

**Demand signals from adjacent products:** The growth of telehealth platforms (Teladoc, Amazon Clinic) that require prior record access before consultations, and the expansion of direct-to-consumer genetic and lab testing (23andMe, Function Health), signal sustained consumer appetite for owning and sharing health data across providers.

---36:T81d,

## Recommended MVP

## Core Features:

**1. FHIR API-native record aggregation.** Connects to CommonWell, Carequality, and CMS payer APIs to pull structured patient records electronically, without fax or mail. This replaces PatientBank's entire operational infrastructure — the 2.5M contact database, the fax machine, the manual follow-up workflow — with software integrations. The original PatientBank absorbed analog costs linearly with volume; this version does not.

**2. LLM-powered record structuring and summarization.** Uses GPT-4o (May 2024) or Claude 3.5 (June 2024) to extract and normalize clinical data — diagnoses, medications, procedures, lab values, dates of service — from ingested records, including legacy PDFs from providers not yet on FHIR networks. Outputs a structured, searchable longitudinal record. PatientBank stored documents but could not make them queryable without expensive manual curation; this feature makes the stored record the core value asset.

**3. Attorney/adjuster request portal with bulk ordering and status tracking.** A B2B workflow layer that allows personal injury law firms, life insurance underwriters, and disability claims adjusters to submit, track, and receive structured record packages at scale. Includes HIPAA-compliant patient authorization collection via e-signature. PatientBank built consumer authorization flows; this repurposes that infrastructure for institutional buyers with high willingness to pay and recurring volume.

**4. Residual fax/mail fallback with cost transparency.** For the minority of providers not yet reachable via FHIR networks, the system routes requests through automated fax (via eFax or similar API) and flags estimated fulfillment time and cost to the requesting party. This is not the primary workflow — it is an explicit fallback with visible unit economics, not a hidden operational cost.

**What we will NOT build:** Consumer-facing per-record fee product. Patient-owned personal health record vault as a primary use case. Hospital scorecard or content marketing infrastructure. Native mobile app in the MVP phase.

## Success metrics:

- 10 paying B2B customers (law firms or insurers) within 90 days of launch
- Average revenue per customer ≥ $2,000/month
- ≥ 70% of record requests fulfilled via FHIR API (not fax fallback) within 6 months
- Gross margin ≥ 60% per fulfilled request batch by month 6

---

## Go-to-Market Strategy

**Target customer segment:** Personal injury law firms with 5–50 attorneys, operating in states with high litigation volume (California, Florida, Texas, New York). These firms request medical records on every active case, pay $50–$200+ per retrieval through incumbent services (Ciox, independent ROI companies), and have a paralegal or case manager whose job includes record chasing. They have recurring, predictable volume, institutional willingness to pay, and no loyalty to current vendors beyond switching cost. This is the segment PatientBank identified early via its Yale-New Haven relationship but abandoned for consumer growth — the rebuild starts here.

**Primary distribution channel and tactics:** Direct outbound sales to law firm operations managers and paralegals via LinkedIn Sales Navigator, targeting firms with active personal injury practice pages. Secondary channel: partnerships with legal practice management software platforms (Clio, MyCase) that have established law firm distribution. Clio alone serves over 150,000 legal professionals (per Clio's published figures); an app integration surfaces the product at the point of workflow.

**Pricing strategy:** Monthly subscription per seat ($199–$399/month per paralegal user) plus a per-request fee for fax fallback fulfillment only ($15–$25, cost-plus). FHIR-fulfilled requests are included in the subscription. This model inverts PatientBank's fatal flaw: the subscription creates predictable revenue, the per-request fee only applies to the genuinely costly analog fallback, and gross margin improves as FHIR network coverage expands. Pricing is justified by the $50–$200+ incumbents charge per record on a pure per-transaction basis.

**Differentiation vs. 2026 competitors:** Datavant and Ciox serve hospitals, not requestors. PicnicHealth serves consumers, not legal professionals. No current competitor combines FHIR-native retrieval, LLM-powered structuring, and a B2B workflow portal purpose-built for legal and insurance use cases. The rebuilt PatientBank's moat is the combination of regulatory tailwinds (mandated API access), AI-powered structuring (making records actionable, not just stored), and a distribution wedge through legal software integrations that incumbents have not prioritized.
