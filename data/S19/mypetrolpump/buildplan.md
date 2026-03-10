# Build Plan: MyPetrolPump 2026

## Overview

MyPetrolPump (ANB Fuels Pvt. Ltd.) was a Bengaluru-based B2B on-demand diesel delivery startup founded in 2016 by Ashish Gupta and Naveen Roy; it delivered fuel directly to fleet operators, apartment complexes, schools, and DG set owners across Bangalore, Hyderabad, and Pune before being acquired by FuelBuddy in May 2021 for undisclosed consideration — absorbed and dissolved, never scaled. The company's failure was not a market failure: 4,000 calls arrived within three days of launch, and the acquirer grew to 30 cities and 100+ refuellers post-merger. MyPetrolPump died because it was chronically undercapitalised relative to the hardware cost of its fleet, and because it operated in a regulatory grey zone that made institutional investors unwilling to commit the Series A it needed.

The rebuild thesis is this: PESO's 2021 draft amendment to Petroleum Rules has begun formalising the licensing framework that never existed for MyPetrolPump, IoT tank sensors now available under $50 per unit enable a predictive subscription model that improves route density and unit economics, and FuelBuddy's post-merger focus on bulk industrial customers (1,700L average order) has left the smaller B2B segment — apartment complexes, SME fleets, schools — structurally underserved. The new version is a managed energy infrastructure company for India's mid-market B2B segment: predictive, subscription-first, and built on a regulatory foundation its predecessor never had.

---

## Why Now?

## The single most important change since MyPetrolPump's failure is the emergence of a formal regulatory pathway for mobile fuel dispensing in India.

When MyPetrolPump launched in June 2017, it operated with no licence under Petroleum Rules, 2002 — a fact confirmed by RTI filings in April 2019. PESO shut it down within four days of commercial launch. The company spent its entire operational life in a regulatory grey zone that made institutional investors unwilling to commit capital at Series A scale. In 2021, PESO issued a draft amendment to Petroleum Rules specifically to regulate mobile fuel dispensing units. As of this writing, the precise status of that amendment's finalisation is not publicly confirmed in available sources, and a rebuild team must verify current licensing requirements directly with PESO before committing capital. However, even a draft framework represents a categorically different starting position than 2017: a new entrant can engage with a defined regulatory process rather than fight for the creation of one. This alone changes the investor conversation.

**Second, the unit economics problem is now solvable with hardware that did not exist at viable price points in 2017.** IoT-enabled ultrasonic tank level sensors are now available at under $50 per unit. Fitted to a customer's diesel generator or fuel storage tank, these sensors transmit real-time fuel level data, enabling the operator to predict refill timing, batch nearby orders into a single route, and shift from reactive on-demand delivery to proactive subscription dispatch. This directly attacks the utilisation problem that capped MyPetrolPump at roughly 2–3 orders per vehicle per shift: a predictive model allows route planning 24–48 hours in advance, increasing orders per vehicle per shift and reducing per-litre delivery cost.

**Third, the market proof point now exists.** The combined FuelBuddy entity had delivered approximately 40 million litres across 100,000 orders by May 2021. The $100 billion Indian HSD market cited at acquisition is no longer a first-principles argument — it is a demonstrated commercial reality. MyPetrolPump had to convince investors the market existed; a 2026 entrant does not.

**Fourth, UPI's near-universal B2B adoption eliminates the cash handling and reconciliation overhead** that would have complicated operations in 2017. Automated invoicing, recurring payment mandates via UPI AutoPay, and digital fuel logs are now standard infrastructure, not custom builds.

Specific distribution channels available now include the ONDC network (launched 2022–2023) for B2B commerce discovery, and WhatsApp Business API with 500M+ Indian users for low-friction B2B order management — neither existed at MyPetrolPump's launch.

---

## Current Market Analysis

## Market Size

The Indian high-speed diesel (HSD) market was cited at approximately $100 billion at the time of the FuelBuddy acquisition in May 2021, with doorstep delivery estimated to have potential for up to 26% market share — a $26 billion addressable opportunity. These figures should be treated as directional; they reflect total HSD consumption, not the subset realistically convertible to on-demand delivery. No updated independent market sizing for the doorstep B2B diesel delivery segment in 2025–2026 is available in public sources reviewed for this report, and a rebuild team should commission primary research before finalising TAM claims for investors. What is confirmed: FuelBuddy's continued growth post-acquisition across 30+ cities demonstrates the addressable market is large enough to sustain a well-capitalised operator.

## Competition Map and Gaps

The current competitive landscape is dominated by **FuelBuddy** (Treis Solutions LLP), which absorbed MyPetrolPump and has the largest fleet and geographic footprint in India. FuelBuddy's specific weakness is structural: its average order size of 1,700 litres reflects a deliberate focus on large industrial customers — refineries, large logistics hubs, construction sites. This leaves the mid-market B2B segment (apartment complexes with 50–200 units, SME fleets of 5–30 vehicles, small schools) underserved. FuelBuddy's route economics are optimised for bulk; a 300-litre apartment complex order is a poor fit for its model.

**Repos Energy** operates primarily in rural and semi-urban markets via a franchise model, with less urban B2B penetration. **PepFuel** and **Simply Auto** remain smaller regional operators; their current funding status and geographic reach are not confirmed in available sources and should be verified. No major platform incumbent — Indian Oil, BPCL, HPCL — has launched a credible on-demand B2B delivery product at scale. This is the defensibility question that requires honest treatment.

**Why won't the oil marketing companies (OMCs) simply add this feature?** The OMCs — Indian Oil, BPCL, HPCL — have the fuel supply relationships, brand trust, and capital to enter this market. They have not done so at scale for structural reasons: their distribution model is built around petrol station franchisees, who are a politically organised constituency that actively lobbied against MyPetrolPump in 2017. Cannibalising franchisee revenue is not in the OMCs' institutional interest. This is a real structural protection, not a permanent one — if the market grows large enough, OMC entry becomes more likely. A rebuild must be built to reach defensible customer lock-in (multi-year subscription contracts, embedded IoT hardware) before that window closes. There is no guarantee it will hold indefinitely, and this plan should not pretend otherwise.

**Demand signals from adjacent products:** The growth of backup power solutions (inverters, solar-plus-diesel hybrid systems) in Indian apartment complexes and the expansion of last-mile logistics fleets (Delhivery, Shadowfax, Porter) both increase the addressable base of recurring diesel consumers who would benefit from managed fuel delivery.

---

## Recommended MVP

## Feature 1: IoT Tank Monitoring + Predictive Dispatch

Install sub-$50 ultrasonic fuel level sensors on customer DG sets and fuel storage tanks at no upfront cost to the customer (hardware bundled into subscription). The sensor transmits real-time fuel levels to the operator's dispatch system, which triggers a delivery order when the tank crosses a defined threshold. This matters because it solves the utilisation problem that killed MyPetrolPump: predictive dispatch allows route batching 24–48 hours in advance, increasing orders per vehicle per shift from the estimated 2–3 reactive orders to a planned 4–6. Unlike the original, which was purely reactive and on-demand, this model gives the operator control over route density.

## Feature 2: Subscription Fuel Management for Mid-Market B2B

Offer apartment complexes, SME fleets, and small schools a monthly subscription that includes sensor hardware, automated refuelling when tanks drop below threshold, digital fuel logs, and a fixed per-litre delivery fee above the prevailing market price. Target a minimum order size of 500 litres (above MyPetrolPump's 300L average, below FuelBuddy's 1,700L) to improve per-trip economics while remaining accessible to the underserved mid-market. Subscription contracts of 12 months minimum create revenue predictability and reduce churn.

## Feature 3: Compliance-First Onboarding and Regulatory Dashboard

Build regulatory compliance into the product from day one: maintain a real-time dashboard of PESO licence status, vehicle inspection records, and supply chain documentation for every delivery. Share a simplified compliance summary with customers as part of the service — this is a trust signal that MyPetrolPump never had and that FuelBuddy's bulk-industrial focus may not prioritise for smaller customers. This feature also serves as investor due diligence collateral.

## Feature 4: WhatsApp-Native Order Management

For customers who do not want to manage an app, offer full order visibility, delivery confirmations, digital invoices, and UPI AutoPay via WhatsApp Business API. This reduces friction for the SME and apartment complex RWA (Resident Welfare Association) customer who manages fuel procurement informally today.

**What we will NOT build:** Consumer petrol delivery, a marketplace model connecting third-party drivers, or a hydrogen/EV charging product in the MVP phase. The original company's long-term energy platform vision was intellectually coherent but strategically distracting at the fundraising stage. The rebuild focuses exclusively on B2B diesel delivery until it reaches 50 vehicles and formal PESO licensing in two cities.

**Success Metrics:** 200 active subscription customers in one city within 12 months of launch; average order size ≥500 litres; ≥4 orders per vehicle per shift; customer churn below 5% monthly; PESO licence secured before the 6-month mark.

**Cold-Start Problem:** This model does not require network effects between customers — each subscription customer is independently valuable. However, route density requires geographic clustering: the MVP must target a single city (Bengaluru, given the original's strongest customer base there) and a single customer type (apartment complexes with DG sets) until it has 50 active sensor-equipped customers within a 15km radius. At that density, a single vehicle can serve 4–5 customers per shift on a predictive schedule. Reaching 50 customers requires approximately 8–10 weeks of direct B2B sales to RWAs, which is achievable with a two-person sales team.

---

## Go-to-Market Strategy

## Target Customer Segment

The primary target is apartment complex Resident Welfare Associations (RWAs) in Bengaluru with 100+ units and a diesel generator for backup power. This segment is narrow and specific for three reasons: DG sets create predictable, recurring diesel consumption (typically 50–200 litres per refuelling event); RWAs are a single point of contact for a building with dozens of implicit end-users; and Bengaluru's power infrastructure reliability issues make DG dependency structurally persistent. Secondary targets in months 7–12 are SME logistics fleets (5–20 vehicles) operating from fixed depots in Bengaluru's outer ring road industrial corridors.

## Primary Distribution Channel

Direct B2B sales through RWA management platforms — specifically ApnaComplex and MyGate, which together serve tens of thousands of apartment complexes in Bengaluru. Both platforms have B2B vendor partnership programmes. A listing as a verified fuel management vendor on these platforms provides access to a pre-qualified, geographically clustered customer base without cold outreach. This channel did not exist at MyPetrolPump's launch in 2017. Supplement with WhatsApp-based referral incentives between RWA managers, who communicate actively in city-level RWA WhatsApp groups.

## Pricing Strategy

Subscription fee: ₹2,999/month per customer, which includes sensor hardware, monitoring, and up to two scheduled deliveries. Fuel is charged at prevailing market price plus ₹1.50/litre delivery margin (above MyPetrolPump's Re 1/litre to reflect improved service and IoT value-add).

Stress test against free alternatives: An RWA manager today either sends a staff member to a petrol station (direct labour cost of 2–3 hours per trip, plus vehicle fuel cost) or calls an informal tanker supplier with no quality assurance or digital records. The ₹2,999/month subscription must be justified against this free-but-worse alternative. At two deliveries per month of 150 litres each, the subscription cost is approximately ₹10/litre in service fee — a premium that is justifiable if the RWA manager values staff time, fuel quality assurance, and digital invoicing for society accounts. If they do not, the price will not hold. Sales conversations must lead with the staff time and accountability argument, not the convenience argument.38:T827,

## Differentiation vs. 2026 Competitors

Against FuelBuddy: smaller minimum order, IoT-enabled predictive service, and a subscription model designed for mid-market customers FuelBuddy's bulk focus deprioritises. Against informal tanker suppliers: PESO-compliant documentation, quality-assured fuel sourced from authorised OMC dealers, and digital invoicing. Against doing nothing: quantified staff time savings and elimination of emergency fuel-out events, which carry real operational and reputational cost for RWA committees.
