# Build Plan: Carsabi 2026

## Overview

The single most important change since Carsabi's failure is the emergence of licensed, commercial automotive data infrastructure that eliminates the scraping dependency that killed the original company overnight. In 2012, there was no clean path to Craigslist's private-party inventory without unauthorized crawling. In 2026, that constraint is gone.

MarketCheck now offers real-time licensed feeds covering 6+ million active used car listings from dealers, auctions, and classifieds. Similar structured inventory APIs are available from Lotame and through OEM data partnerships. Facebook Marketplace—which has displaced Craigslist as the dominant private-party car listing platform in most U.S. markets—offers a Partner API accessible through approved integrations. OfferUp provides additional private-party inventory. A rebuilt Carsabi could negotiate data licensing agreements before writing a single line of product code, making data access a business development problem rather than a legal time bomb.

The second structural shift is on the extraction side. GPT-4 (March 2023) and Claude 3 (March 2024) can parse unstructured dealer website listings, inconsistent classified formats, and PDF inventories with accuracy that would have required months of custom engineering in 2012. What took Berner and Crow three months to build for 20,000 listings per day can now be scaffolded in weeks and scaled to millions.

The market has also validated Carsabi's core thesis. CarGurus built a $1B+ public company on its "Instant Market Value" and "Deal Rating" features—essentially the "sort by biggest savings" ranking Carsabi pioneered. CarGurus' 2023 annual revenue was approximately $869 million (CarGurus 10-K, 2023), confirming that consumers respond to relative value signals when buying used cars. The demand was always real. The data infrastructure to serve it reliably was not.

---

## Why Now?

## Current Market Analysis

The U.S. used car market has grown substantially since 2012. At Demo Day, Carsabi cited $650 billion in total annual car sales. The used car segment specifically reached approximately $840 billion globally in 2023, with the U.S. representing the largest single market (Grand View Research, 2024—exact U.S.-only figure not confirmed in research report). COVID-era digital acceleration normalized online-first car research and purchasing: Carvana, Vroom, and CarMax's online channel all scaled significantly between 2020 and 2023, reducing the consumer education burden a new aggregator would face.

## Current competitor map:

- **CarGurus** (public, ~$869M 2023 revenue): Closest analog to the rebuilt vision. Weakness: dealer-centric inventory model underrepresents private-party listings; Deal Rating algorithm is opaque to users; no AI-assisted search or conversational interface.
- **Cars.com** (public): Traditional dealer listing network. Weakness: no meaningful value-ranking; UI largely unchanged since 2012; no private-party inventory integration.
- **AutoTrader/KBB** (Cox Automotive): Dominant brand awareness, massive dealer network. Weakness: consumer experience is ad-heavy and optimized for dealer revenue over buyer outcomes; no cross-source aggregation.
- **Carvana**: Transactional, not search. Weakness: inventory limited to Carvana-owned vehicles; no comparison across sources.
- **Facebook Marketplace**: Largest private-party inventory. Weakness: zero value-ranking, no structured search, no deal quality signals.

**The gap:** No current product aggregates dealer *and* private-party inventory across all major sources while surfacing value-relative rankings with AI-assisted natural language search. CarGurus comes closest but excludes Facebook Marketplace's private-party volume. That gap is the rebuild opportunity.

---36:T673,

## Recommended MVP

## Feature 1: Licensed Multi-Source Inventory Aggregation

Ingest real-time used car listings via licensed API feeds from MarketCheck (dealer inventory), Facebook Marketplace Partner API (private-party), and OfferUp (private-party), covering the full market spectrum Carsabi attempted to scrape. This directly solves the original failure mode—data access is contractual, not contingent on a platform's tolerance for crawlers. Unlike Carsabi, no single source termination kills the product.

## Feature 2: AI-Powered Deal Score

Using GPT-4o (May 2024) or equivalent, calculate a real-time Deal Score for every listing by comparing price against a dynamic fair market value model built from comparable recent sales in the same geography. Surface this score prominently in search results, ranked by savings percentage rather than raw price. This is the "biggest savings" feature Carsabi pioneered, now executable with LLM-assisted valuation modeling rather than hand-coded heuristics.

## Feature 3: Natural Language Search

Allow buyers to query in plain English ("reliable SUV under $20k with low miles, good in snow") and return ranked results across all sources. No current major competitor offers this. Differentiation from CarGurus is immediate and demonstrable.

**What we will NOT build:** Dealer CRM tools, financing integrations, transaction processing, social sharing features, or mobile apps in the MVP phase. No feature that requires dealer sales relationships to function.

## Success metrics:

- 50,000 monthly active searchers within 6 months of launch
- Data licensing agreements with at least 3 sources covering 500,000+ active listings at launch
- 40%+ 7-day search return rate (users returning to check deal updates)

---

## Go-to-Market Strategy

**Target customer:** Private buyers aged 28–45 actively searching for a used vehicle priced $10,000–$35,000, who have already decided on a make/model and need help identifying the best available deal across fragmented sources. This is the highest-intent, lowest-education-cost segment—they know what they want, they distrust dealers, and they will immediately understand the value of a cross-source Deal Score.

**Primary distribution channel:** SEO via long-tail automotive search queries ("best deal on 2021 Honda CR-V in [city]"), supplemented by Reddit communities (r/whatcarshouldibuy, r/UsedCars, combined 800,000+ subscribers) where deal-hunting buyers are already active and receptive to tool recommendations. No paid acquisition in year one.

**Secondary channel:** The Shopify App Store analogy does not apply here, but the CarGurus affiliate program and automotive finance blogs (e.g., NerdWallet's auto section) offer cost-effective referral traffic from high-intent audiences.

**Pricing:** Free consumer search, monetized through dealer lead generation at $15–$40 per qualified lead (consistent with industry standard; CarGurus charges dealers in this range per connection). Avoid display advertising in MVP—it signals dealer capture to the exact buyers the product is trying to win.

**Differentiation vs. 2026 competitors:** Every major incumbent is optimized for dealer revenue. The rebuild's positioning is explicitly buyer-side: licensed data, transparent Deal Scores, natural language search, and zero dealer-paid ranking manipulation. CarGurus' weakness—opacity and dealer-first incentives—is the rebuild's headline.
