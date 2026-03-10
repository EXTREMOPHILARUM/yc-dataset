# Research Report: Carsabi

## Overview

Carsabi was a used car search aggregator founded in October 2011 by Christopher Berner and Dwight Crow.Operating out of San Francisco as a two-person team, it aimed to be the "Google for used cars"—crawling Craigslist, dealer websites, and specialty auto classifieds to surface real-time deals ranked by savings rather than raw price.The company graduated from Y Combinator's Winter 2012 batch, earned a spot on TechCrunch's list of the ten best companies from Demo Day, and raised a seed round from YC and DCVC.

It shut down within a year.The core failure was structural: Carsabi's entire value proposition depended on scraping Craigslist without a data licensing agreement.When Craigslist blocked access, traffic halved overnight.

With only two employees and approximately $20,000 in total funding, the company had no resources to negotiate, litigate, or rebuild around alternative sources.The founders were acqhired by Facebook in October 2012; the product was sold to Ark.com in December 2012 and closed by February 2014.

<report-gallery>
<media-image src="https://techcrunch.com/wp-content/uploads/2012/03/yc-demo-day-w12.jpg" alt="YC W12 Demo Day at the Computer History Museum, Mountain View, March 2012" caption="Y Combinator Winter 2012 Demo Day at the Computer History Museum — where Carsabi pitched to a room of investors, reported 10% week-on-week growth, and earned a spot on TechCrunch's list of the ten best companies of the day. Seven months later, the company would be gone."></media-image>
<media-image src="https://techcrunch.com/wp-content/uploads/2012/10/carsabi-founders-join-facebook-23-pm-copy-2-done-copy.png" alt="TechCrunch article: Facebook Acqhires Founders of Carsabi — October 1, 2012" caption="The article that marked the end: TechCrunch's October 1, 2012 report on Facebook's acqhire of Berner and Crow. Buried in the announcement was the real cause of death — Craigslist had quietly blocked Carsabi's crawler, cutting traffic in half and leaving a two-person team with no path forward."></media-image>
</report-gallery>

## Founding Story

Carsabi was founded in October 2011 by Christopher Berner and Dwight Crow.<sup><a href="https://tracxn.com/d/companies/carsabi/__3VILNexhHYyahlev1iSu65_JdiEv7e0vup270Hzc86E">[1]</a></sup> The two operated out of San Francisco, working from 22 Battery Street.<sup><a href="https://www.cbinsights.com/company/carsabi">[2]</a></sup> No public record details their prior professional backgrounds or how they met, but their acceptance into Y Combinator's Winter 2012 batch—within weeks of founding—indicates the idea was compelling enough to win YC's attention almost immediately after inception.<sup><a href="https://vator.tv/2012-10-02-facebook-lures-away-carsabi-co-founders/">[3]</a></sup>

The founding thesis was straightforward: buying a used car online was broken. Listings were scattered across Craigslist, dealer websites, and specialty classifieds, with no single tool that let buyers compare value across all of them simultaneously. Berner and Crow set out to fix that by building a crawler that would index every automotive listing it could find and present results ranked by actual savings—not just sticker price. Their stated goal, as written on the Carsabi blog, was "to index every automotive vehicle and connect more users to their car of choice each day."<sup><a href="https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/">[4]</a></sup>

By January 2012—just three months after founding—the product was already operational, indexing approximately 20,000 dealership and classified car listings daily.<sup><a href="https://carsabi.wordpress.com/">[5]</a></sup> Dwight Crow managed the company blog, publishing used car buying tips that doubled as content marketing for the nascent product.<sup><a href="https://carsabi.wordpress.com/">[6]</a></sup>

One notable dimension of the founding period: Dwight Crow was simultaneously a cast member on Bravo's reality show *Silicon Valley Startups* at the time of the company's operation.<sup><a href="https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/">[7]</a></sup> The show gave Carsabi a degree of public visibility disproportionate to its actual scale—a two-person startup with a seed-stage product. Whether the media obligations affected execution focus is unknown; no evidence in either direction exists.

<media-image src="https://techcrunch.com/wp-content/uploads/2012/03/yc-demo-day-w12.jpg" alt="YC W12 Demo Day at the Computer History Museum, Mountain View, March 2012" caption="Y Combinator Winter 2012 Demo Day at the Computer History Museum in Mountain View — where Carsabi pitched alongside Crowdtilt, Priceonomics, and others in Session 3."></media-image>

The company did not undergo any documented pivots. From founding through shutdown, Carsabi pursued the same core product: an aggregated used car search engine that ranked listings by value. The speed of the founding-to-YC pipeline, the early product activity, and the absence of pivots all suggest a team that moved fast and stayed focused—but also one that never had the runway to stress-test its most critical assumption: that the data sources it depended on would remain accessible.

---

## Timeline

- **October 2011** — Carsabi founded by Christopher Berner and Dwight Crow in San Francisco.<sup>[[1]](https://tracxn.com/d/companies/carsabi/__3VILNexhHYyahlev1iSu65_JdiEv7e0vup270Hzc86E)</sup>

- **January 2012** — Product operational; blog active; indexing approximately 20,000 car listings daily.<sup>[[5]](https://carsabi.wordpress.com/)</sup>

- **February 2012** — Carsabi officially launches its used car search engine.<sup>[[8]](https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/)</sup>

- **March 27, 2012** — Carsabi presents at YC W12 Demo Day at the Computer History Museum; reports 10% week-on-week growth since launch; raises seed round from YC and DCVC; named one of TechCrunch's 10 Best Companies from Demo Day.<sup>[[8]](https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/)</sup><sup>[[9]](https://techcrunch.com/2012/03/27/best-of-y-combinator-demo-day/)</sup><sup>[[10]](https://tracxn.com/d/companies/carsabi/__3VILNexhHYyahlev1iSu65_JdiEv7e0vup270Hzc86E)</sup>

- **October 1, 2012** — Facebook acqhires founders Berner and Crow; does not acquire the Carsabi product; founders publicly seek a buyer for the service; VentureBeat reports Craigslist had blocked Carsabi, halving its traffic.<sup>[[11]](https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/)</sup><sup>[[12]](https://venturebeat.com/entrepreneur/facebook-acqui-hires-carsab-more-for-the-sabi-than-the-car/)</sup>

- **December 11, 2012** — Ark.com acquires the Carsabi service; Hacker News post confirms the deal; commenter characterizes it as a minor transaction relative to a full acquisition.<sup>[[13]](https://news.ycombinator.com/item?id=4869526)</sup>

- **February 2014** — Crunchbase records Carsabi's official closed date, indicating the product did not survive under Ark's ownership.<sup>[[14]](https://www.crunchbase.com/organization/carsabi)</sup>

<media-hn url="https://news.ycombinator.com/item?id=4869526" title="Ark bought Carsabi" points="" comments=""></media-hn>

---

## What They Built

Carsabi was a used car search aggregator—a single interface that pulled listings from across the fragmented online car market and presented them in a unified, sortable format. The core problem it addressed was real: in 2012, a buyer looking for a used Honda Civic had to check Craigslist, AutoTrader, Cars.com, individual dealer websites, and specialty classifieds separately, with no easy way to compare value across all of them at once.

<media-image src="https://techcrunch.com/wp-content/uploads/2012/10/carsabi.png" alt="Carsabi logo and branding from TechCrunch acqhire article, October 2012" caption="Carsabi branding as featured in TechCrunch's October 2012 article covering the Facebook acqhire of founders Dwight Crow and Christopher Berner."></media-image>

**How it worked.** Carsabi's algorithms crawled every major online auto site—Craigslist, dealership websites, specialty auto collections, and other classifieds—and extracted structured data from each listing in real time.<sup><a href="https://www.crunchbase.com/organization/carsabi">[15]</a></sup> A user could search by make, model, year, and location, and Carsabi would return results aggregated from all of those sources simultaneously. By January 2012, the system was processing approximately 20,000 listings per day.<sup><a href="https://carsabi.wordpress.com/">[5]</a></sup>

**The key differentiator.** The product's most distinctive feature was sorting by "biggest savings" rather than lowest price.<sup><a href="https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/">[16]</a></sup> This is a meaningful distinction. Lowest price favors high-mileage, high-age vehicles regardless of condition. Biggest savings requires the system to estimate fair market value for a given vehicle configuration and then calculate how far below that value a specific listing sits. A $12,000 listing for a car worth $15,000 would rank above a $9,000 listing for a car worth $9,500. This value-relative framing was Carsabi's primary argument against established players like AutoTrader, which sorted by price alone.

**Social features.** Carsabi integrated a social layer that let users share listings with friends and ask for purchase advice.<sup><a href="https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/">[17]</a></sup> This served two purposes: it gave buyers a way to get a second opinion before committing to a large purchase, and it created a viral distribution mechanism—each share exposed Carsabi to a new potential user. Whether this feature gained meaningful adoption is unknown; no usage data exists in the public record.

<media-image src="https://web.archive.org/web/20120403120000im_/http://carsabi.com/" alt="Archived Carsabi.com homepage from April 2012" caption="Wayback Machine screenshot of Carsabi.com circa April 2012 — the used car search engine that crawled Craigslist, dealer sites, and classifieds to surface the best deals."></media-image>

**Technology.** The product was fundamentally a web crawler paired with a structured data extraction layer and a search interface. Crawling unstructured HTML from diverse sources—each with different page layouts, data formats, and anti-scraping measures—is technically demanding. The fact that two engineers had it operational within three months of founding suggests meaningful technical capability. The architecture, however, created the company's fatal vulnerability: it had no data licensing agreements with any of its sources, meaning access could be revoked unilaterally at any time.

**What made it different.** AutoTrader and Cars.com in 2012 were primarily dealer listing networks—they charged dealers to list vehicles and charged consumers nothing, but their inventory was limited to paying participants. Craigslist had broader inventory but no search sophistication. Carsabi's proposition was to combine the breadth of Craigslist with the structure of AutoTrader and add a value-ranking layer that neither offered. The product vision was coherent. The data supply chain was not.

---

## Market Position

### Target Customers

Carsabi targeted individual used car buyers—consumers navigating a high-stakes, infrequent purchase with limited information. The used car buying process in 2012 was genuinely painful: prices were opaque, listings were scattered, and buyers had no reliable way to assess whether a given price was fair without significant manual research. Carsabi's value proposition was clearest for buyers who already knew what vehicle they wanted and needed help finding the best available deal across all online sources simultaneously.

The social sharing feature suggests the founders also had a secondary target: buyers who involved friends or family in major purchase decisions—a common behavior for a transaction of this size. This group would have been more likely to share listings and generate organic referrals.

### Market Size

At Demo Day, Carsabi cited $650 billion in annual car sales and $3.8 billion in annual auto advertising as the market opportunity.<sup><a href="https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/">[18]</a></sup> These figures are accurate for the total U.S. automotive market but overstate the addressable opportunity for a used car search aggregator. The more relevant figure is the used car segment specifically, and within that, the portion of transactions that originate from online search—a subset that was growing rapidly in 2012 but was not yet dominant.

The advertising revenue model (discussed below) would have competed for a share of the $3.8 billion auto advertising market, primarily the portion allocated to digital channels. That market was real and growing, but it was already contested by well-capitalized incumbents.

### Competition

The competitive landscape in 2012 was well-established and well-funded:

**AutoTrader** was the dominant player, operating a dealer listing network with national scale and significant brand recognition. It charged dealers for listings and generated revenue through advertising. Its weakness was inventory breadth—only paying dealers listed vehicles—and its sorting was price-based rather than value-based.

**Cars.com** operated a similar model to AutoTrader, with comparable strengths and weaknesses. Both AutoTrader and Cars.com had the advantage of direct dealer relationships, which gave them data access that didn't depend on scraping.

**Craigslist** had the broadest used car inventory of any single platform, including private-party sellers who didn't list elsewhere. It had no search sophistication, no value ranking, and no structured data. It was Carsabi's most important data source and, ultimately, its most dangerous dependency.

**TrueCar** (which went public in 2014) was also operating in this period, focused on price transparency for new and used cars through dealer partnerships. It had a different model—dealer-paid, consumer-facing price reports—but addressed the same underlying consumer pain point.

Carsabi's differentiation was real but fragile. Its "biggest savings" ranking required data from all sources simultaneously, which meant it needed scraping access to remain competitive. Any incumbent with direct data relationships—or any new entrant that secured licensing agreements—would have a structurally superior position.

---

## Business Model

Carsabi's intended revenue model was advertising-based, consistent with the broader auto classifieds industry. The $3.8 billion annual auto advertising market cited at Demo Day was the target pool.<sup><a href="https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/">[18]</a></sup> The most natural implementation would have been dealer advertising—charging dealerships to promote their listings or appear prominently in search results, a model used by AutoTrader and Cars.com.

A secondary possibility was lead generation: charging dealers a fee per qualified buyer referral, which was a common model in auto classifieds at the time. TrueCar used a similar approach.

Neither model was publicly confirmed as the primary revenue strategy, and no revenue figures are available in the public record. Given that the company operated for approximately eleven months with two employees and roughly $20,000 in total funding,<sup><a href="https://www.cbinsights.com/company/carsabi">[19]</a></sup> it is unlikely that meaningful revenue was generated before the Craigslist block ended the company's growth trajectory. The business model was aspirational rather than operational at the time of shutdown.

---

## Traction

Carsabi launched in mid-February 2012 and reported 10% week-on-week growth at YC Demo Day on March 27, 2012—approximately six weeks of growth data.<sup><a href="https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/">[8]</a></sup> No absolute user or traffic figures are available, which limits interpretation of this metric. Ten percent week-on-week growth compounding from a very small base produces a still-small number after six weeks.

On the supply side, the product was indexing approximately 20,000 car listings daily as of January 2012,<sup><a href="https://carsabi.wordpress.com/">[5]</a></sup> before the official launch. This suggests the crawling infrastructure was functional and scaling ahead of the consumer-facing product.

The strongest traction signal was editorial: TechCrunch named Carsabi one of the ten best companies from YC W12 Demo Day,<sup><a href="https://techcrunch.com/2012/03/27/best-of-y-combinator-demo-day/">[9]</a></sup> a judgment made by journalists who saw all 66 companies present. This is a meaningful signal of product clarity and pitch quality, though it does not translate directly to user adoption or revenue.

The seed round from YC and DCVC closed on Demo Day.<sup><a href="https://tracxn.com/d/companies/carsabi/__3VILNexhHYyahlev1iSu65_JdiEv7e0vup270Hzc86E">[10]</a></sup> CB Insights records total funding of approximately $20,000,<sup><a href="https://www.cbinsights.com/company/carsabi">[19]</a></sup> consistent with YC's standard investment for the era. If DCVC participated beyond the YC check, the amount was not disclosed and did not appear to provide meaningful additional runway.

---

## Post-Mortem

<media-image src="https://techcrunch.com/wp-content/uploads/2012/10/carsabi-founders-join-facebook-23-pm-copy-2-done-copy.png" alt="TechCrunch article: Facebook Acqhires Founders of Carsabi — October 1, 2012" caption="TechCrunch's October 1, 2012 article covering the Facebook acqhire of Dwight Crow and Christopher Berner, and Carsabi's search for a buyer — the definitive post-mortem on the company."></media-image>

### Primary Cause: Craigslist Blocked Access, Halving Traffic Overnight

The proximate cause of Carsabi's failure was Craigslist blocking the company from indexing its car listings, which caused Carsabi's traffic to drop by approximately 50%.<sup><a href="https://venturebeat.com/entrepreneur/facebook-acqui-hires-carsab-more-for-the-sabi-than-the-car/">[12]</a></sup> The block occurred sometime between Demo Day in late March 2012 and the Facebook acqhire announcement on October 1, 2012—a window of roughly six months.

This was not an unpredictable event. Craigslist had a well-documented history of aggressively blocking scrapers and had previously pursued legal action against aggregators that accessed its data without authorization. Building a product whose core value proposition depended on Craigslist inventory—without a data licensing agreement—was a structural fragility present from day one. Craigslist's car listings were uniquely valuable because they included private-party sellers who did not list on AutoTrader or Cars.com. Losing that inventory didn't just reduce Carsabi's listing count; it eliminated the category of listings that most differentiated it from established competitors.

The team made no documented attempt to negotiate a data license with Craigslist before or after the block. No evidence exists of a legal response or a technical workaround that succeeded. With two employees and approximately $20,000 in total funding,<sup><a href="https://www.cbinsights.com/company/carsabi">[19]</a></sup> the company had no realistic path to litigate, negotiate, or rebuild around alternative sources quickly enough to matter. The block was effectively a death sentence.

VentureBeat captured the downstream consequence clearly: it was "unclear who would want to buy a scraping service that was blocked from one of its key scraping sources and had limited investment as a YC company."<sup><a href="https://venturebeat.com/entrepreneur/facebook-acqui-hires-carsab-more-for-the-sabi-than-the-car/">[12]</a></sup>

### Secondary Cause: Undercapitalization Left No Buffer for Adversity

Carsabi raised approximately $20,000 in total funding across its entire life.<sup><a href="https://www.cbinsights.com/company/carsabi">[19]</a></sup> For a company building a data-intensive product in a market dominated by well-capitalized incumbents—AutoTrader had raised hundreds of millions before going public in 2015—this was an extraordinarily thin capital base.

The undercapitalization had several compounding effects. First, it meant the company could not hire beyond its two founders, limiting its ability to build redundant data pipelines or pursue business development with data providers. Second, it meant the company had no runway to absorb a 50% traffic loss and pivot—when the Craigslist block hit, there was no capital to fund a recovery period. Third, it made the company unattractive as a product acquisition target: VentureBeat noted the limited investment explicitly as a factor reducing acquirer interest in the Carsabi service.<sup><a href="https://venturebeat.com/entrepreneur/facebook-acqui-hires-carsab-more-for-the-sabi-than-the-car/">[12]</a></sup>

Whether the founders chose not to raise more aggressively after Demo Day or were unable to close a larger round is unknown. The seed round from YC and DCVC closed on Demo Day,<sup><a href="https://tracxn.com/d/companies/carsabi/__3VILNexhHYyahlev1iSu65_JdiEv7e0vup270Hzc86E">[10]</a></sup> and no subsequent financing rounds are recorded. Given TechCrunch's favorable coverage and the 10% week-on-week growth metric, investor interest at Demo Day was plausible—but the Craigslist dependency, if known to sophisticated investors, would have been a significant concern.

### Tertiary Cause: No Data Licensing Strategy

Carsabi's product architecture assumed that scraping access to third-party platforms would remain available indefinitely. This assumption was never validated through licensing agreements, and no evidence suggests the founders pursued such agreements before the Craigslist block materialized.

A licensing agreement with Craigslist would have been difficult to obtain—Craigslist was notoriously protective of its data and had no established licensing program for third-party aggregators. But the absence of any documented attempt to secure data access through legitimate channels meant the company was building on borrowed time from its first day of operation.

The alternative—building direct relationships with dealers to obtain inventory data—would have required business development resources the company didn't have and would have replicated the model of AutoTrader and Cars.com rather than differentiating from it. There was no clean path out of the data dependency problem at Carsabi's scale and funding level.

### The Exit: Talent Valued, Product Discarded

On October 1, 2012, Facebook announced it had acqhired Berner and Crow.<sup><a href="https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/">[11]</a></sup> Facebook explicitly did not acquire the Carsabi product. Its public statement—"We are always looking for great entrepreneurs who want to have big impact, and Christopher and Dwight are exactly that. We can't wait to welcome them both to Facebook"<sup><a href="https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/">[20]</a></sup>—was generic. Facebook would not disclose what team the founders were joining, and told TechCrunch there was "nothing specific" that attracted it to them beyond being "awesome entrepreneurs."<sup><a href="https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/">[21]</a></sup> This is the language of a talent acquisition with no strategic interest in the automotive search space.

The founders posted on the Carsabi blog: "We created Carsabi back in Oct 2011 with the goal of easing the process of purchasing a used car... Because Facebook is not acquiring Carsabi.com, we're looking for someone to buy the Carsabi service, so the two of us can focus on our new jobs."<sup><a href="https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/">[22]</a></sup> The framing—"so the two of us can focus on our new jobs"—indicates the founders had already mentally exited the company before a buyer was found.

In December 2012, Ark.com acquired the Carsabi service for undisclosed terms.<sup><a href="https://www.cbinsights.com/company/carsabi">[23]</a></sup> A Hacker News commenter described the deal as "probably beneficial for all parties, but not as big of a deal as a full acquisition (by a mile)."<sup><a href="https://news.ycombinator.com/item?id=4869526">[24]</a></sup> Crunchbase records Carsabi's closed date as February 2014,<sup><a href="https://www.crunchbase.com/organization/carsabi">[14]</a></sup> confirming that the Ark acquisition did not result in a meaningful continuation of the product. What Ark did with the service in the intervening fourteen months is unknown.

The acqhire outcome—Facebook wanting the founders but not the product—is the clearest possible signal that Carsabi's value resided in the people who built it, not in what they built. The product, stripped of its founders and blocked from its primary data source, was worth approximately nothing as a going concern.

---

## Key Lessons

- **Scraping a platform without a licensing agreement is not a data strategy—it is a countdown timer.** Craigslist's decision to block Carsabi was entirely within its rights and entirely predictable given its history of aggressive action against scrapers. Any company whose core value proposition depends on data it does not own, license, or control is one unilateral decision away from losing its product. The lesson is not that scraping is always wrong, but that it cannot be the *only* data strategy for a product that lives or dies by data completeness. Carsabi needed either a licensing agreement, a diversified source base resilient to any single block, or a pivot to a model that owned its data—and it pursued none of these.

- **Early press enthusiasm and week-on-week growth percentages are not substitutes for supply chain resilience.** Carsabi earned a TechCrunch Top 10 designation and reported 10% week-on-week growth at Demo Day.<sup><a href="https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/">[8]</a></sup><sup><a href="https://techcrunch.com/2012/03/27/best-of-y-combinator-demo-day/">[9]</a></sup> Neither metric had any bearing on whether Craigslist would block access six months later. Demand-side signals (users, growth, press) are necessary but not sufficient for a product whose supply side is structurally fragile. Investors and founders should weight supply chain risk equally with demand signals, particularly when the supply chain involves third-party platforms with a history of blocking aggregators.

- **Minimum viable capitalization for a data-dependent business is higher than minimum viable capitalization for a software business.** Two engineers can build and launch a software product on $20,000. They cannot negotiate data licensing agreements, pursue legal remedies against platform blocks, or rebuild data pipelines after a catastrophic source loss on $20,000. Carsabi's funding was appropriate for a prototype but not for a production data business competing against well-capitalized incumbents. The mismatch between the ambition of the product and the capital raised to support it left no margin for the adversity that materialized.

- **The acqhire as outcome reflects founder quality, not product success.** Facebook's decision to hire Berner and Crow while explicitly declining to acquire the product confirms that the founders were talented engineers and entrepreneurs whose skills exceeded the specific application they built. This is a useful frame for evaluating acqhire outcomes generally: when a large company wants the people but not the product, it is paying for optionality on human capital, not validating the startup's thesis.

---

## Sources

1. [Tracxn – Carsabi Company Profile](https://tracxn.com/d/companies/carsabi/__3VILNexhHYyahlev1iSu65_JdiEv7e0vup270Hzc86E)
2. [CB Insights – Carsabi Company Profile](https://www.cbinsights.com/company/carsabi)
3. [Vator.tv – "Facebook Lures Away Carsabi Co-Founders" (October 2, 2012)](https://vator.tv/2012-10-02-facebook-lures-away-carsabi-co-founders/)
4. [TechCrunch – "Facebook Acqhires Founders of Carsabi" (October 1, 2012)](https://techcrunch.com/2012/10/01/facebook-acqhires-founders-of-carsabi-who-will-sell-off-their-car-price-comparison-site/)
5. [Carsabi WordPress Blog](https://carsabi.wordpress.com/)
6. [TechCrunch – "Y Combinator Demo Day Session 3" (March 27, 2012)](https://techcrunch.com/2012/03/27/y-combinator-demo-day-session-3/)
7. [TechCrunch – "Best of Y Combinator Demo Day" (March 27, 2012)](https://techcrunch.com/2012/03/27/best-of-y-combinator-demo-day/)
8. [VentureBeat – "Facebook Acqui-Hires Carsabi" (October 1, 2012)](https://venturebeat.com/entrepreneur/facebook-acqui-hires-carsab-more-for-the-sabi-than-the-car/)
9. [Crunchbase – Carsabi Organization Profile](https://www.crunchbase.com/organization/carsabi)
10. [Hacker News – "Ark bought Carsabi" (December 11, 2012)](https://news.ycombinator.com/item?id=4869526)
