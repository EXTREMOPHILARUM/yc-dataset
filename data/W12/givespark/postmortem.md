# Research Report: GiveSpark

## Overview

Joe Teplow — also referred to in press as Josef Teplow — was a pre-med undergraduate at Yeshiva University in New York when his interest in charitable giving first took an organized form. Before GiveSpark, he had published a newsletter called Good St., built around the idea that giving small amounts frequently was more sustainable and impactful than infrequent large donations.<sup><a href="https://ejewishphilanthropy.com/good-today-brings-the-pushke-to-corporate-social-responsibility/">[3]</a></sup> That newsletter would eventually become Good Today, but in 2012 Teplow's attention was focused on a different problem: the gap between celebrity awareness-raising and actual charitable dollars.

The insight was grounded in observable behavior. Celebrities were already using Twitter to amplify causes they cared about — posting about bone marrow registries, disaster relief funds, and advocacy campaigns. Their followers engaged with those posts. But engagement did not translate into donations. There was no mechanism to close that loop. GiveSpark was Teplow's attempt to build that mechanism.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[4]</a></sup>

The company was accepted into Y Combinator's Winter 2012 batch, one of 66 companies in that cohort.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[5]</a></sup> YC's company listing records a team size of one, making Teplow a solo founder — though VentureBeat's Demo Day coverage refers to "Teplow and his team," suggesting possible informal collaborators whose identities are not confirmed in any public record.<sup><a href="https://www.ycombinator.com/companies/givespark">[6]</a></sup> The company was headquartered in Palo Alto, CA, consistent with the YC residency model.

Teplow's pitch at Demo Day distilled the product concept into a single memorable line: "It's Twitter, just with money."<sup><a href="https://venturebeat.com/company/givespark">[7]</a></sup> That framing captured both the product's strength — it was familiar, social, and low-friction for fans — and its structural dependency: without Twitter-scale celebrity participation, the analogy collapsed.

Before Demo Day, Teplow had already run a test campaign with an unnamed celebrity for a bone marrow foundation, raising $87,000 in two weeks.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[8]</a></sup> That result gave the Demo Day pitch credibility and generated coverage from both TechCrunch and VentureBeat. It also set an expectation that the platform could not subsequently meet — at least not in any documented way.

No information is available on how Teplow connected with the celebrity used in the test campaign, what the original YC application contained, or whether any co-founders or employees joined the company after its founding.

---

## Founding Story

### Timeline

- **February 2012** — GiveSpark's Twitter account (@Givespark) is created, establishing the company's earliest confirmed public presence.<sup>[[9]](https://x.com/givespark)</sup>

- **Early 2012** — GiveSpark founded by Joe Teplow; accepted into Y Combinator's Winter 2012 (W12) batch.<sup>[[1]](https://www.ycombinator.com/companies/givespark)</sup>

- **March 2012** — GiveSpark runs a test campaign with an unnamed celebrity for a bone marrow foundation, raising $87,000 in two weeks — the company's only documented traction metric.<sup>[[8]](https://techcrunch.com/2012/03/27/yc-demo-day-session-1/)</sup>

- **March 27, 2012** — GiveSpark presents at YC W12 Demo Day at the Computer History Museum in Mountain View, CA. TechCrunch and VentureBeat cover the pitch. Teplow describes the product as "It's Twitter, just with money."<sup>[[5]](https://techcrunch.com/2012/03/27/yc-demo-day-session-1/)</sup><sup>[[7]](https://venturebeat.com/company/givespark)</sup>

- **2012–2013** — GiveSpark operates with no further documented campaigns, funding rounds, or press coverage. The company receives a YC seed investment; the exact amount is undisclosed.<sup>[[10]](https://www.crunchbase.com/organization/givespark)</sup>

- **August 2013** — Joe Teplow co-founds Good Today (originally Good St.), a nonprofit subscription charity platform, while GiveSpark is still nominally operating — signaling a shift in founder attention.<sup>[[11]](https://www.crunchbase.com/person/joe-teplow)</sup>

- **April 2014** — Joe Teplow co-founds Rebelmail (later Rebel) with Trever Faden, an interactive email marketing platform. GiveSpark is presumed to have wound down by this point.<sup>[[11]](https://www.crunchbase.com/person/joe-teplow)</sup>

- **October 5, 2018** — Rebel (formerly Rebelmail) is acquired by Salesforce, marking a successful exit for Teplow.<sup>[[12]](https://techcrunch.com/2018/10/05/salesforce-acquires-rebel-maker-of-interactive-email-services-to-expand-its-marketing-cloud/)</sup>

- **October 29, 2019** — TechCrunch reports that after the Salesforce acquisition, Teplow has refocused on Good Today, which launches a new corporate donation tool with Tinder co-founder Sean Rad as co-founder.<sup>[[13]](https://techcrunch.com/2019/10/29/with-sean-rad-signed-on-as-co-founder-good-today-launches-new-tool-for-company-wide-donations/)</sup>

- **May 28, 2021** — eJewishPhilanthropy publishes a profile of Teplow tracing the origin of Good Today to his pre-med undergraduate newsletter at Yeshiva University.<sup>[[3]](https://ejewishphilanthropy.com/good-today-brings-the-pushke-to-corporate-social-responsibility/)</sup>

---

## What They Built

GiveSpark's core product was a fundraising platform that used celebrity social media influence as its primary acquisition channel for donors. The concept was simple: celebrities already had large, engaged audiences on Twitter, and they already used those audiences to highlight causes they cared about. GiveSpark gave those celebrities a structured way to turn that attention into actual donations.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[4]</a></sup>

The intended user experience worked in two directions. On the supply side, a celebrity would connect with GiveSpark, select or be matched with a philanthropic cause, and promote a campaign to their followers. On the demand side, fans who saw that promotion could click through to donate directly to the cause. The platform sat in the middle — handling the transaction infrastructure, the campaign presentation, and presumably the relationship between the celebrity and the nonprofit.

Teplow's "It's Twitter, just with money" framing was not just a pitch line — it described the product's design philosophy.<sup><a href="https://venturebeat.com/company/givespark">[7]</a></sup> Rather than building a standalone charity platform that required users to discover it independently, GiveSpark was designed to ride existing social graphs. The celebrity's Twitter following was the distribution mechanism. The platform did not need to build its own audience; it needed to convert an existing one.

The product was categorized by Crunchbase under Digital Entertainment, Mobile Apps, and Online Portals — suggesting a consumer-facing orientation rather than a B2B or nonprofit SaaS model.<sup><a href="https://www.crunchbase.com/organization/givespark">[10]</a></sup> The technical infrastructure ran on Amazon EC2, consistent with a lean early-stage web product built for rapid iteration.<sup><a href="https://www.crunchbase.com/organization/givespark">[14]</a></sup>

The only documented product deployment was the pre-Demo Day test campaign for a bone marrow foundation, which raised $87,000 in two weeks through an unnamed celebrity's promotion.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[8]</a></sup> That result demonstrated that the core mechanic worked: celebrity promotion could drive meaningful donation volume. What it did not demonstrate was whether the result was repeatable, scalable, or dependent on the specific celebrity's audience characteristics.

No product screenshots, archived UI, or detailed feature documentation are publicly available. The GiveSpark website (givespark.com) has limited captures in the Internet Archive from 2012, but no detailed product walkthroughs have been preserved in accessible press coverage.

What distinguished GiveSpark from existing charity platforms like JustGiving or Causes.com was its explicit reliance on celebrity as the primary distribution mechanism rather than as an optional feature. Most charity platforms treated celebrity endorsement as a marketing add-on. GiveSpark treated it as the product. That distinction made the platform potentially more powerful — and structurally more fragile.

---

## Market Position

### Target Customers

GiveSpark operated a two-sided market with distinct customer segments on each side.

On the supply side, the platform targeted celebrities with existing Twitter followings and demonstrated interest in charitable causes — specifically those who were already using social media to raise awareness but lacked a structured tool to convert that awareness into donations. The ideal celebrity partner was someone with a large, engaged audience and a specific cause affiliation, not a general philanthropic interest. The bone marrow foundation campaign suggests Teplow's initial targets were in the entertainment or sports space, where celebrity-cause associations are common and fan engagement is high.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[8]</a></sup>

On the demand side, the platform targeted fans of those celebrities — people who were already following and engaging with celebrity content on Twitter and could be converted into donors through a trusted, familiar social signal. This was not a traditional charity donor acquisition model. GiveSpark was not targeting existing donors and asking them to give more. It was targeting fans and asking them to give at all, using celebrity affinity as the conversion mechanism.

Nonprofits were a third stakeholder — the beneficiaries of the campaigns — but it is unclear whether they were paying customers, partners, or simply recipients. No information is available on how nonprofits were onboarded or what relationship they had with the platform commercially.

### Market Size

The addressable market for GiveSpark sat at the intersection of online charitable giving and social media marketing. U.S. online charitable giving was growing rapidly in 2012, driven by platforms like Kickstarter (founded 2009) and the broader normalization of digital payments. The total U.S. charitable giving market was approximately $316 billion in 2012, with online giving representing a small but fast-growing share.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[15]</a></sup>

The more relevant frame for GiveSpark's model was the celebrity-driven fundraising niche — campaigns where a specific individual's social capital was the primary driver of donations. This market was real but difficult to size, as it was fragmented across individual campaigns, charity galas, and ad hoc social media appeals. GiveSpark's bet was that systematizing this niche could unlock significant donation volume that was currently being left on the table.

### Competition

In 2012, GiveSpark's competitive landscape included several categories of adjacent platforms, none of which matched its exact model.

General charity fundraising platforms like JustGiving, FirstGiving, and Causes.com allowed individuals to create fundraising pages and share them socially, but they did not specifically target celebrities as the supply side or design their UX around the celebrity-fan dynamic. Causes.com, which operated on Facebook, was the closest analog — it had celebrity participation and social sharing built in — but it was a broader civic engagement platform rather than a celebrity-first fundraising tool.

Crowdfunding platforms like Kickstarter and Indiegogo were growing rapidly in 2012 but focused on creative projects and product funding rather than charitable giving. Their mechanics — reward tiers, campaign deadlines, all-or-nothing funding — were not designed for philanthropic use cases.

The absence of a direct competitor was both an opportunity and a warning sign. It meant GiveSpark had a clear differentiated position. It also meant there was no validated playbook for celebrity-driven charity fundraising at scale, and no evidence that the market would support a standalone for-profit platform in that niche.

---

## Business Model

GiveSpark was structured as a for-profit company despite its charitable focus — a tension that was never publicly resolved.<sup><a href="https://www.crunchbase.com/organization/givespark">[16]</a></sup> No information is available on the intended revenue model. The most plausible structures for a platform of this type would have included: a percentage fee on donations processed (the standard model for charity platforms like JustGiving, which charged 5% in 2012), a fee charged to nonprofits for campaign management, a fee charged to celebrities or their management teams for platform access, or a sponsorship/brand partnership model where companies paid to associate with celebrity campaigns.

None of these models were disclosed by Teplow or documented in press coverage. The for-profit designation on Crunchbase suggests Teplow intended to generate returns for investors, but the mechanism for doing so while routing money to nonprofits — and without alienating donors who might object to a commercial intermediary taking a cut of charitable donations — was never articulated publicly. This ambiguity was itself a structural problem: without a clear revenue model, GiveSpark could not make a credible case to investors for follow-on funding after the YC seed round.

---2f:T636,

## Traction

GiveSpark's only documented traction metric is the pre-Demo Day test campaign: $87,000 raised in two weeks for a bone marrow foundation through an unnamed celebrity's promotion.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[8]</a></sup> That figure was strong enough to anchor the Demo Day pitch and generate coverage from TechCrunch and VentureBeat — two of the most-read tech publications covering the YC cohort.

No subsequent traction data is available. There are no documented campaigns after Demo Day, no user counts, no donor retention figures, no nonprofit partner announcements, and no revenue disclosures. The $87,000 figure remains the entirety of GiveSpark's public performance record.

The YC seed investment — amount undisclosed — was the only confirmed funding round.<sup><a href="https://www.crunchbase.com/organization/givespark">[10]</a></sup> No Series A or follow-on seed round was announced, which is consistent with a company that failed to demonstrate repeatable traction after its initial proof-of-concept.

The gap between the Demo Day result and the absence of any subsequent data is itself informative. Either GiveSpark ran additional campaigns that were not covered by press (possible but unlikely given the Demo Day attention), or the platform failed to run additional campaigns at all after March 2012. The latter interpretation is supported by the timeline: Teplow began co-founding Good Today in August 2013, less than 18 months after Demo Day, suggesting GiveSpark had effectively stalled well before its formal closure.

---

## Post-Mortem

GiveSpark left no public post-mortem. Teplow has not given interviews discussing the company's failure, and no investor statements or shutdown announcements exist in the public record. What follows is an analysis of structural failure modes derived from the available evidence.

### Primary Cause: An Unscalable Celebrity Supply Chain

The most fundamental problem GiveSpark faced was that its entire product depended on a supply side — celebrity participation — that was structurally difficult to acquire, retain, and scale.

Celebrities are not a commodity. Each one is a unique combination of audience size, cause affiliation, management team, contractual obligations, and personal motivation. Acquiring a single celebrity for a test campaign is a relationship problem, not a product problem. Acquiring ten, fifty, or a hundred celebrities is a different category of challenge entirely — one that requires a dedicated partnerships team, legal infrastructure for talent agreements, and ongoing relationship management with celebrity handlers who are professionally skeptical of unproven platforms.

The test campaign raised $87,000, but the celebrity involved was never identified.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[8]</a></sup> That anonymity makes it impossible to assess how representative the result was. A celebrity with 10 million highly engaged followers promoting a cause they have personal history with will produce a very different result than a celebrity with 500,000 followers promoting a cause they were introduced to by a startup. If the test campaign succeeded because of a specific celebrity's exceptional audience engagement or personal connection to bone marrow donation — rather than because of GiveSpark's platform mechanics — then the result was not a proof-of-concept for the platform. It was a proof-of-concept for that one celebrity.

There is no evidence that GiveSpark ran a second campaign after Demo Day. If the company spent the months following Demo Day attempting to replicate the test campaign with additional celebrities and failed, that failure would explain both the absence of subsequent press coverage and Teplow's pivot toward Good Today by August 2013.

### Secondary Cause: An Undefined Revenue Model in a Charitable Context

GiveSpark was structured as a for-profit company, but no revenue model was ever disclosed.<sup><a href="https://www.crunchbase.com/organization/givespark">[16]</a></sup> This created a compounding problem: the company needed to generate returns for investors while routing money to nonprofits, without alienating donors who might object to a commercial intermediary taking a cut of their charitable contributions.

Charity platform fees are a known friction point. Donors who discover that a percentage of their donation goes to a platform rather than the cause often respond negatively — a dynamic that has driven platforms like GoFundMe to experiment with optional tipping models rather than mandatory fees. For GiveSpark, this tension was particularly acute because the platform's value proposition was built on the emotional resonance of celebrity-cause relationships. Any visible commercial layer risked undermining that emotional dynamic.

Without a clear revenue model, GiveSpark could not make a credible case to investors for follow-on funding. The YC seed round provided initial runway, but converting Demo Day attention into a Series A requires demonstrating not just that the product works, but that it can generate revenue. GiveSpark had neither a revenue model to demonstrate nor, apparently, the additional campaigns needed to show repeatable donation volume.

### Tertiary Cause: Solo Founder with Insufficient Runway to Iterate

YC's company listing records GiveSpark's team size as one.<sup><a href="https://www.ycombinator.com/companies/givespark">[6]</a></sup> Building a two-sided marketplace — one side requiring relationship-intensive celebrity acquisition, the other requiring consumer-facing product development — as a solo founder is an exceptionally difficult execution challenge.

Celebrity acquisition requires a different skill set than product development. It demands relationship management, negotiation, and the kind of social capital that is typically built over years in entertainment, sports, or media. A solo technical founder building a web product in Palo Alto is structurally disadvantaged in that effort. Without a co-founder or early hire with direct access to celebrity talent pipelines, GiveSpark's supply-side acquisition problem was compounded by a team composition problem.

The YC seed round — standard at the time at approximately $150,000 for the W12 batch — provided limited runway for a solo founder attempting to solve a relationship-intensive supply-side problem while simultaneously building and iterating on a consumer product. If the first celebrity campaign took significant time and relationship capital to arrange, the runway to arrange a second, third, and fourth campaign while also developing the product may simply have run out.

Teplow's decision to begin co-founding Good Today in August 2013 — less than 18 months after Demo Day — suggests he had concluded by mid-2013 that GiveSpark was not going to achieve the traction needed to raise follow-on funding.<sup><a href="https://www.crunchbase.com/person/joe-teplow">[11]</a></sup> The formal closure followed sometime before April 2014, when he co-founded Rebelmail.<sup><a href="https://www.crunchbase.com/person/joe-teplow">[11]</a></sup>

### Structural Observation: The Single Data Point Problem

GiveSpark's Demo Day pitch was built on a single campaign result. That result was compelling — $87,000 in two weeks is a meaningful sum for a pre-launch startup — but it was also a single data point from a single unnamed celebrity for a single cause. Investors evaluating GiveSpark after Demo Day had no basis for assessing whether the result was repeatable, scalable, or dependent on factors outside the platform's control.

The absence of a second campaign in the public record suggests that GiveSpark could not replicate the conditions that produced the first result quickly enough to maintain investor interest. In a market where follow-on funding decisions are made within months of Demo Day, the inability to show a second data point — even a smaller one — is often fatal.

<media-tweet url="https://x.com/joeteplow" author="@joeteplow" date="2009-04-01" text="founder @GoRebelMail (acquired by @Salesforce) do good with me @goodtoday @ycombinator alum"></media-tweet>

---

## Key Lessons

- **Two-sided marketplaces with high-friction supply sides require a dedicated acquisition strategy before launch, not after.** GiveSpark's supply side — celebrity participation — required relationship capital, legal infrastructure, and ongoing management that a solo technical founder could not build quickly enough with a single seed round. Platforms that depend on a scarce, high-value supply side (celebrities, top creators, licensed content) need a co-founder or early hire with direct access to that supply before the product is built, not after traction is demonstrated.

- **A single proof-of-concept campaign is not a repeatable business model.** The $87,000 bone marrow campaign was a strong signal, but it was also a single data point from an unidentified celebrity under unspecified conditions. The inability to replicate that result — or the failure to attempt replication quickly enough — meant GiveSpark could not build the evidence base needed for follow-on funding. Startups with marketplace models need to demonstrate repeatability, not just peak performance, before Demo Day.

- **For-profit structures in charitable contexts require explicit revenue model disclosure.** GiveSpark's for-profit designation was never accompanied by a public explanation of how the company would generate revenue without undermining donor trust. This ambiguity created a credibility gap with both investors (who needed a path to returns) and donors (who needed assurance their money was going to the cause). Platforms operating at the intersection of commerce and charity need to resolve this tension explicitly and early.

- **Founder trajectory can reveal what a failed company taught its builder.** Teplow's pivot from GiveSpark (celebrity-dependent, relationship-intensive, unclear revenue model) to Rebelmail (B2B, recurring revenue, no supply-side dependency) and then back to Good Today (recurring micro-donations, corporate CSR focus, structurally simpler than GiveSpark) suggests a deliberate evolution away from the failure modes of the first company.<sup><a href="https://techcrunch.com/2018/10/05/salesforce-acquires-rebel-maker-of-interactive-email-services-to-expand-its-marketing-cloud/">[12]</a></sup><sup><a href="https://techcrunch.com/2019/10/29/with-sean-rad-signed-on-as-co-founder-good-today-launches-new-tool-for-company-wide-donations/">[13]</a></sup> Good Today's model — small recurring donations, no celebrity dependency, corporate subscription revenue — addresses each of GiveSpark's structural weaknesses directly.

---

## Sources

1. [GiveSpark — Y Combinator Company Profile](https://www.ycombinator.com/companies/givespark)
2. [GiveSpark — Crunchbase Organization Profile](https://www.crunchbase.com/organization/givespark)
3. [Good Today Brings the Pushke to Corporate Social Responsibility — eJewishPhilanthropy (May 28, 2021)](https://ejewishphilanthropy.com/good-today-brings-the-pushke-to-corporate-social-responsibility/)
4. [YC Demo Day Session 1 — TechCrunch (March 27, 2012)](https://techcrunch.com/2012/03/27/yc-demo-day-session-1/)
5. [GiveSpark — VentureBeat Company Profile](https://venturebeat.com/company/givespark)
6. [Joe Teplow — Crunchbase Person Profile](https://www.crunchbase.com/person/joe-teplow)
7. [Salesforce Acquires Rebel — TechCrunch (October 5, 2018)](https://techcrunch.com/2018/10/05/salesforce-acquires-rebel-maker-of-interactive-email-services-to-expand-its-marketing-cloud/)
8. [With Sean Rad Signed On as Co-Founder, Good Today Launches New Tool for Company-Wide Donations — TechCrunch (October 29, 2019)](https://techcrunch.com/2019/10/29/with-sean-rad-signed-on-as-co-founder-good-today-launches-new-tool-for-company-wide-donations/)
9. [GiveSpark Twitter/X Account (@Givespark)](https://x.com/givespark)
10. [Joe Teplow Twitter/X Profile (@joeteplow)](https://x.com/joeteplow)
11. [This Orthodox Jew Made Daily Tzedaka Giving a Habit for Celebrities and Major Corporations — Jew in the City (July 2020)](https://jewinthecity.com/2020/07/this-orthodox-jew-made-daily-tzedaka-giving-a-habit-for-celebrities-and-major-corporations/)
12. [GiveSpark.com — Internet Archive Wayback Machine](https://web.archive.org/web/20120601000000*/givespark.com)
13. [Y Combinator Demo Day March 2012 Overview — VentureBeat](https://venturebeat.com/2012/03/27/y-combinator-demo-day-march-2012)
