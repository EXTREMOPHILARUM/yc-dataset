# Build Plan: Opkit 2026

## Overview

By 2026, Opkit is a self-serve API for outbound healthcare verification calls—insurance eligibility, prior auth status, prescription coverage—built specifically for virtual-first specialty clinics (weight management, mental health, GLP-1 practices). The product is narrowly focused, deeply integrated, and priced on usage: $0.45 per call, no setup tax, no human handoff required.

The market shift is simple: voice AI is now reliable enough to work without a human fallback. The original Opkit needed humans to catch failures; the rebuilt version doesn't. That changes the unit economics entirely—verification calls that cost $3–5 with a human safety net now cost $0.45 fully automated. Virtual clinics with thin margins and high call volume win immediately.

Distribution is direct: Canvas Medical's app directory and Hint Health's partner network give you 3,000+ target customers without a sales team. The go-to-market is self-serve onboarding, transparent pricing, and a 90-day target of 10 paying clinics. You win by being the only vendor that works out of the box for this segment—no IVR mapping, no compliance theater, just API calls that work.34:T9d3,

## Why Now?

The single most important change since Opkit's failure: production-grade voice AI is now reliable enough to eliminate the human-in-the-loop fallback as a structural cost center.

When Opkit built its AI call center in 2024, the human escalation layer was not a product choice—it was an engineering necessity. Accent recognition failures, IVR navigation errors, and multi-turn dialogue breakdowns were frequent enough that a human fallback team was operationally required. That constraint directly compressed margins and made the path to venture-scale gross margins longer than available runway allowed.

By 2026, that constraint is materially weaker. GPT-4o (May 2024) introduced real-time audio processing with sub-300ms latency. ElevenLabs' v3 voice synthesis (2025) produces speech indistinguishable from human agents in blind tests, per the company's published benchmarks. Deepgram's Nova-3 model (2025) achieves word error rates below 5% on medical terminology and diverse accents—the specific failure mode Callaway cited publicly. Combined, these three components now handle the majority of insurance carrier IVR trees and multi-turn verification calls without human intervention. The human fallback can be retained as a genuine edge-case safety net rather than a primary operational channel, restoring the unit economics of a software business.

Additional structural tailwinds are now in place. HIPAA-compliant managed infrastructure—AWS HealthLake, Google Cloud Healthcare API, Azure Health Data Services—is available off the shelf, eliminating the compliance engineering burden that contributed to Opkit's 18-month gap between founding and public launch. The US telehealth market has normalized post-COVID into a stable cohort of virtual-first specialty clinics with multi-year operating histories and demonstrated willingness to pay for administrative automation. This is a more mature, more closeable buyer than existed in 2021.

Market data on the RCM automation segment specifically is not publicly available at the sub-segment level; the broader RCM market is estimated at $240B+ annually (CAQH 2023 Index), with phone-based administrative transactions representing a disproportionate share of manual cost.

Distribution channels unavailable to Opkit now exist: the athenahealth Marketplace, Hint Health's partner ecosystem (serving 3,000+ direct primary care practices), and the Canvas Medical app directory provide direct access to virtual-first clinic operators without cold outbound.

---

## Current Market Analysis

### Market Size

The US healthcare administrative cost burden attributable to phone-based transactions is large and structurally persistent. CAQH's 2023 Index estimates that the healthcare industry spends $350B annually on administrative transactions, with eligibility and benefit verification alone costing $11B per year—$9.5B of which remains manual. Phone calls are the dominant manual channel. This figure has grown since Opkit's 2021 founding, not shrunk, because payer incentives to adopt electronic alternatives remain absent. Specific market size data for the AI voice automation sub-segment is not publicly available as of this writing.

## Competition Map and Gaps

The competitive landscape has matured but remains fragmented:

- **Thoughtful AI** (formerly Thoughtful Automation): Raised $20M Series A in 2024. Targets hospital systems and large health networks. Weakness: enterprise sales cycles of 9–18 months; no self-serve or API offering for smaller practices.
- **Bland AI**: General-purpose voice AI platform, not healthcare-specific. Weakness: no HIPAA compliance, no payer IVR mapping, no medical terminology tuning. Requires significant customer-side configuration.
- **Vapi**: Developer-focused voice AI infrastructure. Weakness: same as Bland—horizontal platform with no vertical healthcare layer. Strong with engineers, weak with clinic operators.
- **11x ("Jordan")**: The Opkit acquirer's own product. Targets sales and business development calls, not healthcare back-office. Weakness: no RCM domain knowledge; Jordan is explicitly not positioned for insurance verification.
- **Availity / Change Healthcare**: Incumbent payer-provider networks. Weakness: built for large health systems; API access is expensive, slow to integrate, and not designed for virtual-first clinics.

**The gap**: No current competitor combines a healthcare-specific voice AI layer, a self-serve API for developer teams at virtual clinics, and pricing accessible to practices with under 500 patients. Flourish's testimonial—"We literally could not run our business without Opkit"—came from exactly this underserved segment.

## Demand Signals from Adjacent Products

Hint Health's 3,000+ direct primary care practices and the growth of GLP-1 virtual weight-loss clinics (Fella, Calibrate, Found) signal a large and growing cohort of virtual-first specialty practices actively seeking administrative automation. These clinics share a common profile: high call volume, small administrative staff, and no legacy EHR vendor relationship locking them into incumbent RCM tools.

---

## Recommended MVP

## Core Features

### Automated Insurance Verification Calls

The system initiates outbound calls to insurance carriers, navigates IVR trees, and returns structured eligibility and benefit data—coverage status, copay, deductible remaining, and prior authorization requirements—via webhook or dashboard. This is Opkit's original product, rebuilt on GPT-4o real-time audio and Deepgram Nova-3, which together eliminate the accent and IVR navigation failures that required human escalation. Unlike the original, this version targets sub-60-second call completion for standard verifications, making it viable for same-day scheduling workflows.

## Prescription and Prior Authorization Status Checks

The system calls pharmacy benefit managers and carrier prior authorization lines to retrieve prescription coverage status and PA approval states. This was a feature of Opkit's 2024 pivot that had no equivalent in the original product. It matters because GLP-1 medications—the primary driver of growth at virtual weight-loss clinics—require frequent PA checks that consume disproportionate staff time. This feature directly addresses the workflow of the target customer segment.

## Developer API with Structured Output

Every call type is accessible via a documented REST API returning JSON, with webhook support for async call completion. This preserves Opkit's strongest differentiator—the developer-first integration layer—and enables virtual clinic platforms (Canvas Medical, Elation Health) to embed verification natively. Unlike the original, the API will include pre-built payer IVR maps for the 50 largest US commercial insurers, reducing integration time for new customers from weeks to hours.

## What We Will NOT Build

- Inbound call handling or patient-facing voice agents (out of scope; different compliance and UX requirements)
- Billing, claims submission, or payment processing (adjacent but requires separate payer contracting)
- A proprietary human agent network (human fallback routes to customer's own staff via escalation webhook, not an Opkit-staffed team)

## Success Metrics

- 10 paying virtual-first specialty clinics within 90 days of launch
- Average call completion rate (no human escalation) ≥ 85% within 60 days of customer onboarding
- Net Revenue Retention ≥ 110% at 6 months (usage growth within existing accounts)
- Time-to-first-verification for new API customers ≤ 2 hours

---

## Go-to-Market Strategy

### Target Customer Segment

Virtual-first specialty clinics in weight management, mental health, and nutrition with 200–2,000 active patients, 2–10 administrative staff, and no existing RCM vendor contract. This is the exact profile of Opkit's validated beta customers—Fella and Flourish—and represents a segment large enough to generate meaningful revenue but narrow enough to close quickly. These clinics share a common payer mix (commercial insurance, GLP-1 PA-heavy), a common tech stack (Canvas Medical or Elation Health as EHR), and a common pain point: insurance verification and PA checks consuming 30–50% of administrative staff time.

## Primary Distribution Channel and Tactics

The Canvas Medical app directory and Hint Health partner ecosystem are the primary channels. Both provide direct access to the target segment without cold outbound. Tactics: (1) publish a native Canvas Medical integration that auto-triggers verification on appointment scheduling; (2) offer a 30-day free trial with no engineering required for Canvas customers; (3) sponsor the Direct Primary Care Coalition annual conference (attendance: ~800 clinic operators). Secondary channel: YC founder network referrals to virtual clinic founders in the S21–S24 batches.

## Pricing Strategy

Usage-based pricing at $0.45 per verification call and $0.08 per minute of call duration, with a $299/month platform fee that includes 500 verification calls. This positions the product below the cost of a single hour of administrative staff time per day while maintaining gross margins above 70% at scale (assuming GPT-4o API costs at current published rates; this should be modeled explicitly before launch). The platform fee creates predictable revenue and filters out low-volume customers unlikely to expand.

## Differentiation vs. 2026 Competitors

Against Bland AI and Vapi: pre-built payer IVR maps and HIPAA compliance out of the box—no configuration required. Against Thoughtful AI: self-serve onboarding and API access in under 2 hours, versus enterprise sales cycles. Against 11x: purpose-built for healthcare back-office, not sales calls—different regulatory posture, different payer domain knowledge, different buyer. The rebuild's core bet is that vertical depth in a single, structurally persistent workflow—insurance verification for virtual specialty clinics—is more defensible in 2026 than the horizontal AI voice platforms that have proliferated since Opkit's acquisition.
