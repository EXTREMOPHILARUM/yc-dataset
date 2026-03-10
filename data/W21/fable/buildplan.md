# Build Plan: Fable 2026

## Overview

Fable was a New York-based B2B productivity startup (YC W21) that built a collaborative product specification editor with two-way sync to Jira, Linear, Productboard, and Asana; it wound down quietly in mid-to-late 2022 after failing to monetize, as its core sync-layer value proposition was absorbed natively by the very platforms it depended on.

The rebuild thesis is not to retry the sync layer — it's to solve the problem one level up. AI coding agents (Cursor, GitHub Copilot Workspace, Devin) now execute engineering tickets autonomously, and they fail catastrophically on ambiguous specs; a rebuilt Fable becomes an AI-native spec compiler that enforces structured, machine-readable product requirements at the point of writing, turning the PM's document into the authoritative input for both human engineers and AI agents alike. In one line: **Fable 2026 is the spec quality layer that makes AI-assisted engineering actually work.**

---

## Why Now?

The single most important change since Fable's failure is the emergence of AI coding agents as a mainstream engineering workflow. Cursor crossed 1 million active developers in late 2024 (per Cursor's own public announcement); GitHub Copilot Workspace entered public beta in April 2024; Devin (Cognition AI) launched publicly in 2024 with enterprise contracts. These agents do not read Confluence pages or Notion docs — they consume tickets. And the quality of their output is directly, measurably constrained by the quality of the ticket they receive. This is a structurally new problem that did not exist when Fable operated, and it is one that Jira, Linear, and Notion are architecturally ill-positioned to solve because their editors are general-purpose, not spec-quality-enforcing.

The second critical change is the Model Context Protocol (MCP), introduced by Anthropic in November 2024 and adopted by OpenAI, Google DeepMind, and major tool vendors through 2025. MCP allows an AI application to read from and write to Jira, Linear, GitHub, and other tools through a standardized interface — without brittle point-to-point API integrations. This directly eliminates the maintenance burden that likely consumed Fable's two-person engineering capacity. A rebuilt Fable can write structured tickets to any MCP-compatible tool with a single integration surface, not four separate ones.

On market timing: the AI developer tools market was valued at approximately $4.7 billion in 2024 and is projected to reach $22.5 billion by 2030 (MarketsandMarkets, 2024 — exact figures should be independently verified before use in investor materials). The PM tooling segment specifically is harder to size precisely; the research report cites approximately 875,000 PMs in the U.S. alone, with global estimates exceeding 3 million.

Distribution channels unavailable to Fable in 2022 now include: the **Linear Marketplace** (launched 2024), the **Cursor Plugin Directory**, the **GitHub Marketplace** with Copilot Extensions (opened to third parties in 2024), and the **Atlassian Marketplace** with AI app categories added in 2023–2024. Each of these channels places a spec-quality tool directly in front of the engineering workflow where the pain is now most acute.

---

## Current Market Analysis

**Market size today vs. 2021–2022:** The PM tooling market is not cleanly reported as a standalone segment. The broader project management software market was approximately $6.1 billion in 2021 (Grand View Research) and is estimated at $9–10 billion in 2024 — growth driven substantially by AI feature additions. The AI-augmented developer productivity segment is growing faster; specific figures for "spec tooling" as a category do not exist in available sources and should not be invented. What is documentable: Linear reported over 25,000 paying companies in 2024 (per their public blog), and Notion reported 20 million users in early 2022, a figure that has grown since. The addressable buyer pool is larger and better-funded than in 2022.

## Competition map and gaps:

- **Linear Docs** (launched 2022–2023): Absorbed Fable's original use case — spec writing adjacent to tickets. Weakness: Linear Docs are freeform; they enforce no structure, no completeness checks, and no machine-readability standards. A PM can write "make the button blue" and Linear will accept it without complaint.
- **Notion AI** (launched February 2023): Offers AI writing assistance inside documents but has no native ticket-generation or spec-validation logic. Weakness: Notion is a horizontal tool; it has no concept of what a "good" product spec looks like for an AI agent to consume.
- **Confluence + Atlassian Intelligence** (AI features added 2023–2024): Deep Jira integration but the AI layer is summarization and search, not spec quality enforcement. Weakness: Confluence's editor is legacy-heavy and the AI features are add-ons, not core workflow.
- **Cycle.app** (YC W22, active as of 2024): A PM workspace with Jira/Linear sync — the closest living analog to Fable. Weakness: Cycle is still primarily a sync and aggregation layer, not an AI-native spec compiler. It faces the same platform dependency risk Fable faced.
- **Emerging AI PM tools** (Notion AI, Productboard Pulse, Airfocus AI): All focused on roadmap prioritization and stakeholder communication, not spec-to-agent quality.

**Demand signals from adjacent products:** Cursor's popularity has generated a visible secondary market for "prompt engineering for developers" — teams are writing internal guides on how to write tickets that Cursor can execute. This is an unmet need being solved with Google Docs and tribal knowledge. That is a product gap.

**Defensibility analysis:** The platform incumbents — Atlassian, Linear, Notion — could theoretically add spec-quality enforcement. The structural reason they are unlikely to do so quickly: their editors are general-purpose by design, and adding opinionated quality gates would alienate the majority of users who are not writing AI-agent-targeted specs. A startup can be more opinionated than a platform. Additionally, a rebuilt Fable's defensibility comes not from API sync (which is replicable) but from **proprietary spec quality models** — trained on what makes a ticket successfully executable by Cursor or Copilot Workspace — which accumulate as a data asset over time. This is a genuine moat that the original Fable lacked entirely. That said, if Linear or Atlassian decide to prioritize this problem, they have the distribution to win. This risk should be disclosed to investors honestly; the window is real but not permanent.

---

## Recommended MVP

## Core Feature 1: AI Spec Compiler

The editor accepts natural-language product intent from a PM and uses Claude 3.5 Sonnet or GPT-4o (both available as of mid-2024) to generate a structured spec with explicit acceptance criteria, edge cases, and dependency flags. Unlike Fable's original editor — which was a blank canvas that PMs filled manually — this feature actively co-writes the spec, enforcing completeness before the PM can publish. This matters because AI coding agents fail on underspecified tickets; the compiler makes failure-by-ambiguity structurally harder.

## Core Feature 2: Agent-Readability Score

Each spec receives a real-time score (0–100) measuring how executable it is by an AI coding agent — based on criteria such as: are acceptance criteria testable? Are edge cases enumerated? Are dependencies named? This score is visible to the PM before ticket creation and to engineering leads in a team dashboard. This is not a feature Fable had, and it is not a feature any current competitor offers. It creates a feedback loop that improves PM behavior over time and generates proprietary data.

## Core Feature 3: MCP-Native Ticket Push

Using MCP (available as a standard from November 2024), the tool pushes structured tickets to whichever issue tracker the team uses — Linear, Jira, GitHub Issues — without maintaining separate API integrations. This directly solves the maintenance burden that likely overwhelmed Fable's two-person team. The PM does not need to choose a supported integration; if the tracker is MCP-compatible, it works.

## Core Feature 4: Spec-to-Ticket Diff Tracker

When a spec is revised after tickets have been pushed, the tool flags which tickets are now stale and generates a suggested update. This is a lightweight version of Fable's "Build Progress" feature, but scoped to spec integrity rather than status reporting.

**What you will NOT build (MVP):** No roadmap views, no stakeholder communication features, no Gantt charts, no OKR tracking, no meeting notes, no AI-generated PRDs from scratch without PM input. The MVP does one thing: it makes specs machine-readable and pushes them to wherever engineers work.

## Success metrics:

- 50 teams (not individual users) actively using the spec compiler within 90 days of launch
- Agent-readability score average above 75 for published specs (internal benchmark)
- At least 3 teams reporting measurable reduction in ticket clarification cycles (qualitative, collected via structured interviews)
- First paying customer within 60 days of launch

**Cold-start problem:** This product does not depend on network effects or local density. A single PM on a single team derives value from the spec compiler on day one, independent of how many other teams use the product. There is no cold-start threshold to clear.

---

## Go-to-Market Strategy

**Target customer segment:** Engineering-led startups with 10–75 employees that have adopted AI coding agents (Cursor, GitHub Copilot, or Devin) as part of their standard engineering workflow and are experiencing the "garbage in, garbage out" problem with ticket quality. Specifically: companies where at least one engineer has complained in a team Slack or retro that "the AI didn't understand the ticket." This is a narrow, identifiable, and self-aware buyer.

**Primary distribution channel:** The **Cursor Plugin Directory** and **GitHub Marketplace** (Copilot Extensions), both of which place the tool directly in the engineering workflow where the pain is felt. Secondary channel: direct outreach to engineering leads at Cursor-heavy companies, identifiable via public GitHub activity and job postings that mention Cursor or Copilot. Tertiary: content marketing targeting the search query "how to write tickets for Cursor" — a query with documented organic volume (exact figures not available in research sources) and no authoritative answer yet.

**Pricing strategy:** $49/month per PM seat, with free read-only access for engineers and stakeholders. This mirrors Figma's and Linear's editor-seat models and is consistent with Fable's original per-maker intent.

Stress-test against free alternatives: A PM can write specs in Notion (free tier) and manually push tickets to Linear (free tier). The free alternative is worse — it produces no agent-readability score, no completeness enforcement, and no MCP push — but it costs $0. The $49/seat price is justified only if the PM can point to a measurable reduction in engineering rework caused by bad tickets. This means the GTM motion must lead with the agent-readability score as a quantifiable output, not with "better specs" as a qualitative promise. If a team cannot articulate the cost of a bad ticket in engineering hours, they will not pay $49/month. Sales conversations must start with that cost calculation.

**Differentiation vs. 2026 competitors:** Cycle.app is the most direct competitor; it is a sync layer, not a quality layer. The rebuilt Fable's differentiation is the agent-readability score and the MCP-native architecture — neither of which Cycle offers as of the research report date. Notion AI and Confluence AI are horizontal; they will not build opinionated spec-quality enforcement without alienating their broader user bases. The rebuilt Fable is the only tool that treats "will an AI agent be able to execute this ticket?" as a first-class product question.
