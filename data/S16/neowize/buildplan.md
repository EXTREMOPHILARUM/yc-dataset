# Build Plan: NeoWize 2026

## Overview

The 2026 NeoWize is a semantic personalization engine for mid-market Shopify merchants ($5M–$100M GMV) who already own their customer data stack. Instead of asking retailers to trust a black box, we show them exactly why each product recommendation appears—and prove lift through server-side A/B testing before they pay. The product lives in the API layer, not JavaScript, so it works across every channel and survives ad blockers.

The shift that makes this work now: LLMs can generate rich semantic embeddings from product catalogs instantly, eliminating the cold-start problem that plagued the original company. Merchants now expect to own their data and integrate tools via APIs, not hand everything to a SaaS vendor. And Shopify's Hydrogen and Statsig's experimentation APIs didn't exist in 2019—they're table stakes now.

We win by being the only player focused on merchants who already use Segment or Klaviyo, charging per-transaction lift rather than flat fees. Enterprise competitors like Dynamic Yield start at $100K/year and require implementation teams. We start free, prove ROI in 30 days, and scale with the merchant's revenue.34:T914,

## Why Now?

The single most important change since NeoWize's 2019 acquisition is the arrival of large language models capable of generating rich semantic product embeddings from unstructured catalog data — eliminating the cold-start problem that was NeoWize's entire technical reason for existing.

NeoWize's core innovation was reducing the behavioral interactions needed to infer preferences from ~50 to ~5. In 2026, that number is effectively zero. GPT-4 (March 2023) and its successors can compute zero-shot semantic similarity between a product catalog and a new visitor's first click — before any behavioral signal is collected — by embedding product descriptions, reviews, and images into a shared vector space. A rebuilt NeoWize doesn't need to solve cold-start; it starts warm by default.

This matters because the original technical moat has inverted into a distribution opportunity. The capability NeoWize spent years building can now be provisioned in days, which means the competitive advantage in 2026 belongs to whoever reaches merchants fastest and builds switching costs through data accumulation — not whoever has the best ML research team.

The distribution channel NeoWize used has also scaled dramatically. Shopify reported 4.6 million active merchants in 2023 (source: Shopify investor relations), compared to a far smaller base in 2016 — roughly a 10x expansion of the addressable merchant pool through the same zero-configuration plugin model. The Shopify App Store now hosts over 10,000 apps, meaning organic discovery is harder but the merchant base is large enough to support meaningful revenue even at modest conversion rates.

The mid-market personalization segment ($10M–$500M GMV merchants) has been validated as a paying market by Dynamic Yield's ~$300M acquisition by McDonald's (2019) and subsequent acquisition by Mastercard (2022), and by Nosto raising $40M+ (source: Crunchbase). These exits confirm enterprise and mid-market willingness to pay for exactly the capability NeoWize was building — at price points far above what SMB Shopify plugins could command.

Real-time behavioral data infrastructure — Segment, Rudderstack, Snowplow — is now available via API, eliminating the proprietary data pipeline engineering that consumed significant resources on a 3-person team in 2016.

## Current Market Analysis

The global e-commerce personalization market was valued at approximately $1.1 billion in 2021 and is projected to reach $3.8 billion by 2028 at a CAGR of roughly 19% (source: Fortune Business Insights). The SMB segment NeoWize originally targeted has grown in merchant count but remains constrained in per-merchant willingness to pay; the mid-market segment ($10M–$500M GMV) has emerged as the highest-value underserved tier.

## Current competitor map and gaps:

- **Dynamic Yield** (now Mastercard): Enterprise-focused, minimum contracts typically $100K+/year, requires dedicated implementation teams. Gap: completely inaccessible to mid-market merchants without enterprise IT resources.
- **Nosto**: The closest analog to the original NeoWize, Shopify-native, raised $40M+. Weakness: product recommendation logic is primarily collaborative filtering; cold-start performance on catalogs under 10,000 SKUs remains weak. Pricing starts around $99/month but scales opaquely, creating trust issues with mid-market buyers.
- **Bloomreach**: Strong on search and content; personalization layer is secondary and requires significant implementation. Weakness: 3–6 month onboarding cycles, priced for enterprise ($2,000+/month).
- **LimeSpot / Rebuy**: Shopify-native, SMB-focused, priced $50–$300/month. Weakness: no semantic understanding of products; purely behavioral, meaning cold-start performance is poor and catalog-level intelligence is absent.

**Demand signals from adjacent products:** Klaviyo's $6.9B IPO (2023) validated that mid-market e-commerce merchants will pay meaningfully for data-driven personalization in adjacent channels (email, SMS). Merchants already paying $500–$2,000/month for Klaviyo are a pre-qualified audience for on-site personalization at similar price points.36:Ta1e,

## Recommended MVP

## Feature 1: Semantic Cold-Start Engine

On merchant install, the system ingests the full product catalog — titles, descriptions, tags, images — and generates semantic embeddings using a hosted embedding model (e.g., OpenAI text-embedding-3-large, available since January 2024). From the first visitor's first click, the engine surfaces semantically similar products without requiring any prior behavioral data. This directly replaces NeoWize's active machine learning approach with a capability that performs equivalently on day one, at a fraction of the engineering cost.

## Feature 2: Behavioral Signal Accumulation via Rudderstack or Segment Integration

Rather than building proprietary event pipelines, the MVP connects to the merchant's existing Segment or Rudderstack workspace (or provisions a lightweight SDK) to capture hover, scroll, and click events. As behavioral data accumulates, the personalization layer shifts from pure semantic similarity toward a hybrid semantic-behavioral model. This mirrors NeoWize's original architecture but eliminates the data pipeline engineering that consumed disproportionate resources on a small team.

## Feature 3: Server-Side Personalization via Shopify Hydrogen / Storefront API

Personalization logic is injected at the API layer rather than via client-side JavaScript, eliminating the page-load penalties and ad-blocker vulnerabilities that plagued 2016-era plugin tools. For merchants on headless stacks (Hydrogen, Commerce.js), this is a first-class integration; for traditional Shopify themes, a lightweight server-side middleware handles injection. This is architecturally distinct from the original NeoWize and from current competitors like Nosto and LimeSpot, which remain client-side.

## Feature 4: Revenue-Lift Dashboard with Integrated A/B Testing via Statsig

Using Statsig's experimentation API (available since 2021), the MVP replicates NeoWize's original free-trial proof model — personalization runs on a configurable percentage of traffic, and revenue lift is reported in a merchant-facing dashboard — without requiring custom A/B testing infrastructure. This preserves the core sales motion Justin Kan identified as NeoWize's strongest go-to-market asset.

**What we will NOT build:** A standalone analytics product, mobile app personalization, multi-channel orchestration, or any vertical outside e-commerce. No custom data warehouse integrations in the first 12 months.

**Success metrics:** 50 paying mid-market merchants within 6 months of launch; average contract value ≥ $500/month; measured revenue lift ≥ 8% in merchant A/B tests; monthly gross revenue retention ≥ 90%.

## Go-to-Market Strategy

**Target customer segment:** Shopify Plus and Shopify Advanced merchants generating $5M–$100M in annual GMV, with existing Klaviyo or Segment subscriptions as a qualifying signal. These merchants have demonstrated willingness to pay for data infrastructure, have catalogs large enough to benefit from semantic personalization, and are underserved by both SMB tools (LimeSpot, Rebuy) and enterprise platforms (Dynamic Yield, Bloomreach). This is a narrower target than NeoWize's original SMB focus and a more accessible entry point than the full enterprise tier.

**Primary distribution channel:** The Shopify App Store (2M+ merchants on paid plans as of 2023, per Shopify investor relations) provides organic discovery, but the primary acquisition motion for mid-market merchants is partner-led: Shopify Plus agency partners (there are 5,000+ certified Shopify Partners globally) who implement stores for exactly this merchant segment. A 20% referral commission to agency partners is standard in the ecosystem and creates a scalable, low-CAC channel that NeoWize did not appear to pursue.

Secondary channel: direct outreach to Klaviyo customers via the Klaviyo App Marketplace, positioning the product as the on-site complement to Klaviyo's email personalization — a natural cross-sell framing that requires no education about the category.

**Pricing strategy:** Three tiers. A free tier capped at 1,000 monthly visitors (seeding the Shopify App Store review base). A Growth tier at $299/month for up to 50,000 monthly visitors. A Scale tier at $799/month for up to 250,000 monthly visitors, including the Segment/Rudderstack integration and server-side injection. These price points are 3–5x above SMB tools and 70–80% below enterprise platforms — deliberately occupying the mid-market gap. Annual prepay at 20% discount to improve cash flow and reduce churn.

**Differentiation vs. 2026 competitors:** The rebuilt NeoWize's primary differentiator is semantic cold-start performance — measurably better product recommendations on day one for catalogs under 50,000 SKUs, where collaborative filtering tools like Nosto underperform. The server-side architecture is a secondary differentiator for the growing headless commerce segment, where client-side tools cannot operate. The integrated A/B testing dashboard, powered by Statsig rather than custom infrastructure, preserves NeoWize's original proof-of-value sales motion while reducing implementation time from weeks to hours — directly addressing the switching cost problem that made the original product easy to replace.
