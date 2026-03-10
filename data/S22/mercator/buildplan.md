# Build Plan: Mercator 2026

## Overview

The 2026 Mercator is a dbt-native AI query assistant for mid-market analytics teams. It sits between your data warehouse and your existing tools—reading your schema, your dbt models, and your team's metric definitions—to generate accurate SQL that analysts actually run without editing. Target: B2B SaaS companies with 2–8 person data teams already on Snowflake or BigQuery.

The market shift is simple: foundation models have made text-to-SQL a commodity feature, not a defensible product. What's scarce now is *context*—understanding a specific team's data semantics, governance rules, and metric definitions. By anchoring to dbt (the industry standard for analytics engineering), we own the semantic layer that every other AI analytics tool ignores or bolts on poorly.

Go-to-market is distribution, not sales. Launch a free dbt package that adds AI query generation to the dbt Hub, build in the dbt Slack community, and convert power users to a paid team tier ($399/month) for warehouse connection management and audit logs. We win the segment between open-source flexibility and enterprise bloat—the dbt-native mid-market that Vanna and DataGPT both miss.33:T719,

## Why Now?

The single most important change since Mercator's failure: **the text-to-SQL product layer is now fully commoditized at the foundation model level, which paradoxically creates the opening**. In 2024, Mercator had to spend $273 and significant engineering time fine-tuning GPT-3.5 to beat benchmarks. By 2026, GPT-4o (May 2024), Claude 3.5 Sonnet (June 2024), and Gemini 1.5 Pro achieve >70% on BIRD-SQL zero-shot, with no fine-tuning required. The technical moat Mercator was trying to build has evaporated — but that means a rebuild team can skip the infrastructure layer entirely and compete on product and distribution instead.

The cost economics have shifted dramatically in the rebuild's favor. GPT-4o mini (July 2024) runs at approximately $0.15 per million input tokens — a fraction of the GPT-4 Turbo inference costs Mercator documented at <$0.14 per query. A per-query SaaS model that was marginally viable in 2024 is now structurally profitable at scale.

Critically, the market validation Mercator had to argue for now exists empirically. Vanna.ai, Defog, and DataGPT have collectively demonstrated that enterprise buyers will pay for schema-aware natural language SQL tooling. The sales education burden — "why would I trust AI to write my SQL?" — has been absorbed by the market. Specific market data on the AI-native BI segment size in 2026 is not available in the research report, though the broader BI software market exceeded $25 billion annually as of 2023–2024.

The distribution channel that didn't exist for Mercator is now mature: **dbt Hub and the dbt Cloud integration marketplace**, serving a documented community of 40,000+ active dbt projects (dbt Labs, 2024). Data teams already living inside dbt represent a captive, high-intent audience that Mercator never had access to.

---

## Current Market Analysis

**Market Size:** The broader BI software market exceeded $25 billion annually as of 2023–2024 per the research report. The AI-native analytics sub-segment size in 2026 is not independently documented in the research materials, though venture investment in the category accelerated substantially through 2024–2025. The fleet telematics market was estimated at $20+ billion globally growing ~15% annually as of the original Mercator period; current 2026 figures are not available in the research report.

## Competition Map — Text-to-SQL / AI Analytics:

- **Vanna.ai**: Open-source-first, strong developer community, weak enterprise packaging and support SLAs. Buyers who need SOC 2 compliance and dedicated onboarding have nowhere to go.
- **Defog**: Strong on API-first integrations, limited native UI for non-technical business users. Targets developers, not the analyst persona.
- **DataGPT**: Positioned as a "conversational analyst," but pricing and sales motion skew toward large enterprise, leaving mid-market data teams underserved.
- **Tableau / Looker / ThoughtSpot**: Natural language features bolted onto legacy BI architecture. Schema awareness is shallow; query accuracy on complex joins remains poor per independent evaluations (specific 2026 benchmark data not available in research report).
- **Cursor / GitHub Copilot for SQL**: General-purpose code completion, not schema-aware in the way a purpose-built text-to-SQL product can be.

**Gap:** No current competitor owns the mid-market data team (10–100 person companies, 2–10 person data teams) with a product that combines schema-aware SQL generation, a clean analyst-facing UI, and dbt-native integration. This is the exact gap Mercator's "startups to large enterprises" positioning failed to name.

**Demand signals:** dbt's 40,000+ active project community, Snowflake's 9,000+ customer base (Snowflake FY2024 earnings), and the proliferation of modern data stack tooling all indicate a large, reachable population of data teams actively seeking productivity tooling.

---

## Recommended MVP

## Core Features:

## Schema-Aware Natural Language Query Engine

Connects directly to a user's existing data warehouse (Snowflake, BigQuery, Redshift) and ingests schema metadata, column descriptions, and sample values to generate accurate SQL from plain English. This matters because generic LLM SQL generation fails on proprietary schemas — the schema-awareness layer is where Mercator's RAG approach from the arXiv paper (arXiv:2404.12560) remains genuinely valuable. Unlike the original Dubo, this is not a standalone editor but a warehouse-native integration that meets analysts where they already work.

## dbt Semantic Layer Integration

Reads dbt model definitions, metric configurations, and documentation to ground SQL generation in the team's existing data semantics. This matters because dbt has become the de facto transformation layer for modern data teams, and any SQL tool that ignores dbt context will generate queries that conflict with established business logic. The original Mercator had no documented dbt integration; this is the primary distribution wedge.

## Query Review and Explanation Mode

For every generated query, produces a plain-English explanation of what the SQL does, flags potential performance issues (e.g., missing filters on large tables), and surfaces the confidence level of the generation. This matters because enterprise data teams will not run AI-generated SQL on production databases without auditability. This directly addresses the trust barrier that Mercator's benchmark-focused positioning never resolved.

## What We Will NOT Build:

- A proprietary SQL editor UI (use VS Code extension or warehouse-native interfaces instead)
- Fine-tuned foundation models (commodity LLMs are sufficient; Mercator proved this at $273)
- Fleet management or geospatial features
- A general-purpose BI dashboard layer

## Success Metrics:

- 50 paying teams within 6 months of launch
- Query acceptance rate (user runs generated SQL without editing) ≥ 60%
- Net Revenue Retention ≥ 110% at month 12
- Average time-to-first-value ≤ 15 minutes from warehouse connection

---

## Go-to-Market Strategy

## Target Customer Segment:

Data analysts and analytics engineers at B2B SaaS companies with 50–500 employees, 2–8 person data teams, and an existing dbt + Snowflake or BigQuery stack. This segment has budget authority at the team level (no lengthy procurement), high SQL query volume, and acute productivity pain. It is the segment Mercator's "startups to large enterprises" framing obscured entirely.

## Primary Distribution Channel:

The **dbt Hub marketplace** and **dbt Slack community** (20,000+ members as of dbt Labs 2024 figures). Tactics: (1) publish a free dbt package that adds schema documentation enrichment, creating a usage-to-paid conversion funnel; (2) sponsor dbt Community office hours and Coalesce conference; (3) direct outreach to dbt Cloud users via the integration marketplace. Secondary channel: Snowflake Marketplace and the Snowflake Partner Network, which provides access to Snowflake's 9,000+ customer base.

## Pricing Strategy:

## Differentiation vs. 2026 Competitors:

Where Vanna.ai wins on open-source flexibility and DataGPT wins on enterprise scale, this rebuild owns the **dbt-native mid-market** — a segment neither competitor has explicitly claimed. The dbt integration is not a feature; it is the distribution strategy. Every dbt project that installs the free package is a qualified lead. Mercator's original failure was competing on benchmark scores with no distribution wedge; this rebuild competes on ecosystem fit with a measurable acquisition funnel from day one.
