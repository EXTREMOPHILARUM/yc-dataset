# Build Plan: Sorted 2026

## Overview

Sorted was a Copenhagen-based SaaS management platform that entered Y Combinator's Winter 2023 batch promising fully automated software license tracking, access management, and cost visibility for startups — then quietly shut down within roughly 12–18 months, never raising a seed round and leaving no public trace of traction.

The rebuild thesis is not to fix Sorted's product — it is to fix its customer. Three structural changes make this viable now: AI-powered transaction parsing has made the "fully automated" promise technically real without a large integration team; the post-ZIRP SaaS rationalization wave has created an urgent, budget-backed buyer in finance ops leaders at 50–500 person companies; and near-universal OAuth/SCIM adoption means a small team can cover 100+ integrations in months. **The new version is a finance-led SaaS spend intelligence tool that pays for itself in recovered license waste within 90 days — sold to CFOs, not founders.**

---

## Why Now?

### The single most important change: AI-powered transaction parsing has made "fully automated" technically achievable for a small team.

Sorted's core marketing claim — complete automation — was aspirational in 2022–2023. Building and maintaining integrations with dozens of SaaS APIs was engineering-intensive work that consumed teams of 50+ at Torii and BetterCloud. A two-person team could not credibly deliver it. That constraint no longer applies in the same way. Large language models with tool-use capabilities — specifically GPT-4 Turbo (November 2023) and Claude 3.5 Sonnet (June 2024) — can parse bank and corporate card transaction feeds, classify vendors, identify subscription patterns, and flag anomalies with high accuracy without requiring a hand-built integration for every vendor. A rebuild team can achieve meaningful SaaS discovery coverage from day one by connecting to a single financial data source rather than building 100 individual API integrations.

**The buyer has changed.** Post-ZIRP budget pressure in 2023–2024 created a new urgency in finance operations. According to Gartner (2024), organizations waste an estimated 25–30% of their SaaS spend on unused or underutilized licenses — a figure that has become a board-level conversation at companies that were previously indifferent to software sprawl. CFOs and finance ops leaders at 50–500 person companies are now actively auditing software spend in a way that did not exist with the same urgency when Sorted launched. This is a buyer with a budget line, a measurable ROI requirement, and a willingness to pay for tools that demonstrably reduce costs.

**Protocol infrastructure has matured.** OAuth 2.0 and SCIM adoption among SaaS vendors has become near-universal since 2022. Platforms like Merge.dev and Apideck now offer unified API layers covering 100+ SaaS integrations, meaning a rebuild team can access provisioning and user data across the major tools without building each connector from scratch. This directly addresses the scope risk that constrained Sorted's two-person team.

**Distribution channels now exist that did not in 2022.** Ramp's software management module and Brex's spend analytics have demonstrated that finance teams will adopt SaaS management tooling when it is embedded in their existing financial workflows — validating a finance-first distribution path through accounting software integrations (QuickBooks, NetSuite) and corporate card partnerships.

---

## Current Market Analysis

**Market size:** The global SaaS management platform market was valued at approximately $3.4 billion in 2023 and is projected to reach $7.9 billion by 2028 (MarketsandMarkets, 2023). The adjacent software asset management market adds several billion more. Sorted's original target — self-serve SaaS management for early-stage startups — was a small, low-willingness-to-pay slice of this. The rebuild targets the 50–500 person company segment, which represents a meaningfully larger and better-monetizable portion of the addressable market. Precise TAM figures for this specific sub-segment are not publicly available.

## Competition map and gaps:

- **Torii** (founded 2017, raised ~$50M): Strong on discovery and workflow automation, but priced and positioned for 500+ person enterprises. Onboarding requires IT involvement and weeks of setup. Weakness: inaccessible to the 50–200 person company that lacks a dedicated IT team.
- **BetterCloud** (founded 2013, raised ~$187M): Deep on Google Workspace and Microsoft 365 governance, but narrow in SaaS coverage outside those ecosystems. Weakness: not finance-led; ROI story is security and compliance, not cost savings.
- **Zylo** (raised ~$72M): Explicitly enterprise-focused, with a sales-assisted motion and pricing that starts well above SMB budgets. Weakness: structurally inaccessible to the rebuild's target segment.
- **Ramp's software management module**: The most direct competitive threat. Ramp has distribution, trust with finance teams, and an existing spend data layer. Weakness: it is a feature within a corporate card product, not a standalone tool — companies not on Ramp cannot access it, and its depth is limited relative to a dedicated product.
- **Rippling**: Bundles SaaS provisioning into HR/IT, but requires full platform adoption. Weakness: companies already on a different HRIS will not switch platforms for SaaS management alone.

**Demand signals:** Ramp's rapid growth (reported $300M+ ARR in 2024, per public statements) and the expansion of Brex's spend analytics confirm that finance teams at growth-stage companies are actively seeking software cost visibility. The gap is a standalone, finance-led SaaS intelligence tool that works regardless of which corporate card or HRIS a company uses.

**Defensibility analysis:** The honest answer is that Ramp and Brex could build this feature more deeply and distribute it to their existing customer bases. The structural defense is not technical — it is neutrality. A standalone tool that connects to any bank feed, any corporate card, and any HRIS is more useful to a CFO who does not want to be locked into a single financial platform. Ramp's SaaS module only works if you use Ramp. The rebuild's defensibility depends on becoming the card-agnostic, HRIS-agnostic layer — a position that platform incumbents are structurally motivated to leave open. This is a real but narrow moat; it must be built quickly before one of the platforms decides neutrality is worth replicating.

---

## Recommended MVP

### Core features:

**1. AI-powered SaaS discovery via transaction feed parsing.** Connect to a corporate card feed or bank account (via Plaid or direct CSV import) and automatically identify every SaaS subscription the company is paying for, including shadow IT purchases made on personal cards that get expensed. This is the entry point — it delivers immediate value without requiring any IT involvement or manual data entry. Unlike Sorted's original approach, which likely required individual tool integrations, this works from a single financial data connection and uses LLM classification to handle vendors it has never seen before.

**2. License utilization scoring.** For the top 20–30 most common SaaS tools (Google Workspace, Slack, Notion, Zoom, Salesforce, etc.), connect via OAuth to pull actual login and activity data and compare it against the number of paid seats. Surface a ranked list of "waste candidates" — licenses being paid for but not actively used — with a dollar figure attached to each. This is the ROI engine: it converts the product from a visibility tool into a cost-recovery tool. The original Sorted claimed this capability; the rebuild delivers it with a concrete savings estimate on the dashboard from day one.

**3. Renewal calendar and spend forecasting.** Parse contract terms and billing cycles from transaction history to build a forward-looking renewal calendar. Alert finance ops leaders 30, 60, and 90 days before major renewals with utilization data and a recommended negotiating position. This is the feature that creates recurring engagement — the product becomes part of the quarterly budget review process, not just an onboarding exercise.

**What you will NOT build (MVP scope):** Full SCIM-based provisioning and deprovisioning workflows, compliance audit automation, security policy enforcement, or an employee-facing app catalog. These are real features that belong in a later version, but they require IT buyer involvement and extend the sales cycle. The MVP is a finance tool, not an IT tool.

## Success metrics:

- 50 paying customers within 6 months of launch, each paying at least $200/month
- Average identified license savings ≥ 3× the monthly subscription cost within 30 days of activation (the core ROI proof point)
- 60-day retention ≥ 75% (the product must become a habit, not a one-time audit)
- Time to first "waste candidate" surfaced: under 10 minutes from account connection

**Cold-start problem:** This product does not depend on network effects or local density. Value is delivered to a single company from the moment their transaction feed is connected. There is no minimum user threshold. The cold-start risk is integration coverage — if a company's primary SaaS tools are not in the OAuth library, the utilization scoring feature is incomplete. Mitigate by launching with coverage for the 25 most common SaaS tools (which account for the majority of spend at 50–500 person companies) and being transparent about current coverage limits.

---

## Go-to-Market Strategy

**Target customer segment:** Finance ops leaders and CFOs at B2B SaaS companies with 50–300 employees, $5M–$50M ARR, and a SaaS stack of 30+ tools. This segment has a dedicated finance function (unlike early-stage startups), a real budget for software rationalization, and enough SaaS complexity to generate meaningful savings. They are not yet large enough to have a dedicated IT team running a formal SMP procurement process (unlike enterprise buyers), which means the finance leader can make the purchase decision unilaterally.

**Primary distribution channel:** Outbound to finance ops communities (CFO Alliance, Pavilion Finance, SaaStr community) combined with integration-led distribution through accounting platforms. A QuickBooks or NetSuite app listing puts the product in front of finance teams at the moment they are already thinking about software costs. This is a channel Sorted never had access to and that larger incumbents have not prioritized because their enterprise sales motions do not depend on it.

**Tactics:** (1) Cold outbound to finance ops leaders at Series A/B SaaS companies with a personalized "we found $X in potential waste at companies like yours" hook — this requires running the analysis on publicly available data to make the outreach credible. (2) Content marketing targeting "SaaS spend audit" and "software license waste" search queries, which have high commercial intent and relatively low competition. (3) Partnerships with CFO-focused fractional finance firms who advise multiple portfolio companies simultaneously.

**Pricing:** $299/month flat for companies up to 100 employees; $599/month for 101–300 employees. Annual plans at a 20% discount. No free tier — a 14-day free trial with full feature access instead.

**Price stress-test:** The honest competitive pressure here is Ramp's software management module, which is free for Ramp customers. A CFO already on Ramp has a reasonable free alternative. The $299/month price is justified only if the product (a) works for companies not on Ramp, (b) covers more SaaS tools than Ramp's module, and (c) provides deeper utilization data and renewal forecasting. If the rebuild cannot demonstrate meaningfully better savings identification than Ramp's free feature within the trial period, the price will not hold. The pricing strategy therefore depends entirely on delivering a demonstrably superior ROI story — not on brand, not on features, but on the dollar figure on the dashboard. If the average customer recovers $1,500/month in license waste, $299/month is an easy sell. If the average recovery is $400/month, the product is not ready to charge.

**Differentiation vs. 2026 competitors:** The rebuild's primary differentiator is card-agnostic, HRIS-agnostic finance-led discovery — it works regardless of which corporate card, bank, or HR system a company uses. Ramp and Brex require platform adoption. Torii and Zylo require IT involvement and enterprise procurement. The rebuild is the only option for a CFO at a 100-person company who wants a 10-minute setup, a clear savings estimate, and no IT ticket required.
