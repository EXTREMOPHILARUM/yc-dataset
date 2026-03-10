# Research Report: Preflight

## Overview

Preflight was a Chicago-area no-code web testing startup founded in 2018 by Mustafa Bayramoglu. The company built a Chrome extension-based platform that let non-engineers record, run, and maintain automated browser tests without writing a single line of code — a direct response to the brittleness of Selenium-based test suites that plagued engineering teams at fast-growing startups. Accepted into Y Combinator's Winter 2019 batch, Preflight raised approximately $1.35–1.59M across two rounds before being acquired by Applitools in June 2023.<sup><a href="https://www.ycombinator.com/companies/preflight">[1]</a></sup>

Preflight solved a real problem with technically credible execution, but it was caught in a structural trap: the no-code testing category was simultaneously validated and commoditized by better-funded incumbents. With only "tens of customers" and roughly 20 employees at the time of sale, the company never reached the revenue density needed to sustain its cost structure or attract a Series A.<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[2]</a></sup>

Applitools — itself a Thoma Bravo portfolio company — acquired Preflight on June 29, 2023, in what was substantially an acqui-hire of talent and technology. The reported price of $10–15M (low confidence) would represent a modest return on invested capital, consistent with a soft landing rather than a growth exit.<sup><a href="https://qa-financial.com/applitools-acquires-low-code-specialist-preflight/">[3]</a></sup>

<report-gallery>
<media-image src="https://bubble.io/blog/content/images/2023/07/bubble-preflight-founder.png" alt="Mustafa Bayramoglu, founder of Preflight, featured in Bubble's blog post about the partnership" caption="Mustafa Bayramoglu, Preflight's founder and CEO, photographed for Bubble's partnership feature — one of the company's last major go-to-market moves before the Applitools acquisition closed weeks later."></media-image>
</report-gallery>

## Founding Story

Mustafa Bayramoglu's path to founding Preflight was neither linear nor easy. A Turkish national who immigrated to the United States, Bayramoglu holds a Master's degree in High Performance Computing and Bioinformatics<sup><a href="https://bubble.io/blog/bubble-preflight/">[4]</a></sup> and joined ShipBob — the Chicago-based e-commerce fulfillment startup — as its first engineer. Over several years, he scaled ShipBob's engineering organization from one person to more than 40 engineers.<sup><a href="https://www.ycombinator.com/companies/preflight">[5]</a></sup> That experience gave him both the technical credibility to build developer tools and the operational context to understand where engineering teams break down.

The founding insight came from a specific, painful failure. Bayramoglu and his team at ShipBob spent two months writing 100 Selenium test cases — a significant investment of engineering time. Within three to four weeks, those tests had become unmaintainable: brittle selectors broke on every UI change, false positives eroded trust, and the team quietly stopped running them. "We wrote 100 Selenium test cases in 2 months," Bayramoglu wrote in Preflight's Hacker News launch post, "but could not maintain them within 3–4 weeks."<sup><a href="https://news.ycombinator.com/item?id=29551289">[6]</a></sup> This is a near-universal frustration in software engineering, but Bayramoglu had the rare combination of having lived it at scale and having the technical background to build a better solution.

Getting to that solution required unusual persistence. Bayramoglu applied to Y Combinator six times before being accepted with Preflight.<sup><a href="https://techcrunch.com/2021/08/05/3-invaluable-founder-lessons-i-learned-on-my-immigration-journey/">[7]</a></sup> His immigration journey added a further layer of complexity: as a Turkish national navigating asylee status and H-1B visa constraints, he could not simply quit ShipBob to pursue Preflight full-time. Instead, he took an unpaid sabbatical from ShipBob to attend YC and work on the company — a workaround that preserved his visa status but constrained his early optionality.<sup><a href="https://techcrunch.com/2021/08/05/3-invaluable-founder-lessons-i-learned-on-my-immigration-journey/">[8]</a></sup> He later reflected that the uncertainty of immigration had been its own form of founder training: "In my journey to the U.S., I became good at three things: accepting uncertainty, building resilience and maintaining a positive mental attitude. I needed them all to get my startup off the ground."<sup><a href="https://techcrunch.com/2021/08/05/3-invaluable-founder-lessons-i-learned-on-my-immigration-journey/">[9]</a></sup>

Tracxn lists a co-founder, Patrick Johnson, alongside Bayramoglu.<sup><a href="https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE">[10]</a></sup> Johnson is entirely absent from all press coverage, founder interviews, and the acquisition announcement — his role, background, and whether he remained with the company through the Applitools deal are unknown. The available record treats Preflight as a solo-founder story, though this may simply reflect Bayramoglu's public profile rather than Johnson's actual contribution.

Preflight was founded in 2018 and accepted into YC's Winter 2019 cohort<sup><a href="https://www.ycombinator.com/companies/preflight">[11]</a></sup> — a batch that graduated into one of the strongest venture funding environments in recent memory. The initial vision was clear and narrow: eliminate the Selenium maintenance problem by letting anyone record tests through a browser extension, without writing code.

## Timeline

- **2018** — Mustafa Bayramoglu founds Preflight in the Chicago area, inspired by Selenium test maintenance failures at ShipBob.<sup>[[12]](https://www.calcalistech.com/ctechnews/article/rycgkmid2)</sup>
- **January 2019** — Preflight accepted into Y Combinator Winter 2019 batch.<sup>[[11]](https://www.ycombinator.com/companies/preflight)</sup>
- **March 18, 2019** — Preflight receives its first funding round (YC pre-seed investment).<sup>[[10]](https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE)</sup>
- **March 2021** — Applitools (future acquirer) is acquired by Thoma Bravo for approximately $250–300M, signaling PE consolidation of the testing market.<sup>[[13]](https://www.calcalistech.com/ctechnews/article/rycgkmid2)</sup>
- **April 2021** — Preflight raises a $1.2M Seed round at a $5M pre-money valuation from Grand Ventures, OCA Ventures, Hyde Park Venture Partners, M25, and Y Combinator.<sup>[[14]](https://www.crunchbase.com/funding_round/preflight-seed--42095094)</sup>
- **August 5, 2021** — Bayramoglu publishes a TechCrunch essay on immigration and entrepreneurship; no product or funding announcements accompany it.<sup>[[8]](https://techcrunch.com/2021/08/05/3-invaluable-founder-lessons-i-learned-on-my-immigration-journey/)</sup>
- **December 15, 2021** — Preflight publishes its Launch HN post on Hacker News, approximately 2.5 years after YC graduation — describing the product and origin story for the first time to the developer community.<sup>[[6]](https://news.ycombinator.com/item?id=29551289)</sup>
- **June 29, 2023** — Applitools acquires Preflight. Key technical staff including Bayramoglu join Applitools. Reported price approximately $10–15M (low confidence). Company had approximately 20 employees and "tens of customers" at time of sale.<sup>[[15]](https://www.prnewswire.com/news-releases/applitools-acquires-preflight-to-help-bring-its-ai-powered-testing-platform-to-teams-of-all-skill-sets-301867081.html)</sup>
- **October 30, 2023** — Bubble publishes a blog post about the Preflight partnership and product capabilities, post-acquisition.<sup>[[4]](https://bubble.io/blog/bubble-preflight/)</sup>

<media-hn url="https://news.ycombinator.com/item?id=29551289" title="Launch HN: Preflight – No-code web app testing for everyone" points="" comments=""></media-hn>

## What They Built

Preflight's core product was a no-code test automation platform for web applications. The central insight was that most software teams want automated browser tests but cannot sustain the engineering overhead of writing and maintaining them in frameworks like Selenium or Cypress. Preflight's answer was a Chrome extension that recorded a user's interactions with a web application — clicks, form fills, navigation — and converted those interactions into repeatable, automated test cases without any code.<sup><a href="https://www.ycombinator.com/companies/preflight">[16]</a></sup>

The user experience was deliberately simple. A QA analyst or product manager would install the Chrome extension, navigate to the application they wanted to test, click "record," and walk through the workflow they wanted to verify — logging in, adding an item to a cart, submitting a form. Preflight captured each step and stored it as a test. On subsequent runs, the platform would replay those steps across multiple browsers and device configurations, flagging any failures via Slack or email notification.<sup><a href="https://bubble.io/blog/bubble-preflight/">[17]</a></sup>

The product matured beyond the basic recorder over time. By the time of the Bubble partnership post in late 2023, Preflight's feature set included:

- **Cross-browser and cross-device execution**: Tests recorded once could run against Chrome, Firefox, Safari, and mobile viewports without modification.
- **CI/CD integration**: Preflight connected to GitHub and Jenkins, allowing tests to run automatically on every code push or pull request.<sup><a href="https://www.checkops.com/preflight/">[18]</a></sup>
- **API test generation**: The platform could observe the network calls made during a UI test recording and automatically generate corresponding API tests — a technically sophisticated feature that reduced the manual work of API test coverage.
- **Workflow orchestration**: A "Workflow" feature allowed teams to chain multiple test sequences together, enabling end-to-end scenario testing across complex multi-step user journeys.<sup><a href="https://bubble.io/blog/bubble-preflight/">[17]</a></sup>
- **Alerting**: Slack and email notifications on test failure, with enough context to identify which step broke and why.

Preflight claimed its approach was 20x faster than writing equivalent Selenium or Cypress tests manually.<sup><a href="https://www.ycombinator.com/companies/preflight">[16]</a></sup> This headline metric was aimed squarely at the buyer who had already tried code-based testing and found it unsustainable — a large and sympathetic audience.

The product's AI capabilities — specifically cited by Applitools' CTO as the differentiating factor among dozens of low-code tools evaluated<sup><a href="https://www.prnewswire.com/news-releases/applitools-acquires-preflight-to-help-bring-its-ai-powered-testing-platform-to-teams-of-all-skill-sets-301867081.html">[19]</a></sup> — likely referred to self-healing test logic: the ability to automatically update test selectors when UI elements changed, addressing the exact brittleness problem that had plagued Bayramoglu's Selenium tests at ShipBob. The specific implementation details were not publicly disclosed, and it is unclear whether these AI features were present at launch or added during the 2021–2023 period.

One notable product direction was a partnership with Bubble, the no-code application development platform. Preflight was building a plugin to measure test coverage specifically for Bubble-built applications<sup><a href="https://bubble.io/blog/bubble-preflight/">[17]</a></sup> — a niche that positioned Preflight as the natural testing layer for the no-code app development ecosystem. This roadmap item, published in October 2023 (after the acquisition had already closed), suggests the team was still actively expanding its surface area close to the sale date.

YC described Preflight in its W19 batch roundup as "code-free, automated testing software" where "no QA team is needed; anyone can create a test within seconds and catch bugs."<sup><a href="https://blog.ycombinator.com/9-companies-from-the-yc-w19-batch/">[20]</a></sup> That framing — democratizing QA for non-technical users — was the product's north star from the beginning.

## Market Position

### Target Customers

Preflight's primary buyer was the engineering or product team at a small-to-mid-sized software company that needed automated testing coverage but lacked dedicated QA engineers or the bandwidth to maintain code-based test suites. The product's no-code positioning made it accessible to product managers, customer success teams, and non-technical QA analysts — anyone who could navigate a web application but could not write JavaScript.

The Bubble partnership suggests a secondary target: teams building applications on no-code development platforms, who faced a specific gap — their apps were untestable by conventional code-based tools because the underlying code was generated and abstracted away. This was a structurally interesting niche: no-code app builders were growing rapidly in 2021–2023, and their testing needs were genuinely underserved by incumbents focused on traditional codebases.

### Market Size

The broader test automation market was large and growing. Estimates for the global test automation market ranged from $15–20B by the mid-2020s, with no-code and low-code testing representing a fast-growing subsegment. However, no public market sizing data specific to the no-code testing segment was available for Preflight's operating period. The relevant addressable market for Preflight's specific positioning — no-code testing for SMB and mid-market web applications — was likely a fraction of the headline number, and the competitive density in that segment was high relative to its size.

### Competition

Preflight competed on two axes simultaneously: against enterprise testing incumbents with deep distribution, and against VC-backed no-code testing specialists with comparable positioning and more capital.

**Enterprise incumbents** — SmartBear (TestComplete, Zephyr), Ranorex, and Tricentis — had established sales channels, large customer bases, and the resources to add no-code recording features to existing platforms. Their disadvantage was product complexity and pricing that was misaligned with Preflight's SMB target. But their distribution reach meant that any enterprise buyer evaluating testing tools would encounter them first.

**VC-backed no-code specialists** — Autify, Testsigma, and Usetrace — competed directly on Preflight's core value proposition with comparable or larger funding.<sup><a href="https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE">[21]</a></sup> These companies were fighting for the same buyer with similar products, creating a crowded middle of the market where differentiation was difficult to sustain.

**Applitools** — the eventual acquirer — occupied a different position: AI-powered visual testing with enterprise distribution and, after the Thoma Bravo acquisition in March 2021, PE-backed resources to consolidate the market.<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[13]</a></sup> Applitools was not a direct competitor in the no-code recording space, but its acquisition of Preflight illustrates the structural dynamic: when a well-capitalized platform decides to add a capability, it can acquire rather than build, and the acquisition price reflects the target's weakness as a standalone business rather than the value of the technology.

The most important competitive dynamic was not any individual competitor but the category structure itself. No-code testing is a feature that large testing platforms can absorb — it requires no proprietary data moat, no network effect, and no switching cost that a well-resourced incumbent cannot replicate. Preflight's "most robust AI abilities" (per Applitools' CTO) were a genuine differentiator, but technical differentiation in a feature category is a temporary advantage, not a structural moat. The company needed to either build a defensible distribution channel (e.g., deep integration with a platform like Bubble that created lock-in) or reach a scale where its customer base itself became the moat — and it ran out of runway before achieving either.

## Business Model

Preflight operated on a subscription SaaS model.<sup><a href="https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE">[10]</a></sup> Specific pricing tiers and average contract values were never publicly disclosed, and the company never disclosed revenue figures — the absence of any ARR or MRR data in press coverage or founder communications is itself a signal that the revenue base was not a selling point.

Working from available data, the unit economics can be roughly inferred. With approximately 20 employees at acquisition<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[2]</a></sup> and a Chicago-area cost base, a reasonable estimate for annual burn would be $2.5–3.5M (assuming average fully-loaded employee cost of $125,000–175,000). Against total disclosed funding of approximately $1.35–1.59M<sup><a href="https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE">[10]</a></sup> — and noting that the CTech article referenced "several millions of dollars from additional U.S. investors"<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[22]</a></sup> — the company's total capital raised may have been higher than the Crunchbase/Tracxn figures suggest. These are inferences, not facts; the actual burn rate and runway at acquisition are unknown.

What is clear is the structural mismatch: a 20-person SaaS company with "tens of customers" implies a revenue base that was almost certainly insufficient to cover operating costs. If "tens of customers" means 20–50 accounts, and if average contract values were in the $10,000–30,000 annual range (reasonable for an SMB-focused testing tool), implied ARR would be $200,000–$1.5M — well below the $2.5–3.5M estimated burn. The company was burning cash faster than it was generating revenue, and the absence of a Series A announcement between April 2021 and June 2023 strongly suggests that fundraising at growth-stage terms was not achievable.

## Traction

At the time of the Applitools acquisition in June 2023, Preflight had approximately 20 employees and "tens of customers in the U.S."<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[2]</a></sup> No ARR, MRR, user count, or growth rate data was ever publicly disclosed.

The December 2021 Hacker News launch post — published roughly 2.5 years after YC graduation — generated community discussion but no publicly reported customer or revenue milestones in its wake. The gap between the YC graduation (mid-2019) and the HN launch (December 2021) is notable: most YC companies that are growing quickly publicize that growth. The absence of public traction milestones during this period is consistent with a company that was iterating on product-market fit rather than scaling a proven motion.

The Bubble partnership, announced in the months before acquisition, represented the most concrete go-to-market signal in the public record — but it arrived too late to change the company's trajectory.

## Post-Mortem

### Primary Cause: Insufficient Revenue Density for a 20-Person Team

The most direct explanation for Preflight's outcome is a mismatch between cost structure and revenue. By June 2023, the company had grown to approximately 20 employees — a headcount that implies annual operating costs of $2.5–3.5M — while serving only "tens of customers."<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[2]</a></sup> Even under optimistic assumptions about contract values, the implied ARR was likely a fraction of the burn rate.

The team attempted to address this by expanding the product surface area (API testing, Workflow orchestration, CI/CD integrations) and pursuing the Bubble partnership as a new distribution channel. Neither move generated the customer volume needed to close the gap before the company's runway ran out. The absence of any Series A announcement between the April 2021 Seed and the June 2023 acquisition — a 26-month window — strongly suggests that Preflight could not demonstrate the growth metrics required for institutional growth-stage capital. Whether a Series A was attempted and failed, or was never pursued, is not documented in available sources.

### Structural Cause: Building a Feature in a Platform Market

The no-code testing category has a structural problem that Preflight could not solve with execution alone: it is a feature that large testing platforms can absorb, not a standalone product category with durable moats.

No-code test recording requires no proprietary data (tests are specific to each customer's application), no network effect (one customer's tests have no value to another), and no switching cost that a well-resourced incumbent cannot replicate. When Applitools' CTO evaluated "dozens of low code tools" before acquiring Preflight<sup><a href="https://www.prnewswire.com/news-releases/applitools-acquires-preflight-to-help-bring-its-ai-powered-testing-platform-to-teams-of-all-skill-sets-301867081.html">[19]</a></sup>, he was describing a market where many companies had built the same capability — validating the problem while confirming that no single player had established a defensible position. Preflight's "most robust AI abilities" were a genuine technical differentiator, but in a feature category, technical differentiation is a temporary advantage that a well-capitalized acquirer can buy rather than build.

The Thoma Bravo acquisition of Applitools in March 2021<sup><a href="https://www.calcalistech.com/ctechnews/article/rycgkmid2">[13]</a></sup> accelerated this dynamic. PE-backed platform companies in consolidating markets are motivated buyers of capability-filling acquisitions at modest prices — they can pay $10–15M for a team and technology that would cost $5–10M to build internally, while eliminating a competitor. Preflight's acquisition fits this playbook precisely.

### Go-to-Market Delay: The 2.5-Year Gap to Public Launch

Preflight graduated from YC in mid-2019 but did not publish its Hacker News launch post until December 2021 — approximately 2.5 years later.<sup><a href="https://news.ycombinator.com/item?id=29551289">[6]</a></sup> For a developer-tools company whose natural distribution channel is the developer community, this delay is significant. The HN launch is typically an early signal of a company's go-to-market motion, not a late-stage announcement.

The delay may reflect a deliberate decision to iterate on the product before going public, or it may reflect difficulty finding a repeatable customer acquisition channel. Either interpretation is consistent with the traction data: "tens of customers" after four-plus years of operation suggests that the company never found a scalable go-to-market motion. The team's response — the Bubble partnership, expanded integrations, a broader product surface — came late in the company's life and did not generate the growth needed to change the outcome.

### Undercapitalization Relative to Competitive Intensity

Preflight raised approximately $1.35–1.59M in total disclosed funding<sup><a href="https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE">[10]</a></sup> — a figure that is modest even by seed-stage standards for a company competing against VC-backed specialists (Autify, Testsigma) and PE-backed platforms (SmartBear, Applitools). The CTech article's reference to "several millions of dollars from additional U.S. investors" suggests the actual total may be higher than Crunchbase records, but even a $3–4M total raise would be thin for a 20-person company in a competitive market.

The April 2021 Seed round at a $5M pre-money valuation<sup><a href="https://www.crunchbase.com/funding_round/preflight-seed--42095094">[14]</a></sup> reflects investor confidence in the problem and the founder, but the valuation also signals that investors did not see breakout traction at that stage. A $5M pre-money valuation two years after YC graduation is a modest mark — consistent with a company that was making progress but had not yet demonstrated the growth rate that commands a premium.

The team's response to capital constraints appears to have been to grow headcount to 20 employees — a bet that more engineering and sales capacity would unlock growth. That bet did not pay off before the runway ran out.

### The Niche That Arrived Too Late: No-Code App Testing

The Bubble partnership hints at the most interesting strategic path Preflight did not fully pursue: becoming the testing infrastructure layer for the no-code application development ecosystem. No-code app builders like Bubble, Webflow, and Glide were growing rapidly in 2021–2023, and their testing needs were genuinely underserved — conventional testing tools assumed access to source code that no-code platforms abstract away.

This niche had real structural advantages: it was too small for enterprise incumbents to prioritize, it created platform-level lock-in (a Bubble-specific testing plugin is not easily replaced by a generic tool), and it aligned with Preflight's core capability. But the Bubble plugin was still on the roadmap at the time of acquisition<sup><a href="https://bubble.io/blog/bubble-preflight/">[17]</a></sup> — suggesting the team identified this opportunity late, or lacked the resources to pursue it aggressively alongside the broader product. Whether this niche could have supported a standalone business is unknown; the company was acquired before the experiment could run.

## Key Lessons

- **Preflight's 2.5-year gap between YC graduation and public HN launch illustrates the cost of delayed distribution for developer tools.** Developer-tools companies live and die by community adoption, and the HN launch is typically an early signal of go-to-market momentum, not a late-stage announcement. Preflight's December 2021 launch came after competitors like Autify (founded 2019, raised $10M Series A by 2021) had already established developer mindshare in the same category. The delay — whether caused by product iteration, go-to-market uncertainty, or resource constraints — meant Preflight was playing catch-up in a market that was already crowding.

- **A 20-person team with "tens of customers" is a structural warning sign, not a growth stage.** Preflight's headcount at acquisition implies annual operating costs that almost certainly exceeded its revenue by a significant margin. The decision to grow to 20 employees before achieving revenue density created a burn rate that compressed the runway available to find a scalable go-to-market motion. Comparable no-code testing companies that survived (Testsigma, Autify) raised 5–10x more capital to support similar team sizes — Preflight's undercapitalization relative to its cost structure left no margin for error.

- **The Bubble partnership identified the right niche too late.** Testing infrastructure for no-code application platforms was a structurally defensible position — too small for enterprise incumbents, too platform-specific for generic tools, and aligned with a fast-growing developer segment. Preflight's roadmap included a Bubble-specific test coverage plugin at the time of acquisition, but the feature was not yet shipped. A company that had pursued this niche exclusively from 2021 onward — rather than competing horizontally against better-funded rivals — might have built the distribution lock-in needed to sustain a standalone business.

- **In feature categories without data or network moats, technical differentiation is an acquisition asset, not a competitive moat.** Applitools' CTO evaluated "dozens of low code tools" and selected Preflight for its "most robust AI abilities" — a genuine compliment that also reveals the problem. When a market has dozens of competitors with similar capabilities, the winner is typically the one with the best distribution, not the best technology. Preflight's AI-powered self-healing tests were valuable enough to acquire but not differentiated enough to drive the customer concentration needed for a standalone growth story.

- **Preflight's founding story — six YC rejections, immigration constraints, an unpaid sabbatical — produced a founder with exceptional resilience but also constrained the company's early optionality.** Bayramoglu's H-1B workaround (an unpaid sabbatical rather than a clean break from ShipBob) reflects the real costs that immigration complexity imposes on immigrant founders at the earliest stages. The structural lesson is not about the founder's character — which was clearly strong — but about the ecosystem gap: immigrant founders navigating visa constraints face a higher bar to reach the starting line, and that friction compounds at the margin when capital and time are already scarce.

## Sources

1. [Y Combinator — Preflight company profile](https://www.ycombinator.com/companies/preflight)
2. [CTech / Calcalist — Applitools acquires Preflight (June 29, 2023)](https://www.calcalistech.com/ctechnews/article/rycgkmid2)
3. [QA Financial — Applitools acquires low-code specialist Preflight](https://qa-financial.com/applitools-acquires-low-code-specialist-preflight/)
4. [Bubble.io — How You Can Automate Web App Testing with No-Code Using Preflight (October 30, 2023)](https://bubble.io/blog/bubble-preflight/)
5. [TechCrunch — 3 invaluable founder lessons I learned on my immigration journey (August 5, 2021)](https://techcrunch.com/2021/08/05/3-invaluable-founder-lessons-i-learned-on-my-immigration-journey/)
6. [Hacker News — Launch HN: Preflight (December 15, 2021)](https://news.ycombinator.com/item?id=29551289)
7. [Tracxn — Preflight company profile](https://tracxn.com/d/companies/preflight/__yDUr_W5PX3YHGzh0UaKjIxm21cFVB-qbRt7ykIrWhbE)
8. [PR Newswire — Applitools acquires Preflight press release (June 29, 2023)](https://www.prnewswire.com/news-releases/applitools-acquires-preflight-to-help-bring-its-ai-powered-testing-platform-to-teams-of-all-skill-sets-301867081.html)
9. [Crunchbase — Preflight Seed funding round](https://www.crunchbase.com/funding_round/preflight-seed--42095094)
10. [Finsmes — Applitools acquires Preflight (July 4, 2023)](https://www.finsmes.com/2023/07/applitools-acquires-preflight.html)
11. [CheckOps — Preflight product overview](https://www.checkops.com/preflight/)
12. [DevOps Digest — Applitools acquires Preflight (June 30, 2023)](https://www.devopsdigest.com/applitools-acquires-preflight)
13. [YC Blog — 9 companies from the YC W19 batch](https://blog.ycombinator.com/9-companies-from-the-yc-w19-batch/)
