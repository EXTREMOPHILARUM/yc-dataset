# Build Plan: CarWoo 2026

## Overview

CarWoo 2026 is a real-time competitive offer engine for new car buyers, embedded as a white-label benefit inside credit union and employer platforms. Instead of building a consumer brand, it lives where buyers already manage their finances—Navy Federal, PenFed, regional credit unions—reaching pre-qualified, in-market shoppers with zero acquisition friction.

The market shift is dealer consolidation. When CarWoo failed, fragmented independent dealers made national density impossible. Today, three dealer management systems (CDK, Reynolds & Reynolds, Dominion) control 80%+ of U.S. franchises. One API integration reaches thousands of dealers instantly. Simultaneously, credit unions are desperate for member engagement tools beyond lending—this solves that problem while generating a new revenue stream.

The play: buyers submit preferences through conversational AI, dealers get 48 hours to submit binding offers on anonymized briefs, and the buyer sees ranked, real-time pricing. No spam, no haggling theater, no contact harvesting. Dealers win because they compete on price efficiency rather than sales pressure. Credit unions win because members get tangible value and stay engaged. We win by charging per-activated-member fees—predictable, scalable, and aligned with partner success.33:T84f,

## Why Now?

The single most important change since CarWoo's 2014 failure is dealer consolidation. When CarWoo shut down, it had spent years and millions of dollars signing 11,000 individual franchise dealerships one at a time. Today, the top 10 dealer groups — AutoNation (~250 stores), Lithia Motors (~300+ stores), Sonic Automotive, Penske, and others — collectively control thousands of rooftops under unified procurement and technology decisions. A rebuilt CarWoo could negotiate a single master agreement with AutoNation and reach more dealers than CarWoo signed in three years of field sales. This structural shift alone changes the supply-side economics of the business.

The second enabling change is conversational AI. Claude 3 Opus (March 2024) and GPT-4 (March 2023) can now handle the full buyer intake, preference qualification, and dealer briefing workflow asynchronously at near-zero marginal cost. CarWoo's original model required human-touch customer support to shepherd buyers through an unfamiliar auction mechanic. That cost is now effectively eliminated.

On distribution, the Costco Auto Program currently serves over 1 million members annually and demonstrates that consumers will accept a structured, fee-embedded car-buying service inside a trusted membership relationship. A rebuilt CarWoo embedded in employer benefits platforms (e.g., Alight Solutions, which serves 70+ million employees) or credit union networks (Navy Federal, with 13 million members) could acquire buyers at a fraction of CarWoo's standalone CAC without charging a visible per-transaction fee.

Real-time dealer inventory APIs from CDK Global and Reynolds & Reynolds — not available at CarWoo's scale in 2010–2014 — now allow automatic inventory and pricing verification, eliminating the operational complexity that forced CarWoo to drop entire vehicle segments like Ram trucks.

TrueCar's documented dealer network defections in 2019–2020 (publicly reported by Automotive News) confirm the market has not been definitively solved. Dealer receptivity to alternatives is higher today than at any point since CarWoo's closure.

---

## Current Market Analysis

The U.S. new car market generated approximately $600 billion in retail sales in 2023 (Cox Automotive estimate), up from roughly $500 billion during CarWoo's operating years. The online automotive lead-generation and marketplace segment is harder to isolate precisely — exact 2026 figures are not available at time of writing — but Cox Automotive, which owns Autotrader and Kelley Blue Book, reported $2.8 billion in revenue in 2022, indicating the addressable intermediary market remains large.

## Current competitor map and gaps:

- **TrueCar** (NASDAQ: TRUE): The direct heir to CarWoo's market position. Revenue has declined from ~$350M (2018) to under $200M (2023), reflecting the dealer defection crisis of 2019–2020 when dealers including AutoNation publicly exited the platform over pricing disputes. TrueCar's weakness is that it is a price-transparency tool, not a negotiation tool — it shows historical transaction data but does not generate competitive real-time offers.

- **CarGurus**: Strong on used inventory search; its new car offering is thinner and relies on dealer advertising rather than buyer-side mechanics. Weakness: no anonymity, no competitive bidding.

- **Carvana / Vroom**: Fully online but limited to used vehicles and their own inventory. Not a marketplace. Carvana's near-bankruptcy in 2022–2023 has cooled consumer enthusiasm for fully disintermediated models.

- **Costco Auto Program**: High consumer trust, but operates as a fixed-price referral program with no competitive dynamic. Dealers pay a flat referral fee; buyers get a pre-negotiated price but not necessarily the best available price.

**Gap:** No current platform combines buyer anonymity, real-time competitive dealer offers, and AI-assisted negotiation briefing. TrueCar's struggles have left dealers actively seeking alternative digital lead sources with better ROI transparency.

**Demand signal:** The Costco Auto Program's 1M+ annual transactions demonstrate sustained consumer appetite for structured, low-friction car buying outside the traditional dealership floor.

---

## Recommended MVP

## Core Features:

### AI-Powered Anonymous Buyer Intake (Claude 3.5 Sonnet or equivalent, 2024)

A conversational AI agent collects buyer preferences, budget, trade-in details, and timeline through a chat interface, then generates a structured dealer brief — without ever exposing the buyer's contact information. This replaces CarWoo's manual intake form and eliminates the consumer education burden that made the original product confusing. Unlike CarWoo's static form, the AI can handle ambiguous inputs ("something like a RAV4 but bigger") and resolve them into actionable vehicle configurations.

## Consolidated Dealer Group API Integration

Rather than signing individual dealers, the MVP integrates directly with CDK Global and Reynolds & Reynolds APIs to pull live inventory from dealer group partners. Launch with two to three large groups (targeting AutoNation and Lithia as anchor partners) covering 500+ rooftops before opening to independent dealers. This inverts CarWoo's supply-side strategy: start dense in fewer markets rather than thin across all markets. Unlike CarWoo's manual dealer onboarding, inventory verification is automated and real-time.

## Competitive Offer Engine with 48-Hour Window

Dealers receive anonymized buyer briefs and submit binding price offers within a 48-hour window. The buyer sees ranked offers with dealer ratings and response time scores. No contact information is exchanged until the buyer accepts an offer. This preserves CarWoo's core anonymity mechanic — its most defensible consumer value proposition — while shortening the auction window from CarWoo's 3.5-day average to 48 hours, reducing buyer drop-off.

## Embedded Membership Distribution

The buyer fee is not charged as a standalone transaction cost. Instead, the service is offered as a benefit through credit union networks and employer benefits platforms. Target Navy Federal Credit Union (13M members) and one mid-market employer benefits aggregator as launch partners. This eliminates the friction of CarWoo's $19–$100 per-search fee while generating B2B subscription revenue from the distribution partner.

## What we will NOT build at MVP:

- Used car inventory or private-party listings
- Financing or insurance products
- A mobile app (web-first only)
- Coverage outside the top 15 U.S. metro markets

## Success Metrics:

- 500 completed buyer transactions within 6 months of launch
- Dealer offer response rate ≥ 70% within 48-hour window
- Buyer-to-offer-acceptance conversion ≥ 40%
- Geographic coverage: ≥ 3 competing dealer offers per buyer request in all 15 launch markets

---

## Go-to-Market Strategy

### Target Customer Segment:

Primary: Credit union members aged 28–50 with household income above $75,000 who are actively in-market for a new vehicle within 90 days. This segment is narrow by design. Credit union members already have a trust relationship with a financial institution, are accustomed to member benefits, and skew toward considered purchases. They are not the casual browser CarWoo's free tier attracted — they are the high-intent buyer CarWoo's $49 fee was trying to filter for, delivered pre-qualified through the distribution partner.

## Primary Distribution Channel:

Credit union co-marketing partnerships. Navy Federal, Pentagon Federal (PenFed, 2.9M members), and regional credit unions with auto loan portfolios have direct financial incentive to help members get better vehicle prices — lower purchase prices mean lower loan amounts, but higher member satisfaction and loan capture rates. Pitch the service as a member benefit that increases auto loan origination, not as a competitor. This channel is currently underserved: no major car-buying platform has built a credit-union-first distribution strategy.

## Pricing Strategy:

B2B SaaS model: charge credit unions and employer benefits platforms a per-activated-member annual fee (estimated $15–$30 per member per year, based on comparable automotive benefit program pricing — exact market rate requires validation). Dealers pay a per-closed-transaction fee of $200–$400, consistent with current automotive lead pricing benchmarks from TrueCar and CarGurus. No consumer-facing fee at launch. This eliminates CarWoo's most visible friction point while generating revenue from both sides of the marketplace.

## Differentiation vs. 2026 Competitors:

TrueCar shows historical prices; this platform generates real-time competitive offers. CarGurus requires contact submission; this platform maintains buyer anonymity through transaction close. Costco Auto Program offers fixed prices; this platform creates genuine competition among dealers. The combination of AI-assisted intake, consolidated dealer group supply, and embedded distribution is not replicated by any current competitor — and the credit-union channel specifically is uncontested.
