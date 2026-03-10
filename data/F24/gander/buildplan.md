# Build Plan: Gander 2026

## Overview

Gander was a New York-based YC F24 startup founded in 2024 by Arjan Guglani and Andrew Dixon to automate airline customer service — specifically, back-office reimbursement claim processing and proactive outbound rebooking calls for disrupted passengers — before being quietly acqui-hired in 2024–2025 after failing to close its first commercial airline customer, likely due to the structural mismatch between enterprise aviation procurement timelines and pre-seed runway.

The rebuild thesis is this: the DOT's October 2024 automatic cash refund mandate has transformed airline reimbursement processing from a discretionary efficiency play into a legal compliance obligation, creating a procurement forcing function that did not exist when Gander launched — and targeting low-cost carriers (LCCs) and ultra-low-cost carriers (ULCCs) instead of legacy network carriers cuts the sales cycle from eighteen months to a window where a well-capitalized seed-stage company can survive. **Gander 2.0 is a compliance-first AI claims processing platform for LCCs, using mandatory DOT refund workflows as the wedge into broader disruption automation.**

---31:Ta4c,

## Why Now?

The single most important change since Gander's failure is regulatory: the U.S. Department of Transportation's final rule on Airline Refunds, effective October 28, 2024, now requires airlines to automatically issue cash refunds — without passengers requesting them — for cancelled flights and significant delays (defined as delays of three or more hours for domestic flights). This rule did not exist when Gander launched its YC post. It transforms reimbursement processing from a cost-reduction opportunity into a legal compliance requirement with enforcement teeth, including civil penalties. Airlines that fail to comply face DOT enforcement action. This is a categorically different procurement conversation: "would you like to save money on claims?" becomes "you are legally required to process these claims automatically or face fines."

This regulatory shift directly validates Gander's original back-office automation thesis and creates a compliance-driven forcing function that compresses procurement timelines. Compliance software purchases move faster than efficiency software purchases in regulated industries — this is well-documented in healthcare (HIPAA) and finance (SOX) and is now replicating in aviation.

On the technical side, the core barrier to Gander Voice — voice AI latency — has been resolved. OpenAI's Realtime API (launched October 2024) and ElevenLabs Conversational AI now deliver sub-500ms end-to-end voice latency, enabling natural-sounding outbound rebooking calls that would not have caused passenger rejection. LLM-native document parsing via GPT-4o and Claude 3.5 Sonnet (both available by mid-2024) can now extract structured routing data from Route Availability Documents and IATA fare rules with high accuracy, eliminating the expensive manual data integration work that would have consumed a pre-seed engineering team.

The vertical AI agent category has also matured. Abridge (clinical documentation), Harvey (legal), and Tennr (healthcare intake) have demonstrated that domain-specific AI can close enterprise contracts in regulated verticals, reducing the buyer skepticism that would have been a significant headwind for Gander in 2024. Aviation buyers in 2026 are not being asked to be early adopters of a novel category — they are being asked to adopt a proven model in a new domain.

Specific market data on LCC claims processing volume is not publicly available, but the DOT reported approximately 1.3 million flight cancellations and significant delays in the U.S. in 2023 (DOT Air Travel Consumer Report, 2024), each now triggering mandatory automatic refund workflows.

---

## Current Market Analysis

**Market size:** Gander's original TAM claim of $80 billion in global airline customer service spend is accurate in aggregate but not useful for planning. The more relevant figure is the U.S. airline refund and compensation processing market. The DOT reported that U.S. airlines paid approximately $600 million in refunds in 2023 (DOT, 2024) — a figure that will grow materially under the new automatic refund rule, as airlines must now proactively identify and process eligible passengers rather than waiting for claims. The serviceable market for a compliance automation platform targeting U.S. LCCs and ULCCs — carriers like Spirit, Frontier, Allegiant, Sun Country, and Breeze — is not publicly quantified, and we will not invent a number. What is known is that these carriers collectively operate hundreds of daily flights and have lean back-office teams relative to their disruption volumes, making automation ROI structurally higher than at legacy carriers with larger operations teams.

**Competition map:** The competitive landscape has three layers.

*Incumbent aviation software vendors* — Amadeus, SITA, IBS Software — have existing airline relationships and are embedding AI into customer service modules. Their weakness is that their AI features are bolt-ons to legacy platforms, not purpose-built compliance automation. Procurement cycles with these vendors are long, and their refund automation capabilities are not publicly demonstrated as DOT-rule-compliant as of early 2026.

*Generic AI customer service platforms* — Intercom, Zendesk AI, Salesforce Einstein — have broad enterprise reach but no aviation-specific compliance logic, no RAD parsing, and no understanding of DOT refund rule eligibility criteria. They are horizontal tools being asked to solve a vertical compliance problem.

*Point-solution AI voice vendors* — Bland AI, Retell AI, ElevenLabs — provide the voice infrastructure layer but not the aviation workflow logic, eligibility determination, or regulatory compliance layer on top.

The gap is a purpose-built, DOT-compliance-first claims automation platform with aviation-specific AI — a category that does not currently have a dominant player.

**Defensibility against platform incumbents:** The honest answer is that this is a real risk. Amadeus or SITA could build this. The structural advantage of a rebuild is speed and specialization: a focused team can ship DOT-compliant refund automation in months; an incumbent's product roadmap moves in years. The window of defensibility is 18–36 months, after which the rebuild must have enough customer relationships and switching costs (deep integration into airline reservation systems, trained compliance workflows, audit trails) to be sticky. This is not a forever moat — it is a timing moat that must be converted into a data and integration moat before incumbents catch up.

---

## Recommended MVP

**Feature 1: DOT Refund Compliance Engine.** An automated workflow that ingests flight disruption data from airline reservation systems, applies DOT eligibility rules (cancellation, 3+ hour domestic delay, 6+ hour international delay), identifies affected passengers, calculates refund amounts, and initiates payment — without agent involvement. This is the core wedge: it directly addresses a legal compliance obligation, not a discretionary efficiency goal. Unlike Gander's original back-office automation pitch, this feature leads with compliance language and audit trail generation, not cost savings, which changes the procurement conversation from "nice to have" to "required."

**Feature 2: Outbound Disruption Voice Agent.** Using OpenAI Realtime API or ElevenLabs Conversational AI (both available with sub-500ms latency as of late 2024), an outbound voice agent calls disrupted passengers before they reach the airport, presents rebooking options from available inventory, and completes the rebooking without human agent involvement. Unlike Gander Voice, this version is built on production-grade low-latency infrastructure that makes the conversation feel natural rather than robotic — the technical barrier that would have caused passenger rejection in 2024 is now resolved.

**Feature 3: RAD-Aware Rebooking Recommendations.** Using GPT-4o's document parsing capabilities, the system ingests Route Availability Documents to identify eligible rerouting options and surfaces them to the voice agent and claims engine. This is the domain-specific AI layer that differentiates the product from generic AI customer service tools and cannot be replicated by a horizontal vendor without aviation expertise.

**What we will NOT build:** A fleet management platform, a private jet product, a general-purpose airline CRM, or any feature that requires integration with more than two airline data systems in the MVP. The original Gander's pivot to private jet fleet management was a distraction that required rebuilding the product from scratch. This rebuild stays in its lane.

**Success metrics:** One signed LCC customer with a live DOT refund compliance workflow processing real claims within 9 months of founding. Average claims processing time reduced by 70% vs. manual baseline (to be measured with the first customer). Voice agent rebooking completion rate above 40% of outbound calls connected.

**Cold-start problem:** This product does not depend on network effects or local density. It is a B2B SaaS tool that delivers value to a single airline customer from day one of deployment. No minimum user threshold applies.

---

## Go-to-Market Strategy

**Target customer segment:** U.S.-based low-cost and ultra-low-cost carriers with 50–500 daily departures — specifically Spirit Airlines (currently in bankruptcy restructuring as of 2025, creating procurement openness), Frontier Airlines, Allegiant Air, Sun Country Airlines, and Breeze Airways. These carriers share three characteristics that make them the right first customers: lean back-office teams relative to disruption volume (high automation ROI), less bureaucratic procurement than legacy network carriers (Delta, United, American), and acute exposure to DOT refund rule compliance risk given their high load factors and point-to-point route structures that limit rebooking options.

**Primary distribution channel:** Direct enterprise sales via aviation industry relationships, specifically through introductions from YC's network, aviation investor networks (Insight Partners has aviation software exposure), and the World Aviation Festival and Routes Americas conference circuit where the original Gander team had established presence. No PLG motion is appropriate for this customer segment.

**Pricing strategy:** Usage-based pricing tied to claims processed — estimated at $8–15 per claim resolved automatically, with a monthly platform fee of $5,000–$15,000 depending on flight volume. Stress-test: there is no free alternative for DOT-compliant automatic refund processing. Airlines currently use manual agent workflows (expensive) or legacy vendor modules (slow and not DOT-rule-specific). The pricing is justified not against a free alternative but against the cost of non-compliance (DOT civil penalties) and the fully-loaded cost of manual claims processing (estimated at $25–50 per claim in agent time, though this figure is not publicly disclosed by carriers and should be validated with the first customer). A subscription-only model would face resistance; usage-based pricing aligns cost with value and lowers the barrier to a pilot contract.

**Differentiation vs. 2026 competitors:** The rebuild's differentiation is the combination of DOT compliance specificity (not a generic AI tool), aviation data integration depth (RAD parsing, reservation system connectors), and the compliance-first sales narrative that horizontal competitors cannot credibly claim. The rebuild leads every sales conversation with "you are legally required to do this" — a message that Amadeus, Zendesk, and Bland AI cannot deliver with the same credibility.
