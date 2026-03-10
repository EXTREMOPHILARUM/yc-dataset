# Build Plan: Anywhere.FM 2026

## Overview

Anywhere.FM 2026 is a managed cloud locker for music collectors—the 28–45 year old who buys lossless downloads from Bandcamp, Beatport, and artist stores, then wants frictionless access across all devices without managing their own server. We're solving the gap between streaming services (which don't own your library) and self-hosted solutions like Plex (which require technical setup most people won't do).

The Music Modernization Act fundamentally changed the licensing math. What killed the original in 2008—the need for complex label negotiations—is now a solved problem with clear statutory rates. Combined with fingerprinting technology (AcoustID) that's mature and cheap, we can match uploaded files to metadata instantly, eliminating the legal gray area that haunted the category for 15 years.

We win by being the easiest path to a portable music library. Launch with a freemium model ($5.99/month unlimited), target Bandcamp's community directly where music buyers already congregate, and prove the unit economics with 5,000 paying subscribers in six months—the metric the original never reached. No social features, no complexity. Just upload, play, own.34:T9af,

## Why Now?

The single most important change since Anywhere.FM's 2008 failure is the Music Modernization Act (MMA), signed into law in October 2018. For the first time, the MMA created a unified mechanical licensing collective (the MLC), standardized royalty rates for interactive streaming, and eliminated the legal ambiguity that made the "personal backup copy" doctrine a fragile foundation for any cloud music business. Anywhere.FM operated under a legal theory that was never tested in court on its behalf — and that theory was later invalidated when applied to Mp3tunes (EMI v. MP3tunes, decided 2014). A 2026 rebuild operates in a categorically different legal environment.

The infrastructure economics have also inverted. AWS S3 storage costs fell from approximately $0.15/GB/month in 2007 to $0.023/GB/month in 2024 — an 85% reduction per the rebuild signals above. Storing 45TB of music (equivalent to Anywhere.FM's 9 million songs at ~5MB each) now costs under $1,100/month versus roughly $6,750/month at 2007 prices. This alone changes the unit economics from structurally unviable to bootstrappable.

Distribution channels that didn't exist in 2007 now provide direct access to the highest-intent audience. Bandcamp (acquired by Songtradr in 2022, then restructured) retains a community of buyers who purchase music rather than stream it — exactly the user who has a local library worth preserving. Plex's developer ecosystem and Jellyfin's open-source community have collectively demonstrated, between 2015 and 2024, that millions of users will pay for managed "your library, anywhere" access. The Plex Pass subscription (currently $4.99/month or $119.99 lifetime, per Plex's public pricing) is a direct pricing proof point.

Spotify's Web API (available since 2014, with current catalog matching endpoints) now enables automatic matching of uploaded local tracks to licensed catalog entries — eliminating the legal locker risk while preserving the core value proposition. This technical capability did not exist in 2007 and changes the product architecture entirely.

The market signal is unambiguous: vinyl sales hit 40-year highs in 2022 (RIAA data), and streaming catalog removals (most visibly Neil Young's 2022 Spotify protest and ongoing Taylor Swift licensing disputes) have created documented consumer anxiety about library permanence. The "own your music" sentiment is not nostalgia — it is a measurable behavioral shift among high-value music buyers.

---

## Current Market Analysis

**Market size:** The global cloud storage market was valued at approximately $137 billion in 2024 (MarketsandMarkets, 2024 — specific music locker sub-segment data is not publicly available). The more relevant proxy is the personal cloud media management market, where Plex reported 8 million registered users as of 2023 (Plex blog, 2023). Anywhere.FM's total addressable market in 2007 was theoretically large but practically inaccessible due to licensing barriers; in 2026, the MMA has opened a statutory licensing pathway that makes the market genuinely reachable.

## Competition map and gaps:

- **Plex** (founded 2009): The dominant player in personal media servers, with 8M+ registered users and a proven freemium model. Critical weakness: Plex is self-hosted-first, requiring users to maintain a home server or NAS device. The managed SaaS version (Plex Cloud) was discontinued in 2018, leaving a direct gap for a fully managed cloud music locker. Plex also treats music as a secondary feature behind video.

- **Jellyfin** (open-source, forked from Emby in 2018): Free and self-hosted only. No managed cloud option by design. Serves technically sophisticated users; inaccessible to mainstream music buyers.

- **Apple Music** (launched 2015, 88M subscribers by 2022 per Bloomberg): Includes iCloud Music Library, which matches uploaded tracks to Apple's licensed catalog. Critical weakness: Apple ecosystem lock-in, no cross-platform library portability, and no social or discovery layer. Serves Apple device owners only.

- **Amazon Music Unlimited** (launched 2016): Includes cloud locker features inherited from Amazon Cloud Player (2011). Weakness: bundled with Prime, not positioned as a standalone music ownership product, weak metadata handling for non-Amazon purchases.

- **Spotify** (600M+ users, Q1 2024 earnings): No local file sync on mobile since 2022 (feature removed). This removal is a documented user complaint with active Reddit communities (r/spotify, 500K+ members) requesting its return — a direct demand signal.

**Adjacent demand signals:** Bandcamp's continued growth among music buyers who purchase FLAC and MP3 downloads, combined with Spotify's removal of local file sync, has created a documented gap: users who buy music digitally have no elegant way to access those purchases alongside their streaming library on mobile. This is the exact problem Anywhere.FM solved in 2007, now with a more monetizable audience.

---

## Recommended MVP

## Core Features:

## Managed Cloud Locker with Automatic Catalog Matching

Users upload local music files (MP3, FLAC, AAC) via a desktop uploader or drag-and-drop web interface; the service uses AcoustID fingerprinting and the Spotify Web API's track-matching endpoints to automatically link uploaded tracks to licensed catalog metadata, enriching artwork, lyrics, and credits without manual tagging. This differs from the original Anywhere.FM in one critical way: matched tracks stream from licensed sources where available, reducing storage costs and legal exposure simultaneously. Unmatched tracks (rare bootlegs, local recordings, Bandcamp exclusives) stream from the user's uploaded file. This hybrid architecture is technically feasible today using AcoustID (open-source, production-ready since 2013) and was impossible in 2007.

## Cross-Platform Web and Mobile Player

A responsive web player and native iOS/Android app providing access to the full uploaded library from any device. The interface prioritizes library navigation over algorithmic discovery — sortable by album, artist, year, and user-defined tags — directly addressing the documented frustration with Spotify's removal of local file sync on mobile (2022). Unlike the original Anywhere.FM's iTunes-mimicking browser player, this is a native mobile experience with offline caching for premium subscribers.

## Freemium Subscription with Hard Storage Tier

Free tier: up to 10,000 tracks stored, web player only. Premium tier ($5.99/month or $49.99/year): unlimited tracks, mobile apps, offline caching, and lossless FLAC streaming. This monetization model was never implemented by the original Anywhere.FM — it is the single most important structural difference between the original and the rebuild. Pricing is benchmarked against Plex Pass ($4.99/month) and Apple One ($19.95/month), positioning the service as a focused, affordable alternative for music-specific use cases.

## What we will NOT build (at MVP):

- Social profiles or Friend Radio (the original's social layer added complexity without monetization; validate the locker first)
- Podcast or video support (Plex's mistake was scope creep; music focus is the differentiator)
- Label licensing deals or original content (the MMA provides statutory licensing; direct label relationships are a Series A problem)
- Desktop application beyond a lightweight uploader (browser and mobile cover 95% of use cases)

## Success Metrics:

- 5,000 paying subscribers within 6 months of launch (validates willingness to pay, not just free usage — the metric Anywhere.FM never reached)
- Average uploaded library size ≥ 500 tracks per paying user (engagement signal indicating genuine library migration, not casual testing)
- Month-3 retention ≥ 60% for premium subscribers (subscription businesses require retention above 50% to be viable at this price point)
- Storage cost per paying user ≤ $0.80/month at steady state (unit economics threshold for profitability at $5.99 price point with 85%+ gross margin target)

---

## Go-to-Market Strategy

## Target customer segment:

The primary customer is a 28–45 year old music buyer who purchases digital downloads (Bandcamp, Beatport, HDtracks, or direct artist stores), owns a library of 500–5,000 tracks accumulated over 10–20 years, and has experienced Spotify's 2022 removal of local file sync as a direct pain point. This person is not a casual listener — they are a music collector who has already demonstrated willingness to pay for music ownership. They are disproportionately represented in electronic music, jazz, classical, and independent rock communities where catalog gaps on Spotify are well-documented. This is a narrow segment by design: estimated at 2–5 million users in the U.S. and EU combined (no precise data available), but with high intent and low price sensitivity relative to the general streaming market.

## Primary distribution channel:

Bandcamp's community forums, artist newsletters, and the Bandcamp Weekly podcast audience represent the highest-concentration channel for music buyers with local libraries. Secondary channels: Reddit communities r/audiophile (1.2M members), r/spotify (500K members, actively complaining about local file removal), and r/flac (180K members). These are organic, low-cost channels populated by exactly the target user. A referral program offering 2 free months of premium for each paying referral (benchmarked against Dropbox's successful referral model) accelerates word-of-mouth within these communities.

## Pricing strategy:

## Differentiation vs. 2026 competitors:

Against Apple Music: cross-platform (Windows, Android, Linux) and library-portable — your files are always exportable. Against Plex: zero infrastructure required, music-first UX, mobile-native. Against Spotify: your purchased music is permanent and accessible regardless of licensing disputes or catalog removals. The positioning statement is explicit and simple: *"The music you bought, everywhere you go — permanently."* This directly addresses the documented consumer anxiety about streaming catalog impermanence that has grown measurably since 2022, and it is a positioning no major streaming service can credibly adopt without undermining their own licensing model.
