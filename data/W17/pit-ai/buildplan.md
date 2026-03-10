# Build Plan: Pit.AI 2026

## Overview

Pit.AI 2026 is a B2B SaaS platform for quantitative hedge funds and systematic traders—not a hedge fund itself. The product: an RL-based strategy discovery engine that surfaces tradeable patterns directly from market data, paired with an LLM layer that extracts alpha signals from SEC filings and earnings calls. Users backtest, validate, and deploy to live paper trading in one workflow. The target is sub-$500M AUM quant funds and tech-forward family offices that have capital but lack the in-house ML infrastructure to compete with larger players.

The timing works now because the foundational ML stack is open-source and cheap (FinRL, RLlib, Claude API), eliminating the five-year research tax that killed the original. Financial data APIs are commoditized. And the market has bifurcated: mega-funds have internal AI teams; everyone else is underserved and willing to pay for outsourced strategy discovery.

Go-to-market is direct sales to quant portfolio managers at regional systematic funds—people who remember the original Pit.AI thesis and understand the problem. Land with a free backtesting audit, prove edge detection works on their historical data, then move to SaaS pricing ($5K–$15K MRR per customer). The win is speed to alpha: what took a human quant six months now takes the engine34:T840,

## Why Now?

## Current Market Analysis

**Market size:** The global hedge fund industry managed approximately $4.3 trillion in AUM as of 2024 (Preqin), up from $3.2 trillion in 2017. More relevant to a rebuild, the quantitative and systematic strategies segment has grown disproportionately — exact current share data is not publicly available, but Preqin reported quant strategies represented roughly 30% of new fund launches in 2023. The family office market, a more accessible LP segment, now manages an estimated $6 trillion globally (UBS Global Family Office Report 2024), with technology-forward offices actively allocating to algorithmic strategies.

**The B2B software opportunity is better-sized for a startup.** The financial analytics and trading software market was valued at approximately $11.6 billion in 2023 (MarketsandMarkets; exact 2026 projection unavailable), growing at a reported CAGR of ~11%. This is the market a rebuilt Pit.AI should target first.

## Competition map:

- **Kensho (S&P Global):** Acquired for $550M in 2018; now embedded inside S&P's enterprise stack. Weakness: inaccessible to sub-$1B AUM funds; no self-serve offering.
- **Alpaca:** Provides brokerage API and market data infrastructure. Weakness: execution-layer only; no strategy generation or portfolio optimization layer.
- **Numerai:** Crowdsourced model tournament; pays contributors in NMR token. Weakness: black-box ensemble structure gives no transparency to allocators; not a tool funds can deploy internally.
- **Composer (acquired by Betterment, 2023):** No-code automated trading for retail. Weakness: retail-only; no institutional-grade risk controls or alternative data integration.
- **QuantConnect:** Open-source backtesting and live trading platform. Weakness: requires deep coding expertise; no AI-native hypothesis generation; no LLM signal layer.

**The gap:** No current product combines RL-based strategy generation, LLM-powered signal extraction, and a self-serve SaaS delivery model targeting sub-$500M AUM quantitative funds and sophisticated family offices. That is the white space.

**Demand signal:** Alpaca's 500,000+ developer accounts and QuantConnect's 200,000+ registered users (per their public documentation) confirm that a large, technically sophisticated audience is actively building algorithmic strategies and would pay for a superior AI-native layer on top of execution infrastructure.

---

## Recommended MVP

**The core pivot from the original:** Do not operate as a hedge fund. Sell the AI-Quant engine as a B2B SaaS tool to existing quantitative funds and family offices. This eliminates the LP fundraising gauntlet, the compliance infrastructure burden, and the track-record chicken-and-egg problem that killed the original company.

## Feature 1 — Automated Strategy Discovery Engine

An RL-based pipeline (built on FinRL and RLlib) that ingests market data via Polygon.io or Databento and surfaces candidate trading strategies optimized for Sharpe ratio and maximum drawdown — without requiring a human analyst to propose a hypothesis first. This is the original Pit.AI core thesis, now buildable in months rather than years. Unlike QuantConnect, which requires users to write strategies manually, this engine generates them autonomously.

## Feature 2 — LLM Signal Extraction Layer

A structured pipeline using GPT-4 or Claude 3.5 Sonnet to parse SEC filings, earnings call transcripts, and macroeconomic releases into quantitative signals that feed the RL optimizer. This directly addresses the signal-to-noise problem the founder cited in 2020 — adding a fundamental data layer that pure price-action RL cannot access. No current self-serve competitor combines LLM signal generation with RL portfolio optimization.

## Feature 3 — Backtesting and Walk-Forward Validation Dashboard

A transparent, auditable backtesting environment with walk-forward validation, regime detection, and overfitting diagnostics. This is the credibility layer that institutional users require before deploying any strategy. Unlike Numerai's black-box ensemble, every strategy is fully inspectable.

## Feature 4 — Alpaca / Interactive Brokers Paper Trading Integration

One-click deployment to paper trading accounts via Alpaca's API, enabling users to build a live (simulated) track record before committing capital. This solves the track-record bootstrapping problem that destroyed the original company.

**What we will NOT build:** A fund. No LP relationships, no SEC fund registration, no AUM management, no carry structure — at least in the first 18 months.

## Success metrics:

- 50 paying B2B customers within 12 months of launch
- $15,000 MRR within 12 months
- At least 3 customers deploying strategies to live (real-money) accounts via integrated brokers within 18 months

---

## Go-to-Market Strategy

**Target customer (narrow):** Quantitative analysts and portfolio managers at sub-$500M AUM systematic hedge funds and technology-forward single-family offices who currently use QuantConnect or build internal Python pipelines — and who have the technical sophistication to evaluate RL-generated strategies but lack the engineering bandwidth to build the AI layer themselves. This segment is large enough to reach $1M ARR but narrow enough to message precisely.

**Primary distribution channel:** Developer-led, bottoms-up adoption through the Alpaca developer community (500,000+ accounts) and QuantConnect's user base (200,000+ registered users). Tactics: publish open-source strategy benchmarks on GitHub comparing RL-generated strategies against manual baselines; write technical content on Substack and Towards Data Science targeting quant practitioners; sponsor or present at QuantCon and similar practitioner conferences. The goal is to become the tool that quant developers recommend to each other before any enterprise sales motion begins.

**Secondary channel:** Direct outreach to family office technology committees via LinkedIn and the Tiger 21 / TIGER 21 network (exact membership data not publicly available, but the network is documented as serving ultra-high-net-worth individuals managing pooled capital).

**Pricing:** Three tiers.
- *Research* ($299/month): Strategy discovery engine + backtesting dashboard; data via user's own API keys. Targets individual quant practitioners.
- *Professional* ($1,499/month): Adds LLM signal layer, walk-forward validation, and paper trading integration. Targets small funds and family offices.
- *Institutional* ($5,000+/month, custom): White-label deployment, dedicated data feeds, SLA. Targets funds requiring audit trails and compliance documentation.

Justification: QuantConnect's institutional tier is priced at $600–$2,000/month for execution infrastructure alone; the AI-native strategy generation layer commands a meaningful premium. Pricing is anchored below Kensho's enterprise-only model to remain accessible to the sub-$500M AUM segment that incumbents ignore.

**Differentiation in 2026:** The rebuilt Pit.AI is the only self-serve platform combining assumption-free RL strategy generation with LLM-powered fundamental signal extraction, at a price point accessible to sub-institutional funds. Numerai requires contributing to a tournament rather than owning your strategies. QuantConnect requires writing strategies manually. Kensho is inaccessible below enterprise scale. The rebuilt product owns the gap between developer tools and enterprise platforms — exactly where the 2026 quant practitioner market is underserved.
