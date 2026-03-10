# Build Plan: Clear Genetics 2026

## Overview

By 2026, Clear Genetics rebuilds as the automation layer for mid-sized health systems expanding genomic testing faster than their counselor capacity can scale. The product is a conversational AI platform—web, SMS, and voice—that handles pre-test education, informed consent, insurance navigation, and results interpretation. It escalates only the 10–15% of cases requiring human judgment to a counselor queue with full context, freeing counselors to focus on complex families and rare variants instead of routine workflows.

The market shift is Invitae's bankruptcy collapse, which eliminated the dominant incumbent and left health systems with fragmented, outdated infrastructure. Simultaneously, LLM and voice AI matured enough in 2024 to make natural, compliant patient conversations viable at scale—something that wasn't possible in 2019.

The go-to-market targets genetics department heads at 500–2,000 bed systems already running high-volume testing programs. Distribution runs through direct sales and lab partnerships. Pricing ties to patient conversations processed, so revenue scales with the customer's testing volume. The win is simple: 3–5x faster patient throughput per counselor, lower cost per interaction, and zero regulatory friction because the AI never interprets variants—it only guides workflow.34:T94b,

## Why Now?

The single most important change since Clear Genetics' 2019 acquisition is the collapse of its acquirer. Invitae filed for bankruptcy in February 2023 and liquidated its assets, almost certainly deprecating or orphaning the Gia and Clinic Hub products. The workflow automation niche Clear Genetics built and validated—with named deployments at Geisinger and Huntsman Cancer Institute and 67,000 patients served at 92% satisfaction—now has no incumbent defending it. This is not a greenfield market; it is a proven market with a vacant throne.

The second transformative change is the capability leap in conversational AI. Gia's 2017–2019 architecture relied on rule-based NLP that could handle structured flows but broke down on ambiguous questions, emotional responses, and clinical edge cases. GPT-4 (March 2023) and Claude 3 (March 2024) can conduct genuinely nuanced, multi-turn clinical conversations—explaining variant pathogenicity, navigating insurance questions, and responding to patient anxiety—at a quality level that was technically impossible when Clear Genetics was operating. This directly removes the core limitation that constrained Gia's clinical scope.

Two regulatory changes further reduce friction that slowed the original company. The 21st Century Cures Act (2020) mandated FHIR R4 interoperability across certified EHR systems, replacing the custom integration work that would have consumed significant engineering resources in 2017–2019. A rebuilt platform can connect to Epic, Oracle Health, and athenahealth via standardized APIs on day one.

The genetic counselor shortage has intensified structurally. The US had approximately 5,000 certified genetic counselors in 2019; the American Board of Genetic Counseling projects demand will continue outpacing supply through the 2030s. Genomic testing volumes have grown dramatically—specific current figures are not available in the research record, but the directional trend is unambiguous and well-documented. The bottleneck Clear Genetics targeted is larger today than when the company was founded.

Additionally, voice AI (real-time speech-to-speech models, commercially available from ElevenLabs and OpenAI as of late 2024) now enables phone-based counseling automation, reaching elderly and low-literacy patients entirely outside the app-based chatbot paradigm Gia operated within.

---

## Current Market Analysis

## Market Size

The global clinical genomics market was valued at approximately $14.4 billion in 2022 and is projected to exceed $30 billion by 2030 (Grand View Research; specific figures should be independently verified). The patient engagement and workflow automation layer—where a rebuilt Clear Genetics would compete—is a subset of this market without a precise published size in the available research record. However, the structural driver is clear: every incremental genetic test ordered generates a pre-test education, consent, and post-test results communication workflow that currently requires genetic counselor time. Testing volume growth directly expands the addressable market for automation software.

## Competition Map and Gaps

The most significant competitive fact is what is absent. Invitae's bankruptcy eliminated the most credible incumbent. Nest Genomics (YC W22), founded by the original Clear Genetics founders, is the most directly relevant successor, but its current product scope and market position are not fully documented in the available research record—this should be investigated before committing to a rebuild, as it represents either the primary competitor or a potential partnership signal.

Current adjacent competitors include:
- **Fabric Health** and **Buoy Health**: General-purpose AI triage tools without genetics-specific clinical depth or counselor workflow integration.
- **Genome Medical**: A telehealth genetics service that deploys human genetic counselors remotely—a direct substitute for automation rather than a software platform, with cost structures that limit scalability.
- **Color Health**: Population genomics platform with some workflow tooling, but primarily focused on employer and health plan channels rather than health system clinical workflows.

The gap is specific: no current vendor combines LLM-powered patient conversation, FHIR-native EHR integration, and a clinician-side triage dashboard purpose-built for genetics workflows. That combination is the rebuild opportunity.36:T8c0,

## Demand Signals from Adjacent Products

The direct-to-consumer genomics market—23andMe (now in bankruptcy proceedings as of 2024) and AncestryDNA—has created tens of millions of consumers who have already engaged with genetic data and are actively seeking clinical interpretation. This pre-educated patient population represents both a demand signal and a potential distribution channel. The collapse of 23andMe specifically creates a population of consumers with existing genetic data and no current platform supporting them clinically.

---

## Recommended MVP

## Core Features

## LLM-Powered Patient Conversation Engine

A multi-turn conversational interface—deployable as web chat and SMS—that guides patients through pre-test education, informed consent, insurance navigation, and results interpretation for hereditary cancer, carrier screening, and cardiology indications. Unlike Gia's 2017 rule-based NLP, this engine uses GPT-4o or Claude 3.5 Sonnet fine-tuned on genetic counseling protocols co-developed with certified counselors, enabling genuine handling of ambiguous questions and emotional responses. The clinical scope is deliberately narrower than Gia's original five specialties—three indications at launch reduces validation complexity while covering the highest-volume use cases.

## Voice-Based Outreach Module

An automated phone call workflow using real-time voice AI (ElevenLabs or OpenAI Realtime API, both commercially available as of late 2024) for pre-test consent and post-results notification. This directly addresses the patient population—elderly, low-literacy, limited smartphone access—that text-based chatbots cannot reach, expanding the addressable patient population beyond what Clear Genetics served and differentiating from every current competitor.

## FHIR-Native Clinician Dashboard

A care management interface connecting via FHIR R4 APIs to Epic and Oracle Health, surfacing patient conversation summaries, consent status, and AI-generated triage flags that identify which patients require direct counselor attention. This replaces Clinic Hub's functionality with a modern integration architecture that eliminates the custom EHR integration work that would have consumed significant engineering resources in 2017–2019.

## Counselor Collaboration Layer

An asynchronous handoff workflow allowing the AI to escalate specific patient questions to a genetic counselor queue with full conversation context preserved. This maintains the "augmentation not replacement" framing that was central to Clear Genetics' clinical adoption strategy and directly addresses the professional resistance failure mode common in healthcare automation.

## What We Will NOT Build

- A diagnostic or variant interpretation engine (regulatory complexity, out of scope for workflow automation positioning)
- A direct-to-consumer product (enterprise B2B only at launch)
- Custom integrations for EHR systems outside Epic and Oracle Health in year one
- Proprietary genomic database or lab infrastructure

## Success Metrics

- 3 signed health system contracts within 12 months of launch
- 10,000 patient conversations completed with ≥85% completion rate
- Counselor time-per-patient reduced by ≥40% at pilot sites (measured against baseline)
- HIPAA audit passed; no reportable security incidents in year one

---

## Go-to-Market Strategy

## Target Customer Segment

The primary target is mid-sized integrated health systems (500–2,000 beds) with existing genetics programs that are actively expanding genomic testing volumes but cannot recruit sufficient genetic counselors to match. This segment is more accessible than Geisinger-scale systems (which have longer procurement cycles and more complex IT requirements) and more financially capable than small community hospitals. Specific indicators: systems that have launched or are planning hereditary cancer or cardiac genetics programs, have Epic or Oracle Health as their EHR, and have a genetics department head who can serve as internal champion.

## Primary Distribution Channel and Tactics

The primary channel is direct enterprise sales through genetics department heads and CMIOs, supplemented by partnerships with genetic testing laboratories (the same channel that made Invitae a customer-then-acquirer for Clear Genetics). The research record demonstrates that laboratory partnerships compress sales cycles: labs that order tests need patient communication infrastructure and will co-sell or refer a platform that solves their post-order workflow problem.

Secondary channel: the Epic App Orchard and Oracle Health Marketplace, both of which provide discovery access to health system IT buyers already evaluating Epic-integrated tools. This distribution channel did not exist in its current form during Clear Genetics' operating period.

Tactic: replicate Clear Genetics' strategy of targeting a marquee academic medical center as the first named customer—a single Geisinger-equivalent deployment generates the clinical credibility that compresses subsequent sales cycles from 18 months to 6.

## Pricing Strategy

Volume-based SaaS pricing tied to patient conversations processed, with a platform fee floor. This aligns revenue growth with the customer's testing volume growth—the same natural pricing structure the research record identifies for the original Clear Genetics model—and makes the ROI calculation straightforward: cost per automated patient interaction versus cost per genetic counselor hour (approximately $80–120/hour; specific current figures should be verified). Target entry contract: $150,000–$250,000 annually for a mid-sized health system processing 2,000–5,000 genetic consultations per year. Pricing should be validated against current market rates before launch.

## Differentiation vs. 2026 Competitors

Against Genome Medical: fully automated at a fraction of the per-patient cost, with no human counselor bottleneck limiting throughput. Against Fabric/Buoy: genetics-specific clinical depth, counselor co-development credibility, and FHIR-native EHR integration purpose-built for genetics workflows. Against Nest Genomics (if competing): the rebuild team's differentiation depends on what Nest Genomics has built—this competitive position requires direct research before committing. The core differentiation claim is the same one Clear Genetics proved: a platform built by people who have already deployed genetic workflow automation at population scale, now with LLM capabilities and interoperability infrastructure that did not exist in 2019.
