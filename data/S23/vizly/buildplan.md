# Build Plan: Vizly 2026

## Overview

## Why Now?

## Current Market Analysis

The global business intelligence and analytics software market was valued at approximately $29 billion in 2023 (source: research report); analyst projections for 2026 are not confirmed in the provided research and should be independently verified before fundraising. The AI-augmented analytics subcategory has grown substantially, driven by enterprise AI adoption budgets that expanded post-2023.

## Competitive landscape in 2026:

*Platform incumbents* — Microsoft Copilot in Power BI and Excel, Google Duet AI in Looker and Sheets — dominate the horizontal market. Their specific weakness is data residency: both require data to transit Microsoft or Google cloud infrastructure, making them non-starters for regulated industries under HIPAA, SOC 2 Type II, FedRAMP, or EU data sovereignty requirements.

*Dedicated AI BI tools* — ThoughtSpot (well-capitalized, enterprise sales team, but cloud-only and expensive, typically $100K+ annual contracts), Julius AI (strong prosumer traction but no on-premises offering), Rows.com (spreadsheet-native, cloud-only). None offer true local deployment.

*OpenAI Advanced Data Analysis* — free for ChatGPT Plus subscribers, zero setup friction, but sends all data to OpenAI servers. Banned outright at many regulated enterprises.

**The gap:** No well-resourced competitor currently offers a vertical-specific, on-premises AI analytics product with a sub-$500/month entry price point targeting mid-market regulated companies (50–500 employees). ThoughtSpot is too expensive for this segment. Microsoft and Google are architecturally disqualified. Julius AI and Rows are cloud-only.

**Demand signals from adjacent products:** Coefficient's fundraise validates spreadsheet-native AI analytics as a paying category. The growth of privacy-focused AI coding tools (Continue.dev, Cursor's local mode) demonstrates enterprise willingness to pay a premium specifically for on-premises AI inference. Healthcare-specific data tools (Abridge, Nabla) show that vertical focus dramatically accelerates enterprise sales cycles.

---

## Recommended MVP

## Core Feature 1: On-Premises Natural Language Query Engine

Connects to a single data source — initially PostgreSQL and Google Sheets only — and translates plain English questions into SQL or Python using a locally hosted Llama 3.1 70B instance via Ollama, with an optional cloud-fallback to Claude Haiku for complex queries. This is the product Vizly built, but with 2024-generation model quality that eliminates the accuracy gap that made the 2023 version a hard sell. Unlike the original, the model selection is invisible to the end user; the system routes automatically based on query complexity and data sensitivity settings configured by the IT administrator at setup.

## Core Feature 2: Compliance-Ready Audit Log

Every query, every generated SQL statement, and every result is logged locally with user attribution, timestamp, and data source reference — exportable as a PDF or CSV for compliance review. This feature did not exist in Vizly's documented product. It directly addresses the CISO objection that AI-generated queries create unauditable data access patterns, and it is the feature that converts a security conversation from a blocker into a buying signal.

## Core Feature 3: Google Workspace Add-On with Local Relay

A Google Sheets add-on (distributed via Google Workspace Marketplace) that routes queries through a lightweight local relay agent the IT team installs once. Individual users get a familiar spreadsheet interface; data never leaves the organization's network. This solves Vizly's distribution problem — the Chrome extension was the right instinct, but without the local relay architecture, it could not serve regulated enterprises.

**What we will NOT build:** Multi-database connectors beyond PostgreSQL and Google Sheets, custom visualization builders, mobile apps, multi-LLM model selection UI, or any consumer-facing free tier. Vizly's scope was too broad for a two-person team; this rebuild ships one workflow exceptionally well.

**Success metrics:** 10 paying customers at $500+/month within 6 months of launch; query accuracy rate (correct SQL on first attempt, validated by user acceptance) above 85% in user testing; setup time under 2 hours for a non-technical IT administrator.

---

## Go-to-Market Strategy

**Target customer segment:** IT or data managers at U.S.-based healthcare organizations with 50–500 employees — specifically outpatient clinic groups, regional hospital networks, and health-tech companies that handle PHI under HIPAA and have already banned or restricted ChatGPT and Microsoft Copilot for internal analytics. This segment has a documented, budget-backed pain point (HIPAA-compliant AI analytics), a clear economic buyer (CTO or CISO), and a faster sales cycle than large enterprise — typically 30–90 days versus 6–12 months. Vizly's horizontal ICP made every sales conversation a custom negotiation; this rebuild enters every conversation with a pre-built compliance narrative.

**Primary distribution channel:** Direct outbound to healthcare IT decision-makers via LinkedIn Sales Navigator, combined with presence in HIMSS (Healthcare Information and Management Systems Society) community forums and the Google Workspace Marketplace for inbound discovery. The Workspace Marketplace listing serves as a low-friction proof-of-concept entry point; the local relay architecture converts Marketplace installs into enterprise conversations.

**Pricing:** $499/month per organization (up to 25 users), billed annually at $4,999/year — a 17% discount that incentivizes annual commitment. This is 25x Vizly's maximum price point, aligned with mid-market healthcare SaaS benchmarks, and still dramatically below ThoughtSpot's entry price. A 14-day free trial with a mandatory IT setup call replaces the open free tier, ensuring every trial involves a qualified buyer.

**Differentiation vs. 2026 competitors:** The combination of on-premises inference, HIPAA-specific audit logging, and Google Workspace-native distribution is not offered by any current competitor at this price point. Microsoft Copilot requires cloud data transit. ThoughtSpot requires enterprise procurement. Julius AI has no compliance story. This rebuild wins on the intersection of compliance credibility and deployment simplicity — the exact gap Vizly identified but could not close.
