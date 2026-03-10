# Build Plan: Optilly/Installmonetizer 2026

## Overview

The 2026 version is a creative intelligence platform for mobile app marketers who've hit the ceiling of platform automation. It's built for Series B–D consumer apps (gaming, fintech, health) spending $50K–$500K monthly on Meta and Apple Search Ads — teams that know their CAC is stuck because black-box algorithms can't learn from creative performance across channels.

The market shift is SKAdNetwork maturity. Apple's privacy framework forced attribution to aggregate level, which broke the feedback loop that made creative optimization possible. Simultaneously, Meta's Advantage+ became so opaque that marketers lost visibility into what actually drives installs. There's now a 18-month gap between creative test and actionable insight — and no tool bridges it.

We win by making creative the variable that moves the needle again. LLM-powered variant generation produces hundreds of ad combinations from a single brief. SKAdNetwork-native dashboards translate privacy signals into creative insights. Cross-platform incrementality testing proves which creatives actually drive incremental lift, not just last-click attribution. The result: marketers regain control of their highest-leverage lever when platforms have made it invisible.34:T822,

## Why Now?

The single most important change since Optilly's failure is the commoditization of bid-level optimization by the platforms themselves. Meta's Advantage+ (launched 2022) and Google's Performance Max (launched 2021) have absorbed the exact functionality Optilly charged for in 2014 — automated bidding, audience expansion, and basic creative rotation — directly into their free native tools. This is not a threat to a rebuild; it is the prerequisite for one. It clears the field of undifferentiated competitors and forces the market to the next layer of the stack: creative intelligence and privacy-resilient measurement.

That next layer is now buildable in a way it wasn't in 2014. GPT-4 (March 2023) and Claude 3 (March 2024), combined with image generation via Midjourney v6 (December 2023) and Stable Diffusion 3 (February 2024), enable the production of thousands of ad creative variants at near-zero marginal cost. Optilly's 2014 multivariate testing engine was bottlenecked by the cost and time of producing human-made assets. That bottleneck is gone.

Simultaneously, Apple's App Tracking Transparency framework (ATT, April 2021) and the mandatory adoption of SKAdNetwork have created a measurement crisis that did not exist when Optilly operated. According to AppsFlyer's 2023 State of App Marketing report, iOS app marketers are misattributing or losing visibility into a significant share of their conversion data — the firm estimates over $7 billion in annual mobile ad spend is affected by attribution degradation. Specific figures on total misattributed spend vary by source and should be verified against current AppsFlyer and Adjust benchmark reports.

Distribution channels unavailable to Optilly now exist at scale: the Meta Business Partner directory (with direct API access to ~10M advertisers), the Shopify App Store (2M+ merchants increasingly running app-install campaigns for their mobile commerce apps), and the Apple Search Ads partner program provide structured, credentialed go-to-market paths that a 2014-era startup had to build from scratch.

---

## Current Market Analysis

The mobile app install advertising market has grown substantially since Optilly's 2014 pivot. Data.ai (formerly App Annie) estimated global app install ad spend at approximately $118 billion in 2022, up from roughly $13 billion in 2014 (Statista). The specific 2026 projection is not available in the research report, but the directional trend — continued growth driven by gaming, fintech, and commerce apps — is well-documented. Readers should verify current figures against Data.ai's 2025 State of Mobile report.

## Competition map and gaps:

- **Meta Advantage+**: Handles bid automation and basic audience targeting natively. Weakness: black-box optimization with no cross-platform creative intelligence or incrementality measurement. Marketers cannot understand *why* a creative works, only that it did.
- **AppsFlyer / Adjust**: Strong on mobile measurement and attribution. Weakness: measurement-only tools; neither offers creative generation or cross-platform campaign orchestration. AppsFlyer's SKAdNetwork support is functional but complex to implement.
- **Smartly.io**: Creative automation and campaign management for social. Weakness: expensive (enterprise-tier pricing, typically $2,000+/month), built primarily for brand advertisers rather than performance-focused app marketers. Limited probabilistic attribution capability.
- **Kenshoo (Skai)**: Cross-channel bid management. Weakness: weak on creative intelligence; primarily a reporting and budget allocation layer rather than a creative-testing engine.
- **Triple Whale / Northbeam**: Strong on e-commerce attribution. Weakness: built for DTC brands, not app-install marketers; limited SKAdNetwork and probabilistic modeling for mobile.

The gap is specific: no current tool combines LLM-powered creative generation, SKAdNetwork-native measurement, and cross-platform incrementality testing in a single workflow designed for mid-market app-install marketers spending $50K–$500K/month. Enterprise tools are too expensive; native platform tools are too opaque.

**Demand signals:** The explosion of mobile measurement consultancies (MMPs, measurement partners) and the growth of incrementality testing vendors like Measured and Recast signal acute, unmet demand for post-ATT measurement clarity.

---

## Recommended MVP

## Feature 1: LLM-Powered Creative Variant Engine

Integrates GPT-4o (May 2024) for copy generation and Stable Diffusion 3 for image variants to produce hundreds of ad creative combinations from a single brief. The marketer inputs a product description, target audience, and performance goal; the system generates structured variant sets organized for statistically valid multivariate testing. This differs from Optilly's 2014 approach, which required human-produced assets for every variant — a cost and time constraint that limited test breadth to dozens of combinations rather than hundreds.

## Feature 2: SKAdNetwork-Native Attribution Dashboard

Translates SKAdNetwork's privacy-aggregated conversion signals into actionable creative and audience insights using probabilistic modeling. Surfaces which creative clusters drive downstream retention, not just installs. This addresses the measurement crisis created by Apple ATT (April 2021) — a problem that did not exist when Optilly operated and that current native platform tools handle poorly.

## Feature 3: Cross-Platform Incrementality Testing

Runs geo-based or time-based holdout experiments across Meta and Apple Search Ads simultaneously to measure true incremental lift rather than last-touch attribution. Outputs a channel-level incrementality coefficient that informs budget allocation. This operates at a higher abstraction layer than Optilly's five-minute bid adjustments, which the platforms now handle natively.

## Feature 4: Creative Performance Memory

Maintains a structured, searchable record of every creative test result — what worked, what didn't, and under what audience and placement conditions — building a proprietary performance database per account over time. This creates compounding switching costs absent from Optilly's 2014 product.

**What we will NOT build:** A bidding engine (commoditized by Advantage+ and PMax), a publisher bundling network (the original InstallMonetizer model remains reputationally and regulatorily untenable on desktop), or a full-stack media buying agency layer.

**Success metrics:** 20 paying customers within 6 months of launch; average managed spend per customer ≥ $75K/month; 90-day net revenue retention ≥ 105%; creative engine producing statistically significant test results within 14 days of onboarding.

---

## Go-to-Market Strategy

**Target customer segment:** Mobile app marketing managers at Series B–D consumer apps (gaming, fintech, health/fitness) spending $50K–$500K/month on Meta and Apple Search Ads, who have an in-house performance team but lack dedicated measurement infrastructure post-ATT. This segment is large enough to support meaningful revenue but narrow enough to build a reference customer base quickly. They are sophisticated enough to value incrementality measurement but not so large that they have built custom internal tooling.

**Primary distribution channel:** The Meta Business Partner directory provides credentialed access to this segment with built-in trust signals. Supplemented by direct outreach through the Mobile Marketing Association and AppsFlyer's partner ecosystem, where mid-market app marketers actively seek measurement solutions. Content marketing targeting "SKAdNetwork optimization" and "post-ATT attribution" search queries addresses a high-intent, underserved keyword cluster.

**Pricing strategy:** Percentage of managed ad spend (3–5%), with a minimum monthly floor of $2,500. This aligns incentives — the product earns more when the marketer's campaigns perform better — and mirrors the pricing model familiar to this buyer from existing MMP relationships. It avoids the flat-fee SaaS trap that makes the product feel expensive before value is demonstrated. Pricing is justified by the measurement gap: if the product recovers even 10% of misattributed spend for a $100K/month advertiser, the $3,000–$5,000 fee is easily defensible.

**Differentiation vs. 2026 competitors:** Smartly.io targets enterprise brand advertisers at 3–5x the price point. Native platform tools (Advantage+, PMax) offer no cross-platform view and no creative intelligence transparency. The rebuild's differentiation is the combination of LLM-generated creative volume, SKAdNetwork-native measurement, and a proprietary creative performance memory that improves with every test — none of which any single current competitor offers in an integrated, mid-market-accessible package. Unlike Optilly's 2014 differentiation claim ("technology and account management"), this differentiation is specific, measurable, and tied to a structural market shift (ATT) that competitors built before 2021 cannot easily retrofit.
