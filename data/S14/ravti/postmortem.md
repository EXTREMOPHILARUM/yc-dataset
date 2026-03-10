# Research Report: Ravti

## Overview

Ravti was a commercial real estate software company founded by Alex Rangel and Chris Ginter, operating from approximately 2012 to 2020. The company built a platform to digitize, manage, and procure HVAC systems for commercial property owners — solving a problem that Rangel had witnessed firsthand as a sales engineer at Trane: most building managers had no reliable record of what HVAC equipment they owned, let alone a system to maintain or replace it efficiently. Ravti participated in Y Combinator's Summer 2014 batch and raised from a proptech-focused investor syndicate that included Homebrew, Brick & Mortar Ventures, and MetaProp.

Ravti built a genuinely useful product and demonstrated early traction, but it remained a narrow point solution in a market where distribution belonged to incumbent property management platforms. The company could not scale independently to the size required for a standalone enterprise software business.

In January 2021, Building Engines acquired Ravti for an undisclosed sum, immediately folding its technology into a new HVAC module inside Building Engines' Prism platform. Ten months later, JLL (Jones Lang LaSalle) acquired Building Engines for approximately $300 million — meaning Ravti's technology ultimately landed inside one of the world's largest commercial real estate services firms. The value accrued to the platform aggregator, not the point solution.

<report-gallery>
<media-image src="https://www.buildingengines.com/wp-content/uploads/2021/03/ravti-mockup-new-480x296.png" alt="Ravti HVAC management platform UI mockup as shown on Building Engines' website post-acquisition" caption="Ravti's HVAC management interface as showcased by Building Engines after the January 2021 acquisition — the product that had operated as a standalone platform for six years was rebranded as a module inside Prism within months of the deal closing."></media-image>
</report-gallery>

## Founding Story

Alex Rangel came to the HVAC software problem the hard way: by living inside it. Working as a sales engineer for Trane in Florida, Rangel encountered the same dysfunction repeatedly across commercial properties — building managers who could not identify which HVAC units they owned, had no maintenance history for their equipment, and were paying retail prices for replacements because they lacked the purchasing leverage that came with organized inventory data.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[1]</a></sup>

The insight was not abstract. Rangel had watched property owners overpay for equipment and services because the information asymmetry between vendors and buyers was structural — vendors knew exactly what units were installed and what they cost; building managers often did not. Digitizing that inventory was the first step toward closing the gap.

Rangel co-founded Ravti with Chris Ginter, a high-school friend.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[2]</a></sup> The founding team's complementary skills are not well-documented in public sources — Ginter's specific role (technical, operational, or commercial) has not been reported. What is documented is that the company was reportedly conceived as early as 2012, though Ravti's formal YC participation in 2014 is the more commonly cited founding date.<sup><a href="https://tracxn.com/d/companies/ravti/__QLlAlKO0X1w-hrWMEvZFIDB0qmuE30c16Bg_NRkCdM4">[3]</a></sup> The two-year gap likely reflects a period when Rangel was developing the concept and early product while still in Florida before relocating to pursue institutional backing.

Ravti joined Y Combinator's Summer 2014 batch and presented at Demo Day on August 19, 2014.<sup><a href="https://techcrunch.com/2014/08/19/yc-demo-day-session-2-helion-bitaccess-ubiome-fixed-and-more/">[4]</a></sup> Rangel entered the program with some skepticism — YC's S14 cohort skewed heavily toward consumer applications, and enterprise sales into commercial real estate operates on a fundamentally different rhythm than consumer growth. But Rangel credited the experience with improving Ravti's software UX: "A lot of the problem with enterprise software is that it doesn't have the users in mind. When we can make using this software easier, everyone wins."<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[5]</a></sup> Exposure to consumer-facing founders pushed the team to think about the end user — the building technician scanning a rooftop unit — not just the property manager signing the contract.

The initial vision was a two-sided marketplace: digitize the inventory on one side, aggregate vendor pricing on the other, and extract value from the spread. The KAYAK analogy Rangel used at Demo Day was deliberate — not just a pitch shorthand, but a description of the intended business architecture.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[6]</a></sup> That architecture would evolve significantly over the following six years.

## Timeline

- **2012** — Ravti reportedly founded per Tracxn; likely reflects when Rangel began developing the concept while at Trane in Florida. True incorporation date uncertain.<sup>[[3]](https://tracxn.com/d/companies/ravti/__QLlAlKO0X1w-hrWMEvZFIDB0qmuE30c16Bg_NRkCdM4)</sup>

- **August 19, 2014** — Ravti presents at YC S14 Demo Day. At this point the company has already tagged 30 million square feet of commercial real estate and secured agreements with a national portfolio manager. First institutional funding (YC seed) received.<sup>[[4]](https://techcrunch.com/2014/08/19/yc-demo-day-session-2-helion-bitaccess-ubiome-fixed-and-more/)</sup> TechCrunch covers the KAYAK-for-HVAC positioning and 18–40% savings claim.<sup>[[1]](https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/)</sup>

- **2014–2015** — Homebrew invests in Ravti (inferred from Homebrew's January 2021 blog post noting the investment was "more than six years" prior).<sup>[[7]](https://homebrew.co/blog/2021/01/20/ravti-acquired-by-building-engines)</sup> Brick & Mortar Ventures and Palm Drive Capital also invest across this period.<sup>[[8]](https://www.crunchbase.com/organization/ravti)</sup>

- **2015** — Deepak Jhalani joins as CTO after finding Ravti on YC's Work at a Startup platform. He brings experience managing engineering teams of 40+. Company begins building IoT hardware capability alongside core software.<sup>[[9]](https://www.ycombinator.com/blog/hired-on-work-at-a-startup-deepak-jhalani-cto-at-ravti-yc-s14/)</sup>

- **January 26, 2017** — Ravti closes its last disclosed funding round — a Seed round with MetaProp NYC as a new investor. This is the final known external capital event before the 2021 acquisition.<sup>[[10]](https://tracxn.com/d/companies/ravti/__QLlAlKO0X1w-hrWMEvZFIDB0qmuE30c16Bg_NRkCdM4/funding-and-investors)</sup>

- **2017–2020** — Ravti operates without disclosed additional funding. Product expands to include IoT real-time monitoring, tenant compliance tracking for triple-net leases, and ASHRAE-based capital expenditure scoring. Team reaches approximately 17 employees.<sup>[[11]](https://www.ycombinator.com/companies/ravti)</sup>

- **2020** — Ravti is acquired by Building Engines (transaction later announced publicly in January 2021).<sup>[[11]](https://www.ycombinator.com/companies/ravti)</sup>

- **January 11, 2021** — Building Engines publicly announces acquisition of Ravti. Ravti's software designated as foundation of new HVAC module in Building Engines' Prism platform. Acquisition price undisclosed.<sup>[[12]](https://www.businesswire.com/news/home/20210111005224/en/Building-Engines-Acquires-Ravti)</sup>

- **January 20, 2021** — Homebrew publishes blog post celebrating the acquisition, praising the team's "relentless" vision.<sup>[[7]](https://homebrew.co/blog/2021/01/20/ravti-acquired-by-building-engines)</sup>

- **November 30, 2021** — JLL (Jones Lang LaSalle) closes acquisition of Building Engines for approximately $300 million, making Ravti's technology part of one of the world's largest commercial real estate services firms.<sup>[[13]](https://www.jll.com/en-us/newsroom/jll-closes-acquisition-of-building-engines)</sup>

## What They Built

Ravti's core product solved a problem that sounds almost embarrassingly basic: most commercial building managers did not know what HVAC equipment they owned.

**Version 1: Digital Inventory**

The initial product was a field-first digitization tool. Technicians would physically visit each rooftop unit, photograph it, and attach a unique digital barcode. That data uploaded to a cloud database, creating — often for the first time — a complete, searchable inventory of every HVAC unit in a property portfolio.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[14]</a></sup>

The practical value was immediate. When a unit failed, a building manager could pull up the exact unit record — model, age, service history, vendor — rather than calling a technician to identify the equipment before any repair work could begin. Vendors could be dispatched directly through the platform without the manager needing to remember complicated unit codes.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[15]</a></sup>

**The Marketplace Layer**

The more ambitious layer was procurement. Rangel's KAYAK analogy described a comparison engine: because Ravti had aggregated inventory data across a large portfolio, it could present multiple vendor quotes for any repair or replacement job, enabling bulk purchasing that bypassed the marked-up retail pricing that individual building managers typically paid. Ravti claimed savings of 18% to 40% on HVAC replacement through this mechanism.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[16]</a></sup>

The business model was SaaS priced per square foot — a sensible alignment with the scale of the customer's portfolio.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[17]</a></sup> At launch, Ravti also held LEED certification from the U.S. Green Building Council, providing a sustainability credential that likely served as a differentiator with ESG-conscious property managers.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[18]</a></sup>

**Product Expansion: IoT and Compliance**

Over the following years, Ravti added two significant product layers. The first was IoT hardware: physical sensors attached to HVAC units that captured real-time equipment health data, enabling energy efficiency monitoring and predictive maintenance without requiring a technician visit.<sup><a href="https://www.ycombinator.com/blog/hired-on-work-at-a-startup-deepak-jhalani-cto-at-ravti-yc-s14/">[9]</a></sup> CTO Deepak Jhalani acknowledged the complexity this introduced: "Building a hardware and software product is really challenging."<sup><a href="https://www.ycombinator.com/blog/hired-on-work-at-a-startup-deepak-jhalani-cto-at-ravti-yc-s14/">[19]</a></sup>

The second expansion was tenant compliance tracking — software that automatically monitored whether tenants in triple-net leases were fulfilling their contractual obligation to maintain HVAC units. This was a targeted feature for retail and industrial landlords, where tenants bear maintenance responsibility but enforcement is manual and inconsistent.<sup><a href="https://ravti.zendesk.com/hc/en-us/articles/1260806052349-Ravti-How-To">[20]</a></sup>

A final layer added ASHRAE-based scoring for equipment life expectancy, giving property managers a data-driven framework for capital expenditure planning — when to repair versus replace, and how to budget for equipment turnover across a portfolio.<sup><a href="https://www.businesswire.com/news/home/20210111005224/en/Building-Engines-Acquires-Ravti">[21]</a></sup>

By the time of acquisition, Ravti had evolved from a barcode-and-photo inventory tool into a multi-layer platform spanning inventory management, procurement, IoT monitoring, lease compliance, and CapEx planning. The breadth was real — but so was the execution complexity.

## Market Position

### Target Customers

Ravti's primary customers were commercial property managers and owners responsible for large portfolios — specifically those managing retail, industrial, and commercial office space where HVAC costs are material. The tenant compliance product was explicitly targeted at triple-net lease operators, where landlords need visibility into tenant maintenance behavior without direct control over it. The per-square-foot pricing model favored large portfolio holders over single-building owners, suggesting Ravti was selling to institutional property managers rather than small landlords.

### Market Size

At Demo Day in August 2014, Ravti framed the addressable market as $1 billion, representing approximately 32% of commercial real estate operating spend.<sup><a href="https://techcrunch.com/2014/08/19/yc-demo-day-session-2-helion-bitaccess-ubiome-fixed-and-more/">[22]</a></sup> The breakdown by property type is instructive: HVAC accounts for roughly 30% of operating budgets in retail and industrial properties, versus 15–20% in commercial office.<sup><a href="https://therealreporter.com/briefs/building_engines_announces_the_acquisition_of_ravti">[23]</a></sup> This concentration in retail and industrial — property types with high HVAC intensity and triple-net lease structures — explains why Ravti's tenant compliance feature was a logical extension rather than a distraction.

The $1 billion figure was likely a conservative framing of the procurement opportunity rather than the total software market. The SaaS market for commercial real estate operations software was smaller but growing rapidly through the 2014–2020 period, driven by institutional investors demanding better data from their property managers.

### Competition

Ravti's competitive position is best understood along two axes: **product depth** (how comprehensive the HVAC-specific functionality was) and **distribution reach** (how many property managers the platform could access through existing relationships).

On product depth, Ravti had a genuine advantage. No incumbent property management platform had built HVAC-specific features with the granularity Ravti offered — barcode-level equipment tracking, ASHRAE scoring, vendor comparison, and IoT integration in a single workflow. The domain expertise Rangel brought from Trane was real and difficult to replicate quickly.

On distribution reach, Ravti was structurally disadvantaged. The major property management platforms — Yardi, MRI Software, Building Engines, and later AppFolio — already had established relationships with the institutional property managers Ravti needed to reach. These platforms were not HVAC specialists, but they were the systems of record for building operations. Any property manager evaluating a new tool had to weigh the friction of adding a standalone HVAC platform against the convenience of waiting for their existing platform to add the feature natively.

This is the structural dynamic that ultimately defined Ravti's ceiling. The company was not competing against a better HVAC product — it was competing against the gravitational pull of integrated platforms. Yardi and MRI had distribution advantages that no amount of product depth could fully offset. When Building Engines decided to build an HVAC module, the fastest path was acquisition rather than development — which is precisely what happened.

The competitive landscape also shifted during Ravti's operating years. The proptech sector attracted significant capital between 2015 and 2020, and incumbent platforms accelerated their feature roadmaps. The window for a standalone HVAC point solution to establish itself before being absorbed or replicated narrowed over time.

## Business Model

Ravti charged property owners by the square footage of the buildings under management — a per-square-foot SaaS model that aligned revenue with portfolio scale.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[17]</a></sup> The intended architecture included a marketplace layer where Ravti would facilitate bulk procurement and potentially earn a take rate on transactions, though whether this was ever operationalized at scale is not documented in public sources.

**Revenue data is not publicly available.** Ravti never disclosed ARR, customer count, or revenue at any point in its operating life. The absence of revenue disclosure is itself a signal — companies that achieve meaningful scale in enterprise SaaS typically use revenue milestones as fundraising and press anchors.

What can be inferred directionally: with approximately 17 employees<sup><a href="https://www.ycombinator.com/companies/ravti">[11]</a></sup> and a last funding round in January 2017, Ravti's annual burn rate was likely in the $1.5–2.5 million range (assuming fully-loaded costs of $90–150K per employee, consistent with a Tampa-based team with some New York presence). If the company operated for roughly three years post-2017 funding without raising additional capital, it either achieved near-breakeven on its SaaS revenue or drew down reserves from the 2017 seed round. This is an inference, not a documented fact.

PitchBook lists total disclosed funding as $120,000 — almost certainly reflecting only the YC standard seed tranche.<sup><a href="https://pitchbook.com/profiles/company/66151-45">[24]</a></sup> Crunchbase lists four funding rounds with investors including Y Combinator, Homebrew, Brick & Mortar Ventures, Palm Drive Capital, and MetaProp.<sup><a href="https://www.crunchbase.com/organization/ravti">[8]</a></sup> Total capital raised across all rounds is undisclosed, making it impossible to assess investor returns from the acquisition.

## Traction

At YC Demo Day in August 2014 — before the company had completed its first year of institutional backing — Ravti had already tagged HVAC equipment across 30 million square feet of commercial real estate and secured agreements with a national portfolio manager.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[25]</a></sup> For a pre-Series A enterprise software company, this was unusually strong early validation.

The 30 million square feet figure is also the most significant data anomaly in Ravti's public record. The same number appears in Building Engines' acquisition announcement in January 2021 — "Ravti digitized HVAC inventory across more than 30 million square feet of retail, industrial, and commercial office spaces."<sup><a href="https://www.buildingengines.com/blog/ravti-joins-the-building-engines-family/">[26]</a></sup> Whether this reflects genuine stagnation in portfolio coverage, a reporting artifact (the metric was simply not updated in press materials), or a definitional shift in how square footage was counted is unresolved. But the absence of a larger number — after six years of operation and multiple funding rounds — is notable. A company that had grown from 30 million to 300 million square feet would almost certainly have publicized that figure.

The team reached approximately 17 employees at some point during its operating life,<sup><a href="https://www.ycombinator.com/companies/ravti">[11]</a></sup> suggesting the company remained small and likely capital-efficient but never achieved the headcount growth associated with hypergrowth enterprise software companies. No ARR, churn, or net dollar retention figures are available in public sources.

## Post-Mortem

Ravti operated for approximately six to eight years, raised from credible investors, built a product with genuine utility, and exited via acquisition rather than shutdown. By startup standards, this is not a failure — it is a modest outcome. But the gap between the company's early traction and its eventual exit as a feature inside a larger platform warrants examination.

### The Core Problem: Point Solution in a Platform Market

The most important structural explanation for Ravti's ceiling is not a company-specific misstep — it is the nature of the market it was selling into.

Commercial property management is a workflow-dense environment. Building managers use systems of record — Yardi, MRI Software, Building Engines — that touch every aspect of operations: leases, work orders, tenant communications, financial reporting. Adding a standalone HVAC tool requires a building manager to maintain a separate login, a separate data silo, and a separate vendor relationship. The switching cost is not the software itself; it is the workflow disruption.

Ravti's product was most powerful when HVAC data was connected to the broader building operations workflow — when a failing unit triggered a work order, which triggered a vendor dispatch, which updated the lease compliance record, which fed the CapEx model. But that integration required either deep API partnerships with incumbent platforms (which incumbents had little incentive to enable for a potential competitor) or convincing customers to replace their existing system of record entirely (which was not Ravti's pitch).

Building Engines' decision to acquire Ravti rather than build the feature internally confirms that Ravti had built something technically non-trivial. But it also confirms the distribution dynamic: the acquirer had the customer relationships; Ravti had the product depth. The value of the combination accrued to the party with distribution.

### The Stagnant Traction Metric

The 30 million square feet figure appearing unchanged between August 2014 and January 2021 is the most concrete signal of a growth problem.<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[25]</a></sup><sup><a href="https://www.buildingengines.com/blog/ravti-joins-the-building-engines-family/">[26]</a></sup> Enterprise software companies that are growing replace their headline metrics with larger ones. The persistence of the same number across six years of press coverage suggests one of two things: the company stopped growing its portfolio coverage after the initial national portfolio manager agreement, or the metric was simply never updated in external communications. Either interpretation is consistent with a company that achieved early product-market fit at the unit level but could not replicate its initial wins at scale.

The attempted remedy — product expansion into IoT hardware, tenant compliance, and CapEx scoring — added genuine value but also added execution complexity. CTO Deepak Jhalani's acknowledgment that "building a hardware and software product is really challenging"<sup><a href="https://www.ycombinator.com/blog/hired-on-work-at-a-startup-deepak-jhalani-cto-at-ravti-yc-s14/">[19]</a></sup> suggests the IoT layer consumed significant engineering resources. Whether it drove proportional revenue growth is unknown, but the absence of any public milestone around the IoT product suggests it did not become a breakout feature.

### The Series A Gap

Ravti's last disclosed funding round closed in January 2017.<sup><a href="https://tracxn.com/d/companies/ravti/__QLlAlKO0X1w-hrWMEvZFIDB0qmuE30c16Bg_NRkCdM4/funding-and-investors">[10]</a></sup> The company operated for approximately four more years before the acquisition without raising additional disclosed capital. This four-year gap is the clearest financial signal in the public record.

Series A investors in enterprise SaaS typically require evidence of repeatable sales motion: consistent new logo acquisition, low churn, and a clear path to $5–10 million ARR. Enterprise sales into commercial real estate is structurally slow — procurement cycles are long, portfolio-level deals require executive sign-off, and implementation requires field work (the physical tagging of equipment). Ravti's early traction with a national portfolio manager was impressive, but replicating that deal across dozens of similar accounts at a pace that satisfied Series A growth benchmarks appears to have been the challenge.

Whether Ravti attempted to raise a Series A and could not, or chose not to raise and operated on reserves, is not documented. The outcome — a seed-stage exit after six years — is consistent with either path.

### UX Improvement as Insufficient Moat

Rangel's insight from YC — that enterprise software "doesn't have the users in mind" and that improving UX benefits everyone<sup><a href="https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/">[5]</a></sup> — was correct as a product philosophy but insufficient as a competitive moat. Better UX is replicable. Domain expertise in HVAC equipment taxonomy, vendor relationships, and ASHRAE scoring is harder to replicate — but it is also acquirable, which is exactly what Building Engines did.

The UX advantage Ravti built was real enough to attract acquisition interest but not durable enough to prevent incumbents from eventually building or buying comparable functionality. In a market where distribution is the primary competitive variable, product quality determines acquisition price, not independence.

### COVID-19 as Possible Accelerant

The acquisition closed in 2020 — the year commercial real estate was most severely disrupted by the COVID-19 pandemic. Office occupancy collapsed, retail tenants stopped paying rent, and property managers faced unprecedented pressure on operating budgets. Whether this accelerated Ravti's decision to sell — by compressing near-term revenue expectations or creating urgency around finding a larger distribution partner — is not documented but is plausible context. A standalone HVAC software company dependent on commercial real estate activity would have faced a difficult 2020 regardless of its underlying product quality.

## Key Lessons

- **Early traction in enterprise software does not validate a standalone distribution model.** Ravti tagged 30 million square feet and secured a national portfolio manager agreement before Demo Day in August 2014 — genuinely impressive early validation. But that initial deal was likely won through Rangel's personal network and domain credibility from Trane, not through a repeatable sales motion. The same 30 million square feet figure appearing in the 2021 acquisition announcement suggests the company never developed the systematic outbound sales engine needed to replicate that early win at scale. Domain expertise opens the first door; distribution infrastructure determines how many doors follow.

- **Hardware expansion in a software business multiplies execution risk without proportional revenue upside.** Ravti's decision to add IoT sensors to its core software platform was a logical product extension — real-time equipment health data is more valuable than periodic manual inventory. But Jhalani's explicit acknowledgment that "building a hardware and software product is really challenging" signals that the IoT layer consumed engineering resources disproportionate to its commercial contribution. No public milestone around the IoT product exists, suggesting it did not become a revenue driver. For a small team operating without disclosed funding after January 2017, this complexity may have crowded out focus on the core SaaS growth problem.

- **In workflow-dense enterprise markets, the system of record wins the distribution war.** Ravti competed in a market where Yardi, MRI Software, and Building Engines already held the primary vendor relationships with institutional property managers. Adding a standalone HVAC tool required customers to maintain a separate workflow outside their system of record — a friction cost that compounded over time. The acquisition outcome confirmed this dynamic: Building Engines paid for Ravti's product depth precisely because it already had the distribution that Ravti lacked. Startups entering markets with entrenched systems of record need either a platform partnership strategy or a wedge that forces workflow migration — Ravti had neither at sufficient scale.

- **A four-year gap between last funding and acquisition is a signal, not a coincidence.** Ravti's last disclosed funding round closed in January 2017; the acquisition occurred in 2020. The absence of a Series A in a period when proptech funding was abundant suggests the company could not demonstrate the growth metrics institutional investors required — likely because commercial real estate sales cycles are long and portfolio-level deals are difficult to replicate systematically. Companies that achieve Series A growth in enterprise SaaS typically do so within 18–24 months of their seed round. Ravti's six-year seed-to-exit timeline reflects a business that found product-market fit at the unit level but not at the growth rate required for independent scale.

- **The double acquisition chain (Ravti → Building Engines → JLL) validates the thesis but not the vehicle.** JLL's $300 million acquisition of Building Engines in November 2021 — just ten months after Building Engines acquired Ravti — confirms that HVAC data management is genuinely valuable to large commercial real estate operators.<sup><a href="https://www.jll.com/en-us/newsroom/jll-closes-acquisition-of-building-engines">[13]</a></sup> The value Rangel identified in 2012 was real. But the value accrued to the platform aggregator (Building Engines) and ultimately to the global services firm (JLL), not to the point solution that first digitized the problem. Being right about the market is necessary but not sufficient — the question is whether the company is positioned to capture the value it creates, or whether it is building infrastructure that a better-distributed acquirer will monetize.

## Sources

1. [TechCrunch — YC-backed Ravti wants to digitize the HVAC industry (August 19, 2014)](https://techcrunch.com/2014/08/19/yc-backed-ravti-wants-to-digitize-the-hvac-industry/)
2. [TechCrunch — YC Demo Day Session 2: Helion, Bitaccess, uBiome, Fixed and more (August 19, 2014)](https://techcrunch.com/2014/08/19/yc-demo-day-session-2-helion-bitaccess-ubiome-fixed-and-more/)
3. [Tracxn — Ravti company profile](https://tracxn.com/d/companies/ravti/__QLlAlKO0X1w-hrWMEvZFIDB0qmuE30c16Bg_NRkCdM4)
4. [Tracxn — Ravti funding and investors](https://tracxn.com/d/companies/ravti/__QLlAlKO0X1w-hrWMEvZFIDB0qmuE30c16Bg_NRkCdM4/funding-and-investors)
5. [YC — Hired on Work at a Startup: Deepak Jhalani, CTO at Ravti (YC S14)](https://www.ycombinator.com/blog/hired-on-work-at-a-startup-deepak-jhalani-cto-at-ravti-yc-s14/)
6. [YC — Ravti company profile](https://www.ycombinator.com/companies/ravti)
7. [Homebrew — Ravti acquired by Building Engines (January 20, 2021)](https://homebrew.co/blog/2021/01/20/ravti-acquired-by-building-engines)
8. [Crunchbase — Ravti organization profile](https://www.crunchbase.com/organization/ravti)
9. [BusinessWire — Building Engines Acquires Ravti (January 11, 2021)](https://www.businesswire.com/news/home/20210111005224/en/Building-Engines-Acquires-Ravti)
10. [Building Engines — Ravti joins the Building Engines family](https://www.buildingengines.com/blog/ravti-joins-the-building-engines-family/)
11. [The Real Reporter — Building Engines announces acquisition of Ravti](https://therealreporter.com/briefs/building_engines_announces_the_acquisition_of_ravti)
12. [JLL — JLL closes acquisition of Building Engines (November 30, 2021)](https://www.jll.com/en-us/newsroom/jll-closes-acquisition-of-building-engines)
13. [PitchBook — Ravti company profile](https://pitchbook.com/profiles/company/66151-45)
14. [Mergr — Building Engines acquires Ravti](https://mergr.com/building-engines-acquires-ravti)
15. [Ravti — How To (Zendesk support documentation)](https://ravti.zendesk.com/hc/en-us/articles/1260806052349-Ravti-How-To)
