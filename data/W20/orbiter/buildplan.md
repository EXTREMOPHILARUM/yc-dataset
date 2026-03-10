# Build Plan: Orbiter 2026

## Overview

The single most important change since Orbiter's failure is the emergence of LLM-powered reasoning as a practical, affordable capability for small teams. In 2020, automated root cause analysis — explaining *why* a metric dropped, not just *that* it dropped — required either a large data engineering team or expensive proprietary ML infrastructure that Orbiter couldn't build on a pre-seed budget. GPT-4 (March 2023) and Claude 3 (March 2024) changed this equation entirely: a rebuilt Orbiter can now query a warehouse's metadata API, pull recent schema changes, inspect dbt model lineage, and ask an LLM to synthesize a plain-English explanation of a metric anomaly — all in a single API call costing fractions of a cent. This collapses what was previously a multi-engineer workflow into a product feature a two-person team can ship.

The second structural shift is the standardization of the modern data stack. In 2020, the analytics ecosystem was fragmented across dozens of warehouse configurations, custom SQL dialects, and bespoke pipeline architectures. By 2026, the market has consolidated: Snowflake reported 9,820 customers as of fiscal year 2024 (Snowflake Q4 FY2024 earnings), BigQuery serves millions of projects, and Databricks crossed 10,000 customers in 2023. Each platform now exposes native metadata APIs, query history endpoints, and access logs — meaning a rebuilt Orbiter can achieve deeper, more reliable integrations in weeks rather than the months it would have taken in 2020.

Critically, dbt has become the de facto transformation layer for mid-market data teams, with over 50,000 companies using dbt Cloud or dbt Core as of 2024 (dbt Labs, 2024). The dbt semantic layer and dbt Metrics codify business metric definitions in version-controlled YAML — a rebuilt Orbiter can hook directly into these definitions rather than inferring metrics from raw SQL, which was almost certainly a major source of false positives in Orbiter's original ML models.

Distribution friction has also collapsed. Slack's Workflow Builder, Microsoft Teams' adaptive card ecosystem, and the normalization of bot-delivered operational alerts mean that a non-engineering team receiving an automated metric alert in 2026 requires zero change management. In 2020, this was a novel behavior that required selling. Today it is expected.

The Slack App Directory currently lists over 2,600 apps with 750,000+ daily active users on the platform (Slack, 2023 — more recent figures not publicly available). The specific mid-market segment — companies with 50–500 employees on Snowflake or BigQuery with an active dbt project — is addressable through dbt's own partner ecosystem and Snowflake's partner marketplace, both of which did not exist as meaningful distribution channels in 2020.

---

## Why Now?

## Current Market Analysis

**Market size:** The global data observability market was valued at approximately $1.5B in 2023 and is projected to reach $4.5B by 2028 at a 24.5% CAGR (MarketsandMarkets, 2023). These figures cover the full observability stack; the specific sub-segment of business metric monitoring for non-engineering users is not separately sized in any public source, and any figure here would be fabricated. What is confirmed: Monte Carlo's $1.6B valuation (May 2022) and Bigeye's $66M raise (September 2021) validate that enterprises pay significant sums for this category. The market existence risk Orbiter faced in 2020 is gone.

## Competition map and gaps:

- **Monte Carlo** ($236M raised, ~$1.6B valuation): Dominates enterprise data observability with a focus on data pipeline reliability and data quality for engineering and data teams. Minimum contract sizes are reported in the $50K–$100K+ ARR range (unverified; based on sales motion signals and G2 reviews). Weakness: explicitly not targeting non-engineering business users; onboarding requires data engineering involvement; pricing excludes mid-market.

- **Bigeye** ($66M raised): Similar enterprise positioning to Monte Carlo, focused on data quality monitoring at the pipeline level. Weakness: same structural gap — built for data engineers, not product managers or growth analysts.

- **Anomalo**: Enterprise data quality, similar profile. No publicly disclosed funding post-2022.

- **Amplitude, Mixpanel**: Analytics platforms that have added native anomaly alerting. Weakness: only monitor events they ingest; cannot monitor warehouse-native metrics (revenue, margin, inventory) or metrics defined outside their own event schema. A company tracking revenue in Snowflake and user behavior in Amplitude has no unified monitoring layer.

- **Datadog** (market cap ~$40B as of early 2025): Has expanded into business metrics monitoring but remains engineer-configured and engineer-operated. Weakness: non-engineers cannot self-serve; pricing is infrastructure-oriented.

**Demand signals:** The explosive growth of the "analytics engineer" role (dbt's 2024 community survey reports 40,000+ active practitioners) and the proliferation of self-serve BI tools (Metabase, Lightdash, Evidence) signal that mid-market companies are investing in data infrastructure without necessarily having dedicated data observability budgets. These companies have metric definitions in dbt but no automated monitoring layer.

**Defensibility analysis:** The honest answer is that this is a real risk. Amplitude could extend anomaly detection to warehouse-connected metrics; dbt Labs could build native alerting into dbt Cloud; Snowflake could add metric monitoring to its native apps marketplace. The structural defense is not technology — it is workflow specificity. A rebuilt Orbiter that deeply integrates LLM-generated root cause explanations into the non-engineer's decision workflow (Slack threads, Linear tickets, Notion pages) becomes stickier than a feature checkbox in a data platform. The original Orbiter had no such depth. That said: if dbt Labs ships native metric alerting with LLM explanations in dbt Cloud, this rebuild faces an existential threat. Founders should monitor dbt Labs' product roadmap as a leading indicator.

---

## Recommended MVP

## Core Feature 1: dbt Semantic Layer Integration with Anomaly Detection

Connect to a customer's dbt project (Cloud or Core via dbt Artifacts) and automatically discover all defined metrics. Run statistical anomaly detection — using a combination of simple time-series methods (STL decomposition, z-score on rolling windows) augmented by GPT-4o (released May 2024) for contextual interpretation — against warehouse query results on a configurable schedule. This differs from the original Orbiter in a critical way: rather than inferring what metrics matter from raw SQL, the rebuilt product reads metric definitions the customer has already written, eliminating the configuration burden and dramatically reducing false positives.

## Core Feature 2: LLM-Generated Root Cause Explanations

When an anomaly is detected, automatically query the warehouse's metadata API (Snowflake Information Schema, BigQuery INFORMATION_SCHEMA) for recent schema changes, inspect dbt model lineage for upstream failures, and synthesize a plain-English explanation delivered alongside the alert: "Revenue dropped 18% yesterday. The `orders` model shows a 34% drop in rows processed at 2:14 AM, coinciding with a schema change to the `payments` source table." This is the feature Orbiter described wanting to build but could not execute on 2020-era ML. It is now a prompt-engineering problem, not an ML research problem.

## Core Feature 3: Slack and Teams Alert Delivery with Feedback Loop

Deliver alerts as structured messages in Slack or Microsoft Teams with one-click feedback buttons ("This was a real issue" / "False positive"). Feedback is logged and used to tune detection sensitivity per metric. This mirrors Orbiter's original feedback loop design but benefits from Slack's Block Kit (mature since 2019) and Teams' Adaptive Cards for richer, more actionable alert formatting.

## What you will NOT build (MVP):

- Custom ML model training per customer
- Support for non-dbt metric definitions (raw SQL, Looker LookML, Tableau calculated fields) — this is a V2 problem
- A standalone dashboard or web UI beyond basic configuration — alerts live in Slack/Teams
- Enterprise SSO, SOC 2 compliance, or custom data residency — pursue these only after $500K ARR

## Success metrics:

- 20 paying customers within 6 months of launch
- Alert-to-feedback rate ≥ 40% (users engaging with alerts, not ignoring them)
- False positive rate ≤ 15% as reported by user feedback within 90 days of onboarding
- Net Revenue Retention ≥ 100% at month 12

**Cold-start problem:** This product does not depend on network effects or local density. Value is delivered to a single user on day one — the moment the first anomaly alert fires with a coherent root cause explanation, the product has demonstrated its value. The minimum viable dataset is any dbt project with at least 30 days of metric history in the connected warehouse, which is a low bar for any company that has been using dbt for more than a month.

---

## Go-to-Market Strategy

**Target customer segment:** Data-forward mid-market companies (50–500 employees) with an active dbt Cloud subscription, a Snowflake or BigQuery warehouse, and at least one analytics engineer or data analyst on staff — but without a dedicated data observability budget or a data engineering team large enough to configure Monte Carlo. Concretely: Series A and Series B SaaS companies, e-commerce operators, and marketplace businesses where a metric drop has direct revenue consequences and where the person who owns the metric (a PM or growth lead) is not the person who can investigate it (a data analyst). This is the exact customer Orbiter's founders described from their own experience at Tesla and DoorDash.

**Primary distribution channel:** The dbt Partner Ecosystem and dbt Hub. dbt Labs maintains a curated list of integrations; a rebuilt Orbiter listed as a native dbt semantic layer integration reaches the exact ICP at the moment they are already thinking about their metric infrastructure. Secondary channel: Snowflake Marketplace and the Snowflake Startup Program, which provides co-selling support and access to Snowflake's 9,820-customer base. Both channels were unavailable to Orbiter in 2020.

**Pricing strategy:** $500/month flat for up to 50 monitored metrics and 5 connected Slack/Teams channels; $1,000/month for up to 200 metrics. Annual plans at 20% discount.

Stress test against free alternatives: A PM can approximate this workflow today using Slack's built-in scheduled reports from Amplitude (free tier), manual SQL queries, or a homemade dbt test with a Slack webhook. The free alternative is meaningfully worse — it requires someone to remember to check, it doesn't explain anomalies, and it doesn't cover warehouse-native metrics outside Amplitude's event schema. The $500/month price is justified if it replaces 2–3 hours per week of analyst time spent on manual metric review; at a $120K analyst salary, that's ~$12K/year of labor cost, making $6K/year in software a straightforward ROI conversation. The price is *not* justified for a company where the analyst genuinely enjoys the manual review process or where metric volume is too low to generate meaningful alerts. Qualify out these customers early.

**Differentiation vs. 2026 competitors:** Monte Carlo and Bigeye require data engineering involvement to configure and are priced for enterprise procurement cycles. Amplitude's native alerting only covers Amplitude-ingested events. A rebuilt Orbiter is the only product that (a) reads metric definitions from dbt without additional configuration, (b) delivers LLM-generated root cause explanations in plain English, and (c) is priced and onboarded for a single analytics engineer to activate in an afternoon without a sales call.
