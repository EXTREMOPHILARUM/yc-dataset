# Build Plan: RadMate AI 2026

## Overview

RadMate AI was a San Francisco-based YC W24 startup that built an AI copilot for radiologists — converting dictated findings into structured, proofread radiology reports — but collapsed before closing a single documented hospital contract, undone by a $500K pre-seed against 12–24 month enterprise sales cycles and a category leader, Rad AI, that had already locked up a third of all U.S. health systems before RadMate AI presented at Demo Day.

The rebuild thesis is not to fight Rad AI for health system contracts — it is to go underneath them. Rad AI's enterprise sales motion leaves an enormous, underserved long tail: the roughly 3,000+ independent radiology practices and teleradiology groups in the U.S. that lack the IT infrastructure, procurement bandwidth, or contract size to attract a vendor selling $110M+ worth of enterprise software. The new RadMate wins by selling a self-serve, API-native reporting copilot directly to individual radiologists and small practice owners — no procurement committee required.

---34:Ta59,

## Why Now?

**The single most important change since RadMate AI's failure is the commoditization of the core technical stack.** In 2023–2024, building a voice-to-structured-report pipeline required assembling and fine-tuning multiple specialized components — a speech recognition model, an NLP structuring layer, a template engine, and a proofreading module — each requiring dedicated engineering time and infrastructure investment. In 2026, that entire pipeline is available as commodity API infrastructure: OpenAI's Whisper handles medical dictation transcription at near-zero marginal cost, and GPT-4o (released May 2024) or Anthropic's Claude 3.5 Sonnet (released June 2024) can structure, format, and proofread a radiology report from raw dictation in a single model call. A working prototype that would have taken RadMate AI's two-person team months to build can now be assembled in weeks. This is not a marginal improvement — it eliminates the primary capital sink that made RadMate AI's $500K pre-seed structurally insufficient for reaching a deployable product.

**The market has been validated at scale.** Rad AI's $110M+ in cumulative funding and its penetration of 9 of the 10 largest U.S. radiology practices confirms that AI-generated radiology reports are not a speculative category — they are a proven, paying product. Rad AI's success is the rebuild's best market research.

**Procurement cycles are shortening for smaller buyers.** The rise of ambient clinical documentation tools — Abridge (raised $150M+ as of 2025), Nabla, and Suki — has educated hospital IT and practice administrators on AI workflow tools, reducing the "education tax" that first-movers paid. Crucially, independent radiology practices and teleradiology groups operate outside hospital procurement bureaucracy entirely: the decision-maker is often the practice owner or a managing radiologist who can approve a SaaS subscription without a legal review committee.

**Specific distribution channel now available:** Nuance PowerScribe (Microsoft) and Philips Intellispace are the dominant PACS-integrated dictation platforms, but neither offers a modern API marketplace. However, the FHIR-compliant EHR ecosystem — Epic's App Orchard (with 300+ integrated apps as of 2025) and athenahealth's Marketplace — now provides a documented integration pathway for smaller vendors that did not exist in a usable form in 2024. This is not a fast path, but it is a defined one.

**Market size data:** The global radiology AI market was approximately $2 billion in 2023; specific sizing for the independent practice sub-segment is not available in public sources.

---

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

### Core Feature 1: Voice-to-Report in One Click

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

**Target customer segment:** Independent radiologists and small radiology practices (1–10 radiologists) in the U.S., with a specific focus on teleradiology groups — radiologists who read studies remotely and are already accustomed to software-first workflows, have no hospital IT department gatekeeping their tool choices, and make purchasing decisions individually or as a small partnership. This segment is narrow enough to reach through direct channels and large enough to build a real business: there are thousands of teleradiology physicians in the U.S., and this data point is not precisely quantified in available sources.

**Primary distribution channel:** Direct-to-radiologist, community-led. The American College of Radiology's online communities, radiology-specific subreddits (r/Radiology has 100K+ members), and LinkedIn groups for teleradiologists are the primary acquisition channels. The tactic is a free trial with no credit card required — a radiologist uploads three dictations, gets three formatted reports, and experiences the value before any sales conversation. This is the opposite of RadMate AI's enterprise motion and is specifically designed to bypass the procurement cycle entirely.

**Pricing strategy:** $199/month per radiologist seat, with a 14-day free trial. Stress-test: the free alternative is Dragon Medical One's transcription layer (which does not generate structured reports) and manual formatting (which is what radiologists currently do). The $199 price is not competing against a free product that does the same thing — it is competing against 20–40 minutes of a radiologist's time per day spent on documentation. At a radiologist's effective hourly rate (median U.S. radiologist compensation is approximately $400K/year, or roughly $200/hour), recovering even 15 minutes per day is worth $500+/month in time value. The $199 price is deliberately set below the psychological threshold where a radiologist needs to justify the expense to a practice administrator. A group discount tier ($149/seat for 3+ seats) creates an incentive for practice-level adoption without requiring a formal procurement process.

**Differentiation vs. 2026 competitors:** Rad AI requires a procurement committee and a multi-month sales cycle. Nuance transcribes but does not structure. The rebuild's differentiation is self-serve deployment, usage-based trial, and a product experience built specifically for the independent radiologist — not the health system CIO.
