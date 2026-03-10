# Build Plan: Souffle Club 2026

## Overview

Souffle Club was a San Francisco-based professional networking startup (YC S19) that attempted to build a "10x better LinkedIn alternative" anchored in richer profiles, then pivoted to TrustedFor — an invite-only Silicon Valley recommendation community — before quietly winding down in December 2021 after raising only $150K and failing to reach the network density required to deliver value.

The rebuild thesis is not another LinkedIn challenger. It is a vertical trust graph: a paid, globally accessible professional community for a single high-value cohort — ML engineers — where peer reputation is structured, LLM-synthesized, and cryptographically verified, making the product valuable to a member of one and defensible at a few thousand. Think "Bloomberg Terminal for professional reputation" in a vertical where credentials are already contested and hiring signal is broken.

---

## Why Now?

The single most important change since TrustedFor's failure is the arrival of LLMs capable of synthesizing qualitative peer input into structured, comparable reputation signals — something that was technically impossible in 2019 and that directly solves the product's core scaling problem.

TrustedFor's manual curation model required human moderators to evaluate every recommendation, which is why it could never escape Silicon Valley. GPT-4 (March 2023) and Claude 3 Opus (March 2024) can now ingest dozens of structured peer responses — "Describe a specific situation where this person solved a problem you couldn't" — and synthesize them into a calibrated competency profile that is both human-readable and machine-queryable. This transforms curation from a headcount problem into a compute problem, and compute scales.

On the verification side, the infrastructure that didn't exist in 2019 now does. Persona (identity verification, API-available since 2020), Certn (background and employment verification, API-available), and GitHub's public contribution graph provide a layered verification stack that can confirm work history, identity, and demonstrated output without requiring a human reviewer. LinkedIn Skills Assessments launched in 2019 but remain low-signal — a 15-question multiple choice quiz is not a competency proof. The gap between what LinkedIn offers and what a serious technical hiring manager needs has widened, not closed.

On distribution: Maven launched its cohort-based course platform in 2020 and now hosts thousands of ML and AI practitioners. Luma has become the default event infrastructure for technical communities. The ML Engineer cohort — the proposed target vertical — is globally distributed, highly online, and already self-organizes in Discord servers, Hugging Face forums, and NeurIPS Slack groups. These are warm distribution channels, not cold ones.

Market data on the specific "verified professional reputation" segment is not publicly available in a clean form. The broader talent intelligence market was valued at approximately $2.5 billion in 2023 (Grand View Research), but this figure includes enterprise ATS and sourcing tools that are adjacent, not identical, to the proposed product. Specific TAM data for the ML engineer vertical should be validated before fundraising.

---

## Current Market Analysis

**Market size:** The global ML engineer population is estimated at roughly 300,000–500,000 practitioners (LinkedIn talent data, 2023 estimates; exact figures not independently verified here). At a $20/month membership price, the theoretical revenue ceiling for 10% penetration of the low end is approximately $72M ARR — a meaningful but not venture-scale number without vertical expansion. This is honest: the initial market is small, and the rebuild must be designed to expand vertically (climate tech founders, biotech researchers) once the ML cohort is proven.

## Competition map:

- **LinkedIn** remains the category, but its specific weakness in this vertical is signal quality. ML engineers routinely complain that LinkedIn recommendations are generic and that endorsements for "Python" from a college roommate carry the same visual weight as an endorsement from a NeurIPS paper co-author. LinkedIn has no structured competency verification for technical roles and has shown no signs of building one — its revenue model (recruiter subscriptions, job ads) does not require it.
- **Levels.fyi** has built strong trust in the ML/engineering community for compensation data but does not offer reputation or recommendation infrastructure. It is a data product, not a network.
- **Polywork** attempted the "richer professional profile" thesis (launched 2021, raised ~$28M) and has not achieved breakout growth. Its weakness is that it remained horizontal — every professional, every vertical — and never built the trust-graph mechanic that makes recommendations meaningful.
- **Contra** targets independent contractors with verified work history but focuses on freelance placement, not community reputation.
- **Hugging Face** has become the de facto professional identity layer for ML practitioners (model cards, repositories, follower graphs) but is a code/model hosting platform, not a reputation or networking product.

**Demand signals:** The explosion of AI hiring in 2023–2025 has created a specific, documented problem: hiring managers cannot distinguish genuine ML engineers from credential-inflated applicants. This is a demand signal for verified reputation, not just better profiles.

**Defensibility against platform incumbents:** LinkedIn could theoretically add structured technical recommendations tomorrow. The honest answer is that this is a real risk. The structural defense is vertical depth and community switching costs: if the ML engineer community adopts this platform as its canonical reputation layer — the way Dribbble became canonical for designers — the social cost of leaving becomes high regardless of LinkedIn's feature additions. This is not a guaranteed moat. It requires winning the vertical before LinkedIn prioritizes it, which means speed matters more than defensibility in the early phase.

---

## Recommended MVP

## Feature 1: Structured Peer Recommendation Engine

Members request recommendations by selecting a competency domain (e.g., "distributed training infrastructure," "RL from human feedback") and nominating 3–5 peers to respond. Recommenders answer 4 specific situational questions rather than writing free-form praise. This differs from TrustedFor's model — which relied on open community responses — by directing requests to named individuals with domain-specific prompts, producing higher-signal input with less moderation overhead.

## Feature 2: LLM-Synthesized Reputation Profile

Once a member accumulates 5+ structured recommendations, GPT-4o (available via API, May 2024) synthesizes the responses into a calibrated competency summary with confidence intervals based on recommender count and recency. The output is a human-readable narrative plus a structured JSON object queryable by recruiters. This is the feature that was technically impossible in 2019 and that directly addresses the "gaming" problem: because recommenders answer specific situational questions, generic praise is structurally harder to produce.

## Feature 3: Verified Work History Layer

Integration with GitHub (public contribution graph), Persona (identity), and optionally Certn (employment verification) provides a cryptographic anchor for the reputation profile. Members can display a "verified" badge on specific claims. This differs from LinkedIn's Skills Assessments by verifying demonstrated output (merged PRs, published models on Hugging Face) rather than quiz performance.

## Feature 4: Cohort-Based Access and Cold-Start Seeding

The first 500 members are invited exclusively from three sources: NeurIPS/ICML 2024–2025 author lists (public), Hugging Face top contributors (public), and Maven ML course alumni (warm channel via partnership). This is the cold-start solution: the product does not open to general applications until the founding cohort is dense enough that any new member can receive at least 3 relevant recommendations within 30 days of joining.

**What we will NOT build:** A job board, a feed/timeline, a messaging product, or a mobile app in year one. Each of these expands scope without solving the core reputation problem and invites direct competition with LinkedIn on its strongest surfaces.

**Success metrics:** 500 founding members with verified profiles within 6 months; average of 7+ structured recommendations per member within 90 days of joining; 40%+ monthly active rate (defined as logging in and either requesting or completing a recommendation); recruiter NPS above 50 on profile quality.

**Cold-start threshold:** The product delivers value to a member when they have received at least 5 structured recommendations. The founding cohort strategy targets 500 members before public launch specifically to ensure that every new member can reach this threshold quickly through existing network density.

---34:T95e,

## Go-to-Market Strategy

**Target customer:** ML engineers with 3+ years of experience, globally distributed, who are either actively job-seeking or building a public research profile. Secondary customer: technical hiring managers at AI-native companies (Cohere, Mistral, AI startups) who are paying LinkedIn Recruiter fees ($8,000–$10,000/seat/year) and finding the signal quality inadequate for senior ML hires.

**Primary distribution channel:** Hugging Face community + conference author lists. Hugging Face has over 500,000 registered users (2024 estimate; exact figure not independently verified) with public profiles that already function as partial reputation signals. Outreach to top contributors is warm, not cold — these users already care about professional reputation in the ML community. NeurIPS 2024 had approximately 16,000 attendees; the author list is public and filterable by institution.

**Secondary channel:** Maven partnership. Maven hosts ML courses with paying cohorts of practitioners who have already demonstrated willingness to invest in professional development. A co-marketing arrangement (not confirmed; would require outreach) could seed the first 200–300 members.

**Pricing:** $20/month for members (individual reputation profile + recommendation access); $500/month for recruiters (queryable access to verified profiles + direct introduction requests). The $20/month individual price stress-tests as follows: LinkedIn Premium Career costs $39.99/month and is widely perceived as low-value by engineers. Discord and Slack communities are free but offer no structured reputation output. The $20 price is justified only if the member receives a tangible career outcome — a better job offer, a speaking invitation, a co-founder introduction — traceable to their profile. This means the product must instrument and surface these outcomes explicitly, or churn will be high. If the product cannot demonstrate outcome attribution within 6 months of launch, the individual subscription price should be reconsidered.

**Differentiation vs. 2026 competitors:** Polywork remains horizontal and unverified. LinkedIn remains generic and low-signal for technical roles. The rebuild's differentiation is vertical depth plus verification — not a better profile editor, but a trust graph that a hiring manager at a serious AI lab would treat as a primary signal rather than a supplementary one.
