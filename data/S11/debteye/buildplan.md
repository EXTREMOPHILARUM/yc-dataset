# Build Plan: Debteye 2026

## Overview

Debteye was a YC Summer 2011 company that attempted to automate credit counseling for debt-distressed Americans, using Yodlee-powered bank aggregation to generate personalized debt resolution plans in seven minutes — but it collapsed because its "automation" stopped at the creditor's door, producing fax forms and phone scripts rather than completed transactions, and it could not sustain a subscription business against free tools or earn trust from vulnerable users at scale.

The rebuild thesis is straightforward: the CFPB's 2024 open banking rule (Section 1033) and modern embedded lending infrastructure have finally closed the creditor integration gap that killed Debteye, making it possible to build what the original team actually envisioned — a product that doesn't just diagnose debt but resolves it, either by submitting a machine-generated debt management plan directly to a participating creditor or by refinancing the debt in-app when negotiation fails.

---

## Why Now?

The single most important change since Debteye's failure is the arrival of a standardized, legally mandated creditor data interface. The CFPB's Section 1033 open banking rule, finalized in October 2024, requires covered financial institutions to expose consumer account data through standardized APIs by compliance deadlines beginning in 2026 for the largest banks. This is the IRS e-file equivalent that Debteye's TurboTax analogy always required but never had. The original product's automation ended at the creditor's door because no programmatic submission pathway existed; that structural blocker is now being dismantled by regulatory mandate.

Layered on top of this infrastructure shift are three enabling technologies that did not exist in 2011:

**Plaid, MX, and Finicity** (all reaching production-grade coverage between 2013 and 2018) have already normalized credential-free, OAuth-based bank connectivity for tens of millions of consumers. The trust barrier that TechCrunch flagged in July 2011 — "debt management is serious business, and Debteye is going to have to work hard to win users' trust" — has been substantially reduced by a decade of consumers sharing financial data with Robinhood, Venmo, and Cash App.

**GPT-4o with function calling** (released May 2024) enables dynamic, creditor-specific negotiation letters and settlement offers generated from a user's live debt profile, replacing Debteye's static pre-filled forms with adaptive communication that updates based on creditor responses in real time.

**Embedded lending infrastructure** — specifically Unit and Synctera (both reaching enterprise-grade compliance tooling by 2023) — allows a debt counseling platform to offer in-app refinancing as a fallback when negotiation fails, replicating in a single product the insight that took Debteye's founders two years and a full company pivot to discover at Avant.

On market demand: U.S. consumer debt reached $17.5 trillion in Q4 2024 (Federal Reserve), with credit card balances alone hitting a record $1.17 trillion. The debt relief services market is estimated at approximately $13 billion annually as of 2024 (IBISWorld; exact figure should be verified independently). The demand signal is unambiguous.

---

## Current Market Analysis

**Market size.** Debteye's 2011 Demo Day pitch cited a $2 billion addressable market for debt counseling and credit programs. The debt relief services market has grown substantially since then — IBISWorld estimates place it in the $11–14 billion range as of 2024, though this figure should be independently verified, as industry definitions vary. The broader population of Americans carrying problematic unsecured debt (credit cards, medical bills, personal loans) has expanded materially: credit card balances hit a record $1.17 trillion in Q4 2024 per the Federal Reserve, up from roughly $800 billion in 2011.

## Competition map.

- **Freedom Debt Relief / National Debt Relief** (the dominant debt settlement incumbents): charge 15–25% of enrolled debt as fees, require consumers to stop paying creditors and accumulate in escrow accounts, and carry significant regulatory risk under the FTC's Telemarketing Sales Rule. Their weakness is a predatory fee structure and a model that deliberately damages credit scores. They are also under increasing CFPB scrutiny following Regulation F (effective November 2021).

- **GreenPath / InCharge / NFCC-affiliated nonprofits**: legitimate, low-cost, but operationally analog. Intake is still largely phone-based; plan submission to creditors is manual or semi-automated. Their weakness is speed and UX — they are solving the right problem with 1990s infrastructure.

- **Tally** (shut down August 2024 after raising $172 million): the closest modern analog to the Debteye rebuild. Tally automated credit card debt management through a line of credit that paid down high-interest cards. It failed due to credit losses during the 2022–2023 rate environment, not because the product concept was wrong. Its shutdown is a direct demand signal and leaves a gap in the market.

- **Bright Money**: AI-driven debt payoff optimization, ~$14.99/month subscription. Weakness: still primarily a payment optimization tool, not a negotiation or settlement executor.

**Defensibility against platform incumbents.** This is the honest hard question. Apple (Wallet), Google (Pay), and Intuit (Mint's successor, Credit Karma) all have adjacent financial data products. Credit Karma in particular offers debt recommendations and has 130 million members. The structural answer is that debt *negotiation and settlement execution* — the actual creditor-facing workflow — is not something any of these platforms has built, because it requires regulatory licensing (credit counseling agency certification in most states), liability exposure for bad outcomes, and active creditor relationship management. These are not features a platform adds; they are compliance and operational commitments that create genuine moats. That said, if Credit Karma or Intuit chose to acquire an NFCC-affiliated agency and build this natively, the moat would narrow quickly. The rebuild must move fast enough to establish creditor relationships and a compliance infrastructure before that window closes.

---

## Recommended MVP

### Feature 1: Open Banking Debt Aggregation with Triage Scoring

Using Plaid (launched 2013, now covering 12,000+ institutions) and MX, the product pulls all unsecured debt balances, interest rates, and payment history automatically via OAuth — no credential sharing required. A triage algorithm classifies each debt by resolution pathway: self-managed payoff, debt management plan (DMP), settlement candidate, or refinance candidate. This replaces Debteye's Yodlee-powered analysis but adds a structured triage output rather than a binary settlement/DMP recommendation. The critical difference from the original: the triage output feeds directly into automated execution workflows rather than a form-generation layer.

## Feature 2: AI-Generated, Creditor-Specific Negotiation Packets

GPT-4o (May 2024) generates personalized settlement offer letters and DMP enrollment requests calibrated to each creditor's known acceptance patterns, the user's specific hardship profile, and current regulatory constraints. Unlike Debteye's static scripts, these packets update dynamically if a creditor counters. This is the product's core differentiation from both incumbent counseling agencies (which use standardized templates) and free tools (which offer no execution support at all).

## Feature 3: Programmatic DMP Submission to Section 1033-Compliant Creditors

For creditors covered under the CFPB's 2024 open banking rule, the platform submits DMP enrollment requests programmatically via API rather than by fax. This is the feature Debteye could not build. The MVP will be limited to the subset of creditors with compliant APIs by 2026 — realistically the largest 10–15 card issuers, which represent the majority of consumer credit card debt by volume. Fax/mail fallback remains for non-compliant creditors, but this is explicitly a transitional state, not the product's identity.

## Feature 4: In-App Refinancing Fallback (via Embedded Lending)

Using Unit or Synctera's banking-as-a-service infrastructure, users whose debt profiles qualify can receive an in-app personal loan offer to consolidate high-interest balances at a lower rate when negotiation is unlikely to succeed. This replicates the Avant insight — sometimes the right answer is a new creditor, not a negotiation — without requiring a separate company. This feature requires a lending license or a bank partner relationship; it should be scoped for Month 6+ of the MVP, not Day 1.

**What we will NOT build:** a financial education content library, a budgeting tracker, a credit score monitoring dashboard, or a general personal finance app. SpringCoin's pivot toward these features was a retreat from the hard problem. This product does one thing: resolve debt.

## Success metrics:

- 500 users with at least one debt account enrolled in an active resolution plan within 90 days of launch
- ≥40% of enrolled DMPs submitted programmatically (not by fax) within 6 months
- Net Promoter Score ≥50 among users who complete a resolution (not just sign up)
- Average time from account connection to first creditor contact: <24 hours (vs. Debteye's 7-minute analysis but multi-day execution)

**Cold-start note:** This product does not depend on network effects or local density. Value is delivered to a single user on Day 1 based on their own debt profile and creditor relationships. There is no minimum user threshold before the core feature delivers value.

---

## Go-to-Market Strategy

**Target customer segment.** The narrow initial target is millennials and Gen Z consumers (ages 28–40) carrying $10,000–$50,000 in unsecured credit card debt, with household incomes between $45,000 and $90,000 — too indebted to self-manage, too digitally native to trust a phone-based counseling agency, and too income-constrained to absorb the 15–25% fees charged by debt settlement firms. This is the same segment Tally served before its August 2024 shutdown, and Tally's 500,000+ user base represents a warm, unserved audience.

**Primary distribution channel.** Tally's shutdown is the single best distribution opportunity in the market. Tally users received shutdown notices in August 2024 and were left without a replacement product. A targeted acquisition campaign — Reddit communities (r/personalfinance, r/debtfree, both with 1M+ members), TikTok personal finance creators, and direct outreach to Tally's former user base via email lists if acquirable — can capture this displaced demand at low CAC before competitors fill the gap.

Secondary channel: B2B2C partnerships with NFCC-affiliated nonprofit counseling agencies, selling the programmatic submission infrastructure as a SaaS tool to agencies that already have creditor relationships and state licensing. This sidesteps the regulatory licensing burden for the direct-to-consumer product while building the creditor API relationships that make the consumer product defensible.

**Pricing.** $29/month subscription, with a 30-day free trial and a success-based fee option (1.5% of enrolled debt resolved, capped at $500) for users who prefer outcome-aligned pricing. The stress test: Bright Money charges $14.99/month for debt optimization without execution. The rebuild charges $29/month for actual creditor submission — a meaningfully different value proposition. Free alternatives (r/personalfinance advice, Credit Karma recommendations, NFCC's free counseling hotline) exist, but none execute on the user's behalf. The willingness-to-pay argument is that users in $20,000+ of credit card debt at 24% APR are paying $400/month in interest; $29/month for a product that actively reduces that balance is a straightforward ROI case, not a lifestyle subscription.

**Differentiation vs. 2026 competitors.** Freedom Debt Relief and National Debt Relief charge 15–25% of enrolled debt and damage credit scores by design. NFCC nonprofits are legitimate but slow and analog. Bright Money optimizes payments but does not negotiate. The rebuild is the only product that combines programmatic creditor submission (via Section 1033 APIs), AI-generated adaptive negotiation, and in-app refinancing in a single mobile-first flow — at a price point that is a rounding error relative to the debt it resolves.
