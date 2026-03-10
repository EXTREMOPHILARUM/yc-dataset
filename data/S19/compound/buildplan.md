# Build Plan: Compound 2026

## Overview

By 2026, Compound is a software-first financial planning platform for tech employees with complex equity compensation—not a traditional wealth management firm. It serves mid-career engineers and product managers at growth-stage startups and recently public tech companies who need clarity on their equity decisions without paying six-figure minimums or waiting weeks for advisor callbacks.

The rebuild works because large language models now make it economically viable to automate the hardest part of the original business: parsing messy equity documents and extracting actionable financial data. A free tier with LLM-powered document ingestion and scenario modeling drives acquisition; a $49/month Pro tier adds tax estimation and real-time modeling; an optional advisor layer ($200–500/month) connects users to CFPs asynchronously. This inverts the unit economics—software scales, advisors become a high-margin add-on, not the core cost center.

The go-to-market is direct: target the 50,000+ employees at Series B–D startups and recent IPOs through community channels, Slack communities, and founder networks. Win by being 10x faster and 100x cheaper than Compound Planning's high-touch model, while remaining credible enough for six-figure equity packages. The path to venture scale is recurring SaaS revenue, not AUM.34:T7ef,

## Why Now?

The single most important change since Compound's failure is the emergence of large language models capable of parsing complex financial documents at scale. GPT-4 (March 2023) and Claude 3 Opus (March 2024) can now extract structured data from cap tables, option grant agreements, 83(b) election forms, and RSU schedules with high accuracy — eliminating the manual tracking labor that made Compound's illiquid asset aggregation expensive and structurally unscalable. In 2022, Compound employed roughly one staff member per 18 clients. LLM-powered document parsing could collapse that ratio by an order of magnitude, converting the company's most expensive operational burden into a software problem.

The second critical change is the maturation of RIA infrastructure-as-a-service. Platforms like Altruist, Orion, and RIA-in-a-Box now allow a new firm to register as a Registered Investment Advisor and launch with compliant portfolio management, billing, and reporting infrastructure in weeks, not the months or years Compound spent building this from scratch. This removes the primary justification for Compound's three-year stealth period.

The third change is macro: the 2022–2023 tech downturn that compressed Compound's catalyst-event pipeline has passed. IPO filings are recovering (Renaissance Capital reported 2024 U.S. IPO proceeds up approximately 50% year-over-year — specific 2025–2026 data unavailable at time of writing). More importantly, a new cohort of tech employees is accumulating equity in AI-era private companies — Anthropic, OpenAI, xAI, Perplexity, and others — recreating exactly the illiquid-equity complexity Compound was built to address, with a larger and wealthier underlying population than the 2019 cohort.

Distribution has also matured. LinkedIn's creator tools, Substack, and X/Twitter now provide direct, low-cost access to the exact audience Compound reached through a single essay in 2019 — but with persistent, compounding audience ownership rather than a one-time spike.

---

## Current Market Analysis

The U.S. RIA market managed approximately $128 trillion in assets as of 2023 (Investment Adviser Association, 2023 Evolution Revolution report). Compound's actual addressable market — tech employees with illiquid equity complexity — is a fraction of this, but it is a meaningfully larger fraction in 2026 than in 2019. The AI startup boom has created a new generation of employees holding options in companies valued at tens of billions of dollars privately, before any liquidity event. The population of people holding pre-IPO equity in companies valued above $1 billion (so-called "unicorn employees") has grown substantially since 2019, though precise current headcount data is not publicly available.

## Competition map:

- **Compound Planning** (the merged successor): $4B+ AUM, 30+ advisors, growing rapidly. Its weakness is that it remains a high-touch, high-minimum service — not meaningfully more accessible than a traditional RIA for employees earlier in their equity lifecycle.
- **Harness Wealth**: Marketplace model connecting clients to CPAs and RIAs. Weakness: referral-layer friction, no integrated software experience, no proprietary advisory relationship.
- **Equity FTC / Keystone Global Partners**: Boutique RIAs serving tech employees. Weakness: no technology differentiation, limited scalability, geographically concentrated.
- **Carta** (equity management): Deep on cap table administration for companies, not employees. Weakness: no financial planning layer, no tax integration, no investment management.
- **Wealthfront / Betterment**: Robo-advisors with no illiquid asset handling, no equity compensation modeling, no human advisory layer for complex decisions.

The gap in the market is clear: no current competitor combines automated illiquid asset aggregation, LLM-powered equity scenario modeling, and human advisory access at a price point accessible to mid-career tech employees (not just executives with $1M+ in liquid assets).

Demand signal from adjacent products: Blind and Levels.fyi — anonymous compensation discussion platforms — consistently surface equity compensation confusion as a top concern among tech employees, indicating persistent, unmet demand for accessible expert guidance.

---

## Recommended MVP

### Core Feature 1: LLM-Powered Equity Document Ingestion

Users upload option grant agreements, RSU schedules, cap table summaries, and offer letters; the system extracts structured data (strike price, vesting schedule, expiration dates, exercise windows, share class) and populates a unified equity dashboard automatically. This matters because manual data entry was Compound's primary operational bottleneck and the reason its advisor-to-client ratio was unsustainable. Unlike the original, this is a software-first workflow requiring no human labor for standard document types.

## Core Feature 2: Scenario Modeling Engine

An interactive calculator that models the financial outcomes of key equity decisions — early exercise vs. waiting, NSO vs. ISO tax treatment, cashless exercise at IPO, secondary sale — under user-defined assumptions about exit valuation and timing. This matters because option exercise decisions are the highest-stakes, most time-sensitive moments in a tech employee's financial life, and getting them wrong is irreversible. Unlike the original Compound, this feature is self-serve and available before a client pays for advisory services, functioning as both a product and a top-of-funnel acquisition tool.

## Core Feature 3: Integrated Tax Estimation

Real-time AMT exposure calculation, QSBS eligibility flagging, and state tax impact modeling tied directly to the scenario modeling engine. This replaces Compound's in-house tax firm — a fixed-cost operational burden — with a software layer built on top of existing tax calculation APIs (e.g., TaxJar, Avalara, or custom models). Human CPA review is available on-demand at variable cost through a vetted partner network rather than full-time staff.

## Core Feature 4: Advisor Access on Demand

Asynchronous messaging and scheduled video consultations with a small team of CFPs, available as an add-on tier rather than bundled into every plan. This preserves the human advisory layer that differentiated Compound from pure software tools, while making it a variable cost that scales with revenue rather than a fixed headcount commitment.

## What we will NOT build (MVP):

- In-house tax filing or CPA employment
- Investment management or AUM-based portfolio management
- Cryptocurrency portfolio tracking (defer to Phase 2)
- Mobile app (web-first)

## Success metrics:

- 500 paying subscribers within 6 months of launch
- Advisor-to-client ratio of 1:100 or better at month 6
- Net Revenue Retention > 110% at 12 months
- Document ingestion accuracy ≥ 95% on standard grant agreement formats (measured by QA sampling)

---

## Go-to-Market Strategy

**Target customer segment:** Mid-career software engineers and product managers at Series B–D startups and recently public tech companies, holding between $100K and $2M in unvested or recently vested equity, who have never worked with a financial advisor and are facing their first major equity decision within the next 12 months. This is narrower than Compound's original target (which included founders, executives, and crypto investors) and deliberately excludes the highest-complexity, highest-cost-to-serve clients until the advisory model is proven at scale.

**Primary distribution channel:** Content-driven organic acquisition on LinkedIn and Substack, replicating and systematizing the essay-driven playbook that generated Compound's original 1,300+ consultations. The rebuilt company publishes a weekly Substack on equity compensation decisions — option exercise timing, AMT traps, QSBS eligibility, secondary markets — targeting the exact search and social queries that tech employees generate when facing catalyst events. Each piece of content links to the free scenario modeling tool, converting readers into registered users before any sales conversation occurs. LinkedIn is the primary amplification channel because equity compensation discussions are already endemic there among the target demographic.37:T4ad,- **Free tier:** Equity document upload + basic scenario modeling (acquisition and activation)
- **Pro tier:** $49/month — full scenario modeling, tax estimation, AMT alerts, document vault
- **Advisory tier:** $299/month — Pro features plus async advisor messaging and one video consultation per quarter

Pricing is anchored significantly below Compound's reported ~$2,000/month representative price point, targeting the mid-career employee who cannot justify or access traditional RIA minimums. The free-to-Pro conversion funnel is the primary growth mechanism; the Advisory tier captures clients approaching high-stakes decisions.

**Differentiation vs. 2026 competitors:** Compound Planning serves clients with existing liquid wealth; this rebuild serves employees *before* liquidity, when decisions matter most and no competitor is present. Harness Wealth charges for referrals; this product charges for software. Carta serves companies; this serves employees. The rebuilt Compound owns the pre-liquidity moment — the highest-anxiety, highest-value point in a tech employee's financial life — and builds the advisory relationship that persists through every subsequent catalyst event.38:T8fb,

## Pricing strategy:

# Velo

## 1. Overview

Velo is a self-serve wealth intelligence platform for tech employees navigating complex equity compensation — stock options, RSUs, and pre-IPO grants. A modern revival of Compound (YC S19), Velo replaces the manual advisory bottleneck with LLM-powered document ingestion, interactive scenario modeling, and on-demand CFP access, serving mid-career engineers and PMs at the exact moment equity decisions matter most. The core value proposition: upload your grant documents, model every exercise scenario with real tax implications, and get a CFP on a video call — all before your options expire.

---

## 2. Core Features

**Equity Document Ingestion**
- Upload option grant agreements, RSU schedules, offer letters, and cap table summaries (PDF, PNG, JPEG)
- LLM extracts: strike price, grant date, vesting schedule (cliff + monthly), expiration date, share class (ISO/NSO/RSU), exercise window post-termination
- Structured equity dashboard auto-populated from extracted data
- Manual override for any extracted field with audit trail
- Document vault storing all uploaded files with extraction status

**Scenario Modeling Engine**
- Interactive calculator for: early exercise vs. wait, ISO vs. NSO tax treatment, cashless exercise at IPO, secondary sale
- User-defined inputs: assumed exit valuation, exit timing (1–10 years), current FMV, personal income
- Side-by-side comparison of up to 3 scenarios
- Output: net proceeds after federal + state tax, AMT exposure, effective tax rate per scenario
- Shareable scenario links (read-only, expiring 7 days)

**Integrated Tax Estimation**
- Real-time AMT exposure calculation tied to scenario inputs
- QSBS eligibility flagging (Section 1202 — 5-year hold, C-corp, $50M asset threshold)
- State tax impact modeling for CA, NY, WA, TX, MA, and all other US states
- ISO spread bargain element calculation at exercise
- 83(b) election deadline alerts (30-day window from exercise)

**Advisor Access (Advisory Tier)**
- Async messaging thread with assigned CFP, 48-hour response SLA
- Scheduled 30-minute video consultations via embedded calendar (one per quarter on base Advisory plan)
- Shared scenario workspace: advisor can annotate and comment on client scenarios
- Advisor notes visible to client in their dashboard
