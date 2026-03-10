# Build Plan: Bump 2026

## Overview

Bump 2026 is a proximity-based professional networking platform built for mid-size conferences and corporate events. It lets attendees exchange digital profiles instantly when they meet in person—no QR codes, no manual entry—while giving organizers real-time visibility into networking patterns and engagement across their event.

The viability shift is hardware: Ultra-Wideband is now standard on flagship phones and cheap enough to embed everywhere. What required expensive server-side sensor fusion in 2009 is now a $2 hardware problem. Combined with the digital business card market growing 100% by 2030, there's a real wedge between AirDrop (peer-to-peer, no context) and LinkedIn (asynchronous, no serendipity).

The go-to-market is event organizers, not consumers. A 500-person tech conference pays $15–25K for better attendee engagement and post-event ROI metrics. You win by making networking frictionless for attendees while giving organizers the data they've always wanted—who connected with whom, when, and where. It's B2B2C with a clear unit economics path.34:T9ff,

## Why Now?

## The single most important change: UWB is now commodity hardware, eliminating Bump's most expensive engineering problem.

Bump's original server-side accelerometer-matching algorithm was a genuine technical achievement — a distributed sensor-fusion system that identified paired devices in real time using GPS and accelerometer data. It was also expensive to operate at scale and introduced latency that made the product feel less magical than it appeared. Ultra-Wideband (UWB) chips, standardized under IEEE 802.15.4z, are now embedded in every iPhone 11 and later (released September 2019) and in a growing majority of Android flagships including the Samsung Galaxy S21+ series and Google Pixel 6 Pro onward. UWB enables centimeter-accurate, sub-10ms proximity detection natively at the hardware level, with no proprietary server matching required. A rebuilt Bump can use UWB as its proximity trigger — more accurate, lower latency, and dramatically cheaper to operate than Bump's 2009 infrastructure.

**The cross-platform gap AirDrop created is real and unaddressed.** AirDrop works only between Apple devices. Android's equivalent — Nearby Share, rebranded as Quick Share in 2024 — works only between Android devices and select Chromebooks. There is no native, frictionless proximity sharing solution for an iPhone user standing next to an Android user in 2026. This is not a niche scenario: Android holds approximately 72% of global smartphone market share (Statcounter, 2024), meaning the majority of professional interactions involve cross-platform pairs.

**The B2B digital identity market has validated the monetization model Bump never found.** HiHello has raised over $10M and reports enterprise customers paying $5–12/user/month for digital business card infrastructure. Popl, which uses NFC-enabled physical cards as a proximity trigger, has sold over 1 million cards and offers team plans at $6.49–$14.99/user/month (Popl pricing page, 2024). These companies prove that the contact-exchange use case — which Bump gave away free — can support SaaS-scale revenue when repositioned as a professional tool. Exact revenue figures for HiHello and Popl are not publicly disclosed.

**Distribution channels unavailable in 2009 now exist for B2B SaaS.** Salesforce AppExchange hosts 7,000+ apps with direct access to enterprise procurement workflows. HubSpot's App Marketplace reaches 200,000+ customers. Event technology platforms like Cvent and Hopin have established API ecosystems that a rebuilt Bump could integrate with directly, embedding proximity networking into existing event management workflows rather than requiring standalone app adoption.

---

## Current Market Analysis

**Market size:** The global digital business card market was valued at approximately $195M in 2023 and is projected to reach $390M by 2030 (Grand View Research, 2023). The broader professional networking software market — which includes event networking platforms, CRM integrations, and contact management tools — is harder to bound precisely; exact figures are not available in public sources. What is documented: the event technology market was valued at $7.5B in 2023 (Allied Market Research), and contact exchange is a core workflow within it.

## Competition map and specific gaps:

- **HiHello** (founded 2018, $10M+ raised): Digital business card platform with QR code and NFC sharing. Weakness: no proximity detection, requires active user intent (opening app, displaying QR), no cross-platform gesture mechanic. Strong on CRM integration, weak on in-person UX.
- **Popl** (founded 2020): NFC-card-triggered profile sharing. Weakness: requires purchasing a physical card ($15–30), no software-only option, Android NFC implementation is inconsistent across devices, no event analytics layer.
- **Bizzabo / Cvent** (enterprise event platforms): Include attendee networking features but rely on scheduled meeting booking and QR badge scanning — high friction, no ambient proximity detection. Weakness: networking is a secondary feature, not a core product.
- **LinkedIn's "Find Nearby"** feature: Bluetooth-based proximity discovery, buried in the app, requires both users to actively enable it simultaneously. Effectively unused; LinkedIn has not invested in the feature since launch. Weakness: opt-in friction makes it non-functional in practice.
- **Apple AirDrop**: Native, frictionless, zero-install — but Apple-only, transfers files rather than structured professional profiles, and has no CRM integration or analytics.

**Demand signals:** Popl's 1M+ card sales and HiHello's enterprise traction confirm that professionals will pay for better contact exchange. The failure of LinkedIn's Nearby feature confirms that the UX must be nearly zero-friction — which is exactly what UWB enables.

**Defensibility analysis:** This is the critical question, and the honest answer is mixed. Apple could extend AirDrop to support structured contact profiles and cross-platform sharing — technically feasible, strategically plausible. Google could do the same with Quick Share. The structural argument for defensibility is threefold: first, cross-platform proximity sharing requires cooperation between Apple and Google, which has historically not materialized for consumer features; second, the enterprise workflow layer — CRM sync, event analytics, team dashboards — is not something Apple or Google has shown appetite to build; third, the go-to-market motion (selling to event organizers and enterprise HR teams) is a B2B sales motion that platform companies structurally avoid. This is a real but not ironclad moat. If Apple and Google jointly standardize cross-platform proximity sharing (as they did with COVID exposure notification), this rebuild faces the same existential risk as the original. Founders should build toward CRM and event platform lock-in as fast as possible, because the UWB proximity trigger alone is not defensible.

---

## Recommended MVP

## Core Feature 1: Cross-Platform UWB/Bluetooth Proximity Profile Exchange

When two users with the app installed come within approximately 1 meter of each other and both make a deliberate confirmation gesture (a single tap, not a physical bump), their professional profiles exchange automatically — name, title, company, LinkedIn URL, and one custom field. This differs from the original Bump in two ways: it uses UWB for reliable cross-platform detection rather than server-side accelerometer matching, and it requires a single intentional tap rather than a physical collision, reducing false positives in crowded conference environments. For devices without UWB (older Android models), the fallback is Bluetooth Low Energy proximity with QR confirmation — explicitly a degraded experience, not the primary flow.

## Core Feature 2: Event Context Layer

Users join a named event (conference, sales kickoff, recruiting fair) on entry, either via a QR code at registration or an organizer-generated link. All exchanges within that event are tagged and grouped automatically. Post-event, each user receives a structured summary of every contact made, with one-click export to HubSpot, Salesforce, or a CSV. This is the retention mechanic the original Bump never had: the product delivers its highest value *after* the event, pulling users back to review contacts and follow up. The original Bump had no post-interaction value; this version makes the post-event summary the primary product.

## Core Feature 3: Organizer Dashboard

Event organizers get an aggregate view of networking activity — total exchanges, most-connected attendees, networking density by session or time block — without accessing individual contact data. This is the B2B monetization hook: organizers pay for the platform, attendees use it free. This feature did not exist in the original Bump, which had no B2B layer at all.

**What we will NOT build:** Consumer file transfer, photo sharing, payment triggers, or any feature that requires both users to have the app pre-installed before the event. The cold-start problem is addressed by selling to event organizers first: when an organizer deploys the platform for a 500-person conference, they drive installation through pre-event communications, eliminating the bilateral install dependency that constrained Bump's consumer growth. Minimum viable density is approximately 30% of attendees at a single event — below that threshold, the exchange frequency is too low to demonstrate value. Organizer contracts should include an attendee communication requirement to hit this threshold.

**Success metrics:** 40%+ of attendees at a deployed event complete at least one exchange; 25%+ of users open the post-event summary within 48 hours; organizer NPS ≥ 50 after first event; 3-month organizer retention ≥ 70%.

---37:Ta3e,

## Go-to-Market Strategy

**Target customer:** Mid-size professional conference organizers running events of 200–2,000 attendees in the United States — specifically, technology industry conferences, recruiting events, and sales kickoffs where contact exchange density is high and attendees are already carrying UWB-capable devices. This excludes consumer events (concerts, weddings) and massive trade shows (CES, NAB) where the enterprise sales cycle is too long for an early-stage company.

**Primary distribution channel:** Direct outbound to event organizers via conference industry networks (PCMA, MPI membership directories) combined with integration listings on Cvent's marketplace and Eventbrite's partner directory. The sales motion is organizer-first: one organizer contract deploys the product to hundreds of attendees simultaneously, solving the bilateral install problem that killed consumer Bump. Secondary channel: inbound from attendees who experienced the product at an event and want to bring it to their own company's events — a natural referral loop that requires zero additional marketing spend.

**Pricing:** $3–5 per attendee per event for organizers, with a minimum of $500 per event. At a 500-person conference, this yields $1,500–2,500 per event. Annual enterprise contracts (unlimited events, team dashboard, CRM integration) at $12,000–24,000/year for organizers running 6+ events annually. Attendees pay nothing.

This pricing must be stress-tested against free alternatives. LinkedIn's Nearby feature is free but effectively non-functional due to opt-in friction — not a real competitive threat on UX grounds. QR code badge scanning (standard at most conferences) is free but produces unstructured data with no CRM sync and no post-event summary. The $3–5/attendee price is justified if the organizer can demonstrate ROI through attendee satisfaction scores or sponsor engagement metrics — which the organizer dashboard enables. The honest risk: if organizers perceive networking as a solved problem (badges + LinkedIn), the sales conversation requires education before it requires pricing justification.

**Differentiation in 2026:** HiHello and Popl require active user intent and don't solve cross-platform proximity. LinkedIn Nearby is abandoned. No current competitor combines UWB proximity detection, cross-platform support, event context grouping, and CRM export in a single product. The rebuild's differentiation is the combination, not any single feature — which is also why building the CRM integration layer quickly is essential before a better-funded competitor assembles the same stack.
