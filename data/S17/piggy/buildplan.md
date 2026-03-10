# Build Plan: Piggy 2026

## Overview

Piggy 2026 is a wealth intelligence platform, not a distribution intermediary. It targets the 8M+ Indian professionals already investing in mutual funds through other platforms—people with ₹10–50L portfolios who lack a coherent financial strategy. The 2026 product connects all their financial accounts via Account Aggregator, shows them a unified net worth view, and surfaces tax optimization and goal-based rebalancing opportunities they're currently missing.

The market shift is Account Aggregator + UPI AutoPay, live since 2021. This infrastructure didn't exist when Piggy first launched. Now you can build a trust layer on top of aggregated data—not compete on distribution. Competitors like Groww own acquisition but are weak on engagement and advisory; they're distribution-first, not intelligence-first.

The go-to-market is subscription advisory: free net worth dashboard to acquire, then convert 15% to a ₹999/year SEBI RIA tier for personalized portfolio reviews and tax reports. You win by being the only platform that understands their full financial picture and acts as their annual financial operating system, not their fund store.34:T830,

## Why Now?

## Current Market Analysis

India's mutual fund industry AUM reached ₹67 lakh crore (~$800B USD) as of March 2025, per AMFI — more than 2.5x the ~$300B market Piggy entered in 2017. SIP monthly inflows crossed ₹26,000 crore (~$3.1B) in early 2025, up from roughly ₹4,000 crore in 2017. The addressable market has grown dramatically; the unsolved problem has shifted upstream from access to optimization.

## Current competitor map and specific weaknesses:

- **Groww** (est. 50M+ users, ~$3B valuation as of 2023): Dominant in acquisition but weak in post-onboarding engagement. Its advisory layer is thin — portfolio recommendations are generic, not goal-linked. Revenue depends heavily on equity trading commissions, creating the same conflict-of-interest Piggy was built to avoid.
- **Kuvera** (acquired by CAMS in 2023): Strong on tax optimization for sophisticated users, but UX remains dense and intimidating for the emerging affluent segment. Post-acquisition product velocity has slowed noticeably; no public feature releases of significance since mid-2024 (specific data unavailable).
- **Zerodha Coin**: Excellent for existing Zerodha brokerage users; poor standalone value proposition. No meaningful goal-based planning features. Locked to Zerodha's ecosystem.
- **INDmoney**: Broad multi-asset aggregation but monetizes through US stocks and insurance cross-sell, creating misaligned incentives. AA integration is present but advisory quality is low.
- **Fi / Jupiter**: Neobank-first, investment-second. Weak on mutual fund depth and SEBI RIA-grade advice.

**Gap:** No current competitor combines AA-powered true net worth aggregation, SEBI RIA-grade personalized advice, and goal-based planning at a sub-₹1,500/year price point accessible to India's 30–45M emerging affluent households. Demand signal: CRED Wealth's rapid growth within CRED's existing user base confirms willingness to pay for curated financial guidance among credit-verified, income-verified users.

---

## Recommended MVP

## Core Feature 1 — AA-Powered Net Worth Dashboard

Connects all financial accounts (mutual funds, EPF, bank savings, equities) via the Account Aggregator framework with user consent, displaying a unified real-time net worth view. This matters because it creates immediate, tangible value on day one without requiring any investment action — reducing the activation barrier that plagued Piggy's funnel. Unlike Piggy's manually built integrations, this uses the standardized AA API, meaning the entire integration surface is maintained by the AA ecosystem, not the startup's engineering team.

## Core Feature 2 — Goal-Based SIP Planner with LLM-Generated Rationale

Users define financial goals (home purchase, child education, retirement) with timelines and amounts; the system recommends a direct-plan mutual fund portfolio with AI-generated, SEBI-compliant rationale explaining each fund selection. SIPs are set up via UPI AutoPay in under 60 seconds. This differs from Piggy's original product, which presented funds as a catalog rather than as goal-linked instruments — a critical UX distinction for converting browsers into committed investors.

## Core Feature 3 — Annual Tax Optimization Report

At financial year-end, the system analyzes the user's portfolio for LTCG/STCG harvesting opportunities and ELSS utilization under Section 80C, generating a plain-language action plan. This is the feature Kuvera does best but presents in a format inaccessible to non-expert users. Delivered as a PDF and in-app walkthrough, it creates a concrete annual "save money" moment that justifies subscription renewal.

## Core Feature 4 — SEBI RIA Subscription Tier (₹999/year)

Unlocks personalized portfolio review, goal rebalancing alerts, and direct messaging with an AI-assisted advisor (human-reviewed for compliance). Priced at ₹999/year (~$12), below Kuvera's comparable tier and within the SEBI RIA fee cap. The LLM cost structure makes this margin-positive at scale in a way it was not for Piggy in 2020.

**What we will NOT build:** A neobank, debit card, US stocks product, insurance marketplace, or equity trading platform. No feature that requires a banking license or NBFC registration in year one.

## Success metrics:

- 10,000 AA-linked accounts within 90 days of launch
- 15% free-to-paid conversion within 6 months (industry benchmark for Indian fintech subscription tiers is 8–12%; 15% is achievable with goal-based framing)
- Monthly SIP volume of ₹5 crore ($600K) within 12 months
- Net Promoter Score ≥ 50 at 6 months

---

## Go-to-Market Strategy

**Target customer segment:** Urban Indian professionals aged 28–42, household income ₹15–50L/year (~$18K–$60K), already investing via SIPs but without a consolidated view of their finances or a structured goal plan. This is the demographic CRED has verified at scale — credit-active, digitally fluent, and demonstrably willing to pay for financial products. It is explicitly not Piggy's original first-time investor target; that segment is now served adequately by Groww. The emerging affluent segment has higher LTV, lower churn, and a genuine unmet need for optimization rather than access.

**Primary distribution channel:** CRED partner API program and Zerodha Rainmatter ecosystem. CRED's 12M+ users are pre-qualified by income and credit behavior — the highest-quality fintech distribution list in India that does not require building from scratch. Rainmatter has funded and distributed fintech tools to Zerodha's 10M+ brokerage users. Both channels offer access without paid acquisition costs in exchange for revenue share or equity. Secondary channel: LinkedIn organic content targeting the ₹15–50L income bracket, where financial anxiety content (tax deadlines, SIP adequacy calculators) drives high-intent inbound.

**Pricing strategy:** Freemium with a hard paywall at the tax optimization and personalized advisory features. Free tier includes AA dashboard and basic goal calculator — enough to demonstrate value. Paid tier at ₹999/year (~$12), justified by a single tax-saving action that typically saves users ₹5,000–₹50,000. The ROI framing ("this subscription pays for itself") is the conversion mechanism. Annual billing only, to maximize LTV and reduce churn.

**Differentiation vs. 2026 competitors:** Every major competitor monetizes through product cross-sell (insurance, US stocks, trading) that creates advisor conflict. The rebuild's differentiation is structural purity: SEBI RIA registration, flat fee, no commissions, no cross-sell. This is the original Piggy thesis — but now viable because LLMs make the advisory economics work at ₹999/year, and the AA framework makes aggregation a feature rather than an engineering project.
