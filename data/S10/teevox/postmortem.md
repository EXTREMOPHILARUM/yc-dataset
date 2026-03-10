# Research Report: Teevox

## Overview

Teevox was a Y Combinator-backed startup (Summer 2010) that began as a hardware-free iPhone remote for Hulu and Netflix, then pivoted into a multi-stream eSports viewing platform built on top of Twitch.Founded by two MIT graduates, Jong-Moon Kim and Andrew Sugaya, the company reached 700,000 monthly users at its peak before shutting down in 2012.

The core thesis of failure is one of timing: Teevox built a technically sophisticated product for an audience that was real but too small to sustain a business.Copycat competitors fragmented an already thin user base, the company had no monetization strategy, and the $20,000 YC seed round provided no meaningful runway. The eSports viewing market that would have validated Teevox's thesis — growing from roughly 15 million to over 200 million monthly viewers — did not materialize until 2015–2016, three years after the company closed. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[1]</a></sup>

## Founding Story

Teevox was founded in 2010 by Jong-Moon Kim (known online as "Jiggity") and Andrew Sugaya, both former MIT students. <sup><a href="https://techcrunch.com/2010/08/19/teevox/">[2]</a></sup> Sugaya graduated at the top of his class. <sup><a href="https://usa2018.augmentedworldexpo.com/speakers/andrew-sugaya/">[3]</a></sup> The company was headquartered in Cupertino, California, placing it squarely inside the consumer tech ecosystem that defined the early smartphone era. <sup><a href="https://www.ycombinator.com/companies/teevox">[4]</a></sup>

The founding insight was straightforward and grounded in a real product gap. In 2010, the market for iPhone remote control apps was crowded, but Kim observed that every existing solution required either proprietary hardware — an Apple TV, a Boxee box — or a separate software installation on the target computer. His pitch was that Teevox required neither. As Kim put it at the time: "While there are hundreds, if not thousands of iPhone remote apps. If you take a closer look, you'll notice they all require proprietary hardware (Apple TV, Boxee) or separate software you need to download and install." <sup><a href="https://techcrunch.com/2010/08/19/teevox/">[5]</a></sup> The product, teevoxRemote, let a user control Hulu and Netflix from their iPhone without touching anything else.

The team was accepted into Y Combinator's Summer 2010 cohort — one of 36 companies in what TechCrunch described as YC's biggest Demo Day yet. <sup><a href="https://readwrite.com/2010/08/24/ycombinator-demoday">[6]</a></sup> YC provided early validation, network access, and a seed check of approximately $20,000, with angel investor David Nakayama also participating. <sup><a href="https://www.cbinsights.com/company/teevox">[7]</a></sup>

<media-image src="https://techcrunch.com/wp-content/uploads/2010/08/teevox.png" alt="Teevox iPhone remote app interface showing Hulu and Netflix control screen" caption="TechCrunch's August 2010 coverage of Teevox — the YC S10 startup that turned an iPhone into a remote control for Hulu and Netflix without requiring any additional hardware or software."></media-image>

The original product did not survive long enough to become the company's defining identity. At some point in 2011, Kim made a pivot that would reshape Teevox entirely. He was a StarCraft player and fan of competitive gaming, and he noticed that watching multiple eSports livestreams simultaneously on Twitch was technically impossible with existing tools. He built a multi-stream viewer, initially naming it after a StarCraft unit called the Warp Prism, then rebranded it as Teevox to generalize the product across other games. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[8]</a></sup>

The pivot was organic rather than strategic — a founder scratching his own itch — and it would define both the company's peak and its eventual collapse.

---

## Timeline

- **2010** — Teevox founded by Jong-Moon Kim and Andrew Sugaya; headquartered in Cupertino, CA. <sup>[[4]](https://www.ycombinator.com/companies/teevox)</sup>
- **August 2010** — Teevox accepted into Y Combinator Summer 2010 cohort; raises approximately $20,000 seed round from YC and David Nakayama. <sup>[[7]](https://www.cbinsights.com/company/teevox)</sup>
- **August 19, 2010** — TechCrunch publishes launch coverage of teevoxRemote, the iPhone/iPod Touch app for controlling Hulu and Netflix without proprietary hardware. <sup>[[5]](https://techcrunch.com/2010/08/19/teevox/)</sup>
- **August 24, 2010** — Teevox presents at YC Demo Day; True Ventures notes the company as an innovative use of tablets. <sup>[[9]](https://trueventures.com/blog/thoughts-on-y-combinator-demo-day)</sup>

<media-hn url="https://news.ycombinator.com/item?id=4343685" title="Watch 3 concurrent streams of the Curiosity landing with HN/Reddit Chat" points="" comments=""></media-hn>

- **2011** — Teevox pivots to eSports multi-stream viewing platform; product launches on Twitch and hits the front page of Reddit. <sup>[[8]](https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/)</sup>
- **Summer 2011** — Teevox grows substantially during StarCraft tournament season, reaching a peak of 700,000 monthly users. <sup>[[10]](https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/)</sup>
- **August 2012** — Jong-Moon Kim posts to Hacker News promoting Teevox's multi-stream viewer for the Mars Curiosity landing, showing the product's expanded use case beyond gaming.
- **2012** — After seven months of stagnation, Teevox is shut down. Twitch attempts to hire Kim around the same time. <sup>[[11]](https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/)</sup>
- **January 2016** — Kim posts a Show HN announcing the rebuilt Teevox, constructed with React and Firebase.
- **February 5, 2016** — AList Daily publishes an interview with Kim about the resurrection of Teevox, citing eSports audience growth from 15 million to over 200 million monthly viewers since 2011. <sup>[[1]](https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/)</sup>

---

## What They Built

### Version 1: teevoxRemote (2010)

The original Teevox product was an iPhone and iPod Touch application that turned a smartphone into a remote control for streaming video on a computer. The core use case was simple: a user sitting on their couch could browse and control Hulu or Netflix on their laptop or desktop without getting up or using a keyboard and mouse. <sup><a href="https://www.ycombinator.com/companies/teevox">[12]</a></sup>

The app included one-touch show selection, play/pause/volume controls, synchronized shared viewing with a friend, and Twitter and Facebook integration. <sup><a href="https://www.crunchbase.com/organization/teevox">[13]</a></sup> Planned expansions included iPad support and iTunes store integration. <sup><a href="https://techcrunch.com/2010/08/19/teevox/">[14]</a></sup>

The differentiating claim was the absence of required hardware or software. Competing remote apps in 2010 all required either a dedicated device (Apple TV, Boxee) or a companion program installed on the target computer. Teevox required neither. Whether this technical claim held up under scrutiny is unclear from available records, but it was the central pitch at YC Demo Day.

### Version 2: eSports Multi-Stream Viewer (2011–2012)

The pivot product was a web-based platform that allowed users to watch multiple Twitch livestreams simultaneously in a single browser window. This was technically non-trivial. Twitch's native interface supported only one stream at a time. Teevox built a custom player that could load and display multiple streams side by side, with the user controlling which audio feed was active.

The technical innovations Kim later identified as distinguishing Teevox from competitors were stream preloading — loading a stream in the background before the user switched to it, eliminating buffering delays — and variable bitrate control, which dynamically adjusted stream quality based on available bandwidth across multiple concurrent feeds. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[15]</a></sup> These were meaningful engineering achievements for 2011, when browser-based video was still technically constrained.

The product also released an Android app, suggesting the team was investing in mobile access to the multi-stream experience. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[16]</a></sup>

The initial focus was StarCraft II, which had a structured tournament calendar with multiple simultaneous matches. The product name "Warp Prism" — a StarCraft unit — reflected this origin. Kim later renamed it Teevox to signal that the platform could serve any game with concurrent streams. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[8]</a></sup>

<media-image src="https://web.archive.org/web/20120806000000im_/http://teevox.com/" alt="Archived Teevox homepage circa August 2012 showing the multistream eSports viewer interface" caption="Archived snapshot of teevox.com from around August 2012 — the period when Jong-Moon Kim posted to HN about watching 3 concurrent streams of the Curiosity Mars landing, and when Teevox was at its peak with 700,000 monthly users."></media-image>

### Version 3: The 2016 Rebuild

After the 2012 shutdown, Kim rebuilt Teevox in 2016 using React for the front end and Firebase for the backend — a modern static web architecture that would have been unavailable or impractical in 2012. He described the result as "sleeker, faster, and more powerful than I could've imagined possible in 2012." <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[17]</a></sup> The rebuilt product integrated directly with Twitch's follow graph, allowing users to load their personal list of followed streamers and watch them simultaneously.

<media-hn url="https://news.ycombinator.com/item?id=10940507" title="Show HN: Teevox – Twitch Multistream Player, made in Static HTML, React, Firebase" points="" comments=""></media-hn>

<media-tweet url="https://twitter.com/teevox" author="@teevox" date="2016-01-01" text="BIG update #2. You now load your Twitch stream follows! https://teevox.com pic.twitter.com/cg58kAqDlh"></media-tweet>

---

## Market Position

### Target Customers

Teevox's original target customer was a mainstream consumer who watched streaming video on a laptop or desktop and wanted a more comfortable couch-based experience. This was a broad market in 2010, but it was also a market that Apple, Roku, and Google were actively competing for with dedicated hardware products.

After the pivot, the target customer narrowed sharply to eSports viewers — specifically, fans of competitive StarCraft II and other games who watched multiple simultaneous tournament streams on Twitch. This was a highly engaged but numerically small audience. The eSports viewer base in 2011 was approximately 15 million monthly viewers globally. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[1]</a></sup> Within that group, the subset who wanted to watch multiple streams at once — rather than following a single match — was smaller still.

### Market Size

The total addressable market for eSports viewing in 2011–2012 was real but thin. Kim's own framing in 2016 captures the problem precisely: the audience had grown from 15 million to over 200 million monthly viewers between 2011 and 2016. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[1]</a></sup> That is a 13x increase in roughly five years. Teevox was operating at the low end of that curve, before the inflection point.

The broader streaming video market in 2010 was large and growing. Netflix had approximately 20 million subscribers in the United States by the end of 2010. Hulu had tens of millions of monthly unique visitors. But Teevox's original product — a remote control app — was a thin layer on top of these platforms, not a destination in itself. It captured no direct share of the streaming market's value.

### Competition

In the iPhone remote app market (2010), Teevox competed against a crowded field of apps, most of which required additional hardware or software. Kim's pitch was that Teevox was the only no-friction option. Whether this moat was defensible was never tested, because the company pivoted before the original product matured.

In the eSports multi-stream market (2011–2012), Teevox was an early mover but not a permanent one. Kim described the competitive landscape at shutdown: "The scene had become very crowded since Teevox's first release. A number of other organizations had launched Teevox-like products under their own brands and we were all competing for a fraction of the tiny viewership back then." <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[18]</a></sup>

The most significant structural competitor was Twitch itself. Twitch was also a YC company, and it was building the infrastructure layer — the streaming platform — that Teevox depended on entirely. Twitch had both the incentive and the capability to build multi-stream features natively, which would have eliminated Teevox's reason to exist regardless of market size. Twitch's eventual acquisition by Amazon in 2014 for $970 million confirmed that the infrastructure layer, not the viewing experience layer, captured the majority of value in the eSports streaming ecosystem.

---

## Business Model

Teevox had no documented revenue model at any stage of its existence. The original teevoxRemote app may have been a paid download or freemium product, but no pricing data is available in the public record. The eSports multi-stream platform appears to have been entirely free to users. Kim's 2016 post-mortem described "hemorrhaging money for an extended period" with no path to self-sustainability, which implies the company was spending on infrastructure costs — primarily bandwidth and server costs for multi-stream delivery — with no offsetting revenue. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[19]</a></sup>

The $20,000 YC seed round was the only external capital the company raised. <sup><a href="https://www.cbinsights.com/company/teevox">[7]</a></sup> No Series A or follow-on angel round is documented. For a product serving 700,000 monthly users with real bandwidth costs and no revenue, the financial math was unsustainable from the start. The company appears to have operated on founder savings or minimal personal income for the duration of its life.

---2e:T7a1,

## Traction

Teevox's traction story is one of the more striking in the YC S10 cohort — genuine user growth with no corresponding business model to capture its value.

At YC Demo Day in August 2010, the original teevoxRemote product reported 1,200 users in its first 24 hours after launch. <sup><a href="https://techcrunch.com/2010/08/24/y-combinator-demo-day-2/">[20]</a></sup> True Ventures specifically called out Teevox as an example of innovative tablet use cases. <sup><a href="https://trueventures.com/blog/thoughts-on-y-combinator-demo-day">[9]</a></sup> This early investor attention did not translate into follow-on funding.

The eSports pivot produced substantially stronger organic traction. The product hit the front page of Reddit upon launch — a signal of genuine product-market fit with the gaming community, not a paid acquisition event. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[21]</a></sup>

At its peak, Teevox reached 700,000 monthly users. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[10]</a></sup> For a two-person team with no marketing budget, this was a meaningful number. However, growth was seasonal and event-driven. The product spiked during summer StarCraft tournament seasons, when multiple matches ran concurrently and the multi-stream use case was most compelling. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[22]</a></sup> Outside of tournament windows, usage dropped. No daily active user figures, retention rates, or engagement depth metrics are available in the public record.

The seasonality pattern was a structural warning sign. A product whose usage is tied to a tournament calendar rather than daily habit is vulnerable to off-season churn and cannot demonstrate the consistent engagement metrics that investors require for a Series A.

---

## Post-Mortem

Teevox's failure was not a single event but a compounding sequence of structural problems, each of which might have been survivable in isolation. Together, they were fatal.

### Primary Cause: A Market That Was Real But Too Small

The eSports viewing audience in 2011–2012 was genuine but numerically insufficient to support a standalone business. Kim's own retrospective framing is the clearest statement of this problem: the global eSports audience grew from approximately 15 million monthly viewers in 2011 to over 200 million by 2016. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[1]</a></sup> Teevox was operating at the beginning of that growth curve, before the inflection point that would have made the market commercially viable.

Within that 15 million viewer base, Teevox's addressable segment was smaller still: viewers who specifically wanted to watch multiple streams simultaneously, who were technically capable of using a web-based multi-stream tool, and who were watching games with concurrent tournament matches. Reaching 700,000 monthly users from this subset was a genuine achievement. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[10]</a></sup> But 700,000 free users with no monetization path and real bandwidth costs is not a business — it is an expensive hobby.

The team's attempted remedy was to launch additional product lines and pursue partnerships to increase viewership. Kim described this directly: "I had tried to launch other product lines and created partnerships to increase viewership, but it was coming up short." <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[23]</a></sup> No details on what those product lines or partnerships were are available in the public record. What is clear is that they failed to move the needle before the company ran out of money.

### Secondary Cause: Copycat Proliferation Fragmented an Already Thin Audience

Teevox's technical innovations — stream preloading, variable bitrate control — were real but not patented or otherwise defensible. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[15]</a></sup> Once the product demonstrated that multi-stream eSports viewing was a viable use case (validated by the Reddit front page moment and 700,000 monthly users), other organizations built similar tools under their own brand names.

Kim described the result: "The scene had become very crowded since Teevox's first release. A number of other organizations had launched Teevox-like products under their own brands and we were all competing for a fraction of the tiny viewership back then." <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[18]</a></sup> The compounding problem was that some of these competitors were established gaming media brands with existing audiences, distribution channels, and revenue from other products. They could afford to offer a multi-stream viewer as a free feature. Teevox could not.

The team's response was to wait — seven months of stagnation elapsed between the growth plateau and the shutdown decision. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[11]</a></sup> This suggests Kim was hoping the market would grow fast enough to re-accelerate Teevox's user base. It did not grow fast enough within the available runway.

### Tertiary Cause: No Monetization Strategy and Insufficient Capital

Teevox raised $20,000 from YC and David Nakayama. <sup><a href="https://www.cbinsights.com/company/teevox">[7]</a></sup> No follow-on funding was raised at any stage. For a product serving hundreds of thousands of monthly users with real infrastructure costs — bandwidth, servers, CDN fees for multi-stream video delivery — this was an untenable financial position.

The absence of a revenue model compounded the capital problem. A product with 700,000 monthly users and even a modest $1/month subscription tier would have generated $700,000 in monthly recurring revenue — enough to sustain operations and potentially attract Series A interest. But Teevox was entirely free. Kim's post-mortem language is unambiguous: "After hemorrhaging money for an extended period of time, I felt the future looked bleak for Teevox to ever become something self-sustainable." <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[19]</a></sup>

Why no monetization was attempted is not documented. Possible explanations include the founder's belief that charging would kill growth in a small market, the difficulty of monetizing a product that competed with free alternatives, or simply a lack of business model focus during the growth phase. None of these explanations are confirmed by available sources.

### Structural Factor: The Infrastructure Layer Captured the Value

Twitch — also a YC company — was building the platform that Teevox depended on entirely. Teevox was a viewing experience layer on top of Twitch's infrastructure. This created a fundamental dependency: if Twitch built multi-stream viewing natively, Teevox's core value proposition would disappear overnight.

Twitch's interest in Kim was not incidental. The company attempted to hire him in 2012, around the time of Teevox's shutdown. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[24]</a></sup> This is both a validation of Kim's technical expertise and a signal of where the value in the eSports streaming stack was accumulating. Twitch was acquired by Amazon in 2014 for $970 million. The infrastructure layer won. The experience layer built on top of it did not.

<media-image src="https://www.alistdaily.com/wp-content/uploads/2016/02/teevox_logo.jpg" alt="Teevox logo and branding from 2016 relaunch" caption="Teevox's branding as featured in the AList Daily interview with founder Jong-Moon Kim in February 2016, when he resurrected the platform for the new age of eSports on Twitch."></media-image>

### The 2016 Resurrection: Vindication Without Resolution

Kim's 2016 relaunch of Teevox is the clearest evidence that the original thesis was directionally correct. By 2016, the eSports audience had grown to over 200 million monthly viewers — a 13x increase from 2011. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[1]</a></sup> The technical infrastructure had also improved: React and Firebase made it possible to build a faster, more capable product with less engineering effort than the 2012 version required. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[17]</a></sup>

Whether the 2016 version succeeded is unknown. No follow-up coverage, shutdown announcement, or success metrics appear in the public record. The outcome of the resurrection attempt remains unresolved.

---

## Key Lessons

- **Market timing is a capital problem, not just a strategy problem.** Teevox's thesis was correct — eSports viewing became a massive market — but the company had $20,000 in funding and no revenue to bridge the gap between 2012 and the 2015–2016 inflection point. <sup><a href="https://www.cbinsights.com/company/teevox">[7]</a></sup> Founders entering nascent markets need to calculate not just whether the market will arrive, but whether they have the runway to survive until it does. Teevox did not.

- **Building on a single platform's infrastructure creates an existential dependency.** Teevox's entire product depended on Twitch's streaming infrastructure. Twitch had both the capability and the incentive to build multi-stream viewing natively, which would have eliminated Teevox's core value proposition. Startups building experience layers on top of platform infrastructure need either a defensible technical moat, a partnership agreement, or a plan for what happens when the platform competes directly.

- **700,000 free users is not traction — it is a cost center.** Teevox reached a meaningful user base with no monetization strategy, which meant that growth increased costs without increasing revenue. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[10]</a></sup> The lesson is not that free products are wrong, but that a free product requires either a clear path to monetization or a funding strategy that can sustain operations until that path is found. Teevox had neither.

- **Copycat competition is fastest in small markets.** In a large market, a first-mover can grow fast enough to build a defensible position before competitors arrive. In a small market, copycats arrive at the same time as the original product but with larger existing audiences and cross-subsidized cost structures. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[18]</a></sup> Teevox's technical innovations were real but undefended, and the market was too small to outrun the competition.

- **Seasonal, event-driven usage is a warning sign, not a growth signal.** Teevox's peak usage correlated with StarCraft tournament seasons. <sup><a href="https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/">[22]</a></sup> This pattern indicated that the product had not yet become a daily habit — users came for tournaments and left when they ended. A product that cannot demonstrate consistent engagement outside of peak events will struggle to attract institutional investment and will be vulnerable to user base erosion during off-peak periods.

---

## Sources

1. [AList Daily — "How Teevox Was Resurrected for New Age of eSports" (February 5, 2016)](https://www.alistdaily.com/strategy/how-teevox-was-resurrected-for-new-age-of-esports/)
2. [TechCrunch — "Teevox" launch article (August 19, 2010)](https://techcrunch.com/2010/08/19/teevox/)
3. [Augmented World Expo 2018 — Andrew Sugaya speaker profile](https://usa2018.augmentedworldexpo.com/speakers/andrew-sugaya/)
4. [Y Combinator — Teevox company profile](https://www.ycombinator.com/companies/teevox)
5. [CB Insights — Teevox company profile](https://www.cbinsights.com/company/teevox)
6. [ReadWrite — "YCombinator Demo Day" (August 24, 2010)](https://readwrite.com/2010/08/24/ycombinator-demoday)
7. [True Ventures — "Thoughts on Y Combinator Demo Day"](https://trueventures.com/blog/thoughts-on-y-combinator-demo-day)
8. [Crunchbase — Teevox organization profile](https://www.crunchbase.com/organization/teevox)
9. [Crunchbase — Andrew Sugaya person profile](https://www.crunchbase.com/person/andrew-sugaya)
10. [Golden — Teevox wiki entry](https://golden.com/wiki/Teevox-99B6KVD)
11. [TechCrunch — "Y Combinator Demo Day 2" (August 24, 2010)](https://techcrunch.com/2010/08/24/y-combinator-demo-day-2/)
12. [Hacker News — "Watch 3 concurrent streams of the Curiosity landing with HN/Reddit Chat" (2012)](https://news.ycombinator.com/item?id=4343685)
13. [Hacker News — "Show HN: Teevox – Twitch Multistream Player, made in Static HTML, React, Firebase" (2016)](https://news.ycombinator.com/item?id=10940507)
