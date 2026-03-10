# Build Plan: Beek 2026

## Overview

Beek was a Spanish-language audio subscription platform founded in Austin, Texas around 2014–2015 by Pamela Valdes Esteva and Max Holzheu; it grew from an emoji-based book review app into a $12/month audiobook and podcast service with 4 million users and a catalog of 250,000+ originals before being absorbed by Audible in 2024, with YC listing the company as inactive. The company's structural failure was not a bad thesis — Audible's own 2024 year-end report validated the identical market gap — but a classic aggregation outcome: Beek built the proof of concept, and the incumbent with superior distribution absorbed the catalog.

The rebuild thesis is this: AI-generated narration has collapsed the cost of producing Spanish-language audio content by roughly 100x, eliminating the creator subsidy that made Beek's original model expensive and acquisition-prone, while Spotify's proven audiobook subscription in Latin America means the market no longer needs to be educated. The new version is a lean, AI-native Spanish-language audio studio and subscription platform built explicitly to be acquired — not to out-scale Audible, but to become the catalog asset that Spotify, Apple, or a LatAm media conglomerate needs next.

---33:T5b0,

## Why Now?

### The single most important change: AI narration has eliminated the cost structure that made Beek's model fragile.

Beek's creator marketplace required the company to subsidize recording studios, audio editing services, and production support to lower the barrier for independent Spanish-language creators. This cost center was offset by creator-driven user acquisition (70%+ of new users), but it also meant Beek's catalog was expensive to build and its creator relationships were contingent on continued platform support. When Audible offered global distribution, the economics shifted.

As of 2024–2025, ElevenLabs, OpenAI TTS, and Google's Chirp 2 can produce near-human Spanish narration — including regional accent variants for Mexican, Colombian, Argentine, and Castilian Spanish — at under $0.01 per minute of finished audio. A 6-hour audiobook that previously required $2,000–5,000 in studio time and narration fees can now be produced for under $50 in compute costs. This is not a marginal improvement; it is a structural elimination of the primary cost barrier Beek faced.

## Specific market signals:

- Audible's December 2024 year-end review explicitly cited 486 million native Spanish speakers and approximately 50,000 Spanish audiobooks as a strategic priority — the same gap Beek identified in 2019, barely closed five years later. (Source: Audible Newsroom, December 2024.)
- Spotify's audiobook tier, launched in the U.S. in 2023 and expanded to multiple markets in 2024, now reaches 100M+ Latin American users who are already paying subscribers — the subscription behavior Beek had to educate the market on is now ambient.
- WhatsApp audio messaging has 90%+ penetration in Mexico and Brazil, establishing habituated mobile audio consumption among the exact demographic Beek targeted. No behavior change is required.
- Mercado Pago and Stripe's Mexico/Brazil expansion (Stripe launched full Mexico support in 2022) have matured the creator payout infrastructure that made per-minute royalty distribution operationally complex for Beek in 2019.
- The global audiobook market was valued at approximately $6.7 billion in 2023 and is projected to reach $35 billion by 2030 (Grand View Research, 2024 — note: LatAm-specific breakdown not publicly available in sources reviewed).

The distribution channels available now — Spotify's partner API, Apple Podcasts Connect, and WhatsApp Business for creator acquisition — did not exist in their current form when Beek was building. A new entrant does not need to build distribution from scratch.

---

## Current Market Analysis

### Market size today vs. Beek's operating years:

The Spanish-language audio content gap has barely closed despite five years of incumbent attention. Audible's own December 2024 data cites approximately 50,000 Spanish audiobooks — up from the 25,000 Beek cited in 2019, but still roughly 10x less than English-language catalog depth relative to speaker population. The global audiobook market has grown significantly (estimated $6.7B in 2023 per Grand View Research), but LatAm-specific revenue figures are not publicly available in sources reviewed for this report. What is documented: Spotify reports 100M+ monthly active users in Latin America as of 2024, and the region represents one of its fastest-growing podcast markets — confirming audio consumption at scale.

## Competition map and gaps:

- **Audible (Amazon)**: Dominant in English; now explicitly targeting Spanish. Weakness: its catalog model is licensing-first, not creator-native. It acquired Beek's catalog but has not replicated Beek's creator marketplace. Its subscription UX is optimized for English-language listeners. It has no per-minute creator payout infrastructure.
- **Spotify**: Massive distribution (100M+ LatAm users), strong in Spanish-language podcasts, expanding into audiobooks. Weakness: audiobook catalog in Spanish is thin; creator monetization for long-form audio (vs. podcasts) is underdeveloped. Spotify is a distribution platform, not a content studio.
- **Storytel**: Swedish subscription platform with LatAm ambitions. Weakness: licensing-first model, limited original Spanish content, no creator marketplace, limited brand recognition in Mexico and Colombia specifically.
- **Podimo**: Danish platform investing in original content. Weakness: primarily European focus; Spanish-language LatAm catalog is shallow; no AI-native production infrastructure.
- **Scribd**: U.S.-based subscription with some Spanish content. Weakness: not LatAm-native, limited creator relationships, no original production.

**The gap**: No current competitor combines (a) AI-native Spanish audio production at low cost, (b) a creator revenue-share model with per-minute payouts, and (c) a catalog strategy explicitly designed around M&A value to a major platform. The creator-native, AI-assisted model is genuinely unoccupied.

## Defensibility analysis — the platform commoditization question:

Beek's original failure was platform commoditization: Audible absorbed the catalog. The rebuild must answer why this doesn't happen again.

The honest answer is that it probably will — and the strategy should be designed around that reality rather than against it. The defensible position is not "build a moat Audible can't cross" but "build a catalog asset faster and cheaper than Audible can replicate internally, then sell to the highest bidder among Spotify, Apple, and LatAm media conglomerates before Audible can absorb it again." AI narration compresses the time-to-catalog from years to months. The window for independent operation is shorter, but the exit path is clearer. Spotify has explicit incentive to acquire a Spanish-language original audio catalog that would deepen its audiobook tier in LatAm — and unlike Audible, Spotify has not yet made a major Spanish-language catalog acquisition. Apple Podcasts and Apple Books represent a second potential acquirer. Televisa-Univision and Grupo Globo represent LatAm-native media conglomerates with distribution and brand but limited original audio infrastructure.

If the goal is long-term independence rather than a catalog exit, the defensibility case is weaker and should be stated honestly: a well-capitalized incumbent can replicate this model within 18–24 months of seeing it work.

---36:T4a5,$7.99/month (vs. Beek's $12/month). Justification: Spotify Premium in Mexico costs approximately MXN $99/month (~$5.50 USD as of 2025); a Spanish-language audio subscription must price within 50% of Spotify to avoid the "why not just use Spotify" objection. Spotify's audiobook catalog in Spanish is thin — this is the differentiation — but the price anchor is Spotify, not Audible. Free alternatives that overlap: Spotify free tier (podcast audio, no audiobooks), YouTube (some Spanish audiobook content, ad-supported), WhatsApp audio (social, not curated). The $7.99 price is defensible if the catalog contains original content unavailable elsewhere — which is the explicit strategy. If the catalog is not exclusive, the price is not defensible. Annual plan at $59.99 (~$5/month) should be offered at launch to improve cash flow and reduce churn.

**Stress-test:** A Mexican listener currently gets Spanish-language podcasts free on Spotify and can find some audiobook content on YouTube. The $7.99/month ask requires the catalog to contain content they cannot get elsewhere. This means exclusivity windows on creator content are non-negotiable from day one — not a nice-to-have.37:T985,

## Recommended MVP

## Core features:

### AI-Assisted Audio Studio for Spanish-Language Creators

An in-browser production tool that takes a creator's manuscript or outline and produces a narrated audiobook using ElevenLabs or OpenAI TTS (both available via API as of 2024), with regional accent selection (Mexican, Colombian, Argentine, Castilian) and basic audio mastering. This replaces the recording studio subsidies that cost Beek significant operational overhead. Unlike the original, creators do not need to record themselves — they submit text and receive a finished audio file within hours. Creators who want their own voice can upload recordings for AI voice cloning (ElevenLabs supports this as of 2023). The studio is free for creators; the platform takes a revenue share on listener minutes.

## Per-Minute Creator Payouts via Mercado Pago and Stripe

Creators earn a fixed rate per minute listened, paid out monthly via Mercado Pago (Mexico, Argentina, Brazil, Colombia) or Stripe (where available). This replicates Beek's most successful creator incentive — 35% of Beek's creators earned above local minimum wage in their first month — but with payment infrastructure that now exists across LatAm markets. Unlike the original, payout reconciliation is automated via API rather than manual. The cold-start problem for creator supply is addressed by targeting existing Spanish-language podcast creators on Spotify who already have audiences but no long-form monetization path.

## Curated Subscription Feed with LLM-Powered Discovery

A $7.99/month subscription (see pricing rationale in Section 4) giving listeners unlimited access to the catalog, with a personalized feed generated by GPT-4o (available via API, April 2024) or Claude 3.5 Sonnet (June 2024) based on listening history, completion rates, and explicit preferences. This directly addresses Valdes's post-Series A goal of making Beek "addictive" — the Tamber acquisition Beek made in 2022 to solve this problem is now replaceable with a commodity LLM API call. Unlike the original, discovery is personalized from day one rather than requiring catalog scale to become useful.

## What you will NOT build:

- A social layer or community features (Beek v1's book review community was engaging but not monetizable; avoid repeating this)
- Podcast hosting or distribution (Spotify owns this; compete on long-form originals only)
- Physical studio infrastructure or in-person creator support
- A proprietary recommendation model (use LLM APIs until catalog exceeds 50,000 titles)

## Success metrics with thresholds:

- 500 creator accounts with at least one published title within 90 days of launch
- 10,000 paying subscribers within 6 months (validates subscription willingness before scaling)
- Average listener completion rate above 60% per title (proxy for content quality and discovery relevance)
- Creator payout-to-CAC ratio: creator-driven acquisition should account for at least 50% of new subscribers within 6 months, replicating Beek's flywheel at lower cost

**Cold-start problem:** This platform does not require local density — audio is consumed asynchronously and individually. The minimum viable catalog for the subscription to feel non-empty is approximately 500 titles across 10+ genres. At $50/title in AI production costs, this requires $25,000 in content investment before launch — a manageable seed allocation. Target Mexico City-based creators first (largest Spanish-language creator concentration, strongest Mercado Pago infrastructure) to build initial supply before expanding to Colombia and Argentina.

---

## Go-to-Market Strategy

### Target customer segment:

Primary: Spanish-language podcast creators in Mexico with existing audiences of 5,000–50,000 followers on Spotify or YouTube who have no long-form audio monetization path. These creators already produce audio content, already have distribution habits, and already understand the format — they lack a revenue model for long-form work. Secondary: their existing listeners, who convert to subscribers when their favorite creator launches an audiobook on the platform. This replicates Beek's creator-as-distributor flywheel with a pre-qualified supply base.

## Primary distribution channel and tactics:

Direct outreach to the top 500 Spanish-language podcast creators on Spotify Mexico (Spotify for Podcasters dashboard provides public listener data). Offer a 90-day exclusive window with a guaranteed minimum payout of $500 for their first AI-produced audiobook — funded from seed capital, not ongoing operations. This is a creator acquisition cost, not a subsidy. WhatsApp Business for creator onboarding and support (90%+ penetration in Mexico; creators already use it for audience communication). No paid consumer acquisition until creator flywheel is validated.

## Pricing strategy:

# Voxa

## 1. Overview

Voxa is an AI-native Spanish-language audio subscription platform — a modern revival of Beek — where independent creators submit text manuscripts and receive finished, narrated audiobooks within hours using AI voice synthesis with regional accent selection. Listeners pay $7.99/month for unlimited access to an exclusive catalog of original Spanish-language audio content, while creators earn per-minute-listened royalties paid out via Mercado Pago and Stripe. The core value proposition is a two-sided flywheel: AI production collapses the cost of creating Spanish-language audio content by 100x, enabling a catalog depth no licensing-first competitor can match, while per-minute creator payouts turn creators into the platform's primary distribution channel.

---

## 2. Core Features

**Creator Studio**
- Submit manuscript (plain text or DOCX upload) to generate a narrated audiobook via ElevenLabs TTS API
- Select regional accent: Mexican, Colombian, Argentine, or Castilian Spanish
- Upload own voice recording for AI voice cloning (ElevenLabs voice clone API)
- Preview generated audio chapter-by-chapter before publishing
- Edit chapter order, titles, and cover art before publishing
- Track per-title listening minutes, completion rates, and estimated earnings in real time
- View monthly payout history and upcoming payout date

**Content Catalog**
- Browse catalog by genre (ficción, no ficción, desarrollo personal, negocios, historia, ciencia, meditación)
- Search titles, authors, and descriptions with full-text search
- View title detail page: cover, description, sample audio, creator profile, listener count
- Play 5-minute sample without subscription

**Listener Experience**
- Persistent audio player with playback speed control (0.5×–3×), sleep timer, and chapter navigation
- Personalized "For You" feed powered by GPT-4o based on listening history and explicit preferences
- Continue listening queue across devices (progress synced server-side)
- Mark titles as favorites; build a personal library
- Rate titles (1–5 stars) after completing 80%+ of content

**Subscription & Payments**
- $7.99/month or $59.99/year subscription via Stripe
- 7-day free trial for new subscribers
- Subscription management: upgrade, downgrade, cancel, reactivate
- Mercado Pago checkout for Mexico, Argentina, Colombia, Brazil (currency-local pricing)
- Invoice history and downloadable receipts

## Differentiation vs. 2026 competitors:

Against Audible: creator-native, not licensing-native; faster catalog growth via AI production; LatAm-first UX and payment infrastructure. Against Spotify: long-form original content focus, per-minute creator payouts, no ad tier. Against Storytel/Podimo: AI production cost advantage means 10x more titles at the same content budget; explicit LatAm market focus rather than European-first expansion. The rebuild's clearest differentiation is speed-to-catalog: at $50/title vs. $2,000–5,000/title, a $500K content budget produces 10,000 titles instead of 100–250 — a catalog depth that no licensing-first competitor can match at equivalent capital deployment.
