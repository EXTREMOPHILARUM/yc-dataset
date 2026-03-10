# Research Report: Fabius

## Overview

Fabius Technologies was a San Francisco-based AI startup that built a sales coaching and deal-scoring layer on top of existing conversation intelligence tools like Gong and Chorus.Founded in September 2020 by two former LiveRamp engineers, the company spent over two years in stealth before entering Y Combinator's Winter 2023 batch.

Its core thesis was that B2B sales teams suffer from a systematic gap between their defined sales methodology and what reps actually do in the field — and that LLMs could close that gap by scoring calls, flagging at-risk deals, and coaching reps in real time.Despite generating modest early revenue and earning a YC stamp of approval, Fabius appears to have stalled after its pre-seed round.

With a two-person team, no publicly documented follow-on funding, and no meaningful public presence, the company likely ran out of runway before it could differentiate itself in a market where well-capitalized incumbents were rapidly building the same features natively.

## Founding Story

Neil Madsen and Andy Day both came out of LiveRamp, the data connectivity company that helps brands and publishers connect customer data across platforms. Their shared background was not incidental to what Fabius became. Madsen served as Head of Technical Services at LiveRamp, overseeing all customer-facing technical teams — Sales Engineering, Implementation, Technical Account Management, and Support.<sup><a href="https://www.ycombinator.com/companies/fabius">[1]</a></sup> Day led the Pixel Serving Engineering team, building the data pipeline infrastructure that powered LiveRamp's core product.<sup><a href="https://www.ycombinator.com/companies/fabius">[2]</a></sup> Together, they had direct exposure to both the go-to-market motion of a complex B2B sale and the engineering required to process large volumes of behavioral data.

Fabius Technologies, Inc. was incorporated on September 14, 2020.<sup><a href="https://www.crunchbase.com/organization/fabius-66e4">[3]</a></sup> The company was headquartered in San Francisco.<sup><a href="https://www.crunchbase.com/organization/fabius-66e4">[4]</a></sup> Madsen holds a BS in Computer Science from The Ohio State University, graduating in 2015.<sup><a href="https://www.crunchbase.com/person/neil-madsen-d773">[5]</a></sup> Day attended Northwestern University, graduating in 2011.<sup><a href="https://www.linkedin.com/in/andrewkday/">[6]</a></sup>

The founding insight appears to have come directly from Madsen's time running customer-facing teams. Sales organizations invest heavily in defining methodologies — frameworks like MEDDPICC that prescribe exactly what information a rep should gather and what steps they should complete before a deal advances. In practice, reps routinely skip steps, misqualify prospects, and report deal health optimistically. Madsen had watched this dynamic play out from the inside. The problem was not that companies lacked a process; it was that they had no reliable way to verify whether the process was being followed.

What is less clear is what the company was doing between its founding in September 2020 and its entry into YC's W23 batch in January 2023 — a gap of more than two years. Crunchbase notes a possible connection to Alchemist Accelerator, which focuses on enterprise startups, though this is unconfirmed.<sup><a href="https://www.crunchbase.com/organization/fabius-66e4">[7]</a></sup> If accurate, it would suggest an earlier product iteration predating the LLM-powered version that launched publicly in early 2023. No milestones, pivots, or funding events from this period have been documented publicly.

The YC experience itself produced at least one memorable moment. Andy Day later recounted on LinkedIn that a YC partner ejected them from office hours for debating whether to add "AI" to the company name: *"I cannot believe you're wasting my office hours on this. Come back when you have something real."* Day described the episode as a turning point that redirected the team toward customers and revenue.<sup><a href="https://www.linkedin.com/in/andrewkday/">[8]</a></sup> The anecdote is revealing — it suggests a team that, at least briefly, was susceptible to branding distractions in a moment when execution was everything.

---

## Timeline

- **September 14, 2020** — Fabius Technologies, Inc. incorporated by Neil Madsen and Andy Day; @FabiusTech Twitter account created but never used.<sup>[[3]](https://www.crunchbase.com/organization/fabius-66e4)</sup>
- **September 2020 – December 2022** — Company operates for over two years with no publicly documented milestones, funding, or product launches.
- **January 2023** — Fabius enters Y Combinator's Winter 2023 (W23) batch.<sup>[[9]](https://www.ycombinator.com/companies/fabius)</sup>
- **February 17, 2023** — Fabius launches publicly on YC's platform, describing its AI-powered sales process scoring and rep coaching product.<sup>[[10]](https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals)</sup>
- **May 5, 2023** — Fabius raises a pre-seed round from Y Combinator (amount disputed: $125K per Tracxn,<sup>[[11]](https://tracxn.com/d/companies/fabius/__9SqVGM5ZuyIcC2E375vW_UmtnjzoIPvxyLuCJP-JnJM/funding-and-investors)</sup> $500K per LinkedIn/Crunchbase<sup>[[12]](https://www.linkedin.com/company/fabius-technologies)</sup>).
- **February 2026** — No follow-on funding recorded, no shutdown announcement published, website still live with active "Book a Demo" CTA, Andy Day's LinkedIn and GitHub still list Fabius as current role.<sup>[[13]](https://www.ycombinator.com/companies/fabius)</sup><sup>[[14]](https://www.linkedin.com/in/andrewkday/)</sup><sup>[[15]](https://github.com/adayNU)</sup>

---

## What They Built

Fabius built an AI layer that sat on top of a sales team's existing conversation intelligence stack. Rather than replacing tools like Gong or Chorus, Fabius ingested the data those tools already captured — recorded calls, transcripts, emails — and applied a company's specific sales methodology as a scoring rubric.<sup><a href="https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals">[10]</a></sup>

The core problem Fabius addressed was what the founders called the "rose-colored glasses" effect: sales reps consistently overestimate deal health, skip qualification steps, and fail to surface the information their managers need to forecast accurately. A company might run MEDDPICC — a rigorous enterprise sales framework requiring reps to document Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion, and Competition — but have no automated way to verify whether any of those boxes were actually checked in a given call.<sup><a href="https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals">[16]</a></sup>

Fabius addressed this through several interconnected features:

**Deal Scoring.** Fabius worked with each customer to build custom rubrics for stages like Discovery and Closing. After every call, the system scored the deal against those rubrics and surfaced specific gaps — not just a score, but a direction: what the rep should do differently next time.<sup><a href="https://www.fabius.io/">[17]</a></sup>

**Just-in-Time Rep Feedback.** Rather than waiting for a weekly pipeline review, Fabius delivered coaching to individual reps immediately after calls, while the conversation was still fresh. The goal was to change rep behavior at the moment it could still affect the deal.<sup><a href="https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals">[18]</a></sup>

**Automated Post-Call Emails.** Fabius generated personalized follow-up emails after customer calls, incorporating tailored structure, relevant case studies, ROI proof points, and technical documentation drawn from the company's own materials.<sup><a href="https://www.fabius.io/">[19]</a></sup>

**CRM Auto-Update.** The system kept CRM records current automatically, reducing the manual data entry burden on reps and improving the accuracy of the data sales managers relied on for forecasting.<sup><a href="https://www.fabius.io/">[19]</a></sup>

**Forecast Improvement.** By surfacing which deals were missing key qualification steps, Fabius gave sales leaders a more accurate picture of pipeline health — reducing the surprise losses that plague enterprise sales forecasts.<sup><a href="https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals">[18]</a></sup>

The product ingested a broad range of inputs: calls, emails, pitch decks, blog posts, product marketing materials, and internal training documents — all to ensure that the AI's coaching was grounded in the company's actual context rather than generic sales advice.<sup><a href="https://www.fabius.io/">[20]</a></sup>

Fabius was listed in the Zoom marketplace, indicating at least one formal integration partnership beyond Gong and Chorus.<sup><a href="https://www.linkedin.com/company/fabius-technologies">[21]</a></sup> The product required these third-party integrations to function, which meant Fabius was architecturally dependent on the continued cooperation of the very incumbents it was trying to augment.

What distinguished Fabius from Gong or Chorus directly was the customization layer. Gong's AI coaching features were trained on aggregate data across thousands of companies. Fabius's pitch was that generic benchmarks miss the point — what matters is whether *your* reps are following *your* process. The rubric-based scoring was designed to encode company-specific methodology rather than industry averages.

---

## Market Position

### Target Customers

Fabius targeted B2B sales organizations that had already invested in a formal sales methodology and a conversation intelligence platform, but were not getting reliable adherence or visibility into execution. The ideal customer was a mid-market or enterprise company running a structured process like MEDDPICC or SPIN Selling, with a sales team large enough that individual rep coaching was becoming a bottleneck for managers.

Named early customers included Airbyte, the open-source data integration company, and Fermat, a YC-adjacent e-commerce startup.<sup><a href="https://www.ycombinator.com/companies/fabius">[22]</a></sup> Both were within the YC network, which raises a question about whether Fabius's early traction reflected genuine product-market fit or the social capital of a shared accelerator community.

### Market Size

The sales intelligence and conversation analytics market was large and growing during Fabius's operating period. Gong alone was valued at $7.25 billion in its 2021 Series E, having raised over $500 million in total funding. Chorus was acquired by ZoomInfo in 2021 for $575 million. The broader sales enablement software market was estimated at several billion dollars annually, with AI-powered coaching tools representing a fast-growing subsegment.

Fabius was not competing for the entire market. Its positioning as a methodology-enforcement layer meant it was targeting a specific workflow within companies that had already purchased Gong or Chorus — a narrower addressable market, but one with potentially high willingness to pay if the product demonstrably improved win rates.

### Competition

The competitive landscape was the central structural challenge for Fabius. The company faced pressure from three directions simultaneously.

**Incumbent expansion.** Gong and Chorus were not standing still. Both platforms were actively building AI coaching features during 2022 and 2023, using the same LLM technology Fabius was deploying. Gong's "Gong Engage" and AI-powered deal intelligence features were announced and expanded during this period. A company that had already paid for Gong had a strong default preference for using Gong's native coaching tools rather than adding a second vendor.

**New AI-native entrants.** The W23 YC batch itself included multiple companies in the sales AI space. The broader 2023 cohort of AI startups produced dozens of tools targeting sales workflows — call summarization, email generation, CRM automation — many of which overlapped with Fabius's feature set.

**Point solution fatigue.** Enterprise buyers in 2023 were simultaneously being pitched dozens of AI add-ons for their existing stacks. Procurement teams were consolidating vendors, not adding them. A two-person startup asking a VP of Sales to integrate yet another tool into their workflow faced a high bar for demonstrating differentiated ROI.

---

## Business Model

Fabius operated on a B2B SaaS model, selling to sales organizations on what was likely a per-seat or per-team subscription basis, though no pricing has been publicly disclosed. The product required integration with existing conversation intelligence platforms (Gong, Chorus, Zoom), meaning the sales motion involved both a technical integration step and a change management component — the sales team needed to adopt a new coaching workflow on top of tools they were already using.

The company's early revenue of approximately $100,000–$200,000 before the YC batch started suggests it was closing deals, though whether these were annual contracts, monthly subscriptions, or pilot arrangements is unknown.<sup><a href="https://www.linkedin.com/in/andrewkday/">[23]</a></sup> The presence of named enterprise-adjacent customers like Airbyte suggests the average contract value was meaningful, but the customer base appears to have been small. No pricing page, tier structure, or contract terms have been made public.

---

## Traction

Andy Day stated on LinkedIn that Fabius generated approximately $100,000–$200,000 in early revenue before the W23 batch began — described as "proof we could close deals."<sup><a href="https://www.linkedin.com/in/andrewkday/">[23]</a></sup> Named customers included Airbyte and Fermat, both YC-connected companies, which used Fabius to score calls and identify qualification gaps.<sup><a href="https://www.ycombinator.com/companies/fabius">[22]</a></sup>

Day also referenced a $6.2 million preemptive investment from General Catalyst before Demo Day.<sup><a href="https://www.linkedin.com/in/andrewkday/">[23]</a></sup> This claim is critically ambiguous. No corresponding funding record appears on Crunchbase or Tracxn for Fabius, and the context of Day's LinkedIn post is unclear — it is possible the reference is to a different company or a hypothetical scenario used to illustrate a lesson about YC. This report treats the General Catalyst figure as unverified and does not incorporate it into the funding narrative.

Beyond these data points, public traction signals are sparse. The @FabiusTech Twitter account has never posted a single tweet since its creation in September 2020 and has accumulated only 50 followers.<sup><a href="https://x.com/FabiusTech">[24]</a></sup> No Hacker News launch post exists. No G2, Capterra, or Reddit reviews have been found. The company appears to have operated entirely through direct outbound sales, with no inbound or community-driven growth motion.

---

## Post-Mortem

Fabius has not published a formal post-mortem, and neither founder has publicly characterized the company as having failed. What follows is an analysis of the structural and strategic factors that most likely explain why the company did not scale, based on available evidence.

### Insufficient Capital to Compete in a Rapidly Commoditizing Market

The most significant factor in Fabius's apparent stagnation was the mismatch between its funding and the competitive environment it entered.

Fabius's only confirmed institutional funding was a pre-seed round from Y Combinator, with the amount disputed between $125,000 and $500,000.<sup><a href="https://tracxn.com/d/companies/fabius/__9SqVGM5ZuyIcC2E375vW_UmtnjzoIPvxyLuCJP-JnJM/funding-and-investors">[11]</a></sup><sup><a href="https://www.linkedin.com/company/fabius-technologies">[12]</a></sup> No follow-on round has been recorded on Crunchbase or Tracxn as of February 2026.<sup><a href="https://www.crunchbase.com/organization/fabius-66e4">[25]</a></sup> The company it was most directly competing with — Gong — had raised over $500 million and was valued at $7.25 billion at its peak. Chorus had been acquired by ZoomInfo for $575 million.

A two-person team with pre-seed capital cannot match the product velocity, sales capacity, or marketing reach of incumbents at that scale. More critically, Gong and Chorus were actively building AI coaching features using the same underlying LLM technology during 2022 and 2023. The window in which Fabius's methodology-scoring approach represented a genuine capability gap was closing as the incumbents shipped native versions of similar features.

The team's attempt to address this was to position Fabius as a complement to Gong rather than a competitor — an overlay that added customization the incumbents could not match. This was a reasonable strategic choice, but it created a dependency: Fabius needed Gong and Chorus to remain open platforms and to not build the specific customization features Fabius offered. As incumbents expanded their AI roadmaps, that bet became increasingly difficult to sustain.

### Over-Reliance on the YC Network for Early Customers

Fabius's named customers — Airbyte and Fermat — were both YC-adjacent companies.<sup><a href="https://www.ycombinator.com/companies/fabius">[22]</a></sup> The YC network is a powerful distribution channel for early sales, but it is not a proxy for broader market demand. YC companies are unusually receptive to trying new tools from fellow founders, have higher risk tolerance for unproven products, and often make purchasing decisions based on relationship rather than rigorous vendor evaluation.

The absence of any named customers outside the YC ecosystem, combined with zero inbound marketing activity (no tweets, no press, no HN posts), suggests Fabius may not have successfully translated its YC-network traction into repeatable sales motions in the broader enterprise market. Enterprise sales organizations outside the startup world have longer procurement cycles, more stakeholders, and higher proof-of-value requirements than early-stage YC companies.

There is no evidence the team attempted to address this gap through a structured outbound sales process, a channel partnership, or a content marketing strategy. The @FabiusTech account's complete silence across its entire existence — zero tweets in over four years — is consistent with a company that was entirely dependent on founder-led direct sales with no scalable acquisition channel.<sup><a href="https://x.com/FabiusTech">[24]</a></sup>

### Architectural Dependency on Incumbents

Fabius's product required integration with Gong, Chorus, or Zoom to function.<sup><a href="https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals">[10]</a></sup> This was a deliberate positioning choice — rather than rebuilding call recording and transcription infrastructure, Fabius focused on the intelligence layer. The tradeoff was that Fabius's value proposition was contingent on the continued availability and openness of those integrations.

This dependency created two compounding risks. First, any incumbent that chose to restrict API access or build competing features natively could eliminate Fabius's distribution channel and product differentiation simultaneously. Second, the sales motion required convincing a prospect to add a new vendor on top of a platform they had already paid for — a harder sell than replacing an existing tool.

The Zoom marketplace listing suggests Fabius recognized this dependency and tried to formalize at least one integration relationship.<sup><a href="https://www.linkedin.com/company/fabius-technologies">[21]</a></sup> But marketplace listings alone do not generate enterprise pipeline, and there is no evidence of a formal partnership with Gong or Chorus that would have provided co-selling or distribution benefits.

### Team Size Constraint

Fabius operated as a two-person company throughout its documented history.<sup><a href="https://www.ycombinatorcompanies.com/company/fabius">[26]</a></sup> For a B2B SaaS product targeting enterprise sales organizations, this created a structural ceiling on what the company could accomplish simultaneously: product development, customer success, sales, and fundraising all competed for the same two people's time.

Enterprise sales organizations require hands-on onboarding, ongoing support, and regular business reviews to retain and expand. A two-person team that is also building the product cannot deliver that level of service to more than a handful of customers. This constraint likely limited both the number of customers Fabius could serve and the quality of the experience those customers received — making it harder to generate the case studies and references needed to close new deals.

<media-tweet url="https://x.com/FabiusTech" author="@FabiusTech" date="2020-09" text="[No tweets posted — account created September 2020, zero posts as of February 2026, 50 followers]"></media-tweet>

---

## Key Lessons

- **Positioning as a complement to incumbents is a viable strategy only if the incumbents cannot build the same feature natively.** Fabius bet that Gong and Chorus would not build customizable methodology-scoring features. That bet required constant monitoring and a contingency plan. When incumbents began expanding their AI coaching roadmaps in 2022–2023, Fabius had neither the resources to pivot nor the differentiation to survive the overlap. Any startup building on top of a platform must have a clear answer to the question: what happens when the platform ships this feature?

- **Early revenue from a captive network is a weak signal of product-market fit.** Fabius's first customers were YC-adjacent companies — a community with unusually high trust in fellow founders and low procurement friction. Closing deals within that network is a necessary first step, but it does not validate that the product can win in a competitive enterprise sales process. Founders should deliberately seek customers outside their immediate network early, even if those deals are harder to close, to stress-test the value proposition against realistic buyer behavior.

- **A zero-investment public presence is a compounding disadvantage for B2B startups.** Fabius's Twitter account posted nothing in over four years.<sup><a href="https://x.com/FabiusTech">[24]</a></sup> No press coverage, no HN post, no content marketing. In a market where buyers research vendors before taking a sales call, the absence of any public signal makes it harder to generate inbound leads, build credibility with enterprise procurement teams, and attract talent. For a two-person team, content and community are among the few scalable distribution channels available — and Fabius did not use them.

- **The YC office hours anecdote contains a real lesson about prioritization under resource constraints.** Andy Day's account of being ejected from office hours for debating a naming decision illustrates a broader pattern: early-stage teams with limited runway can lose weeks to decisions that do not move revenue.<sup><a href="https://www.linkedin.com/in/andrewkday/">[8]</a></sup> The team appears to have course-corrected — the pre-batch revenue hustle suggests genuine execution discipline — but the episode is a reminder that the cost of distraction is higher for a two-person team than for any other organizational structure.

---

## Sources

1. [Y Combinator – Fabius Company Profile](https://www.ycombinator.com/companies/fabius)
2. [YC Launch Post – "Fabius: Unlock the Power of Your Sales Process"](https://www.ycombinator.com/launches/I37-fabius-unlock-the-power-of-your-sales-process-and-drive-urgency-to-win-more-deals)
3. [Crunchbase – Fabius Organization Profile](https://www.crunchbase.com/organization/fabius-66e4)
4. [Crunchbase – Neil Madsen Profile](https://www.crunchbase.com/person/neil-madsen-d773)
5. [LinkedIn – Andy Day Profile](https://www.linkedin.com/in/andrewkday/)
6. [LinkedIn – Fabius Technologies Company Page](https://www.linkedin.com/company/fabius-technologies)
7. [Fabius.io – Product Website](https://www.fabius.io/)
8. [Tracxn – Fabius Funding and Investors](https://tracxn.com/d/companies/fabius/__9SqVGM5ZuyIcC2E375vW_UmtnjzoIPvxyLuCJP-JnJM/funding-and-investors)
9. [YC Companies Directory – Fabius](https://www.ycombinatorcompanies.com/company/fabius)
10. [GitHub – Andy Day (@adayNU)](https://github.com/adayNU)
11. [X / Twitter – @FabiusTech](https://x.com/FabiusTech)31:T44f,Fabius 2026 is a lightweight methodology enforcement layer for mid-market sales teams priced out of Gong. It lives in HubSpot, ingests call transcripts from any source (Gong, Chorus, Zoom), and automatically scores every deal against a sales leader's actual framework — MEDDPICC, SPICED, or custom — then surfaces qualification gaps and auto-populates CRM fields. No native recording, no real-time coaching, no complexity.

The market shift is LLM inference cost collapse. In 2022, extracting structured qualification data from calls was prohibitively expensive. Now GPT-4o makes it viable at $499/month for teams of 10–50 reps. Gong's $1,200+ per seat pricing leaves this segment completely underserved, and they're actively moving upmarket.

Go-to-market is HubSpot App Marketplace as the primary channel, with founder outreach into RevOps communities (RevGenius, Pavilion) where sales ops leaders congregate. Win on three axes: SMB pricing, company-specific rubric customization that Gong can't match, and zero implementation friction. Target: 10 paying customers at $500+/month within 90 days.32:T757,
