# Build Plan: Brevy 2026

## Overview

Brevy was a San Francisco-based B2B software startup that cycled through at least four unrelated products — a bug-reporting Chrome extension, an AI customer support chatbot, content marketing services, and a Medicaid caregiving tool — between its YC S20 founding in July 2020 and its quiet dissolution in 2024, never publicly disclosing a single paying customer or revenue figure across four years of operation.

The rebuild thesis centers on Brevy Care, the company's final and most structurally interesting pivot: a self-serve tool that helps family caregivers navigate Medicaid HCBS waiver eligibility and reimbursement. What killed the original wasn't the idea — it was the team's lack of domain relationships, regulatory literacy, and runway to develop them. In 2026, multimodal LLMs can parse state-specific Medicaid waiver rules and auto-populate applications at near-caseworker accuracy, and a growing network of caregiver advocacy organizations provides a distribution channel the original team never had. The rebuild is a vertical AI agent for family caregivers: a TurboTax-style guided workflow that turns a 90-day bureaucratic ordeal into a 20-minute self-serve process.

---34:T89e,

## Why Now?

## The single most important change: LLMs can now reliably parse and reason over state-specific Medicaid regulatory text.

## Current Market Analysis

## Market Size

The addressable market for Medicaid caregiver navigation is large but requires careful scoping. Medicaid total expenditure exceeded $800 billion in 2023 (CMS data), with HCBS representing the fastest-growing segment — over $120 billion in 2022, up from $84 billion in 2019 (KFF Health Policy data). The relevant addressable market for a navigation product is not total Medicaid spend but the population of eligible-but-unenrolled family caregivers: AARP estimates that fewer than 15% of eligible caregivers successfully access HCBS reimbursement programs, suggesting a large latent demand pool. Specific TAM figures for caregiver navigation software do not appear in public databases; this is a gap the rebuild team should address through primary research with AAA directors.

## Competition Map and Gaps

Current competitors fall into three categories, each with specific weaknesses:

- **Wellthy** (founded 2015, raised ~$30M): Offers human care coordinators paired with a software platform, targeting employer benefits programs. Weakness: high cost per user (employer-subsidized, not self-serve), no Medicaid-specific workflow, inaccessible to caregivers whose employers don't offer it as a benefit.
- **Papa** (founded 2017, raised ~$240M): Connects older adults with "Papa Pals" for companionship and assistance. Weakness: service delivery model, not a navigation tool; does not address Medicaid application complexity.
- **Transcarent** (founded 2020, raised ~$200M): Employer-facing health navigation platform. Weakness: enterprise sales motion, no consumer or Medicaid-specific product.
- **State Medicaid agency portals**: Uniformly poor UX, no guided eligibility assessment, no cross-state functionality.

The gap is a self-serve, consumer-priced Medicaid HCBS navigation tool with state-specific waiver intelligence — a product none of the above competitors offer.36:T95c,

## Defensibility Against Platform Incumbents

The honest answer is that Google, Apple, and Amazon are not structurally positioned to build this product. Medicaid navigation requires state-specific regulatory data pipelines, relationships with AAAs and advocacy organizations, and compliance with HIPAA and state data-sharing agreements — none of which are adjacent to the core competencies of consumer tech platforms. The more realistic platform risk is from healthcare incumbents (UnitedHealth's Optum, CVS Health's Aetna) expanding into navigation services. These companies have regulatory relationships but historically poor consumer UX and no incentive to make Medicaid navigation self-serve (it competes with their managed care revenue). This is a genuine but manageable risk, not an immediate threat to a seed-stage product.

---

## Recommended MVP

## Core Features

## State-Specific Eligibility Assessment Engine

A conversational intake flow (10–15 questions) that ingests caregiver and care-recipient information and produces a plain-language eligibility assessment for the relevant HCBS waiver programs in the user's state. Powered by a retrieval-augmented generation (RAG) pipeline over state waiver manuals, updated quarterly. Unlike Brevy's original undifferentiated chatbot, this is a narrow, high-stakes workflow where accuracy is the product — not a general-purpose assistant. Success requires 90%+ accuracy on eligibility determinations validated against caseworker outcomes; this threshold must be established in closed beta before public launch.

## Guided Application Packet Generator

Once eligibility is confirmed, the product auto-populates the required state application forms using information collected during intake, generates a supporting documentation checklist, and produces a submission-ready PDF packet. This is the core value delivery: turning a 90-day ordeal into a 20-minute session. The original Brevy Care had no documented equivalent; this feature is the primary reason the unit economics of a self-serve product are now viable where they were not in 2023.

## Status Tracking and Follow-Up Prompts

A lightweight case management layer that tracks application submission dates, prompts users at key follow-up intervals (30, 60, 90 days), and surfaces state-specific appeal language if an application is denied. This addresses the post-submission abandonment problem — most caregiver navigation tools stop at submission, leaving users without support during the review period.

## What We Will NOT Build

No human care coordinator marketplace. No employer benefits integration. No general-purpose caregiver resource directory. No multi-condition health navigation outside Medicaid HCBS. Scope discipline is the primary lesson from Brevy's history.

## Cold-Start and Network Effects

This product does not depend on network effects or local density. Value is delivered to a single user on first use. The cold-start problem is a data pipeline problem, not a user density problem: the product requires accurate, current waiver data for at least 5 states before launch. Begin with the 5 states with the highest HCBS enrollment (California, New York, Texas, Florida, Pennsylvania — enrollment data available via CMS HCBS Scorecard).

## Success Metrics

- 500 completed eligibility assessments within 90 days of launch
- 40%+ conversion from assessment to application packet generation
- 70%+ user-reported accuracy on eligibility determinations (validated via follow-up survey)
- First 10 paying customers within 60 days of public launch

---

## Go-to-Market Strategy

## Target Customer Segment

Primary: Adult children (ages 40–60) who have recently taken on caregiving responsibility for an aging parent and are navigating Medicaid for the first time. This segment is digitally literate, time-constrained, and motivated by a specific acute event (a parent's health crisis or care transition) — the same trigger that drives TurboTax adoption. They are not professional caregivers and have no existing relationship with Medicaid caseworkers.

## Primary Distribution Channel

Partnership with Area Agencies on Aging (AAAs). The 600+ AAAs funded under the Older Americans Act are actively seeking digital tools to extend their capacity; they are trusted by the target segment and have no competing product. The go-to-market motion is a referral agreement: AAA staff refer newly identified caregivers to the product as a self-serve complement to their existing services. This is not a sales channel that requires enterprise contracts — most AAAs can approve a referral partnership at the program director level. Target 10 AAA partnerships in the first 5 launch states within 6 months.

## Pricing Strategy

One-time fee of $149 per application packet, with a free eligibility assessment. This mirrors TurboTax's model: the assessment (analogous to TurboTax's free federal return estimate) is free to drive top-of-funnel volume; the application packet (the actual work product) is the paid deliverable.

Stress-test against free alternatives: The free alternative is a Medicaid caseworker (free but 6–12 week wait times and limited availability) or a Medicaid planning attorney ($200–$500/hour). A $149 one-time fee is defensible against both. The free alternative is not worse in price — it is worse in speed and accessibility. The pricing must be justified on time savings, not feature superiority. A caregiver who waits 8 weeks for a caseworker appointment and then submits an incomplete application is the target customer; $149 to avoid that outcome is a straightforward value proposition.

## Differentiation vs. 2026 Competitors

Wellthy and Transcarent are employer-benefit products with human-in-the-loop models and price points ($500+/year) that exclude self-paying consumers. The rebuild's differentiation is consumer pricing, self-serve access, and state-specific accuracy — not breadth of services. The product does one thing (Medicaid HCBS navigation) better than any alternative available to a family caregiver without employer benefits or attorney access.
