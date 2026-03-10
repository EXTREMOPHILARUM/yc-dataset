# Research Report: Automate Ads

## Overview

Andrew Torba and Charles Szymanski were childhood best friends from Scranton, Pennsylvania. Torba had recently graduated from the University of Scranton; Szymanski was attending Drexel University when they co-founded the company in 2011.<sup><a href="https://technical.ly/startups/gab-andrew-torba-kuhcoon-startup/">[1]</a></sup> The two are also described as college roommates at the time of founding, though the exact living arrangement across two different universities is unclear.<sup><a href="https://en.wikipedia.org/wiki/Automate_Ads">[2]</a></sup>

The founding insight was practical. Torba later told Wishpond in a February 2015 podcast interview that he started Kuhcoon after finding it nearly impossible to manage a client's Facebook ad campaigns on mobile — the existing tools were desktop-bound, manual, and time-consuming.<sup><a href="https://wishpond.com/blog/kuhcoon-ceo-andrew-torba-tells-us-how-he-grew-his/">[3]</a></sup> The solution he envisioned was not a better dashboard but a system that would make decisions on behalf of the advertiser: pause underperforming ads, rotate creative variants, and allocate budget — all without human intervention.

The company operated for roughly three years before gaining significant outside validation. There is no public record of revenue, customers, or product milestones from 2011 to late 2014 — suggesting a long bootstrapped or pre-revenue period. In late 2014, Torba and Szymanski won a competition that resulted in Y Combinator accepting Kuhcoon into its Winter 2015 batch.<sup><a href="https://en.wikipedia.org/wiki/Andrew_Torba">[4]</a></sup> The acceptance prompted a move from Scranton to Palo Alto, which Torba marked with a Medium post on New Year's Eve 2014: "Scranton will always be our home, but Silicon Valley has always been our destiny."<sup><a href="https://www.mercurynews.com/2018/11/01/from-silicon-valley-elite-to-social-media-hate-the-radicalization-that-led-to-gab/amp/">[5]</a></sup>

That framing — Silicon Valley as destiny — would prove bitterly ironic. Within two years, Torba would describe his experience there as a disillusionment: "I became incredibly disillusioned after only one year living and working with some of the 'top names' and companies. These are not good people."<sup><a href="https://www.mercurynews.com/2018/11/01/from-silicon-valley-elite-to-social-media-hate-the-radicalization-that-led-to-gab/amp/">[6]</a></sup>

At YC, the team was described by Washington Post sources as "mild-mannered and largely unremarkable" — not top of the batch, but respected for their work ethic.<sup><a href="https://www.mercurynews.com/2018/11/01/from-silicon-valley-elite-to-social-media-hate-the-radicalization-that-led-to-gab/amp/">[7]</a></sup> Torba served as CEO and the public face of the company; Szymanski served as CTO and handled the technical architecture.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[8]</a></sup> The two-person founding team structure — with no other executives on record — would later prove to be a critical single point of failure.

---

## Founding Story

### Timeline

- **2011** — Andrew Torba and Charles Szymanski co-found Kuhcoon in Scranton, Pennsylvania. Torba is CEO; Szymanski is CTO.<sup>[[2]](https://en.wikipedia.org/wiki/Automate_Ads)</sup>

- **December 2014** — Y Combinator accepts Kuhcoon into its Winter 2015 batch. Torba publishes a Medium post announcing the move to Northern California: "Silicon Valley has always been our destiny."<sup>[[9]](https://en.wikipedia.org/wiki/Automate_Ads)</sup>

- **February 2015** — TechCrunch covers Kuhcoon during the YC W15 Demo Day period. The company claims 6,000 advertisers in 90+ countries. Torba states the grand plan is to "automate all of paid media spending on the Internet."<sup>[[10]](https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/)</sup>

- **June 25, 2015** — Company renames itself from Kuhcoon to Automate Ads.<sup>[[2]](https://en.wikipedia.org/wiki/Automate_Ads)</sup>

- **August 2015** — Per TheCompanyCheck (low confidence), company raises a $1M Seed round. Investors listed include Wefunder, AdHawk, Y Combinator, S2 Capital, and Tikhon Bernstam.<sup>[[11]](https://www.thecompanycheck.com/company/b/automate-ads/h0aro24os9z2j8390)</sup> Company also runs a Wefunder crowdfunding campaign.<sup>[[12]](https://wefunder.com/automateads)</sup>

- **September 2015** — Per TheCompanyCheck (low confidence), company raises a second Seed round of $118,600.<sup>[[11]](https://www.thecompanycheck.com/company/b/automate-ads/h0aro24os9z2j8390)</sup>

- **2015–2016** — Company develops Advertise.ai, an AI-powered chatbot for Facebook Messenger and Slack, and releases an Android mobile app for cross-channel campaign management.<sup>[[13]](https://media-index.kochava.com/ad_partners/kuhcoon)</sup>

- **August 2016** — Andrew Torba steps down as CEO of Automate Ads. That same month, Torba co-founds Gab with former Automate Ads employee Ekrem Büyükkaya.<sup>[[2]](https://en.wikipedia.org/wiki/Automate_Ads)</sup>

- **November 2016** — Torba is expelled from Y Combinator's alumni network for violating its harassment policy, following clashes with other YC founders on Facebook after the 2016 U.S. presidential election. A YC partner confirms he was removed "for speaking in a threatening, harassing way toward other YC founders."<sup>[[14]](https://techcrunch.com/2016/11/12/pro-trump-ceo-gets-booted-from-y-combinator/)</sup>

- **October 18, 2017** — AdHawk acquires Automate Ads for an undisclosed amount. AdHawk CEO Todd Saunders confirms the company had "basically shut down" prior to the acquisition. No team members join AdHawk; only CTO Szymanski consults briefly during the transition.<sup>[[15]](https://techcrunch.com/2017/10/18/adhawk-acquires-automate-ads/)</sup>

---

## What They Built

Kuhcoon — later Automate Ads — built a software platform that managed Facebook advertising campaigns on behalf of small and medium-sized businesses, removing the need for human day-to-day campaign management.

**The core problem it solved.** Running Facebook ads effectively in 2014–2015 required constant manual attention: testing multiple ad creatives, pausing underperformers, reallocating budget, and interpreting results. Tools like AdEspresso could surface insights and make recommendations, but the advertiser still had to act on them. Kuhcoon's pitch was that it would act for you.

**How it worked.** The user provided three inputs: a budget, a creative or conversion goal, and a target demographic. The platform then handled everything else. Its key technical differentiator was running one ad at a time per audience segment and rotating between creative variants, rather than uploading all ads simultaneously. CTO Szymanski explained the logic: "you're actually competing with Facebook's own optimization algorithms" when you upload multiple ads in one campaign, because Facebook's system distributes spend unevenly across variants before meaningful data accumulates.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup> By running one ad at a time, Kuhcoon gathered clean performance data on each variant before rotating to the next.

Torba described the competitive distinction plainly: "What AdEspresso does, they'll say, 'This ad isn't performing well, you should pause it.' We're actually going to pause it for you."<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup>

**Target segment.** The product focused on advertisers spending between $20,000 and $1 million per month on Facebook, with particular emphasis on those spending under $100,000.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup> Enterprise competitors like Nanigans and Kenshoo served large brands with dedicated account teams; Szymanski identified this as a deliberate gap: "competitors offering 'full automation,' like Nanigans and Kenshoo, were focused on huge advertisers."<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup>

**Product evolution.** The initial product was Facebook-only. By mid-2015, the company had rebranded to Automate Ads and announced plans to expand to Google AdWords, Twitter, and Pinterest — though there is no confirmed evidence these integrations were ever fully shipped. The company later developed Advertise.ai, an AI-powered chatbot assistant for Facebook Messenger and Slack that tracked and reported on advertising performance across Facebook, Instagram, Google AdWords, and Twitter.<sup><a href="https://media-index.kochava.com/ad_partners/kuhcoon">[13]</a></sup> An Android mobile app for cross-channel campaign management was also released.<sup><a href="https://www.similarplay.com/kuhcoon_inc/automate_ads/apps/com.kuhcoon.automateads">[16]</a></sup>

The pivot to a chatbot interface in 2016 was consistent with broader industry trends — Facebook had just opened Messenger to third-party bots in April 2016 — but there is no public data on whether Advertise.ai attracted meaningful adoption. The company was building in multiple directions simultaneously (core platform, chatbot, mobile app, multi-channel expansion) without confirmed success in any of them beyond the original Facebook product.

When AdHawk acquired the company in October 2017, it specifically cited Automate Ads' campaign creation tools as complementary to AdHawk's optimization focus — confirming that the underlying technology retained value even as the business had collapsed.<sup><a href="https://techcrunch.com/2017/10/18/adhawk-acquires-automate-ads/">[15]</a></sup>

---

## Market Position

### Target Customers

Automate Ads targeted SMBs spending $20,000 to $1 million per month on Facebook advertising, with the sweet spot below $100,000 per month.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup> These were businesses large enough to have meaningful ad budgets but too small to justify the account minimums or contract sizes required by enterprise platforms. In practice, this meant e-commerce companies, local service businesses, and direct-response advertisers who were managing Facebook campaigns themselves or through small agencies.

The customer profile was defined by a specific pain point: these advertisers had enough budget to benefit from optimization but lacked the in-house expertise or time to manage campaigns at the granularity that performance required. The product's promise — give us three data points and we handle the rest — was designed to match exactly this profile.

### Market Size

The Facebook advertising market was growing rapidly during the company's active years. Facebook reported $3.59 billion in advertising revenue in Q4 2014 and $4.3 billion in Q1 2015, with the majority coming from mobile.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup> The SMB segment was a stated priority for Facebook itself, which had been actively courting small businesses onto its ad platform since 2012.

The broader ad-tech software market — tools that help advertisers manage, optimize, and automate campaigns — was estimated in the billions globally by 2015, though the specific SMB Facebook automation niche was a fraction of that. Torba's stated ambition was to expand beyond Facebook to "automate all of paid media spending on the Internet,"<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup> which would have placed the company in a much larger addressable market — but that expansion never materialized.

### Competition

The competitive landscape in 2015 split into three tiers.

**Enterprise platforms** — Nanigans, Kenshoo, and Marin Software — served large brands and agencies with dedicated account management, high contract minimums, and deep integrations. These were not competing for Automate Ads' target customer.

**SMB-focused tools** — AdEspresso (acquired by Hootsuite in 2017) was the most direct competitor. AdEspresso offered A/B testing, analytics, and campaign management for Facebook ads, but its model was advisory: it surfaced recommendations and left execution to the user. Automate Ads' differentiation was full automation rather than assisted management.

**Facebook itself** — This was the most dangerous competitive force, and the one the founders explicitly acknowledged. Facebook's own Power Editor and Ads Manager were continuously improving, and Facebook had a structural incentive to make advertising as easy as possible for SMBs to increase spend. Szymanski's insight about competing with Facebook's optimization algorithms was astute in 2015, but it also identified the core fragility: any improvement Facebook made to its own ad delivery system narrowed the gap that Automate Ads was exploiting. By 2016–2017, Facebook had introduced automated bidding strategies, campaign budget optimization, and dynamic creative tools that replicated much of what Automate Ads had built.

---

## Business Model

Automate Ads operated as a SaaS platform, charging advertisers a subscription fee or percentage of managed ad spend to automate their Facebook campaigns. The specific pricing structure is not publicly documented.

The Wefunder crowdfunding campaign described the company as a "Fully Automated, Performance-Driven Ad Platform" and cited customers managing $50,000 in ads per week — suggesting the company was taking a cut of managed spend or charging based on spend volume, which is the standard model for ad-tech platforms serving SMBs.<sup><a href="https://wefunder.com/automateads">[12]</a></sup>

The business model had an inherent tension: the company's value proposition was saving advertisers money (claiming 40% ad spend savings and 31% cheaper conversions on average),<sup><a href="https://media-index.kochava.com/ad_partners/kuhcoon">[17]</a></sup> but if the platform charged a percentage of managed spend, reducing spend would reduce revenue. Whether the company resolved this tension through flat-rate subscription pricing or a hybrid model is unknown. No revenue figures were ever publicly disclosed.

---

## Traction

At the time of YC Demo Day in February 2015, Automate Ads claimed 6,000 advertisers across more than 90 countries.<sup><a href="https://en.wikipedia.org/wiki/Automate_Ads">[2]</a></sup> This figure has not been independently verified, and no revenue or MRR data was disclosed alongside it.

The company's self-reported performance metrics were aggressive. Kuhcoon claimed it saved advertisers 40% of their spending and more than 20 hours per week on average.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[10]</a></sup> The Wefunder campaign cited 145% ROI versus manually managed campaigns and 46% week-over-week customer growth, with 1,800 customers since launch and $50,000 in ads managed per week.<sup><a href="https://wefunder.com/automateads">[12]</a></sup> A separate source cited 31% cheaper conversions than human-managed campaigns on average.<sup><a href="https://media-index.kochava.com/ad_partners/kuhcoon">[17]</a></sup>

The discrepancy between the 6,000 advertiser figure cited in February 2015 and the 1,800 customers since launch figure on the Wefunder page (timing unclear) is notable and unresolved. It is possible the 6,000 figure included free or trial users while 1,800 represented paying customers, or the figures reflect different time periods.

Washington Post sources described the team as not in the top of the YC W15 batch but respected for hard work — suggesting the company was performing adequately but not breaking out within the cohort.<sup><a href="https://www.mercurynews.com/2018/11/01/from-silicon-valley-elite-to-social-media-hate-the-radicalization-that-led-to-gab/amp/">[7]</a></sup> No follow-on growth metrics, retention data, or revenue figures were ever published after the February 2015 press cycle.

---

## Post-Mortem

Automate Ads collapsed for one proximate reason and several structural ones. The proximate cause was founder abandonment. The structural causes — thin capitalization, single-platform dependency, and an eroding product moat — made the company too fragile to survive it.

### Primary Cause: CEO Departure and Ideological Disillusionment

In August 2016, Andrew Torba stepped down as CEO of Automate Ads.<sup><a href="https://en.wikipedia.org/wiki/Automate_Ads">[2]</a></sup> That same month, he co-founded Gab — a social network explicitly positioned as a free-speech alternative to Twitter — with Ekrem Büyükkaya, who had also worked at Automate Ads.<sup><a href="https://en.wikipedia.org/wiki/Automate_Ads">[2]</a></sup> The simultaneity of the departure and the new founding makes clear that Torba's attention had fully shifted before he formally left.

Torba's stated reason was ideological alienation from Silicon Valley culture. He later described his experience: "I became incredibly disillusioned after only one year living and working with some of the 'top names' and companies. These are not good people."<sup><a href="https://www.mercurynews.com/2018/11/01/from-silicon-valley-hate-the-radicalization-that-led-to-gab/amp/">[6]</a></sup> This was not a strategic handoff to a successor CEO or a planned transition. There is no public record of anyone taking over the CEO role after Torba's departure, and no account from CTO Szymanski about what happened to the company in the 14 months between Torba's exit and the AdHawk acquisition.

The consequences compounded in November 2016, when Torba was expelled from Y Combinator's alumni network for violating its harassment policy. A YC partner confirmed he was removed "for speaking in a threatening, harassing way toward other YC founders" following clashes on Facebook after the 2016 U.S. presidential election.<sup><a href="https://techcrunch.com/2016/11/12/pro-trump-ceo-gets-booted-from-y-combinator/">[14]</a></sup> The expulsion eliminated the company's most valuable institutional asset — YC network access, investor relationships, and the credibility that comes with active YC alumni status — at the moment the company most needed support.

By October 2017, when AdHawk acquired the company, CEO Todd Saunders confirmed that Automate Ads had "basically shut down" prior to the acquisition.<sup><a href="https://techcrunch.com/2017/10/18/adhawk-acquires-automate-ads/">[15]</a></sup> No team members joined AdHawk. Only Szymanski consulted briefly during the technology transition.<sup><a href="https://techcrunch.com/2017/10/18/adhawk-acquires-automate-ads/">[15]</a></sup> This was not an acqui-hire — it was a technology salvage operation.

### Structural Vulnerability: Thin Capitalization

The company's funding history is contested, but even the most generous interpretation leaves it severely undercapitalized. CBInsights reports total funding of $120,000.<sup><a href="https://www.cbinsights.com/company/kuhcoon">[18]</a></sup> TheCompanyCheck reports $1.12 million across two 2015 rounds.<sup><a href="https://www.thecompanycheck.com/company/b/automate-ads/h0aro24os9z2j8390">[11]</a></sup> The true figure is unknown, but even $1.12 million is extremely thin runway for an ad-tech platform attempting multi-channel expansion, product development across three surfaces (web, mobile, chatbot), and customer acquisition across 90 countries.

The Wefunder crowdfunding campaign — which raised from retail investors rather than institutional VCs — is a signal that the company struggled to raise traditional follow-on funding after YC.<sup><a href="https://wefunder.com/automateads">[12]</a></sup> The YC standard deal at the time provided $120,000 in exchange for 7% equity. If CBInsights' figure is accurate, the company never raised beyond the YC check. A company attempting to build a multi-platform ad automation product on $120,000 in total capital had essentially no margin for error on execution, hiring, or founder stability.

### Structural Vulnerability: Single-Platform Dependency

Automate Ads' entire business was built on top of Facebook's advertising API. This created two compounding risks.

First, Facebook controlled the rules. Any change to Facebook's ad delivery system, API terms, or algorithm could directly impair the product. The company's core technical insight — running one ad at a time per segment to avoid competing with Facebook's optimization — was a workaround for a platform behavior that Facebook could change at any time.

Second, Facebook was the most motivated competitor. Facebook had a direct financial incentive to make advertising easy for SMBs, and it had the resources to build features that replicated third-party tools. Between 2015 and 2017, Facebook introduced campaign budget optimization, automated bidding, dynamic creative optimization, and improved audience targeting — each of which narrowed the gap that Automate Ads was exploiting. The company's planned expansion to Google AdWords, Twitter, and Pinterest was announced in February 2015 but never confirmed as shipped, leaving the business entirely dependent on a single platform whose own product roadmap was its primary competitive threat.

### Structural Vulnerability: Unproven Product-Market Fit Beyond Early Adopters

The 6,000 advertiser figure from February 2015 was the company's peak public traction claim.<sup><a href="https://en.wikipedia.org/wiki/Automate_Ads">[2]</a></sup> No subsequent growth metrics were ever published. The Wefunder campaign cited 1,800 customers since launch — a figure that, depending on timing, may represent a smaller paying customer base beneath the broader user count. The company never disclosed revenue, retention rates, or customer lifetime value.

The pivot to Advertise.ai (a chatbot) and the Android mobile app, without confirmed success on the core Facebook product, suggests the team may have been responding to stalling growth by chasing adjacent opportunities rather than deepening the core product's moat. Building three products simultaneously on thin capital is a pattern associated with teams that have lost conviction in their primary thesis.

### Compounding Factor: Two-Person Team with No Succession Depth

The company's entire executive structure consisted of two people: Torba as CEO and Szymanski as CTO.<sup><a href="https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/">[8]</a></sup> YC's company directory lists the team size as two.<sup><a href="https://www.ycombinator.com/companies/automate-ads">[19]</a></sup> When Torba left, there was no sales leader, no head of product, no COO, and no investor board with the leverage or interest to recruit a replacement CEO. Szymanski, as CTO, was not positioned to run the business side. The company had no organizational resilience to absorb the loss of its only business-side founder.

The technology-only nature of the AdHawk acquisition is the clearest evidence of what survived and what did not. AdHawk acquired Automate Ads because its campaign creation tools complemented AdHawk's optimization focus — the underlying code had genuine value.<sup><a href="https://techcrunch.com/2017/10/18/adhawk-acquires-automate-ads/">[15]</a></sup> The business, the customer relationships, the team, and the brand did not survive. The product outlasted the company.

---

## Key Lessons

- **Founder commitment is a structural asset, not a given.** Automate Ads had a technically sound product and early traction, but the entire business-side of the company resided in one person. When Torba's ideological disillusionment with Silicon Valley reached a breaking point in August 2016, there was no succession plan, no co-CEO, and no investor board with the leverage to intervene. A two-person founding team where one founder holds all external relationships and the other holds all technical knowledge creates a single point of failure that no amount of product quality can compensate for.

- **Building on a single platform is a bet on that platform's strategic interests remaining aligned with yours.** Automate Ads' core differentiation was a workaround for Facebook's ad delivery behavior — a behavior Facebook had every incentive to improve away. The company announced multi-platform expansion in February 2015 but never confirmed shipping it. Staying Facebook-only meant the company's moat was eroding from the moment Facebook's own product team started building automated bidding and dynamic creative tools. Platform dependency is survivable when the platform has no incentive to compete with you; it is fatal when the platform is your most motivated competitor.

- **Crowdfunding as a fundraising signal.** The Wefunder campaign, combined with the conflicting funding data and the absence of any confirmed institutional follow-on round after YC, suggests the company struggled to raise from professional investors after Demo Day. When a YC company turns to retail crowdfunding rather than closing a seed round from institutional investors, it typically indicates that the company's growth metrics did not meet the threshold required for a conventional raise. Thin capital constrained every subsequent decision — hiring, product development, and the ability to weather a founder departure.

- **Product pivots without confirmed core traction are a warning sign, not a strategy.** The expansion from Facebook automation to a Messenger/Slack chatbot (Advertise.ai) and an Android mobile app, without any published evidence that the core product had achieved sustainable growth, suggests the team was building in multiple directions simultaneously. Diversifying the product surface area on limited capital, before the primary product has demonstrated durable retention and revenue, typically accelerates cash burn without proportionally increasing the probability of finding product-market fit.

- **Institutional relationships are fragile and non-recoverable once broken.** Torba's expulsion from the YC alumni network in November 2016 — three months after he had already left Automate Ads — eliminated the company's most valuable remaining asset at the worst possible time. YC alumni network access provides warm introductions to investors, potential acquirers, and talent. Losing it while the company was already in distress removed the last institutional backstop that might have enabled a recovery or a better-structured acquisition.

---

## Sources

1. [Technical.ly — Gab, Andrew Torba, Kuhcoon startup (January 2021)](https://technical.ly/startups/gab-andrew-torba-kuhcoon-startup/)
2. [Wikipedia — Automate Ads](https://en.wikipedia.org/wiki/Automate_Ads)
3. [Wishpond — Podcast interview with Andrew Torba, CEO of Kuhcoon (February 2015)](https://wishpond.com/blog/kuhcoon-ceo-andrew-torba-tells-us-how-he-grew-his/)
4. [Wikipedia — Andrew Torba](https://en.wikipedia.org/wiki/Andrew_Torba)
5. [Mercury News — From Silicon Valley elite to social media hate: The radicalization that led to Gab (November 2018)](https://www.mercurynews.com/2018/11/01/from-silicon-valley-elite-to-social-media-hate-the-radicalization-that-led-to-gab/amp/)
6. [TechCrunch — YC-Backed Kuhcoon Promises To Automate Facebook Ad Campaigns For Small Businesses (February 2015)](https://techcrunch.com/2015/02/19/yc-backed-kuhcoon-promises-to-automate-facebook-ad-campaigns-for-small-businesses/)
7. [TechCrunch — Pro-Trump CEO gets booted from Y Combinator (November 2016)](https://techcrunch.com/2016/11/12/pro-trump-ceo-gets-booted-from-y-combinator/)
8. [TechCrunch — AdHawk acquires Automate Ads to improve Google and Facebook ad campaigns (October 2017)](https://techcrunch.com/2017/10/18/adhawk-acquires-automate-ads/)
9. [CBInsights — Kuhcoon / Automate Ads company profile](https://www.cbinsights.com/company/kuhcoon)
10. [TheCompanyCheck — Automate Ads company profile](https://www.thecompanycheck.com/company/b/automate-ads/h0aro24os9z2j8390)
11. [Wefunder — Automate Ads crowdfunding campaign](https://wefunder.com/automateads)
12. [Kochava Media Index — Kuhcoon ad partner profile](https://media-index.kochava.com/ad_partners/kuhcoon)
13. [SimilarPlay — Automate Ads Android app profile](https://www.similarplay.com/kuhcoon_inc/automate_ads/apps/com.kuhcoon.automateads)
14. [Y Combinator — Automate Ads company directory](https://www.ycombinator.com/companies/automate-ads)
15. [YCDB — Automate Ads company listing](https://www.ycdb.co/company/automate-ads)
16. [Crunchbase — Kuhcoon organization profile](https://www.crunchbase.com/organization/kuhcoon-ba0b)
17. [Crunchbase — Broadlume acquires Kuhcoon acquisition record](https://www.crunchbase.com/acquisition/broadlume-acquires-kuhcoon--c2d37972)
18. [Product Hunt — Kuhcoon iOS app launch page](https://www.producthunt.com/posts/kuhcoon-1)
19. [Owler — Kuhcoon company profile](https://www.owler.com/company/kuhcoon)
20. [Twitter/X — @AutomateAds official profile](https://x.com/automateads)
21. [YC Blog — Kuhcoon (YC W15) blog post](https://www.ycombinator.com/blog/kuhcoon-yc-w15-promises-to-automate-facebook-ad-campaigns-for-small-businesses/)
