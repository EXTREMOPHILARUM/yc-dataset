# Build Plan: Cardinal 2026

## Overview

Cardinal was an AI-powered product backlog platform that aggregated customer feedback, CRM data, and call recordings to quantify feature demand by revenue opportunity; founded in January 2023, it was acquired by Miro in May 2024 and rebranded as Miro Insights — a textbook platform absorption of a well-executed point solution by a larger platform with superior distribution.

The rebuild thesis is not that Cardinal failed — it didn't — but that its acquisition created a structural gap: Miro Insights serves Miro's installed base, leaving every product team running on Linear, Figma, or Jira-native workflows without a standalone AI product intelligence layer. Foundation models available in 2025–2026 have collapsed the unit economics that made this category expensive to build, and the validated workflow Miro Insights now runs in production — sales call → AI extraction → PRD matching → revenue signal — can be rebuilt as a platform-agnostic product targeting the teams Miro cannot reach without asking them to switch collaboration tools.

---34:T9a1,

## Why Now?

## Current Market Analysis

**Market size:** The product management software market was approximately $3.5 billion in 2023 (Grand View Research). A 2026 figure is not available in the public record, but the category has grown consistently at double-digit rates. The more relevant sizing is the addressable segment: B2B software companies with active sales motions, a product team of 3+ PMs, and existing Gong or Chorus deployments. This is a narrower but higher-willingness-to-pay segment than the total PM tools market.

## Competition map:

- **Productboard** is the incumbent with the largest installed base and reported $100M+ ARR. Its weakness, confirmed by at least one Cardinal user review in the research record, is that it struggles to scale gracefully with thousands of feedback items across many teams. Its AI features, added in 2023–2024, are bolt-ons to a workflow built before LLMs existed — the data model is not AI-native. Productboard also lacks deep call transcript integration; its feedback ingestion is primarily manual or form-based.
- **Miro Insights** is the most direct functional analog, but it is structurally limited to Miro's installed base. Teams running Linear, Jira, or Notion as their primary workflow will not adopt Miro as a collaboration layer to access product intelligence. This is the gap.
- **Aha!** targets enterprise roadmapping with a broad feature set but is widely perceived as heavyweight and expensive. Its AI features are nascent. It does not compete on the revenue-quantification-from-calls workflow.
- **Jira Product Discovery** (Atlassian) is the most dangerous incumbent for Jira-native teams. It has distribution, but its AI features as of early 2026 are limited to basic summarization, not revenue-signal extraction from call recordings. Atlassian's product velocity in AI has been slower than its distribution advantage would suggest.

**Demand signals from adjacent products:** Gong's App Directory lists Miro Insights as an integration, confirming that sales-call-to-product-backlog is a workflow enterprise buyers are actively seeking. Fireflies.ai and Chorus (ZoomInfo) have both grown their installed bases significantly, creating a larger pool of teams with structured call recording data that a Cardinal rebuild could tap.

**Defensibility analysis:** The honest answer is that platform absorption risk remains real. Atlassian could add revenue-quantified prioritization to Jira Product Discovery; Linear could build it natively. The structural defense is not technical moat — it is workflow depth and multi-platform neutrality. A rebuild that integrates simultaneously with Gong, Chorus, Fireflies, Linear, Jira, and Notion occupies a position that no single platform can replicate without creating competitive conflicts with its own ecosystem partners. Miro cannot deeply integrate with Figma's competitor tools; Atlassian cannot neutrally serve Linear teams. Platform-agnostic depth is the defensible position, and it requires staying independent long enough to build it. This is a real but narrow moat, and the plan should be honest that a well-resourced Atlassian move into this space would be a serious threat.

---

## Recommended MVP

## Feature 1: Multi-source call transcript ingestion with revenue tagging

Connect to Gong, Chorus, and Fireflies simultaneously via their published APIs, extract structured feature requests using GPT-4o or Claude 3.5 Sonnet, and tag each request with the associated customer's ARR pulled from a connected CRM (HubSpot or Salesforce). This is the core workflow Miro Insights runs in production, but the rebuild does it across all three major call recorders simultaneously — a multi-platform approach Miro cannot pursue due to competitive positioning. Unlike Cardinal's 2023 version, the AI extraction requires no fine-tuning; foundation model APIs handle it at near-zero marginal cost.

## Feature 2: Revenue-weighted feature backlog with Linear and Jira sync

Surface a ranked backlog where each feature cluster shows total ARR requesting it, number of accounts, and representative quotes. Sync confirmed features bidirectionally to Linear issues or Jira tickets via their public APIs. This is the prioritization output Cardinal built, but delivered as a native integration into the tools product teams already use as their system of record — not as a replacement primary tool. The original Cardinal required PMs to work inside Cardinal; the rebuild pushes output into wherever PMs already work.

## Feature 3: Slack-native weekly digest

Deliver a weekly summary of the top revenue-weighted feature requests to a designated Slack channel, with one-click routing to the backlog. This addresses the adoption problem Cardinal faced: PMs who don't open a new tool daily still receive the signal. It also creates a viral loop — sales and CS teams see the digest and begin tagging their own calls.

**What we will NOT build:** A visual collaboration layer, a PRD editor, a strategy framework tool, or any feature that competes with Miro, Notion, or Figma. The rebuild is an intelligence layer, not a workspace replacement.

**Success metrics:** 25 paying teams within 90 days of launch; average weekly active usage by at least 2 PMs per team; 60-day retention above 70%; at least one customer citing a specific roadmap decision driven by the revenue signal within 30 days of onboarding.

**Cold-start problem:** This product does not depend on network effects or local density. Value is delivered to a single team from day one, as long as that team has at least one connected call recorder with 30+ calls in the last 90 days. The minimum viable data threshold is low, and the onboarding flow should surface this threshold explicitly during signup to prevent teams from connecting an empty account and churning before seeing value.

---37:Taca,

## Go-to-Market Strategy
