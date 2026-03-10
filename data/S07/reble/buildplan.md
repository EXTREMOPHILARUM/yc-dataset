# Build Plan: Reble 2026

## Overview

Reble was a Windows-only desktop application launched in public beta in February 2008 that let users stream music in real time directly from friends' local libraries using the Jabber P2P protocol; it was acquired by Playlist.com around 2009 after failing to solve a structural cold-start problem in a market rapidly moving to browser-based, catalog-first streaming.

The rebuild thesis is that every technical and legal barrier that killed Reble has since been resolved by others: WebRTC enables browser-native P2P audio, Spotify's API exposes friends' listening data without requiring local libraries, and blanket licensing has made the legal gray zone Reble occupied irrelevant. The new version is a licensed, browser-based social listening layer — a "listen together" product built on top of Spotify's catalog and social graph — that delivers Reble's original emotional promise (hearing exactly what your friend is hearing, right now) without asking anyone to install software, stream from their hard drive, or trust an untested legal theory.

---32:T94a,

## Why Now?

The single most important change since Reble's failure is the Spotify Web API, launched in 2014 and substantially expanded through 2020, which allows third-party applications to read a user's currently playing track, listening history, playlists, and friend activity in real time — without any P2P infrastructure, without local library access, and without a software installation. This eliminates the bilateral cold-start problem that was Reble's structural death sentence: a new user can see what friends are listening to the moment they authenticate with Spotify OAuth, even if none of their friends have ever heard of the rebuild product.

The second critical enabler is WebRTC, standardized by W3C and IETF in 2021 and broadly supported in all major browsers since approximately 2017. WebRTC enables real-time peer-to-peer audio and data streaming directly in the browser. TechCrunch explicitly identified Reble's Windows-only installation requirement as its primary adoption barrier at launch; WebRTC eliminates that barrier entirely. A "listen along" session can now be initiated from a URL shared in iMessage or Discord — no download, no account creation required for the guest.

On the licensing side, the landscape has matured from existential threat to solved problem. Spotify, Apple Music, and YouTube Music have established blanket licensing agreements with all three major labels (Universal, Sony, Warner). Services building on top of Spotify's licensed catalog inherit those agreements by design. The legal gray zone Reble was navigating — streaming-not-downloading, private transmission vs. broadcast — is simply not a question a Spotify API-based product needs to answer.

Market data on the social listening segment specifically is limited in public sources, but adjacent signals are strong: Spotify reported 602 million monthly active users as of Q1 2024 (Spotify Investor Relations), and third-party social music apps built on the Spotify API — including Soundiiz and various "stats" products like Stats.fm — have demonstrated that Spotify users will authenticate third-party apps and share listening data. Discord's Spotify integration, which shows friends what you're listening to in real time, has been one of the platform's most-used status features since its 2018 launch, suggesting the demand signal Reble was chasing is real and large.

---

## Current Market Analysis

**Market size:** The global music streaming market was valued at approximately $19.4 billion in 2023 and is projected to reach $29.3 billion by 2030 (Grand View Research). The social music discovery sub-segment is not broken out as a standalone market in any public source this report has access to — that data gap should be treated honestly as a risk. What is documentable is the platform: Spotify's 602 million MAUs and Apple Music's estimated 88 million subscribers (MIDiA Research, 2023) represent the addressable pool from which a social listening layer would draw.

## Competition map:

- **Spotify's native friend activity feed** shows what friends are listening to in a sidebar, but it is passive, non-interactive, and hidden behind a desktop-only UI element that Spotify has repeatedly deprioritized in mobile redesigns. It does not support synchronized playback or real-time communication. Its weakness is intentional neglect — Spotify's core product investment is in podcasts and audiobooks, not social features.
- **Discord's Spotify integration** shows listening status but offers no synchronized playback or music-specific social features. Its weakness is context: Discord is a gaming and community platform; music is ambient, not primary.
- **Rave** (iOS/Android, active as of 2024) allows synchronized video and music listening with friends and has genuine traction in the Gen Z segment. It is the most direct current competitor. Its weakness is that it requires app installation, does not integrate natively with Spotify's social graph, and its UX is optimized for video co-watching rather than music-first experiences.
- **Vertigo** and **Quorus** are smaller Spotify-API-based listen-together products with limited public traction data. Their weakness is distribution — neither has found a sustainable acquisition channel.

**Demand signals:** Discord's Spotify status feature, Apple Music's "Friends Are Listening To" shelf, and the organic popularity of "listening party" threads on Twitter/X all confirm that the behavior Reble was building for exists at scale. The gap is a product that makes synchronous listening interactive, low-friction, and socially legible without requiring a full app install.

**Defensibility analysis:** This is the hardest question for the rebuild, and it deserves an honest answer. Spotify could build this natively — and has the social graph, the catalog, and the engineering resources to do so. The structural argument for why it hasn't, and may not, is threefold: (1) Spotify's product roadmap has visibly deprioritized social features in favor of creator monetization and podcast/audiobook expansion; (2) a standalone product can build cross-platform (Spotify + Apple Music + YouTube Music) social listening, which Spotify cannot do without cannibalizing its platform lock-in; and (3) the rebuild's value is in the interaction layer — voice, text, reactions during listening — which is adjacent to Discord's competency, not Spotify's. None of these arguments is airtight. If Spotify decides social listening is strategic, this product loses its primary distribution advantage. Founders should treat platform dependency as the primary existential risk, not a solved problem.

---

## Recommended MVP

## Feature 1: One-Click Listen-Along Sessions

A user authenticates with Spotify OAuth, shares a URL (via iMessage, Discord, or any messaging app), and a friend joins a synchronized listening session in the browser — no installation required. The host's playback state (track, position, queue) is mirrored to all guests in real time using WebRTC for synchronization signals and Spotify's playback API for actual audio. This differs from Reble's original in that audio comes from Spotify's licensed catalog, not a friend's hard drive, eliminating both the bilateral installation requirement and the legal exposure. The cold-start problem is addressed directly: a session has value with exactly two people, and the second person requires no prior account.

## Feature 2: Lightweight In-Session Communication

Text reactions, emoji responses, and optional voice chat (WebRTC audio) layered over the listening session. This is the interaction layer that Spotify's native friend feed entirely lacks and that Rave implements only partially for music. It transforms passive co-listening into the experience of being in the same room. The original Reble had a Jabber-based IM layer; this rebuilds that intent with modern WebRTC infrastructure and no separate messaging client required.

## Feature 3: Friend Library Browsing via Spotify API

A read-only view of what friends have been listening to recently — their top tracks, recent plays, and public playlists — surfaced as a browsable "what's on their shelf" interface. This is the direct spiritual successor to Reble's core insight (friends' libraries as a discovery surface) implemented legally through Spotify's existing data-sharing permissions. No P2P streaming, no local file access.

**What we will NOT build:** A proprietary streaming layer, a music catalog, a social network with profiles and followers, a mobile app (browser-first only for MVP), or any feature requiring Apple Music or YouTube Music integration before Spotify product-market fit is confirmed.

**Success metrics:** 500 listen-along sessions completed in the first 60 days post-launch; 40% of sessions involving a user who joined via shared URL without a prior account; 25% week-over-week retention among users who complete at least two sessions.

**Cold-start:** The product delivers value with two users. Session initiation requires only one authenticated Spotify user; the second participant needs only a browser and a Spotify account to join. There is no minimum network density threshold — this is the structural fix the rebuild makes over Reble's original architecture.

---35:T9bb,

## Go-to-Market Strategy

**Target customer:** Spotify-subscribed users aged 18–28 who already share music recommendations in Discord servers, group iMessage threads, or Twitter/X music communities — specifically, people who have already experienced the friction of saying "listen to this" and waiting for a friend to find the track independently. This is a narrow, identifiable segment with a demonstrated behavior gap.

**Primary distribution channel:** Discord. The target customer already lives there. The go-to-market tactic is direct integration: build a Discord bot that initiates a listen-along session from a slash command (`/listen [Spotify track URL]`), generating a browser session link posted directly in the channel. Discord has approximately 150–200 million monthly active users (Discord, 2023) and an established bot ecosystem with documented developer access. This channel requires no paid acquisition and reaches the exact social context — group music sharing — where the product's value is highest. Secondary channel: Spotify's own community forums and Reddit communities (r/spotify, r/ifyoulikeblank) where music discovery discussions are already happening organically.

**Pricing:** Free tier with sessions up to 3 participants and no voice chat. Paid tier at $4.99/month per user for unlimited participants, voice chat, and session history. The stress-test: users currently accomplish group listening coordination for free via Discord's Spotify status + a shared playlist link. The paid tier must be justified against that free alternative. The justification is synchronization (Discord shows what you're playing; it does not sync playback across listeners) and the voice-over-music layer (Discord's voice channels mute Spotify; the rebuild runs both simultaneously). If that differentiation does not resonate in user interviews, the pricing model should be reconsidered before launch — this is a genuine risk, not a solved question.

**Differentiation vs. 2026 competitors:** Against Rave, the rebuild wins on zero-installation friction and Spotify-native social graph integration. Against Spotify's native features, it wins on interactivity and cross-platform potential. Against Discord's integration, it wins on synchronization and music-first UX. The rebuild loses to all of them on brand recognition and distribution scale — which is why the Discord bot channel, which meets users where they already are, is the correct first move rather than attempting standalone app growth.
