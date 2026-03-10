# Build Plan: Nophin 2026

## Overview

The single most important change since Nophin's failure is the arrival of reliable, cheap long-document parsing via large language models — specifically GPT-4 (March 2023) and Claude 3.5 Sonnet (June 2024). This is not a general "AI got better" observation. It is a precise infrastructure unlock for the exact technical bottleneck that killed Cresa.

In 2022, parsing a 60-page offering memorandum or a broker-formatted rent roll required either fine-tuned NLP models trained on domain-specific CRE documents — expensive to build, brittle when document formats varied across brokers — or rule-based extraction logic that broke on any deviation from expected structure. Nophin hired a specialized ML engineer formerly at Kensho/S&P Global just to attempt this. The product was still unreliable. Today, GPT-4o with a structured output prompt and a PDF-to-text pipeline extracts cap rates, NOI, price per unit, occupancy, and debt service coverage from an OM in seconds, with accuracy sufficient for screening-level decisions. The marginal cost per document is fractions of a cent. The engineering time to build this pipeline is days, not months.

The second critical change is market conditions. The post-2022 CRE dislocation — rising interest rates, compressed debt availability, distressed multifamily assets coming to market from forced sellers — has simultaneously increased the volume of deals acquisition teams must screen and reduced the analyst headcount firms are willing to carry. According to MSCI Real Assets (data cited in industry press; specific 2025 figure not independently verified here), transaction volume in multifamily has begun recovering from 2023 lows, with more distressed and value-add deals entering the market. Acquisition teams that previously screened 20 deals per month to find one worth pursuing are now screening 40–60. The ROI case for automated screening — which Nophin struggled to prove in a low-volume 2022 environment — is now self-evident to buyers.

Third, the tooling ecosystem has matured. LangChain, LlamaIndex, and the OpenAI Assistants API (launched November 2023) provide off-the-shelf RAG infrastructure for document Q&A. Excel's Python integration (launched 2023) and the Google Sheets API make reliable model sync buildable in days. Time-to-MVP has compressed from months to weeks, meaning a two-person founding team can reach a testable product before burning meaningful capital.

Distribution channels that did not exist or were immature in 2022 now include the NMHC (National Multifamily Housing Council) digital community, LinkedIn Sales Navigator targeting CRE acquisition titles, and the GP/syndicator networks on platforms like Juniper Square and Covercy, which have established software-buying behavior among exactly the target customer.

---

## Why Now?

## Current Market Analysis

### Market Size

The U.S. multifamily CRE market is large in asset value — estimates of total investable multifamily stock exceed $4 trillion — but the relevant addressable market for a deal screening SaaS tool is the software budget of acquisition teams, not the asset base. The number of active multifamily acquisition teams in the U.S. is estimated in the low thousands (specific 2026 figure not independently verified; this is an inference from industry directories and NMHC membership data). At $500–$1,500 per seat per month, a 2,000-team market with 3 seats per team represents $36M–$108M in annual recurring revenue at full penetration — a real but not enormous TAM. Expansion to other CRE asset classes (industrial, office, retail) is the path to venture scale, and that expansion is now more tractable given LLM generalization across document formats.

## Competition Map and Gaps

The current competitive landscape has matured significantly since 2022:

- **Blooma** (raised ~$10M, focused on CRE loan origination screening for lenders, not acquisition teams) — serves a different buyer; acquisition teams are not its primary customer.
- **Dealpath** (deal management and pipeline tracking, not document intelligence) — strong on workflow management, weak on AI-native document parsing; acquisition teams use it after a deal passes screening, not during it.
- **Cherre** (property data aggregation, raised ~$50M) — data platform, not a screening workflow tool; requires significant integration effort and is priced for enterprise.
- **Leni** (AI for CRE document Q&A, early stage) — the most direct competitor; limited public information on traction or pricing as of early 2025.
- **CoStar / CBRE / JLL** — the platform absorption threat. CoStar has the data and distribution to add AI screening as a feature. This is the most serious structural risk and must be addressed directly.

## Defensibility Against Platform Incumbents

CoStar's structural weakness is that it is a data business, not a workflow business. Its incentive is to sell data subscriptions, not to build opinionated screening workflows that embed a firm's proprietary investment criteria. A rebuild of Cresa that stores and learns from each firm's specific underwriting criteria — cap rate floors, target markets, return thresholds, deal-killer flags — creates a proprietary data layer that CoStar cannot replicate without access to each firm's internal decision logic. This is the structural moat: not the document parsing (which CoStar could add), but the criteria memory and institutional knowledge layer that accumulates with each deal screened. That said, this moat is thin at early stage and requires deliberate product investment to build. If the rebuild does not prioritize criteria learning from day one, platform absorption remains a real risk.

## Demand Signals

Juniper Square (fund administration for GPs) and Covercy (GP/LP management) have both reported growth in their mid-market syndicator customer bases, signaling that the target buyer segment is actively adopting software. This is a meaningful demand signal for adjacent workflow tools.

---

## Recommended MVP

## Core Features

### OM Ingestion and Criteria Matching

The user uploads an offering memorandum (PDF) and defines their firm's investment criteria — minimum cap rate, target geography, price per unit range, minimum unit count, return thresholds. The product extracts key deal metrics from the OM using GPT-4o with structured output prompts and scores the deal against the firm's criteria, flagging pass/fail on each dimension within 60 seconds. This is the core value proposition Cresa promised but could not reliably deliver in 2022; it is now buildable in days with off-the-shelf LLM APIs. Unlike Cresa, the rebuild stores criteria persistently and learns which flags matter most to each firm over time.

## Rent Roll and T-12 Analysis

The user uploads a rent roll and trailing twelve-month income/expense statement. The product extracts occupancy by unit type, average in-place rent vs. market rent, expense ratios, and NOI, and surfaces anomalies — unusual vacancy concentrations, below-market leases, expense line items that deviate from market norms. This is the feature that required specialized NLP engineering in 2022; it is now a structured extraction prompt. The rebuild adds an anomaly-detection layer that flags items a junior analyst might miss, differentiating it from a simple document reader.

## Excel Model Sync

Extracted deal metrics populate a standardized Excel underwriting template via the Excel Python integration or a direct API push. The user's existing model is not replaced — data flows into it. This was a stated Cresa feature that likely had reliability issues in 2022 due to immature API tooling; the rebuild treats this as a non-negotiable reliability requirement, not a nice-to-have, and ships it only when it works on 95%+ of tested model formats.

## Deal Memory and Criteria Learning

Every deal screened is stored with its pass/fail outcome and the analyst's disposition (pursued, passed, reason). Over time, the product surfaces patterns — "you've passed on 12 deals in Phoenix with cap rates below 5.2%; your effective floor appears to be 5.5%" — and refines screening criteria automatically. This is the proprietary data layer that creates switching costs and differentiates the rebuild from a generic LLM document tool.

## What We Will NOT Build (MVP)

No market research automation, no investment memo generation, no CRM integration, no mobile app, no multi-asset-class support beyond multifamily. These are post-PMF features.

## Success Metrics

- 20 paying acquisition teams within 6 months of launch (proof of willingness to pay, not just usage)
- Average of 10+ deals screened per team per month (proof of workflow integration, not one-time use)
- 80%+ month-2 retention among paying customers
- Net Promoter Score ≥ 40 among active users

## Cold-Start Problem

This product does not depend on network effects or local density. Each team's value is derived from their own deal history and criteria. The product delivers value to a single user on day one — the first OM they upload produces a screening result immediately. There is no cold-start problem in the traditional sense; the challenge is sales, not density.

---

## Go-to-Market Strategy

### Target Customer Segment

The primary target is the acquisition analyst or associate (not the principal) at mid-market multifamily private equity firms and syndicators managing $50M–$500M in assets under management, with 2–8 person acquisition teams, actively screening 20+ deals per month. These firms are large enough to have a software budget and a real screening volume problem, but small enough that they lack the internal engineering resources to build their own tools. Firms above $500M AUM typically have custom-built or enterprise-contracted solutions; firms below $50M AUM often lack the deal volume to justify the subscription cost.

## Primary Distribution Channel

Direct outbound via LinkedIn Sales Navigator targeting "Acquisition Analyst," "Director of Acquisitions," and "VP Acquisitions" titles at multifamily-focused PE firms and syndicators. Secondary channel: partnerships with CRE brokers (CBRE, Marcus & Millichap, Newmark) who send OMs to acquisition teams daily and have a direct incentive to help buyers screen faster. A broker referral program — where brokers can send OMs directly through the platform to their buyer contacts — creates a distribution flywheel that Nophin never had.

## Pricing Strategy

$299 per seat per month, with a minimum of 2 seats per firm ($598/month floor). Annual commitment at $249/seat/month.

Stress test against free alternatives: acquisition analysts currently accomplish deal screening using a combination of manual Excel work, email, and their own judgment — not a paid software tool. The free alternative is 2 hours of analyst time per deal. At a fully-loaded analyst cost of $100K–$150K/year ($50–$75/hour), screening 30 deals per month costs $3,000–$4,500 in analyst time. A $299/month tool that reduces screening time by 50% pays for itself on the first deal of the month. The price is not competing against a free software alternative; it is competing against analyst labor cost, which makes the ROI case straightforward and the price defensible. The risk is not price sensitivity — it is trust: will analysts trust AI-extracted numbers on high-stakes investment decisions? The Excel sync feature (which lets analysts verify every extracted figure in their own model) is the trust mechanism, not a convenience feature.35:T7eb,

## Differentiation vs. 2026 Competitors

Against Leni and generic LLM document tools: the criteria memory and deal history layer creates switching costs that a generic document Q&A tool cannot replicate. Against Dealpath: the rebuild is a screening tool, not a pipeline management tool — it lives upstream of Dealpath in the workflow and can integrate with it rather than competing. Against CoStar: the rebuild is opinionated about each firm's specific investment criteria; CoStar is a data platform that cannot store or learn from a firm's internal decision logic without a dedicated product investment that is not in CoStar's core business model.
