# Build Plan: Newslabs 2026

## Overview

NewsLabs (YC W2010) built NewsTilt, a curated network where credentialed journalists could publish independently while the company handled advertising, SEO, and community management — the platform launched in April 2010, survived two months, and shut down in June 2010 after its core differentiating feature (journalist-owned personal domains) was cut from the MVP, advertising economics proved unworkable, and a co-founder communication breakdown prevented recovery.

The rebuild thesis is simple: every infrastructure problem that killed NewsTilt in 2010 is now a commodity. Custom domain provisioning takes hours, not months. Stripe Connect automates revenue splits. AI handles the SEO and distribution work that required a manual team. And Substack has already proven — at scale — that journalists will pay for tools that help them own their audience. The new version is a white-label publishing infrastructure layer for mid-career journalists leaving institutional media, built on subscriptions from day one, with personal domains and brand ownership as table stakes rather than aspirational features.

---34:T987,

## Why Now?

## Current Market Analysis

**Market size:** The creator economy broadly is estimated at $250 billion in 2023 (Goldman Sachs Research), though the specific segment of professional journalist publishing tools is not broken out in public data — any figure cited here would be an inference. What is documented: Substack reported over 35 million active subscriptions in 2023, Ghost processes payments for over 2 million subscribers across its hosted platform, and Beehiiv raised a $33 million Series B in 2023 citing rapid newsletter creator growth. The addressable market for professional journalist publishing infrastructure is real and actively contested.

## Competition map and specific gaps:

- **Substack** (dominant): Takes 10% of subscription revenue with no ceiling, offers no custom domain ownership by default (domains are `writer.substack.com`), provides no SEO infrastructure, and has faced repeated creator backlash over content moderation decisions. Its core weakness is the revenue take rate at scale — a journalist earning $500,000 annually pays $50,000/year to Substack for infrastructure that costs a fraction of that to provide.
- **Ghost** (open-source/hosted): Technically strong, subscription-native, and charges flat SaaS fees rather than revenue cuts. Its weakness is that it is a publishing tool, not a network — it provides no discovery, no cross-promotion, and no audience acquisition support. Writers must bring their own audience entirely.
- **Beehiiv** (newsletter-focused): Strong growth tools and referral infrastructure, but optimized for newsletter-first creators rather than long-form journalism. Limited article/archive SEO capability.
- **WordPress.com** (legacy): Ubiquitous but not journalist-specific, no subscription infrastructure, and no network effects.

**The gap:** No current competitor combines (a) flat-fee or low-percentage pricing, (b) genuine personal domain ownership, (c) AI-assisted SEO and distribution, and (d) a curated professional network with cross-promotion between journalists. Substack has the network; Ghost has the ownership model; nobody has both plus AI-assisted distribution.

**Defensibility against platform incumbents:** This is the honest hard question. Meta (Threads), LinkedIn, and Google (via Search) all have adjacent products and could theoretically add newsletter or publishing features. LinkedIn has already added newsletters natively. The structural defense is not technical moat — it is switching cost and brand identity. A journalist whose byline lives at `janesmith.com`, whose subscriber list is portable, and whose SEO authority accrues to her own domain has no reason to migrate to a platform-controlled URL. The rebuild must make data portability and domain ownership non-negotiable from day one. If a future platform incumbent commoditizes the infrastructure layer, the journalist's audience, domain, and SEO equity remain hers. This is a real but imperfect defense — it depends on execution, not on any structural barrier that incumbents cannot cross.

---

## Recommended MVP

## Core Feature 1: Journalist-Owned Personal Domains (Day One, Non-Negotiable)

Every journalist on the platform publishes at their own domain (`janesmith.com` or `janesmith.yourplatform.com` as a stepping stone), provisioned automatically via Cloudflare for SaaS integration. This is the feature NewsTilt cut and never recovered from. It is not a premium add-on — it is the product's reason to exist. Unlike NewsTilt's from-scratch build, this is implemented on top of Ghost's open-source CMS layer, reducing engineering scope to the domain provisioning and network layer only.

## Core Feature 2: Subscription-First Revenue with Flat-Fee Pricing

Journalists set their own subscription prices; the platform charges a flat monthly SaaS fee (see pricing below) rather than a percentage of revenue. Stripe Connect handles all payment processing and automated payouts. This directly addresses Substack's core weakness at scale and gives the platform a clear, defensible pricing narrative. Unlike NewsTilt's advertising model — which required traffic that didn't exist — subscriptions generate revenue from a journalist's first paying reader.

## Core Feature 3: AI-Assisted SEO and Distribution

Using GPT-4o (available May 2024) or equivalent, the platform auto-generates SEO meta descriptions, Open Graph social cards, and weekly newsletter digest drafts for each journalist's archive. This is the operational promise NewsTilt made but could not staff with two engineers. It is now a prompt-engineering integration, not a headcount problem. Unlike Substack and Ghost, which leave SEO entirely to the writer, this feature delivers on the "we handle distribution" value proposition that originally attracted journalists to NewsTilt.

## Core Feature 4: Curated Cross-Promotion Network

Accepted journalists can opt into a weekly cross-recommendation digest — each journalist recommends one other journalist on the platform to their subscriber list. This is a lightweight network effect that Ghost and Beehiiv do not offer, and it addresses the cold-start problem directly (see below). It requires no minimum platform size to deliver value: even two journalists cross-promoting each other generates incremental subscriber growth for both.

**What we will NOT build:** A reader-facing destination site or homepage. NewsTilt's fatal confusion was positioning itself as a destination competing with news organizations. This rebuild is infrastructure, not media. No editorial vetting beyond basic quality standards. No advertising sales. No proprietary CMS built from scratch.

**Cold-start problem:** This product does not require local density or network scale to deliver core value. A single journalist with zero platform peers still benefits from personal domain ownership, subscription infrastructure, and AI-assisted SEO. The cross-promotion network adds value incrementally as the journalist cohort grows — it is an enhancement, not a prerequisite. Target 50 active publishing journalists within 90 days of launch as the threshold at which cross-promotion becomes meaningfully valuable.37:T9a5,

## Success metrics:

- 50 active publishing journalists within 90 days (defined as: published at least 2 pieces in the trailing 30 days)
- Average journalist MRR from subscriptions exceeds platform fee within 6 months (journalists are net-positive on the platform)
- 30-day journalist retention above 70%
- Median time-to-first-subscriber under 14 days for new journalists

---

## Go-to-Market Strategy
