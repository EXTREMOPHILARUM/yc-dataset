# Build Plan: CustomerOS 2026

## Overview

## Why Now?

## The single most important change: LLMs have eliminated the manual signal curation cost that made intent data platforms structurally inaccessible to pre-seed companies.

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

## Core Feature 1: First-Party Signal Ingestion Pipeline

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

**Primary distribution channel:** GitHub + the PostHog and Supabase integration ecosystems. The open source repository is the top-of-funnel; integration listings in PostHog's app library and Supabase's marketplace provide direct access to the exact technical RevOps audience described above. Secondary channel: founder-led content on LinkedIn targeting RevOps practitioners, using the "pipeline blindness" framing that CustomerOS's final iteration articulated well but never had the distribution to amplify.36:T570,

## Pricing strategy:
