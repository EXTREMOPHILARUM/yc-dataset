# Build Plan: Eventjoy 2026

## Overview

Eventjoy was a mobile-first event management platform founded in 2013 by Todd Goldberg and Karl White, acquired by Ticketmaster just seven months after its February 2014 public launch, and ultimately retired in September 2015 when Ticketmaster merged it into Universe — not because the product failed, but because a large incumbent absorbed it as a feature before it could build a durable independent business.

The rebuild thesis: three structural changes have converged to make this viable as a standalone company in 2026 — the mid-market event app space has been vacated by consolidation (DoubleDutch, Guidebook, and Quickmobile are all gone or pivoted), embedded finance infrastructure now enables a revenue model that doesn't require charging organizers, and post-COVID behavioral norms have eliminated the attendee app adoption friction that constrained Eventjoy's growth. The new version is a composable event operating system for independent organizers — free to use, monetized through float revenue and self-serve promotional tools — built to be too sticky to absorb cheaply.

---34:Taf5,

## Why Now?

## Current Market Analysis

**Market size:** The global event management software market was estimated at approximately $14.5 billion in 2023 (Grand View Research), up from roughly $6 billion in 2014 when Eventjoy operated. The DIY and independent organizer segment — events with 50–2,000 attendees, budgets under $50,000, no dedicated technical staff — is not broken out separately in available public data, so the addressable slice of this market for a rebuild is an inference, not a verified figure.

## Current competition and gaps:

- **Eventbrite** remains the dominant ticketing incumbent but has moved aggressively toward its own discovery marketplace, creating a structural conflict with organizers who don't want their attendees exposed to competitor events. Its mobile app experience for attendees remains generic and non-customizable. Eventbrite's fee structure (3.7% + $1.79 per paid ticket as of 2024) creates ongoing organizer resentment that a free alternative can exploit.
- **Whova** is the closest current analog to what Eventjoy was building — bundled ticketing, attendee app, networking, and analytics. Its weakness is pricing: Whova charges $1,500–$5,000+ per event, pricing out the independent organizer segment entirely. It is explicitly positioned for professional conference organizers, not community event runners.
- **Luma** (lu.ma) has emerged as a credible free-tier competitor for small events, with clean design and good social sharing. Its weakness is the ceiling: Luma has no native attendee app, no in-event communication layer, and no meaningful analytics. It serves the "fancy Eventbrite" use case but not the "event operating system" use case.
- **Bevy** and **Hopin** (now RingCentral Events) have both pivoted toward virtual and hybrid enterprise events, effectively abandoning the in-person independent organizer market.

**Demand signals:** Luma's rapid growth among tech community organizers — without a native app or in-event tools — signals strong latent demand for a more complete product at the same price point (free). Organizers are actively choosing worse tools to avoid Eventbrite's fees, which is a clear willingness-to-switch signal.

**Defensibility analysis:** This is the hardest question for any Eventjoy rebuild, and it deserves an honest answer. Eventbrite could add a native attendee app and in-event chat tomorrow — it has the engineering resources and the organizer base. The structural reason it likely won't is the same reason it hasn't in the decade since Eventjoy was acquired: Eventbrite's business model depends on per-ticket fees, which creates an organizational incentive to maximize ticket volume rather than deepen organizer tooling. A rebuild monetized through float and promotional tools has a different incentive structure — one aligned with organizer success rather than ticket volume. That alignment is a real but soft moat. It is not a technical barrier. If the rebuild reaches meaningful scale (say, $50M+ GMV), Eventbrite or a well-funded new entrant could replicate the model. The defensibility window is approximately 18–36 months of focused execution before the competitive response arrives. Founders should plan accordingly and not assume the moat is permanent.

---

## Recommended MVP

## Core Feature 1: Composable event pages with embedded ticketing (free)

A single-URL event page that handles registration, ticketing (free and paid), and attendee communications — built on Stripe Connect for payment processing, with float revenue as the business model rather than per-ticket fees. Unlike Eventjoy's 2014 version, this is not a custom-built payment stack; it composes Stripe's infrastructure, reducing the surface area that incumbents can absorb by replicating proprietary technology. The "free" positioning is sustainable because the revenue model doesn't depend on organizer fees — it depends on float yield and promotional upsells.

## Core Feature 2: Native attendee app with QR check-in and push announcements

A white-labeled mobile app (iOS and Android) that organizers can configure in under 10 minutes, with QR code check-in, push notification announcements, and a basic event schedule. This is the feature Eventjoy built in 2014 that required convincing attendees to download an app for a single event — a behavioral ask that is now normalized. Unlike Eventjoy's version, the 2026 rebuild should offer a Progressive Web App (PWA) fallback so attendees who won't install a native app still get the core experience via browser, eliminating the adoption floor problem.

## Core Feature 3: In-event communication layer

Real-time attendee-to-organizer messaging and organizer broadcast announcements, built on Stream's Chat API (launched 2015, now production-grade) rather than custom infrastructure. This is the feature Eventjoy added in January 2015 and cited as addressing "a big pain point during events" — but it was added post-acquisition and never monetized. In 2026, this feature is the primary premium upsell: free for events under 200 attendees, paid tier ($49/month or $149/event) for larger events with moderation tools and analytics.

## Core Feature 4: Self-serve promotional tools

Paid event promotion via Meta Ads API and Google Events structured data, offered as a managed service inside the organizer dashboard. Organizers set a budget ($50–$500), the platform runs the campaign, and charges a 15% management fee on ad spend. This is the "event promotion" premium service Eventjoy announced in May 2014 but never executed — it was aspirational then because Ticketmaster's distribution was the only meaningful promotional channel. In 2026, Meta Ads API and Google's event rich results provide measurable, self-serve promotional ROI that organizers will pay for.

**What we will NOT build (MVP):** venue sourcing, virtual/hybrid event streaming, enterprise SSO, custom integrations marketplace, social media aggregation walls, or any feature requiring a dedicated sales motion. The MVP is self-serve only.

## Success metrics:

- 500 organizers running at least one event within 90 days of launch
- $1M in GMV processed within 6 months (enabling ~$40,000–$50,000 in annualized float revenue at current yield rates — a proof-of-model milestone, not a profitability threshold)
- 40% of organizers running a second event within 60 days of their first (retention signal)
- In-event communication paid tier conversion: 15% of events with 200+ attendees upgrading within 30 days of the feature gate

**Cold-start problem:** This product does not depend on local density or network effects between attendees — each event is a self-contained deployment. An organizer running a 300-person beer festival gets full value from the platform on day one, regardless of how many other organizers are using it. The cold-start problem is an organizer acquisition problem, not a network density problem. The threshold for the core feature to deliver value is one organizer running one event.

---

## Go-to-Market Strategy

**Target customer segment:** Independent event organizers running recurring in-person events with 100–1,500 attendees — specifically: tech community organizers (meetup series, hackathons, developer conferences), local festival and market operators, and professional association chapter leads. These organizers share three traits: they run events frequently enough to develop platform loyalty, they are currently paying Eventbrite fees they resent, and they have enough attendees to generate meaningful float GMV. Single-event organizers (weddings, one-off fundraisers) are explicitly out of scope for the initial GTM — their churn rate makes them uneconomical to acquire.

**Primary distribution channel:** Community-led, not paid acquisition. The founding team should personally run or sponsor 20–30 events in the first six months using the platform — exactly as Eventjoy's founders did with Startup Weekend events in 2013. This generates authentic case studies, surfaces product gaps under real conditions, and creates word-of-mouth in the organizer community. Secondary channel: the Luma user base, which has demonstrated willingness to use free event tools but is hitting Luma's feature ceiling. Direct outreach to Luma power users (identifiable via public event pages) with a "you've outgrown Luma" positioning is a specific, executable tactic.37:T53a,- Core platform: free (ticketing, event pages, QR check-in, basic attendee app)
- In-event communication: free under 200 attendees; $49/month subscription or $149/event for larger events
- Promotional tools: 15% management fee on ad spend, minimum $50 campaign

The free core must be stress-tested against Luma (free, no app), Eventbrite (paid, full-featured), and group chats (WhatsApp/Slack, free, zero friction). The honest answer: a WhatsApp group and a Google Form can run a 100-person event for free. The rebuild wins only if the organizer values the QR check-in, the attendee app, and the analytics enough to switch workflows — which is a real but non-trivial ask. The GTM must lead with the check-in and app features (demonstrable, immediate value) rather than the float model (invisible to organizers) or the promotional tools (future value). Organizers should feel the product saves them time on event day before they're asked to pay for anything.

**Differentiation vs. 2026 competitors:** Against Luma — native attendee app and in-event communication. Against Eventbrite — zero fees and organizer-aligned incentives. Against Whova — 10x lower price point for the same core feature set. The positioning is not "better than Eventbrite" — it is "Eventbrite for organizers who run events as a community, not a business."38:T896,

## Pricing strategy:
