# Research Report: Natero

## Overview

Natero was a B2B SaaS customer success platform founded in May 2012 by Craig Soules and Garth Goodson in Mountain View, California. The company built software that ingested granular product usage data from SaaS vendors, integrated it with CRM, support, and billing systems, and applied machine learning to predict customer churn and identify expansion opportunities. Natero participated in Y Combinator's Summer 2012 batch and raised a total of $3.42 million across two rounds before being acquired by Freshworks in May 2019.<sup><a href="https://www.ycombinator.com/companies/natero">[1]</a></sup>

Natero was not a failure in the conventional sense — it achieved product-market fit, generated enough revenue to fund its own expansion after 2014, and was acquired by a strategic buyer. The constraint was structural: in a winner-take-most category where primary competitor Gainsight raised over $100 million in venture capital, Natero's $3.42 million total raise left it unable to compete on distribution, brand, or integrations at scale. The acquisition by Freshworks was the rational terminal outcome for a technically differentiated product that was more valuable inside a larger CRM suite than as a standalone subscription.

Freshworks acquired Natero on May 21, 2019, rebranding the technology as Freshsuccess and integrating it into the Freshworks 360 suite. Both founders transitioned to Freshworks roles before departing in 2023 to co-found Springtail, a scale-out replicated database startup — returning to the infrastructure roots that preceded Natero.<sup><a href="https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/">[2]</a></sup>

<report-gallery>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/f015cf85720ead0fa510cb99c99d24dc92ec0a41.jpg" alt="Natero on Y Combinator" caption="Natero's Y Combinator profile avatar — the company's public face during its S12 batch, when Soules and Goodson were still searching for the right vertical to apply their data infrastructure expertise."></media-image>
<media-image src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008918865/original/tYnhdI0Rg88yb3qiZfD1Pn3gYmLIFZAfpA.png?1689667812" alt="Natero platform Slack integration UI" caption="A screenshot of Natero's Slack integration feature, showing how customer success managers received real-time alerts inside their collaboration tools — a workflow layer that made Natero's ML predictions actionable without leaving existing toolchains."></media-image>
<media-image src="https://s3.amazonaws.com/cdn.freshdesk.com/data/helpdesk/attachments/production/50008918447/original/a3w59V6vrKVol1xiKkZdCliYJIpuoQiyUw.png?1689667453" alt="Natero Infusionsoft integration UI" caption="The Natero-Infusionsoft integration screen, illustrating the platform's strategy of embedding into existing CRM and marketing workflows — the same integration depth that ultimately made Natero more valuable as a Freshworks feature than as a standalone product."></media-image>
</report-gallery>

## Founding Story

Craig Soules and Garth Goodson brought an unusual profile to a customer success startup: both held PhDs from Carnegie Mellon University and had spent the preceding decade building enterprise infrastructure at scale.<sup><a href="https://www.natero.com/company/">[3]</a></sup>

Soules spent six years at HP Labs leading R&D on a distributed database system. Goodson spent eight years at NetApp as a founding member of the Advanced Technology Group within the CTO's Office.<sup><a href="https://www.natero.com/company/">[4]</a></sup> Neither had a background in sales, customer success, or SaaS go-to-market — a fact that would shape both the company's product strengths and its eventual limitations.

The founding insight came from Soules's time at HP. He observed a persistent gap between the data processing tools available to engineers — powerful, flexible, but requiring deep technical expertise — and the tools available to business users, who needed actionable insights and readable charts rather than raw database access.<sup><a href="https://www.idgconnect.com/article/3577558/natero-machine-learning-for-saas-customer-retention.html">[5]</a></sup> The problem was not a lack of data; it was a lack of infrastructure to translate data into decisions for non-technical operators.

Soules later described the founding aim directly: "I co-founded Natero in 2012 with the aim of making companies more data-driven. That ultimately led to the launch of Natero's customer success platform in late 2015 and its eventual acquisition by Freshworks in 2019."<sup><a href="https://www.success.ai/profile/Craig-Soules-85498767857">[6]</a></sup>

The path to customer success was not immediate. Before settling on B2B SaaS, Soules investigated eCommerce and the Internet of Things as potential verticals for the same underlying data-translation thesis.<sup><a href="https://www.idgconnect.com/article/3577558/natero-machine-learning-for-saas-customer-retention.html">[7]</a></sup> This deliberate market search — testing the thesis across multiple domains before committing — suggests disciplined validation rather than trend-chasing. The SaaS customer success category was chosen because it offered a clear, measurable outcome (churn reduction), a data-rich environment (product usage logs), and a customer base (SaaS companies) that was already predisposed to data-driven decision-making.

Natero was incorporated in May 2012 and joined Y Combinator's Summer 2012 batch the same year.<sup><a href="https://contactout.com/Craig-Soules-82593338">[8]</a></sup> YC provided early validation, network access, and seed capital — situating Natero at the beginning of the customer success management (CSM) software category's formation. Gainsight, which would become the dominant player, had been founded only a year earlier in 2011. The founders were early, but not first.

The division of responsibilities followed naturally from their backgrounds: Soules took the CEO role, handling product vision and external positioning; Goodson took the CTO role, leading platform architecture. No public record details how they met beyond their shared CMU affiliation, but the complementary infrastructure expertise — distributed systems at HP and NetApp — suggests a pre-existing professional relationship.

## Timeline

- **May 2012** — Craig Soules and Garth Goodson co-found Natero in Mountain View, CA.<sup>[[9]](https://contactout.com/Craig-Soules-82593338)</sup>
- **August 2012** — Natero participates in Y Combinator S12 batch and raises an undisclosed seed round.<sup>[[10]](https://www.crunchbase.com/funding_round/natero-seed--5faf4767)</sup>
- **2014** — Natero raises $3.3M Series A from Merus Capital (lead), Salesforce Ventures, Y Combinator, and Andreessen Horowitz Seed — its last disclosed funding round.<sup>[[11]](https://blog.natero.com/natero-unveils-customer-success-platform)</sup>
- **September 2015** — Natero posts a Machine Learning Engineer job on Hacker News, signaling active hiring ahead of product launch.<sup>[[12]](https://news.ycombinator.com/item?id=10155385)</sup>
- **December 2015** — Natero officially launches its customer success platform.
- **February 11, 2016** — Natero publicly announces platform availability; CEO Soules positions it against intuition-based competitors Gainsight and Totango.<sup>[[13]](https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html)</sup>
- **2016** — Natero included in Gartner's Hype Cycle for CRM Sales 2016 and CRM Vendor Guide 2016 in Customer Success Management categories.<sup>[[14]](https://pressreleasejet.com/news/natero-included-in-two-recent-gartner-crm-reports-for-its-customer-success-platform.html)</sup>
- **October 2016** — Freshdesk selects Natero as its Customer Success Management Platform, citing data-volume handling superiority.<sup>[[15]](https://finance.yahoo.com/news/freshdesk-leverages-natero-customer-success-140000022.html)</sup>
- **February 6, 2019** — Natero acquires Irish customer success consulting firm CustomerLink to expand EMEA operations; CustomerLink founder John Kelly becomes VP of EMEA.<sup>[[16]](https://www.siliconrepublic.com/business/natero-customerlink-customer-success)</sup>
- **May 21, 2019** — Freshworks acquires Natero for an undisclosed amount; acquisition triggered by Natero seeking additional capital to expand.<sup>[[17]](https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/)</sup>
- **September 2019** — Natero's technology rebranded as Freshsuccess and integrated into the Freshworks 360 suite.<sup>[[18]](https://diginomica.com/refresh-2019-can-freshworks-change-cx-market-better-customer-success-metrics)</sup>
- **September 2023** — Craig Soules departs Freshworks and co-founds Springtail, a scale-out replicated database startup, with Garth Goodson.<sup>[[19]](https://www.ycombinator.com/companies/natero)</sup>

<media-hn url="https://news.ycombinator.com/item?id=10155385" title="Natero (YC S12) is hiring a Machine Learning Engineer" points="" comments=""></media-hn>

## What They Built

Natero's core product was a customer success platform designed for B2B SaaS companies — specifically, the customer success managers (CSMs) responsible for ensuring that enterprise software customers renewed their subscriptions and expanded their usage over time.

The platform operated in three layers. First, it ingested data: Natero captured granular product usage data directly from a SaaS vendor's own application, tracking which features customers used, how frequently, and at what depth. It then pulled in data from CRM systems (Salesforce, HubSpot), support platforms (Zendesk, Freshdesk), and billing tools (Stripe, Zuora) to build a unified customer profile.<sup><a href="https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html">[20]</a></sup>

Second, it analyzed: Natero applied machine learning models to continuously evaluate hundreds of usage and business metrics simultaneously, generating churn risk scores and expansion opportunity signals for each customer account.<sup><a href="https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html">[21]</a></sup> The ML layer was the company's primary differentiator. As Soules stated at launch: "Existing customer success solutions are based solely on intuition and best-guesses rather than data science and business intelligence."<sup><a href="https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html">[22]</a></sup>

Third, it surfaced insights: CSMs received prioritized task lists, automated alerts, and account health dashboards that translated the ML outputs into specific actions — which accounts to call, which to flag for executive review, which were ready for an upsell conversation. Goodson described the design philosophy: "SaaS companies have massive amounts of data about their customers. The trick is to aggregate and mine this data to uncover actionable insights — without the need to involve IT or engineering teams every time."<sup><a href="https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html">[23]</a></sup>

The platform also included workflow management tools: playbooks (standardized processes for common CSM scenarios), automated email triggers, and Slack integration for real-time alerts — making ML predictions actionable inside the tools CSMs already used daily.

<media-youtube id="bPTX-Ma3ayU" title="Natero product demo from the Freshdesk partnership announcement, October 2016"></media-youtube>

The three-year gap between founding (May 2012) and product launch (late 2015) is notable. No public record documents what the product looked like during this period — whether there were earlier beta versions, significant architectural pivots, or extended customer discovery. The most plausible inference is that building a production-grade ML pipeline capable of ingesting heterogeneous SaaS data at scale required substantial engineering investment before the product was ready for commercial deployment. The September 2015 Hacker News job posting for a Machine Learning Engineer suggests the ML layer was still being staffed as late as three months before launch.<sup><a href="https://news.ycombinator.com/item?id=10155385">[24]</a></sup>

Post-launch, the product evolved to add an EMEA-focused services layer through the February 2019 acquisition of CustomerLink, a Dublin-based customer success consulting firm.<sup><a href="https://www.siliconrepublic.com/business/natero-customerlink-customer-success">[25]</a></sup> This move — bundling professional services with software — is common in enterprise sales but unusual for a company of Natero's size, and suggests that closing deals in Europe required more hands-on implementation support than the product alone could provide.

After the Freshworks acquisition, the technology was rebranded as Freshsuccess and integrated into the Freshworks 360 customer experience suite, confirming that the product was viable enough to absorb into a larger platform but not to scale independently.<sup><a href="https://diginomica.com/refresh-2019-can-freshworks-change-cx-market-better-customer-success-metrics">[26]</a></sup>

## Market Position

### Target Customers

Natero's primary customers were customer success teams at B2B SaaS companies — specifically, companies large enough to have dedicated CSMs but small enough that they lacked internal data science resources to build churn prediction models themselves. The product was positioned for the mid-market: companies with enough customers to generate meaningful usage data but without the engineering bandwidth to analyze it. Known customers included Freshdesk, WhiteHat Security, and Rainforest QA — all B2B SaaS companies with subscription revenue models where churn was a material business risk.<sup><a href="https://pressreleasejet.com/news/natero-included-in-two-recent-gartner-crm-reports-for-its-customer-success-platform.html">[27]</a></sup>

### Market Size

The customer success management software category emerged in the early 2010s as SaaS subscription models made churn a board-level metric. The logic was straightforward: in a recurring revenue business, retaining existing customers is as important as acquiring new ones, and the CSM function needed dedicated tooling just as sales had CRM. The category grew substantially through the decade, with Gainsight alone reaching a reported $100M+ ARR before its 2020 acquisition by Vista Equity Partners. Natero entered at the category's formation — a genuine timing advantage — but the market's growth also attracted well-capitalized competitors who could outspend on sales, marketing, and integrations.

### Competition

Natero's primary competitors were Gainsight and Totango, which Soules described in 2016 as "slightly larger" than Natero.<sup><a href="https://www.idgconnect.com/article/3577558/natero-machine-learning-for-saas-customer-retention.html">[28]</a></sup> The competitive landscape is best understood along two axes: **distribution reach** (the ability to land enterprise accounts through brand recognition, sales teams, and ecosystem partnerships) and **product depth** (the sophistication of the underlying analytics and ML).

Natero competed on product depth. Its ML-driven approach was a genuine technical differentiator in 2016, when most CSM platforms relied on rule-based health scores — manually configured thresholds that flagged accounts when usage dropped below a set level. Natero's models evaluated hundreds of variables simultaneously and updated continuously, which was architecturally more sophisticated.

Gainsight competed on distribution. It raised over $100 million in venture capital — roughly 30 times Natero's total raise — and used that capital to build a large enterprise sales force, sponsor the Pulse conference (which became the defining industry event for customer success professionals), and develop deep integrations with Salesforce. By the time Natero launched publicly in late 2015, Gainsight had already established itself as the category default for enterprise buyers. The Pulse conference alone gave Gainsight a community moat that no amount of ML sophistication could replicate quickly.

This is the structural dynamic that constrained Natero: in enterprise software, distribution advantages compound. A large sales team generates more customer relationships, which generates more data, which improves the product, which justifies a larger sales team. Natero's ML differentiation was real but not durable — Gainsight could acquire or build similar capabilities once the market validated their importance, and its distribution advantage would remain. The competitive landscape did not shift because of a platform move or a regulatory change; it shifted because Gainsight's capital deployment bought the brand and ecosystem presence that Natero could not match on $3.42 million.

Totango occupied a middle position — larger than Natero but less dominant than Gainsight — and competed primarily on ease of implementation for smaller SaaS companies. Neither Gainsight nor Totango was displaced by Natero's ML claims; both continued to grow through the period when Natero was operating.

The Freshdesk relationship, which began in October 2016, illustrates a different competitive dynamic: the risk of a strategic customer becoming a strategic acquirer. Freshdesk selected Natero over other evaluated solutions specifically because of its data-volume handling capabilities.<sup><a href="https://finance.yahoo.com/news/freshdesk-leverages-natero-customer-success-140000022.html">[29]</a></sup> That relationship gave Freshworks (Freshdesk's parent) three years of direct product exposure before the acquisition conversation began — making Freshworks the most informed and most motivated potential acquirer in the market.

## Business Model

Natero operated on a subscription-based revenue model, with pricing structured around the number of users and the volume of data processed.<sup><a href="https://app.dealroom.co/companies/natero">[30]</a></sup> This is standard for enterprise SaaS CSM platforms, where pricing typically scales with the size of the customer's customer base — a natural alignment between the vendor's cost structure (data storage and compute) and the customer's value received (more accounts managed).

The company never disclosed revenue figures publicly. The absence of ARR or growth rate data is itself a signal: companies that achieve strong revenue growth in competitive categories typically publicize those numbers to attract talent, customers, and follow-on capital. Natero's silence on revenue metrics, combined with its decision not to raise additional equity after the 2014 Series A, suggests the company reached a stable but modest revenue base — sufficient to fund operations but insufficient to justify the growth multiples that would attract a Series B at a meaningful valuation.

Soules confirmed to TechCrunch that after the 2014 Series A, Natero funded its expansion through revenue rather than additional equity.<sup><a href="https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/">[31]</a></sup> With a reported headcount of approximately 11 employees at the time of acquisition and a five-year operating period on roughly $3.42 million in total funding, the company was clearly operating lean. Assuming a blended fully-loaded cost of $150,000–$200,000 per employee annually, a team of 11 would require $1.65M–$2.2M per year just in personnel costs — meaning the company needed to be generating meaningful revenue to sustain operations after the seed capital was deployed. This is an inference from available data, not a confirmed figure.

The February 2019 CustomerLink acquisition added a professional services revenue stream, though the terms were undisclosed. Bundling consulting with software is a common enterprise sales tactic but typically compresses margins and adds operational complexity — a trade-off that may have accelerated the decision to seek additional capital, which in turn triggered the Freshworks acquisition conversation.

## Traction

Natero achieved several concrete traction milestones, though the company never disclosed ARR, customer count, or growth rates.

Analyst recognition arrived in 2016, when Gartner included Natero in both its Hype Cycle for CRM Sales 2016 and its CRM Vendor Guide 2016 in the Customer Success Management categories.<sup><a href="https://pressreleasejet.com/news/natero-included-in-two-recent-gartner-crm-reports-for-its-customer-success-platform.html">[32]</a></sup> Gartner inclusion at this stage of a company's life typically requires a minimum number of enterprise customer references and a demonstrated product — a meaningful signal for a company that had launched publicly only months earlier.

The Freshdesk partnership in October 2016 was the most significant traction event. Freshdesk — a company with tens of thousands of customers of its own — evaluated multiple CSM platforms and selected Natero specifically for its ability to handle data volume at scale.<sup><a href="https://finance.yahoo.com/news/freshdesk-leverages-natero-customer-success-140000022.html">[33]</a></sup> Winning a customer of Freshdesk's scale validated both the product's technical architecture and its enterprise readiness.

Known customers — Freshdesk, WhiteHat Security, and Rainforest QA — represent a coherent segment: B2B SaaS companies with subscription revenue models and enough customers to generate meaningful usage data. The customer list is small by public record, but the quality of logos suggests Natero was competing and winning in its target segment.

The CustomerLink acquisition in February 2019 implied EMEA customer demand sufficient to justify a dedicated regional presence, though the scale of that demand was not disclosed.

## Post-Mortem

### Primary Cause: Capital Asymmetry in a Distribution-Dependent Category

The central constraint on Natero's independent trajectory was not product quality — it was the gap between its $3.42 million total raise and the capital deployed by its primary competitor. Gainsight raised over $100 million in venture funding during the same period Natero was operating on seed and Series A capital. That capital asymmetry translated directly into distribution advantages that Natero could not overcome through product differentiation alone.

In enterprise software, distribution compounds. Gainsight's capital funded a large direct sales force, the Pulse conference (which became the industry's defining annual event and gave Gainsight a community moat), and deep Salesforce ecosystem integrations that made Gainsight the default recommendation for any Salesforce-native enterprise. By the time Natero launched publicly in late 2015, Gainsight had already established category leadership. Natero's ML differentiation was real in 2016, but it was not durable: Gainsight could acquire or build similar capabilities once the market validated their importance, while its distribution advantage would persist.

Natero's response to this dynamic was to compete on product depth and revenue efficiency rather than scale. Soules confirmed that after the 2014 Series A, the company funded expansion through revenue — an operationally disciplined choice that preserved independence but capped growth velocity.<sup><a href="https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/">[34]</a></sup> The outcome was a stable, profitable-or-near-profitable business that could not grow fast enough to close the gap with better-capitalized competitors.

### Secondary Cause: The Three-Year Build Cycle Ceded First-Mover Advantage

Natero was founded in May 2012 but did not launch publicly until late 2015 — a roughly three-year build cycle. In a category that was forming rapidly during this period, that gap had consequences. Gainsight and Totango were both signing enterprise customers and building brand recognition while Natero was still in development. By the time Natero's ML-driven platform was ready for market, the category's early adopters had already made vendor selections, and switching costs in CSM software (which requires deep integration with a company's product usage data, CRM, and support systems) are non-trivial.

No public record explains what caused the extended build cycle. The most plausible inference is that building a production-grade ML pipeline capable of ingesting heterogeneous SaaS data at scale — without requiring IT or engineering involvement from customers — was genuinely hard, and the founders' infrastructure backgrounds led them to prioritize technical correctness over speed to market. The September 2015 Hacker News job posting for a Machine Learning Engineer, three months before launch, suggests the ML layer was still being staffed at that stage.<sup><a href="https://news.ycombinator.com/item?id=10155385">[35]</a></sup>

The attempted remedy was to differentiate sharply on ML sophistication at launch — positioning the three-year build as a technical moat rather than a delay. Soules's February 2016 launch statement explicitly attacked competitors as relying on "intuition and best-guesses."<sup><a href="https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html">[36]</a></sup> The positioning was credible but insufficient: enterprise buyers who had already deployed Gainsight were unlikely to switch based on ML claims alone, and new buyers evaluating the category for the first time faced a choice between a well-known, well-resourced vendor and a smaller, technically sophisticated alternative.

### Tertiary Cause: Feature Absorption Risk — The Standalone CSM Platform Trap

Soules's explanation for why the Freshworks acquisition was a natural fit reveals a structural vulnerability: "More and more people wanted to take data from Natero and take it to sales tools."<sup><a href="https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/">[37]</a></sup> This observation describes a classic feature absorption dynamic. Natero's most valuable output — churn risk scores and expansion signals — was most useful when embedded inside the CRM and sales tools that account executives and CSMs already lived in. As a standalone platform, Natero required users to context-switch; as a feature inside Freshworks, Salesforce, or HubSpot, the same data would be consumed where decisions were already being made.

This dynamic made Natero more valuable as an acquisition target than as an independent company. The Freshworks acquisition confirmed the pattern: the technology was rebranded as Freshsuccess and integrated into the Freshworks 360 suite, where it became a differentiating feature of a broader CRM platform rather than a standalone subscription product.<sup><a href="https://diginomica.com/refresh-2019-can-freshworks-change-cx-market-better-customer-success-metrics">[38]</a></sup>

The CustomerLink acquisition in February 2019 — bundling professional services with the software — may have been an attempt to address this dynamic by adding implementation depth that would increase switching costs and justify standalone deployment. But acquiring a consulting firm is an expensive and operationally complex way to solve a product positioning problem, and it appears to have accelerated the capital need that triggered the Freshworks conversation rather than resolving the underlying issue.<sup><a href="https://www.enterprisetimes.co.uk/2019/05/23/natero-acquisition-slots-into-freshworks/">[39]</a></sup>

### Structural Factor: The Strategic Customer-to-Acquirer Pipeline

The Freshworks acquisition was not a random outcome. Freshdesk (later Freshworks) selected Natero as its CSM platform in October 2016, giving Freshworks three years of direct product exposure before the acquisition conversation began.<sup><a href="https://finance.yahoo.com/news/freshdesk-leverages-natero-customer-success-140000022.html">[40]</a></sup> Freshworks CEO Girish Mathrubootham confirmed that the acquisition was triggered by Natero seeking additional capital, at which point Freshworks converted the funding conversation into an acquisition offer.<sup><a href="https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/">[41]</a></sup>

This sequence — strategic customer becomes strategic acquirer — is a recognizable pattern in enterprise software. A large customer that deeply integrates a vendor's product into its operations has both the information advantage (knowing the product's real capabilities and limitations) and the strategic motivation (eliminating a vendor dependency by owning the technology) to make an acquisition. For Natero, the Freshdesk relationship was simultaneously its most important customer win and the beginning of its exit path.

## Key Lessons

- **Revenue sustainability is not the same as competitive sustainability in winner-take-most categories.** Natero's ability to fund expansion through revenue after 2014 was operationally impressive, but it was strategically insufficient in a category where Gainsight's $100M+ raise bought distribution, brand, and ecosystem integrations that compounded over time. The lesson is not that Natero should have raised more money — it may not have been able to at the valuations required — but that choosing to compete on capital efficiency in a capital-intensive category is a bet on being acquired rather than on winning independently.

- **A three-year build cycle in a forming category is a first-mover tax, not a moat.** Natero founded in 2012 but launched in late 2015, ceding three years of customer acquisition and brand building to Gainsight and Totango during the period when enterprise buyers were making their initial CSM vendor selections. The technical sophistication that required the extended build was real, but switching costs in enterprise software meant that late entry required not just a better product but a dramatically better product — a bar Natero's ML differentiation did not clear for buyers already deployed on competing platforms.

- **Strategic customers are the most likely acquirers — and should be managed accordingly.** Freshdesk's October 2016 selection of Natero as its CSM platform was the most important event in Natero's commercial history, not because of the revenue it represented but because it gave Freshworks three years of deep product exposure. When Natero sought additional capital in early 2019, Freshworks was uniquely positioned to convert that conversation into an acquisition offer. For small enterprise software companies, the relationship between strategic customer and eventual acquirer is not coincidental — it is the most common exit path, and should be cultivated deliberately.

- **ML differentiation in enterprise software is a temporary moat, not a permanent one.** Natero's core competitive claim — that its machine learning approach was superior to the rule-based health scores used by Gainsight and Totango — was credible in 2016 but not durable. Larger competitors with more resources could acquire or build similar capabilities once the market validated their importance. Natero's ML advantage was a product-level differentiator in a market where the decisive competition was happening at the distribution and ecosystem level.

- **Returning to infrastructure roots after an application-layer exit is a signal worth examining.** Both Soules and Goodson departed Freshworks in 2023 to co-found Springtail, a scale-out replicated database startup — returning to the infrastructure domain they had worked in before Natero.<sup><a href="https://www.ycombinator.com/companies/natero">[42]</a></sup> Whether this reflects a deliberate strategic choice or a natural return to domain expertise, it raises a question about founder-market fit: the customer success application layer may have been a vehicle for their data infrastructure thesis rather than a terminal passion, and the acquisition may have been the natural conclusion of that journey rather than a constrained exit.

## Sources

1. [Y Combinator — Natero company profile](https://www.ycombinator.com/companies/natero)
2. [TechCrunch — Freshworks acquires customer success service Natero (May 21, 2019)](https://techcrunch.com/2019/05/21/freshworks-acquires-customer-success-service-natero/)
3. [Natero — Company page (archived)](https://www.natero.com/company/)
4. [IDG Connect — Natero: Machine learning for SaaS customer retention](https://www.idgconnect.com/article/3577558/natero-machine-learning-for-saas-customer-retention.html)
5. [Success.ai — Craig Soules profile](https://www.success.ai/profile/Craig-Soules-85498767857)
6. [ContactOut — Craig Soules career history](https://contactout.com/Craig-Soules-82593338)
7. [Crunchbase — Natero seed funding round](https://www.crunchbase.com/funding_round/natero-seed--5faf4767)
8. [Natero blog — Platform launch announcement (February 11, 2016)](https://blog.natero.com/natero-unveils-customer-success-platform)
9. [Yahoo Finance / Marketwired — Natero unveils industry's most advanced customer success platform](https://finance.yahoo.com/news/natero-unveils-industrys-most-advanced-140000936.html)
10. [Hacker News — Natero (YC S12) is hiring a Machine Learning Engineer (September 2015)](https://news.ycombinator.com/item?id=10155385)
11. [PressReleaseJet — Natero included in two recent Gartner CRM reports](https://pressreleasejet.com/news/natero-included-in-two-recent-gartner-crm-reports-for-its-customer-success-platform.html)
12. [Yahoo Finance — Freshdesk leverages Natero customer success platform (October 4, 2016)](https://finance.yahoo.com/news/freshdesk-leverages-natero-customer-success-140000022.html)
13. [Silicon Republic — Natero acquires CustomerLink (February 6, 2019)](https://www.siliconrepublic.com/business/natero-customerlink-customer-success)
14. [Enterprise Times — Natero acquisition slots into Freshworks (May 23, 2019)](https://www.enterprisetimes.co.uk/2019/05/23/natero-acquisition-slots-into-freshworks/)
15. [PR Newswire — Freshworks acquires Natero press release (May 21, 2019)](https://www.prnewswire.com/news-releases/freshworks-acquires-natero-a-leader-in-customer-success-cloud-software-300853853.html)
16. [Diginomica — Refresh 2019: Can Freshworks change the CX market with better customer success metrics (September 6, 2019)](https://diginomica.com/refresh-2019-can-freshworks-change-cx-market-better-customer-success-metrics)
17. [PitchBook — Natero company profile](https://pitchbook.com/profiles/company/62266-06)
18. [Dealroom — Natero company profile](https://app.dealroom.co/companies/natero)
19. [PitchBook — CustomerLink company profile](https://pitchbook.com/profiles/company/265272-22)
