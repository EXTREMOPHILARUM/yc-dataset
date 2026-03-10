# Build Plan: Zigfu 2026

## Overview

Zigfu 2026 is a cross-platform hand-tracking SDK for Unity developers building spatial computing apps on Meta Quest 3, Apple Vision Pro, and web browsers. It abstracts away the fragmentation that currently forces developers to write separate integrations for each platform—one API, three hardware targets, shipped as a $199 perpetual license on the Unity Asset Store from day one.

The market shift is simple: spatial computing hardware is now real and shipping at scale, but the developer tooling layer remains fragmented. Meta and Apple both lock developers into their own SDKs; open-source alternatives like MediaPipe require custom integration work. Zigfu wins by being the neutral, production-ready abstraction layer that saves developers 4–6 weeks of integration work per project.

The go-to-market is ruthlessly focused: launch on the Unity Asset Store immediately (not after raising capital), target independent developers and small studios as the primary segment, and use the $27B digital signage market as the anchor enterprise wedge. Pricing is $199 per developer seat with optional monthly support—low enough to convert the long tail of indie builders, high enough to fund sustainable growth without chasing venture capital.34:T946,

## Why Now?

The single most important change since Zigfu's 2012 failure is the elimination of its core platform risk. Zigfu's entire product depended on Microsoft Kinect hardware, PrimeSense NITE middleware, and the OpenNI framework — all controlled by third parties. PrimeSense's 2013 acquisition by Apple killed OpenNI entirely, which would have destroyed Zigfu's product even if the company had survived its fundraising crisis. In 2026, that risk structure no longer exists.

Apple Vision Pro (launched February 2024) and Meta Quest 3 (launched October 2023) ship hand tracking at the OS level, built directly into visionOS and Meta's Presence Platform respectively. A rebuilt Zigfu building on these platforms has Apple and Meta as distribution infrastructure, not dependency risks. The hardware manufacturers are now incentivized to keep developer tooling alive — the opposite of the Kinect situation.

Critically, dedicated depth sensors are no longer required at all. MediaPipe (Google, open-sourced 2019) and Apple's ARKit hand tracking deliver production-grade skeleton and hand tracking on commodity hardware — smartphones, laptops, standard webcams. The original Zigfu required developers to own a $150 Kinect peripheral with a small installed base. A rebuilt Zigfu targets the 3B+ smartphone install base.

Distribution has also transformed. Unity's Asset Store generated over $200M in annual developer revenue as of 2023, with 1.5M+ monthly active creators — validating the exact $200/seat SDK model Zigfu launched in March 2012, too late and too underfunded to exploit. The Shopify App Store analogy applies directly: a gesture SDK listed on Unity's Asset Store today reaches a pre-qualified, paying developer audience that simply did not exist at scale in 2012.

WebXR (W3C standard, ratified 2019) replaces Zigfu's browser plugin architecture entirely, enabling zero-install gesture-controlled web experiences in any compatible browser — eliminating the adoption friction that limited ZigJS.

The investor landscape has shifted structurally. Andreessen Horowitz's a16z Games fund (launched 2022, $600M) and dedicated XR investment theses at Benchmark, Khosla, and others mean the "doesn't fit VC pattern-matching" problem Hirsch identified as a core fundraising obstacle is materially reduced for a spatial computing developer tools company with traction.

---

## Current Market Analysis

## Market Size

The global digital signage market — where Zigfu found its only profitable OEM customers — reached $27B in 2023, up from approximately $14B in 2012 (source: Grand View Research). Gesture-controlled kiosks are now a validated commercial category deployed in retail, healthcare, and hospitality, meaning the B2B revenue thesis Zigfu stumbled toward at the end is now a fundable, proven market rather than a speculative one.

The broader spatial computing developer tools market is harder to size precisely in isolation — no authoritative standalone figure is available for this specific segment. However, the no-code/low-code developer tools market reached $13B in 2023 (source: Gartner), providing a comparable category benchmark. Unity's Asset Store alone demonstrates $200M+ in annual developer tool transactions.

## Competition Map and Gaps

Current competitors fall into three tiers:

- **Meta's Presence Platform and Apple's visionOS SDK**: First-party tools with deep hardware integration but platform-locked. A Unity developer building cross-platform gesture experiences cannot use either natively across both headsets simultaneously. This is Zigfu's 2026 opening — the cross-platform abstraction layer that neither Apple nor Meta will build because it benefits their competitor.

- **Ultraleap** (formerly Leap Motion): Hardware-dependent hand tracking SDK with strong enterprise traction but requires proprietary peripheral hardware, limiting addressable market. Weakness: no smartphone or webcam support.

- **8th Wall / Niantic**: WebAR platform with gesture features, but optimized for marketing experiences rather than developer infrastructure. Weakness: not a general-purpose SDK; pricing targets enterprise marketing budgets, not indie developers.

- **Mediapipe-based open-source projects**: Free but fragmented, undocumented, and unsupported. Weakness: no Unity integration, no commercial support, no cross-platform abstraction.36:T8d0,

## Demand Signals

Unity's XR Interaction Toolkit (open-source) has 2,000+ GitHub stars and active issues requesting better hand-tracking abstraction across devices — direct evidence of unmet developer demand for exactly what Zigfu built.

---

## Recommended MVP

## Core Features

## Cross-Platform Hand Tracking SDK for Unity (the ZDK, rebuilt)

A single Unity package that abstracts hand tracking across Meta Quest 3, Apple Vision Pro, and webcam/smartphone via MediaPipe — one API, three hardware targets. This directly addresses the gap neither Apple nor Meta will fill. Unlike the original ZDK, it ships on Unity's Asset Store on day one, not twelve months after product readiness. It targets Unity 6 (released 2024) and integrates with the XR Interaction Toolkit rather than replacing it.

## WebXR Gesture Component Library

A JavaScript/TypeScript library providing pre-built gesture UI components (menus, carousels, drag-and-drop) that run in any WebXR-compatible browser via MediaPipe, with zero installation required. This replaces Zigfu's ZigJS and browser plugin with a standards-compliant, frictionless alternative. Unlike the original, it requires no browser plugin and works on any device with a camera.

## Digital Signage Integration Module

A pre-packaged Unity module targeting the $27B digital signage market — Zigfu's most commercially durable original customer segment. It includes touchless interaction templates for retail kiosks, healthcare check-in, and hospitality wayfinding, with a commercial licensing tier priced for enterprise deployment. Unlike the original OEM pivot, this is a product sale, not a custom engineering engagement.

## What We Will NOT Build

No proprietary game content (no Sushi Warrior equivalent). No motion OS for TV OEMs. No custom contracting engagements in year one. No hardware of any kind.

## Success Metrics

- 500 paid Unity Asset Store licenses within 6 months of launch (threshold: $100K ARR at $200/seat)
- 3 signed enterprise digital signage contracts within 9 months (threshold: $150K total contract value)
- 2,000 WebXR library npm downloads/month within 6 months (developer adoption signal)

---

## Go-to-Market Strategy

## Target Customer Segment

Primary: Independent Unity developers and small studios (1–10 people) building XR applications for Meta Quest 3 or Apple Vision Pro who need hand tracking to work consistently across both platforms without maintaining two separate codebases. These developers are already paying for Unity Pro ($2,040/year) and actively purchasing Asset Store packages — they are pre-qualified buyers with demonstrated willingness to pay for developer tools.

Secondary (months 6–12): Enterprise buyers deploying touchless kiosks in retail and healthcare, where post-COVID hygiene preferences have created durable demand for gesture-controlled interfaces. This segment has budget, longer sales cycles, and higher contract values.

## Primary Distribution Channel

Unity Asset Store, launched on day one of commercial availability — the exact mistake Zigfu did not make. Tactics: (1) submit to Asset Store before any investor meetings; (2) publish a "Show HN" and Unity forum thread simultaneously with launch; (3) target Unity's official "Verified Solutions" partner program for Asset Store featuring.

Secondary channel: GitHub open-source core with a commercial license tier, following the Ultraleap and Mapbox model. Open-source drives developer discovery; commercial license converts enterprise buyers.

## Pricing

- Unity SDK: $199/developer seat (perpetual) + $49/month for updates and support — matching Zigfu's original price point but adding a recurring support tier that Zigfu never offered.
- Enterprise digital signage module: $2,500–$10,000 per deployment site, based on installation scale.
- WebXR library: Free and open-source core; $99/month commercial license for white-label deployments.

## Differentiation vs. 2026 Competitors

Unlike Ultraleap, no proprietary hardware required. Unlike Meta/Apple first-party SDKs, genuinely cross-platform. Unlike open-source MediaPipe wrappers, commercially supported with SLA. The rebuilt Zigfu's moat is the cross-platform abstraction layer — the one thing neither hardware manufacturer will build for competitive reasons, and the one thing open-source projects cannot sustain commercially.
