# Build Plan: Station 2026

## Overview

Station was a Paris-based desktop productivity application (2017–2021), incubated by eFounders and accelerated through YC W18, that aggregated 600+ SaaS web apps into a single unified interface with a sidebar dock, universal search, and consolidated notifications — reaching 40,000 weekly active users spending six hours per day in the product before quietly winding down after exhausting its $3.25M seed round without ever generating revenue.

The rebuild thesis rests on two structural changes: enterprise buyers now have established budget lines for AI-powered cross-app search (Glean's $4.6B valuation proves it), and LLMs can finally deliver the semantic search across unstructured SaaS content that was technically impossible in 2017. Station 2026 is an AI-native work browser that sells to teams, not individuals — a $20/user/month semantic search and SaaS command layer that converts the engagement Station proved into the enterprise revenue it never built.

---

## Why Now?

## The single most important change: enterprise buyers now have a recognized budget category for cross-app AI search that did not exist when Station operated.

When Station launched in 2017, "SaaS aggregation" was a consumer novelty. In 2026, it is a funded enterprise category. Glean — which does for enterprise knowledge retrieval what Station's "automated knowledge base" pivot was attempting — raised at a $4.6B valuation in 2024. Guru, Notion AI, and Microsoft Copilot for M365 collectively validate that knowledge workers and their employers will pay $15–30/user/month for cross-app intelligence. Station was directionally correct in its late-stage pivot; it simply arrived before the market existed.

**The second change: LLMs make the core feature actually work.** Station's universal search in 2017 was DOM-scraping and text indexing — it could find a Slack message by keyword but could not answer "what did we decide about the Q3 pricing model?" GPT-4 (March 2023) and Claude 3 (March 2024) APIs now enable genuine semantic retrieval across unstructured content: Slack threads, Notion docs, Gmail chains, Linear tickets. This transforms Station's most defensible feature from a convenience into a knowledge infrastructure product.

**The third change: SaaS sprawl has dramatically worsened the problem.** The average enterprise used approximately 8 SaaS applications in 2015; by 2023, that figure exceeded 130 applications per organization, according to BetterCloud's State of SaaSOps report. The pain Station was solving is roughly 16x more acute than when it launched.

**Distribution channels unavailable in 2017:** Slack's App Directory (with 750,000+ daily active developers as of 2023, per Slack), the Microsoft Teams App Store, and the Notion integrations marketplace all provide direct access to the exact buyer persona — knowledge workers already inside the SaaS stack — that Station could only reach through organic Product Hunt discovery.

**On performance:** Tauri (v2.0, released October 2024), built on Rust, delivers desktop application memory footprints roughly 50–70% smaller than equivalent Electron applications, according to published benchmarks from the Tauri project. The sluggishness that drove users to Ferdium is now a solvable engineering problem, not a framework constraint.

---

## Current Market Analysis

**Market size:** The enterprise search and knowledge management market was valued at approximately $4.9 billion in 2023 and is projected to reach $12.4 billion by 2030, per Grand View Research. The adjacent SaaS management platform market — tools that help IT and operations teams govern SaaS sprawl — was valued at approximately $3.5 billion in 2023, per MarketsandMarkets. Station 2026 sits at the intersection of both. The specific segment most relevant — AI-powered workplace search for knowledge workers — did not exist as a named category when Station operated; it now has multiple funded entrants and recognized buyer budgets.

## Competition map and gaps:

- **Glean** ($4.6B valuation, 2024): The most direct competitor. Glean indexes enterprise SaaS content and delivers AI-powered search. Its weakness is price and deployment complexity — Glean targets large enterprises (500+ seats), requires IT-led procurement, and is priced accordingly (estimated $15–25/user/month at scale, with significant implementation overhead). It does not offer a unified app interface; it is a search tool, not a work browser.
- **Arc Browser** (The Browser Company): Validated the "opinionated browser" category and charges nothing — Arc is free. Its AI features (Arc Search, released February 2024) are consumer-grade and do not index private SaaS content. Arc's weakness is that it is a general browser, not a work-context tool, and has no enterprise data connectors.
- **Notion AI / Notion as work OS**: Captures the knowledge base use case but only for content that lives inside Notion. Users with Slack, Gmail, and Linear data outside Notion get no cross-app intelligence.
- **Microsoft Copilot for M365**: Powerful within the Microsoft ecosystem; effectively useless for teams running Notion + Linear + Figma + Slack stacks, which describes most high-growth tech companies.
- **Ferdium** (open-source Station successor): Functionally equivalent to 2017 Station — a webview wrapper with no AI layer, no team features, and no monetization. Confirms the user need persists; confirms users will not pay for the wrapper alone.

**Demand signals from adjacent products:** Raycast (AI-powered launcher, $30M Series B in 2023) has demonstrated that power users at tech companies will pay for a fast, AI-augmented command interface. Its growth validates the "keyboard-first, cross-app command" interaction model that Station's universal search approximated.

**Defensibility analysis:** The honest answer is that Microsoft Copilot and Google Workspace AI are the existential platform threats. Both are building cross-app AI search within their own ecosystems. The structural defense is the same one that keeps Glean alive: a large and growing portion of knowledge workers — particularly at high-growth tech companies — run heterogeneous SaaS stacks that span neither Microsoft nor Google's ecosystem exclusively. A team using Notion, Linear, Figma, Slack, and Loom has no incumbent platform that indexes all five. Station 2026's defensibility depends on owning the heterogeneous-stack segment and building switching costs through a proprietary cross-app knowledge graph that deepens with use. This is a real but narrow moat; if Microsoft or Google meaningfully expands ecosystem coverage, the addressable market shrinks. This risk should be disclosed to investors.

---

## Recommended MVP

## Feature 1: AI Semantic Search Across Connected Apps

A natural-language query interface that retrieves answers — not just links — from across a user's connected SaaS stack (Slack, Gmail, Notion, Linear, Google Drive at launch). A user types "what's the current status of the rebrand project?" and receives a synthesized answer with source citations, not a list of search results. This is the feature Station's universal search aspired to be but could not deliver with 2017-era NLP. It is powered by Claude 3.5 or GPT-4o APIs with retrieval-augmented generation over indexed SaaS content. This is the primary paid feature and the primary reason to charge — it is not replicable by Ferdium or any free webview wrapper.

## Feature 2: Unified App Dock with Notification Triage

A persistent sidebar that surfaces connected apps with unread counts, plus an AI-powered notification digest that summarizes and prioritizes cross-app alerts every morning. Unlike Station's original unified notifications (which simply aggregated everything), this version uses LLM classification to distinguish urgent from ambient notifications and suppress noise. This addresses the core engagement driver Station proved while adding a layer of intelligence that justifies the paid tier.

## Feature 3: Team Knowledge Snapshots

A shared, auto-generated digest of what the team decided, shipped, or discussed across connected apps in the past 24–48 hours — surfaced as a team-readable summary, not a raw activity feed. This is the "automated knowledge base" feature Station pivoted toward in 2018 but never shipped. It creates team-level switching costs that individual-use features cannot: once a team's institutional memory lives in Station's knowledge graph, migration cost rises significantly.

## What we will NOT build at MVP:

- 600 app integrations. Launch with 8–10 integrations covering the modal tech-company stack (Slack, Gmail, Notion, Linear, GitHub, Google Drive, Figma, Loom). Breadth killed Station's engineering capacity; depth wins the initial customer.
- A third-party developer platform. Station's 2018 pivot toward opening the platform to external developers was premature and diluted focus. Build this only after achieving $1M ARR.
- A free tier. The original Station's free-forever positioning is the single most important mistake to avoid repeating.

## Success metrics:

- 500 paying teams (average 10 seats) within 12 months of launch = $1.2M ARR at $20/user/month
- Week-4 retention above 60% for teams (not individuals)
- AI search used at least 3x per user per day (validates the core feature is load-bearing, not decorative)

**Cold-start problem:** This product does not depend on network effects between strangers, but it does require sufficient connected apps per user to make AI search useful. A single connected app produces weak results; five connected apps produce genuinely useful cross-context retrieval. The onboarding flow must connect at least three apps before the user sees the main interface. Target teams of 5–15 people as the minimum viable unit — a team with shared Slack, Notion, and Linear provides enough cross-app signal to make the knowledge snapshot feature immediately valuable on day one.

---

## Go-to-Market Strategy

**Target customer segment:** Engineering and product teams of 5–25 people at Series A–C technology companies running heterogeneous SaaS stacks outside the Microsoft or Google ecosystem. Specifically: companies using Notion (not Confluence), Linear (not Jira), and Slack (not Teams) — a stack profile that describes the majority of high-growth startups founded after 2019 and that has no incumbent AI search solution covering all three. This segment is narrow enough to reach through focused channels and large enough to support a $5M ARR business before requiring expansion.

**Primary distribution channel:** Bottom-up, individual-to-team conversion via the Notion integrations marketplace and Slack App Directory. A power user installs Station individually, uses AI search to surface Notion and Slack content, and shares a team knowledge snapshot with their team — creating a natural viral loop into team adoption. This mirrors how Notion itself grew: individual adoption creating team pull. Secondary channel: direct outreach to engineering leads at YC-backed companies through the YC alumni network, which provides warm access to exactly the target segment.

**Pricing:** $20/user/month, billed annually, with a 14-day free trial for teams (no individual free tier). Stress-test: a team currently accomplishes cross-app search via browser tabs, Cmd+F, and memory — effectively free. The $20/user/month price is justified only if AI semantic search saves a meaningful amount of time daily. At 30 minutes saved per user per day (a conservative estimate for a 10-app knowledge worker), $20/month represents roughly $0.03 per minute of recovered time — a favorable ROI framing for a buyer who already pays $15/month for Notion and $12/month for Linear without hesitation. The price is deliberately set below Glean (which is out of reach for Series A companies) and above free alternatives (which offer no AI layer). Annual commitment reduces churn risk from the free-tier migration pattern that killed Station.

**Differentiation vs. 2026 competitors:** Against Glean — dramatically simpler deployment, no IT procurement required, priced for growth-stage companies. Against Arc — private SaaS content indexing and team features that a general browser cannot offer. Against Microsoft Copilot — works for the Notion/Linear/Slack stack that Microsoft does not own. Against Ferdium — AI search and team knowledge features that a free webview wrapper structurally cannot build.
