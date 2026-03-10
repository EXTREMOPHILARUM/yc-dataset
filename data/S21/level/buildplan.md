# Build Plan: Level 2026

## Overview

## Why Now?

## The single most important change since Level's failure is the collapse in the cost of underwriting infrastructure.

In 2021, Level had to build its loan tape ingestion, borrower monitoring, and credit decisioning stack largely from scratch, against a $2.3M equity base that also had to fund the loan book itself. In 2026, that same stack can be assembled from commodity components at a fraction of the cost — and that changes the math on whether a small team can reach institutional debt thresholds before running out of runway.

## Specific technology shifts:

## Market validation since 2021:

## Current Market Analysis

## Market size:

The total U.S. warehouse lending market is estimated in the hundreds of billions of dollars annually, but that figure is dominated by mortgage warehouse lines and large-scale consumer lending facilities — not the early-stage fintech segment Level targeted. The addressable market for a rebuilt Level is the sub-$10M first warehouse facility segment: companies that have originated loans, have 3–12 months of performance data, and are too small for traditional specialty finance lenders whose minimums typically start at $10M–$25M. Precise sizing of this segment is not publicly available; this is a known gap in the research.

What is documentable: YC alone has backed 40+ lending-adjacent companies since 2019 (YC company directory, public). Across all accelerators and seed funds globally, the pipeline of new fintech lenders entering the market each year is in the hundreds. Each one faces the same cold-start capital problem Level identified.

## Competition map:

## Defensibility against platform incumbents:

This is the honest answer: Stripe, Unit, and Synctera are the most plausible platform threats. Stripe Capital already extends financing to Stripe users; it could theoretically extend warehouse-style facilities to fintech lenders built on Stripe Treasury. The structural defense is that warehouse lending for third-party lenders requires credit underwriting of *loan portfolios* — a fundamentally different risk model than underwriting a merchant's payment volume. Stripe has no demonstrated appetite for this complexity. Unit and Synctera are infrastructure providers, not balance sheet lenders; they have no incentive to compete with their own customers' capital providers. The more honest risk is not platform commoditization but a well-capitalized specialty finance entrant deciding the segment is worth serving — and there is no permanent structural defense against that. Speed to data moat (proprietary loan performance benchmarks across dozens of early-stage lenders) is the best available answer.

---

## Recommended MVP

## Core features:

## Automated loan tape ingestion and scoring (the underwriting engine)

Connects to a borrower's loan origination system or accounting platform via Plaid, MX, or direct API, ingests the loan tape, and uses an LLM-assisted pipeline (built on GPT-4o or Claude 3.5 Sonnet, both available as of mid-2024) to normalize, validate, and score the portfolio against configurable credit criteria. This is the direct successor to Level's original underwriting engine, but built on commodity AI infrastructure rather than custom NLP — reducing build time from months to weeks and marginal cost per underwrite to near zero. Unlike the original, this engine produces an auditable, structured credit memo that can be shared with co-investors or future institutional lenders, accelerating the borrower's path to graduation.

## Graduated facility management dashboard

A borrower-facing interface showing current facility utilization, available capacity, performance metrics, and the specific milestones (e.g., 6 months of <2% delinquency on $500K+ in originations) required to unlock the next tranche. This directly addresses Level's transitional product problem by making the graduation path explicit and measurable — turning "outgrowing Level" into a feature, not a churn event, because the platform generates the documentation package a borrower needs to approach a traditional warehouse lender.

## Syndicated capital layer (not a pure balance sheet model)

Rather than deploying only equity capital into loan purchases — the constraint that killed the original Level — the rebuild structures each facility as a co-investment between the platform's balance sheet (10–20% first-loss tranche) and a small network of accredited investors or family offices seeking yield. This is the structural fix the original lacked. Percent and similar platforms have demonstrated this model is executable. The platform earns an origination fee plus a servicing spread; the balance sheet exposure per facility is capped, extending runway dramatically.

**What you will NOT build:** A consumer-facing lending product, a mortgage warehouse facility, a full loan origination system for borrowers' end customers, or any product targeting lenders with existing institutional warehouse relationships. Stay in the $500K–$5M, sub-12-month-history lane until the data moat is established.

## Success metrics:

- 10 active borrowers with at least one funded facility within 6 months of launch
- Average time-to-first-funding under 3 weeks (vs. 3–6 months for traditional warehouse lines)
- Net credit loss rate under 3% annualized across the portfolio
- At least 3 borrowers successfully "graduated" to a traditional warehouse facility within 18 months, with Level-generated documentation cited in the new lender's diligence

**Cold-start note:** This product does not require network effects or local density. Each borrower relationship is bilateral. The minimum viable portfolio is 3–5 active facilities — enough to generate meaningful performance data and stress-test the underwriting model. Reach that threshold through direct outreach to YC fintech lending alumni (a warm, accessible channel) before building any inbound marketing.

---

## Go-to-Market Strategy

## Target customer segment:

YC-backed and top-accelerator-backed fintech lending startups in their first 6–18 months of origination, with $200K–$2M in loans already on book, seeking their first $500K–$3M warehouse facility. This is narrow by design. These founders are reachable, credible-reference-able, and acutely aware of the capital problem — they have already built a product and proven demand; the warehouse gap is their stated #1 growth constraint.

## Primary distribution channel:

Direct outreach through the YC alumni network, fintech accelerator demo days (Barclays, Plug and Play, Techstars Fintech), and fintech founder Slack communities (Fintech Devs, Fintech Founders). The original Level had this channel available and used it — the rebuild should treat it as the only channel for the first 12 months. A single warm introduction from a YC partner or a respected fintech founder carries more weight than any paid acquisition strategy in this segment.

## Pricing strategy:

Origination fee of 1.5–2.5% on each facility, plus a monthly servicing spread of 1.0–1.5% annualized on deployed capital. Total cost to a borrower on a $1M facility: approximately $15,000–$25,000 upfront plus $10,000–$15,000 annually in servicing costs.

*Stress test against free alternatives:* The relevant free alternative is not a group chat or an OS feature — it is the absence of capital entirely, or a friends-and-family equity round at 20–30% dilution. A $1M warehouse facility at 3–4% all-in annual cost is dramatically cheaper than equity dilution and faster than any traditional lender. The pricing is defensible not against free alternatives but against the cost of *not* having the capital. The risk is not that borrowers find a cheaper option; it is that they cannot afford the fees at all in a cash-constrained early stage. Mitigate by structuring origination fees as deductible from the first facility draw rather than payable upfront.

## Differentiation vs. 2026 competitors:

Percent serves larger, more established borrowers. Capchase and Arc serve SaaS companies, not lenders. No current competitor offers a purpose-built, graduated warehouse facility for sub-$5M fintech lenders with an explicit graduation pathway. The rebuild's differentiation is specificity: every feature, every underwriting criterion, and every pricing structure is designed for exactly one customer type — and that specificity is the product.
