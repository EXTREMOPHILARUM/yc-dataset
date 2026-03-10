# Build Plan: StrongIntro 2026

## Overview

The 2026 version is a fully async, AI-powered referral activation platform for Series A/B tech companies. It lives in Slack and your ATS—no sourcing parties, no dedicated recruiter. Employees spend 20 minutes reviewing their enriched network, flag warm connections, and the system generates personalized outreach on their behalf. You pay a platform fee plus 10% of first-year salary on hires that close.

The shift that makes this work now: LLMs can draft contextual outreach at scale, and APIs from Clay and Apollo have made network enrichment cheap and instant. The human bottleneck that killed StrongIntro is gone. You're competing against Gem's recruiter-centric model and Teamable's passive matching—both miss the insight that employees are your best sourcers if you remove friction from their workflow.

Distribution is built-in: Greenhouse and Ashby's integration marketplaces reach your exact customer. You're not selling recruiting; you're selling a referral multiplier that plugs into tools they already use. The unit economics work because you only pay when someone gets hired.33:T87e,

## Why Now?

## Current Market Analysis

## Market Size

The global recruitment software market was valued at approximately $3.1 billion in 2023 and is projected to reach $4.5 billion by 2028 (MarketsandMarkets; exact 2016 baseline unavailable for direct comparison). The employee referral software subcategory is smaller but growing; specific subcategory sizing data is not available in the research provided.

## Competitive Landscape

The 2026 competitive map has four meaningful clusters, each with exploitable weaknesses:

- **Gem** (Series C, ~$100M raised): Dominant in sourcing workflow for in-house recruiters, but built around recruiter-driven outreach, not employee network activation. Gem does not systematically parse employee second-degree connections. Weakness: ignores the referral channel entirely.

- **Greenhouse + Ashby** (ATS platforms): Excellent at managing candidates already in the funnel; weak at top-of-funnel referral generation. Their referral modules are passive—email reminders and bonus tracking—not active network mining. Weakness: referral features are afterthoughts, not core products.

- **Teamable** (StrongIntro's original direct competitor per Tracxn): Raised venture funding and survived, validating the market. However, Teamable's product remains largely a passive matching tool without AI-generated outreach or async facilitation. Weakness: pre-LLM architecture, no agentic workflow layer.

- **LinkedIn Recruiter**: Expensive ($10,000+/year per seat), requires recruiter expertise to operate, and surfaces cold candidates rather than warm second-degree connections. Weakness: high cost, no employee network activation.35:T986,

## Demand Signals

Clay's rapid growth to a reported $50M+ ARR (2024, per public reporting) demonstrates strong demand for programmatic contact enrichment. Rippling's HR platform growth signals that companies want integrated, automated people-operations workflows. The persistence of referral bonuses ($1,000–$5,000 per hire) at most tech companies confirms that demand for referral-channel improvement is real and budgeted—companies are already paying for outcomes, just inefficiently.

---

## Recommended MVP

## Core Features

## AI-Facilitated Async Sourcing Session

A structured 20-minute Slack or browser-based workflow that guides employees through reviewing their enriched second-degree network and flagging warm connections for open roles. Unlike StrongIntro's in-person sourcing party, this runs asynchronously—employees complete it on their own schedule, with no recruiter present. This eliminates the per-engagement labor cost that made the original model unscalable. The session is triggered by the hiring manager, not a StrongIntro employee.

## Automated Network Enrichment via API

Integration with Clay and Apollo.io APIs to automatically enrich employee connections with current job title, seniority level, company, and LinkedIn open-to-work status—without requiring employees to manually import contacts. This replaces StrongIntro's Chrome extension and email/Facebook import workflow, reducing employee friction from 15 minutes of manual setup to a single OAuth connection.

## LLM-Generated Personalized Outreach

Once a warm connection is flagged, GPT-4o (May 2024) drafts a personalized outreach message from the referring employee—referencing the specific connection context, the role, and a genuine personal note. The employee reviews and sends with one click. This replaces the dedicated recruiter's most time-intensive task and is the direct substitute for the human labor layer that defined StrongIntro's cost structure.

## ATS Integration (Greenhouse and Ashby only)

Bidirectional sync with Greenhouse and Ashby to push sourced candidates directly into the hiring pipeline and track conversion from referral to hire. This is the revenue-recognition trigger for the performance-fee model and the data layer needed to prove ROI to customers.

## What We Will NOT Build

No proprietary candidate database. No full ATS. No recruiter-facing sourcing tools (that is Gem's market). No enterprise compliance or HRIS integrations in v1. No mobile app.

## Success Metrics

- 10 paying customers within 90 days of launch
- Average of 40+ warm candidates surfaced per sourcing session (vs. StrongIntro's reported 50–100 with human facilitation; lower threshold reflects async format)
- At least 1 confirmed hire per 3 sessions run (conversion rate threshold)
- Net revenue retention >100% at 6 months (customers run repeat sessions)
- CAC payback period under 4 months

---

## Go-to-Market Strategy

## Target Customer Segment

Series A and Series B technology companies, 30–150 employees, actively hiring 3+ engineers simultaneously, using Greenhouse or Ashby as their ATS. This segment is narrow by design: they have large enough employee networks to generate meaningful candidate volume, they have budget authority without enterprise procurement cycles, and the ATS integration requirement pre-qualifies them as operationally mature buyers. Geographic focus is irrelevant given the async-first product—target English-speaking markets globally from day one.

## Primary Distribution Channel

The Greenhouse Partner Marketplace and Ashby's integration directory are the primary acquisition channels. Greenhouse has 12,000+ customers (2024); even 0.5% conversion represents 60 customers. Listing is free; the channel provides warm inbound from buyers already evaluating recruiting workflow tools. Secondary channel: direct outreach to YC-batch companies via the YC company directory—replicating StrongIntro's original distribution advantage but systematically, not relationally.

## Pricing Strategy

Retain the performance-fee model—10% of first-year base salary per hire—but add a $500/month platform fee per active role to cover infrastructure costs and create immediate cash flow. The platform fee solves StrongIntro's fatal unit economics problem: revenue begins at contract signing, not 4–6 months later at hire completion. The performance fee preserves the low-friction sales motion that generated StrongIntro's Demo Day customer list. Blended pricing is now validated by Hired's hybrid model (subscription + placement fee).

## Differentiation vs. 2026 Competitors

Against Teamable: fully async, LLM-powered outreach generation versus Teamable's passive matching. Against Gem: employee network activation versus recruiter-driven cold sourcing—complementary positioning, not direct competition. Against LinkedIn Recruiter: 10x lower cost, warm candidates only, no recruiter expertise required. The core differentiation is the same thesis StrongIntro had—referrals outperform cold sourcing—delivered through infrastructure that finally makes the unit economics work.
