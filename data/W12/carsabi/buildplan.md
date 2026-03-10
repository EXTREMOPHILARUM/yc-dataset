# Build Plan: Carsabi 2026

## Overview

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
