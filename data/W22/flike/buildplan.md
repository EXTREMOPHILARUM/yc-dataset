# Build Plan: Flike 2026

## Overview

Flike 2026 is a native Excel and Google Sheets plugin that solves the core problem the original product identified: spreadsheet chaos in finance teams. It combines three capabilities—AI-powered formula generation with automatic audit trails, Git-style version control with per-cell attribution, and structured collaborative review workflows—into a single layer that sits where finance teams already work.

The timing is different now. LLMs can generate and explain formulas reliably, and finance teams have grown desperate for auditability as spreadsheets drive larger decisions. The market has also matured: generic AI assistants like Copilot for Excel exist, but they create compliance nightmares for regulated finance work. There's a clear gap for purpose-built tooling.

The go-to-market targets FP&A analysts and controllers at Series B–D tech companies—teams large enough to feel spreadsheet pain acutely but still lean enough to adopt new tools quickly. Distribution happens through direct sales to finance ops leaders, paired with product-led onboarding via the plugin itself. The win is simple: reduce audit friction, eliminate version conflicts, and make collaborative finance work traceable. No pivots. No crowded segments. Just the original insight, finally executable.

## Why Now?

The single most important change since Flike's failure: **LLM-powered formula generation and audit capabilities now exist natively**, directly eliminating the core technical barrier that made Flike's original "GitHub for spreadsheets" vision expensive to build. When the Müller brothers founded Flike in 2021, automating formula creation, error detection, and change explanation required custom ML infrastructure. Today, GPT-4o (May 2024) and Claude 3.5 Sonnet (June 2024) can generate, audit, and explain complex Excel and Google Sheets formulas with high accuracy out of the box — collapsing what would have been months of ML engineering into API calls.

The market Flike originally targeted has since been validated by adjacent products. Notion has surpassed 100M users (per Notion's 2024 public statements), Coda raised at a $600M valuation, and Airtable reached $11.7B at peak — collectively proving that knowledge workers will pay for structured collaboration layered on document and data primitives. Flike's $20B addressable market framing (per Tobias Müller's 2022 writing) was not wrong; it was early.

Critically, Microsoft Copilot for Excel and Google Duet AI for Sheets have now shipped — but both are generic productivity tools, not finance-workflow-specific. Neither provides FP&A-grade audit trails, formula change attribution, or model review workflows. This is the gap: a vertical AI collaboration layer purpose-built for financial modeling teams, not general spreadsheet users.

Distribution infrastructure has also matured. The Microsoft 365 App Store and Google Workspace Marketplace now offer direct access to enterprise finance teams without requiring a direct sales motion to get to first users. Specific pricing data for these channels in 2026 is not available, but both marketplaces have expanded enterprise procurement integrations since 2023.

LLM inference costs have fallen dramatically post-2024 price compression, making the unit economics of per-formula AI calls viable at seed-stage burn rates — a structural advantage Flike never had.

---

## Current Market Analysis

**Market Size:** The global financial planning and analysis (FP&A) software market was valued at approximately $2.8B in 2023 (MarketsandMarkets) and is projected to reach $5.5B by 2028. The broader spreadsheet collaboration and automation layer — Flike's original framing — remains largely unaddressed by dedicated vertical tooling. Exact 2026 market size data is not yet available; the figures above are the most recent published estimates.

**What Has Been Validated:** Notion, Coda, and Airtable collectively proved the collaboration-on-data-primitives market. More directly, tools like Equals (spreadsheet-native BI with version history) and Grid (spreadsheet publishing) have raised seed and Series A rounds targeting adjacent finance-team workflows, confirming sustained investor and user demand.

## Competition Map and Gaps:

- **Microsoft Copilot for Excel** — Generic AI assistant; no finance-specific audit trails, no model review workflows, no change attribution by collaborator. Weakness: horizontal product cannot serve vertical compliance and review needs.
- **Google Duet AI for Sheets** — Same structural weakness as Copilot; optimized for general productivity, not FP&A governance.
- **Equals** — Spreadsheet-native analytics with version control; strong on BI and dashboarding, weak on collaborative model-building workflows and AI-assisted formula auditing.
- **Pigment / Anaplan** — Enterprise FP&A platforms that require full migration away from Excel/Sheets. High switching cost is their weakness; most mid-market finance teams will not migrate.
- **Causal** — Modeling-focused; strong on scenario planning, limited on Excel/Sheets interoperability.

**The Gap:** No current product combines (1) version control and change attribution, (2) AI-powered formula generation and error explanation, and (3) collaborative review workflows — all layered on top of Excel and Google Sheets without requiring migration. That is the exact product Flike originally envisioned, now buildable with 2026 infrastructure.

**Demand Signal:** The FP&A community on LinkedIn and communities like CFO Connect (35,000+ members) consistently surfaces spreadsheet governance and error-prevention as top pain points, per publicly available community discussions.

---

## Recommended MVP

**Return to the original thesis.** The rebuild abandons the AI sales co-pilot direction entirely and executes the "GitHub for spreadsheets" vision that Flike's founders identified but could not build with 2022 tooling. This is not nostalgia — it is a bet that the original problem was real, the market has since been validated by adjacent products, and the technical barriers have collapsed.

## Core Feature 1: AI-Powered Formula Audit and Generation

A sidebar plugin for Excel (via Microsoft 365 Add-in framework) and Google Sheets (via Apps Script / Workspace Add-on) that uses GPT-4o or Claude 3.5 Sonnet to generate formulas from plain-English descriptions, explain existing formulas in plain language, and flag likely errors with suggested corrections. This directly addresses the "frequent errors in spreadsheets" pain point the Müller brothers identified as foundational. Unlike Copilot for Excel, this feature is scoped specifically to financial modeling conventions — it understands DCF structures, three-statement models, and FP&A naming conventions rather than generic spreadsheet patterns.

## Core Feature 2: Version Control with Change Attribution

Git-style commit history for spreadsheet files, with per-cell change tracking, collaborator attribution, and plain-language commit messages auto-generated by the AI layer. Finance teams reviewing a model before a board presentation or audit need to know who changed what, when, and why — a workflow that neither Excel's native history nor Google Sheets' revision history adequately supports. Unlike Equals (which focuses on BI outputs), this feature targets the model-building and review process itself.

## Core Feature 3: Collaborative Review Workflows

Structured comment threads anchored to specific cells or ranges, with a formal approval/sign-off mechanism that creates an auditable record. A controller reviewing a budget model can request changes, an analyst can respond and mark resolved, and the final approved version is locked with a timestamp. This mirrors pull-request workflows from GitHub — the original product metaphor — applied to the finance team's actual review process. No current competitor offers this as a native spreadsheet layer without requiring migration to a new platform.

## What We Will NOT Build (at MVP):

- CRM integrations or sales email generation (the pivot that killed the original company)
- A standalone spreadsheet application (migration requirement is the primary reason Pigment and Anaplan lose mid-market deals)
- Mobile applications
- Custom ML models (all AI features run on third-party LLM APIs to preserve capital)

## Success Metrics:

- 50 paying finance teams (FP&A, controllers, CFO offices at companies with 50–500 employees) within 6 months of launch
- Week-4 retention ≥ 60% (measured by teams with ≥3 active sessions in week 4)
- Net Promoter Score ≥ 40 from paying customers at 90 days
- Average contract value ≥ $500/month per team (5 seats at $100/seat)

---

## Go-to-Market Strategy

**Target Customer Segment:** FP&A analysts and controllers at Series B–D technology companies with 50–500 employees — specifically companies that run their financial modeling in Excel or Google Sheets and have 3–10 people touching the same models. This segment is narrow enough to reach through community channels, large enough to support a repeatable sales motion, and underserved by both enterprise FP&A platforms (too expensive, require migration) and generic AI tools (not finance-specific). Avoid early-stage startups (too small, no budget) and public companies (compliance requirements exceed MVP scope).

**Primary Distribution Channel:** The CFO Connect community (35,000+ finance professionals, per public membership data) and the broader FP&A community on LinkedIn are the primary acquisition channels. Unlike Flike's YC-network-only strategy — which the post-mortem identifies as a structural ceiling — this approach targets the actual buyer persona directly. Tactics: (1) publish genuinely useful content on financial modeling best practices and AI-assisted FP&A workflows, targeting the LinkedIn audience that already discusses these pain points; (2) offer a free audit of one financial model as a conversion mechanism, using the AI formula-audit feature as the hook; (3) pursue a Microsoft 365 App Store listing and Google Workspace Marketplace listing for inbound discovery from enterprise IT procurement.

**Pricing Strategy:** $99/seat/month, minimum 3 seats ($297/month floor), with a 14-day free trial. Justification: Equals prices at $49–$99/seat; Causal at $50–$100/seat; the audit trail and compliance value proposition supports a premium relative to pure analytics tools. Per-seat pricing aligns incentives with team growth and mirrors how comparable tools (Lavender, Notion) have successfully monetized finance and knowledge-worker buyers.

**Differentiation vs. 2026 Competitors:** The rebuild's durable advantage is vertical specificity. Microsoft Copilot and Google Duet AI are horizontal products that cannot prioritize finance-workflow conventions without alienating their broader user bases. Equals and Causal require migration. The rebuilt Flike is the only product that combines AI-powered formula intelligence, version control, and collaborative review workflows as a layer on top of the tools finance teams already use — with no migration required and no sales-email pivot to distract the roadmap.
