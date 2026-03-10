# Build Plan: Bifrost 2026

## Overview

Bifrost was a San Francisco-based YC W22 startup that built smart contract-based crypto estate planning tools — letting holders designate beneficiaries for self-custody wallets without exposing private keys — before going inactive in 2022–2023, killed by a 70% crypto market collapse, a double trust burden that a four-person startup couldn't overcome, and a fundraising window that closed at the worst possible moment.

The rebuild thesis is not to try again as a consumer product. Three things have changed that make a different version viable: ERC-4337 Account Abstraction has made programmable inheritance technically clean, SECURE 2.0 has made crypto estate planning a compliance obligation rather than an optional behavior, and the $140B+ lost-crypto narrative has created pull demand from financial advisors and estate attorneys who now need a tool to sell. The new version is a white-label B2B2C platform sold to exchanges, RIAs, and estate attorneys — not to crypto holders directly.

---

## Why Now?

The single most important change since Bifrost's failure is the arrival of ERC-4337 Account Abstraction, finalized on Ethereum mainnet in March 2023. This is not an incremental improvement — it is a structural replacement for the brittle multi-sig workarounds that would have defined Bifrost's original technical architecture. ERC-4337 enables programmable wallet recovery, time-locked transfers, and social recovery natively at the smart contract layer, without requiring users to manage multiple private keys or trust a startup to hold a co-signing key. The security model that Bifrost had to engineer around is now a protocol primitive. This eliminates the most significant technical liability in the original product and makes the inheritance trigger mechanism auditable, standardized, and interoperable across wallets.

The second structural change is regulatory. The SECURE 2.0 Act, signed in December 2022, and expanding IRS guidance on digital asset estate taxation have converted crypto inheritance from a voluntary planning behavior into an active compliance concern. Financial advisors and estate attorneys — who previously had no professional obligation to address client crypto holdings — now face liability exposure if they fail to account for digital assets in estate plans. This creates a B2B pull signal that did not exist in 2022: advisors are actively looking for tools, not passively waiting to be educated.

Third, the market has recovered. Bitcoin's return to all-time highs following the spot ETF approval in January 2024 (BlackRock's iShares Bitcoin Trust reached $10B AUM within weeks, per Bloomberg) has restored the psychological precondition for estate planning: users need to believe their assets will be worth something in twenty years before they'll plan around them. The Chainalysis estimate of $140B+ in permanently lost Bitcoin — a figure that was abstract in 2022 — has become a mainstream media narrative, meaning consumer awareness of the problem now exists without requiring Bifrost to build it from scratch.

Specific distribution channels available now that did not exist in usable form in 2022: the Coinbase Developer Platform (launched 2023) with API access to 100M+ verified accounts, and the emerging RIA fintech stack (Orion, Riskalyze/Nitrogen) through which advisor-facing tools can reach tens of thousands of credentialed financial planners in a single integration.

---

## Current Market Analysis

**Market size:** The global estate planning software market was valued at approximately $1.1B in 2023 and is projected to reach $2.1B by 2030 (Grand View Research — note: this figure covers traditional estate planning software broadly; a crypto-specific subset has not been formally sized). The more relevant proxy is the addressable population: Coinbase reported 110M verified users as of 2024, and Galaxy Digital estimated that approximately 50M Americans held crypto assets as of early 2024. If even 5% of that population — 2.5M people — would pay for a structured inheritance solution, the market is material. The conversion rate from "crypto holder" to "crypto estate planner" remains unvalidated; this is an honest unknown.

## Competition map:

- **Trust & Will / Willful / LegalZoom:** These incumbents have added crypto guidance to their document templates but offer no smart contract automation, no wallet integration, and no on-chain execution. Their weakness is that they solve the documentation problem, not the access problem — a beneficiary still needs the private key to actually claim assets.
- **Coinbase:** Has no formal inheritance product as of early 2025. Custodial beneficiary designation remains absent from their product surface despite being a single-sprint feature. Their weakness is organizational inertia and regulatory caution around anything that touches estate law.
- **Safe (formerly Gnosis Safe):** Offers multi-sig infrastructure that technically supports inheritance setups, but requires significant technical sophistication to configure and has no consumer-facing estate planning UX. Their weakness is that they are infrastructure, not a product.
- **Ledger:** Offers Ledger Recover (a seed phrase backup service) but no inheritance or beneficiary designation feature. Their weakness is that recovery and inheritance are different problems — Ledger Recover helps you recover your own wallet, not transfer it to someone else.

**Demand signals:** The growth of crypto tax software (CoinTracker, Koinly, TaxBit) demonstrates that crypto holders will pay for compliance-adjacent tools when there is a regulatory forcing function. SECURE 2.0 provides exactly that forcing function for estate planning.

**Defensibility analysis:** The original Bifrost was vulnerable to platform commoditization — Coinbase could add a beneficiary form and eliminate the core use case for custodial assets. The rebuild addresses this directly by targeting the self-custody and multi-platform layer (ERC-4337 wallets, hardware wallets, multi-chain holdings) that exchanges cannot absorb, and by selling to advisors rather than competing for the same end users as exchanges. The honest caveat: if Coinbase ships a native inheritance product, it will capture the custodial segment. The rebuild's defensibility depends on owning the self-custody and advisor-distribution layer, which Coinbase has structural reasons not to prioritize (regulatory complexity, liability exposure). That is a real but not guaranteed moat.

---

## Recommended MVP

## Feature 1: ERC-4337 Inheritance Module

A smart contract module built on Account Abstraction that allows a wallet owner to designate a beneficiary address and a time-lock condition (e.g., no wallet activity for 12 months triggers a claimable transfer). The beneficiary can initiate a claim after the inactivity window, which the owner can cancel at any time while alive. Unlike Bifrost's multi-sig approach, this requires no co-signing key held by the startup — the logic lives entirely on-chain. This eliminates the "trust a startup with your assets" problem that was structurally fatal to the original product.

## Feature 2: Advisor Dashboard

A white-label portal for estate attorneys and RIAs to onboard clients, view their connected wallet holdings, and generate a crypto asset schedule for inclusion in a traditional will. LLM-based document generation (Claude 3.5 or GPT-4o, both available as of 2024) auto-generates jurisdiction-specific legal language at near-zero marginal cost — solving the legal enforceability gap that would have required expensive attorney partnerships in 2022. This is the distribution wedge: advisors bring their existing client relationships; the product does not need to acquire consumers directly.

## Feature 3: Multi-Chain Wallet Aggregation

Read-only connection to Ethereum, Bitcoin (via PSBT-based time-lock scripts), Solana, and major EVM chains, giving advisors and users a unified view of crypto holdings across wallets. This is the data layer that makes the advisor dashboard useful and creates switching costs. Unlike Bifrost, which had undisclosed chain support, this version ships with explicit multi-chain coverage from day one.

**What you will NOT build:** A consumer mobile app, NFT-specific features, crypto tax filing, or any custodial product that requires holding user assets. Do not build a legal services marketplace. Stay in the infrastructure and tooling layer.

## Success metrics:

- 50 advisor or estate attorney accounts active within 6 months of launch
- 500 end-user inheritance modules deployed on-chain within 12 months
- $10,000 MRR within 12 months (advisor subscription tier)
- Zero smart contract security incidents (table-stakes threshold, not a growth metric)

**Cold-start note:** This product does not depend on network effects or local density. An advisor with one client using the platform delivers full value to that client. The cold-start problem does not apply in the traditional sense — but the advisor channel requires a minimum of 10–15 credible early adopters (estate attorneys willing to be named as references) before the sales motion becomes self-reinforcing. Recruit these through crypto-focused estate law firms and SECURE 2.0 compliance webinars before the product launches publicly.

---

## Go-to-Market Strategy

**Target customer segment:** Estate attorneys and RIAs (Registered Investment Advisors) with existing high-net-worth clients who hold $100,000+ in crypto assets. Specifically, advisors already using crypto tax tools (CoinTracker, TaxBit) or serving clients who have asked about digital asset inheritance — a segment that SECURE 2.0 has made newly urgent. This is narrow by design: do not target general financial planners or consumer crypto holders in year one.

**Primary distribution channel:** Direct outreach to estate law firms and RIA networks, followed by integration into the Orion and Nitrogen (formerly Riskalyze) advisor platforms, which collectively serve tens of thousands of credentialed advisors. Secondary channel: co-marketing with crypto tax software providers (CoinTracker, Koinly) who already have the advisor relationship and a natural upsell moment at tax season.

## Pricing strategy:

- Advisor seat license: $199/month per advisor, covering unlimited client modules up to 25 clients. Above 25 clients, $5/client/month.
- End-user direct (for self-custody holders without an advisor): $99/year flat.

Stress-test against free alternatives: A crypto holder can today write their seed phrase on paper and store it with a lawyer — free, but creates a permanent security vulnerability. They can use Safe's multi-sig — free, but requires technical configuration that most users cannot complete. They can do nothing — the actual dominant behavior. The $99/year price is justified not against these alternatives on features, but on the compliance and liability framing: advisors need a documented, auditable process for SECURE 2.0 compliance, and $199/month is below the cost of a single billable hour of estate attorney time. The consumer $99/year is harder to justify against "do nothing" — this tier should be deprioritized until advisor distribution is proven.

**Differentiation vs. 2026 competitors:** Trust & Will and LegalZoom offer documents, not execution. Coinbase offers custodial convenience, not self-custody coverage. Safe offers infrastructure, not advisor UX. The rebuild's differentiation is the combination of on-chain execution (ERC-4337), advisor-facing workflow tooling, and LLM-generated legal document output — no current competitor offers all three in a single product. The risk is that any of these incumbents could acquire or replicate individual components; the defensibility is in the integrated workflow and the advisor distribution relationships built in year one.
