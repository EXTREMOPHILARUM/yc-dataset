# Build Plan: Lotus 2026

## Overview

By 2026, Lotus is a cloud-native billing engine purpose-built for AI API companies. It handles the complexity that Stripe Billing can't: multi-dimensional pricing (tokens + compute + model tier), real-time metric ingestion at scale, and instant plan experimentation. The product is lean, opinionated, and ships with AI-specific templates that work out of the box.

The market shift is concrete: AI infrastructure companies are hitting the wall with generic billing tools. Token-based pricing, tiered compute costs, and dynamic rate limits require metering infrastructure that Stripe wasn't designed for. These companies need to iterate on pricing weekly, not quarterly. That urgency didn't exist in 2022.

Go-to-market is direct and narrow. Land with AI API startups at $500K–$5M ARR through technical communities (Hugging Face, Together AI, Replicate forums) and founder networks. Win by being 10x faster to deploy than building custom billing logic. Monetize with usage-based pricing on Lotus itself—charge per million events ingested—so early-stage customers pay nothing until they scale. This aligns incentives and removes the enterprise sales friction that killed the first version.33:T7ba,

## Why Now?

## Current Market Analysis

The billing and subscription management software market was estimated at approximately $7.8 billion in 2022. By 2025, independent analyst estimates place the market between $12–15 billion (exact 2026 figure unavailable), with usage-based billing as the fastest-growing segment. OpenView's 2023 SaaS Benchmarks report found that 61% of SaaS companies had adopted some form of usage-based pricing — a figure that has likely increased further as AI products normalized consumption billing for end users.

**Orb** — The best-funded pure-play usage-based billing vendor ($89M total raised). Cloud-only, no self-hosted option, pricing starts at approximately $1,500/month. Weakness: inaccessible to companies under $2M ARR; no open-source community flywheel; no pricing experimentation or backtesting tooling.

**Lago** — The most direct open-source analog to Lotus, also YC-backed (W22), raised $22M Series A. Lago is alive and operating. Weakness: its open-source repository has shifted toward a more restrictive license over time, and its cloud product is priced at enterprise tiers that exclude early-stage AI companies. Lago's public GitHub activity has slowed since 2024 (exact commit frequency data unavailable), suggesting reduced community investment.

**Stripe Billing** — Dominant distribution but documented ceiling for multi-metric usage scenarios. Weakness: percentage-of-revenue pricing (0.5–0.8%) becomes expensive at scale; no self-hosted option; no pricing experimentation layer.

**Chargebee / Maxio** — Mid-market incumbents optimized for seat-based SaaS, not token-based AI billing. Weakness: UI and data models were not designed for sub-second metering events at AI API volumes.

**Demand signal from adjacent products:** Metronome (raised $95M through 2024) targets enterprise AI infrastructure companies with a high-touch, high-price billing platform. Its existence and funding confirm that the top of the market is real — and that the bottom and middle remain underserved.

## Recommended MVP

## Core Feature 1: AI-Native Metric Templates

Pre-built metering schemas for token consumption, compute-seconds, model tier switching, and context window billing — deployable in under 30 minutes via SDK. This matters because AI companies currently hand-roll metering logic in application code, creating billing debt that compounds as pricing models evolve. The original Lotus required operators to define all metrics from scratch; this version ships with the ten most common AI billing patterns out of the box.

## Core Feature 2: Multi-Metric Plan Builder with Backtesting

A visual interface for composing pricing plans across multiple simultaneous metrics, with a backtesting engine that simulates proposed pricing changes against 90 days of historical usage data. This was Lotus's most differentiated original feature and remains unmatched by Stripe Billing, Chargebee, or Lago's cloud product. It directly addresses the "pricing experimentation" use case that no incumbent has prioritized.

## Core Feature 3: Stripe Migration Importer

A one-command tool that reads a company's existing Stripe Billing configuration — products, prices, subscriptions, and usage records — and imports it into the rebuilt Lotus. This creates the displacement motion that the original Lotus lacked: a concrete, low-friction path for "Stripe refugees" hitting multi-metric billing ceilings.

## Core Feature 4: Managed Cloud with Usage-Based Pricing on Lotus Itself

A cloud-hosted version priced on metering volume (e.g., per million events ingested), not a flat monthly fee. This aligns incentives with early-stage AI companies that have unpredictable usage growth and cannot commit to $1,500/month minimums.

**What we will NOT build:** Revenue recognition, dunning management, tax calculation, or payment processing. These are solved problems with dedicated vendors (Avalara, Stripe, Paddle). Building them dilutes focus and extends time-to-value.

**Success metrics:** 50 self-hosted deployments within 90 days of launch; 10 paying cloud customers within 6 months; $15,000 MRR within 12 months; GitHub repository reaching 1,000 stars within 60 days of launch.

## Go-to-Market Strategy

**Target customer segment:** AI API companies and AI infrastructure startups with $500K–$5M ARR that have outgrown Stripe Billing's flat-rate or simple usage plans and are billing on two or more simultaneous metrics (e.g., tokens + compute + model tier). This segment is narrow enough to focus outreach, large enough to build a business, and technically sophisticated enough to self-host — making them ideal for a developer-led, bottom-up motion.

**Primary distribution channel:** GitHub and AWS Marketplace in combination. The GitHub repository serves as the top-of-funnel discovery channel for engineering-led organizations — the same motion that worked for Lotus's community traction, now paired with a conversion path. AWS Marketplace listing targets procurement-approved enterprise buyers with committed AWS spend, providing a B2B sales channel that requires no dedicated sales team to operate. Secondary channel: direct outreach to YC AI companies from the W23–W26 batches, which represent a concentrated, accessible population of the exact ICP.

**Pricing strategy:** Three tiers, with a deliberate departure from MIT licensing. The self-hosted version is released under AGPL — free for open-source and internal use, but requiring a commercial license for SaaS deployment. This preserves community adoption while creating structural upgrade pressure that the original MIT license eliminated. Cloud tier: $0.50 per 100,000 metered events, with a $200/month minimum. Enterprise tier: custom contract with SLA, starting at $2,000/month. The usage-based pricing on the cloud tier directly mirrors the AI companies being targeted, building credibility through alignment.

**Differentiation vs. 2026 competitors:** Orb and Metronome are priced out of the sub-$5M ARR segment. Lago's community investment has slowed. Stripe Billing cannot be self-hosted and lacks backtesting. The rebuilt Lotus is the only option that combines self-hostability, AI-native metric templates, pricing experimentation tooling, and a Stripe migration path — at a price point accessible to early-stage AI companies.
