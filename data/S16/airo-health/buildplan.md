# Build Plan: Airo Health 2026

## Overview

By 2026, Airo is a B2B mental health platform—not a consumer wearable. The product is a clinical-grade armband that continuously monitors HRV-based stress, paired with an LLM-driven coaching layer that delivers real-time micro-interventions. The buyer is the enterprise HR department, not the individual; the unit economics work because employers self-insure and desperately need absenteeism and burnout reduction.

The market shift is simple: in 2016, there was no proven B2B distribution channel for wearable health data. Now there is. Employers have normalized health benefits platforms (Ro, Headspace for Work, Calm Business), and they're actively buying into workplace mental health. Meanwhile, WHOOP's $3.6B valuation proved the underlying science—HRV stress tracking works—but left the enterprise market completely unserved.

The go-to-market is direct sales to mid-market self-insured employers in high-burnout verticals (tech, finance, healthcare). Airo wins by being the only vendor combining validated hardware, real-time coaching, and HR-grade analytics in a single platform. The pitch: measurable ROI on absenteeism and retention within 90 days.33:T8b3,

## Why Now?

## Current Market Analysis

**Market Size:** The global mental health app market was estimated at approximately $587 million in 2018; it reached approximately $6.2 billion in 2023 and is projected to exceed $17 billion by 2030 (source: Grand View Research — note: exact figures should be independently verified at time of fundraising). The corporate wellness market, the more relevant distribution target for a rebuilt Airo, is estimated at $61 billion globally in 2023 (Global Wellness Institute — verify independently). US employer mental health benefits spending specifically reached $15.5 billion in 2023, up roughly 3x from 2016.

## Competition Map and Gaps:

- **Whoop 4.0** — The most direct validator of Airo's thesis. Weakness: priced at $239/year subscription targeting elite athletes and fitness enthusiasts, not workplace stress management. No enterprise HR sales motion. No LLM-driven adaptive coaching.
- **Apple Watch Series 9 / Ultra 2** — Dominant consumer wearable with HRV features. Weakness: general-purpose device with no dedicated stress management workflow, no enterprise benefits integration, and no clinical-grade intervention layer.
- **Calm for Business / Headspace for Work** — Proven enterprise mental health buyers. Weakness: software-only, no passive biometric monitoring. Require active user engagement to generate data.
- **Muse S (InteraXon)** — EEG-based meditation headband. Weakness: requires active use sessions; not a passive continuous monitor; no enterprise sales channel.
- **Spire Health Tag** — Breathing-based stress monitor clipped to clothing. Weakness: low consumer awareness, limited enterprise penetration, no LLM coaching layer.

**Gap:** No current competitor combines passive, continuous HRV-based stress monitoring with LLM-driven adaptive coaching delivered through an enterprise HR benefits channel. That is the white space.

**Demand signals:** Calm and Headspace's enterprise pivots demonstrate that HR buyers will purchase mental health tools at scale. Whoop's $3.6 billion valuation demonstrates consumer willingness to pay for HRV-based wearables. The combination has not been built.

---

## Recommended MVP

## Core Features:

## Continuous HRV Stress Monitoring via Validated Armband Hardware

The device samples HRV using optical photoplethysmography at medically meaningful resolution, leveraging reference designs for BLE biosensor wearables now available through contract manufacturers. This directly inherits Airo's 2016 product architecture but ships on validated, manufacturable hardware rather than a prototype — the specific execution failure that ended the original company. Unlike Whoop, the form factor and UX are designed for office wear, not gym wear.

## On-Device Real-Time Stress Classification and Alerting

Using on-device ML inference (targeting Qualcomm QCC5181 or equivalent chip available in 2024–2025 reference designs), the armband classifies stress-rise events locally and delivers haptic alerts without cloud dependency. This makes the "alert when stress is rising" feature Airo described in 2016 technically reliable at low latency and low battery cost — constraints that were severe on 2016 hardware and are now solved.

## LLM-Driven Adaptive Coaching Layer

When a stress event is detected, the companion app surfaces a GPT-4o (May 2024) or Claude 3.5 Sonnet (June 2024) generated micro-intervention — a breathing sequence, a reframe prompt, a movement cue — personalized to the user's recent HRV history, time of day, and self-reported context. This replaces the static "built-in exercises" Airo described with a coaching layer that improves with use, without requiring a clinical content team.

## Enterprise HR Dashboard and Benefits Integration

An aggregate, anonymized dashboard for HR buyers showing team-level stress trends, intervention engagement rates, and absenteeism correlations. This is the distribution mechanism Airo never had — it converts the device from a consumer product into a benefits line item with a measurable ROI narrative for self-insured employers.

**5. NOT Building:** Consumer DTC e-commerce channel (at launch), passive nutrition or calorie tracking of any kind, sleep tracking, fitness/activity tracking, clinical diagnostic claims, or any feature requiring FDA clearance in the first 18 months.

## Success Metrics:

- 3 enterprise pilot contracts signed (minimum 50 employees each) within 6 months of hardware availability
- ≥60% of enrolled employees wearing device ≥4 days/week at 90-day mark
- ≥40% of stress-alert events resulting in a completed LLM coaching interaction
- Hardware unit cost below $80 at 500-unit pilot run, targeting $149 enterprise-subsidized retail

---

## Go-to-Market Strategy

**Target Customer Segment:** Self-insured US employers with 200–2,000 employees in high-burnout industries — specifically technology companies, financial services firms, and healthcare organizations with documented mental health benefits spend and existing EAP (Employee Assistance Program) relationships. This segment has demonstrated willingness to pay for mental health benefits, has HR buyers with budget authority, and is small enough that a two- to four-person founding team can close deals through direct outreach without an enterprise sales organization.

**Primary Distribution Channel:** Direct enterprise HR sales, initially through warm introductions via benefits brokers and PEO (Professional Employer Organization) networks. Benefits brokers — who advise self-insured employers on benefits packages — represent a leveraged channel: a single broker relationship can unlock dozens of employer accounts. This channel did not meaningfully exist for a hardware mental health startup in 2016 and is now a proven path used by competitors including Calm for Business and Spring Health.

**Pricing Strategy:** Hardware at cost or subsidized ($0–$99 per employee device) bundled into an annual SaaS contract at $15–$25 per employee per month, billed to the employer. This mirrors the Whoop enterprise model and the Calm for Business pricing architecture. Justification: HR buyers have established budget categories for per-employee-per-month mental health benefits spend; a hardware-inclusive SaaS price fits existing procurement frameworks and removes the consumer purchase friction that constrained Airo's DTC model.

**Differentiation vs. 2026 Competitors:** Calm for Business and Headspace for Work offer software with no passive monitoring — they require active engagement and generate no objective stress data. Whoop targets athletes with a fitness-first narrative incompatible with HR benefits positioning. A rebuilt Airo is the only product combining passive continuous HRV monitoring, LLM-adaptive coaching, and an enterprise HR dashboard in a single benefits-ready package — making it the first offering that gives HR buyers objective, aggregate mental health data rather than self-reported engagement metrics.
