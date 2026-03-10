# Build Plan: Fabius 2026

## Overview

The single most important change since Fabius's original failure is the commoditization of LLM inference. In 2022, extracting structured MEDDPICC qualification data from unstructured call transcripts required expensive custom NLP pipelines that a two-person team could not realistically build and maintain. GPT-4 (March 2023) and Claude 3 (March 2024) demonstrated that this extraction is now a prompt-engineering problem, not a machine learning infrastructure problem. The engineering cost to build Fabius's core scoring feature has dropped by an order of magnitude.

Three additional timing factors compound this shift:

**Gong's pricing has created a structural gap.** Gong charges approximately $1,200–$1,600 per seat per year (exact current pricing not publicly confirmed for 2026, but consistent with reported ranges from 2023–2025). This prices out any sales organization under roughly 50 reps, leaving a large mid-market and SMB segment with no methodology-enforcement tooling. The sales enablement software market was estimated at $2.6 billion in 2023 (MarketsandMarkets); current 2026 figures are not available in this report.

**Adjacent products have validated the demand.** Tools like Momentum (CRM auto-population via Slack) and Orum (AI-assisted dialing with live coaching) have raised meaningful rounds and found paying customers, confirming that sales teams will pay for automated workflow enforcement as a standalone product — not just as a feature inside Gong.

**Distribution infrastructure now exists.** The HubSpot App Marketplace (with 200,000+ customers as of 2024, per HubSpot's public reporting) and Salesforce AppExchange provide inbound discovery channels that did not exist as viable SMB distribution paths for a two-person team in 2023. Fabius's original go-to-market was entirely founder-led outbound; that constraint is now addressable.

---

## Why Now?

## Current Market Analysis

## Market Size

The sales intelligence and conversation analytics market was anchored by Gong's $7.25 billion valuation (2021 Series E) and Chorus's $575 million acquisition by ZoomInfo (2021). The broader sales enablement market was estimated at $2.6 billion in 2023 (MarketsandMarkets). A 2026 figure is not available in this report. What is clear is that the market has not contracted — Gong, Clari, and Salesloft have all continued expanding headcount and product surface area through 2024–2025 based on public LinkedIn data.

## Competition Map and Gaps

- **Gong**: The dominant incumbent. Weakness: enterprise pricing ($1,200–$1,600/seat/year) excludes sub-50-rep teams; methodology customization is shallow — scoring is benchmarked against Gong's aggregate dataset, not a company's specific rubric. G2 and Reddit discussions from 2023–2025 confirm that MEDDPICC adherence remains a reported pain point even among Gong customers.
- **Chorus (ZoomInfo)**: Largely stagnant post-acquisition. Weakness: product investment has slowed; ZoomInfo's 2024 revenue decline (publicly reported) suggests internal prioritization challenges.
- **Clari**: Focused on revenue operations and forecasting at the enterprise tier. Weakness: not a coaching product; does not address rep-level methodology adherence.
- **Momentum**: Automates CRM updates via Slack. Weakness: workflow automation without methodology scoring — it moves data but does not evaluate whether the right qualification steps occurred.
- **Salesloft (post-Drift merger)**: Broad sales engagement platform. Weakness: methodology enforcement is not a core differentiator; coaching features are generic.

**The Gap**: No current product combines (a) customizable methodology rubrics, (b) per-call scoring against those rubrics, and (c) SMB-accessible pricing. This is the exact gap Fabius identified — it remains open.34:T8d4,

## Demand Signals

Orum's growth in AI-assisted live coaching and Momentum's CRM automation traction both confirm that sales teams below the Gong price threshold are actively buying point solutions to solve execution gaps.

---

## Recommended MVP

## Core Features

## Methodology Rubric Builder

A no-code interface that lets a sales leader encode their specific sales framework — MEDDPICC, SPICED, SPIN, or a custom variant — as a structured scoring rubric with weighted criteria. This matters because Gong's coaching benchmarks against industry aggregates, not company-specific process; the rubric builder is the foundational differentiator that makes every downstream feature company-specific rather than generic. The original Fabius built this manually in onboarding; the rebuild makes it self-serve, reducing time-to-value from days to under an hour.

## Post-Call Methodology Score

After each recorded call, GPT-4o (May 2024) or equivalent extracts structured qualification signals from the transcript and scores the deal against the customer's rubric, surfacing specific missing steps with plain-language explanations for the rep. This is the core value delivery moment — it closes the gap between defined process and actual rep behavior that Fabius's founders identified at LiveRamp. Unlike the original, this feature runs entirely on commodity LLM inference with no custom NLP pipeline, making it maintainable by a two-person team.

## CRM Auto-Population

Qualification data extracted during scoring is written directly to HubSpot or Salesforce deal fields via API, eliminating manual rep data entry. This feature has been validated as standalone willingness-to-pay by Momentum's growth; bundling it with methodology scoring creates a combined ROI story (better data AND better coaching) that justifies the subscription cost. The original Fabius included this feature but it was secondary; the rebuild treats it as a co-equal value driver.

## What We Will NOT Build (MVP)

- Native call recording or transcription infrastructure (ingest from Gong, Chorus, or Zoom transcripts only)
- Real-time in-call coaching overlays
- Manager-facing forecasting dashboards
- Email generation features
- Any feature requiring more than two API integrations at launch

## Success Metrics

- 10 paying customers within 90 days of launch, each on a contract of at least $500/month
- Average methodology rubric setup time under 45 minutes
- 70%+ of scored calls result in rep opening the feedback within 24 hours (engagement threshold)
- Net Revenue Retention above 100% at the 6-month cohort mark

---

## Go-to-Market Strategy

## Target Customer Segment

B2B SaaS companies with 10–50 sales reps, a defined sales methodology (MEDDPICC or SPICED), and an existing HubSpot or Salesforce CRM. This segment is explicitly priced out of Gong, has enough reps that individual manager coaching is becoming a bottleneck, and has already demonstrated process-orientation by adopting a named methodology. Revenue Operations leads and VP of Sales at Series A–B companies are the primary buyers.

## Primary Distribution Channel

HubSpot App Marketplace as the primary inbound channel, supplemented by founder-led outbound to RevOps communities (RevGenius, Pavilion). The HubSpot marketplace serves 200,000+ customers (per HubSpot's 2024 public reporting), the majority of whom are in the 10–200 employee range — the exact target segment. Marketplace listings generate inbound discovery without requiring a marketing team. This directly addresses Fabius's original failure mode of zero inbound presence.

Secondary: LinkedIn content from the founders documenting methodology-enforcement case studies — the zero-tweet failure of the original Fabius is a specific, correctable mistake.

## Pricing

## Differentiation vs. 2026 Competitors

The rebuild wins on three axes simultaneously that no current competitor matches: SMB-accessible pricing, company-specific rubric customization (not industry benchmarks), and a HubSpot-native integration path. Momentum automates CRM but does not score methodology. Gong scores calls but not against your rubric and not at your price point. The rebuild occupies the intersection of both.
