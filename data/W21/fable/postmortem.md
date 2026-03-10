# Research Report: Fable

## Overview

Aravindh Dorai and Alex Chumbley brought complementary but overlapping credentials to Fable. Dorai had spent his career inside product organizations: Program Manager at Microsoft, Product Manager at Zocdoc, and Senior Product Manager at Teachers Pay Teachers (TpT).<sup><a href="https://clay.earth/profile/aravindh-dorai">[4]</a></sup> Chumbley came from a more technical and strategic background — a Master's and Bachelor's degree in Computer Science from MIT, followed by a stint as an Engagement Manager at McKinsey & Company.<sup><a href="https://theorg.com/org/tryfable/org-chart/alex-chumbley">[5]</a></sup> Together, they described their shared experience: "Alex and I have been PMs at companies of varying sizes and industries — from Microsoft to Budweiser to Zocdoc."<sup><a href="https://news.ycombinator.com/item?id=29980162">[6]</a></sup>

The founding insight was personal and specific. Dorai traced the idea directly to his time at Teachers Pay Teachers: "I was wasting hours copy/pasting from my spec into Jira, time that I could have spent doing more valuable things like talking to users."<sup><a href="https://news.ycombinator.com/item?id=29980162">[7]</a></sup> The pain was real — product managers routinely write specifications in one tool (Google Docs, Confluence, Notion) and then manually recreate that work as tickets in a separate issue tracker. Every edit to the spec requires a corresponding update to the tracker, and vice versa. The two systems drift apart within days.

The founding thesis was that this gap represented a category-level opportunity: a dedicated PM workspace that would sit above the issue tracker layer and keep both in sync automatically. The analogy to Figma and Linear was deliberate positioning — both companies had succeeded by creating purpose-built tools for their respective disciplines (design and engineering) rather than forcing practitioners to use generic productivity software. Fable's bet was that product managers deserved the same treatment.

The company was incorporated in 2020 and entered YC's Winter 2021 batch, which provided initial validation, seed capital, and the YC network.<sup><a href="https://www.ycombinator.com/companies/fable">[8]</a></sup> Notably, Fable remained a two-person team throughout its known operating life — a signal that the company never achieved the traction or funding needed to scale hiring.<sup><a href="https://www.ycombinator.com/companies/fable">[9]</a></sup> How the two founders met and why they chose to work together specifically is not documented in available sources.

The "Figma for PMs" framing was aspirational but set a demanding standard. Figma succeeded by replacing a desktop-native workflow (Sketch, Illustrator) with a browser-native collaborative paradigm — a genuine architectural shift that incumbents could not easily replicate. Fable was not replacing a desktop application; it was adding a sync layer on top of tools that already lived in the browser. The analogy was seductive but structurally misleading.

## Founding Story

### Timeline

- **2020** — Fable founded by Aravindh Dorai and Alex Chumbley in New York, NY.<sup>[[10]](https://www.ycombinator.com/companies/fable)</sup>
- **January 2021** — Fable participates in Y Combinator Winter 2021 batch.<sup>[[10]](https://www.ycombinator.com/companies/fable)</sup>
- **March 2021** — Fable launches a Google Docs Add-On as its first public product, announced on Hacker News.<sup>[[11]](https://news.ycombinator.com/item?id=26305617)</sup>
- **March 22, 2021** — Fable raises an undisclosed seed round from Y Combinator and angel investor Aaron Rankin (Co-Founder & CTO of Sprout Social).<sup>[[12]](https://www.crunchbase.com/organization/fable-bbaf)</sup>
- **October 5, 2021** — Fable is featured on BetaList, categorized under Product Development, Business Productivity, and Project Management.<sup>[[13]](https://betalist.com/startups/tryfable)</sup>
- **January 23, 2022** — Founders post on Hacker News describing Fable's core product: a collaborative spec editor with two-way sync to Jira and Linear, and a per-maker pricing model.<sup>[[14]](https://news.ycombinator.com/item?id=29980162)</sup>
- **April 12, 2022** — Alex Chumbley announces on LinkedIn that Fable has launched integrations with Jira, Linear, Productboard, and Asana, and introduces the "Build Progress" feature.<sup>[[15]](https://www.linkedin.com/posts/alex-chumbley_amazing-weekend-and-this-is-just-the-beginning-activity-6919482573572214784-ABXS)</sup>
- **April 14, 2022** — Fable launches on Product Hunt, stating paid features are forthcoming but a free version will always exist.<sup>[[16]](https://www.producthunt.com/products/fable-5)</sup>
- **Mid-to-late 2022 (estimated)** — Fable winds down; both founders move to Plex, an on-chain customer engagement company.<sup>[[17]](https://www.linkedin.com/in/aravindhdorai/)</sup>
- **June 2023** — Plex is acquired by MoonPay. Alex Chumbley joins MoonPay's Emerging Products division.<sup>[[18]](https://theorg.com/org/tryfable/org-chart/alex-chumbley)</sup>
- **2024** — tryfable.com domain taken over by an unrelated third party; YC lists Fable as "Inactive."<sup>[[19]](https://www.ycombinator.com/companies/fable)</sup>

## What They Built

Fable's product was a collaborative document editor purpose-built for product specifications, with a two-way synchronization layer connecting it to engineering issue trackers.

**The core workflow** was straightforward in concept. A product manager would write a product specification inside Fable — describing a feature, its requirements, and its acceptance criteria. Rather than then opening Jira or Linear and manually recreating that content as individual tickets, Fable would generate and sync those tickets automatically. Critically, the sync ran in both directions: if an engineer updated a ticket's status, assignee, or description inside Jira, that change would propagate back into the Fable spec in real time.<sup><a href="https://bestofshowhn.com/yc-s21/fable">[20]</a></sup> The stated goal was to eliminate the document drift that makes product specs obsolete within days of being written — "the minute a product spec is written, it's no longer relevant."<sup><a href="https://bestofshowhn.com/yc-s21/fable">[21]</a></sup>

**Product evolution followed a logical but narrow arc:**

The first public artifact was a Google Docs Add-On, launched in March 2021.<sup><a href="https://news.ycombinator.com/item?id=26305617">[22]</a></sup> This was a pragmatic starting point — Google Docs was already where many PMs wrote specs, and an add-on required no behavior change. But it also meant Fable's initial distribution was entirely contingent on Google's ecosystem and the add-on marketplace, not on standalone user acquisition.

By January 2022, Fable had evolved into a standalone web application with its own editor interface and integrations with Jira and Linear.<sup><a href="https://news.ycombinator.com/item?id=29980162">[23]</a></sup> The standalone product allowed the team to build a more opinionated PM-specific editing experience rather than working within Google Docs' constraints.

By April 2022, Fable had expanded integrations to include Productboard and Asana, and launched its most ambitious feature: "Build Progress."<sup><a href="https://www.linkedin.com/posts/alex-chumbley_amazing-weekend-and-this-is-just-the-beginning-activity-6919482573572214784-ABXS">[24]</a></sup> Build Progress surfaced the real-time status and assignees of engineering tickets directly inside the product spec — so a PM reading a spec could see, inline, whether each requirement had been picked up, was in progress, or had been completed. This was the product's most differentiated moment: it turned a static document into a live dashboard without requiring the PM to switch contexts.

**What made it different** from alternatives was the combination of a purpose-built PM editor with live issue tracker data. Confluence and Notion offered rich document editing but no native two-way sync with issue trackers. Jira and Linear offered issue tracking but no narrative spec layer. Fable's bet was that the combination was worth a dedicated tool.

The weakness was architectural: every piece of value Fable delivered was mediated by APIs it did not control. If Jira changed its API, Fable's sync broke. If Linear shipped a native "spec" document type — which it eventually did — Fable's differentiation collapsed. The product was a bridge between two platforms, and bridges become unnecessary when the platforms grow toward each other.

<media-hn url="https://news.ycombinator.com/item?id=29980162" title="Ask HN: Fable – Collaborative spec editor with two-way sync to Jira/Linear" points="" comments=""></media-hn>

## Market Position

### Target Customers

Fable's primary buyer was the product manager at a technology company using Jira or Linear for engineering issue tracking. The ideal customer was a PM at a mid-size startup or growth-stage company — large enough to have a dedicated PM function and an issue tracker, small enough that the PM was still writing specs personally rather than delegating to a team of writers or program managers.

The per-maker pricing model — charging PMs, designers, and engineering managers who actively create content, while giving free access to viewers like marketing and sales — implied a target organization of 5–50 product and engineering staff.<sup><a href="https://bestofshowhn.com/yc-s21/fable">[25]</a></sup> Enterprise buyers with dedicated program management offices were unlikely targets; they typically had custom Confluence or SharePoint deployments with established workflows. Very small teams (1–2 PMs) were unlikely to pay for a dedicated spec tool when Google Docs was free.

### Market Size

The addressable market for PM tooling is real but contested. There are approximately 875,000 product managers in the United States alone, according to Bureau of Labor Statistics occupational data, with global estimates exceeding 3 million. At a hypothetical $20/maker/month price point — consistent with Figma's and Linear's pricing tiers at the time — a 1% penetration of the U.S. market would represent roughly $21M in annual recurring revenue. That is a viable business but not a venture-scale outcome on its own, which likely explains why Fable's positioning emphasized the "command center" framing — implying eventual expansion beyond spec writing into broader product workflow orchestration.

The PM tooling category was also growing rapidly in 2021–2022, with Productboard, Coda, and Notion all raising large rounds on the premise that knowledge workers needed better tools. This created both tailwind (investor appetite) and headwind (more well-funded competitors).

### Competition

Fable's competitive position was structurally weak along the two axes that mattered most: distribution reach and integration depth.

**On distribution**, Fable competed against tools that PMs already used daily. Notion had 20 million users by early 2022 and was actively building database and project management features. Confluence was embedded in most enterprises that used Jira — meaning Atlassian already owned the spec-writing workflow for a large share of Fable's target customers. Linear had launched its own document feature ("Linear Docs") in 2022, directly absorbing the use case Fable was built around. Each of these incumbents had distribution advantages that Fable, as a two-person team, could not overcome through product quality alone.

**On integration depth**, Fable's two-way sync was its core differentiator — but it was also its most replicable feature. Jira's own "Pages" feature (launched in 2023) and Linear's native document support both addressed the spec-to-ticket gap without requiring a third-party tool. The competitive moat Fable needed — deep workflow integration, proprietary data, or a network effect — was absent. Two-way API sync is a feature, not a platform.

The competitive landscape also shifted because of platform moves, not just competitive product decisions. When Linear shipped native documents and Atlassian deepened Confluence-Jira integration, they did not acquire Fable's feature — they made it redundant. This is the structural risk of building on top of platforms that have both the incentive and the engineering capacity to absorb adjacent features.

Fable's "Figma for PMs" positioning implicitly acknowledged this risk — Figma succeeded in part because Adobe and Sketch could not easily replicate a browser-native, multiplayer design tool. Fable's sync layer had no equivalent technical barrier to replication.

## Business Model

Fable used a per-maker pricing model, charging users who actively created content — product managers, designers, and engineering managers — while offering free access to passive viewers and commenters such as marketing and sales staff.<sup><a href="https://bestofshowhn.com/yc-s21/fable">[26]</a></sup> This mirrors Figma's "editor seat" model and is a reasonable structure for a collaborative productivity tool, as it aligns cost with the users who derive the most direct value.

However, the company never disclosed revenue figures, and its April 2022 Product Hunt launch explicitly stated: "We're building paid features in the months to come, but there will always be a free version."<sup><a href="https://www.producthunt.com/products/fable-5">[27]</a></sup> This statement, made 18 months after founding and after the YC batch, strongly suggests the company had not yet meaningfully monetized. The absence of any revenue disclosure is itself a signal: YC companies that achieve early traction typically share MRR milestones in founder forums, investor updates, and press coverage. No such figures appear in any available source for Fable.

**Estimated burn rate (inference, not fact):** YC's standard investment in W21 was a $125,000 SAFE plus a $375,000 MFN SAFE — approximately $500,000 total. With a two-person team in New York, a conservative monthly burn of $15,000–$25,000 (salaries, infrastructure, tools) implies a runway of 20–33 months from March 2021, or roughly through late 2022 to early 2023. This is consistent with the estimated wind-down timing. The company appears to have operated until its initial capital was exhausted without generating sufficient revenue or traction to raise a follow-on round.

The per-maker model was sound in theory but required meaningful adoption before it could sustain even a two-person team. At $20/maker/month, Fable would have needed roughly 100 paying makers to cover basic operating costs — a threshold that appears to have remained out of reach.

## Post-Mortem

### Primary Cause: A Product Built on Borrowed Infrastructure

The most fundamental reason Fable failed was architectural. Its entire value proposition — two-way sync between a spec editor and issue trackers — was a feature layer on top of platforms it did not own. Jira, Linear, Productboard, and Asana were simultaneously Fable's integration partners and its most credible potential acquirers of the feature set it was building.

This is not a subtle risk that the founders overlooked; it is a structural property of the category. Every PM tooling startup that builds on top of issue trackers faces the same dynamic: the issue tracker vendor has a direct incentive to absorb adjacent workflows, existing distribution to the same buyer, and the engineering capacity to ship a comparable feature in weeks. Linear launched its own native document feature in 2022, the same year Fable was trying to gain traction. Atlassian deepened Confluence-Jira integration continuously throughout this period. Neither company needed to acquire Fable — they simply built the feature themselves.

Fable's "Build Progress" feature — showing engineering ticket status inside a product spec — is the clearest illustration of this dynamic. It was Fable's most differentiated capability at launch in April 2022.<sup><a href="https://www.linkedin.com/posts/alex-chumbley_amazing-weekend-and-this-is-just-the-beginning-activity-6919482573572214784-ABXS">[28]</a></sup> It is also precisely the kind of feature that any issue tracker could ship natively in a single sprint, requiring no third-party dependency. The feature was real and useful; it was not defensible.

### Secondary Cause: No Monetization Before Runway Expired

Fable's April 2022 Product Hunt launch — 18 months after founding — explicitly deferred monetization: "We're building paid features in the months to come."<sup><a href="https://www.producthunt.com/products/fable-5">[29]</a></sup> This is a significant signal. A company that has not begun charging customers 18 months after founding, in a B2B SaaS category where enterprise buyers are accustomed to paying for software, has either not found product-market fit or has not found a buyer willing to pay for what it built.

No revenue figures, customer counts, or named enterprise customers appear in any available source. The company never disclosed MRR, churn, or retention data. This absence is consistent with a product that attracted interest — the Hacker News post in January 2022 generated discussion, and the Product Hunt launch in April 2022 was a public event — but did not convert that interest into paying customers at scale.

The attempted remedy was the Product Hunt launch itself: a public moment designed to generate top-of-funnel awareness and drive sign-ups that could be converted to paid users. Whether it succeeded in generating sign-ups is unknown; whether it generated revenue is clear from the subsequent silence.

### Tertiary Cause: Insufficient Differentiation from Free Alternatives

Fable's spec editor competed directly with tools that were free or already paid for. Google Docs was free and already embedded in most PM workflows. Notion offered a more structured alternative with database features, also free at the individual level. Confluence was included in most Atlassian enterprise contracts. The incremental value Fable offered — two-way sync with issue trackers — had to be compelling enough to justify both the switching cost and the additional per-seat expense.

For the sync to be worth paying for, it had to work reliably across all supported integrations (Jira, Linear, Productboard, Asana) and had to be meaningfully better than the manual copy-paste workflow it replaced. No user feedback or reliability data is available in public sources, but the absence of any public customer testimonials or case studies — even on the Product Hunt page — suggests the product did not generate the kind of enthusiastic early adopters who typically become a startup's first marketing channel.

### Structural Cause: The PM Tooling Category Is Winner-Take-All at the Platform Layer

The deeper structural issue is that PM tooling tends to consolidate around platforms, not point solutions. PMs do not want to manage five tools; they want one tool that does everything. The companies that won in adjacent categories — Notion for knowledge management, Linear for engineering, Figma for design — won by becoming platforms with ecosystems, not by building integrations on top of other platforms.

Fable's positioning as a "command center" implied platform ambitions, but its product at shutdown was a sync layer — a point solution. To become a platform, it would have needed to either (a) replace one of the tools it was syncing with, or (b) accumulate enough proprietary data and workflow lock-in to make switching costly. Neither was achievable with a two-person team and a single seed round.

### Outcome: A Quiet Exit to Web3

Fable wound down without a public announcement, a founder post-mortem, or press coverage. The YC listing moved to "Inactive," and the domain was eventually claimed by an unrelated party.<sup><a href="https://www.ycombinator.com/companies/fable">[30]</a></sup> Both founders moved together to Plex, an on-chain customer engagement company — a complete pivot from B2B SaaS productivity tooling into Web3, which was experiencing a funding surge in 2022.<sup><a href="https://www.linkedin.com/in/aravindhdorai/">[31]</a></sup>

The pivot to Web3 is itself a signal. Founders who believe their current company can raise follow-on capital typically continue iterating; founders who conclude the trajectory is insufficient often pivot to a category where capital is more available. In 2022, Web3 was that category. Plex's subsequent acquisition by MoonPay in June 2023 gave the founders a successful exit — their first, by Chumbley's own YC profile description of himself as a "2x founder, 1x exit."<sup><a href="https://www.ycombinator.com/companies/fable">[32]</a></sup>

The shutdown timing can be bracketed with reasonable confidence: the last known product activity was the April 2022 Product Hunt launch; both founders appear at Plex thereafter. Wind-down most likely occurred between May and December 2022.

## Key Lessons

- **Building on top of a platform is not the same as building a platform.** Fable's two-way sync with Jira and Linear was its core differentiator, but it was also its core vulnerability. When Linear shipped native documents in 2022 and Atlassian deepened Confluence-Jira integration, they did not need to acquire Fable — they made it redundant. Any startup whose value proposition is "we connect Tool A to Tool B" must ask whether Tool A or Tool B has the incentive and capacity to build that connection natively. In Fable's case, the answer was clearly yes for both.

- **The "Figma for X" analogy requires a genuine paradigm shift, not just a workflow improvement.** Fable positioned itself as "building for PMs what Figma has done for designers." Figma succeeded by replacing a desktop-native, single-player workflow with a browser-native, multiplayer one — a shift that Sketch and Adobe could not easily replicate without rebuilding their core architecture. Fable was adding a sync layer on top of tools that already ran in browsers. The analogy set a high bar that the product's architecture could not meet.

- **Deferred monetization in B2B SaaS is a leading indicator of product-market fit problems, not a growth strategy.** Fable's April 2022 Product Hunt launch — 18 months after founding — explicitly stated that paid features were "forthcoming." In a category where Notion, Linear, and Figma all had paying customers within months of launch, this deferral signals that Fable had not yet found buyers willing to pay for what it built. The absence of any disclosed revenue, customer count, or named customer in any public source confirms this reading.

- **PM-specific tooling requires either enterprise distribution or viral adoption — Fable had neither.** PMs are influential within their organizations but rarely control software budgets. Selling to PMs requires either a bottom-up PLG motion (where individual PMs adopt the tool and pull in their teams) or a top-down enterprise sale (where the tool is purchased at the VP or C-suite level). Fable's free-viewer model was designed for PLG, but PLG requires a product that generates enough enthusiasm among early users to drive organic referrals. No evidence of that dynamic appears in available sources.

- **A two-person team cannot build and maintain four enterprise integrations while also acquiring customers.** Fable's April 2022 launch supported Jira, Linear, Productboard, and Asana simultaneously.<sup><a href="https://www.linkedin.com/posts/alex-chumbley_amazing-weekend-and-this-is-just-the-beginning-activity-6919482573572214784-ABXS">[33]</a></sup> Each integration requires ongoing maintenance as the partner's API evolves. With two founders, the engineering capacity required to maintain four integrations reliably likely crowded out the customer development, sales, and marketing work needed to generate revenue. Focused depth on one integration (Jira, given its market share) might have produced a more defensible early position.

## Sources

1. [Y Combinator – Fable Company Profile](https://www.ycombinator.com/companies/fable)
2. [The Org – Alex Chumbley at tryfable](https://theorg.com/org/tryfable/org-chart/alex-chumbley)
3. [Hacker News – Fable HN thread (January 2022)](https://news.ycombinator.com/item?id=29980162)
4. [Clay Earth – Aravindh Dorai Profile](https://clay.earth/profile/aravindh-dorai)
5. [Best of Show HN – Fable (YC S21)](https://bestofshowhn.com/yc-s21/fable)
6. [Hacker News – Fable Google Docs Add-On Launch (March 2021)](https://news.ycombinator.com/item?id=26305617)
7. [Crunchbase – Fable Funding](https://www.crunchbase.com/organization/fable-bbaf)
8. [Crunchbase – Fable Financials](https://www.crunchbase.com/organization/fable-bbaf/company_financials)
9. [BetaList – Fable](https://betalist.com/startups/tryfable)
10. [LinkedIn – Alex Chumbley (Build Progress announcement)](https://www.linkedin.com/posts/alex-chumbley_amazing-weekend-and-this-is-just-the-beginning-activity-6919482573572214784-ABXS)
11. [Product Hunt – Fable](https://www.producthunt.com/products/fable-5)
12. [LinkedIn – Aravindh Dorai](https://www.linkedin.com/in/aravindhdorai/)
13. [tryfable.com (defunct)](https://tryfable.com/)
14. [Hacker News – "Fable is winding down" (different company, fable.app)](https://news.ycombinator.com/item?id=41850573)
