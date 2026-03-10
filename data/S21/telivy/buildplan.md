# Build Plan: Telivy 2026

## Overview

Telivy was a San Francisco-based cybersecurity startup founded in 2021 that attempted to automate cyber risk assessments for SMBs, first as an embedded insurance distribution platform and then as an MSP security tooling vendor, before being acquired by Cytracom in January 2025 for undisclosed terms after raising only $2.6M across its entire operating life. The company built genuinely useful technology — automated Attack Surface Management and Data Security Posture Management for MSPs — but was killed by undercapitalization, a false-positive problem in its PII scanning core, and a market consolidating around platforms that could absorb point solutions.

The rebuild thesis is this: compliance mandates that were aspirational in 2021 are now legally non-negotiable, LLM-based classification (GPT-4o, Claude 3.5 Sonnet) can eliminate the false-positive problem that eroded MSP trust, and PSA/RMM platform API marketplaces now offer the distribution channel Telivy had to beg for. The new version is a compliance-mapped security assessment layer that lives natively inside the MSP tools MSPs already use, sells itself through regulatory urgency, and builds a proprietary risk dataset that platform incumbents cannot easily replicate.

---34:Tade,

## Why Now?

## The single most important change since Telivy's failure: compliance mandates have converted discretionary security spending into legally required, auditable, recurring expenditure.

When Telivy launched in 2021, cyber risk assessments were a best practice that MSPs could recommend and SMB clients could decline. That dynamic has structurally reversed. Three specific regulatory changes now make continuous risk assessment non-optional for large swaths of the SMB market:

- **CMMC 2.0** (Department of Defense, enforcement phased from 2024–2026) requires any company in the defense industrial base — estimated at 300,000+ contractors and subcontractors — to achieve and document specific cybersecurity maturity levels. Third-party assessments are mandatory for Level 2 and above. MSPs serving defense contractors must now deliver assessable, documented security posture, not just best-effort monitoring.
- **FTC Safeguards Rule** (amended rule effective June 2023) requires non-bank financial institutions — auto dealers, mortgage brokers, tax preparers, accountants — to implement and document a formal information security program. The FTC has signaled active enforcement. This covers an estimated 200,000+ businesses that are disproportionately served by MSPs.
- **SEC Cybersecurity Disclosure Rules** (effective December 2023) require public companies to disclose material cybersecurity incidents within four business days and describe their risk management processes annually. While this targets public companies directly, it creates downstream pressure on their vendors and supply chain partners — many of which are SMBs managed by MSPs.

The global MSP market is projected to exceed $500B by 2028 (source: research report; independent verification of this specific figure is not available, but the directional growth is consistent with multiple analyst estimates). The compliance-driven security assessment segment within that market is the fastest-growing subsegment, because the demand is now pull-based rather than push-based.

The second enabling change is technical. **GPT-4o (May 2024) and Claude 3.5 Sonnet (June 2024)** now make it feasible to classify unstructured data — email archives, shared drives, legacy databases — with accuracy rates that reduce false positives to a manageable threshold. Telivy's known product weakness was precisely this: its PII scanning generated enough false positives to erode MSP trust. That problem is now solvable with off-the-shelf LLM APIs at a cost that a seed-stage company can afford.

Distribution has also changed materially. **NinjaRMM's app marketplace**, **ConnectWise's Invent partner program**, and **Datto's Marketplace** all now offer documented API integration paths and co-marketing support that did not exist in their current form when Telivy was navigating the ConnectWise PitchIT program in 2023. A new entrant can achieve native PSA/RMM integration in weeks, not quarters.

---

## Current Market Analysis

**Market size:** The global MSP market was approximately $239B in 2021 when Telivy launched; it is projected to exceed $500B by 2028 (research report; specific sourcing for the 2021 baseline figure is not independently verified here). The security-specific segment of MSP revenue is growing faster than the overall market, driven by the compliance mandates described above. The US cyber insurance market — relevant as a demand signal for risk assessment tooling — grew from approximately $4.8B in 2021 to an estimated $12B+ in 2024 (source: industry estimates; exact figures vary by source and should be independently verified before use in investor materials).

## Competition map and gaps:

- **Cytracom (post-Telivy acquisition):** The most direct successor. Cytracom acquired Telivy's technology but is an infrastructure-first MSP vendor whose core business is UCaaS and networking. Security risk management is a new product category for them. Integration of acquired technology into a new platform typically takes 12–24 months to reach feature parity with a purpose-built competitor. The window to compete is open now, not in 2028.
- **ConnectWise Cybersecurity Management:** Deep PSA integration but security features are add-ons to a workflow platform, not a purpose-built risk assessment engine. Pricing is bundled and opaque; MSPs report difficulty isolating security value from the broader platform cost.
- **Huntress:** Strong in threat detection and response for SMBs, with genuine MSP channel traction. Weakness: Huntress is endpoint-focused and does not offer compliance-mapped risk assessment or DSPM. It is a complement, not a substitute.
- **Axonius:** Enterprise-grade asset management with MSP capabilities. Weakness: pricing starts at a level that excludes small and mid-tier MSPs (managing fewer than 500 endpoints). No compliance workflow layer.
- **Drata / Vanta:** Compliance automation platforms with strong SMB traction. Weakness: designed for the SMB to manage its own compliance, not for an MSP to manage compliance across a client portfolio. No MSP multi-tenant architecture.

**The gap:** No current vendor offers a purpose-built, MSP-native, compliance-mapped risk assessment platform with LLM-powered DSPM that integrates natively into all three major PSA/RMM stacks (ConnectWise, Kaseya/Datto, NinjaRMM) and maps findings directly to CMMC 2.0, FTC Safeguards, and SOC 2 control frameworks. That is the white space.

**Defensibility against platform incumbents:** This is the honest version of the answer. ConnectWise, Kaseya, and NinjaRMM could build or acquire this capability. The structural advantage of the rebuild is not that incumbents cannot replicate it — they can — but that: (1) they are platform vendors whose incentive is to offer "good enough" security features that retain customers, not best-in-class point solutions; (2) compliance mapping requires continuous regulatory tracking and framework expertise that is not a natural competency for infrastructure vendors; and (3) a proprietary risk dataset built across thousands of MSP client assessments becomes a genuine moat over time, enabling benchmarking and predictive risk scoring that a platform vendor starting from zero cannot replicate quickly. This moat is real but takes 2–3 years to build. In the interim, the defensibility argument is speed and focus, not structural lock-in.

---

## Recommended MVP

## Core Features:

## Compliance-Mapped Risk Assessment Engine

Automated external attack surface scan (built on open-source tooling: ProjectDiscovery's Nuclei and OWASP Amass, both of which have matured significantly since 2021) that maps findings directly to CMMC 2.0 Practice requirements, FTC Safeguards Rule controls, and SOC 2 Trust Service Criteria. Each finding generates a remediation task with a compliance citation, not just a severity score. This differs from Telivy's original ASM in that the output is a compliance artifact, not a security report — it answers the question an MSP's client actually needs answered: "Am I compliant, and what do I need to fix?"

## LLM-Powered DSPM with Confidence Scoring

PII and sensitive data scanning across cloud storage (Google Drive, SharePoint, OneDrive, Dropbox) using GPT-4o API calls for unstructured document classification, with a confidence threshold filter that suppresses findings below 85% confidence before surfacing them to the MSP. Every finding includes the source document excerpt and the classification rationale, so the MSP can audit the result in 30 seconds rather than investigating a false positive for 30 minutes. This directly addresses Telivy's known product failure mode.

## Multi-Tenant MSP Dashboard with Client Portfolio View

A single-pane-of-glass view showing risk posture, compliance status, and open findings across all managed clients, with drill-down to individual client detail. Exportable compliance reports in PDF format, formatted for client QBRs. This is table stakes for MSP tooling but was not fully realized in Telivy's product based on available evidence.

## Native PSA/RMM Integration (ConnectWise Manage + NinjaRMM at launch)

Remediation tasks automatically create tickets in the MSP's PSA. Risk assessment triggers can be scheduled from within the RMM. This is the distribution moat: an MSP that has integrated the tool into their ticketing workflow has a high switching cost. Telivy pursued ConnectWise integration late and through a competitive program; the rebuild makes it the first engineering priority.

**What we will NOT build at MVP:** Cyber insurance distribution, carrier integrations, white-label capabilities for insurance agencies, or mobile applications. These were Telivy's original complexity traps.

## Success metrics:

- 15 paying MSP customers within 6 months of launch (threshold for product-market fit signal)
- Net Revenue Retention > 110% at 12 months (MSPs expanding seats as they add clients)
- False-positive rate on DSPM findings < 10% (measured by MSP-reported dismissal rate)
- PSA ticket creation rate > 70% of surfaced findings (integration adoption proxy)

**Cold-start problem:** This product does not depend on network effects or local density. Each MSP customer derives full value from day one based on their own client portfolio. The cold-start challenge is sales, not product — addressed in GTM below.

---

## Go-to-Market Strategy

**Target customer segment:** MSPs with 20–150 managed clients, serving at least one of three compliance-sensitive verticals: defense contractors (CMMC), financial services (FTC Safeguards), or healthcare (HIPAA). These MSPs have a compliance-driven buyer — their client is legally required to demonstrate security posture — which converts the sales conversation from "would this be useful?" to "when can we start?" This segment is narrow enough to build repeatable sales motion and large enough to reach $1M ARR without requiring hundreds of customers.

**Primary distribution channel:** The **ConnectWise Invent Marketplace** and **NinjaRMM App Store** as the primary discovery channels, combined with direct outbound to MSPs who have publicly listed CMMC or FTC Safeguards compliance as a service offering (identifiable via their own website copy and LinkedIn). Secondary channel: partnerships with CMMC Registered Practitioner Organizations (RPOs), which are consulting firms that help defense contractors achieve CMMC certification and actively refer MSPs to tooling vendors.

**Pricing strategy:** $299/month per MSP for up to 25 managed clients, $499/month for 26–75 clients, $799/month for 76–150 clients. Annual prepay at 20% discount.

*Stress test against free alternatives:* MSPs currently accomplish risk assessment through a combination of manual spreadsheet-based questionnaires, free NIST CSF self-assessment templates, and ad-hoc Nmap/Nessus scans. The free alternative is real but takes 7–8 days of manual work per client assessment (Telivy's own documented benchmark). At $299/month, an MSP with 25 clients is paying $12/client/month to eliminate that manual burden. If an MSP bills clients $150–$300/month for managed security services, the tool pays for itself by freeing one hour of technician time per client per month. The price is justified not by comparison to free alternatives but by the labor cost it displaces — a framing that MSPs, who think in terms of technician utilization, will immediately understand. The harder objection is not price but inertia: MSPs who have not yet sold compliance assessment as a service line need to be convinced to add a new offering, not just a new tool. The GTM motion must therefore lead with the revenue opportunity for the MSP ("add a $500/month compliance assessment service to every client") rather than the cost savings.

**Differentiation vs. 2026 competitors:** Against Cytracom's post-acquisition Telivy integration: faster time-to-value (purpose-built vs. integrated), cleaner compliance mapping, and no bundling with UCaaS infrastructure the MSP may not need. Against Huntress: complementary positioning (Huntress detects threats; this tool documents compliance posture), not competitive. Against Drata/Vanta: MSP-native multi-tenant architecture vs. single-tenant SMB tool.
