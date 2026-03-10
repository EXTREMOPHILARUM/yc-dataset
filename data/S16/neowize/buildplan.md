# Build Plan: NeoWize 2026

## Overview

The 2026 NeoWize is a semantic personalization engine for mid-market Shopify merchants ($5M–$100M GMV) who already own their customer data stack. Instead of asking retailers to trust a black box, we show them exactly why each product recommendation appears—and prove lift through server-side A/B testing before they pay. The product lives in the API layer, not JavaScript, so it works across every channel and survives ad blockers.

The shift that makes this work now: LLMs can generate rich semantic embeddings from product catalogs instantly, eliminating the cold-start problem that plagued the original company. Merchants now expect to own their data and integrate tools via APIs, not hand everything to a SaaS vendor. And Shopify's Hydrogen and Statsig's experimentation APIs didn't exist in 2019—they're table stakes now.

We win by being the only player focused on merchants who already use Segment or Klaviyo, charging per-transaction lift rather than flat fees. Enterprise competitors like Dynamic Yield start at $100K/year and require implementation teams. We start free, prove ROI in 30 days, and scale with the merchant's revenue.34:T914,

## Why Now?

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
