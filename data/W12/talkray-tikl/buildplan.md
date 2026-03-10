# Build Plan: Talkray (TiKL) 2026

## Overview

By 2026, Talkray is a B2B workforce communications platform for operations teams managing field workers—delivery fleets, maintenance crews, warehouse staff. The product combines instant push-to-talk channels with searchable voice transcription and automatic dispatch integration, solving the real problem: teams today juggle Slack, radio systems, and fragmented tools when they need one coordinated voice layer that creates an audit trail.

The market shift is simple: enterprise customers now pay for compliance and searchability. Talkray's original consumer app failed because voice-over-data was a commodity feature. But in logistics and field service, a PTT channel that auto-transcribes every transmission and integrates with ServiceNow or Zendesk is defensible—and worth $200–500/month per team.

The go-to-market targets operations managers at SMBs (10–200 field workers) in last-mile delivery, maintenance, and warehousing. Launch with a tight integration to one dispatch system, win 10 paying accounts in 90 days, and expand vertically. The win is speed and compliance where Motorola's enterprise PTT is overkill and Slack has no voice.33:T76a,

## Why Now?

## Current Market Analysis

**Market size:** The enterprise push-to-talk software market is a subset of the broader workforce communications and field service management space. Exact 2026 market sizing is unavailable in the research report; independent verification against current Gartner or IDC reports is recommended before fundraising. What is confirmed: Motorola Solutions' WAVE PTX at $15–30/user/month represents the current pricing ceiling, and Zello reported 150 million registered users as of 2023, validating durable demand for the PTT interaction model.

## Competition map and gaps:

- **Motorola Solutions WAVE PTX**: The incumbent enterprise PTT platform. Strength: brand trust with large enterprises and public safety. Weakness: legacy pricing ($15–30/user/month), hardware-bundled sales motion, poor UX for SMB buyers, no self-serve onboarding.
- **Zello**: 150 million registered users, strong in crisis response and informal professional use (trucking, construction). Weakness: consumer-grade UX, limited enterprise integrations, no workflow tooling, freemium model that struggles to convert to paid.
- **Microsoft Teams Walkie Talkie**: Native PTT within Teams. Weakness: requires Teams licenses, no standalone deployment, poor performance on low-bandwidth connections, no offline capability.
- **Voxer**: PTT with asynchronous voice. Weakness: stagnant product development, no meaningful enterprise integrations since approximately 2019 (exact date unavailable).

**The gap:** No current competitor offers a self-serve, SMB-priced enterprise PTT tool with native workflow integrations (ticketing, dispatch, incident logging) at a price point below $10/user/month. This is the gap a rebuild occupies.

**Demand signals:** Zello's surge to #1 in app stores during Hurricane Harvey (2017) and the Ukraine conflict (2022) confirms that PTT demand is durable and spikes predictably during exactly the operational scenarios — logistics disruption, field emergencies, coordinated response — where enterprise buyers have budget.

---

## Recommended MVP

## Core Feature 1: Instant PTT Channels with Role-Based Access

Press-and-hold voice transmission across named channels (e.g., "Warehouse Floor," "Dispatch," "Site 3"), with manager-controlled permissions. Built on Agora SDK or Daily.co WebRTC for sub-300ms latency. This is what TiKL built for consumers; the rebuild delivers it with enterprise access controls TiKL never implemented.

## Core Feature 2: Persistent Voice Logs with Searchable Transcription

Every PTT transmission is automatically transcribed using Whisper API (OpenAI, available via API since November 2022) and stored with speaker ID, timestamp, and channel tag. This transforms ephemeral voice into auditable operational records — a compliance and accountability feature that enterprise buyers in logistics, construction, and field service will pay for and that no current PTT competitor offers natively.

## Core Feature 3: Dispatch-to-Channel Workflow Trigger

Inbound tickets from connected tools (ServiceNow, Zendesk, or a simple webhook) automatically open a PTT channel and alert the assigned team. Closes the loop between task assignment and real-time coordination without requiring workers to switch apps. This is the integration layer TiKL's API pivot attempted but never executed with a specific buyer workflow in mind.

**What we will NOT build:** Consumer-facing features, text messaging, image/video sharing, a public app store listing targeting individual downloads, or any feature requiring a social graph. No general-purpose communications suite. The original Talkray pivot toward WhatsApp-style messaging is explicitly off the roadmap.

## Success metrics:

- 10 paying enterprise accounts within 90 days of launch (minimum 5 users/account)
- Net Revenue Retention ≥ 110% at 6 months
- Average session-to-transmission rate ≥ 70% (users who open the app send a PTT message)
- Monthly churn below 3%

---

## Go-to-Market Strategy

**Target customer segment:** Operations managers at SMBs with 10–200 field or deskless workers in three verticals: last-mile logistics (delivery fleet coordinators), commercial construction (site supervisors), and facilities/property management. These buyers have active PTT needs, existing frustration with Motorola WAVE's pricing, and budget authority under $500/month — below enterprise procurement thresholds that require lengthy sales cycles.

**Primary distribution channel:** Microsoft Teams App Store (320 million MAUs per Microsoft FY2023) and the ServiceNow Store. Both provide direct access to operations buyers who already have approved vendor relationships and IT-cleared app installation. Supplemented by outbound to Zello's known professional user communities (trucking forums, construction subreddits, field service LinkedIn groups) where dissatisfaction with Zello's lack of enterprise features is documented in public reviews.

**Pricing strategy:** $8/user/month (annual) or $10/user/month (monthly), with a 14-day free trial and a free tier capped at 3 users and 30-day log retention. This undercuts Motorola WAVE PTX ($15–30/user/month) by 50–75% while positioning above Zello's freemium floor. The price point is justified by the transcription and workflow integration features, which have direct operational ROI (reduced incident response time, compliance documentation). No advertising revenue model — the structural failure of TiKL's monetization is avoided by design.

**Differentiation vs. 2026 competitors:** WAVE PTX requires hardware bundles and enterprise contracts. Zello lacks workflow integrations and searchable logs. Teams Walkie Talkie requires full Microsoft licensing. The rebuild is the only self-serve, integration-native PTT tool priced for SMB operations teams — a positioning that none of the current competitors can occupy without cannibalizing their existing revenue models.
