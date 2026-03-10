# Build Plan: CapWay 2026

## Overview

The 2026 CapWay targets hourly workers at mid-sized employers—retail, food service, logistics—who get paid weekly or bi-weekly but lack reliable banking infrastructure. It's a white-labeled embedded finance play: employers become the distribution channel, offering CapWay accounts as a payroll benefit that workers can access immediately, with no credit checks or minimum balances.

The infrastructure shift that makes this viable now is the post-Synapse rebuild. The middleware collapse forced fintech to move away from fragile third-party layers toward direct bank partnerships and cleaner APIs. That means lower operational risk and faster onboarding—exactly what employers need to integrate payroll accounts at scale.

The go-to-market angle is employer-first, not consumer-first. You're not competing with Chime for attention in an app store. You're selling HR and payroll teams a retention tool that costs them nothing to offer and solves real cash-flow problems for their workforce. Workers get same-day or next-day access to earned wages. Employers reduce turnover. You build a defensible moat through embedded distribution.33:T8df,

## Why Now?

## Current Market Analysis

**Market Size:** The U.S. underbanked population stands at approximately 19 million households as of the FDIC's 2023 survey, down from the 52 million "financially underserved" figure CapWay cited in 2020 — a number that used a broader definition including the working poor in banking deserts. The narrower FDIC underbanked figure is still a substantial addressable market. Precise TAM figures for employer-sponsored financial wellness specifically are not available in the research report, but DailyPay's $1.75 billion valuation and Walmart's acquisition of Even signal that the B2B2C channel serving hourly workers is a multi-billion-dollar segment.

## Competition Map:

- **Chime** (est. 22M customers, 2023): Dominant in mobile-first banking for underserved millennials, but optimized for direct deposit users with stable income. Weak on financial literacy, weak on rural/banking-desert distribution, and facing its own profitability pressure post-2022 valuation reset.
- **Current** (raised $220M+ through 2021, status unclear): Explicitly targeted the underbanked demographic and was cited by investors as the reason to pass on CapWay. Current's specific weakness: no employer-sponsored distribution channel and no AI-powered coaching layer. Post-2022 fintech downturn fundraising status is not confirmed in available sources.
- **Cash App** (Block, Inc.): Massive distribution but not designed for the unbanked; lacks financial literacy infrastructure and employer partnerships.
- **Dave** and **Varo**: Adjacent positioning; Varo holds a national bank charter but has reported significant losses and has not demonstrated profitability serving low-income users.

**Gaps:** No current competitor combines employer-sponsored B2B2C distribution, AI-powered financial coaching, and direct-BaaS infrastructure targeting banking-desert geographies. The CRA modernization finalized in 2023 by the OCC, FDIC, and Federal Reserve creates new incentives for large banks to partner with fintechs serving exactly these geographies — a partnership channel that did not exist during CapWay's operating years.

**Demand Signals:** DailyPay's growth, Walmart's Even acquisition, and the proliferation of earned wage access products confirm that hourly workers — CapWay's core demographic — are actively seeking and adopting employer-distributed financial tools.

---

## Recommended MVP

## Core Features:

**1. Employer-Sponsored Account Onboarding.** A white-labeled onboarding flow that employers (retailers, logistics companies, food service operators) deploy to hourly workers as a payroll benefit, pre-loading the CapWay account with the worker's first direct deposit. This matters because it eliminates the direct-to-consumer customer acquisition cost that made the interchange model unworkable at CapWay's funding level. Unlike the original CapWay, which identified this channel but did not scale it, the 2026 rebuild makes employer distribution the *primary* go-to-market motion, not a secondary experiment.

**2. AI-Powered Financial Coaching via GPT-4o (released May 2024) or Claude 3.5.** A conversational in-app coach that answers questions about overdraft fees, savings goals, credit building, and bill management in plain language — personalized to the user's actual transaction history. This replaces CapWay's manually produced static financial literacy modules with a near-zero marginal cost, always-current alternative. The differentiation from Chime and Current is direct: neither offers conversational AI coaching embedded in the account experience.

**3. Direct-BaaS Account and Debit Card via Column Bank or Synctera.** FDIC-insured checking account and Visa debit card built on a direct-bank API stack, eliminating the Synapse-style middleware dependency that contributed to CapWay's closure. This is infrastructure, not a feature — but it is the infrastructure decision that determines whether the company survives a banking partner disruption.

**4. Earned Wage Access (EWA) Integration.** On-demand access to earned but unpaid wages, delivered through the employer partnership. This is the highest-value feature for hourly workers and the primary reason workers adopt employer-sponsored financial tools, per DailyPay's growth trajectory.

**What We Will NOT Build:** A proprietary banking license, a consumer lending product, a credit card, a crypto wallet, or a standalone consumer app requiring paid user acquisition. These are capital-intensive additions that can follow scale — they are not MVP requirements.

## Success Metrics:

- 10 signed employer partnerships within 6 months of launch
- 5,000 active monthly users (defined as at least one transaction per month) within 12 months
- Average revenue per user exceeding $15/month (interchange + EWA fees combined) within 12 months
- Banking partner uptime SLA of 99.9%, with a documented backup partner relationship in place before launch

---

## Go-to-Market Strategy

**Target Customer Segment:** Hourly workers at mid-sized employers (50–500 employees) in retail, food service, logistics, and light manufacturing — specifically those operating in banking deserts or employing workforces with documented low rates of direct deposit adoption. This is narrow by design: it mirrors CapWay's original demographic insight while routing around the direct-to-consumer CAC problem that made the interchange model unworkable.

**Primary Distribution Channel:** B2B2C through employer HR and payroll partnerships. The tactical sequence: (1) target Gusto's 300,000+ small business customers via Gusto's partner marketplace, where a CapWay integration can be offered as a financial wellness benefit; (2) pursue direct outreach to regional employers in the Southeast — starting in Atlanta and Mississippi, where CapWay's founder had established relationships and brand recognition — using the CRA modernization as a sales hook for employers whose banking partners now have regulatory incentives to support financial inclusion programs.

**Pricing Strategy:** Free to employees; employers pay a per-seat monthly fee of $3–$8 per enrolled employee, benchmarked against the lower end of financial wellness platform pricing (data on exact competitor pricing is not available in the research report, but DailyPay's employer fee model is the reference). Interchange revenue from employee card spending is additive. This dual-revenue model — employer SaaS fee plus interchange — directly addresses the unit economics problem that made CapWay's interchange-only model insufficient for a low-income user base.

**Differentiation vs. 2026 Competitors:** The combination of employer-first distribution, AI coaching (not available in Chime or Current), and direct-BaaS infrastructure (eliminating Synapse-style risk) is not replicated by any current competitor. The CRA regulatory environment gives large bank partners a new reason to co-market with a CapWay successor that the original company never had access to. Capital strategy should prioritize CDFI funding, impact-focused funds (Fearless Fund, Harlem Capital), and CRA-motivated bank partnerships before approaching traditional venture — directly addressing the structural funding barrier Allen identified as CapWay's root cause of failure.
