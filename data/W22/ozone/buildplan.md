# Build Plan: Ozone 2026

## Overview

Ozone 2026 is a browser-native video editor built for small creative agencies and in-house social teams producing short-form content at scale. It's not a general-purpose tool—it's purpose-built for the workflow of 5–50 person teams who need to collaborate in real-time, move fast, and ship to multiple platforms. The product emphasizes speed (4K editing in-browser, zero installation), collaboration (simultaneous review and approval), and automation (one-click captions and localization).

The timing window is now. CapCut's forced US divestment in January 2025 displaced millions of creators and agencies who built their workflows around it. Unlike the original Ozone, which competed on technical novelty against entrenched incumbents, this version competes on migration friction—we solve the immediate problem of teams who need to move their projects somewhere trustworthy and fast. One-click CapCut import removes the switching cost entirely.

Go-to-market is direct sales to creative agencies and in-house video teams, starting with agencies already losing CapCut access. The pitch is simple: keep your workflow, add collaboration, keep your data in the US. Launch with 500 paying teams in six months, target $150/month per account, and own the post-CapCut vacuum before Adobe or another well-funded player fills it.33:T8cc,

## Why Now?

The single most important change since Ozone's failure is the CapCut displacement event. In January 2025, the US government forced ByteDance to divest or face a TikTok/CapCut ban under the Protecting Americans from Foreign Adversary Controlled Applications Act. While enforcement has been inconsistent, the legislative threat created genuine anxiety among the estimated 200M+ US CapCut users and the agencies, brands, and social media teams that built workflows around it. This is a structural demand signal Ozone could not have anticipated — a large, trained user base actively looking for a credible alternative with no obvious destination.

The second critical change is infrastructure commoditization. WebCodecs and WebGPU APIs, broadly supported in Chrome and Edge as of 2024–2025, now enable hardware-accelerated video decoding and processing natively in the browser. Ozone spent approximately three years and most of its $7.22M building proprietary compression algorithms to achieve browser-based 8K playback. A 2026 rebuild can replicate that core technical feat in months, not years, using platform-native APIs — dramatically compressing the development timeline and preserving runway for go-to-market execution.

On the infrastructure side, Cloudflare Stream (pricing available at cloudflare.com/products/cloudflare-stream) now offers programmable video transcoding and delivery at commodity rates, replacing what would have been a significant cost center. OpenAI's Whisper (open-source, released September 2022) delivers near-human transcription accuracy at near-zero marginal cost via API, eliminating the expensive caption feature that Ozone gated behind its $29/month Pro plan.

The video editing software market was valued at approximately $2.1B in 2023 (source: research report). Specific 2025–2026 market size data is not available to this author, but the CapCut displacement event represents a near-term demand spike that is time-sensitive and real.

Distribution channels unavailable to Ozone now exist: the Shopify App Store (2M+ merchants producing product video), the Notion partner ecosystem, and Slack's App Directory all offer direct access to the B2B team workflows that are the correct target for a 2026 rebuild.

---

## Current Market Analysis

**Market size:** The global video editing software market was approximately $2.1B in 2023, growing at ~7% CAGR through 2030 (source: research report). Updated 2026 figures are not available to this author. The broader creator economy was estimated at over $100B in 2023, with the software layer representing a fraction of that. The more relevant market for a 2026 rebuild is the B2B video workflow segment — agencies, social media teams, and localization teams — where willingness to pay is higher and switching costs are structurally greater than in the solo creator segment.

## Competition map and gaps:

- **CapCut (ByteDance):** 200M+ US users, free, deeply TikTok-integrated — but facing ongoing US regulatory risk and enterprise distrust due to ByteDance ownership. Its weakness is precisely its ownership structure and the absence of a credible team/agency workflow layer.
- **Descript:** Strong for podcast and long-form text-based editing; weak on short-form social video workflows and real-time multi-user timeline collaboration. Raised $50M in 2022 (source: research report).
- **Runway:** Focused on AI video generation, not editing workflows. Raised at a $1.5B valuation (source: research report). Weak on practical day-to-day editing for social teams.
- **Adobe Premiere/Express:** Powerful but expensive ($55+/month), desktop-heavy, and organizationally complex for small agency teams.
- **Frame.io (Adobe):** Handles review and approval but is not an editor — it is a feedback layer on top of Premiere.

**The gap:** No current tool combines browser-native editing, real-time team collaboration, and a CapCut-comparable short-form UX in a US-owned, enterprise-trustworthy package. That gap is the rebuild opportunity.

**Demand signals from adjacent products:** Loom's $975M acquisition by Atlassian in 2023 (source: research report) confirms enterprise willingness to pay for video-native B2B workflows. Figma's continued dominance post-Adobe-acquisition-block validates the browser-native collaborative tool model at scale.

---

## Recommended MVP

## Core Feature 1: Browser-native timeline editor with WebCodecs/WebGPU acceleration

A clean, fast, browser-based video timeline supporting up to 4K footage without installation, leveraging WebCodecs and WebGPU APIs available natively in Chrome and Edge as of 2024–2025. This replicates Ozone's headline technical achievement in a fraction of the original build time. Unlike Ozone's proprietary compression approach, this uses platform-native APIs, reducing maintenance overhead and improving reliability across devices.

## Core Feature 2: Real-time collaborative review and approval layer

Multiple team members — editors, account managers, clients — can comment, annotate, and approve cuts on a shared timeline simultaneously, with version history. This is not solo-creator collaboration theater; it is the specific workflow that agencies and social media teams actually need: getting client sign-off on a cut without emailing MP4 files. Unlike Frame.io, this is built into the editor itself, eliminating the Premiere → Frame.io → Premiere round-trip.

## Core Feature 3: Whisper-powered auto-captions with one-click localization

Automatic caption generation using OpenAI's Whisper API (open-source, September 2022) at near-zero marginal cost, with one-click translation into the top 10 languages. This directly addresses the localization team use case — a structurally collaborative workflow — and is a feature that CapCut offers only in limited form. Unlike Ozone's original implementation, this is not gated behind a credit system; it is included in the base paid plan to drive retention.

## Core Feature 4: CapCut project import

A one-click importer for CapCut project files, allowing displaced CapCut users to migrate existing projects without rebuilding from scratch. This is a direct response to the CapCut displacement event and a distribution mechanism disguised as a feature.

**What we will NOT build:** AI video generation (Runway owns this), AI image generation, AI speech synthesis, or any generative AI feature that requires significant compute infrastructure. These were Ozone's reactive additions in 2024 and contributed to scope creep on a small team. We will not build a mobile app in the first 12 months.

## Success metrics:

- 500 paying teams (not individual users) within 6 months of launch
- 60-day team retention ≥ 40%
- Average revenue per account ≥ $150/month
- CapCut import used by ≥ 30% of new signups in first 90 days

---

## Go-to-Market Strategy

**Target customer segment:** Social media managers and video editors at independent creative agencies with 5–50 employees, producing short-form video content for brand clients on TikTok, Instagram Reels, and YouTube Shorts. Specifically, agencies that currently use CapCut for editing and Frame.io or email for client review — a workflow that is broken, expensive, and now legally uncertain. This is narrow by design: these users have genuine collaborative workflow pain (client approval is a team activity), they have budget authority, and they are actively looking for a CapCut alternative.

**Primary distribution channel:** Direct outreach to agency owners via LinkedIn, combined with a CapCut Migration Program — a dedicated landing page offering free white-glove migration support for agencies moving off CapCut. This is time-sensitive and should launch within 60 days of MVP completion. Secondary channel: the Shopify App Store (2M+ merchants), targeting e-commerce brands with in-house social video teams.

**Pricing strategy:** $149/month per team (up to 5 seats), $249/month for up to 15 seats. No free tier — a deliberate departure from Ozone's freemium model, which attracted price-sensitive solo creators rather than teams with budget. The price point is justified by the Frame.io + CapCut replacement value (Frame.io alone costs $15/user/month at scale). A 14-day free trial replaces the free tier.

**Differentiation vs. 2026 competitors:** Against CapCut — US-owned, enterprise-trustworthy, team-workflow-native. Against Descript — short-form video-first, not podcast-first; real-time collaboration, not async text editing. Against Frame.io — editing and review in one tool, not two. Against Runway — practical daily editing workflow, not AI generation research. The positioning is simple: the first browser-native video editor built specifically for agency teams who need to edit fast and get client approval faster.
