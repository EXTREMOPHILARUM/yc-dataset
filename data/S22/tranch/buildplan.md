# Build Plan: Tranch 2026

## Overview

Tranch was a B2B invoice payments platform founded in 2021 by Philip Kelvin and Beau Allison that raised ~$104M, narrowed from broad B2B BNPL into legal-sector invoice payments, and was acquired by Elite — the dominant financial management software for large law firms — on January 3, 2025, at an undisclosed price after tripling payment volume in 2024.

The acquisition validated the vertical-specific invoice payments thesis so completely that it created a new gap: Elite's enterprise focus on Am Law 200 firms almost certainly leaves mid-market law firms ($5M–$50M revenue, roughly Am Law 201–600 and regional firms) without a purpose-built payments solution. The rebuild is not a copy of Tranch — it is the version of Tranch that Elite cannot afford to build, priced and distributed for the firms too small for Elite's sales motion but too large for generic payment processors to serve well. Think Tranch for the long tail of law: a modern invoice-to-payment platform with embedded BNPL, real-time rails, and LLM-powered AR automation, sold directly into the Clio and MyCase ecosystems where mid-market firms already live.

---

## Why Now?

### The single most important change: Elite's acquisition of Tranch has structurally orphaned the mid-market.

Elite's software is priced and architected for Am Law 200 firms — organizations with $150M+ in annual revenue, dedicated IT departments, and multi-year software contracts. The acquisition of Tranch accelerates Elite's roadmap for that segment, but it does not solve the problem for the 2,000+ US law firms with $5M–$50M in revenue that run on Clio, MyCase, or PracticePanther. These firms have the same invoice payment friction — large client bills, check-dominated settlement, no embedded financing options — but no purpose-built solution now that Tranch is inside an enterprise platform they cannot access or afford.

**Real-time payment infrastructure is now table-stakes, not a differentiator to build around.** FedNow launched in July 2023 and, combined with The Clearing House's RTP network, now covers the majority of US bank accounts. Tranch had to negotiate JP Morgan infrastructure partnerships to access these rails; a 2026 entrant can access FedNow-connected APIs through middleware providers like Moov, Unit, or Treasury Prime without a direct bank partnership. This reduces time-to-market for the Pay Now equivalent from 12+ months to weeks.

**Open banking underwriting is now cheap and fast.** Plaid, MX, and Finicity cover 95%+ of US financial institutions with standardized APIs (Plaid's coverage figure, per their 2023 developer documentation). In 2021, assembling the open banking data layer Tranch used for creditworthiness assessment required custom integrations. In 2026, it is a commodity API call. This directly lowers the cost of replicating Tranch's differentiated underwriting model.

**LLMs can now parse legal billing formats automatically.** GPT-4 (March 2023) and Claude 3 (March 2024) can extract structured data from LEDES-format invoices and PDF bills with high accuracy — a capability that did not exist at Tranch's founding. Tranch's AR automation required engineering effort to build; a 2026 rebuild can implement invoice ingestion in weeks using off-the-shelf model APIs, meaningfully reducing the headcount required to operate the product.

**The mid-market legal software market has consolidated around Clio.** Clio reached a $900M+ valuation and serves 150,000+ legal professionals (per Clio's 2023 State of Legal Technology report). Its App Marketplace is the primary distribution channel for legal tech add-ons targeting mid-market firms — a direct analog to the Shopify App Store for legal software. This distribution channel did not exist at meaningful scale in 2021.

---

## Current Market Analysis

**Market size:** The Am Law 200 firms collectively generate over $150B in annual revenue, per the research report. The broader universe of US law firms with $5M–$50M in revenue is harder to size precisely — this data is not publicly available in aggregate — but the Am Law 201–600 segment alone generates tens of billions in annual billings. Even at a 1% blended take rate on payment volume processed, the addressable revenue in this segment is in the hundreds of millions annually. The B2B payments market broadly exceeds $25 trillion in annual US flows, with legal services representing a meaningful slice given average invoice sizes.

## Competition map:

- **Tranch (now within Elite):** The most direct competitor, but now structurally inaccessible to mid-market firms. Elite's sales motion targets Am Law 200; its pricing and implementation complexity exclude smaller firms. This is the gap.
- **LawPay (AffiniPay):** The dominant payment processor for law firms, with 150,000+ users. LawPay handles card payments and ACH but offers no embedded financing, no BNPL, and no AR automation. Its weakness is that it is a payment terminal, not a payments platform — it processes transactions but does not help firms get paid faster or offer clients flexible terms.
- **Clio Payments:** Clio's native payment feature handles basic card and ACH collection but has no credit extension capability and limited AR workflow automation. Its weakness is depth — it is a convenience feature, not a standalone payments product.
- **Resolve and Behalf:** B2B BNPL players focused on eCommerce and smaller ticket sizes ($1K–$25K). Neither has legal vertical focus, legal billing software integrations, or underwriting models calibrated to law firm client creditworthiness. Per the research report, these players have struggled as the B2B BNPL market bifurcated post-2022.
- **Stripe:** Could theoretically serve law firms but has no legal billing workflow integration, no LEDES invoice parsing, and no credit extension product. Stripe's legal vertical presence is minimal.

**Demand signals:** Clio's 2023 Legal Trends Report found that 44% of legal clients prefer to pay in installments when given the option — a direct demand signal for embedded BNPL in legal billing. LawPay's dominance despite its feature limitations confirms that law firms are willing to adopt purpose-built payment tools; the gap is financing and automation, not payment acceptance itself.

**Defensibility:** Elite/Tranch will not rebuild downmarket. PE-backed enterprise software companies (TPG acquired Elite's majority in 2023) optimize for revenue per customer, not market breadth. The mid-market requires a different sales motion, different pricing, and different integrations (Clio, not Elite). This is a structural, not temporary, gap.

---

## Recommended MVP

### Core features:

**1. Embedded Pay Later for Clio and MyCase (the anchor feature).** The product allows law firms to offer clients installment payment plans on invoices from $5,000 to $150,000, directly within their existing billing software workflow. The firm receives full payment immediately from the platform; the client repays in 3–12 monthly installments. This differs from Tranch's original product in two ways: it targets smaller invoice sizes appropriate for mid-market firms, and it is distributed through Clio's App Marketplace rather than through a direct enterprise sales motion — reducing customer acquisition cost dramatically. Network effects are not required for this feature to deliver value to the first firm that installs it; each firm's benefit is independent of other firms' adoption.

**2. LLM-Powered Invoice Ingestion and AR Automation.** Using GPT-4o or Claude 3.5 Sonnet APIs, the platform automatically parses LEDES-format and PDF invoices uploaded by billing staff, extracts matter numbers, client identifiers, and amounts, and routes them to the correct payment workflow without manual data entry. This directly addresses the AR automation gap that Tranch built with significant engineering effort; in 2026 it can be implemented in weeks. It differs from Tranch's version in that it handles unstructured PDF bills — the format most common in mid-market firms that lack LEDES-compliant billing software.

**3. Real-Time Pay Now via FedNow Rails.** Clients who want to pay immediately can do so via FedNow-connected instant transfer, settling to the firm's account within seconds rather than the 2–3 business days of standard ACH. Implemented via Moov or Treasury Prime APIs rather than direct bank partnerships. This differs from Tranch's Pay Now in that it requires no JP Morgan partnership negotiation — it is available as a commodity API integration from day one.

**What you will NOT build in MVP:** Pay by Card (LawPay already handles this well; competing on card acceptance is a commodity fight), multi-currency international payments, or any product targeting Am Law 200 firms (Elite's territory, not yours).

**Success metrics:** 50 law firms processing payment volume within 90 days of Clio App Marketplace launch; $5M in cumulative invoice volume processed within 6 months; Pay Later attachment rate of 15%+ on eligible invoices (invoices >$5,000 where the client is offered the option); credit loss rate below 2% of Pay Later volume.

**Cold-start:** This product has no network effects. Each law firm's value is independent. The cold-start problem does not apply.

---

## Go-to-Market Strategy

**Target customer:** US law firms with $5M–$50M in annual revenue running Clio or MyCase as their practice management software. This is a narrow, reachable segment: Clio alone serves 150,000+ legal professionals, and its App Marketplace surfaces add-ons directly to this audience. The billing administrator or managing partner at a 10–50 attorney firm is the buyer; they are already in Clio daily.

**Primary distribution channel:** Clio App Marketplace, with a secondary presence on MyCase's integration directory. Clio's marketplace model means the product is discoverable by the exact target customer without a direct sales team. Tactics: (1) launch as a featured integration at Clio's annual conference (ClioCon, typically October); (2) pursue a co-marketing agreement with Clio similar to LawPay's embedded status — Clio has commercial incentive to offer its users a financing option it does not currently provide natively; (3) target Clio's partner newsletter and legal tech press (Above the Law, LawNext) for launch coverage.

**Pricing:** Transaction-based, not subscription. Pay Later: 1.5%–3% per month on outstanding balance, calibrated to client creditworthiness via open banking data — consistent with Tranch's disclosed pricing floor of 1% per month, adjusted upward for the smaller-firm, smaller-invoice context where underwriting cost per dollar is higher. Pay Now: 0.5% of invoice value, flat. No monthly SaaS fee for the law firm; the firm pays nothing unless clients use the product. This is critical for the stress-test: law firms currently accomplish payment collection via LawPay (card fees of ~2.9% + $0.30) or ACH (near-zero cost). The Pay Later product is not competing with free — it is competing with the firm not getting paid at all, or waiting 60–90 days. The value proposition is acceleration and conversion, not cost reduction. Firms that offer Pay Later should see higher invoice collection rates and shorter days-sales-outstanding; if they do not, the product fails on its own merits regardless of price.

**Differentiation vs. 2026 competitors:** LawPay offers no financing. Clio Payments offers no financing. Elite/Tranch does not serve this segment. Resolve and Behalf have no legal vertical integration. The rebuild's differentiation is the combination of legal-workflow-native distribution (Clio marketplace), embedded BNPL at mid-market invoice sizes, and LLM-powered invoice parsing that eliminates the manual data entry that would otherwise make adoption too operationally burdensome for a 15-attorney firm with one billing administrator.
