# Build Plan: Onsite Pro 2026

## Overview

Onsite Pro (incorporated as Greenwork Inc.) launched in March 2021, passed through YC S21, raised $2.4M from GV and Kleiner Perkins Scout Fund, executed two full pivots — from clean energy training to a hiring marketplace, then to HVAC distributor proposal software — and went inactive by 2025 after exhausting its runway without achieving durable product-market fit in any of the three bets. The core failure was arithmetic: two pivots on a pre-seed budget left the final HVAC product with 12–18 months of runway and no reference customers before founder fatigue ended the run.

The rebuild thesis is this: LLMs have eliminated the manual pricebook onboarding cost that made Onsite Pro's distributor model unscalable, IRA incentive APIs now make real-time rebate calculation a software feature rather than a full-time data job, and embedded lending infrastructure turns the proposal tool into a financing origination channel — making the unit economics work where they previously couldn't. The new version is a distributor-facing proposal platform that onboards a pricebook in minutes, calculates live federal and state incentives, and earns revenue on every financed deal it closes.

---

## Why Now?

### The single most important change: LLM-powered catalog ingestion makes the distributor onboarding problem disappear.

Onsite Pro's B2B2C model required loading each distributor's pricebook — SKUs, pricing tiers, AHRI certification matchups, availability — before a single contractor could use the tool. In 2022–2023, this was a manual, labor-intensive process that constrained how many distributors could be onboarded and made the unit economics of pursuing long-tail regional distributors unworkable. GPT-4 (March 2023) and its successors can now extract structured product data from unstructured distributor PDFs, Excel exports, and legacy catalog formats with high accuracy. What previously took days of data entry now takes minutes of automated parsing. This is not a marginal improvement — it removes the primary operational bottleneck that made Onsite Pro's model slow to scale.

**The IRA created a regulatory forcing function that didn't exist in 2022.** The Inflation Reduction Act (signed August 2022) introduced Section 25C tax credits of up to $2,000 for heat pump installations and Section 25D credits for related equipment. State-level programs layered on top — California's TECH Clean California, New York's Clean Heat program, and others — created a patchwork of incentives that contractors must navigate on every proposal. Rewiring America launched a public incentive API (2023) that aggregates federal and state incentive data by zip code. A proposal tool that pulls live incentive calculations into a customer-facing quote is now buildable as a software feature; in 2022, it required a manual research operation. This is a genuine product differentiator that Onsite Pro listed as a goal but could not execute at scale.

**Embedded lending infrastructure has matured.** Unit and Stripe Treasury (both broadly available by 2023–2024) allow software companies to originate financing products without a bank charter. HVAC financing — typically 12–60 month installment loans for $5,000–$20,000 replacement systems — is a high-demand product that contractors currently source through fragmented relationships with GreenSky, FTL Finance, and manufacturer programs. A proposal tool that originates financing at the point of proposal, earning 1–3% of financed volume, generates revenue per closed deal rather than per seat — a fundamentally different and higher-ceiling business model than Onsite Pro's flat pricebook fee.

**Market size signal:** The US residential HVAC replacement market exceeds $15 billion annually in equipment sales alone (source: research report). The field service software market was valued at approximately $3 billion in 2021 and has grown since, validated by ServiceTitan's 2024 IPO. Specific 2026 market size data for the distributor software sub-segment is not available in the research report.

**Distribution channel available now:** HARDI (Heating, Air-conditioning & Refrigeration Distributors International) has an established member directory and annual conference. Onsite Pro joined HARDI — the rebuild inherits that institutional entry point without needing to re-establish it from scratch.

---

## Current Market Analysis

**Market size:** The US HVAC replacement market generates over $15 billion annually in equipment sales, with 5–6 million residential replacement systems installed per year (per research report). The distributor software sub-segment is not independently sized in available data — this is a gap the rebuild team should validate through HARDI member interviews before committing to a pricing model. The broader field service software market, validated by ServiceTitan's 2024 IPO and Jobber's continued growth, confirms that HVAC contractors will pay for software at scale.

## Competition map:

- **ServiceTitan** (dominant FSM platform, $500M+ raised, 2024 IPO): Owns the contractor's daily workflow — scheduling, dispatch, invoicing — and has been systematically expanding its feature set. Its specific weakness in this context is the distributor relationship layer: ServiceTitan sells to contractors, not distributors, and its pricebook integrations are contractor-initiated rather than distributor-pushed. It is the most dangerous platform incumbent, but its go-to-market motion does not naturally reach regional distributors.

- **Jobber** (SMB-focused FSM, strong in Canada and US): Similar profile to ServiceTitan at smaller scale. Weak on proposal sophistication and has no distributor-side product.

- **Contractor Commerce**: The closest direct analog — targets the digital sales layer for HVAC contractors. Approaches from the contractor side rather than the distributor side, which means it lacks the pricebook integration and AHRI matchup depth that makes a distributor-anchored tool sticky. No disclosed funding or scale data available.

- **Manufacturer-owned tools** (Goodman/Daikin, Carrier, Lennox): The most structurally dangerous competitor. Manufacturers can offer proposal tools for free because the tool drives equipment sales. The rebuild's answer to this threat must be **brand neutrality**: a distributor that carries Carrier, Goodman, and Lennox equipment cannot use a manufacturer-subsidized tool without disadvantaging two of its three lines. A neutral, multi-brand proposal platform is the only product a multi-line distributor can deploy without alienating manufacturer partners. This is a genuine structural advantage — but it requires the rebuild to maintain strict neutrality and resist any manufacturer partnership that would compromise it.

**Defensibility against platform incumbents:** ServiceTitan could add distributor-side pricebook management, but its entire go-to-market is contractor-facing. Adding a distributor sales motion would require a separate product team, a separate sales team, and a willingness to compete with the manufacturers whose equipment data ServiceTitan already integrates. This is a real but not permanent moat — the rebuild has a 2–3 year window before ServiceTitan's expansion logic reaches this layer. The rebuild must use that window to establish reference distributor relationships that create switching costs before the platform arrives.

**Demand signals from adjacent products:** Electrical distributor platforms (e.g., Clippings in the UK, Procore's supply chain integrations) and plumbing supply chain software have validated that distributors in adjacent trades will pay for digital catalog and proposal infrastructure. This is a meaningful analog signal.

---

## Recommended MVP

## Core features:

### LLM-Powered Pricebook Onboarding

A distributor uploads their existing catalog — PDF, Excel, or EDI export — and the system uses GPT-4o (available April 2024) to extract SKUs, pricing tiers, AHRI certification numbers, and system matchup rules into a structured database. This eliminates the manual data entry that made Onsite Pro's onboarding slow and expensive. The original Onsite Pro required human effort to load each pricebook; the rebuild makes onboarding a self-serve, sub-hour process. Target: a distributor can go from upload to live pricebook in under 60 minutes without engineering support.

## Live Incentive-Integrated Proposal Builder

Contractors enter a customer's zip code, existing system specs, and replacement equipment selection; the tool pulls real-time federal (IRA Section 25C/25D) and state incentive data via Rewiring America's API and calculates the net customer cost automatically. The output is a professional, customer-ready PDF proposal showing gross price, applicable rebates, net price, and financing options. Onsite Pro listed incentive integration as a feature but could not maintain it at scale without a dedicated data team; the API layer makes this a software problem, not a staffing problem.

## Embedded Financing Origination

At the point of proposal acceptance, the contractor can submit a financing application through an embedded lending partner (Unit or a direct integration with GreenSky or FTL Finance). The rebuild earns 1–3% of financed volume as an origination fee — a revenue model that scales with deal value rather than seat count. This transforms the tool from a proposal SaaS into a financing origination channel, which is a materially higher-margin business.

## What we will NOT build (MVP scope):

- Scheduling, dispatch, or invoicing (ServiceTitan's territory; do not compete)
- A contractor-facing mobile app (web-first, tablet-optimized only)
- A clean energy hiring marketplace (the original Greenwork thesis; a separate product requiring separate capital)
- Multi-trade support (plumbing, electrical) until HVAC is proven

## Success metrics with thresholds:

- 5 paying distributor customers within 6 months of launch (proof that the sales motion works)
- Average pricebook onboarding time under 60 minutes (proof that LLM ingestion delivers on its promise)
- 20%+ of proposals resulting in a financing application (proof that the embedded lending feature has real contractor adoption)
- Net Revenue Retention > 100% at 12 months (proof that distributors expand usage rather than churn)

**Cold-start problem:** This product does not depend on network effects or local density. A single distributor with 50 contractor customers delivers immediate value to those contractors on day one — the pricebook is populated, the proposals work, and the incentive data is live. There is no minimum user threshold before the core feature delivers value. The cold-start challenge is distributor acquisition, not user density.

---

## Go-to-Market Strategy

**Target customer segment:** Regional HVAC distributors with 3–15 locations, carrying 2+ equipment brands (multi-line), operating in states with active IRA incentive programs (California, New York, Massachusetts, Colorado, Illinois). These distributors are large enough to have a dedicated sales or marketing budget but small enough that manufacturer-owned tools — which favor single-brand ecosystems — are not a viable option. They have the most to gain from a neutral, multi-brand proposal platform and the most pain from the current manual proposal process.

**Primary distribution channel:** Direct outbound through HARDI membership and conference attendance. HARDI's annual conference (HARDI Summit) is the primary gathering point for HVAC distributors. Onsite Pro established HARDI membership — the rebuild should treat this as a warm channel, not a cold one. Target 3 signed distributor pilots from the first HARDI Summit appearance. Secondary channel: referrals from HVAC financing partners (GreenSky, FTL Finance) who have existing distributor relationships and a direct incentive to refer a tool that increases their own financing volume.

**Pricing strategy:** $500–$800/month per distributor location, plus 1.5% of financed volume originated through the platform. The SaaS fee is justified by the pricebook onboarding, AHRI matchup maintenance, and incentive data infrastructure — services the distributor currently either pays staff to manage or doesn't do at all. The financing origination fee is the growth lever: a distributor location closing 20 financed deals per month at an average of $8,000 per system generates $2,400/month in origination revenue to the rebuild, making the total revenue per location $2,900–$3,200/month at modest financing attachment rates.

**Stress-testing against free alternatives:** The primary free alternative is the manufacturer-subsidized tool (e.g., a Goodman-provided proposal app). The rebuild's answer is brand neutrality — a multi-line distributor cannot use a manufacturer tool without disadvantaging competing lines. The secondary free alternative is a contractor using a generic quoting tool (Google Sheets, Jobber's basic quoting). The rebuild's answer is the incentive integration: a contractor cannot calculate live IRA rebates in a spreadsheet without manually researching state and federal programs, which takes 30–60 minutes per proposal. The rebuild does it in seconds. The price is justified if it saves a contractor one lost deal per month — at $8,000 average system value, the math is not close.

**Differentiation vs. 2026 competitors:** ServiceTitan does not have a distributor-facing product. Contractor Commerce does not have live incentive integration or embedded financing. Manufacturer tools are not brand-neutral. The rebuild occupies a specific, defensible position at the intersection of distributor neutrality, IRA incentive automation, and financing origination — none of which any current competitor addresses simultaneously.
