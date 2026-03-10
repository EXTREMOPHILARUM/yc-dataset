# Build Plan: ZeroStorefront 2026

## Overview

ZeroStorefront (Eatgeek Inc.) was a restaurant data and marketing automation platform founded by two former Grubhub insiders in 2018–2019, built to give restaurants a unified view of their customers across fragmented delivery, POS, and marketing channels; it raised only $225K–$450K in total disclosed funding, never scaled beyond seven employees, and was acqui-hired by loyalty platform Thanx in April 2022 at terms that reflected a capital-constrained exit rather than a competitive M&A process.

Three structural shifts have converged to make this viable in 2026: delivery platforms have opened APIs under regulatory pressure, AI-powered data orchestration has eliminated the per-integration engineering bottleneck that kept the original team perpetually understaffed, and the restaurant CDP market has been validated at scale by Olo's public listing and Punchh's acquisition — proving that the demand Thanx's CEO called "not currently heavily in demand" in 2022 has since materialized. The rebuild is a vertical AI CDP for multi-location restaurant operators and ghost kitchen operators, delivering automated cross-channel attribution, LLM-generated personalized campaigns, and first-party customer ownership — without requiring a seven-person engineering team to maintain each integration.

---33:Tb1b,

## Why Now?

## The single most important change: AI-powered data orchestration has eliminated the integration engineering bottleneck that killed the original company.

## Current Market Analysis

**Market size.** The U.S. restaurant industry generates over $1 trillion in annual revenue (National Restaurant Association, 2024). The restaurant marketing technology and CDP sub-market is not cleanly segmented in public research, but Olo's ~$400M ARR and PAR Technology's $500M Punchh acquisition establish a credible floor for what the infrastructure layer alone can be worth. The ghost kitchen segment, estimated at $1B+ in U.S. revenue in 2023 by Euromonitor (exact figure not independently verified in the research report), represents an incremental addressable segment that did not exist at meaningful scale in 2019.

## Competition map and gaps.

- **Olo** (public, ~$400M ARR): Dominates online ordering infrastructure for enterprise chains (500+ locations). Weakness: built for large enterprise, pricing and implementation complexity exclude multi-location independents and ghost kitchen operators. Does not offer LLM-generated campaign content or cross-platform attribution at the SMB tier.
- **Thanx** (private, acquirer of ZeroStorefront): Loyalty and CRM for mid-market restaurants. Weakness: loyalty-first architecture means attribution and CDP capabilities remain secondary features grafted onto a points-and-rewards core. The ZeroStorefront integration appears to have been partially absorbed rather than deeply productized, given Wallace's departure five months post-close.
- **Punchh / PAR Technology**: Enterprise loyalty, 200+ brand clients. Weakness: same enterprise-tier pricing and complexity as Olo; no meaningful ghost kitchen or virtual brand offering.
- **Klaviyo / Attentive**: Horizontal email and SMS platforms with restaurant customers. Weakness: no restaurant-specific data model, no delivery platform integrations, no POS-native attribution. Restaurants using these tools are manually exporting CSVs and losing the cross-channel view ZeroStorefront was built to provide.
- **Toast Marketing** (bundled with Toast POS): Growing but POS-locked. Weakness: attribution is limited to Toast-native order data; any order placed through DoorDash, Uber Eats, or a non-Toast channel is invisible.

**Demand signals from adjacent products.** The growth of Attentive and Klaviyo in the restaurant vertical — despite their lack of restaurant-specific data models — signals that operators are actively seeking direct-to-guest communication tools and are willing to pay for them even with imperfect solutions. This is a strong proxy for demand for a purpose-built alternative.

**Defensibility analysis.** The platform incumbents (DoorDash, Uber Eats, Grubhub) have a structural disincentive to build a genuine cross-platform attribution tool, because doing so would make their own CAC contribution visible and comparable to competitors — information that would give restaurants negotiating leverage on commission rates. This is the same dynamic Wallace identified in 2019, and it remains structurally intact. Toast could theoretically build this, but its attribution would remain POS-locked. The rebuild's defensibility comes from the cross-platform data model and the proprietary behavioral dataset that accumulates with each restaurant customer added — a moat that grows with scale in a way that a single-platform incumbent cannot replicate without cannibalizing its own data advantage.

---

## Recommended MVP

## Core Feature 1: AI-Powered Cross-Platform Data Unification

Ingest order, customer, and behavioral data from DoorDash, Uber Eats, Grubhub, Toast, Square, and Yelp via their current open APIs, normalize it into a unified customer record using GPT-4-class structured output pipelines, and surface a single customer view per restaurant. This is what ZeroStorefront built manually with a full engineering team; the rebuild does it with two engineers and AI-assisted normalization. The difference is not incremental — it is the difference between a product that can onboard a new restaurant in days versus months.

## Core Feature 2: Cross-Channel Attribution Dashboard

Show restaurant operators, in plain language, which channels (DoorDash ad spend, Instagram, SMS campaign, Google listing) drove first-time customers, repeat visits, and measurable revenue — with customer acquisition cost and lifetime value calculated per channel. This was ZeroStorefront's most differentiated feature and remains the most underserved capability in the current competitive landscape. The rebuild adds LLM-generated natural language summaries of attribution data, making insights accessible to operators who are not data analysts.

## Core Feature 3: LLM-Generated Personalized Campaign Execution

From the unified customer record, automatically generate and send personalized email and SMS campaigns — win-back sequences for lapsed customers, upsell messages for high-LTV segments, reorder reminders — without requiring the restaurant to write copy or configure automation logic. This collapses the content production cost that made personalized multi-channel campaigns economically inaccessible for independent operators in 2019. The rebuild does not require a marketing team on the restaurant side; the AI generates, schedules, and sends.

## Core Feature 4: Ghost Kitchen Multi-Brand Attribution

For virtual restaurant operators running multiple brands from a single kitchen, provide brand-level attribution across delivery platforms — showing which brand's DoorDash spend is generating profitable repeat customers versus which is acquiring one-time discount seekers. This is a use case the original ZeroStorefront was architecturally suited for but that lacked sufficient market density in 2019. No current competitor offers this as a purpose-built feature.

**What we will NOT build (MVP scope):** New store location intelligence, enterprise loyalty points programs, consumer-facing apps, or POS hardware integrations beyond API-accessible systems. These were scope expansions that diluted ZeroStorefront's core value proposition without the capital to execute them.

## Success metrics with thresholds:

- 50 paying restaurant locations within 6 months of launch (validates willingness to pay)
- Net Revenue Retention > 110% at month 12 (validates that attribution insights drive measurable outcomes operators renew for)
- Average onboarding time < 3 business days (validates the AI-normalization efficiency claim)
- At least 3 ghost kitchen operators (5+ virtual brands each) as paying customers within 9 months

**Cold-start problem:** This product does not depend on network effects or local density. A single restaurant location receives value from day one — the unified customer view and attribution dashboard are useful with one location's data. There is no minimum user threshold before the core feature delivers value. The data moat grows with scale, but the individual restaurant's value is immediate.

---

## Go-to-Market Strategy

**Target customer segment (narrow and specific):** Multi-location independent restaurant operators (3–25 locations) and ghost kitchen / virtual brand operators running 3+ brands across delivery platforms, in U.S. markets with high delivery platform penetration (New York, Los Angeles, Chicago, Houston, Miami). These operators have enough order volume to make attribution meaningful, enough locations to feel the pain of fragmented data, and enough marketing spend to justify a $300–$600/month subscription — but they are too small for Olo or Punchh's enterprise sales motion and too restaurant-specific for Klaviyo.

**Primary distribution channel:** Direct outbound through restaurant industry associations (National Restaurant Association, state-level equivalents), ghost kitchen operator networks (Kitchen United, CloudKitchens tenant communities), and Toast and Square partner marketplaces. The Toast Partner Marketplace and Square App Marketplace provide distribution to operators already using those POS systems — a warm channel that ZeroStorefront did not have access to at the same scale in 2019. Secondary channel: content marketing targeting the "restaurant data" and "delivery platform attribution" search queries that operators are now actively researching, a behavior that was less common in 2019 when the category was less established.

**Pricing strategy:** $299/month for up to 3 locations (includes unified data, attribution dashboard, and 2,000 AI-generated SMS/email sends per month); $499/month for 4–10 locations; $799/month for 11–25 locations or ghost kitchen operators with 5+ brands. SMS send volume priced at marginal cost plus margin above the base tier.

*Stress test against free alternatives:* The primary free alternatives are Toast Marketing (POS-locked, no cross-platform attribution), Mailchimp free tier (no restaurant data model, manual CSV imports), and delivery platform native dashboards (single-platform, no unified view). A restaurant operator currently "accomplishing" attribution for free is doing so by manually reconciling DoorDash, Uber Eats, and Toast reports in a spreadsheet — a process that takes hours per week and produces incomplete data. The $299/month price is justified if the product saves 4+ hours of operator or manager time per month and surfaces one actionable insight per month that improves campaign ROI. At a restaurant manager's fully-loaded hourly cost of ~$25–$35, 4 hours saved equals $100–$140/month in labor alone; the attribution-driven revenue improvement is the remaining justification. This is a defensible price point, not an aspirational one.

**Differentiation vs. 2026 competitors:** Against Toast Marketing — cross-platform, not POS-locked. Against Klaviyo/Attentive — restaurant-native data model with delivery platform integrations, not a horizontal tool requiring manual data export. Against Thanx/Punchh — no loyalty program required; attribution and direct marketing as standalone products accessible to operators who do not want to run a points program. Against Olo — SMB-accessible pricing and self-serve onboarding, not an enterprise implementation project.
