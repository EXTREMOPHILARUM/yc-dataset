# Build Plan: Mini Exhibitions 2026

## Overview

Mini Exhibitions was a New York-based B2B managed virtual events company that graduated from Y Combinator's Winter 2020 batch, built its product on pandemic-era remote work demand, and quietly shut down in late 2022 when return-to-office mandates eroded the market it depended on — a failure of timing and structural position, not execution.

The rebuild thesis is this: the hybrid workplace has created a durable, recurring demand for structured team bonding that didn't exist in 2020, third-party logistics infrastructure has eliminated the fulfillment bottleneck that capped the original company's throughput, and HR software platforms like Lattice and Culture Amp now offer a distribution channel that didn't exist when Mini Exhibitions was selling cold. The new version is a hybrid-native team experience platform — curated, shipped, and bookable directly inside the HR tools enterprises already use.

---

## Why Now?

The single most important change since Mini Exhibitions failed is that hybrid work has replaced remote work as the dominant corporate mode — and hybrid creates a structurally different, more durable demand for team experiences than pure remote ever did.

During 2020–2022, virtual team events were a substitute for in-person connection that buyers tolerated because they had no alternative. In 2026, hybrid mandates from Apple (3 days in-office), Google (3 days), Amazon (5 days for corporate, with documented exceptions), and Salesforce (variable by role) have created a new problem: teams are physically together 2–3 days per week, but those days are unstructured, and the social cohesion that used to happen organically in full-time offices no longer does. HR teams are now buying structured in-person and hybrid experiences — not as a pandemic workaround, but as a permanent line item. This is a recurring need, not a spike.

The second critical change is logistics infrastructure. ShipBob, Whiplash, and Shopify Fulfillment Network now offer per-order fulfillment with no warehouse minimum, API-based order management, and 2-day delivery coverage across the continental US. The physical kits that required Mini Exhibitions to run manual fulfillment operations in 2021 can now be outsourced entirely, with variable cost per shipment rather than fixed operational overhead. Exact per-unit pricing varies by kit weight and destination density, but publicly available ShipBob pricing (as of 2025) suggests pick-and-pack costs in the $3–6 range per order before shipping — a meaningful improvement over in-house operations at small volumes.

Third, distribution has changed. Lattice, Culture Amp, and Leapsome collectively serve tens of thousands of HR teams and are actively building integration marketplaces. A rebuilt Mini Exhibitions embedded as a bookable experience layer inside these platforms reaches buyers at the moment of intent — during performance cycles, onboarding, or team health reviews — rather than through cold outbound sales.

GPT-4 (March 2023) and its successors have made automated scheduling, attendee communication, and internal event marketing viable at near-zero marginal cost, replacing the manual coordination layer that consumed founder time in the original model.

The global corporate team-building market was estimated at approximately $4.8 billion in 2023 (source: Grand View Research; note this figure covers the broader category and should be treated as directional). The hybrid-specific segment is not yet cleanly isolated in public data — this is a gap in available research.

---

## Current Market Analysis

**Market size:** The corporate team-building and employee engagement market has grown since Mini Exhibitions operated. Grand View Research estimated the global team-building market at approximately $4.8 billion in 2023, up from pre-pandemic figures, with hybrid formats representing a growing share. The virtual-only subset that Mini Exhibitions targeted has contracted; the hybrid and in-person subset has expanded. Precise hybrid-specific market sizing is not available in public sources — this is an honest gap.

## Competition map:

*Confetti and Teambuilding.com* are the most direct inheritors of Mini Exhibitions' original positioning. Both offer managed virtual and hybrid team events with physical kit shipping. Their weakness is that they remain catalog-first, transactional businesses with no deep integration into HR software workflows — buyers still have to find them, evaluate them, and manage procurement separately from their existing people-ops tooling.

*Airbnb Experiences for Work* has a large catalog and brand recognition but is optimized for one-off bookings rather than recurring programmatic use. It lacks the enterprise procurement features (PO support, SSO, headcount management) that HR teams at Amazon-scale require.

*Thriver* (formerly Platterz) has moved into the hybrid office experience space with a focus on food and wellness. Its weakness is geographic density dependence — it works well in major metros but has thin coverage for distributed teams.

*Zoom Events and Microsoft Teams* remain the platform incumbents with adjacent features. Their native engagement tools (breakout rooms, polls, Together Mode) address casual interaction but do not offer curated experiences, physical components, or managed logistics. Critically, neither Microsoft nor Zoom has shown strategic intent to enter the managed experience marketplace — their product motion is toward communication infrastructure, not experience curation. This is the structural answer to the platform commoditization risk: the rebuilt Mini Exhibitions is not competing on video infrastructure (where platforms win by default) but on curation, logistics, and HR workflow integration — none of which are on Microsoft or Zoom's product roadmap.

**Demand signals:** Goldbelly's corporate gifting vertical and Airbnb Experiences' survival and growth through the post-pandemic period both validate that companies will pay for shipped, curated physical experiences. Lattice's 2024 integration marketplace launch signals that HR platforms are actively seeking experiential partners to embed in their workflows.

**Defensibility:** The rebuild's defensibility rests on three compounding factors: (1) catalog curation and supplier relationships that take time to replicate, (2) deep integration into HR software platforms that creates switching costs at the distribution layer, and (3) recurring contract structures tied to HR program cycles rather than one-off event bookings. This is meaningfully more defensible than the original, which had none of these. The honest caveat: a well-capitalized competitor (a Confetti with a Series B, or an HR platform that decides to build natively) could replicate the catalog. The integration layer is the real moat, and it must be built aggressively in year one.

---

## Recommended MVP

## Feature 1: Hybrid Experience Catalog (in-person + remote simultaneous)

A curated catalog of 15–20 experiences designed explicitly for hybrid teams — where some participants are in an office together and others are remote. Each experience ships physical kits to remote attendees while providing a facilitated in-room component for the in-office group. This is architecturally different from the original Mini Exhibitions catalog, which assumed all participants were remote. The hybrid format is the product's core structural innovation and its primary differentiation from Confetti and Teambuilding.com, which still treat hybrid as an afterthought.

## Feature 2: 3PL-Powered Kit Fulfillment via API

All physical kit shipping is handled through a third-party logistics partner (ShipBob or equivalent) via API integration, with no in-house fulfillment operations. Clients provide attendee addresses at booking; the system generates and submits fulfillment orders automatically. This directly addresses the operational ceiling that limited the original company — a two-person team can now support dozens of simultaneous events without a warehouse. The MVP does not build proprietary logistics software; it uses existing 3PL APIs.

## Feature 3: HR Platform Booking Integration (Lattice-first)

A native integration with Lattice that allows HR admins to browse, book, and manage team experiences directly within their existing workflow — tied to team health scores, onboarding milestones, or performance cycle events. This is the distribution moat the original company lacked entirely. Lattice is the priority integration because of its active marketplace program and mid-market enterprise focus; Culture Amp and Leapsome follow in phase two.

## Feature 4: Automated Event Coordination Layer

GPT-4-powered (or equivalent, 2026 model) automated attendee communication: calendar invites, pre-event instructions, shipping tracking updates, and post-event feedback collection. This replaces the manual coordination work that consumed founder time in the original model and is the primary labor cost reduction versus the 2021 version.

**What we will NOT build:** A proprietary video conferencing platform. A general-purpose virtual events tool for large conferences. An in-house fulfillment warehouse. A consumer-facing product.

## Success metrics:

- 10 paying enterprise clients within 6 months of launch
- Average contract value ≥ $3,000 per event booking
- Net Promoter Score ≥ 50 from attendees after first 50 events
- At least 1 Lattice integration live and generating inbound leads within 9 months

**Cold-start note:** This product does not depend on network effects or local density. Each event delivers value to the booking company independently. There is no minimum user threshold before the core feature works.

---

## Go-to-Market Strategy

**Target customer:** HR and people-operations leaders at hybrid-first tech companies with 200–2,000 employees, specifically those already using Lattice or Culture Amp as their core HR platform. This segment has dedicated people-ops budgets, is already paying for employee engagement software, and is actively looking for programmatic solutions to hybrid team cohesion — not one-off event vendors. Companies in the 200–2,000 range are large enough to have recurring event budgets but small enough that the HR team makes purchasing decisions without a six-month procurement cycle.

**Primary distribution channel:** HR platform integration marketplaces, led by Lattice. The go-to-market motion is partnership-first: secure a listing in Lattice's integration marketplace, then use that listing as a warm inbound channel. Secondary channel is direct outbound to people-ops leaders at companies already in the Lattice customer base, using Lattice's public customer list as a prospecting source. This is the compounding distribution mechanism the original Mini Exhibitions never built.

**Pricing:** Per-event pricing at $75–$125 per attendee, with a minimum booking of 15 attendees ($1,125–$1,875 floor per event). Annual program packages (6 or 12 events pre-committed) at a 15% discount. No subscription fee.

The stress test: the primary free alternative is a manager-organized Zoom happy hour or an in-office catered lunch, both of which cost nothing in direct spend but require significant internal coordination time. The rebuilt Mini Exhibitions' price is justified by three things the free alternative cannot provide: physical kit delivery to remote attendees (which a Zoom call cannot replicate), zero internal coordination burden (the managed service layer), and a facilitated experience with a professional instructor. The honest risk is that in a budget-constrained environment, HR teams cut discretionary event spend first. The mitigation is the annual program package structure, which moves the product from discretionary line item to planned program budget — harder to cut mid-year than a one-off booking.

**Differentiation vs. 2026 competitors:** Confetti and Teambuilding.com are catalog businesses that require buyers to find them. The rebuilt Mini Exhibitions is an embedded workflow tool that finds buyers inside the software they already use. That distribution difference — not catalog depth or experience quality — is the primary competitive claim in 2026.
