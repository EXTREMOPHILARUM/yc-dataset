# Build Plan: RadMate AI 2026

## Overview

RadMate AI was a San Francisco-based YC W24 startup that built an AI copilot for radiologists — converting dictated findings into structured, proofread radiology reports — but collapsed before closing a single documented hospital contract, undone by a $500K pre-seed against 12–24 month enterprise sales cycles and a category leader, Rad AI, that had already locked up a third of all U.S. health systems before RadMate AI presented at Demo Day.

The rebuild thesis is not to fight Rad AI for health system contracts — it is to go underneath them. Rad AI's enterprise sales motion leaves an enormous, underserved long tail: the roughly 3,000+ independent radiology practices and teleradiology groups in the U.S. that lack the IT infrastructure, procurement bandwidth, or contract size to attract a vendor selling $110M+ worth of enterprise software. The new RadMate wins by selling a self-serve, API-native reporting copilot directly to individual radiologists and small practice owners — no procurement committee required.

---34:Ta59,

## Why Now?

## Current Market Analysis

**Market size and segment:** The global radiology AI market was valued at approximately $2 billion in 2023 and is projected to grow significantly through 2030, driven by imaging volume growth and a documented radiologist workforce shortage (the American College of Radiology has flagged radiologist supply constraints as a structural issue, though specific 2026 figures are not available in the research corpus). The independent radiology practice and teleradiology sub-segment — the rebuild's target — is not separately sized in available public data, but the U.S. alone has approximately 3,000+ independent radiology groups, representing a meaningful addressable market that Rad AI's enterprise motion structurally underserves.

## Competition map:

- **Rad AI** (the dominant incumbent): Serves 9 of 10 largest U.S. radiology practices and a third of all U.S. health systems. Its specific weakness is its sales motion — a $110M-funded enterprise vendor does not build self-serve onboarding, usage-based pricing, or a product experience optimized for a 3-radiologist independent practice. Its contracts are multi-year, high-ACV deals that require procurement committees. It is not competing for the radiologist who wants to try something today.
- **Nuance Dragon Medical One (Microsoft)**: Dominant in speech recognition across hospitals, with deep EHR integrations. Its weakness is that it is a dictation tool, not a report-generation tool — it transcribes what you say, it does not restructure, proofread, or reduce your word count. Microsoft has added some AI features, but the product remains fundamentally a transcription layer, not an LLM-native reporting copilot.
- **Philips Intellispace**: An enterprise PACS and reporting platform with AI features. Same weakness as Nuance — it is infrastructure-first, not workflow-first, and its AI additions are incremental rather than architecturally LLM-native.
- **Cerebriu, Smart Reporting, Agamon Health**: Smaller players with multi-million dollar raises and EHR integration depth. Their weakness is the same as Rad AI's at a smaller scale — enterprise sales motions, no self-serve, no usage-based pricing.

**Demand signals from adjacent products:** Abridge and Nabla have demonstrated that clinicians will pay for ambient AI documentation tools outside of hospital procurement — both have individual and small-practice pricing tiers. This is the strongest demand signal for the rebuild: the behavioral pattern of a clinician paying directly for an AI workflow tool is established.

**Defensibility analysis:** The honest answer is that Microsoft (via Nuance) is the most credible platform threat. Microsoft already owns the dominant dictation infrastructure in radiology and has the Azure OpenAI relationship to add LLM-native report generation natively. This is a real risk, not a dismissible one. The structural defense is speed and specialization: a focused radiology reporting copilot built for independent practices can iterate on template customization, specialty-specific language models, and radiologist UX in ways that a Microsoft product team managing a 10,000-hospital enterprise contract cannot prioritize. The rebuild must reach defensible distribution — a meaningful installed base of independent practices with customized templates and workflow integrations — before Microsoft ships a "good enough" version of this feature into Dragon Medical One. That window is real but finite, estimated at 18–30 months.

---

## Recommended MVP

## Core Feature 1: Voice-to-Report in One Click

A radiologist dictates findings in natural speech — abbreviated, informal, non-linear — and the system produces a formatted, proofread report in the radiologist's personal template within seconds, using GPT-4o or Claude 3.5 Sonnet as the structuring engine over Whisper transcription. This differs from the original RadMate AI in one critical way: it is delivered as a browser-based or lightweight desktop tool that requires zero EHR integration to start — a radiologist can paste the output into their existing reporting system. The original required integration to deliver value; this version delivers value on day one, before any integration is built.

## Core Feature 2: Personal Template Engine

The system learns each radiologist's preferred phrasing, report structure, and specialty-specific language from their first 10–20 reports, building a personal style model that makes output feel authored rather than generated. This matters because radiologists are deeply attached to their report voice — generic AI output is a rejection trigger. The original RadMate AI described template support but had no documented evidence of a learning system; this version makes personalization the primary retention mechanism.

## Core Feature 3: Error Flagging and Confidence Scoring

Before a report is finalized, the system flags potential clinical inconsistencies (e.g., a finding mentioned in dictation that does not appear in the structured report, or laterality conflicts) and surfaces them for radiologist review. This directly targets the >20% error rate the original founders identified. Unlike the original, this feature is explicitly positioned as a review assist — the radiologist confirms every flag — which keeps the product clearly outside FDA diagnostic AI classification.

**What we will NOT build in MVP:** EHR or PACS integration, DICOM image ingestion, multi-user practice management dashboards, billing or coding assistance, or any feature that requires a hospital IT security review to deploy. These are post-revenue features.

**Success metrics:** 50 paying radiologists within 90 days of launch; 70%+ week-4 retention; average report generation time under 45 seconds; net promoter score above 40 from active users.

**Cold-start problem:** This product does not depend on network effects or local density. A single radiologist gets full value from day one — the core loop is individual (dictate → structured report), not social. There is no cold-start threshold to clear.

---37:T9c3,

## Go-to-Market Strategy
