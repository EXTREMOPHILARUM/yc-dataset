# Build Plan: Optimizely 2026

## Overview

The 2026 Optimizely is a lightweight experimentation platform built for product teams at growth-stage SaaS companies ($1M–$20M ARR). It combines AI-powered hypothesis generation from your existing analytics stack with edge-native experiment delivery that eliminates flicker and performance degradation. The core insight: Google Optimize's shutdown in 2023 left a massive gap for teams that need fast, reliable A/B testing without the bloat of enterprise DXPs or the friction of engineering-heavy solutions.

The product wins on speed and clarity. An AI engine ingests your GA4, session recordings, and heatmaps to surface high-impact test ideas automatically. Experiments run on Cloudflare Workers or Vercel Edge—no JavaScript injection, no render delays. When results land, you get plain-language summaries that explain what happened and why, not just p-values. The no-code visual editor with AI variant generation means your PM can ship tests in minutes, not sprints.

Go-to-market targets product and growth leaders at the exact companies that outgrew free tools but can't justify $100K+ annual seats. Land with a free tier, expand through Slack integration and API access, and build a community around experimentation best practices. The market is ready—Google left it empty.35:Taaf,

## Why Now?

## The single most important change since Optimizely's failure: Google Optimize is dead.

## Current Market Analysis

**Market size today vs. 2010:** The A/B testing market in 2010 was nascent enough that Optimizely had to educate buyers on what experimentation was. In 2026, that education problem is solved — every product and marketing team at a company above ~20 people understands experimentation as a practice. The market Optimizely had to create now exists and is actively spending. The MarketsandMarkets estimate of ~$1.1B in 2023 for A/B testing software specifically is the best available figure; broader experimentation platform TAM figures are not reliably sourced in the research provided.

## Competition map and gaps:

- **Current Optimizely (Episerver-owned):** The incumbent brand, now a bloated DXP suite with $400M ARR and a $1.1B debt restructuring completed in December 2024. Its weakness is structural: it is a CMS company that acquired an experimentation brand, not an experimentation company. The product has expanded far beyond its original use case, pricing reflects enterprise contract expectations, and the December 2024 debt restructuring signals financial stress that will constrain R&D investment. It is not competing for the PLG-motion customer.

- **LaunchDarkly:** The clear winner in the developer/feature-flag segment, valued at $3B+ at its 2021 Series D. Its weakness is that it is infrastructure, not intelligence — LaunchDarkly tells you whether a flag is on or off; it does not tell you what to test or what the results mean. It also has no meaningful presence in the non-technical marketer segment.

- **VWO (Visual Website Optimizer):** The most direct functional replacement for the original Optimizely, serving the SMB and mid-market segments. Its weakness is that it is a 2010-era product with a 2010-era interface — no AI hypothesis generation, no edge delivery, no PLG motion. It competes on price, not intelligence.

- **AB Tasty and Kameleoon:** European mid-market competitors with similar functional profiles to VWO. Neither has made a credible AI-native product move as of the research available.

- **Adobe Target:** Bundled into Adobe Experience Cloud. Its weakness is the same as it was in 2020 — it is a feature inside a $500K/year suite, not a standalone product. It is not competing for companies below enterprise scale.

**Demand signals from adjacent products:** The growth of tools like Hotjar (heatmaps), FullStory (session recording), and Heap (product analytics) — all of which have added AI-generated insight layers in 2023–2024 — signals that the market is actively paying for intelligence on top of behavioral data. These tools are natural integration partners and demand signals simultaneously.

**Defensibility analysis:** The platform absorption risk that killed the original Optimizely is real and must be addressed directly. Google Optimize is gone. Adobe Target requires an Adobe suite commitment. Salesforce's experimentation capabilities are similarly suite-locked. The structural defense for a rebuild is not feature superiority — it is the AI layer. An LLM-powered hypothesis engine trained on experiment outcomes across thousands of customers creates a data flywheel that incumbents cannot replicate by adding a feature: the more experiments run through the platform, the better the hypothesis recommendations become. This is a genuine compounding advantage. The honest caveat: if Google launches a new free experimentation product integrated with GA4 and Gemini, the competitive dynamics shift materially. That risk is real and should be monitored.

---

## Recommended MVP

## Core Feature 1: AI Hypothesis Engine

The product ingests a customer's Google Analytics 4 or Segment data, session recordings (via Hotjar or FullStory API), and heatmaps, and returns a ranked list of experiment hypotheses with expected impact estimates and statistical rationale. This matters because the hardest part of experimentation is knowing where to start — Optimizely's original product assumed customers already had hypotheses and just needed tooling to test them. The rebuild inverts this: the AI generates the hypotheses, the human approves them. Unlike the original, this feature compounds in value as the platform accumulates cross-customer experiment outcome data to improve its recommendations.

## Core Feature 2: Edge-Native Experiment Delivery

Experiments are served via Cloudflare Workers or Vercel Edge Functions, not JavaScript injection. Variants are resolved before the page renders, eliminating flicker and latency degradation entirely. This matters because page-flicker was the #1 technical objection that prevented Optimizely from being deployed on high-traffic, performance-sensitive pages — e-commerce checkout flows, landing pages, and mobile web. The rebuild removes this objection structurally, not through workarounds.

## Core Feature 3: Plain-Language Results Interpretation

When an experiment concludes, the platform generates a plain-language summary of results: what happened, why it likely happened (with behavioral data context), what to do next, and what follow-on experiments to run. Statistical significance is calculated automatically using Bayesian methods (not frequentist p-values, which are routinely misinterpreted). This matters because Optimizely's original product showed you a confidence interval and left interpretation to the user — a gap that caused many experiments to produce inconclusive results that were never acted on.

## Core Feature 4: No-Code Visual Editor with AI Variant Generation

A visual editor that allows non-technical users to modify page elements, with an AI layer that can generate variant copy, headlines, and CTAs on demand. This preserves the original Optimizely accessibility advantage while adding generative capability.

**What we will NOT build at MVP:** Full-stack/server-side feature flagging (LaunchDarkly owns this; competing requires a different product and buyer), personalization engines, content management, mobile app testing, or OTT. The original Optimizely's fatal mistake was launching six product lines simultaneously. The rebuild launches one.

**Success metrics with thresholds:** 500 active accounts running at least one experiment per month within 12 months of launch; 15% month-over-month growth in experiments run on the platform; net revenue retention above 110% at 12 months; average time-to-first-experiment under 30 minutes for new signups.

**Cold-start problem:** This product does not depend on network effects or local density. A single user can run a meaningful experiment on day one. The AI hypothesis engine improves with more cross-customer data, but it delivers value from the first experiment using a customer's own analytics data. There is no cold-start threshold to clear before the core feature works.

---38:Ta4b,

## Go-to-Market Strategy
