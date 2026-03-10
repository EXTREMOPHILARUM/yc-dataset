# Build Plan: Reble 2026

## Overview

Reble was a Windows-only desktop application launched in public beta in February 2008 that let users stream music in real time directly from friends' local libraries using the Jabber P2P protocol; it was acquired by Playlist.com around 2009 after failing to solve a structural cold-start problem in a market rapidly moving to browser-based, catalog-first streaming.

The rebuild thesis is that every technical and legal barrier that killed Reble has since been resolved by others: WebRTC enables browser-native P2P audio, Spotify's API exposes friends' listening data without requiring local libraries, and blanket licensing has made the legal gray zone Reble occupied irrelevant. The new version is a licensed, browser-based social listening layer — a "listen together" product built on top of Spotify's catalog and social graph — that delivers Reble's original emotional promise (hearing exactly what your friend is hearing, right now) without asking anyone to install software, stream from their hard drive, or trust an untested legal theory.

---31:T94a,

## Why Now?

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

---34:T9bb,

## Go-to-Market Strategy
