# Build Plan: CareLedger 2026

## Overview

By 2026, CareLedger is a B2B SaaS platform for mid-market self-insured employers (75–300 employees) that makes elective procedure costs transparent and shoppable in real time. Employees get an AI-powered chat interface to compare prices across local providers; employers get a dashboard showing actual savings against baseline spend. The platform works because price transparency data is now federally mandated and machine-readable—the data acquisition problem that killed the original company no longer exists.

The market shift is structural: CMS price transparency rules (effective 2021–2024) have flooded the market with standardized pricing data. Employers are desperate to control procedure costs without restricting choice. CareLedger wins by being the first to combine that public data with a frictionless employee experience and a flexible revenue model—either flat PEPM ($3–$8/employee/month) or shared savings (25–30% of verified reductions). No long sales cycles, no custom integrations, no network effects dependency. Just plug into Turquoise Health's API, launch the navigator, and measure savings month one.34:T772,

## Why Now?

The single most important change since CareLedger's 2015 failure is the elimination of its core data acquisition problem through federal mandate. The Consolidated Appropriations Act of 2021 and CMS hospital price transparency rules (effective January 2021) now legally require hospitals and insurers to publish machine-readable price files covering negotiated rates, cash prices, and payer-specific allowed amounts. CareLedger spent its entire $120,000 trying to manually negotiate and estimate the pricing data that is now publicly available by law. That structural barrier is gone.

Layered on top of this, API-first healthcare data companies have commoditized provider network intelligence. Turquoise Health and Ribbon Health now offer normalized, structured procedure pricing and quality data via API — meaning a rebuilt CareLedger can license in weeks what the original team would have spent months building from scratch, at a fraction of the cost.

The employer market has also matured in CareLedger's favor. KFF's 2023 Employer Health Benefits Survey reports that 65% of covered US workers are now in self-insured plans, up from approximately 61% in 2015. More importantly, HR benefits buyers in 2026 are fluent in reference-based pricing, direct contracting, and shared-savings models — concepts that required significant education in 2015. Transcarent (raised $200M+) and Accolade (NASDAQ: ACCD) have spent hundreds of millions of dollars validating that self-insured employers will pay for exactly this value proposition.

Finally, GPT-4 (March 2023) and its successors have made it possible to replace the implicit manual concierge layer in CareLedger's original model with an AI-powered benefits navigation assistant — dramatically reducing cost-per-case and making the unit economics viable at employer sizes of 50–200 employees that CareLedger could never have served profitably.

---

## Current Market Analysis

The US employer-sponsored healthcare market was approximately $700 billion annually in 2015; KFF estimates total employer and worker premium contributions exceeded $900 billion in 2023, with self-insured plan spending representing the majority of that figure. The specific segment CareLedger targeted — elective ambulatory procedures for self-insured employers — has grown proportionally, though a precise current TAM figure for this sub-segment is not publicly available. CareLedger's original $90B TAM claim methodology was never disclosed and should not be assumed accurate.

## Competition map:

- **Transcarent** (raised $200M+, founded 2020): Targets large employers (1,000+ employees) with a broad health navigation platform. Weakness: minimum employer size effectively excludes the 50–500 employee market; pricing reflects enterprise complexity.
- **Accolade (NASDAQ: ACCD)**: Full-service health advocacy platform. Weakness: high PEPM costs ($15–$30+, per public analyst estimates) make it inaccessible to mid-market employers; product breadth creates implementation friction.
- **Quantum Health**: Strong in large self-insured market. Weakness: legacy technology stack, long implementation timelines, no AI-native interface.
- **Castlight Health** (now merged with Transcarent): Effectively absorbed; no longer an independent competitor.
- **Sana Benefits / Angle Health**: Modern carriers targeting SMBs but focused on plan design, not procedure-level cost steering.

**The gap:** No current competitor credibly serves self-insured employers in the 50–500 employee range with a procedure-level, AI-assisted cost-steering product at a price point those employers can absorb. This is the exact segment CareLedger was too underfunded to reach — and it remains structurally underserved in 2026.

**Demand signals:** The growth of health-sharing ministries, level-funded plans, and direct primary care adoption among SMBs signals that smaller employers are actively seeking cost-reduction tools outside traditional insurance structures.

---

## Recommended MVP

### Feature 1 — AI-Powered Procedure Cost Navigator

An employee-facing chat interface, built on GPT-4o (released May 2024) or Claude 3.5 Sonnet (June 2024), that accepts a procedure name or referral description in plain language and returns a ranked list of local providers with price estimates, quality signals, and estimated out-of-pocket cost under the employer's specific plan. This replaces the manual concierge layer CareLedger's original model implicitly required, reducing cost-per-interaction to near zero. The original CareLedger required human coordination to match employees to providers; this feature makes that process self-serve and instant.

## Feature 2 — Transparent Pricing Engine via API

A backend pricing layer that ingests machine-readable price files from Turquoise Health's API and CMS transparency data to populate real negotiated rates for 200+ high-frequency elective procedures across a target employer's geography. This is the feature CareLedger could not build in 2015 without manual provider negotiations; it now takes weeks to implement via licensed data. Initial launch will cover the 20 highest-volume elective procedures (colonoscopy, MRI, CT scan, outpatient surgery, lab panels) rather than the aspirational 600+ CareLedger claimed.

## Feature 3 — Employer Savings Dashboard

A real-time employer-facing dashboard showing projected vs. actual procedure spend, employee utilization of the navigator, and cumulative savings against the employer's baseline. This directly enables the shared-savings revenue conversation and gives HR buyers the reporting artifact they need to justify renewal. CareLedger had no documented reporting layer; this feature makes the value proposition auditable.

## Feature 4 — Hybrid Revenue Toggle (PEPM + Shared Savings)

A configurable billing module that allows employers to choose a flat PEPM fee ($3–$8/employee/month) or a shared-savings model (25–30% of verified savings). This directly addresses CareLedger's fatal flaw: the pure performance model deferred all revenue past the point of survival. PEPM generates cash at contract signing; shared savings rewards scale.

**What we will NOT build:** insurance plan replacement, a proprietary provider credentialing network, a claims processing engine, or a mobile app at launch. No telehealth, no PBM integration, no wellness programs.

**Success metrics:** 5 signed employer contracts within 6 months of launch; $15,000+ MRR within 9 months; measurable employee utilization rate of ≥20% among eligible employees within 12 months; average verified procedure savings of ≥25% vs. employer baseline.

---

## Go-to-Market Strategy

**Target customer:** Self-insured employers with 75–300 employees, level-funded or fully self-insured, in markets with high procedure price variance (Texas, Florida, Tennessee, and the Carolinas — states with documented wide price dispersion per CMS transparency data). Specifically, companies using third-party administrators (TPAs) like Trustmark, BenefitMall, or regional TPAs who are already familiar with reference-based pricing and are actively seeking add-on cost-reduction tools. HR directors and CFOs at these companies are the buyers; they have direct P&L exposure to claims costs and no dedicated benefits analytics team.

**Primary distribution channel:** TPA and benefits broker partnerships. Rather than direct employer sales — which replicates CareLedger's fatal 6–18 month sales cycle problem — the rebuilt CareLedger sells through TPAs and independent benefits brokers who already have trusted relationships with target employers and influence over annual plan design decisions. Brokers earn a referral fee or revenue share; TPAs bundle CareLedger as a value-add to their existing clients. This channel compresses the sales cycle from 12+ months to 60–90 days and eliminates cold outreach costs. Target: 3 signed TPA or broker distribution agreements before first employer contract.

**Pricing:** Default to PEPM at $5/employee/month for employers under 150 lives; offer shared-savings toggle (28% of verified savings) for employers over 150 lives who prefer performance alignment. PEPM generates immediate, predictable revenue at contract signing — the structural fix CareLedger needed. At $5 PEPM, a 100-employee employer generates $6,000/year; 50 such employers generates $300,000 ARR, sufficient to demonstrate product-market fit for a Series A conversation.

**Differentiation vs. 2026 competitors:** Transcarent and Accolade require enterprise-scale employers and charge enterprise-scale prices. The rebuilt CareLedger wins on segment fit (50–300 employees), speed to value (AI-native, no implementation project), and pricing accessibility. The AI navigator is the product-level differentiator — no current competitor in the SMB self-insured segment offers a conversational, employee-facing procedure cost tool integrated with live CMS transparency data.
