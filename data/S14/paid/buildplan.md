# Build Plan: Paid 2026

## Overview

Paid (later Paid Labs) was a Y Combinator S14 company that built a developer-first API for automating the full accounts receivable lifecycle — invoicing, payment collection, reminders, and reconciliation — before being acquired by Auction Mobility in January 2019 after failing to achieve meaningful scale against Stripe, QuickBooks, and FreshBooks, which absorbed the same functionality at zero marginal cost to their existing customers.

The rebuild thesis is not to fight Stripe again on horizontal ground — it is to go vertical and go deeper. Three structural changes make this viable in 2026: LLMs can now deliver on the "autopilot" promise that was technically impossible in 2014, FedNow and RTP have eliminated the settlement lag that made net-terms invoicing painful, and Stripe Connect has commoditized payment rails to the point where a vertical AR layer built on top of it is defensible rather than redundant. The new Paid is an AI-native AR automation platform for professional services firms — agencies, consultancies, and law firms — billing on complex net-30/60 terms, where Stripe Invoicing is genuinely inadequate and the pain is acute enough to pay for a solution.

---34:T89a,

## Why Now?

## Current Market Analysis

**Market size:** The global accounts receivable automation market was valued at approximately $3.0 billion in 2023 and is projected to reach $6.7 billion by 2030 at a CAGR of roughly 12% (Grand View Research, 2023). The professional services segment — agencies, consultancies, law firms, and accounting firms — represents a meaningful slice of this, though a precise sub-segment figure is not available in the public record. What is documented: U.S. professional services firms collectively manage an estimated $300+ billion in outstanding receivables at any given time (Federal Reserve Flow of Funds data), with average days sales outstanding (DSO) running 45–60 days against stated net-30 terms — a persistent, costly gap.

## Competition map:

- *Stripe Invoicing* — dominant for transactional billing but genuinely weak on complex professional services workflows: no native support for milestone billing, retainage, multi-party invoice splits, or contract-term extraction. Stripe's incentive is to serve the median use case, not the complex one.
- *QuickBooks / FreshBooks / Xero* — strong on bookkeeping integration but dashboard-first, not API-first, and their AR automation features (auto-reminders, payment matching) are rule-based with no LLM layer. Switching cost is high for existing users, but new professional services firms are not locked in.
- *Bill.com* — the closest current competitor; serves SMB AP/AR with $318M in revenue (FY2024). Its weakness is that it is built for volume-based, transactional billing rather than relationship-based, complex-terms billing. Its AI features as of 2025 are limited to basic categorization.
- *Harvest + Stripe* — popular among agencies for time tracking and invoicing, but reconciliation is manual and there is no dunning automation.
- *Modern Treasury* — validates the category but targets enterprise treasury operations ($10M+ ARR customers), not the professional services mid-market.

**Demand signals:** The rise of Deel, Remote, and Rippling in adjacent payroll/contractor payment workflows demonstrates that professional services firms will pay for automation that removes financial operations overhead. Notion's and Linear's success selling to agencies and consultancies confirms this segment's willingness to adopt new SaaS tools.

**Defensibility:** The honest answer is that Stripe could build this. The structural argument for why it won't: Stripe optimizes for payment volume and developer breadth, not for the workflow complexity of a 12-person law firm billing on retainer with milestone releases. The same logic that kept Stripe from building a full ERP keeps it from building deep professional services AR tooling. The rebuild's defensibility comes from vertical depth — contract parsing, relationship-aware dunning, retainage tracking — not from owning payment rails. If Stripe does build this, the exit is an acquisition, not a failure.

---

## Recommended MVP

## Feature 1: Contract-to-Invoice Extraction

Upload a signed engagement letter or SOW, and the system uses an LLM (GPT-4o or Claude 3.5 Sonnet, both available as of mid-2024) to extract billing terms — milestones, retainage percentages, net terms, and payment schedules — and auto-populate a draft invoice schedule. This directly addresses the manual setup problem that made the original Paid high-churn: the "30-minute integration" promise failed because configuring AR rules for complex billing relationships still required significant human effort. The new version eliminates that friction at the point of onboarding.

## Feature 2: Relationship-Aware Dunning Automation

Automated follow-up sequences for overdue invoices that adapt tone and timing based on client relationship history, invoice size, and days overdue — drafted by an LLM and reviewed by the user before sending. Unlike Stripe Invoicing's static reminder templates or QuickBooks' generic nudges, this produces emails that read as if a human wrote them for a specific client relationship. This is the feature most likely to drive word-of-mouth among professional services principals who currently write dunning emails manually.

## Feature 3: Real-Time Reconciliation via FedNow/RTP

Automatic matching of incoming payments to open invoices using bank feed integration (Plaid, available since 2013 but now with significantly broader bank coverage) and real-time payment confirmation via FedNow/RTP rails. Unmatched payments are flagged with LLM-generated match suggestions based on amount, date, and payer metadata. This was technically impossible for Paid in 2014 due to ACH lag; it is table-stakes infrastructure in 2026.

## Feature 4: Stripe Connect Embedded Payments

Payment acceptance via Stripe Connect, supporting ACH, card, and RTP — embedded in the invoice itself with no additional vendor relationship required for the end client. This is not novel, but it is necessary: the original Paid had to build multi-rail payment infrastructure from scratch. Using Stripe Connect reduces infrastructure cost to near-zero and eliminates a major build-vs-buy decision.

**What we will NOT build:** A general-purpose accounting platform, a time-tracking tool, a payroll product, or a mobile app in the MVP phase. No auction industry features. No enterprise treasury operations tooling.

**Success metrics:** 50 paying professional services firms within 6 months of launch; average invoice volume per customer of $50,000+/month; DSO reduction of 10+ days vs. customer baseline within 90 days of activation; monthly churn below 3%.

**Cold-start note:** This product does not depend on network effects or local density. Each customer derives full value from day one of their own integration. No minimum user threshold is required before the core feature delivers value.

---37:T962,

## Go-to-Market Strategy
