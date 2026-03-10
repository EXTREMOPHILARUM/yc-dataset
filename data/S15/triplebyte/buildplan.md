# Build Plan: Triplebyte 2026

## Overview

By 2026, Triplebyte is a two-sided marketplace for senior engineers and early-stage startups, powered by an AI-conducted technical interview that replaces the old human screen bottleneck. Candidates who pass enter a curated, visible pool with verified skill profiles and transparent interview transcripts. Hiring teams get what they originally came for: pre-screened engineers with proven technical depth, not resume proxies.

The market shift is real: AI can now conduct adaptive coding interviews at scale without losing signal. The original Triplebyte thesis — that demonstrated skill beats credentials — was always right. What failed was the execution model, not the insight. By returning to outcome-aligned economics (25% placement fee, 90-day guarantee) and building a genuine two-sided network, the rebuild captures both sides of the value: engineers get fair assessment and visibility; companies get conversion rates that beat the industry standard by 75%.

Go-to-market is structural advantage reborn. The YC alumni network — 4,000+ active founders — is the distribution channel. Early placements into YC companies create proof points that compound. The differentiation is simple: everyone else is either a B2B vendor (Karat) or a job board (Wellfound). This is a marketplace where both sides have skin in the game.34:Ta78,

## Why Now?

The single most important change since Triplebyte's failure is this: the 15-minute phone screen and 45-minute technical interview that made FastTrack work — and made it unscalable — can now be conducted by AI at zero marginal cost per candidate.

Triplebyte's original unit economics were strangled by human interviewer time. Every candidate who passed the initial quiz required a trained Triplebyte interviewer to conduct two live sessions. That labor cost created a hard ceiling on throughput and made the high-touch model incompatible with venture-scale growth. The $35M Series B forced a choice between quality and volume; Triplebyte chose volume and died. That tradeoff no longer exists.

GPT-4 (March 2023) and Claude 3 Opus (March 2024) can now conduct open-ended, adaptive technical conversations — probing for reasoning, not just pattern-matching — at a quality level sufficient to replace Triplebyte's phone screen tier. More specifically, models fine-tuned on structured technical evaluation rubrics (a capability available via OpenAI's fine-tuning API since August 2023) can maintain consistent scoring criteria across millions of candidates simultaneously. The marginal cost of the 45-minute technical interview drops from ~$40–60 in interviewer time to effectively zero.

This resolves the core structural failure. A rebuilt Triplebyte can maintain FastTrack's quality bar — the thing clients actually paid for — while scaling candidate throughput to a level the original model could never reach.

Additional tailwinds are real and documented. LinkedIn's 2023 Future of Work report noted a 21% increase in job postings emphasizing skills over degrees. IBM, Google, and the US federal government have formally removed degree requirements for many roles. Triplebyte had to evangelize skills-based hiring; a 2026 rebuild does not.

The 2022–2023 tech layoff wave (150,000+ US tech workers laid off per Layoffs.fyi) created a structural surplus of experienced, senior engineers actively seeking new roles — precisely the candidate demographic Triplebyte's Screen strategy failed to attract during the 2021 hiring boom. Supply-side conditions have inverted.

Distribution channels unavailable to the original Triplebyte now exist at scale: the Wellfound (AngelList) startup network with 8M+ registered candidates, the Shopify App Store with 2M+ merchants (relevant for commerce-focused engineering roles), and LinkedIn's API partnerships for verified credential overlays. Otherbranch's 2024 founding by ex-Triplebyte employees — people with direct institutional knowledge of what worked — further validates that the thesis survives the company.

---

## Current Market Analysis

**Market Size:** US companies spend an estimated $150 billion annually on recruiting across all functions, per the original research. The technical recruiting subset commands premium fees (15–25% of first-year salary) due to engineering talent scarcity. Specific 2026 market size data for technical recruiting as a standalone category is not available in the research provided; the $150B figure is the best available anchor. The AI-augmented hiring tools market is growing rapidly — exact figures are not available in the research — but the structural demand for better technical screening has only increased as engineering compensation has risen and mis-hires have become more expensive.

## Competition Map:

- **Karat** (acquired Triplebyte's assessment IP): Offers human-in-the-loop technical interviews as a service. Specific weakness: still relies on human interviewers, keeping marginal cost high and throughput limited. Does not operate a two-sided candidate marketplace; it is a B2B screening vendor only.

- **HackerRank / Codility**: B2B coding test platforms sold to HR teams. Specific weakness: assessments are administered to a company's own inbound applicants, not a curated external candidate pool. No marketplace dynamic; no candidate-side value proposition.

- **Wellfound (AngelList Talent)**: Strong startup brand, free job marketplace. Specific weakness: no proprietary screening layer. Candidate quality is unverified; employers still run their own full interview loops.

- **LinkedIn**: Dominant passive sourcing tool. Specific weakness: general-purpose professional network with minimal technical screening capability. Skills assessments are self-reported and unproctored.

- **Otherbranch** (2024, ex-Triplebyte): Direct ideological successor. Specific weakness: early-stage, limited public traction data available; likely facing the same candidate acquisition challenge without AI-native architecture.

**The gap no current competitor fills:** A two-sided marketplace combining AI-conducted technical screening (replacing human interviewers), a curated senior-engineer candidate pool, and outcome-aligned pricing. Karat has the assessment IP but no marketplace. Wellfound has the marketplace but no screening. HackerRank has screening but no candidate supply. The original Triplebyte combination — rebuilt on AI infrastructure — remains unoccupied.

**Demand signals from adjacent products:** Greenhouse and Lever (ATS platforms) have both added AI screening integrations, signaling that hiring teams are actively adopting AI-assisted evaluation. This reduces enterprise change-management friction for a new entrant.

---

## Recommended MVP

## Core Features:

### AI Technical Interview Engine

An asynchronous, AI-conducted technical interview replacing Triplebyte's original two-stage human screen. Candidates complete an adaptive coding assessment followed by a 30-minute conversational AI interview — conducted via text or voice — that probes reasoning, debugging approach, and system design thinking. This differs from the original by eliminating human interviewer scheduling and cost entirely, enabling same-day candidate processing at any volume. It differs from HackerRank by assessing reasoning process, not just output correctness.

## Curated Senior-Engineer Candidate Pool with Verified Skill Profiles

Only engineers who pass the AI interview are admitted to the visible candidate pool. Profiles display skill percentiles, interview transcript summaries, and role-fit tags — no resume required at intake. This directly replicates FastTrack's quality moat. The critical operational rule: the pool stays closed to unscreened candidates regardless of growth pressure. This is the anti-pattern Triplebyte violated with Source and Screen.

## Outcome-Aligned Placement Fee Model

Return to Triplebyte's original 25% first-year salary placement fee with a 90-day guarantee, replacing the subscription model that decoupled revenue from hiring outcomes. This re-establishes incentive alignment with clients and makes the value proposition credible to skeptical buyers burned by Triplebyte's later pivots. Subscription pricing is explicitly deferred until placement volume justifies it.

## Transparent Privacy Architecture

Candidate profiles are private by default, permanently. Candidates explicitly opt in to visibility for each company category (e.g., "Series A–B startups," "enterprise," "fintech"). No profile is ever made public without affirmative, per-instance consent. This is a direct architectural response to the two privacy violations that destroyed Triplebyte's community trust — built into the data model, not enforced by policy alone.

## What We Will NOT Build:

- Free B2B screening tools (the Screen anti-pattern)
- Automated outreach/sourcing bots (the Magnet anti-pattern)
- A public candidate database accessible without placement-fee commitment
- Any international candidate pool until US senior-engineer supply is validated against client demand

## Success Metrics with Concrete Thresholds:

- On-site-to-hire conversion rate ≥ 35% (vs. 20% industry standard) within 6 months of first 10 client placements
- Candidate pool: 500 screened, admitted engineers before opening to paying clients
- Client retention: ≥ 70% of clients make a second placement within 12 months
- Zero privacy incidents (binary threshold; one incident triggers full architectural review before resuming operations)

---

## Go-to-Market Strategy

### Target Customer Segment:

Series A and Series B US-based technology startups with 10–100 employees, actively hiring for their first 5–15 engineering roles. This is the exact segment Triplebyte served successfully in 2015–2018 before expanding to enterprise. These companies have the highest pain-per-mis-hire ratio, the least internal recruiting infrastructure, and the strongest cultural alignment with skills-over-credentials hiring. They are also the most likely to accept a placement-fee model because they lack the procurement bureaucracy that makes enterprise sales slow.

## Primary Distribution Channel + Tactics:

The YC alumni network is the highest-leverage starting point — the same structural advantage Triplebyte used in 2015. In 2026, there are 4,000+ active YC alumni companies. Direct outreach to YC batch companies (W25, S25, W26) through the YC Bookface internal network, combined with a formal YC partnership or preferred-vendor status if achievable, replicates the original captive market. Secondary channel: Wellfound's startup network for job posting integration, surfacing pre-screened candidates to companies already posting roles there.

## Pricing Strategy:

25% of first-year salary per placement, with a 90-day replacement guarantee. At a median senior engineer salary of $180,000 (US, 2025 — exact 2026 figure unavailable), this yields ~$45,000 per placement. Ten placements per month generates $450,000 MRR equivalent — sufficient for profitability at a lean team size, replicating Triplebyte's 2015 profitable-at-small-scale model intentionally. This is a bootstrappable business before it is a venture business. Raise only if the placement-fee model is demonstrably working and the growth constraint is capital, not product-market fit.

## Differentiation vs. 2026 Competitors:

Against Karat: two-sided marketplace with candidate-side value proposition, not just a B2B vendor. Against Wellfound: verified, AI-screened candidate quality with outcome-aligned pricing. Against HackerRank/Codility: candidates come pre-screened to employers; companies don't administer tests to their own inbound pipeline. Against Otherbranch: AI-native interview infrastructure eliminates the unit economics problem that constrained the original model. The single non-negotiable differentiator is the closed, quality-gated candidate pool — the one thing every competitor has either abandoned or never built.
