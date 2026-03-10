# Build Plan: Answerly 2026

## Overview

By 2026, Answerly is a lightweight question-intelligence layer for B2B SaaS companies managing social presence across multiple platforms. It ingests public posts from X, LinkedIn, Reddit, and Bluesky, uses modern LLMs to identify genuine customer questions with commercial intent, and surfaces them in a daily digest ranked by engagement potential. The product is built for lean sales and marketing teams (2–10 people) at mid-market SaaS firms who need to find and respond to high-value customer conversations without manual triage.

The core insight: LLMs have solved the hard problem that killed the original InboxQ—reliable question detection. What was brittle and hand-tuned in 2013 is now commodity. Meanwhile, the social graph has fragmented. No single platform dominates anymore, and customers are scattered across X, LinkedIn, Reddit, and emerging networks. A unified question inbox across all of them is genuinely valuable again.

The go-to-market angle is direct: land with a free tier that surfaces 5–10 questions daily, charge when teams want historical search, team collaboration, or response drafting. Avoid the freemium trap by making the paid tier solve a real workflow problem—not just removing artificial limits. Win by being 10x cheaper and faster than Sprout Social or Hootsuite for this specific use case.33:T863,

## Why Now?

## Current Market Analysis

**Market size:** The social media management software market was estimated at $23.4B globally in 2023 and is projected to reach $41.6B by 2028 (source: MarketsandMarkets, 2023). This compares to a market that was a few hundred million dollars annually when InboxQ operated in 2011–2013. The relevant sub-segment—social customer care and engagement tools—is not broken out separately in public data; exact sizing is unknown.

**The SMB gap:** Sprout Social's entry-level plan starts at $249/month per seat (as of 2024). Sprinklr's enterprise contracts run $100,000+/year. Hootsuite's professional tier starts at $99/month but offers no AI-powered question detection. This pricing architecture leaves a clear gap: SMBs and growth-stage companies (10–500 employees) with active social presences who need more than keyword monitoring but cannot justify enterprise contracts.

## Current competitor weaknesses:

- **Sprout Social** — Excellent analytics and scheduling; question-intent detection is not a feature. Overkill and overpriced for SMBs.
- **Hootsuite** — Broad platform coverage; no semantic matching, no question classification. Commoditized.
- **Brand24** — Strong mention monitoring; no question-intent filtering, no AI-driven response suggestions. Primarily a listening tool, not an engagement tool.
- **Mention** — Similar to Brand24; monitoring-first, engagement-second. No LLM layer.
- **Recently launched competitors:** No known product as of early 2025 specifically combines multi-platform question detection with LLM-powered semantic matching for SMB social engagement. This gap should be validated before building.

**Demand signals:** Clay's growth to $30M+ ARR (reported by multiple outlets in 2024, exact figure unconfirmed) on a signal-surfacing model validates willingness to pay. Reddit's AMA culture, LinkedIn's "ask me anything" posts, and Bluesky's growing question threads all demonstrate that question-intent content has migrated well beyond Twitter/X.

---35:T894,

## Recommended MVP

## Core Feature 1: Multi-Platform Question Ingestion

Ingest public posts from LinkedIn, Reddit, Bluesky, and X (Twitter) simultaneously using each platform's available API tier. This directly addresses InboxQ's fatal single-platform dependency—Twitter's 2012–2013 API restrictions likely contributed to its closure. The MVP should use X's Basic API ($100/month), Reddit's Data API (pricing varies; exact current tier costs should be confirmed before building), LinkedIn's Marketing API (requires partner approval), and Bluesky's open AT Protocol. No single platform shutdown kills the product.

## Core Feature 2: LLM-Powered Semantic Question Classification

Use GPT-4o (May 2024) or Claude 3.5 Sonnet (June 2024) to classify each ingested post for: (a) genuine question intent, (b) commercial relevance to the customer's product or service description, and (c) urgency/recency. The customer inputs a plain-English description of their product—"we sell project management software for construction teams"—and the model matches against it semantically. This eliminates InboxQ's keyword-expansion workaround entirely and should push actionable question yield well above the ~1% ceiling InboxQ achieved, though exact improvement rates should be measured in beta.

## Core Feature 3: Suggested Response Drafts

For each surfaced question, generate a draft response using the customer's product context, tone guidelines, and any uploaded documentation (FAQs, product pages). The human approves or edits before posting. This is not autonomous posting—human review is required. This differs from InboxQ, which offered no response assistance, only question discovery.

## Core Feature 4: Daily Digest with Engagement Scoring

Deliver a daily email or Slack digest ranking the day's top 5–10 questions by estimated engagement value (question specificity, asker follower count, thread activity). This creates a daily-use habit that InboxQ's raw stream never achieved—the digest is valuable even on days when a user doesn't log in.

**What we will NOT build:** Scheduling, publishing, analytics dashboards, sentiment analysis, competitor monitoring, or any feature that competes with Sprout Social or Hootsuite on their home turf. No mobile app in year one.

**Success metrics:** 100 paying customers within 6 months of launch; average revenue per user ≥ $150/month; weekly active usage rate ≥ 60% among paying customers; churn ≤ 5% monthly.

---

## Go-to-Market Strategy
