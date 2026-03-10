# Build Plan: CustomerOS 2026

## Overview

CustomerOS was a London-based YC S22 startup founded in early 2022 by three Voxbone alumni who raised $2.1–2.6M to solve B2B customer data fragmentation; after at least three major pivots — from conversational data platform, to open source CRM framework, to customer success SaaS, to AI-agent GTM intelligence — the company failed to find a durable wedge, exhausted its runway without a follow-on, and appears to have quietly wound down by 2025.

The rebuild thesis is this: the original team was right about the problem but wrong about the timing and the wedge. In 2026, LLM-native signal extraction, a validated open source CRM category (Twenty, Huly), and a privacy-collapsed outbound landscape have converged to make a first-party intent layer — built open source, monetized as a managed cloud product — both technically buildable on a lean budget and commercially defensible in a way it simply was not in 2022. The new CustomerOS is an open source, self-hostable customer intelligence layer that turns a B2B company's own first-party signals (product usage, email threads, web behavior) into a continuously updated ICP score and pipeline priority queue — with no third-party data dependency and no data-network cold-start problem.

---

## Why Now?

### The single most important change: LLMs have eliminated the manual signal curation cost that made intent data platforms structurally inaccessible to pre-seed companies.

In 2022, building a credible intent data product required either (a) purchasing expensive third-party behavioral data from networks like Bombora, or (b) accumulating years of proprietary first-party web traffic across thousands of customer deployments — the moat that 6sense and Demandbase spent a decade building. CustomerOS had neither. By 2026, GPT-4 (March 2023) and its successors can extract structured buying signals — urgency, fit, objection type, competitive consideration — from unstructured first-party inputs: email threads, support tickets, product event logs, and CRM notes. This collapses the signal curation cost from "requires a proprietary data network" to "requires access to your own data," which every company already has. The data-network moat that killed CustomerOS's final iteration is no longer the barrier to entry.

**Privacy collapse has validated the demand side.** Google completed third-party cookie deprecation in 2024. Apple's ATT framework has measurably degraded mobile attribution. GDPR enforcement actions have increased in frequency and fine size. The result: B2B companies that relied on third-party intent data and outbound enrichment are experiencing pipeline visibility collapse in real time. This is not a thesis — it is a reported operational crisis for RevOps teams in 2025.

**The open source CRM category has been validated.** Twenty (open source Salesforce alternative) raised $5M in 2024 and has accumulated meaningful GitHub traction. Huly has demonstrated that developer-led CRM adoption is a real GTM motion, not a theoretical one. CustomerOS abandoned this wedge in 2022 before the category had proof points; those proof points now exist.

**Market data:** Clay reported a $200M ARR run rate in 2024 (source: public reporting). 6sense has raised $200M+. The GTM intelligence market — estimated at $3.1B in 2023 by MarketsandMarkets, though this figure should be treated with caution as analyst estimates in this category vary widely — is growing. Buyer willingness to pay is no longer a risk; execution and differentiation are.

**Distribution infrastructure:** The Supabase Cloud marketplace, Vercel's integration ecosystem, and the GitHub Marketplace now provide direct access to the developer and technical RevOps audience that CustomerOS's open source wedge requires — channels that were less developed in 2022.

---

## Current Market Analysis

**Market size:** The CRM software market was valued at approximately $63.9B globally in 2022 (Grand View Research) and is projected to exceed $130B by 2030. The narrower GTM intelligence and intent data segment — the more relevant competitive frame for this rebuild — is harder to size precisely; analyst estimates range from $3B to $6B in 2024, and this report treats those figures as directional rather than precise. What is clear from Clay's $200M ARR and 6sense's $200M+ in funding is that buyer willingness to pay at scale is established.

## Competition map and gaps:

- **Clay ($200M ARR, 2024):** The current market leader in GTM enrichment and ICP-fit automation. Clay's core weakness is that it is an enrichment and workflow tool, not a customer intelligence layer — it pulls third-party data in, it does not analyze first-party signals already inside a company's stack. Clay also has no open source offering and no self-hostable option, making it a non-starter for data-sensitive enterprise buyers in regulated industries (financial services, healthcare, government).

- **6sense / Demandbase:** Enterprise-grade, expensive ($60K–$200K+ ACV), and dependent on third-party intent data networks that are degrading under privacy regulation. Their moat is the data network; their weakness is that the data network is built on third-party cookies and anonymous IP resolution — both of which are structurally eroding. Neither offers an open source or self-hosted deployment path.

- **Apollo.io ($100M raised):** Primarily an outbound prospecting and sequencing tool. Apollo's intent data is third-party and generic; it does not analyze a company's own customer behavior. Weak on post-signup customer intelligence.

- **Twenty (open source CRM):** The closest structural analog to the rebuild. Twenty is a CRM data store, not an intelligence layer — it does not score leads, extract intent signals, or generate ICP fits. The gap between "open source CRM" and "open source customer intelligence layer" is the rebuild's wedge.

- **HubSpot / Salesforce:** Both have added AI features (Einstein, Breeze) but these are bolt-ons to legacy data models, not first-party signal extraction engines. Both are closed-source, cloud-only, and expensive. Neither can be self-hosted by a data-sensitive buyer.

**Demand signals from adjacent products:** The explosive growth of product analytics tools (PostHog, which is open source and self-hostable, raised $27M in 2023) signals strong demand for first-party behavioral data tools with self-hosting options. RevOps teams are actively looking for alternatives to third-party intent data.

**Defensibility analysis:** The honest answer is that Salesforce or HubSpot could build this. The structural protection is not that they cannot — it is that they will not prioritize it for the segment this rebuild targets (technical RevOps teams at 50–500 person B2B SaaS companies) because that segment is below their enterprise ACV threshold and because open source self-hosting is antithetical to their business model. The rebuild's defensibility comes from the open source community moat (switching cost once self-hosted and integrated), not from data network effects. This is a more honest and more achievable moat than the one CustomerOS originally pursued.

---

## Recommended MVP

### Core Feature 1: First-Party Signal Ingestion Pipeline

A pre-built set of connectors that pull product event data (Segment, PostHog, Mixpanel), CRM activity (HubSpot, Salesforce, Twenty), email metadata (Gmail, Outlook — subject lines and thread counts, not content, to avoid privacy issues), and support ticket volume (Intercom, Zendesk) into a unified customer timeline. This matters because it eliminates the integration work that currently requires a data engineer and 3–6 months of setup. Unlike CustomerOS's original open source framework, which required developers to build the data model from scratch, this ships opinionated connectors for the 10 tools that cover 80% of B2B SaaS stacks — reducing time-to-value from months to days.

## Core Feature 2: LLM-Native ICP Scoring Engine

An on-device or self-hosted LLM inference layer (using Ollama or llama.cpp with Llama 3.1 70B, available since July 2024) that reads the unified customer timeline and outputs a continuously updated ICP fit score, a buying stage classification, and a plain-English summary of why a given account is or is not a fit. This is the core differentiation from Clay and 6sense: the scoring runs entirely on the customer's own data, with no third-party data dependency, and can be self-hosted for data-sensitive buyers. CustomerOS's 2024 iteration attempted something similar but required cloud-based LLM APIs, creating data residency concerns that blocked enterprise deals.

## Core Feature 3: Priority Queue Interface

A lightweight, opinionated UI (not a full CRM) that surfaces the top 10 accounts to contact today, ranked by ICP score delta (accounts moving up in fit) and recency of buying signal. This is deliberately narrow — it is a daily action list, not a reporting dashboard. The original CustomerOS iterations built toward comprehensive platforms; this rebuild ships one screen that a sales rep opens every morning.

**What we will NOT build:** A full CRM, email sequencing, outbound enrichment from third-party databases, a mobile app, or a reporting/analytics dashboard in the first 12 months. These are the features that caused CustomerOS to compete with Gainsight and Salesforce before it had a customer base.

## Success metrics:

- 500 self-hosted deployments within 6 months of open source launch (GitHub stars are a vanity metric; deployments are not)
- 50 paying cloud customers at month 9, with average weekly active usage above 3 sessions per user
- Net Revenue Retention above 110% at month 12 — the signal that the product is delivering enough value to expand

**Cold-start note:** This product does not depend on network effects or local density. ICP scoring from first-party data delivers value to a single company in isolation from day one — there is no minimum user threshold before the core feature works. This is a structural advantage over intent data platforms that require cross-customer behavioral aggregation to generate signal.

---

## Go-to-Market Strategy

**Target customer segment:** Technical RevOps leads and founding AEs at B2B SaaS companies with 50–500 employees, $1M–$20M ARR, an existing product analytics stack (PostHog, Segment, or Mixpanel), and a stated concern about pipeline quality degradation from privacy changes. This segment is narrow enough to reach through focused channels and large enough to generate meaningful early revenue. It explicitly excludes enterprise (too slow, requires SOC 2 before conversation) and SMB below $1M ARR (too price-sensitive and too unlikely to have a structured RevOps function).

**Primary distribution channel:** GitHub + the PostHog and Supabase integration ecosystems. The open source repository is the top-of-funnel; integration listings in PostHog's app library and Supabase's marketplace provide direct access to the exact technical RevOps audience described above. Secondary channel: founder-led content on LinkedIn targeting RevOps practitioners, using the "pipeline blindness" framing that CustomerOS's final iteration articulated well but never had the distribution to amplify.

## Pricing strategy:

- Self-hosted: free, open source (MIT license)
- Cloud managed (up to 3 users, 500 tracked accounts): $0/month — permanent free tier to drive adoption
- Cloud managed (up to 10 users, 5,000 tracked accounts): $299/month
- Cloud managed (unlimited, SSO, audit logs, dedicated support): $999/month

**Stress test against free alternatives:** A RevOps lead can approximate ICP scoring today using HubSpot's free tier, a Google Sheet, and a Clay free trial. The honest answer is that this works — badly, manually, and without continuous updating — for companies under $2M ARR. The $299/month price is justified only if the product demonstrably saves 4+ hours per week of manual scoring work and improves pipeline conversion rate by a measurable amount. The MVP success metrics above (NRR > 110%) are the validation gate for this claim; the pricing should not be locked in until month 6 customer interviews confirm willingness to pay at this level.

**Differentiation vs. 2026 competitors:** Clay wins on third-party enrichment breadth; this product wins on first-party signal depth and self-hosting. 6sense wins on enterprise data network scale; this product wins on price, data residency compliance, and time-to-value for mid-market buyers. Twenty wins on CRM data storage; this product wins on intelligence and action — it tells you what to do with the data, not just where to store it.
