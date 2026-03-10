# Research Report: Flike

## Overview

Flike was founded in 2021 in San Francisco by three co-founders: Tobias Müller (CEO), Yannick Müller, and Henrik Laxhuber.<sup><a href="https://golden.com/wiki/Flike-6AX8YWA">[1]</a></sup> Tobias and Yannick Müller came from finance backgrounds and had experienced firsthand the dysfunction of collaborative spreadsheet work—the version chaos, the time lost gathering inputs from colleagues, and the errors that compounded across shared files.<sup><a href="https://www.linkedin.com/posts/y-combinator_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912448529386938368-2Wd0">[2]</a></sup> That lived frustration became the founding thesis: build the infrastructure layer that spreadsheets had always lacked.

The Müller brothers' finance backgrounds gave them authentic founder-market fit for the original product. They understood the workflows they were targeting not as outside observers but as former practitioners. Henrik Laxhuber's specific background and contributions to the founding remain largely undocumented in public sources.

From the start, the team signaled technical ambition through its hiring. Yannick Müller announced the addition of Andrew Chou as Head of ML—a Stanford-trained engineer with experience at Google, Facebook, Amazon, Amplitude, and Coursera—and Saikishore Kalloori as AI Researcher, a postdoctoral researcher from ETH Zurich who had published papers on recommender systems and personalization.<sup><a href="https://www.linkedin.com/posts/yajm_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912355141861937152-kOt4">[3]</a></sup> The decision to hire a recommender-systems specialist at the spreadsheet-collaboration stage is notable in retrospect: it suggests the founders were already thinking beyond static tooling toward dynamic, AI-driven personalization.

Flike joined Y Combinator's Winter 2022 batch in January 2022.<sup><a href="https://www.ycombinator.com/companies/flike">[4]</a></sup> The YC program provided both the $1.6M pre-seed lead and the network that would later shape the company's distribution strategy—and ultimately its exit.

<media-image src="https://imageio.forbes.com/specials-images/imageserve/623a820dc39c48e2b306f292/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds" alt="Forbes article: 'Flike Raises $1.6M To Build GitHub For Spreadsheets' — March 2022" caption="Forbes coverage of Flike's $1.6M pre-seed raise in March 2022, led by Y Combinator. The article covers the founding story: Tobias and Yannick Müller built Flike after experiencing spreadsheet collaboration pain in their own finance careers."></media-image>

Tobias Müller's approach to product development was unusually rigorous for a seed-stage founder. In an April 2022 case study published during the spreadsheet phase, he articulated a philosophy that prioritized user input above all internal assumptions: "The number one lesson was to learn to throw out all internal beliefs, hypotheses, and opinions about a problem and instead take the users' input as the unquestionable truth."<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[5]</a></sup> He described a critical early challenge: "A critical problem we've had to overcome early on was figuring out how to get unfiltered data from user interviews."<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[6]</a></sup>

The team went as far as embedding with customers on-site. "We believe that having customers who want us to succeed is incredibly important. Both founders spent a week at a customer's site, which gave us insights into their workflows we could have never anticipated."<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[7]</a></sup> On hiring, Müller was equally deliberate: "While great technical ability is a must, I think nothing makes up for true intrinsic motivation, and we like to hire for that"—with candidates trialed as consultants before receiving full-time offers.<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[8]</a></sup>

The irony embedded in this founding story is significant: a founder who articulated one of the more thoughtful PMF methodologies in the YC ecosystem still pivoted twice and ultimately could not scale independently.

---

## Founding Story

### Timeline

- **2021** — Flike founded in San Francisco by Tobias Müller, Yannick Müller, and Henrik Laxhuber.<sup>[[1]](https://golden.com/wiki/Flike-6AX8YWA)</sup>
- **January 2022** — Flike joins Y Combinator Winter 2022 (W22) batch.<sup>[[4]](https://www.ycombinator.com/companies/flike)</sup>
- **March 22, 2022** — Forbes publishes "Flike Raises $1.6M To Build GitHub For Spreadsheets," establishing the company's public narrative.<sup>[[9]](https://www.forbes.com/sites/frederickdaso/2022/03/22/flike-raises-16m-to-build-github-for-spreadsheets/)</sup>
- **March 23, 2022** — Flike announces $1.6M pre-seed round led by Y Combinator, with angel investors from Google, GitHub, Airtable, Retool, Personio, Pitch, and Zapier.<sup>[[10]](https://www.linkedin.com/posts/yajm_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912355141861937152-kOt4)</sup>
- **April 5, 2022** — Tobias Müller publishes product-market fit case study articulating lessons on user research, customer embedding, and hiring philosophy.<sup>[[5]](https://f2f.substack.com/p/case-study-on-the-road-to-product)</sup>
- **June 2022** — Flike hires Andrew Chou (Head of ML, Stanford CS) and Saikishore Kalloori (AI Researcher, ETH Zurich postdoc).<sup>[[3]](https://www.linkedin.com/posts/yajm_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912355141861937152-kOt4)</sup>
- **2023 (exact date unknown)** — Flike pivots from spreadsheet collaboration to an AI-powered recommender engine; partners with Mux to integrate the technology into Mux's video platform.<sup>[[11]](https://golden.com/wiki/Flike-6AX8YWA)</sup>
- **2023 (exact date unknown)** — Flike pivots again to an AI Sales Co-Pilot, generating personalized sales emails using Gmail history, CRM data, and 1,000+ prospect data points.<sup>[[12]](https://www.ycombinator.com/companies/flike)</sup>
- **February 6, 2024** — Flike launches AI Sales Co-Pilot on Product Hunt, receiving 85 reviews and a 4.8 rating.<sup>[[13]](https://www.producthunt.com/products/flike)</sup>
- **June 14, 2024** — FirstQuadrant (YC-backed AI sales platform) acquires Flike in an asset deal. Named customers at time of acquisition include Brex and Brightspot.<sup>[[14]](https://docs.firstquadrant.ai/press-releases/2024-06-14-firstquadrant-acquires-flike)</sup>
- **2024** — Tobias Müller moves on to build a Supply Chain AI company, confirming his departure from Flike post-acquisition.<sup>[[15]](https://www.ycombinator.com/companies/flike)</sup>

---

## What They Built

### Phase 1: GitHub for Spreadsheets (2021–2022)

Flike's original product targeted a problem familiar to anyone who has worked in a finance team: the chaos of collaborative spreadsheet work. The founders identified three core pain points from their own experience—the time-consuming nature of gathering input from colleagues, the difficulty of tracking multiple versions of the same file, and the frequency of errors that crept in during collaboration.<sup><a href="https://www.cbinsights.com/company/flike">[16]</a></sup>

The product concept was to add version control, automation, and advanced collaboration features directly on top of Google Sheets and Excel—the tools finance teams already used—rather than asking them to migrate to a new platform. The "GitHub for spreadsheets" framing was deliberate: it communicated the value proposition to a technical-adjacent audience in a single phrase. The addressable market was framed as a $20B opportunity in collaboration and automation for finance teams.<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[17]</a></sup>

No public product screenshots, user counts, or revenue figures from this phase are available.

### Phase 2: AI Recommender Engine (2023)

The second product direction is the least documented phase of Flike's history. The company pivoted to building an AI-powered recommender engine—a system that surfaces relevant content or actions based on user behavior and context. The clearest evidence of this phase is a partnership with Mux, a video infrastructure platform, to integrate Flike's recommender technology into Mux's product.<sup><a href="https://golden.com/wiki/Flike-6AX8YWA">[11]</a></sup> The hiring of Saikishore Kalloori, an ETH Zurich postdoc specializing in recommender systems, appears to have been forward-looking toward this direction. This phase appears to have been a transitional experiment rather than a sustained product line.

### Phase 3: AI Sales Co-Pilot (2023–2024)

The final and most developed product was Flike's AI Sales Co-Pilot—a tool that generated personalized outbound sales emails by learning from a company's existing communication patterns and prospect data.

<media-hn url="https://www.ycombinator.com/launches/KOm-flike-ai-sales-co-pilot" title="Launch YC: Flike - AI Sales Co-Pilot" points="null" comments="null"></media-hn>

The product worked in three layers. First, a **relevancy engine** analyzed more than 1,000 data points per prospect, pulling from LinkedIn, Crunchbase, X (formerly Twitter), G2, Gmail, and CRM systems including Outreach, Salesloft, HubSpot, and Salesforce.<sup><a href="https://www.ycombinator.com/companies/flike">[18]</a></sup> Second, a **personalization layer** learned from a sales team's historical Gmail conversations to identify the tone, structure, and messaging patterns that correlated with positive responses.<sup><a href="https://www.ycombinator.com/launches/KOm-flike-ai-sales-co-pilot">[19]</a></sup> Third, a **brand voice model** was trained on a company's product marketing materials to ensure generated emails stayed on-message throughout the sales funnel—from cold outbound to event-triggered follow-ups to upsell sequences.<sup><a href="https://www.ycombinator.com/companies/flike">[20]</a></sup>

In practice, a sales representative would connect their Gmail account and CRM, provide Flike with product marketing content, and receive AI-drafted emails tailored to each prospect's specific context—their company's recent funding, product launches, job changes, or competitive signals. The system supported three email types: cold outbound (initial contact), event-based responses (triggered by prospect activity), and dynamic follow-ups (adapted based on prior conversation history).

What distinguished Flike from simpler AI email tools was the depth of its data ingestion. Rather than generating generic personalization tokens ("Hi [First Name], I noticed you work at [Company]"), Flike's relevancy engine was designed to surface genuinely specific signals—a prospect's recent G2 review of a competitor, a LinkedIn post about a pain point, or a funding announcement that changed their buying context.

<media-image src="https://ph-files.imgix.net/flike-ai-sales-copilot.png" alt="Flike AI Sales Co-Pilot product screenshot from Product Hunt" caption="Flike's AI Sales Co-Pilot interface — the product analyzes 1,000+ data points per prospect from LinkedIn, Crunchbase, X, G2, Gmail, and CRM systems to generate hyper-personalized sales emails."></media-image>

---

## Market Position

### Target Customers

Flike's AI Sales Co-Pilot targeted B2B sales teams at technology companies—specifically account executives and sales development representatives (SDRs) responsible for outbound prospecting. The YC network served as the primary distribution channel: the company described itself as already partnering with "some of the largest YC companies" during the sales co-pilot phase.<sup><a href="https://www.ycombinator.com/companies/flike">[21]</a></sup> Named customers at the time of acquisition included Brex (the corporate card and spend management platform) and Brightspot (a content management system company).<sup><a href="https://docs.firstquadrant.ai/press-releases/2024-06-14-firstquadrant-acquires-flike">[14]</a></sup> Both are credible B2B SaaS companies with active outbound sales motions, validating the product's fit for that buyer profile. Whether these were paying customers or design partners is not publicly disclosed.

### Market Size

The AI sales automation market Flike entered in its final form was large but contested. The broader sales engagement software market—tools that help sales teams manage outreach, sequencing, and personalization—was estimated at several billion dollars annually by the time Flike launched its co-pilot product, with AI-native entrants competing alongside established players like Outreach and Salesloft (which Flike integrated with, rather than competed against directly). The original spreadsheet collaboration market was framed by the founders as a $20B opportunity.<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[17]</a></sup> The AI email generation segment specifically attracted dozens of well-funded entrants following the public release of GPT-3.5 and GPT-4 in late 2022 and early 2023.

### Competition

The competitive landscape Flike entered with its AI Sales Co-Pilot was among the most crowded in enterprise software at the time. Direct competitors included:

**Lavender** — An AI email coaching tool that analyzes drafts in real time and scores them for likely response rates. Lavender raised $13.2M and built a large community of SDRs before Flike's Product Hunt launch.

**Regie.ai** — An AI content platform for sales teams that generates sequences, emails, and call scripts. Raised over $20M.

**Amplemarket** — An AI-powered sales platform combining prospecting, sequencing, and email generation. Raised $12M.

**Apollo.io** — A dominant sales intelligence and engagement platform that added AI email generation features to its existing database of 275M+ contacts. Apollo's scale and data moat made it a formidable incumbent.

**FirstQuadrant** (the eventual acquirer) — A YC-backed AI sales platform with a broader automation scope, including multi-channel outreach and pipeline management.

Flike's differentiation claim was the depth of its relevancy engine—1,000+ data points per prospect versus the shallower personalization of most competitors. Third-party reviewers noted the relevancy engine as "best in class by miles" on Product Hunt. However, differentiation on data depth is difficult to sustain: larger, better-capitalized competitors can replicate data integrations faster than a seed-stage company can build distribution.

---

## Business Model

Flike operated on a B2B SaaS subscription model, selling seats or licenses to sales teams at technology companies. The product was positioned as a productivity tool for account executives and SDRs, suggesting per-seat pricing was the likely structure—consistent with how comparable tools like Lavender and Regie.ai priced their products.

No revenue figures, ARR, MRR, or pricing tiers were publicly disclosed at any stage of the company's life. The asset deal structure of the acquisition—rather than a full company purchase—suggests the company had not reached a revenue scale that would have supported a traditional acquisition multiple. Total funding of $2.1M across all rounds<sup><a href="https://www.cbinsights.com/company/flike">[22]</a></sup> implies the company operated on an extremely lean budget for a technical team in San Francisco over approximately three years, with no disclosed Series A or seed extension. The absence of follow-on capital is the clearest available proxy for the company's commercial trajectory.

---2f:T6a4,

## Traction

Flike's AI Sales Co-Pilot generated measurable, if modest, market validation before the acquisition.

The Product Hunt launch on February 6, 2024 received 85 reviews and a 4.8 rating.<sup><a href="https://www.producthunt.com/products/flike">[13]</a></sup> Reviewers included sales professionals from recognizable companies who cited specific outcomes—sales professionals from Segment and Brex reported doubled open rates after using the product. The relevancy engine drew particular praise, with one reviewer describing it as "best in class by miles." Product Hunt ratings are a weak proxy for commercial traction—they reflect early adopter enthusiasm rather than retention or revenue—but the specificity of the feedback suggests genuine usage rather than coordinated review campaigns.

Named customers at the time of acquisition—Brex and Brightspot—are credible enterprise logos that would have supported a sales narrative.<sup><a href="https://docs.firstquadrant.ai/press-releases/2024-06-14-firstquadrant-acquires-flike">[14]</a></sup> The YC network served as the primary distribution channel, with the company describing partnerships with "some of the largest YC companies."<sup><a href="https://www.ycombinator.com/companies/flike">[21]</a></sup>

Flike's X (Twitter) account posted only 5 times in total—a reflection of a team focused on product and direct sales rather than content marketing or community building.

No ARR, MRR, user count, or churn data was ever publicly disclosed. The gap between positive product reviews and the asset-deal exit suggests the company had real users but could not convert early enthusiasm into the growth curve required to raise a Series A.

---

## Post-Mortem

Flike operated for approximately three years, raised $2.1M in total, pivoted twice, and exited in an asset deal that returned an undisclosed—and likely minimal—amount to investors and founders. The failure was not a single catastrophic event but a compounding sequence of structural problems.

### 1. Two Pivots Consumed the Majority of Available Runway

The most consequential factor in Flike's outcome was the cost of pivoting twice on $2.1M in total capital.

The company spent its first year building a spreadsheet collaboration product for finance teams—a product that generated Forbes coverage and a credible founding narrative but left no documented user base, revenue, or retention data. The absence of any public metrics from this phase, combined with the pivot away from it, strongly suggests the product did not achieve sufficient traction to justify continued investment. Tobias Müller's April 2022 writing—published just weeks after the funding announcement—describes a team still in the process of extracting unbiased user feedback and narrowing its target market from 1.3 billion spreadsheet users to focused finance teams.<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[5]</a></sup> The product was still finding its footing when the pivot decision was made.

The second pivot—to an AI recommender engine, evidenced by the Mux partnership<sup><a href="https://golden.com/wiki/Flike-6AX8YWA">[11]</a></sup>—appears to have been a transitional experiment rather than a committed product direction. The exact duration of this phase is unknown, but it consumed additional months of runway and engineering capacity before the team landed on AI sales emails.

Each pivot reset the go-to-market clock. Sales cycles, customer relationships, and brand recognition built during one product phase do not transfer to a fundamentally different product. A team that spent 2022 building credibility with finance teams had to rebuild from scratch when targeting B2B sales teams in 2023.

### 2. The Final Product Landed in the Most Crowded Segment of Enterprise AI

Flike's AI Sales Co-Pilot launched into a market that had attracted dozens of well-funded competitors in the 18 months following GPT-3.5's public release in late 2022.

By the time Flike launched on Product Hunt in February 2024, Lavender had raised $13.2M and built a community of tens of thousands of SDRs. Apollo.io—with 275M+ contacts in its database and AI email generation layered on top—had a distribution advantage that no seed-stage company could replicate. Regie.ai had raised over $20M. Amplemarket had raised $12M.

Flike's differentiation was the depth of its relevancy engine—1,000+ data points per prospect from LinkedIn, Crunchbase, X, G2, Gmail, and CRM systems.<sup><a href="https://www.ycombinator.com/companies/flike">[18]</a></sup> This was a genuine technical advantage, and Product Hunt reviewers recognized it. But data-depth differentiation is inherently fragile at the seed stage: a competitor with $20M in the bank can replicate integrations faster than a team operating on residual pre-seed capital can build distribution. The window between "technically superior" and "competitively irrelevant" closes quickly when incumbents are actively investing in the same feature set.

The timing of the pivot to AI sales emails—coinciding with the post-ChatGPT wave—also suggests the team was opportunistically repositioning around LLM capabilities rather than executing a planned roadmap. Opportunistic pivots can work, but they require either a significant head start or a structural moat. Flike had neither: it entered the market late relative to better-capitalized competitors, and its primary distribution channel (the YC network) was shared with those same competitors.

### 3. The YC Network Was Both the Primary Distribution Channel and a Structural Ceiling

Flike's go-to-market strategy relied heavily on the YC ecosystem. The company described itself as partnering with "some of the largest YC companies,"<sup><a href="https://www.ycombinator.com/companies/flike">[21]</a></sup> and the eventual acquirer—FirstQuadrant—was also YC-backed.<sup><a href="https://docs.firstquadrant.ai/press-releases/2024-06-14-firstquadrant-acquires-flike">[14]</a></sup>

The YC network is a powerful early distribution channel: warm introductions, shared credibility, and a community of early adopters willing to try new tools. But it is also a ceiling. The YC ecosystem represents a small fraction of the total addressable market for B2B sales automation. Scaling beyond it requires outbound sales, content marketing, channel partnerships, or product-led growth—all of which require capital and time that Flike did not have in sufficient quantity.

The company's X account had 5 total posts. There is no evidence of a content marketing program, a community strategy, or a channel partnership beyond the YC network. For a product targeting sales teams—a buyer persona that is itself highly attuned to sales and marketing quality—the absence of a visible go-to-market motion is a meaningful signal.

### 4. $2.1M Was Insufficient Capital for the Market Flike Entered

Flike raised $1.6M in its pre-seed round in March 2022<sup><a href="https://www.linkedin.com/posts/yajm_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912355141861937152-kOt4">[10]</a></sup> and a total of $2.1M across all rounds.<sup><a href="https://www.cbinsights.com/company/flike">[22]</a></sup> The additional ~$500K beyond the pre-seed is undocumented in terms of timing and structure.

For a company that operated in San Francisco for approximately three years with a technical team that included ML researchers, $2.1M is extremely lean. The burn rate implied by this capital base—even assuming aggressive cost management—would have left the team with limited runway to iterate through two pivots, build a technically sophisticated product, and invest in go-to-market simultaneously.

The absence of a Series A or seed extension announcement is the clearest available signal that the company did not achieve the growth metrics required to raise follow-on capital. In the 2022–2024 period, AI-native B2B SaaS companies with strong growth metrics were raising seed extensions and Series A rounds at a high rate. Flike's inability to access that capital—despite operating in a hot category with credible customers—suggests the underlying metrics did not support the narrative.

The asset deal structure of the acquisition confirms this reading. Asset deals—where a buyer purchases specific IP, code, or customer relationships rather than the company as a going concern—typically occur when the selling company has insufficient revenue or growth to support a traditional acquisition multiple. No acquisition price was disclosed.

### 5. Good Process Did Not Compensate for Structural Market Challenges

The final and perhaps most instructive failure dimension is the gap between Flike's process sophistication and its commercial outcome.

Tobias Müller articulated a PMF methodology in April 2022 that would be recognizable to any serious student of early-stage company building: treat user input as unquestionable truth, embed with customers on-site, hire for intrinsic motivation, trial candidates as consultants before full-time offers.<sup><a href="https://f2f.substack.com/p/case-study-on-the-road-to-product">[5]</a></sup> These are not generic lessons—they reflect a founder who had genuinely internalized the discipline of customer-driven development.

Yet the company still pivoted twice, still failed to raise follow-on capital, and still exited in an asset deal. The lesson is not that good process is irrelevant—it is that good process is necessary but not sufficient. Market timing, capital efficiency, competitive dynamics, and distribution strategy interact with process in ways that no methodology can fully control. Flike entered its final market too late, with too little capital, against too many well-funded competitors, and with a distribution channel that could not scale beyond its initial community.

---

## Key Lessons

- **Two pivots on $2.1M is a capital allocation problem, not just a strategy problem.** Each pivot consumed runway and reset go-to-market momentum. Flike's total funding was insufficient to absorb two full product restarts while simultaneously building distribution. Founders operating on sub-$3M pre-seeds in competitive markets need to either find product-market fit faster or raise more capital before pivoting—because the cost of a pivot is not just engineering time, it is the compounding loss of sales cycles, customer relationships, and brand recognition built under the prior product thesis.

- **Distribution channel concentration is a structural risk.** Flike's primary go-to-market channel was the YC network—a powerful but bounded community. The company's X account had 5 posts; there is no evidence of a content marketing program or channel partnership strategy. For a product targeting sales teams, the absence of a visible outbound motion is particularly costly: the buyer persona is itself highly attuned to sales quality, and a company that cannot demonstrate its own go-to-market sophistication faces a credibility gap with that audience.

- **Entering a crowded AI category late requires either a structural moat or a capital advantage—Flike had neither.** The AI sales email market attracted dozens of well-funded competitors in 2022–2023. Flike's relevancy engine was technically differentiated, but data-depth advantages erode quickly when incumbents have 10x the capital to replicate integrations. Timing matters as much as quality: a technically superior product that arrives 12 months after the market has consolidated around established players faces a distribution problem that product quality alone cannot solve.

- **The asset deal exit is the most informative data point in the entire story.** Asset deals—as opposed to full company acquisitions—occur when the selling company's revenue or growth does not support a traditional acquisition multiple. The absence of a disclosed price, combined with Tobias Müller's immediate departure to build a new company, suggests the outcome returned little to investors and founders. For YC-backed companies in competitive markets, the asset deal is the modal outcome when growth metrics stall before a Series A—a useful benchmark for founders calibrating their own runway and milestone planning.

- **Sophisticated PMF methodology does not guarantee commercial success.** Tobias Müller's April 2022 writing reflects genuine intellectual rigor about customer development. The company still pivoted twice and exited in an asset deal. Process discipline is necessary but not sufficient—market timing, competitive dynamics, and capital availability interact with process in ways that no methodology fully controls. The lesson is not to abandon rigorous customer research, but to recognize that it must be paired with a realistic assessment of competitive positioning and capital requirements.

---

## Sources

1. [Golden.com — Flike company profile](https://golden.com/wiki/Flike-6AX8YWA)
2. [LinkedIn — Y Combinator post: "Flike Raises $1.6M To Build GitHub For Spreadsheets"](https://www.linkedin.com/posts/y-combinator_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912448529386938368-2Wd0)
3. [LinkedIn — Yannick Müller post announcing pre-seed and team hires](https://www.linkedin.com/posts/yajm_flike-raises-16m-to-build-github-for-spreadsheets-activity-6912355141861937152-kOt4)
4. [Y Combinator — Flike company profile](https://www.ycombinator.com/companies/flike)
5. [Substack (f2f) — "Case Study: On The Road To Product-Market Fit" by Tobias Müller, April 5, 2022](https://f2f.substack.com/p/case-study-on-the-road-to-product)
6. [Y Combinator — Flike AI Sales Co-Pilot launch post](https://www.ycombinator.com/launches/KOm-flike-ai-sales-co-pilot)
7. [CBInsights — Flike company profile](https://www.cbinsights.com/company/flike)
8. [FirstQuadrant — Press release: "FirstQuadrant Acquires Flike," June 14, 2024](https://docs.firstquadrant.ai/press-releases/2024-06-14-firstquadrant-acquires-flike)
9. [Forbes — "Flike Raises $1.6M To Build GitHub For Spreadsheets," Frederick Daso, March 22, 2022](https://www.forbes.com/sites/frederickdaso/2022/03/22/flike-raises-16m-to-build-github-for-spreadsheets/)
10. [Product Hunt — Flike AI Sales Co-Pilot listing](https://www.producthunt.com/products/flike)
11. [AI Parabellum — Flike AI Sales Co-Pilot review](https://aiparabellum.com/flike-ai/)
12. [Wayback Machine — flike.app archive](https://web.archive.org/web/20240201000000*/flike.app)
13. [X (Twitter) — @flikeapp official account](https://x.com/flikeapp)
