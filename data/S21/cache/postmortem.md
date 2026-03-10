# Research Report: Cache

## Overview

Cache was a Y Combinator Summer 2021 company that attempted to bring convenience store delivery to suburban markets through a network of miniaturized, automated dark stores — proprietary vending-style units called Cache Units — listed as storefronts on DoorDash, UberEats, and Instacart.Founded by two DoorDash alumni, the company's core thesis was that existing rapid-delivery competitors like GoPuff and DashMart were structurally locked out of suburban markets by their high facility and labor costs, and that a hardware-first, unstaffed approach could unlock those markets at a fraction of the cost.

Cache raised only the standard $125,000 YC pre-seed and never closed a follow-on round.With a two-person team, hardware-dependent infrastructure, and a seed round that never materialized, the company quietly wound down — a casualty of both its own capital constraints and the broader collapse of the instant-delivery investment wave in 2022.

## Founding Story

Cache was founded in August 2021 by Christopher Wu and Jimmy Young, two former DoorDash employees who met through their overlapping work in the delivery economy. Their shared employer gave them an unusually direct view into the structural economics of dark stores and delivery platforms — knowledge that became the foundation of Cache's thesis.

Wu had led business development for Ghost Kitchens at DoorDash, a role that put him at the intersection of real estate, operations, and platform economics for delivery-only restaurant concepts. Before DoorDash, he managed a ride type at Lyft and worked in operations and compliance at Funding Circle. Young's background was on the product side: he had served as product lead for DashPass and Affordability at DoorDash, giving him direct exposure to subscription delivery economics and consumer price sensitivity. Before DoorDash, he had held product roles at Lyft, Twitch, and Freelancer.com, and studied computer science and chemical engineering at the University of Sydney. <sup><a href="https://www.ycombinator.com/companies/cache">[1]</a></sup>

The insight that drove Cache was straightforward: the dark store model pioneered by GoPuff and DashMart worked in dense urban cores but broke down economically in suburban markets. Facilities cost over $1 million to build out, and labor ran $50,000 or more per month — costs that required order density that suburbs couldn't provide. <sup><a href="https://yetanotherstartup.com/p/cache">[2]</a></sup> Wu and Young believed that a radically smaller, fully automated unit — one that could be installed in an hour and required no staff — could serve those markets profitably.

In August 2021, Young announced the company publicly: "Proud to announce Christopher Wu & I have officially founded Cache (grabcache.com) and are backed by Y Combinator!" <sup><a href="https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1">[3]</a></sup> The announcement also contained an early signal of the difficulty ahead: "Starting a company is the hardest thing we've ever done. Huge respect to all founders." <sup><a href="https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1">[3]</a></sup>

Cache was accepted into YC's Summer 2021 batch, providing initial validation and $125,000 in pre-seed capital. <sup><a href="https://www.crunchbase.com/organization/cache-0d59">[4]</a></sup> The company was headquartered in San Francisco and, as far as public records indicate, never grew beyond its two founders. <sup><a href="https://www.ycombinator.com/companies/cache">[1]</a></sup>

No public information is available on whether the founders had prior hardware or manufacturing experience relevant to building the Cache Units, or how they divided technical versus business responsibilities.

---

## Timeline

- **August 2021** — Cache founded by Christopher Wu and Jimmy Young; YC S21 backing confirmed. <sup>[[3]](https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1)</sup>

- **August 4, 2021** — Jimmy Young posts LinkedIn announcement of Cache's founding and YC backing, stating the team is "raising our first round very soon." <sup>[[3]](https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1)</sup>

<media-tweet url="https://twitter.com/ycombinator/status/1423054705069109256" author="@ycombinator" date="2021-08-04" text="Welcome to YC S21, Cache! Cache is building online convenience stores on DoorDash & Uber Eats fulfilled by tiny, automated dark stores."></media-tweet>

- **August 30–31, 2021** — YC S21 Demo Day. Cache receives $125,000 pre-seed from Y Combinator. TechCrunch covers Cache as part of the S21 cohort. <sup>[[4]](https://www.crunchbase.com/organization/cache-0d59)</sup> <sup>[[5]](https://techcrunch.com/2021/09/02/tracking-startup-focus-in-the-latest-y-combinator-cohort/)</sup>

- **September 2, 2021** — TechCrunch publishes broader YC S21 Demo Day analysis, placing Cache in the context of the dark store and instant-delivery trend. <sup>[[5]](https://techcrunch.com/2021/09/02/tracking-startup-focus-in-the-latest-y-combinator-cohort/)</sup>

- **April 28, 2022** — Science of the Time publishes a profile of Cache, describing Cache Units as "glassless vending machines" and noting the founders' DoorDash backgrounds. <sup>[[6]](https://scienceofthetime.com/2022/04/28/after-stores-go-dark-they-cache-goods/)</sup>

- **May 9, 2022** — Yet Another Startup publishes the most detailed third-party writeup of Cache, confirming only two live Cache Units — one in Sausalito (medicine and snacks) and one in South San Francisco (ice cream) — and articulating the competitive thesis against GoPuff and DashMart. <sup>[[7]](https://yetanotherstartup.com/p/cache)</sup>

- **2022 (date unknown)** — Cache quietly winds down. No formal shutdown announcement is made. The grabcache.com website remains live. <sup>[[8]](https://www.grabcache.com/)</sup>

- **October 14, 2024** — Moxxie Ventures announces Christopher Wu as a new team member, describing him as "a former YC founder" — the clearest public confirmation that Cache is no longer operating. <sup>[[9]](https://moxxie.substack.com/p/moxxies-got-more-moxxie)</sup>

---

## What They Built

Cache's product was a two-layer system: physical hardware deployed in the real world, and digital storefronts listed on existing delivery platforms.

**The Cache Unit**

The core hardware was a proprietary automated storage unit the company called a Cache Unit. In press coverage, it was described as resembling a "glassless vending machine" — a compact, enclosed unit that held inventory and dispensed items to delivery drivers without any human staff present. <sup><a href="https://scienceofthetime.com/2022/04/28/after-stores-go-dark-they-cache-goods/">[6]</a></sup> The units were designed to be installed in approximately one hour and to operate 24 hours a day, seven days a week, with no on-site employees required. <sup><a href="https://www.grabcache.com/">[8]</a></sup>

Access was restricted to delivery platform partners — DoorDash drivers, UberEats couriers, and similar — rather than walk-in consumers. This made Cache Units functionally invisible to the public: they were infrastructure for the delivery economy, not retail storefronts in the traditional sense.

**The Digital Storefront Layer**

On top of the physical units, Cache created digital storefronts on DoorDash, UberEats, Postmates, and Instacart. <sup><a href="https://alexandre.substack.com/p/-y-combinator-summer-batch-2021">[10]</a></sup> A consumer browsing DoorDash in a Cache-served area would see what appeared to be a convenience store. They would place an order through the platform's standard interface. A nearby delivery driver would receive the order, travel to the Cache Unit, retrieve the items, and complete the delivery. From the consumer's perspective, the experience was identical to ordering from any other store on the platform.

**Product Catalog**

Cache targeted high-urgency, high-margin convenience categories: over-the-counter medicine, personal care items (including plan B, condoms, and tampons), snacks, and ice cream. <sup><a href="https://www.grabcache.com/">[8]</a></sup> These categories share a common characteristic — they are purchased impulsively or in moments of need, making speed of delivery a primary value driver rather than price comparison.

**Competitive Differentiation**

The key differentiator was cost structure. Cache's website claimed its units were "100x cheaper and have a 100x lower operating expense" compared to traditional stores. <sup><a href="https://www.grabcache.com/">[8]</a></sup> This claim was never independently verified, but the underlying logic was coherent: eliminating real estate, build-out costs, and labor from the dark store model would dramatically reduce the minimum viable order density required to reach profitability in any given location.

**Deployment at Shutdown**

As of May 2022 — the most recent detailed coverage of Cache — the company had two live Cache Units: one in Sausalito, California, stocked with OTC medicine and snacks, and one in South San Francisco, California, stocked with ice cream. <sup><a href="https://xunbaodui.com/products/urkc75hl">[11]</a></sup> No public record indicates Cache ever expanded beyond these two pilot locations.

The critical operational question — how Cache managed inventory replenishment for unstaffed units operating 24/7 — was never addressed in public coverage. This is a meaningful gap: a vending machine that runs out of stock generates no revenue, and restocking without staff requires either a separate logistics operation or a very high restocking frequency by the founders themselves.

---

## Market Position

### Target Customers

Cache operated a two-sided model with distinct customer types on each side.

On the consumer side, Cache targeted suburban residents who wanted fast delivery of convenience goods — medicine, personal care items, snacks — but lived outside the service areas of urban-focused rapid-delivery competitors. The implicit consumer profile was someone who needed an item urgently (a sick child at midnight, a forgotten personal care product) and was willing to pay delivery platform fees for speed.

On the supply side, Cache's actual direct customers were the locations that would host Cache Units — property owners, parking lots, or commercial spaces in suburban areas willing to allocate a small footprint to the hardware. This B2B placement relationship was a critical dependency that received almost no public discussion.

Cache also depended on delivery platforms — DoorDash, UberEats, Postmates, Instacart — as distribution channels. <sup><a href="https://alexandre.substack.com/p/-y-combinator-summer-batch-2021">[10]</a></sup> The commercial terms of those relationships (commission rates, algorithmic placement, exclusivity) were never disclosed and represent a significant unknown in the business model.

### Market Size

Cache launched at the peak of the instant-delivery investment wave. In 2021, GoPuff raised $1 billion at a $15 billion valuation. Gorillas, Getir, and Jokr collectively raised hundreds of millions of dollars targeting 10–15 minute delivery in dense urban markets. DashMart, DoorDash's own dark store product, was expanding aggressively. <sup><a href="https://techcrunch.com/2021/09/02/tracking-startup-focus-in-the-latest-y-combinator-cohort/">[5]</a></sup>

Cache's suburban positioning was a deliberate counter-thesis to this urban concentration. The U.S. suburban convenience market is large in aggregate — the convenience store industry generates over $700 billion in annual sales — but Cache's addressable market was specifically the subset of suburban consumers willing to order convenience goods through delivery platforms, a segment with no reliable public sizing data at the time.

The suburban bet carried an inherent tension: lower population density means fewer orders per Cache Unit, which means each unit needs either higher average order values or lower operating costs to reach the same economics as an urban dark store. Cache's "100x cheaper" claim was the answer to this tension, but it was never validated with disclosed unit economics.

### Competition

Cache's primary named competitors were GoPuff and DashMart. <sup><a href="https://yetanotherstartup.com/p/cache">[7]</a></sup>

**GoPuff** operated a network of micro-fulfillment centers in urban and near-suburban markets, stocked with thousands of SKUs. Its model required significant upfront capital — the $1M+ facility costs Cache cited — and ongoing labor. GoPuff's scale gave it purchasing power and brand recognition, but its economics were under sustained scrutiny even at the height of its funding.

**DashMart** was DoorDash's own dark store product, giving it a structural advantage in platform placement that Cache could not replicate. A Cache storefront on DoorDash was competing for algorithmic visibility against DoorDash's own first-party convenience offering — a dynamic the founders' DoorDash backgrounds would have made them acutely aware of.

**Rapid-delivery startups** (Gorillas, Getir, Jokr, Fridge No More) were urban-focused and largely irrelevant to Cache's suburban thesis, but they consumed enormous amounts of investor attention and capital in 2021, potentially crowding out interest in smaller, less-proven models.

The competitive landscape shifted dramatically in 2022. Rising interest rates and post-pandemic normalization of consumer behavior caused rapid-delivery unit economics to deteriorate publicly. Gorillas was acquired by Getir. Jokr exited the U.S. market. Fridge No More shut down. GoPuff conducted multiple rounds of layoffs. The investor appetite that had funded the entire category evaporated — and Cache, still at two units and seeking its first external seed round, had no buffer against that shift.

---

## Business Model

Cache's revenue model was not publicly disclosed in detail, but the structure can be inferred from the product design.

Cache created digital storefronts on DoorDash, UberEats, Postmates, and Instacart. <sup><a href="https://alexandre.substack.com/p/-y-combinator-summer-batch-2021">[10]</a></sup> Revenue would have come from the margin between the wholesale cost of goods stocked in Cache Units and the retail price paid by consumers through the delivery platforms — minus the platform commission (typically 15–30% for delivery apps). This is a standard convenience retail margin model, compressed by platform fees.

A secondary revenue stream could have come from charging property owners or commercial landlords a placement fee for hosting Cache Units, analogous to a vending machine placement model. No public source confirms this.

The "100x cheaper" cost claim implied that Cache's operating expense per unit was dramatically lower than a GoPuff micro-fulfillment center. <sup><a href="https://www.grabcache.com/">[8]</a></sup> If accurate, this would have allowed Cache to reach profitability at much lower order volumes per location — the essential requirement for suburban viability. The hardware cost of the Cache Units themselves, the inventory carrying cost, and the restocking logistics cost were never disclosed, making independent assessment of the unit economics impossible.

---

## Traction

Cache had two live Cache Units at the time of its most detailed press coverage in May 2022: one in Sausalito, California (OTC medicine and snacks) and one in South San Francisco, California (ice cream). <sup><a href="https://xunbaodui.com/products/urkc75hl">[11]</a></sup> No order volume, revenue, average order value, or customer count data was ever publicly disclosed.

The two-unit deployment, roughly nine months after founding, suggests the team was still in early pilot mode at the time the company wound down. Whether the units were generating meaningful revenue, breaking even on a per-unit basis, or operating at a loss is unknown. The absence of any expansion announcement — no third unit, no new market, no partnership press release — is the most telling traction signal available.

---

## Post-Mortem

Cache's failure was confirmed by co-founder Jimmy Young, who wrote in a LinkedIn reflection: "even though my first startup failed, I learned a ton." <sup><a href="https://www.linkedin.com/in/jimmyyoungsydney/">[12]</a></sup> No formal post-mortem, shutdown announcement, or detailed explanation was ever published by either founder. What follows is reconstructed from public records, funding data, and the company's operational timeline.

### Primary Cause: A $125,000 Pre-Seed Cannot Fund Hardware Infrastructure

Cache's fundamental problem was a structural mismatch between its capital and its model.

Hardware-dependent startups require capital before revenue. A Cache Unit must be manufactured, installed, stocked with inventory, and connected to delivery platforms before it generates a single order. Each unit represents a fixed cost that must be recovered through future sales. Proving that the unit economics work — that a Cache Unit in a suburban location generates enough order volume at sufficient margin to cover its costs — requires deploying enough units in enough locations to generate statistically meaningful data.

Cache raised $125,000 from Y Combinator. <sup><a href="https://www.crunchbase.com/organization/cache-0d59">[4]</a></sup> For a two-person team in San Francisco, this covers roughly three to four months of founder salaries at below-market rates, with nothing left for hardware manufacturing, inventory, or logistics. The company managed to deploy two units — in Sausalito and South San Francisco — which suggests the founders were operating with extreme capital efficiency, likely funding inventory out of pocket or through supplier credit. But two units in two adjacent Bay Area markets cannot prove a suburban rollout thesis. They can only prove that the hardware works and that some orders come in.

At Demo Day in August 2021, Young stated Cache was "raising our first round very soon." <sup><a href="https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1">[3]</a></sup> No seed round was ever announced. Crunchbase records no funding beyond the YC pre-seed. <sup><a href="https://www.crunchbase.com/organization/cache-0d59">[13]</a></sup> PitchBook lists Zentani Capital as a possible additional investor, but this is unconfirmed and no amount is recorded. <sup><a href="https://pitchbook.com/profiles/company/471265-75">[14]</a></sup> The most likely interpretation: Cache pitched investors after Demo Day, did not close a round, and exhausted its runway before it could prove enough to change that outcome.

### Secondary Cause: The Seed Round Window Closed as the Market Contracted

Cache was seeking its first external capital in late 2021 and early 2022, precisely as the instant-delivery sector began its public unraveling.

In 2022, the rapid-delivery category that had attracted billions in venture capital in 2020–2021 collapsed with unusual speed. Gorillas was acquired under duress. Jokr exited the U.S. Fridge No More shut down entirely. GoPuff laid off 1,500 employees in March 2022 and another 7% of its workforce in July 2022. DashMart quietly reduced its footprint. The investor narrative shifted from "rapid delivery is the future of retail" to "rapid delivery unit economics are fundamentally broken."

Cache was pitching a dark store model to investors who were watching dark store companies burn cash at scale and still fail to reach profitability. The suburban angle — Cache's core differentiation — required investors to believe that a two-person team with two pilot units had solved the unit economics problem that well-funded competitors with hundreds of employees had not. In a risk-on environment, that pitch might have found takers. In the environment of early 2022, it almost certainly did not.

This is inferred from timing rather than direct evidence. No investor meeting notes or rejection letters are available. But the correlation between the market contraction and Cache's failure to close a round is the most parsimonious explanation for why a team with credible DoorDash pedigree and a coherent thesis could not raise capital.

### Tertiary Cause: Two Founders Cannot Simultaneously Build Hardware, Operate Stores, and Fundraise

Cache's team was two people. <sup><a href="https://www.ycombinator.com/companies/cache">[1]</a></sup> The company's operational requirements included: hardware development and manufacturing (building Cache Units), site selection and installation (finding suburban locations, negotiating placement), inventory management (stocking and restocking units without staff), platform operations (managing storefronts on DoorDash, UberEats, Postmates, Instacart), and fundraising (pitching investors post-Demo Day).

Each of these is a full-time function at a hardware-dependent startup. A two-person team cannot execute all of them simultaneously without making significant tradeoffs. The most likely tradeoff: the founders focused on keeping the two live units operational while fundraising, leaving no bandwidth for the hardware iteration and deployment expansion that would have generated the proof points investors needed to fund the next round.

Young's reflection — "Starting a company is the hardest thing we've ever done" <sup><a href="https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1">[3]</a></sup> — suggests the execution difficulty was felt acutely, though he did not specify which operational dimension was most constraining.

### Structural Risk: Platform Dependency as a Single Point of Failure

Cache's distribution was entirely dependent on third-party delivery platforms. This created a structural vulnerability that the founders, as DoorDash alumni, would have understood intellectually but may have underweighted in practice.

A Cache storefront on DoorDash competed for algorithmic visibility against DashMart — DoorDash's own first-party convenience product. Platform commission rates of 15–30% compressed the already-thin margins of convenience retail. Any policy change by DoorDash or UberEats — a change to storefront listing requirements, a commission increase, a change to driver dispatch logic — could materially affect Cache's revenue without any action by Cache itself.

No public evidence indicates that platform dynamics directly caused Cache's failure. But the dependency meant Cache had no proprietary distribution moat: its customer acquisition was entirely mediated by platforms that had their own competing interests.

### Wind-Down

Cache wound down quietly, with no formal announcement. The grabcache.com website remained live with its original marketing copy and waitlist form, consistent with a company that stopped operating rather than one that formally dissolved. <sup><a href="https://www.grabcache.com/">[8]</a></sup> Young moved to Coinbase. <sup><a href="https://www.linkedin.com/in/jimmyyoungsydney/">[12]</a></sup> Wu joined Samsara, then Hims & Hers, before becoming an investor at Moxxie Ventures in October 2024 — where he was described as "a former YC founder." <sup><a href="https://moxxie.substack.com/p/moxxies-got-more-moxxie">[9]</a></sup>

---

## Key Lessons

- **Hardware startups require hardware-scale capital from day one.** Cache's model required manufacturing, deploying, stocking, and maintaining physical units before generating revenue. The $125,000 YC pre-seed is calibrated for software companies that can reach meaningful traction with a small team and low marginal costs. A hardware-dependent dark store model needed a seed round of $1–3M minimum to deploy enough units to generate proof points. Attempting to prove hardware unit economics on pre-seed capital is structurally very difficult — the capital runs out before the data exists.

- **Platform dependency is a distribution strategy, not a moat.** Cache's entire go-to-market relied on DoorDash, UberEats, Postmates, and Instacart for customer acquisition and order fulfillment. This gave Cache fast access to consumers but no proprietary relationship with them, no pricing power, and no protection against platform policy changes. Building on top of platforms that have their own competing products (DashMart) is a particularly acute version of this risk — the distribution partner is also a direct competitor for algorithmic placement.

- **Market timing is a real variable, not an excuse.** Cache's seed fundraising window coincided almost exactly with the collapse of investor confidence in the rapid-delivery category. A company with the same team, same product, and same two pilot units pitching in mid-2021 — before the category's unit economics became a public narrative — would have faced a materially different fundraising environment. This does not mean Cache's model was sound, but it illustrates that the external fundraising environment can determine a startup's fate independently of product quality.

- **Two-person teams face compounding bandwidth constraints in hardware businesses.** Software startups can sometimes reach product-market fit with two engineers and a laptop. Hardware startups require simultaneous execution across manufacturing, operations, logistics, sales, and fundraising. Cache's two founders could not staff all of these functions, and the gaps — particularly in hardware iteration speed and deployment scale — likely contributed directly to the thin proof points available when they needed to raise capital.

---

## Sources

1. [Cache — Y Combinator Company Profile](https://www.ycombinator.com/companies/cache)
2. [Jimmy Young LinkedIn Founding Announcement (August 4, 2021)](https://www.linkedin.com/posts/jimmyyoungsydney_cache-automated-delivery-first-convenience-activity-6828747289419505664-MCi1)
3. [Yet Another Startup — Cache Deep Dive (May 9, 2022)](https://yetanotherstartup.com/p/cache)
4. [Cache — Crunchbase Funding Profile](https://www.crunchbase.com/organization/cache-0d59)
5. [TechCrunch — Tracking Startup Focus in the Latest Y Combinator Cohort (September 2, 2021)](https://techcrunch.com/2021/09/02/tracking-startup-focus-in-the-latest-y-combinator-cohort/)
6. [Science of the Time — "After Stores Go Dark, They Cache Goods" (April 28, 2022)](https://scienceofthetime.com/2022/04/28/after-stores-go-dark-they-cache-goods/)
7. [Cache Product Website — grabcache.com](https://www.grabcache.com/)
8. [Cache — Product Hunt / Xunbaodui Launch Profile](https://xunbaodui.com/products/urkc75hl)
9. [Moxxie Ventures — "Moxxie's Got More Moxxie" (October 14, 2024)](https://moxxie.substack.com/p/moxxies-got-more-moxxie)
10. [Alexandre Substack — YC Summer Batch 2021 Overview (August 30, 2021)](https://alexandre.substack.com/p/-y-combinator-summer-batch-2021)
11. [Jimmy Young — LinkedIn Profile (Current)](https://www.linkedin.com/in/jimmyyoungsydney/)
12. [Cache — PitchBook Profile](https://pitchbook.com/profiles/company/471265-75)
13. [Medium / Science of the Time — "After Stores Go Dark, They Cache Goods"](https://medium.com/@SotT_team/after-stores-go-dark-they-cache-goods-ab8426dca2c2)
14. [Internet Archive — Wayback Machine Captures of grabcache.com](https://web.archive.org/web/20211001000000*/grabcache.com)
