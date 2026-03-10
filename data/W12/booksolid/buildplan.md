# Build Plan: BookSolid 2026

## Overview

BookSolid 2026 targets independent tour operators drowning in manual booking logistics. The platform is a lightweight SaaS dashboard + consumer marketplace that lets operators manage inventory, pricing, and payouts in one place while reaching travelers through a curated booking interface. Think Stripe for tour operators—we handle the infrastructure, they keep the customer relationship.

The market has fundamentally shifted. Marketplace infrastructure is now commoditized (Stripe Connect, GPT-4 for content, no-code backends). Viator dominates but extracts 25-35% commissions and provides operators almost no analytics or control. Meanwhile, the tours and activities market hit $254B globally in 2023, with independent operators still fragmented across spreadsheets and email.

We win by going narrow first: launch in one high-tourism U.S. city targeting operators running 3-15 experiences. Offer 12-15% commission (half Viator's rate), AI-generated listings, and real demand analytics. Operators get profitability; travelers get transparent, operator-direct bookings. Expand city by city as unit economics prove.

## Why Now?

The single most important change since BookSolid's failure is the commoditization of marketplace infrastructure. In 2012, a solo founder had to build payment splitting, operator dashboards, consumer search, and booking logic from scratch—consuming most of a $120K runway before acquiring a single customer. In 2026, Stripe Connect handles multi-party payouts, commission splits, and refund logic via API calls. This alone collapses what was once a 6–12 month engineering workload into weeks, fundamentally changing the capital math that killed BookSolid.

The second structural shift is distribution. FareHarbor (acquired by Booking.com for a reported ~$250M in 2018) now serves an estimated 20,000+ tour operators as their primary booking software. This creates a known, concentrated supply base that BookSolid never had access to. Rather than cold-calling fragmented operators, a 2026 rebuild can target operators already digitized and already paying for SaaS tools—dramatically reducing supply-side acquisition costs.

On the demand side, consumer behavior has completed the shift BookSolid was betting on prematurely. U.S. travel spending exceeded $1.1 trillion in 2023 (U.S. Travel Association), and Google's "Things to Do" API, launched in 2021, now surfaces activity listings directly in search results—meaning operators with structured inventory data receive organic discovery at no cost. Airbnb Experiences, launched in 2016, normalized the concept of booking local experiences online for a generation of travelers.

Finally, GPT-4 (March 2023) and its successors enable near-zero-cost generation of SEO-optimized tour descriptions, multilingual listings, and structured metadata—eliminating the content operations burden that made scaling marketplace supply expensive for every competitor in this category, including GetYourGuide, which spent years and tens of millions solving this manually.

The market BookSolid was too early and too undercapitalized to build is now ready to be rebuilt leaner, faster, and with a defensible distribution wedge.

---

## Current Market Analysis

The global tours, activities, and experiences market is estimated at approximately $254 billion in 2023, up from roughly $100 billion in the early 2010s when BookSolid operated (source: Allied Market Research; note that methodology varies across research firms and exact figures should be independently verified). Online penetration, historically the category's weakness, has accelerated significantly post-COVID, though precise current penetration rates are not available in public sources.

## Competitive landscape in 2026:

- **Viator (TripAdvisor subsidiary):** The dominant consumer marketplace with the largest inventory globally. Core weakness: operator commission rates of 20–30% are widely resented, and operators report slow payout cycles and limited control over listing presentation. Viator competes for the same consumer eyeballs as its parent, creating internal prioritization conflicts.

- **GetYourGuide:** Valued at $1.9 billion as of 2019 (most recent public valuation; current figure unknown). Strong in Europe, weaker in North America and Southeast Asia. Weakness: heavily dependent on paid search acquisition, making unit economics fragile when Google changes ad auction dynamics. Operator tools remain secondary to the consumer marketplace.

- **Airbnb Experiences:** Embedded within Airbnb's accommodation funnel. Weakness: strict curation limits supply breadth; operators report inconsistent approval processes and limited analytics. Not designed for professional tour operators running multi-SKU businesses.

- **FareHarbor / Rezdy / Peek Pro:** Pure B2B SaaS booking tools. Weakness: they solve operator-side management but provide no consumer discovery layer—operators still depend on Viator or Google for demand. This gap is the primary opportunity.

**The gap:** No current competitor successfully combines operator-grade SaaS tools with a consumer discovery layer that operators control and trust. The rebuild targets exactly this white space—a platform where operators pay for tools and retain margin, rather than surrendering it to a marketplace intermediary.

Adjacent demand signal: FareHarbor's reported acquisition price of ~$250M for a pure B2B tool confirms operators will pay for software. The question is whether they'll pay more for software that also generates demand.

---

## Recommended MVP

### Core Feature 1: Operator Booking & Inventory Management Dashboard

A lightweight SaaS dashboard allowing tour operators to manage availability, capacity, pricing tiers, and booking confirmations in one interface. This matters because FareHarbor's dominance proves operators will pay for this functionality, but FareHarbor charges operators while providing no discovery benefit. The 2026 version integrates directly with Google Things to Do API (launched 2021) to push structured inventory data into organic search results automatically—something BookSolid could not have done and FareHarbor does not prioritize.

## Core Feature 2: AI-Assisted Listing Generation

Using GPT-4o (released May 2024) or equivalent, the platform auto-generates SEO-optimized tour descriptions, structured metadata, and multilingual variants from a short operator input form. This eliminates the content operations bottleneck that made marketplace supply scaling expensive for every prior competitor. It directly addresses the solo-founder constraint that hurt BookSolid: content at scale requires no additional headcount.

## Core Feature 3: Stripe Connect–Powered Marketplace Checkout

A consumer-facing booking and payment flow built on Stripe Connect, handling commission splits, operator payouts (T+2), and refund logic without custom payment engineering. Commission is set at 12%—below Viator's 20–30%—as the primary operator acquisition argument. This is the infrastructure BookSolid would have spent months building in 2012; in 2026 it is a configuration task.

## Core Feature 4: Operator Analytics & Demand Reporting

A simple dashboard showing operators which listings generate views, conversion rates by channel, and revenue attribution. Competitors provide minimal transparency here. This builds operator trust and reduces churn.

**What we will NOT build:** A consumer brand or paid consumer acquisition channel in Year 1. No mobile app. No international markets. No group booking or corporate travel features.

**Success metrics:** 50 operators onboarded within 90 days of launch; $25,000 gross merchandise value (GMV) processed in Month 3; operator monthly churn below 5%; average operator rating of the platform above 4.2/5 at 90 days.

---

## Go-to-Market Strategy

**Target customer (Year 1):** Independent tour operators in a single U.S. metro with high tourism density—specifically, operators running 3–15 SKUs (tours or experiences), generating $100K–$1M in annual revenue, currently using FareHarbor or Peek Pro for booking management but dependent on Viator for discovery. This segment is digitally literate enough to adopt new software quickly but small enough to be underserved by enterprise-focused competitors. New Orleans, Nashville, or Scottsdale are candidate launch markets (specific market selection should be validated with operator density data before committing).

**Primary distribution channel:** Direct outreach to operators already listed on Viator, using Viator's public marketplace as a prospecting database. Operators visible on Viator are pre-qualified: they have inventory, they accept online bookings, and they are paying 20–30% commission—making a 12% alternative a concrete, calculable savings pitch. Secondary channel: FareHarbor integration partnership or API connection, allowing operators to import existing inventory without re-entry (feasibility subject to FareHarbor's API terms, which should be verified).

**Pricing:** $99/month SaaS fee per operator plus 12% commission on marketplace-sourced bookings. The SaaS fee covers dashboard, AI listing tools, and analytics regardless of booking volume. The commission applies only to bookings the platform generates—operators pay nothing extra for bookings from their own channels. This hybrid model mirrors FareHarbor's proven willingness-to-pay while adding a demand-generation value proposition Viator charges twice as much to provide.

**Differentiation vs. 2026 competitors:** The rebuild's core argument to operators is margin preservation plus discovery—a combination no current competitor offers. Viator provides discovery but extracts 20–30%. FareHarbor provides tools but no discovery. The rebuild provides both at a lower combined cost, with full operator control over listing presentation and pricing. Against GetYourGuide, the differentiation is geographic focus and operator relationship depth in a single market before expanding—a lesson directly traceable to BookSolid's failure to concentrate supply before scaling.
