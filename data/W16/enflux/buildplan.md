# Build Plan: Enflux 2026

## Overview

Enflux was a Chicago-based smart apparel startup (2012–2020) that embedded ten IMU sensors into a compression shirt and pants to deliver real-time 3D body movement analysis and form coaching via smartphone — a genuinely differentiated product that died not from lack of demand but from a fatal mismatch between hardware complexity and seed-level funding, leaving the company unable to manufacture at scale against a competitor (Athos) with 200x its capital.

The rebuild thesis is not to repeat the hardware bet. Camera-based AI pose estimation and CMS reimbursement codes for remote therapeutic monitoring (RTM) have together created a path that Enflux never had: a software-first motion coaching product with near-zero COGS, sold into physical therapy clinics as a billable clinical tool, that can expand into consumer fitness once the revenue base funds hardware optionality. **The new Enflux is a software platform that turns any smartphone camera into a clinical-grade movement coach — and gets paid by insurers to do it.**

---34:Ta88,

## Why Now?

## Current Market Analysis

**Market size:** The U.S. physical therapy market was valued at approximately $46 billion in 2023 (Grand View Research), up from roughly $30 billion in 2016. The digital musculoskeletal (MSK) health market — the more specific segment — is harder to bound precisely; Hinge Health's $600M+ raise and $6B+ valuation at its 2024 IPO filing implies investors believe the addressable market is in the tens of billions. The RTM billing market specifically is nascent: the codes were introduced in 2022 and adoption is still accelerating, so precise market size data is not yet available from public sources.

## Competition map:

- **Hinge Health** — The dominant digital MSK platform, focused on employer and insurer channels with a sensor kit (wrist and thigh bands) plus exercise therapy app. Weakness: employer channel requires long sales cycles (6–18 months), minimum group sizes, and is inaccessible to individual PT clinics. Does not use camera-based pose estimation; its sensor kit is proprietary and adds hardware friction.
- **Kaia Health** — App-based MSK coaching using smartphone camera pose estimation (their primary differentiator). Weakness: focused on employer/insurer channel, not direct PT clinic integration; limited RTM billing support for individual practitioners.
- **Sword Health** — AI-powered physical therapy with a sensor kit. Weakness: enterprise-only channel, no individual clinic product, high implementation cost.
- **Vori Health** — Telehealth-first MSK, no wearable component. Weakness: physician-facing, not PT-facing; no movement capture.
- **Reflexion Health (VERA)** — Camera-based PT exercise monitoring, FDA-cleared. Weakness: expensive enterprise deployment model, limited to post-surgical rehab protocols, not general MSK coaching.

**The gap:** No current competitor combines (a) camera-based pose estimation, (b) RTM billing workflow built for individual PT clinics, and (c) a consumer fitness upsell path. Reflexion Health is the closest technical analog but is priced and positioned for hospital systems, not the 35,000+ independent PT clinics that represent the majority of outpatient PT volume.

**Demand signals from adjacent products:** Apple Watch's CoreMotion rep-counting (Series 9, 2023) and the rapid growth of AI fitness apps (Tempo, Tonal, Mirror — all using camera-based form feedback) confirm consumer willingness to engage with movement coaching technology. The failure of Mirror (sold to Lululemon for $500M in 2020, discontinued in 2023) is instructive: consumer hardware subscription models remain fragile, which reinforces the clinical-first strategy.

**Defensibility against platform incumbents:** Apple is the most credible threat. Apple Watch already counts reps and detects exercise type; Apple Vision Pro includes body tracking. However, Apple does not build clinical workflow software, does not pursue RTM billing integration, and does not sell into PT clinic EHR systems. The defensible layer is not the pose estimation (Apple will always win that arms race) — it is the clinical workflow, the RTM billing automation, and the longitudinal movement database built from clinical use. Google and Meta have no meaningful presence in PT clinic software. Amazon has no adjacent product. The honest caveat: if Apple builds a native RTM billing module into Health Records and opens pose estimation to PT clinics directly, the moat narrows significantly. The rebuild must move fast enough to own the clinical workflow layer before that happens.

---

## Recommended MVP

## Core Feature 1: Camera-Based Movement Assessment

Using MediaPipe Pose or Apple's Vision framework, the app captures a patient performing a standardized movement screen (squat, single-leg stance, overhead reach) via the PT clinic's existing iPad or iPhone. The system extracts joint angles, flags deviations from normative ranges, and generates a structured report. This replaces the ten-sensor garment entirely for the assessment use case — the original Enflux product required the patient to own and wear the garment; this requires only the clinic's existing device.

## Core Feature 2: RTM-Ready Home Exercise Monitoring

Between clinic visits, patients perform prescribed exercises at home using their own smartphone camera. The app records movement quality (not just completion), flags form deviations, and logs session data to the clinician dashboard. The system automatically generates the documentation required to support RTM billing under CPT codes 98975–98977 — specifically, the 16-day minimum monitoring threshold and the monthly treatment management note. This is the revenue engine: at ~$115–$130/month per patient in RTM reimbursement, a clinic with 50 active RTM patients generates $5,750–$6,500/month in new billable revenue. The original Enflux had no reimbursement pathway; this feature exists entirely because of the 2022 CMS codes.

## Core Feature 3: LLM-Powered Coaching Feedback

Structured pose data (joint angles, rep timing, asymmetry scores) is passed to GPT-4o via API to generate plain-language feedback for the patient ("your left knee is tracking inward on the descent — try cueing your knee toward your pinky toe") and a clinical summary for the PT. This replaces the 500-trainer labeling effort Enflux undertook. The feedback quality will not match a skilled PT's real-time observation, and the product should not claim otherwise — it is a between-session coaching layer, not a PT replacement.

**What we will NOT build:** A wearable garment (hardware-first is what killed Enflux; this is a software company until revenue justifies hardware optionality), a consumer direct-to-consumer fitness app (the B2C fitness app market is saturated and margins are thin), a VR/gaming SDK (Enflux's platform ambiguity was a strategic error; one vertical first), or a proprietary pose estimation model (MediaPipe and Apple Vision are good enough and free).

## Success metrics:

- 20 PT clinics live and billing RTM within 6 months of launch
- ≥60% of enrolled patients completing ≥16 days of monitoring per month (the RTM billing threshold)
- Clinic NPS ≥ 40 at 90 days
- Average revenue per clinic ≥ $2,000/month within 90 days of activation

**Cold-start problem:** This product does not depend on network effects or local density. Each clinic is an independent deployment. Value is delivered to the first patient on day one — the camera works, the RTM billing works, and the PT gets a report regardless of how many other clinics are using the platform. There is no cold-start problem in the traditional sense.

---

## Go-to-Market Strategy

**Target customer (narrow and specific):** Independent outpatient physical therapy clinics with 1–5 locations, 2–8 treating therapists, and an existing Medicare/commercial insurance patient panel. These clinics are actively looking for RTM revenue because the codes are new, reimbursement is real, and most have not yet implemented a compliant workflow. They are not served by Hinge Health or Sword Health (enterprise-only). There are approximately 35,000+ outpatient PT clinics in the U.S. (APTA data); the independent segment represents the majority.

**Primary distribution channel:** Direct outreach through PT professional associations (APTA state chapters, private practice section) and WebPT's partner marketplace. WebPT serves 75,000+ rehab therapy professionals and has an established partner integration program — a listing and integration here provides immediate access to the target buyer without a large sales force. Secondary channel: PT continuing education (CEU) providers, where a 1-hour RTM billing webinar serves as both education and product demo.

**Pricing strategy:** $299/month per clinic location, unlimited patients, including RTM documentation automation. Stress-test: the free alternative is a PT manually tracking home exercise compliance via phone calls and paper logs, then manually writing RTM documentation. The $299/month subscription is justified not by replacing something free but by enabling $5,750–$6,500/month in new RTM reimbursement the clinic is currently leaving on the table — the ROI is approximately 19–22x the subscription cost. This is not a "pay for something you currently do for free" pitch; it is a "we unlock revenue you cannot currently capture" pitch. That framing survives the free-alternative stress test because no free tool automates RTM billing documentation.

**Differentiation vs. 2026 competitors:** Hinge Health and Sword Health require employer contracts and minimum group sizes — inaccessible to independent clinics. Kaia Health has no RTM billing workflow. Reflexion Health is priced for hospital systems ($50K+ enterprise contracts). The rebuild's differentiation is the combination of camera-based movement capture (no hardware to sell or support), RTM billing automation (direct revenue impact for the clinic), and a price point accessible to a 2-therapist independent practice. The consumer fitness upsell — a patient-facing app that continues coaching after discharge — is a retention and expansion revenue layer to build in year two, once the clinical workflow is proven.
