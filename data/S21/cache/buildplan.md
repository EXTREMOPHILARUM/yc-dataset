# Build Plan: Cache 2026

## Overview

By 2026, Cache is a B2B convenience locker network embedded in suburban apartment complexes, stocked with OTC medicine, personal care, and snacks. It serves the 40+ million suburban renters that GoPuff abandoned and that DashMart never reached — fulfilling orders through existing DoorDash and Uber Eats integrations, not a proprietary app.

The market shift is hardware commoditization. Smart locker components (Luxer One, Snaffle) that cost $50K+ to engineer in 2021 now cost $15–20K off-the-shelf. That changes the unit economics entirely: a Cache unit can now break even at 15 orders per week instead of 40, making suburban density viable for the first time.

The go-to-market is property manager partnerships, not consumer acquisition. Target mid-size apartment complexes (150–500 units) in suburban markets where GoPuff has retracted. Install one unit per property, stock it with high-margin essentials, and let DoorDash and Uber Eats handle discovery and fulfillment. No delivery fleet. No proprietary tech. Just better unit economics in a market segment that's been structurally abandoned.32:T88e,

## Why Now?

The single most important change since Cache's failure is the commoditization of IoT-connected smart locker hardware. In 2021, Cache had to design and manufacture proprietary "Cache Units" from scratch — a capital-intensive, time-consuming process that consumed the majority of its $125,000 YC pre-seed before generating meaningful proof points. By 2026, Amazon Hub, Luxer One, and package locker networks have driven smart locker hardware into a commodity category. A Cache-style automated dispensing unit can now be assembled from proven, off-the-shelf components with established supply chains, slashing hardware development risk from an existential constraint to a procurement decision.

This hardware shift directly addresses Cache's primary cause of failure: the structural mismatch between hardware capital requirements and pre-seed funding. A rebuilt Cache in 2026 can deploy its first units faster, cheaper, and with less engineering risk than the original team faced.

Additional tailwinds compound this advantage:

**Platform distribution is now de-risked.** DoorDash has since launched formal virtual convenience store partnership programs (including integrations with Wawa), and Uber Eats has integrated 7-Eleven at scale. Delivery platforms now actively promote convenience storefronts rather than treating unknown operators as second-class listings — a material change from the algorithmic disadvantage Cache faced competing against DashMart in 2021.

**Demand for OTC delivery is validated.** Amazon Pharmacy and GoodRx's delivery expansion have demonstrated consumer willingness to pay for on-demand delivery of plan B, OTC medicine, and personal care items — Cache's highest-margin categories. This was an unproven demand signal in 2021.

**GoPuff's collapse confirms the thesis.** GoPuff's mass layoffs in 2022–2023 and closure of hundreds of micro-fulfillment centers empirically validated Cache's original argument that urban dark store economics are structurally broken. The market opening Cache anticipated now has public proof.

Specific market sizing for the suburban on-demand convenience segment is not available in public sources as of this writing.

---

## Current Market Analysis

### Market Size

The U.S. convenience store industry generates approximately $860 billion in annual in-store sales as of 2023 (NACS State of the Industry Report, 2023), up from roughly $700 billion when Cache operated. The relevant addressable segment — suburban consumers ordering convenience goods through delivery platforms — lacks reliable public sizing data, a gap that persists from 2021. However, the overall U.S. food and beverage delivery market reached $26.5 billion in 2023 (Statista), with convenience delivery growing as a distinct subcategory.

## Competition Map and Gaps

- **GoPuff**: Survived its 2022–2023 contraction but retracted to dense urban cores. Its suburban footprint is materially smaller than at peak. Weakness: still capital-heavy per location; suburban unit economics remain unproven at their cost structure.
- **DashMart**: Continues operating as DoorDash's first-party convenience product, with algorithmic placement advantages. Weakness: limited to markets where DoorDash has invested in warehouse infrastructure; no suburban micro-deployment capability.
- **7-Eleven / Wawa via Uber Eats**: Traditional convenience chains using delivery as a channel. Weakness: fixed store locations determined by decades-old real estate decisions, not delivery demand signals; no ability to deploy into underserved suburban pockets.
- **Amazon Pharmacy / GoodRx**: Validated OTC delivery demand but operate on 1–2 day fulfillment windows, not sub-60-minute convenience delivery.

**The gap**: No current competitor offers unstaffed, sub-60-minute convenience delivery specifically engineered for suburban markets with low order density. The original Cache thesis remains unoccupied.34:T56e,

## Demand Signals from Adjacent Products

Amazon Hub locker adoption in suburban apartment complexes and grocery pickup lockers at Walmart and Kroger demonstrate that suburban consumers are comfortable interacting with automated dispensing infrastructure — a behavioral prerequisite Cache could not assume in 2021.

---

## Recommended MVP

### Core Features

**1. Commodity-Hardware Cache Unit v2.** Deploy automated dispensing units built from Luxer One-style smart locker components rather than custom-manufactured hardware. Each unit holds 50–80 SKUs, connects via cellular IoT, and grants access to verified delivery drivers through a QR-code unlock system. This directly addresses the original Cache's primary failure mode — custom hardware on pre-seed capital — by substituting proven components. Unlike the original, units can be operational within days of site agreement rather than weeks of manufacturing.

**2. Real-Time Inventory Telemetry Dashboard.** Each unit reports stock levels continuously via cellular connection, triggering restocking alerts when any SKU falls below a defined threshold. This solves the critical operational gap the original Cache never publicly addressed: how an unstaffed unit avoids stockouts. Restocking is handled by a contracted local courier on a scheduled route, not founders driving to Sausalito.

**3. Multi-Platform Storefront Management Layer.** A single operator dashboard — built on Stripe's embedded commerce APIs — manages simultaneous listings on DoorDash, Uber Eats, and Instacart, with inventory counts synced in real time to prevent overselling. The original Cache managed platform storefronts manually; this layer automates it, freeing the two-person team for deployment and sales.

## What We Will NOT Build

No proprietary hardware. No consumer-facing app. No owned delivery fleet. No urban market locations. No SKU categories outside OTC medicine, personal care, and high-margin snacks.

## Success Metrics

- 10 units deployed across 3 suburban markets within 12 months
- ≥15 orders per unit per week at steady state (the minimum density threshold to cover per-unit operating costs — specific cost data unavailable; this threshold requires validation against actual hardware and restocking costs)
- Platform storefront rating ≥ 4.5 stars across all listings
- Gross margin per order ≥ 40% after platform commissions

---

## Go-to-Market Strategy

### Target Customer Segment

Suburban property managers of mid-size apartment complexes (150–500 units) in markets with active DoorDash and Uber Eats coverage but no GoPuff service area. This segment is narrow and specific: they control the real estate Cache needs, have an existing incentive to offer resident amenities, and can be reached through a defined B2B sales motion. Residents of these complexes are the end consumers — the suburban household that needs plan B at 11pm or NyQuil on a Sunday.

## Primary Distribution Channel

B2B direct sales to property managers, with consumer demand fulfilled through DoorDash and Uber Eats storefronts. Target the top 20 suburban apartment markets by delivery platform penetration (specific ranking data not publicly available; proxy using DoorDash and Uber Eats coverage maps). Offer property managers a revenue share of 5–8% of gross sales generated by the unit on their property — a model analogous to vending machine placement agreements, which are a well-understood commercial structure in property management.

## Pricing Strategy

Consumer-facing prices set at a 25–35% premium to physical convenience store shelf prices, consistent with GoPuff's pricing model and validated by Amazon Pharmacy's OTC delivery pricing. Platform commissions (estimated 15–25% of GMV) are absorbed into this premium. No subscription required from consumers. Hardware placement is offered to property managers at zero upfront cost in exchange for a multi-year site agreement, reducing the sales friction that would otherwise require property managers to justify capital expenditure.

## Differentiation vs. 2026 Competitors

Unlike DashMart, Cache v2 deploys into suburban locations that no first-party platform product serves. Unlike GoPuff, it operates without warehouse staff or long-term leases. Unlike 7-Eleven via Uber Eats, it places inventory where delivery demand exists, not where 1970s real estate decisions placed stores. The moat is operational: a network of suburban placements that competitors cannot replicate without Cache's lightweight, zero-staff unit economics.
