# Build Plan: Teevox 2026

## Overview

By 2026, Teevox is a native multi-stream viewer built for competitive eSports—not a remote control app. It solves the core problem that killed the original: letting viewers watch multiple POVs of the same tournament simultaneously, with synchronized audio switching and one-click layout assembly. The product targets serious eSports fans aged 18–34 who follow specific players and teams across League of Legends, Valorant, and CS2, where watching co-streams is already standard practice but fragmented across browser tabs.

The market timing is inverted from 2012. eSports viewership has grown from 15 million to over 200 million monthly viewers, and Twitch's follow-graph API now makes it trivial to auto-load all live channels a user cares about. The insight: competitive viewers *want* multi-stream experiences but have no good tool for it. MultiTwitch exists but is visually dated, has no accounts, and no monetization path.

The go-to-market is direct: launch on Reddit's eSports communities and Discord servers where these viewers already congregate, offer the MVP free, and convert 5–10% to a $4.99/month premium tier for custom layouts and ad-free viewing. First target is League Worlds 2026 viewership surge.33:T8ce,

## Why Now?

The single most important change since Teevox's 2012 failure is the scale of the eSports and live-streaming audience. The market Teevox needed simply did not exist when it operated. The global eSports viewership base has grown from approximately 15 million monthly viewers in 2011 (per founder Jong-Moon Kim's own account) to over 200 million by 2016, and Newzoo's estimates place the broader live-streaming audience — including variety and IRL content on Twitch — well above 700 million monthly viewers by the mid-2020s, though precise 2026 figures are not available in the research record. The demand-side risk that killed the original company has been eliminated.

Three additional structural changes make 2026 materially different from 2012:

**Infrastructure costs have collapsed.** The "hemorrhaging money" problem Kim cited was fundamentally a bandwidth and CDN cost problem. Cloudflare's R2 and Stream products (launched 2022), combined with Fastly's edge delivery network, have reduced multi-stream video delivery costs by an order of magnitude compared to 2012 infrastructure. A rebuilt Teevox no longer faces the same unit economics death spiral.

**The Twitch API is now stable and mature.** Twitch's 2014 acquisition by Amazon for $970 million produced a well-documented, SLA-backed API with OAuth authentication, stream metadata endpoints, and affiliate revenue hooks. The platform fragility risk of building on early Twitch is gone.

**Co-streaming culture is now mainstream.** Major tournaments — League of Legends Worlds, Valorant Champions, The International — routinely feature dozens of streamers broadcasting simultaneous POV feeds of the same event. This behavior did not exist at scale in 2011. It creates a new, high-frequency use case for multi-stream viewing that is structurally different from the original StarCraft tournament use case and generates recurring daily demand rather than seasonal spikes.

**Distribution channels now available:** Twitch's own discovery surface (35M+ daily active users per Twitch's 2023 public disclosures), Reddit communities including r/leagueoflegends (6M+ members) and r/GlobalOffensive (1.5M+ members), and direct integration with Discord servers used by tournament organizers.

---

## Current Market Analysis

**Market size:** The live-streaming viewing market is orders of magnitude larger than in 2011–2012. Twitch alone reported over 35 million daily active users in 2023 (Twitch public disclosures). Precise 2026 figures are not available in the research record, but the directional trend is unambiguous. The eSports-specific segment — Teevox's core audience — is a meaningful subset of this base.

## Existing competitors and their specific weaknesses:

- **MultiTwitch.tv** — The most direct incumbent. Functional but visually dated, with no user accounts, no stream synchronization, no Twitch follow-graph integration, and no mobile support. It is a static URL-builder, not a product. Its persistence despite these limitations confirms ongoing unmet demand.
- **Kadgar.net** — Adds basic layout customization over MultiTwitch but remains a thin web tool with no monetization layer, no social features, and no co-streaming-specific UX. No documented active development.
- **Twitch Squad Stream** — Twitch's native multi-stream feature, limited to four channels, requires all streamers to opt in simultaneously, and is unavailable to viewers watching solo. It solves the streamer coordination problem, not the viewer experience problem.
- **YouTube Multiview** — Launched for NFL Sunday Ticket (2023), limited to four streams, sports-only, no gaming or eSports support.

**The gap:** No current competitor offers synchronized multi-POV viewing of co-streaming events, Twitch follow-graph integration, mobile-native layout, or any monetization layer for power viewers. The market has persistent demand and no dominant product.

**Demand signals from adjacent products:** Discord's Watch Together feature (launched 2021) demonstrated that synchronized co-viewing is a behavior users will adopt at scale. Twitch's own Squad Stream feature, despite its limitations, validated that the platform sees multi-stream viewing as a legitimate use case worth building for.

---

## Recommended MVP

## Core Features:

### Co-Stream Event Hub

When a major tournament is live, Teevox automatically surfaces all co-streaming POVs of that event in a single organized view, pulling from the Twitch API's game and tag metadata. Users can select two to six streams and arrange them in a responsive grid. This differs from the original Teevox by targeting a specific, recurring use case — co-streaming events — rather than generic multi-stream browsing, which creates a natural content calendar and predictable traffic spikes that can be planned around rather than feared.

## Follow-Graph Stream Loader

Users authenticate via Twitch OAuth and instantly load all channels they follow that are currently live, with one-click multi-stream assembly. This feature was the centerpiece of Kim's 2016 rebuild and demonstrated clear user demand in that Show HN response. The 2026 version adds smart grouping — automatically clustering followed channels by game or event — reducing the friction of manual stream selection.

## Synchronized Audio Switching with Hotkeys

A single active audio channel at a time, switchable via keyboard shortcut or tap, with visual indicators showing which stream is "hot." Stream preloading — the technical differentiator Kim identified from the original — is rebuilt using modern browser APIs (MediaSource Extensions, available since Chrome 2016) to eliminate buffering on switch. This directly addresses the core UX problem that made the original product technically distinctive.

## Premium Viewer Tier ($4.99/month)

Unlocks layouts beyond four streams, custom saved layouts, ad-free experience, and early access to new features. This is the monetization layer the original Teevox never built. At even 1% conversion of a 50,000 MAU base, this generates $2,500 MRR — enough to cover CDN costs and sustain a solo founder.

**What we will NOT build:** A mobile app (web-responsive only at launch), streamer-side tools, original content, social features, or any platform beyond Twitch. No hardware integrations.

## Success metrics:

- 10,000 MAU within 90 days of launch
- 500 paid subscribers within 6 months ($2,500 MRR)
- Average session duration above 45 minutes (indicating genuine multi-stream viewing behavior, not bounce traffic)
- 20%+ month-over-month retention at the 30-day mark

---

## Go-to-Market Strategy

**Target customer segment:** Competitive eSports viewers aged 18–34 who follow multiple players or teams in a single title — specifically League of Legends, Valorant, or CS2 viewers during major tournament windows. This segment watches co-streaming events where five to ten streamers simultaneously broadcast their own POV of the same match. They are already on Twitch, already in Discord servers organized around their game, and already frustrated by the absence of a clean multi-stream tool. They are not casual viewers; they are the 5–10% of a game's audience who follow individual players rather than just teams.

**Primary distribution channel and tactics:** Reddit and Discord, not paid acquisition. The original Teevox hit the Reddit front page organically — this playbook is repeatable. Target subreddits: r/leagueoflegends (6M+ members), r/ValorantCompetitive (500K+ members), r/GlobalOffensive (1.5M+ members). Launch during a major tournament window (e.g., League of Legends Worlds, which runs annually in October) when the co-streaming use case is most acute and organic sharing is highest. Post a Show HN simultaneously. Partner with two or three mid-tier streamers (10K–100K followers) to feature Teevox in their Discord servers in exchange for early premium access.

**Pricing strategy:** Freemium with a hard feature gate. The free tier supports up to four streams with standard layouts — sufficient for casual use and viral sharing. The $4.99/month premium tier unlocks six-plus streams, saved layouts, and ad removal. This price point is below Twitch's own subscription tier ($4.99–$24.99) and positions Teevox as a complement to, not a replacement for, platform spending. Annual pricing at $39.99 (33% discount) incentivizes commitment and reduces churn.

**Differentiation vs. 2026 competitors:** MultiTwitch and Kadgar are infrastructure, not products — no accounts, no personalization, no monetization, no mobile. Teevox wins on UX polish, follow-graph integration, and the co-streaming event hub, which gives it a content calendar that drives predictable traffic. Unlike the original Teevox, monetization is built in from day one, solving the structural failure that made 700,000 free users a liability rather than an asset.
