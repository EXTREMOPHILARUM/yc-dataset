# Build Plan: PatientBank 2026

## Overview

The 2026 PatientBank targets personal injury law firms and insurance adjusters who need verified medical records to settle claims faster. Instead of chasing consumer fees, it operates as a B2B API layer that plugs directly into law firm case management systems and pulls structured records electronically from hospital networks via FHIR standards and interoperability networks like CommonWell.

The viability shift is regulatory: the 21st Century Cures Act's information-blocking rules now mandate electronic record sharing, meaning hospitals can no longer hide behind fax machines. The infrastructure PatientBank built in 2015 is finally legal and expected. This transforms the unit economics—no more manual labor bridging analog systems. API calls scale.

The go-to-market is vertical and immediate. Law firms lose thousands per case waiting for records. PatientBank charges per-case or monthly retainer, integrates in weeks, and wins by cutting claim resolution time from 60 days to 10. The market is ready, the regulations are enforced, and the friction is quantifiable in dollars.34:T809,

## Why Now?

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
