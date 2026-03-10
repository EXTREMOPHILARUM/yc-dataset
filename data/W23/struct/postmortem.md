# Research Report: Struct

## Overview

Struct was a Y Combinator-backed startup that built a platform for multi-lingual, real-time AI voice agents capable of handling phone-based tasks across industries including fintech, legaltech, SaaS, and CRM. <sup><a href="https://www.ycombinator.com/companies/struct">[1]</a></sup> Founded in 2023 and accepted into YC's Winter 2023 cohort, the company operated out of a 3-person team with approximately $500,000 in total known funding — the standard YC deal — and positioned itself as infrastructure for businesses that needed AI to conduct or receive calls at scale. <sup><a href="https://www.ycombinator.com/companies/struct">[2]</a></sup>

Struct entered one of the most crowded categories of the 2023 AI boom with minimal capital, a horizontal platform strategy, and no documented vertical focus. The combination proved fatal: better-funded competitors with near-identical positioning — Bland AI, Retell AI, Vapi — emerged in the same window, and the underlying voice AI technology commoditized faster than a 3-person team could build a defensible moat around it.

The company is now listed as "Inactive" on YC's company directory. <sup><a href="https://www.ycombinator.com/companies/struct">[1]</a></sup> No acquisition, acqui-hire, or public post-mortem has been documented. The shutdown appears to have been a quiet wind-down, with no press coverage, no Hacker News launch post, and no public statement from the founding team.

<report-gallery>
<media-image src="https://media.licdn.com/dms/image/v2/D4E03AQHSoCjqFuP8PQ/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1715921303303?e=2147483647&v=beta&t=RaGqFvDDfBnpDoW06Kr2ME6rHTwmEB-oTMg3Q1rCkP0" alt="Manoj Bala Radhakrishna - Founder and CEO of Struct" caption="Manoj Bala Radhakrishna, Struct's founder and CEO — a former Intercom engineering manager who bet on multilingual voice AI before the category became one of 2023's most crowded."></media-image>
<media-image src="https://framerusercontent.com/images/Lbfqx0KmbS5rW3cEM3ynAvfkvRQ.webp" alt="Struct platform marketing image" caption="Struct's marketing positioned the platform as infrastructure for any phone-based AI task — a horizontal bet that proved difficult to defend with a 3-person team and $500K in runway."></media-image>
</report-gallery>

## Founding Story

Struct was founded in 2023 by a small team of three, led by at least one founder — identified as Manoj Bala Radhakrishna — who brought meaningful enterprise software experience to the venture. <sup><a href="https://www.ycombinator.com/companies/struct">[7]</a></sup> Prior to Struct, Radhakrishna had worked at Intercom, the customer messaging platform, in both individual contributor and engineering manager roles, as well as at several UK-based startups. <sup><a href="https://www.ycombinator.com/companies/struct">[7]</a></sup> That background — building customer-facing communication infrastructure at scale — maps directly onto the problem Struct was trying to solve: replacing or augmenting human agents on phone-based customer interactions with AI.

The founding insight appears to have been rooted in a gap Radhakrishna likely observed at Intercom and elsewhere: while chat-based AI automation was advancing rapidly, voice — particularly multilingual voice — remained underserved by existing tooling. Phone calls are still the dominant channel for customer service in many industries and geographies, yet the infrastructure for automating them intelligently was fragmented, expensive, and largely English-only. Struct's pitch was that a unified, language-agnostic platform could unlock this market for businesses that couldn't afford to staff multilingual call centers.

The team applied to YC's Winter 2023 batch, which received over 20,000 applications and funded 282 companies — a roughly 1.4% acceptance rate. <sup><a href="https://www.ycombinator.com/blog/meet-the-yc-winter-2023-batch">[11]</a></sup> Being selected signals that YC saw credibility in either the team's background, the early product, or both. The W23 cohort was announced publicly on April 5, 2023. <sup><a href="https://www.ycombinator.com/blog/meet-the-yc-winter-2023-batch">[11]</a></sup>

Beyond Radhakrishna, the identities and backgrounds of the other two team members are not publicly documented. Whether the team included dedicated AI/ML expertise, telephony engineering experience, or sales capacity is unknown — a gap that matters significantly for a platform play in a technically demanding category.

No major pivot is documented in the public record. The company appears to have pursued its original vision — horizontal AI voice infrastructure — from founding through wind-down, without a documented course correction toward a specific vertical or use case.

## Timeline

- **January 2023** — Struct founded; accepted into Y Combinator's Winter 2023 batch. <sup>[[1]](https://www.ycombinator.com/companies/struct)</sup>
- **January 2023** — Struct receives standard YC investment: $125,000 for 7% equity plus a $375,000 uncapped MFN note, totaling approximately $500,000. <sup>[[12]](https://yourstory.com/2023/04/y-combinator-winter-cohort-2023-indian-startups-atri-labs-magik)</sup>
- **April 5, 2023** — YC publicly announces the W23 batch of 282 companies; Struct included. <sup>[[11]](https://www.ycombinator.com/blog/meet-the-yc-winter-2023-batch)</sup>
- **April 2023** — Struct's product documentation published at docs.struct.app, describing open beta status, sub-600ms latency, and the multi-lingual voice agent platform. <sup>[[10]](https://docs.struct.app/start-here/introduction/)</sup>
- **2023** — Struct claims agents are "live doing tens of thousands of calls daily across the globe and in multiple languages." <sup>[[6]](https://www.ycombinator.com/companies/struct)</sup>
- **2024** — Struct listed as "Inactive" on YC's company directory. No public shutdown announcement made. <sup>[[1]](https://www.ycombinator.com/companies/struct)</sup>2c:Td3f,

## What They Built

Struct built a platform for deploying real-time, conversational AI voice agents capable of handling inbound and outbound phone calls. <sup><a href="https://docs.struct.app/start-here/introduction/">[8]</a></sup> The core value proposition was that businesses could configure and deploy AI agents that could listen, understand, and respond to callers — completing tasks autonomously without human intervention — across multiple languages. <sup><a href="https://docs.struct.app/start-here/introduction/">[9]</a></sup>

**Core Capability: Real-Time Voice Conversation**

The platform's defining technical claim was sub-600ms response latency — meaning the AI agent could respond to a caller within 600 milliseconds of the caller finishing a sentence. <sup><a href="https://docs.struct.app/start-here/introduction/">[9]</a></sup> In voice AI, latency is the primary determinant of whether a conversation feels natural or robotic. A 600ms threshold is roughly at the edge of what most humans perceive as a natural conversational pause, making it a meaningful — if not exceptional — benchmark. Competitors in the same period were targeting similar or lower latency figures, suggesting this was a category baseline rather than a true differentiator.

**Multi-Lingual Architecture**

The "multi-lingual" positioning was Struct's most distinctive angle. The platform was designed from the ground up to handle calls in multiple languages, not just English with add-on translation. This suggested either a multilingual speech recognition stack, multiple language-specific models, or a combination — though the specific languages supported and the underlying technology stack (whether built on OpenAI Whisper, Deepgram, ElevenLabs, or proprietary models) are not publicly documented.

**Platform Breadth**

Struct positioned itself as infrastructure for "any phone-based task" — a deliberately broad framing. <sup><a href="https://www.ycombinator.com/companies/struct">[5]</a></sup> The YC listing tagged the company across fintech, legaltech, SaaS, and CRM — four distinct verticals with meaningfully different compliance requirements, call patterns, and buyer personas. <sup><a href="https://www.ycombinator.com/companies/struct">[5]</a></sup> This horizontal positioning implied an API-first or configurable platform model, where customers could define the agent's behavior, knowledge base, and task logic. Whether the product was API-first, no-code, or a hybrid is not documented.

**Open Beta Status**

At the time its documentation was published in April 2023, Struct's platform was available in "open beta." <sup><a href="https://docs.struct.app/start-here/introduction/">[10]</a></sup> This is a meaningful signal: open beta typically indicates a product that is functional but not yet hardened for production enterprise use — lacking the reliability SLAs, compliance certifications (SOC 2, HIPAA), and support infrastructure that enterprise telephony buyers require before committing to a vendor.

<media-image src="https://framerusercontent.com/images/P3IGdx5RGA8BlfCV114DDrZYG8w.webp" alt="Struct platform interface" caption="A marketing visual from Struct's website illustrating the platform's voice agent capabilities — the product was in open beta as of April 2023, still short of the reliability threshold enterprise telephony buyers typically require."></media-image>

## Market Position

### Target Customers

Struct's stated target was businesses that needed to automate phone-based interactions at scale — specifically those operating across multiple languages or geographies. <sup><a href="https://www.ycombinator.com/companies/struct">[6]</a></sup> The four vertical tags on YC's directory — fintech, legaltech, SaaS, and CRM — suggest the team was pitching to any company with a meaningful call volume: financial services firms handling customer onboarding or collections calls, legal services companies managing intake, SaaS businesses running sales or support, and CRM-adjacent companies automating outreach. <sup><a href="https://www.ycombinator.com/companies/struct">[5]</a></sup>

The multi-lingual angle implied a secondary target: companies operating in non-English markets or serving multilingual customer bases — a segment underserved by most English-first voice AI platforms in 2023. This could have included Latin American fintech companies, European SaaS businesses, or global BPO operators. However, no specific customer names, geographies, or case studies are documented.

### Market Size

The AI voice agent market in 2023 was nascent but growing rapidly. The broader conversational AI market was estimated at several billion dollars annually, with voice-specific applications representing a significant and growing subset driven by enterprise demand for call center automation. The addressable market for phone-based AI automation is large by any measure — global call center spending exceeds $300 billion annually, and even modest automation penetration represents a multi-billion-dollar opportunity. However, market size was not Struct's constraint. The constraint was the ability to capture any portion of it before better-capitalized competitors locked up distribution.

### Competition

The 2023 AI voice agent space was one of the most crowded sub-categories of the broader AI boom, and Struct's competitive position was structurally weak along the dimensions that mattered most.

**The Competitive Axes**

In AI voice infrastructure, the two axes that determined competitive outcomes were: (1) **distribution reach** — how many developers and enterprises could a platform reach through integrations, partnerships, and brand recognition — and (2) **product depth** — how reliable, customizable, and enterprise-ready was the platform. Struct competed on neither axis with any clear advantage.

**Direct Competitors**

Bland AI, Retell AI, and Vapi all emerged in roughly the same window as Struct with near-identical positioning: API-first platforms for deploying AI voice agents at scale. Retell AI (YC W24) and Vapi both raised meaningful seed rounds and built developer communities through aggressive open-source positioning and Product Hunt launches. Bland AI targeted enterprise sales teams specifically. All three achieved greater public visibility than Struct within months of launch.

**Platform Risk**

A more structural threat came from the underlying AI infrastructure providers themselves. OpenAI, Google (via Gemini and Vertex AI), and Amazon (via AWS Connect) all had the capability to offer voice agent functionality natively — and each had distribution advantages that no seed-stage startup could match. When OpenAI introduced real-time voice capabilities in late 2023, it compressed the differentiation window for every independent voice AI platform simultaneously.

**The Incumbents' Natural Advantage**

Established contact center platforms — Twilio, Five9, Genesys, and NICE — were also integrating AI voice capabilities into their existing products. These incumbents had something Struct could never replicate quickly: existing enterprise relationships, compliance certifications, and telephony infrastructure already trusted by the buyers Struct was targeting. A fintech company evaluating an AI voice platform in 2023 had strong reasons to wait for their existing Twilio or Genesys vendor to ship an AI layer rather than bet on a 3-person open-beta startup.

<media-image src="https://framerusercontent.com/images/bmcJbnBy8q3LDwbfmwGQrwsDAw.webp" alt="Struct platform feature visual" caption="Struct's platform marketing emphasized breadth across verticals — a positioning that spread a 3-person team thin against competitors who were narrowing into specific use cases and building deeper integrations."></media-image>

## Business Model

Struct's revenue model is not publicly documented. The company never disclosed pricing, ARR, or customer contract structures. The absence of any revenue disclosure — even in YC marketing materials — is itself a signal: companies with meaningful revenue typically surface it in fundraising contexts.

Based on the platform positioning and the competitive landscape, the most likely model was usage-based pricing tied to call volume (minutes or calls processed), potentially combined with a platform fee. This is the standard model for voice AI infrastructure: Twilio charges per minute of voice, and most AI voice platforms in 2023 adopted similar structures. At scale, usage-based pricing can generate strong unit economics, but it requires significant call volume to generate meaningful revenue — and call volume requires enterprise customers with production deployments.

**Estimated Burn and Runway**

With 3 employees and approximately $500,000 in total funding, <sup><a href="https://www.ycombinator.com/companies/struct">[1]</a></sup> <sup><a href="https://yourstory.com/2023/04/y-combinator-winter-cohort-2023-indian-startups-atri-labs-magik">[12]</a></sup> Struct's runway was structurally limited. A 3-person team in a tech hub (assuming San Francisco or London, given the Intercom background) would carry a monthly burn of approximately $30,000–$50,000 in salaries alone, plus infrastructure costs for a real-time voice platform (compute, telephony APIs, LLM inference). At $40,000/month in total burn — a conservative estimate — $500,000 represents roughly 12–13 months of runway. This places a probable capital exhaustion date in early-to-mid 2024, consistent with the "Inactive" listing. These figures are inferences based on headcount and funding; actual burn is unknown.

The company never raised a follow-on round, which is the clearest signal that it did not achieve the traction metrics — revenue, growth rate, or customer quality — required to attract Series A or even seed extension capital in a market where investors were becoming more selective about AI voice bets by late 2023.

## Traction

Struct's YC listing claimed its agents were "already live doing tens of thousands of calls daily across the globe and in multiple languages." <sup><a href="https://www.ycombinator.com/companies/struct">[6]</a></sup> If accurate, this represents genuine production deployment — not a demo or pilot — and suggests at least some paying customers with real call volume.

However, this claim carries medium confidence. It appears in YC's own marketing copy, which is written by or with the company and is not independently verified. "Tens of thousands of calls daily" could reflect a single large customer, a handful of mid-market deployments, or an aggregation across a free beta tier. No customer names, logos, or case studies are documented anywhere in the public record. No revenue figures were disclosed. No press coverage corroborated the claim.

The breadth of industry tags — fintech, legaltech, SaaS, CRM — may reflect genuine multi-vertical deployments, or it may reflect an unfocused go-to-market that had not yet identified a primary wedge customer. For a 3-person team, serving four distinct verticals simultaneously would have made it nearly impossible to build the vertical-specific features, compliance posture, or reference customers needed to close enterprise deals in any single category.

No Hacker News launch post, Product Hunt listing, or press article about Struct has been identified — a notable absence for a company claiming tens of thousands of daily calls. Companies with that level of production activity typically have at least some public footprint.

## Post-Mortem

### Primary Cause: Structural Overcrowding in a Commoditizing Category

The most important factor in Struct's failure was not a specific decision the team made — it was the market they entered. The AI voice agent category in 2023 attracted an extraordinary concentration of well-funded startups, all with near-identical positioning, in a window where the underlying technology was commoditizing faster than any single team could build defensibility around it.

Bland AI, Retell AI, and Vapi all launched in 2023 with similar pitches: API-first platforms for deploying AI voice agents at scale. Retell AI went through YC's Winter 2024 batch — one cohort after Struct — and raised a seed round with significantly more capital and developer community traction. Vapi built an aggressive developer ecosystem through open-source tooling and Product Hunt launches. These competitors did not necessarily build better technology than Struct; they built better distribution. And in a platform business, distribution compounds in ways that technology alone cannot overcome.

Struct had no documented developer community, no open-source presence, no Product Hunt launch, and no press coverage. In a category where developer mindshare was the primary acquisition channel, this absence was effectively a death sentence.

### Secondary Cause: Horizontal Platform Strategy with Insufficient Capital

Struct described itself as "the platform for multi-lingual AI voice agents for any phone-based task" — a deliberately horizontal positioning that targeted fintech, legaltech, SaaS, and CRM simultaneously. <sup><a href="https://www.ycombinator.com/companies/struct">[5]</a></sup> <sup><a href="https://www.ycombinator.com/companies/struct">[6]</a></sup> For a 3-person team with $500,000 in capital, this was an almost certain path to failure.

Horizontal platform plays require either massive distribution (which requires capital or an existing user base) or a dominant vertical wedge that generates enough revenue and reference customers to fund expansion. Struct had neither. Each of the four verticals it targeted — fintech, legaltech, SaaS, CRM — has distinct compliance requirements, buyer personas, and sales cycles. A fintech company needs FINRA-compliant call recording and PII handling. A legaltech company needs attorney-client privilege considerations. A SaaS company needs CRM integrations. Serving all four simultaneously with three people means serving none of them well enough to generate the reference customers that close the next deal.

No evidence exists that Struct attempted to narrow its focus to a single vertical. Whether this was a deliberate strategic choice or a failure to recognize the problem is unknown.

### Tertiary Cause: Platform-Level Compression from Infrastructure Providers

In late 2023, OpenAI introduced real-time voice capabilities — a direct compression of the differentiation space for every independent voice AI platform. When the underlying model provider ships the feature natively, the value proposition of a thin wrapper around that capability collapses. Struct's sub-600ms latency claim, <sup><a href="https://docs.struct.app/start-here/introduction/">[9]</a></sup> which was a meaningful differentiator in early 2023, became table stakes — or worse, irrelevant — once OpenAI's real-time API offered comparable performance with the distribution advantage of the world's largest AI developer platform.

This is a structural dynamic, not a Struct-specific failure. Every voice AI startup in the 2023 cohort faced the same compression. The ones that survived did so by building vertical depth, proprietary data advantages, or enterprise relationships that made switching costs high enough to withstand the platform move. Struct, still in open beta with no documented enterprise relationships, had none of these buffers.

### Contributing Factor: Open Beta Status and Enterprise Readiness Gap

Struct's product was in open beta as of April 2023. <sup><a href="https://docs.struct.app/start-here/introduction/">[10]</a></sup> Enterprise telephony buyers — the customers with the call volume to make a usage-based voice AI platform economically viable — require production-grade reliability before committing to a vendor. This typically means SOC 2 Type II certification, 99.9%+ uptime SLAs, dedicated support, and compliance documentation. A 3-person team in open beta cannot credibly offer any of these.

The gap between "open beta with tens of thousands of calls" and "enterprise-ready platform with signed contracts" is where many infrastructure startups stall. Crossing it requires either significant engineering investment (to harden the platform) or significant sales investment (to find early-adopter enterprise buyers willing to accept beta-grade reliability). Both require capital and headcount that Struct did not have.

### The Absence of a Public Narrative

One final signal worth noting: Struct left no public record of its existence beyond the YC directory listing and its documentation site. No press coverage. No Hacker News post. No Product Hunt launch. No founder tweets. No LinkedIn activity. For a company claiming tens of thousands of daily calls, this silence is unusual. It may indicate that the traction claim was aspirational, that the team was operating in deliberate stealth, or simply that the company wound down before it had the opportunity to build a public presence. Without founder commentary, the interpretation remains open.

## Key Lessons

- **Horizontal platform positioning is a capital-intensive strategy that a $500K seed cannot support.** Struct tagged itself across fintech, legaltech, SaaS, and CRM simultaneously — four verticals with distinct compliance requirements and buyer personas. Competitors like Bland AI survived the same crowded market in part by narrowing to a specific use case (outbound sales calls) and building reference customers in that lane before expanding. Struct's failure illustrates that "platform for any phone-based task" is a Series B positioning statement, not a seed-stage go-to-market.

- **In developer-tool categories, distribution compounds faster than technology.** Struct built a real-time voice platform with sub-600ms latency and multilingual support — technically credible claims. But it left no documented developer community, no open-source presence, and no Product Hunt launch. Retell AI, which launched one YC cohort later with similar technology, built a developer ecosystem through aggressive public positioning and outpaced Struct in visibility within months. In infrastructure categories, the team that wins mindshare first tends to win the market, regardless of which product is technically superior.

- **The multilingual angle was a genuine differentiator, but differentiation without distribution is insufficient.** Struct's multilingual positioning addressed a real gap — most 2023 voice AI platforms were English-first. But differentiation only creates value if it reaches the buyers who need it. With no documented international partnerships, no language-specific marketing, and no vertical focus that would have concentrated multilingual demand (e.g., Latin American fintech or European SaaS), the differentiator never translated into a defensible customer segment.

- **When OpenAI ships your core feature, the clock starts.** Struct's value proposition — low-latency, real-time AI voice — was directly compressed when OpenAI introduced real-time voice capabilities in late 2023. Startups building on top of commoditizing AI capabilities need either vertical depth (proprietary data, compliance certifications, enterprise relationships) or a switching-cost moat before the platform move happens. Struct, still in open beta with no documented enterprise contracts, had neither buffer when the compression arrived.

## Sources

1. [Y Combinator Company Directory — Struct](https://www.ycombinator.com/companies/struct)
2. [Struct Product Documentation — Introduction](https://docs.struct.app/start-here/introduction/)
3. [Y Combinator Blog — Meet the YC Winter 2023 Batch (April 5, 2023)](https://www.ycombinator.com/blog/meet-the-yc-winter-2023-batch)
4. [YourStory — Y Combinator Winter 2023 Cohort Coverage (April 10, 2023)](https://yourstory.com/2023/04/y-combinator-winter-cohort-2023-indian-startups-atri-labs-magik)
