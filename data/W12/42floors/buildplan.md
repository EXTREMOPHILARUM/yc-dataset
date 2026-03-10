# Build Plan: 42Floors 2026

## Overview

42Floors launched in March 2012 as a consumer-grade search engine for commercial office space, raised $17.4M from NEA, Bessemer, Thrive Capital, and Andreessen Horowitz, and spent seven years trapped between brokers who controlled the listing data it needed and a monetization layer it could never reach — before being acquired by Knotel in 2018, passing through bankruptcy, and ending as a redirected URL inside Yardi's CommercialCafe in May 2024.

The rebuild thesis is not to try again at the same problem with better design. Three structural changes make a different attack viable in 2026: LLMs can now extract structured listing data from unstructured broker documents without broker cooperation, the WeWork and Knotel bankruptcies have left the sub-5,000 sq ft flex market without a dominant discovery layer, and the hybrid work cycle has compressed office decisions from once-a-decade events into annual ones. The new version is a broker-side SaaS platform with a tenant-facing search layer built on top — charging brokers for AI-powered tenant matching rather than competing with them for commissions, and using that cooperation to build the listing coverage that killed the original.

---34:T883,

## Why Now?

## Current Market Analysis

## Market Size

The US commercial real estate leasing market is not cleanly sized for the sub-5,000 sq ft segment in publicly available sources — this is an honest gap in the research. What is documented: JLL estimates the total US flex office market at $50B+ projected for 2024, up from $6B in 2019. CoStar Group's total revenue reached $2.46B in 2023 (CoStar 10-K, 2023), the majority of which comes from commercial listing and data subscriptions, indicating the monetizable layer of CRE information services is large and growing. The sub-5,000 sq ft segment remains the majority of CRE transactions by count, as it was in 2012 — this structural fact has not changed.

## Competition Map

- **CoStar/LoopNet**: The dominant incumbent. LoopNet has 11M+ monthly visitors (CoStar investor materials, 2023) but its UX remains broker-first and data-table-heavy. Its specific weakness in 2026: CoStar's attention is split toward residential (Homes.com), and LoopNet's small-tenant product has not meaningfully improved since 42Floors competed with it. CoStar's data moat is real but its product moat is not.
- **CommercialCafe (Yardi)**: The direct heir to 42Floors' brand and URL. Yardi's weakness is that it is an enterprise software company optimizing for property managers and institutional landlords, not small tenants. The consumer UX gap that 42Floors originally identified still exists inside CommercialCafe.
- **Crexi**: The most credible current challenger, with 500,000+ listings and a mobile-first product (Crexi's own figures, 2023). Crexi's weakness is that it skews toward investment sales and larger transactions, not the sub-5,000 sq ft lease market.
- **Industrious, Regus/IWG, Flex by JLL**: Flex operators with direct booking but no cross-operator search. A tenant cannot compare an Industrious space against a Regus space against a sublease on any single platform. This is the gap.36:T999,

## Defensibility Against Platform Incumbents

Google Maps has the distribution but not the CRE-specific data or transaction infrastructure. Microsoft (via LinkedIn) has the professional graph but not the listing inventory. Neither has demonstrated appetite to build a CRE listing product. CoStar is the real platform risk — but CoStar's incentive is to serve brokers who pay $500–$1,500/month for subscriptions, not to build a free consumer product that disintermediates them. A broker-side SaaS model that makes brokers more productive is structurally aligned with CoStar's customer base in a way that a pure tenant-facing aggregator is not. This is not a complete defense, but it is a structural distinction the original 42Floors lacked.

---

## Recommended MVP

## Feature 1: AI-Powered Listing Ingestion

An LLM pipeline (built on GPT-4o or Claude 3.5 Sonnet, both available as of mid-2024) that ingests broker offering memoranda, email attachments, and PDF flyers and outputs structured listing records — address, square footage, price, lease type, available date, photos. This directly solves the supply-side cold-start problem without requiring broker cooperation. Unlike 42Floors, which needed brokers to manually enter listings, the rebuild can seed its database from documents brokers are already distributing publicly. The pipeline should target 10,000 structured listings in three metro markets (New York, San Francisco, Austin) before public launch.

## Feature 2: Broker Tenant-Matching Dashboard

A paid SaaS tool for brokers that surfaces qualified tenant leads from the platform's search traffic, matched to their active listings by size, budget, and location. Brokers pay for this; tenants use the search layer for free. This is the monetization model 42Floors never attempted — charging brokers for workflow value rather than competing with them for commissions. It is validated by Buildout and VTS proving brokers will pay for software. Unlike a referral fee model, it does not create a conflict of interest that destroys broker cooperation.

## Feature 3: Flex + Traditional Unified Search

A single search interface that surfaces both traditional direct leases and flex/coworking inventory from operators including Industrious, IWG/Regus, and post-WeWork sublease inventory. No current platform does this. The original 42Floors attempted to include co-working as a filter but did not have the flex market scale to make it meaningful. In 2026, the flex inventory exists and is fragmented — this is the specific gap the WeWork bankruptcy created.

## What We Will NOT Build:

- A brokerage business (this killed the original)
- A blockchain listing platform (this killed Knotel)
- A residential product (this is killing CoStar's focus)
- A national launch on day one (this diluted 42Floors' early product quality)

**Cold-Start Threshold:** The product delivers value to a tenant searching in a single market when it has at least 500 structured listings covering the sub-5,000 sq ft segment. The AI ingestion pipeline should reach this threshold in New York before any public marketing spend. Broker dashboard value requires at least 50 active broker accounts in a market generating measurable lead flow — target this as the 90-day milestone in market one.

## Success Metrics:

- 500+ structured listings per launch market before public launch
- 50+ paying broker accounts at $299/month within 6 months of market launch
- 40%+ of tenant searches resulting in a broker contact or tour request (engagement quality, not just traffic)
- Broker churn below 10% monthly

---

## Go-to-Market Strategy

## Target Customer (Narrow)

Primary paying customer: independent commercial real estate brokers and boutique brokerage firms (2–20 agents) in New York City who specialize in sub-10,000 sq ft office leases. These brokers are underserved by CoStar (too expensive, built for large firms) and invisible on LoopNet's consumer-facing product. They have demonstrated willingness to pay for tools that generate qualified leads — this is not an assumption, it is the Buildout and VTS adoption pattern applied to a smaller firm segment.

Primary search user: founders and office managers at companies with 10–100 employees making their first or second office decision, concentrated in New York's tech and creative sectors.

## Primary Distribution Channel

Direct outreach to boutique CRE brokers via LinkedIn Sales Navigator, targeting agents at firms not on CoStar's enterprise contract. Offer the broker dashboard free for 60 days in exchange for listing data contribution. This is the supply-side seeding strategy — brokers get leads, the platform gets listings, tenants get coverage. Secondary channel: SEO targeting long-tail queries ("office space for rent [neighborhood] [city]") where CommercialCafe's Yardi-optimized pages are beatable on content quality and page speed.

## Pricing

Broker dashboard: $299/month per agent, or $799/month for a team of up to five. Stress-test: brokers currently accomplish lead generation through CoStar ($500–$1,500/month), cold outreach, and referrals. At $299/month, the product needs to demonstrably surface one qualified tenant lead per month to justify the cost against a broker's time alternative. This is a low bar if search traffic is real. Tenant search remains free — charging tenants for search is not justified when LoopNet, CommercialCafe, and Crexi all offer free search. The free alternative for tenants is real; the answer is not to charge them but to monetize the broker side of the match.

## Differentiation vs. 2026 Competitors

Against CommercialCafe: consumer UX and flex inventory unification. Against Crexi: focus on lease (not investment sales) and sub-10,000 sq ft. Against LoopNet: price and broker-side workflow tools. Against doing nothing: the AI ingestion pipeline means listing coverage in launch markets is competitive from day one, which was never true for 42Floors.
