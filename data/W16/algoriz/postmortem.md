# Research Report: Algoriz

## Overview

Soraya Taghavi spent four years as a Vice President and Strategist at Goldman Sachs from April 2010 to March 2014, working directly on trading floors where she observed a persistent structural problem.<sup><a href="https://contactout.com/Soraya-Taghavi-1990366">[1]</a></sup> Traders with sophisticated market intuitions — people who understood when and why to move on a position — routinely lacked the programming skills to encode those intuitions into automated algorithms. The gap between "I have an idea" and "I have a working algorithm" required either a technical co-pilot or months of learning to code. Neither was practical at the speed of markets.

After Goldman Sachs, Taghavi moved to Millennium Partners, where she served as Head of Energy Commodities Data Analytics from December 2013 to December 2015.<sup><a href="https://contactout.com/Soraya-Taghavi-1990366">[2]</a></sup> The same problem persisted in a different context. Taghavi held a PhD in Electrical Engineering from the University of Southern California, completed between 2006 and 2010, which gave her the technical foundation to actually build the natural language processing engine the solution would require.<sup><a href="https://www.crunchbase.com/person/soraya-taghavi">[3]</a></sup> She was, in other words, one of the few people who had both observed the problem from the inside and possessed the skills to address it.

As TechCrunch reported in March 2017, Taghavi "previously worked in trading at Goldman Sachs, where she noticed a disconnect between traders with ideas and people actually able to code technical trading algorithms."<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[4]</a></sup> She founded Algoriz in 2015 after departing Millennium Partners, establishing the company in New York City — the natural home for a fintech startup targeting professional traders.<sup><a href="https://app.dealroom.co/companies/algoriz">[5]</a></sup>

The company was built by alumni of Goldman Sachs and Millennium Partners, giving it immediate credibility with its target market.<sup><a href="https://www.crunchbase.com/organization/algoriz">[6]</a></sup> YC's own company page lists a team size of four, though only Taghavi is publicly identified as a founder.<sup><a href="https://www.ycombinator.com/companies/algoriz">[7]</a></sup> The remaining team composition has never been publicly documented.

One data discrepancy is worth noting. Y Combinator's own company page lists Algoriz as a Winter 2016 (W16) batch company, while TechCrunch's March 2017 coverage and the YC W17 Demo Day roundup both describe Algoriz as a W17 participant.<sup><a href="https://techcrunch.com/2017/03/20/yc-demo-day-winter-2017/">[8]</a></sup> The most likely explanation is that Algoriz was accepted into the W16 batch but presented publicly at the W17 Demo Day — or that a data entry error propagated across secondary sources. This report treats the YC W16 acceptance as accurate and the March 2017 Demo Day presentation as the company's primary public milestone.

## Founding Story

### Timeline

- **2015** — Soraya Taghavi founds Algoriz in New York City after departing Millennium Partners, drawing on her Goldman Sachs and Millennium Partners trading floor experience.<sup>[[5]](https://app.dealroom.co/companies/algoriz)</sup>

- **December 2015** — Taghavi departs Millennium Partners, where she served as Head of Energy Commodities Data Analytics since December 2013, to focus on Algoriz full-time.<sup>[[2]](https://contactout.com/Soraya-Taghavi-1990366)</sup>

- **March 22, 2016** — Algoriz receives an undisclosed investment from Y Combinator, associated with the W16 batch per YC's own records.<sup>[[9]](https://www.crunchbase.com/organization/algoriz/company_overview/overview_timeline)</sup>

- **November 2016** — Algoriz platform launches publicly.<sup>[[10]](https://app.dealroom.co/companies/algoriz)</sup>

- **March 3, 2017** — TechCrunch publishes the definitive profile of Algoriz, describing the plain-English algorithm builder and noting the platform cannot yet initiate trades directly — only send email notifications when conditions are met.<sup>[[4]](https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/)</sup>

- **March 20, 2017** — Algoriz presents at YC W17 Demo Day, reporting 500 professional traders signed up and a letter of intent from a $200 million hedge fund. A $120,000 seed round closes with Y Combinator and Cerium Technology Ventures as investors.<sup>[[11]](https://techcrunch.com/2017/03/20/yc-demo-day-winter-2017/)</sup>

- **2017–2020** — No public press coverage, funding announcements, or product updates found. The company's operational history during this period is entirely undocumented.

- **January 2021** — Algoriz listed as "Out of Business" per PitchBook (via Dealroom).<sup>[[12]](https://app.dealroom.co/companies/algoriz)</sup> No shutdown announcement is made. YCDB marks the company as "Dead."<sup>[[13]](https://www.ycdb.co/company/algoriz)</sup>

## What They Built

Algoriz's core product was a natural language processing engine that converted plain-English trading instructions into executable algorithms — without requiring users to write a single line of code.<sup><a href="https://www.ycombinator.com/companies/algoriz">[14]</a></sup>

The mechanic was straightforward in concept. A user typed a trading rule in ordinary English — for example, "If SNAP is up 3% from yesterday, and the S&P is down, sell 100 shares of SNAP" — and the platform parsed that sentence, identified the conditional logic, the securities involved, the directional trigger, and the action, then generated a working algorithm from it.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[15]</a></sup> The same mechanic applied to more sophisticated inputs: users could specify Bollinger Bands, exponential moving averages, and MACD (Moving Average Convergence Divergence) — standard technical indicators used by professional traders — and the platform would incorporate them correctly.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[16]</a></sup>

Once an algorithm was created, users could back-test it against historical market data to evaluate how it would have performed before committing real capital.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[17]</a></sup> This backtesting capability was a meaningful feature: it let traders validate their intuitions against real historical price data without risking money.

The product had a critical gap at the time of its public launch and Demo Day presentation in March 2017. When algorithm conditions were met — when the market moved in the way the user had specified — the platform sent an email notification to the user. It could not yet initiate a trade directly.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[18]</a></sup> The user still had to log into their brokerage account and execute the trade manually. This distinction matters enormously: the difference between "a tool that tells you when to trade" and "a system that trades for you" is the difference between a useful dashboard and an actual automated trading platform. The product was the former presenting itself as the latter.

The planned business model required brokerage integration that had not yet been built. Algoriz intended to allow algorithms to initiate trades directly through connected brokerage accounts, and planned to charge users who used third-party brokerages while keeping the platform free for users who traded through Algoriz itself.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[19]</a></sup>

At some point after Demo Day — the exact timing is unknown — the company did complete brokerage integration with Interactive Brokers, enabling direct trade execution without Algoriz ever holding user funds.<sup><a href="https://app.dealroom.co/companies/algoriz">[20]</a></sup> The platform also eventually expanded to support cryptocurrency trading, including Bitcoin, Ethereum, and XRP, in addition to equities.<sup><a href="https://app.dealroom.co/companies/algoriz">[21]</a></sup> A tiered subscription model was implemented: a free "Lite" plan (2 algorithms, paper trading, 1-year backtest, email notifications, stocks only), a "Professional" plan at $29/month (10 algorithms, 5 screeners, 5+ year backtest, stocks and crypto), a "Premium" plan at $69/month (unlimited algorithms and screeners, SMS notifications, dedicated hosting), and an "Enterprise" plan with custom pricing.<sup><a href="https://captainaltcoin.com/algoriz-review/">[22]</a></sup>

Algoriz also envisioned a second-act product: a marketplace connecting capital allocators with successful traders who had built profitable algorithms on the platform.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[23]</a></sup> This vision — essentially a two-sided market for algorithmic trading strategies — was ambitious and would have required the core product to be fully proven first. There is no evidence it was ever built.

What distinguished Algoriz from alternatives was the NLP translation layer. Competing platforms like Quantopian required users to write Python code directly. Algoriz's bet was that the bottleneck was not market insight but technical implementation — and that removing the coding requirement would unlock a large population of traders who were currently locked out of algorithmic execution.

## Market Position

### Target Customers

Algoriz targeted professional traders — people already working in finance who had developed trading intuitions and strategies but lacked programming skills to automate them.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[4]</a></sup> The 500 users reported at Demo Day were described specifically as "professional traders," not retail investors or hobbyists.<sup><a href="https://techcrunch.com/2017/03/20/yc-demo-day-winter-2017/">[11]</a></sup> The letter of intent from a $200 million hedge fund suggests the company was also pursuing institutional clients — a higher-value but more complex sales motion requiring compliance review, security audits, and longer procurement cycles.

The secondary target was the broader retail algorithmic trading market: individual investors interested in automating their strategies without learning to code. The tiered subscription model, with a free entry tier and paid plans starting at $29/month, was designed to serve this segment.<sup><a href="https://captainaltcoin.com/algoriz-review/">[22]</a></sup>

### Market Size

The algorithmic trading market was large and growing during Algoriz's operational years. Algorithmic trading accounted for a significant share of total equity market volume in the United States by the mid-2010s, with estimates ranging from 60% to 75% of all U.S. equity trades being executed algorithmically. The addressable market for tools enabling non-technical traders to participate in this space was real — validated by the existence of multiple funded competitors pursuing the same opportunity.

The retail algorithmic trading platform market was smaller but meaningful. Quantopian, Algoriz's most prominent competitor, raised over $48 million in venture funding before shutting down in 2020 — a data point that simultaneously confirms the market's attractiveness to investors and its structural difficulty to monetize.<sup><a href="https://tracxn.com/d/companies/algoriz/__YfP-qlMiQDIjOs8LJbMDfh52gN0INEieRRNxeDC5A34">[24]</a></sup>

### Competition

Tracxn identified Algoriz's top competitors as Quantopian, FXlabsplus, and A.I. Capital Management.<sup><a href="https://tracxn.com/d/companies/algoriz/__YfP-qlMiQDIjOs8LJbMDfh52gN0INEieRRNxeDC5A34">[24]</a></sup>

Quantopian was the most significant. Founded in 2011 and backed by Andreessen Horowitz, Point72 Ventures, and others, Quantopian built a Python-based algorithmic trading platform with a large community of quantitative researchers. It required users to code in Python — the exact barrier Algoriz was trying to eliminate. Quantopian shut down in October 2020, citing an inability to find a scalable business model for its crowd-sourced fund. Its failure, despite vastly superior funding and brand recognition, suggests the monetization challenge in this space was structural rather than specific to Algoriz's execution.

The key competitive differentiation Algoriz claimed was the NLP translation layer — the ability to accept plain English rather than code. This was a genuine technical distinction in 2016 and 2017, predating the widespread availability of capable large language models that would later make this kind of natural language interface far easier to build. Whether the NLP engine was accurate enough in practice to be reliable — a critical question for any trading tool — is unknown from available sources.

## Business Model

Algoriz's intended revenue model had two components. The primary model was a tiered subscription: a free "Lite" plan to drive user acquisition, a "Professional" plan at $29/month, a "Premium" plan at $69/month, and an "Enterprise" plan at custom pricing for institutional clients.<sup><a href="https://captainaltcoin.com/algoriz-review/">[22]</a></sup> The secondary model — planned but apparently never implemented — was brokerage revenue: users who traded through Algoriz as their broker would use the platform for free, with Algoriz earning on order flow or brokerage commissions.

The math on the subscription model was challenging. Even if all 500 professional traders reported at Demo Day converted to the highest retail tier ($69/month), monthly revenue would reach approximately $34,500 — insufficient to sustain a four-person fintech team in New York City without additional funding. Converting the $200 million hedge fund LOI to a paying Enterprise contract would have changed the economics materially, but no evidence exists that this conversion occurred. The institutional sales cycle — compliance review, security audits, legal negotiation — typically runs three to twelve months, a timeline incompatible with a startup operating on a $120,000 seed round.2f:T65e,

## Traction

At the YC W17 Demo Day in March 2017, Algoriz reported 500 professional traders signed up on the platform since its November 2016 launch — approximately 500 users acquired in four months.<sup><a href="https://techcrunch.com/2017/03/20/yc-demo-day-winter-2017/">[11]</a></sup> For a niche B2B fintech product targeting a specific professional segment, this was a meaningful early signal.

The company also reported a letter of intent from a $200 million hedge fund to use the platform.<sup><a href="https://techcrunch.com/2017/03/20/yc-demo-day-winter-2017/">[11]</a></sup> A letter of intent is not a contract and carries no revenue obligation, but it indicated that at least one institutional buyer found the product credible enough to signal intent. Whether this LOI converted to a paying relationship is unknown.

According to Algoriz's own webpage (cited in a 2024 review), over 10,000 different strategies were made and tested on the platform.<sup><a href="https://captainaltcoin.com/algoriz-review/">[25]</a></sup> This figure, if accurate, suggests genuine user engagement — traders were not merely signing up but actively building and testing algorithms. However, this claim comes from the company's own marketing materials and cannot be independently verified. The timing of when this milestone was reached is also unknown.

No revenue figures were ever publicly disclosed. No user growth data beyond the 500-trader Demo Day figure was found in any source. The gap between the last press coverage in March 2017 and the company's shutdown around January 2021 represents approximately four years of operational silence.

## Post-Mortem

Algoriz operated for approximately five years — from founding in 2015 to shutdown around January 2021 — and left no public explanation for its closure.<sup><a href="https://app.dealroom.co/companies/algoriz">[12]</a></sup> No founder post-mortem, shutdown announcement, or investor statement was ever published.<sup><a href="https://www.ycdb.co/company/algoriz">[26]</a></sup> What follows is reconstructed from the available evidence.

### Primary Cause: Critically Insufficient Funding for the Problem Being Solved

The most significant factor in Algoriz's failure was a fundamental mismatch between the capital raised and the capital required to build what the company had promised.

Total confirmed funding was $120,000 — the standard YC seed check — raised at Demo Day in March 2017 from Y Combinator and Cerium Technology Ventures.<sup><a href="https://www.crunchbase.com/organization/algoriz/company_overview/overview_timeline">[27]</a></sup> Tracxn's database confirms this as the total funding across all rounds.<sup><a href="https://tracxn.com/d/companies/algoriz/__YfP-qlMiQDIjOs8LJbMDfh52gN0INEieRRNxeDC5A34">[28]</a></sup> No Series A or follow-on funding was ever announced or found in any database.

Building a regulated, brokerage-integrated algorithmic trading platform requires legal compliance work, brokerage API integration, security infrastructure to handle trading credentials, and ongoing data feed costs — none of which are cheap. Fintech Sandbox participation suggests Algoriz was accessing financial data through a nonprofit program rather than paying commercial data rates, which helped extend runway.<sup><a href="https://www.fintechsandbox.org/startup/algoriz/">[29]</a></sup> But data costs were only one line item.

The failure to raise follow-on funding after a YC Demo Day with 500 users and an institutional LOI is itself diagnostic. Investors who saw the Demo Day pitch would have noted the incomplete product — specifically, the absence of direct trade execution — and the thin revenue evidence. The institutional LOI, while validating, was not a signed contract. The regulatory complexity of brokerage integration, combined with a four-person team and $120,000 in capital, likely made the risk profile unattractive for most fintech investors.

### Secondary Cause: An Incomplete Product at the Moment of Maximum Visibility

Algoriz's Demo Day presentation in March 2017 was its highest-visibility moment — covered by TechCrunch, seen by hundreds of investors, and generating the institutional LOI that represented its best near-term revenue opportunity. At that exact moment, the product could not execute trades.<sup><a href="https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/">[18]</a></sup>

The platform sent email notifications when algorithm conditions were met. Users still had to log into their brokerage accounts and execute manually. For a product positioning itself as an "automated trading platform," this gap was not a minor limitation — it was the core value proposition, undelivered.

TechCrunch's March 3, 2017 article, published two weeks before Demo Day, explicitly noted this limitation. Any investor who read the article before the Demo Day pitch knew the product was incomplete. The company's response — acknowledging the gap and describing plans to build brokerage integration — was honest but did not resolve the fundamental problem: the product being demonstrated was not yet the product being sold.

The eventual completion of Interactive Brokers integration addressed this gap, but the timing is unknown.<sup><a href="https://app.dealroom.co/companies/algoriz">[20]</a></sup> If it was completed months after Demo Day, the window for converting institutional interest had likely already closed. Institutional buyers who expressed interest in March 2017 would not have waited indefinitely for a feature that was described as "planned."

### Tertiary Cause: Structural Market Difficulty in Monetizing Retail Algorithmic Trading

Algoriz was not alone in struggling to build a sustainable business in this space. Quantopian — its most prominent competitor, backed by Andreessen Horowitz and Point72 Ventures with over $48 million raised — shut down in October 2020 after failing to find a scalable monetization model for its crowd-sourced algorithmic trading fund.<sup><a href="https://tracxn.com/d/companies/algoriz/__YfP-qlMiQDIjOs8LJbMDfh52gN0INEieRRNxeDC5A34">[24]</a></sup>

The structural challenge is this: retail traders who build profitable algorithms have no incentive to share them. Traders who share their algorithms publicly are, by definition, sharing alpha — the informational edge that makes the strategy profitable. As more traders adopt the same strategy, the edge erodes. This creates a fundamental tension in any marketplace model for algorithmic trading strategies.

Algoriz's planned marketplace — connecting capital with successful algorithm creators — faced this same structural problem. The most successful traders on the platform would have the least incentive to participate in a marketplace that commoditized their strategies.

The subscription model avoided this problem but created a different one: the revenue ceiling was low. At $29–$69/month per user, reaching profitability required either a very large user base (difficult in a niche professional market) or a small number of high-value enterprise contracts (requiring a long sales cycle incompatible with the company's funding level).

### Contributing Factor: The Long Silence (2017–2021)

The four-year gap between Algoriz's last press coverage (March 2017) and its shutdown (January 2021) is unexplained. The company may have operated in a reduced capacity, with Taghavi sustaining it personally or with minimal overhead. It may have continued building the product and acquiring users without public visibility. Or it may have effectively ceased active development shortly after Demo Day and simply remained legally incorporated until a formal closure.

What is clear is that no acquisition, pivot, or asset sale occurred.<sup><a href="https://www.ycdb.co/company/algoriz">[26]</a></sup> The company did not find a buyer for its NLP-to-algorithm technology, its user base, or its brokerage integrations. It simply stopped.

## Key Lessons

- **Maximum visibility requires a complete product.** Algoriz presented at YC Demo Day — its highest-leverage moment for fundraising and institutional sales — with a platform that sent email notifications instead of executing trades. The gap between what was demonstrated and what was promised was visible to every investor in the room. Startups in regulated industries with long sales cycles cannot afford to show institutional buyers a product that is "almost there." The cost of Demo Day with an incomplete product is not just a missed funding round — it is the permanent loss of the institutional relationships that expressed early interest.

- **Funding requirements scale with regulatory complexity.** A consumer app can be built and iterated on $120,000. A brokerage-integrated algorithmic trading platform — requiring compliance infrastructure, security audits, API integrations with regulated financial institutions, and ongoing data feed costs — cannot. The mismatch between Algoriz's capital and its technical roadmap was not a failure of execution; it was a failure of fundraising strategy. The company needed to either raise significantly more capital before building in a regulated domain, or scope the product to something achievable within its actual runway.

- **Institutional LOIs are not revenue.** The $200 million hedge fund letter of intent was Algoriz's most compelling traction signal at Demo Day. But an LOI carries no payment obligation and expires if the product does not deliver. Converting institutional interest to signed contracts requires a complete product, a compliance-ready security posture, and a sales process that can survive a procurement cycle measured in months. None of these were in place at the time the LOI was received.

- **Structural market challenges compound execution problems.** Quantopian's 2020 shutdown — with $48 million raised and a large user community — demonstrated that the monetization challenge in retail algorithmic trading is not purely an execution problem. The fundamental tension between sharing profitable strategies and preserving their value affects every platform in this space. Algoriz's planned marketplace faced this same structural headwind, regardless of how well the core product was built.

- **Silence is not survival.** The four-year gap between Algoriz's last public activity and its formal shutdown suggests the company may have continued operating in a reduced state long after its growth trajectory had stalled. Founders who sustain companies past the point of viable growth delay the reallocation of their own time and talent to more productive opportunities. A faster, more deliberate wind-down — or a more aggressive pivot — might have preserved more value for all stakeholders.

## Sources

1. [Soraya Taghavi career history — ContactOut](https://contactout.com/Soraya-Taghavi-1990366)
2. [Algoriz company profile — Dealroom](https://app.dealroom.co/companies/algoriz)
3. [Soraya Taghavi founder profile — Crunchbase](https://www.crunchbase.com/person/soraya-taghavi)
4. [Algoriz lets you build trading algorithms with no coding required — TechCrunch, March 3, 2017](https://techcrunch.com/2017/03/03/algoriz-lets-you-build-trading-algorithms-with-no-coding-required/)
5. [Algoriz company profile — Crunchbase](https://www.crunchbase.com/organization/algoriz)
6. [Algoriz company page — Y Combinator](https://www.ycombinator.com/companies/algoriz)
7. [YC Demo Day Winter 2017 — TechCrunch, March 20, 2017](https://techcrunch.com/2017/03/20/yc-demo-day-winter-2017/)
8. [Algoriz funding timeline — Crunchbase](https://www.crunchbase.com/organization/algoriz/company_overview/overview_timeline)
9. [Algoriz — Tracxn](https://tracxn.com/d/companies/algoriz/__YfP-qlMiQDIjOs8LJbMDfh52gN0INEieRRNxeDC5A34)
10. [Algoriz — LinkedIn](https://www.linkedin.com/company/algoriz)
11. [Algoriz entry — YCDB](https://www.ycdb.co/company/algoriz)
12. [Algoriz review — CaptainAltcoin, February 2, 2024](https://captainaltcoin.com/algoriz-review/)
13. [Algoriz startup profile — Fintech Sandbox](https://www.fintechsandbox.org/startup/algoriz/)
14. [Soraya Taghavi org chart — The Org](https://theorg.com/org/algoriz/org-chart/soraya-taghavi)
15. [Algoriz archived website — Wayback Machine](https://web.archive.org/web/20161026000000*/algoriz.com)
16. [Algoriz product page — Product Hunt](https://www.producthunt.com/products/algoriz)
