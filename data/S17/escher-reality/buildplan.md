# Build Plan: Escher Reality 2026

## Overview

By 2026, Escher Reality rebuilds as a cross-platform AR session layer that unifies mobile phones, spatial computing headsets, and industrial devices into shared persistent experiences. It targets enterprise AR teams at manufacturing, logistics, and field service companies who need their workers on different devices to see and collaborate on the same digital objects in real space—something no existing platform handles cleanly today.

The viable insight is neural rendering. NeRF and 3D Gaussian Splatting have made photorealistic 3D reconstruction fast and cheap enough to run on-device. That means Escher can anchor shared AR experiences to real-world geometry with far higher fidelity than 2017's feature-based mapping, and do it without heavy cloud dependency. Enterprise customers will pay for that reliability and accuracy.

The go-to-market is direct: land with one industrial use case—say, collaborative equipment assembly or site inspection—where cross-device persistence solves a concrete workflow problem. Build the SDK tight enough that a small AR team can integrate it in weeks, not months. Win on developer velocity and device coverage where Niantic's Lightship remains fragmented.34:T9a3,

## Why Now?

## Current Market Analysis

**Market size.** In 2017, the mobile AR developer tools market was effectively pre-revenue — ARKit had launched weeks before Escher's seed round closed, and the addressable market was theoretical. By 2026, the picture is materially different. The broader spatial computing developer tools market is estimated at approximately $1.2 billion today, growing toward $4.7 billion by 2028 (MarketsandMarkets, 2023; specific segmentation between mobile AR and headset AR tools is not publicly broken out with precision). Enterprise AR software alone — the vertical with the clearest willingness to pay — is estimated at $6.6 billion in 2024 (IDC, 2024; exact figure not independently verified and should be treated as directional).

## Competition map.

*Niantic Lightship (direct descendant of Escher's technology):* The most capable shared/persistent AR SDK available, but carries three structural weaknesses for a rebuild opportunity. First, it is Niantic-controlled and optimized for Niantic's location-based game use cases — enterprise manufacturing or field service workflows are not its design target. Second, Lightship requires Niantic account infrastructure and data flows through Niantic's servers, a non-starter for enterprise customers with data sovereignty requirements. Third, Lightship does not support Apple Vision Pro or Meta Quest 3 natively as of 2024.

*8th Wall (acquired by Qualcomm, 2022):* Strong in WebAR and browser-based experiences, but focused on marketing and retail activations rather than persistent multi-user infrastructure. No meaningful spatial mapping or cross-session persistence capability.

*Immersal (acquired by Hexagon, 2021):* Offers Visual Positioning System (VPS) and spatial mapping for enterprise, but lacks real-time multi-user session management. Strong on persistence, weak on shared experience coordination.

*Unity AR Foundation:* Provides cross-platform ARKit/ARCore abstraction but explicitly does not handle multiplayer state, persistence, or cross-device session management. It is infrastructure for single-user AR, not shared AR.

**Gap:** No neutral, platform-agnostic SDK simultaneously handles cross-platform shared sessions, persistent spatial anchors, and multi-form-factor support (mobile + headset + browser) for enterprise developers. That gap is the rebuild opportunity.

**Demand signals.** Matterport's $2.9 billion acquisition by CoStar (2023) signals enterprise willingness to pay for spatial data infrastructure. PTC's Vuforia and Scope AR's WorkLink both demonstrate that industrial AR with shared workflows commands $50,000–$500,000 annual enterprise contracts — validating that the willingness-to-pay problem Escher never solved (consumer gaming developers monetize slowly) can be bypassed entirely by targeting enterprise from day one.

---

## Recommended MVP

**Core Feature 1: Cross-platform shared session management (mobile + headset).** The SDK handles real-time state synchronization across iOS (ARKit), Android (ARCore), Meta Quest 3, and Apple Vision Pro within a single shared AR session. A field technician on a HoloLens and a remote supervisor on an iPhone see and manipulate the same digital overlay on the same physical equipment simultaneously. This directly replicates Escher Reality's original multiplayer capability but extends it to the headset form factors that now dominate enterprise AR deployments — a surface the original Unity plug-in never addressed.

**Core Feature 2: Gaussian Splat-powered persistent spatial anchors.** Using 3D Gaussian Splatting (Kerbl et al., 2023), the SDK builds a lightweight scene representation from a 30-second phone scan, stores it on the developer's chosen cloud infrastructure, and re-localizes any supported device to that anchor within 2 seconds on subsequent visits. This replaces the expensive custom computer vision pipeline that was Escher Reality's primary technical moat in 2018 with a commodity reconstruction technique, reducing the engineering cost of persistence by an estimated order of magnitude (specific cost benchmarks are not yet publicly established for production Gaussian Splatting pipelines at scale).

**Core Feature 3: WebXR session bridge.** A JavaScript SDK companion that allows browser-based AR sessions (via WebXR Device API) to join the same shared session as native mobile or headset clients. A worker on a factory floor with a headset and a manager reviewing on a laptop browser participate in the same persistent AR overlay without either party installing an application. This addresses the distribution friction that Escher Reality's Unity-only approach could not solve and opens the SDK to web developers — a substantially larger pool than Unity game developers alone.

**Core Feature 4: Enterprise data residency controls.** Spatial anchor data and session logs can be stored in the customer's own cloud environment (AWS, Azure, GCP) rather than on the SDK provider's servers. This is a non-negotiable requirement for manufacturing, defense, and healthcare enterprise customers and is the specific weakness that disqualifies Niantic Lightship from most enterprise procurement processes.

**What we will NOT build:** Consumer gaming features, location-based game infrastructure, a proprietary mapping network (Niantic's competitive moat), a no-code AR authoring tool, or any end-user-facing application. This is infrastructure only.

**Success metrics:** 50 enterprise developer accounts with active integrations within 12 months of launch; at least 3 paying enterprise customers at $24,000+ ARR each by month 18; SDK re-localization accuracy of ≤0.5 meters in 90% of test environments; shared session latency of ≤100ms for 2–8 concurrent users on a standard commercial network.

---

## Go-to-Market Strategy

**Target customer segment.** The primary target is enterprise AR developers at industrial companies — specifically, software engineers and AR solution architects at manufacturing, logistics, and field service firms with 500+ employees who are already deploying or piloting AR for maintenance, training, or inspection workflows. This segment has three properties that make it the right starting point: willingness to pay is established (Scope AR and PTC Vuforia demonstrate $50,000–$500,000 annual contract sizes), the shared/persistent AR use case is immediately obvious without market education (two technicians need to see the same digital overlay on the same physical machine), and data sovereignty requirements create a structural barrier that eliminates Niantic Lightship as a competitor.

**Primary distribution channel.** The PTC Marketplace and the Salesforce AppExchange are the two highest-leverage enterprise AR distribution channels available in 2026 — not consumer app stores. Secondary channel: direct outreach through the AWE (Augmented World Expo) enterprise track and the XR Association's enterprise working groups, where AR solution architects self-select. A Unity Asset Store listing serves as a developer discovery channel for the long tail, mirroring Escher Reality's original distribution logic, but is not the primary revenue driver.

**Pricing strategy.** Three tiers: a free developer tier (up to 5 concurrent users, 10 persistent anchors, no SLA) to replicate Escher's zero-friction adoption model; a Growth tier at $2,000/month (up to 50 concurrent users, 500 anchors, standard SLA) targeting mid-market AR studios; and an Enterprise tier at $24,000–$120,000/year with data residency controls, custom SLA, and dedicated support, targeting industrial customers. This structure is justified by the Agora and Mapbox pricing precedents in adjacent infrastructure categories and by the demonstrated enterprise contract sizes in industrial AR. Usage-based overage charges apply above tier limits, preserving Escher's original alignment-of-incentives logic.

**Differentiation vs. 2026 competitors.** Against Niantic Lightship: platform-neutral, no Niantic data dependency, enterprise data residency, Vision Pro and Quest 3 native support. Against Immersal: real-time multi-user session management, not just VPS. Against 8th Wall: persistent spatial anchors and headset support, not just browser marketing activations. Against Unity AR Foundation: the shared session and persistence layer that Unity explicitly does not provide. The positioning statement is simple and traceable to the original Escher thesis: *the neutral backend for shared, persistent, cross-platform AR — for enterprise teams who cannot build it themselves and cannot trust a competitor's platform to host it.*
