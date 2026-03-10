# Build Plan: Ark 2026

## Overview

Ark 2026 is a B2B identity enrichment platform for sales and recruiting teams. It aggregates professional identity data—LinkedIn, GitHub, email—that users voluntarily connect via OAuth, then uses AI-powered entity resolution to create a unified, searchable professional graph. The product targets GTM teams at mid-market SaaS companies who need to move beyond outdated data brokers.

The viability shift is regulatory and technical. Data portability laws (GDPR, CCPA) and official platform APIs now make user-consented aggregation both legal and scalable—solving the platform dependency problem that killed the original Ark. Meanwhile, modern LLMs can reliably match identities across sources in real time, replacing manual enrichment workflows.

Go-to-market is tight: one-click export to HubSpot and Clay, priced per seat, targeting teams already using those tools. Win by being faster and fresher than ZoomInfo's broker-era databases, and by letting customers own their data graph instead of renting stale records.

## Why Now?

The single most important change since Ark's 2015 failure is the emergence of a legally compliant, user-consented data portability infrastructure that simply did not exist when Facebook revoked Ark's API access in 2013. GDPR (2018), CCPA (2020), and the EU's Data Act (2023) now grant users explicit rights to export their own data from any platform. Meta's Data Transfer Project and LinkedIn's Data Portability API are concrete, policy-sanctioned mechanisms for moving personal data — meaning a rebuilt Ark can be user-initiated rather than platform-scraped, eliminating the exact structural dependency that killed the original.

This matters because Ark's fatal flaw was not the product concept — 234,000 first-month signups proved genuine demand — it was that the data supply chain was controlled by a competitor. Today, the user *is* the data supply chain.

The B2B sales intelligence market has since validated Ark's pivot direction at enormous scale. ZoomInfo IPO'd in 2020 and reported approximately $1.1 billion in revenue for fiscal year 2023 (per ZoomInfo's public filings). Apollo.io reached a reported $100M+ ARR by 2023. Clay raised at a $1.25 billion valuation in 2024. These outcomes confirm that the enriched-contact-data market Ark was stumbling toward in 2013 is real, large, and still not fully served at the mid-market.

Two additional technology shifts lower the rebuild cost dramatically. GPT-4 (March 2023) and Claude 3 (March 2024) can now perform entity resolution, bio normalization, and cross-source identity reconciliation with high accuracy — work that would have required brittle, expensive custom ETL engineering in 2012. LinkedIn's official Partner API provides structured, policy-compliant professional identity data at scale. The professional identity graph has also re-fragmented across LinkedIn, GitHub, Substack, and personal sites since 2012, recreating Ark's original structural gap without Facebook's shadow over it.

Distribution channels unavailable in 2012 now include the Clay integration marketplace, the HubSpot App Marketplace (150,000+ customers), and the Salesforce AppExchange (150,000+ installs across categories) — all with warm, pre-qualified B2B buyers.

---

## Current Market Analysis

**Market size.** The B2B data enrichment and sales intelligence market was nascent when Ark pivoted toward it in 2013. By 2024, it is a multi-billion-dollar category. ZoomInfo alone reported approximately $1.1 billion in fiscal 2023 revenue. The broader sales intelligence software market is estimated at $3–5 billion annually, though the specific sub-segment for AI-powered, privacy-compliant contact enrichment is not independently sized in available public sources.

## Competition map and gaps.

- **ZoomInfo** — dominant incumbent with deep contact databases but built on data-broker-era practices increasingly under regulatory scrutiny. Its GDPR compliance posture has drawn criticism in Europe, and its pricing (typically $15,000–$30,000+/year for team plans) locks out SMBs and mid-market teams. Weakness: expensive, privacy-questionable, poor fit for non-US markets.

- **Apollo.io** — strong mid-market penetration with a freemium model, but contact data quality is inconsistent and the product is primarily email-sequence-focused rather than identity-graph-focused. Weakness: data freshness and accuracy, limited enrichment depth beyond email/phone.

- **Clay** — the most interesting recent entrant; a workflow tool that pulls from 50+ enrichment sources. Clay is a data orchestration layer, not an identity graph. Weakness: requires technical users to configure; not a search product; no unified identity resolution across sources.

- **LinkedIn Sales Navigator** — authoritative professional data but siloed to LinkedIn's own graph, expensive ($900+/user/year), and explicitly prohibited from cross-network enrichment. Weakness: single-network, no public web synthesis.

**The gap.** No current competitor offers a privacy-first, user-consented, cross-network professional identity search product with AI-powered entity resolution aimed at mid-market GTM teams. Clay comes closest architecturally but is a workflow tool, not a search engine. The original Ark thesis — neutral aggregator across fragmented professional identity — remains unoccupied in 2026, now with a viable legal and technical path to execute it.

**Demand signals.** Clay's rapid growth and $1.25B valuation signal that GTM teams are actively paying for better identity data infrastructure. The proliferation of "AI SDR" tools (e.g., 11x, Artisan) creates downstream demand for higher-quality enrichment inputs.

---

## Recommended MVP

### Feature 1: User-Consented Identity Aggregation ("Bring Your Own Graph")

Users connect their own LinkedIn, GitHub, and optionally their email contacts via OAuth and official portability APIs, authorizing Ark to index their extended professional network. This creates a permissioned identity graph seeded by the user's actual connections, not scraped data. This directly inverts Ark's fatal dependency: the platform cannot revoke what the user has explicitly shared. Unlike the original Ark, no data is held without user consent, and the index is personal rather than universal.

## Feature 2: AI-Powered Cross-Source Entity Resolution

Using GPT-4o (released May 2024) and fine-tuned embedding models, Ark reconciles identities across LinkedIn profiles, GitHub accounts, Substack bylines, and personal websites — normalizing inconsistent names, inferring role changes, and deduplicating records. This replaces the brittle ETL engineering that would have consumed Ark's 2012 team for months. The result is a unified professional identity card per person that no single platform can provide.

## Feature 3: Layered Filter Search (Professional Graph Only)

A structured search interface with 10–15 filters — current role, company, location, skills, open-source contributions, writing topics — applied against the user's aggregated network. This is the core Ark UX, rebuilt on a legally defensible data foundation and scoped exclusively to professional identity, not personal social data. Facebook is explicitly excluded from the data model.

## Feature 4: CRM Push and Clay Integration

One-click export of enriched identity records to HubSpot, Salesforce, and Clay workflows via native integrations. This is the monetization bridge: it converts search utility into GTM workflow value and positions Ark as enrichment infrastructure rather than a standalone tool.

**What we will NOT build:** consumer people-search (the original Ark use case), email client functionality (Ark Mail's failed direction), background-check or personal records aggregation, or any scraping of platform data without explicit user consent.

**Success metrics:** 500 paying teams within 6 months of launch; average enrichment accuracy ≥85% validated by user correction rate; <5% monthly churn; at least one HubSpot Marketplace or Clay integration with 100+ active installs.

---

## Go-to-Market Strategy

**Target customer.** The initial wedge is a narrow, high-intent segment: GTM teams of 5–50 people at B2B SaaS companies using HubSpot or Clay who are currently paying for Apollo.io or ZoomInfo but frustrated by data quality or pricing. These buyers already understand enrichment value, have budget allocated, and are actively evaluating alternatives. They are reachable through the HubSpot App Marketplace (150,000+ customers) and Clay's integration ecosystem without requiring a direct outbound sales motion at launch.

**Primary distribution channel.** HubSpot App Marketplace as the primary acquisition channel, supplemented by Clay's integration directory. Both channels surface Ark to buyers at the moment of enrichment intent — when they are already inside their CRM or data workflow. Secondary channel: founder-led content on LinkedIn targeting RevOps and GTM engineering audiences, a community that has demonstrated high organic engagement around data quality topics.

**Pricing.** Freemium entry tier: 250 enriched contacts/month free, designed to generate word-of-mouth within GTM teams. Paid tiers at $99/month (2,500 contacts, 3 seats) and $399/month (unlimited contacts, 10 seats). This undercuts Apollo.io's comparable tiers by approximately 40–60% while positioning above Clay's raw API costs. Annual prepay discount of 20% to improve cash flow predictability. No enterprise tier at launch — avoid the long sales cycles that would drain runway before product-market fit is confirmed.

**Differentiation vs. 2026 competitors.** Ark's rebuild wins on three axes that incumbents cannot easily replicate: (1) user-consented data architecture that is structurally GDPR/CCPA compliant, not retroactively patched; (2) cross-source entity resolution that synthesizes LinkedIn, GitHub, and public web signals that ZoomInfo and Apollo ignore; and (3) pricing accessible to mid-market teams that ZoomInfo's $15,000+ annual contracts exclude. The privacy-first architecture is not merely a compliance checkbox — it is a genuine enterprise procurement advantage as data-handling scrutiny increases in 2025–2026.
