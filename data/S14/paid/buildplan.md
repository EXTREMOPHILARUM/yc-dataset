# Build Plan: Paid 2026

## Overview

Paid (later Paid Labs) was a Y Combinator S14 company that built a developer-first API for automating the full accounts receivable lifecycle — invoicing, payment collection, reminders, and reconciliation — before being acquired by Auction Mobility in January 2019 after failing to achieve meaningful scale against Stripe, QuickBooks, and FreshBooks, which absorbed the same functionality at zero marginal cost to their existing customers.

The rebuild thesis is not to fight Stripe again on horizontal ground — it is to go vertical and go deeper. Three structural changes make this viable in 2026: LLMs can now deliver on the "autopilot" promise that was technically impossible in 2014, FedNow and RTP have eliminated the settlement lag that made net-terms invoicing painful, and Stripe Connect has commoditized payment rails to the point where a vertical AR layer built on top of it is defensible rather than redundant. The new Paid is an AI-native AR automation platform for professional services firms — agencies, consultancies, and law firms — billing on complex net-30/60 terms, where Stripe Invoicing is genuinely inadequate and the pain is acute enough to pay for a solution.

---34:T89a,

## Why Now?

The single most important change since Paid's failure is that the "autopilot for AR" promise is now technically achievable at low marginal cost. In 2014, automating invoice follow-up, payment matching, and reconciliation required brittle rule-based logic and significant human oversight. In 2026, GPT-4o (May 2024) and its successors can parse unstructured payment confirmations from bank statements, draft contextually appropriate dunning emails that adapt tone based on relationship history, and extract billing terms directly from uploaded contracts — eliminating the manual setup that made horizontal AR tools high-churn in the first place.

The second structural change is payment rail modernization. The RTP network launched in 2017 and FedNow launched in July 2023, together enabling instant B2B settlement for the first time in U.S. history. In 2014, ACH settlement took 1–3 business days, which meant AR automation tools were managing float and reconciliation lag as much as they were managing invoices. Today, a professional services firm on net-30 terms can receive payment the moment a client approves an invoice — and the AR automation layer can confirm and reconcile that payment in real time. This materially improves the value proposition.

The third change is distribution infrastructure. Stripe Connect, now serving millions of platform businesses, allows a vertical AR tool to embed payment processing without becoming a payment processor — reducing infrastructure cost to near-zero compared to Paid's 2014 stack. The QuickBooks App Store lists over 750 integrated apps with access to millions of small business customers; the Xero App Store similarly reaches 3.7 million subscribers globally (Xero, FY2024 annual report). These are distribution channels that did not exist in a meaningful form for Paid.

Market validation has also arrived: Modern Treasury raised a $185 million Series C in 2022 at a reported $2 billion valuation (TechCrunch, November 2022), proving that institutional capital will fund B2B payment operations infrastructure when the workflow focus is tight enough. Paid could not demonstrate that signal in 2014–2019. The category is now validated.

---

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

### Feature 1: Contract-to-Invoice Extraction

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

**Target customer:** Independent professional services firms with 5–50 employees, billing $500K–$5M annually on net-30/60 terms — specifically digital agencies, management consultancies, and boutique law firms. This segment is large enough to support a scalable business, specific enough to build a focused product, and underserved enough that the pain is acute. They are not locked into Stripe Invoicing (most use it reluctantly) and are not large enough to justify a Bill.com enterprise contract.

**Primary distribution channel:** Content-led SEO targeting "invoice automation for agencies," "AR automation for consultants," and "net-30 invoice follow-up software" — terms with meaningful search volume and low competition from enterprise vendors. Supplemented by direct outreach through agency communities: Indie Hackers, Bureau of Digital, and the Slack communities associated with tools like Notion, Linear, and Figma (where the target customer already congregates). A QuickBooks App Store listing provides passive inbound from firms already searching for AR add-ons.

**Pricing:** $149/month flat for up to $500K in monthly invoice volume processed, scaling to $299/month for $500K–$2M. This is a subscription, not a transaction fee — deliberately avoiding the margin compression of the original Paid's likely transaction-fee model.

Stress test against free alternatives: A firm currently using Stripe Invoicing (free up to a point, then 0.4% per invoice) plus manual email follow-up is paying in time, not money. The $149/month price is justified if the product recovers one invoice per month that would otherwise have gone 30+ days overdue — at average invoice sizes of $10,000+, that is a 60x+ ROI. The price is not justified for firms with simple, transactional billing; those firms are not the target. Group chats and spreadsheets are the real free alternative for this segment, and the contract-to-invoice extraction feature is the specific capability that makes switching worthwhile.

**Differentiation vs. 2026 competitors:** Bill.com serves volume billing at scale; the rebuild serves relationship billing with complexity. Stripe Invoicing serves payment collection; the rebuild serves the full AR lifecycle including contract parsing and relationship-aware dunning. The positioning is "AR automation that understands your client relationships," not "invoicing software."
