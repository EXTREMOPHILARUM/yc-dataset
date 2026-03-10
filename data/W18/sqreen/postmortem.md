# Research Report: Sqreen

## Overview

1:"$Sreact.fragment"
2:I[39756,["/_next/static/chunks/ff1a16fafef87110.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/803a574de9eda7ae.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"default"]
3:I[8821,["/_next/static/chunks/0d46db6cf73968fd.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/5f4dcbc1da431ca9.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/33f7e5a25c4fcd0b.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"default"]
4:I[37457,["/_next/static/chunks/ff1a16fafef87110.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/803a574de9eda7ae.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"default"]
5:I[22016,["/_next/static/chunks/0d46db6cf73968fd.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/39ad7020066b4868.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/33f7e5a25c4fcd0b.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],""]
6:I[2355,["/_next/static/chunks/0d46db6cf73968fd.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"Analytics"]
11:I[68027,["/_next/static/chunks/ff1a16fafef87110.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/803a574de9eda7ae.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"default"]
12:I[97367,["/_next/static/chunks/ff1a16fafef87110.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/803a574de9eda7ae.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"OutletBoundary"]
13:"$Sreact.suspense"
15:I[93539,["/_next/static/chunks/0d46db6cf73968fd.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/39ad7020066b4868.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/33f7e5a25c4fcd0b.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"ThemeToggle"]
23:I[97367,["/_next/static/chunks/ff1a16fafef87110.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/803a574de9eda7ae.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"ViewportBoundary"]
25:I[97367,["/_next/static/chunks/ff1a16fafef87110.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","/_next/static/chunks/803a574de9eda7ae.js?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt"],"MetadataBoundary"]
:HL["/_next/static/chunks/8be82ca8498e7d4a.css?dpl=dpl_GwuwmMc2oZNJkz1tEEADs8shECJt","style"]
:HL["/_next/static/media/1b99372b3eaef0c8-s.p.758e15a8.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
:HL["/_next/static/media/23b7a97ae3b5c134-s.p.2902b61f.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
:HL["/_next/static/media/68d403cf9f2c68c5-s.p.f9f15f61.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
:HL["/_next/static/media/99e609270109b47d-s.p.64b9304e.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
:HL["/_next/static/media/a7e15459c1805da0-s.p.ec654d65.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
:HL["/_next/static/media/ea3421846039b7f3-s.p.093205c5.woff2","font",{"crossOrigin":"","type":"font/woff2"}]
:HL["/_next/static/media/effe91970fc4db64-s.p.19510058.woff2","font",{"crossOrigin":"","type":"font/woff2"}]

## Founding Story

Pierre Betouin joined Apple in 2006 and spent nine years leading the Red Team for Apple's Internet Services department — the internal group responsible for offensive security assessments, finding vulnerabilities before adversaries did, and designing protections for Apple's web-facing products. <sup><a href="https://www.ycombinator.com/companies/sqreen">[3]</a></sup> Jean-Baptiste Aviat worked alongside him in the same organization. By the time they left to found Sqreen in 2015, both had accumulated a depth of applied security knowledge that few startup founders in the space could match: they had spent nearly a decade thinking about how attackers actually exploit production web applications, not how security vendors marketed protection against them.

The founding insight was direct: the security tools available to web application developers in 2015 were architecturally wrong. Traditional Web Application Firewalls sat in front of applications, inspecting traffic without understanding application context. They generated false positives, slowed development cycles, and required dedicated security teams to operate. The founders had seen this failure mode from the inside at Apple and believed the correct approach was to instrument the application itself — to put security logic where the code ran, not in front of it.

What they built was conceptually analogous to what New Relic had done for performance monitoring: a lightweight library that developers could add in a few commands, which would then instrument application internals and surface signals to a central platform. The security analogue to APM was not a new idea in academic circles, but no company had executed it as a developer-native, self-serve product.

The founders were candid about their limitations. "We were 2 geeks passionate about security and challenging the security status quo, but we had no experience of startups," they wrote in a post-acquisition reflection. <sup><a href="https://alven.co/sqreen-a-journey-with-pierre-betouin-and-jean-baptiste-aviat/">[4]</a></sup> That self-awareness shaped their early strategy: rather than hire salespeople and build a GTM motion they didn't understand, they spent the first two years entirely on product. "For the first two years, we focused our efforts only on the product, without the sales or go to market," Betouin said. "This approach allowed us not to bias the go-to-market and the geography." <sup><a href="https://frenchtechsf.org/news/one-hour-with-sqreen/">[5]</a></sup>

The result was technically excellent but commercially slow. When Alven Capital first met the founders in January 2016 — roughly a year after founding — Sqreen had fewer than a dozen non-paying beta customers. <sup><a href="https://alven.co/sqreen-a-journey-with-pierre-betouin-and-jean-baptiste-aviat/">[6]</a></sup> Alven led the seed round anyway, betting on the founders' credentials and the clarity of the product thesis.

The decision to apply to Y Combinator in late 2017 marked a deliberate acceleration. By then, Sqreen had raised close to $3M, employed about 15 people, and had roughly 100 paying customers — a respectable European SaaS company, but not a company on a trajectory to define a global security category. "For us, it was the obvious ticket to succeed in igniting the market, but it was also a pretty daring bet," Betouin said. <sup><a href="https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/">[7]</a></sup> The standard YC terms required selling 7% of the company in exchange for the program — a meaningful dilution for a company that had already raised $3M and had real customers. Betouin described it plainly: "For us, it was a go big or go home approach." <sup><a href="https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/">[8]</a></sup>

## Timeline

- **2006** — Pierre Betouin joins Apple, eventually leading the Red Team for Apple's Internet Services department. <sup>[[9]](https://bestofshowhn.com/yc-w18/sqreen)</sup>
- **2015** — Sqreen founded in Paris by Pierre Betouin (CEO) and Jean-Baptiste Aviat (CTO). Company enters a two-year product-only development phase with no formal sales or GTM motion. <sup>[[10]](https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/)</sup>
- **January 2016** — Alven Capital first meets the founders. Sqreen has fewer than a dozen non-paying beta customers. <sup>[[6]](https://alven.co/sqreen-a-journey-with-pierre-betouin-and-jean-baptiste-aviat/)</sup>
- **April 29, 2016** — Sqreen raises $2.3M seed round led by Alven Capital, with participation from Point Nine Capital, Kima Ventures, and 50 Partners. <sup>[[11]](https://techcrunch.com/2021/02/12/datadog-to-acquire-application-security-management-platform-sqreen/)</sup>
- **September 13, 2016** — Sqreen reaches the finals of TechCrunch Disrupt SF 2016 Startup Battlefield, selected from ~1,000 applicants. <sup>[[12]](https://blog.sqreen.com/sqreen-in-the-finals-of-techcrunch-startup-battlefield/)</sup>
- **December 2017** — Sqreen applies to and is accepted into Y Combinator's Winter 2018 batch. At this point the company has ~$3M raised, ~15 employees, and ~100 customers. <sup>[[13]](https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/)</sup>
- **February 17, 2018** — TechCrunch covers Sqreen's Security Hub launch, describing it as "the IFTTT of web app security." <sup>[[14]](https://techcrunch.com/2018/02/17/sqreen-wants-to-become-the-ifttt-of-web-app-security/)</sup>
- **February 25, 2018** — Y Combinator formally invests in Sqreen as part of the W18 batch. <sup>[[15]](https://tracxn.com/d/companies/sqreen/__KpAYjTWlqDkptTv2Jjzj23rEc-Ia4YYVznfpd1jeWO8/funding-and-investors)</sup>
- **2019** — Sqreen opens a US office in San Francisco, formalizing its American market presence. <sup>[[16]](https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/)</sup>
- **April 2, 2019** — Sqreen closes $14M Series A led by Greylock Partners (Sarah Guo). Company is protecting 500+ companies. Sarah Guo joins the board. <sup>[[17]](https://www.globenewswire.com/news-release/2019/04/02/1794855/0/en/Sqreen-Closes-14-Million-Series-A-Funding-Round-Led-by-Greylock-Partners.html)</sup>
- **April 17, 2019** — Sarah Guo publishes Greylock's investment thesis, noting she issued a term sheet within four days of meeting Pierre Betouin. <sup>[[18]](https://news.greylock.com/our-investment-in-sqreen-3e49856b54b3)</sup>
- **2020** — Sqreen begins Series B fundraising process. Datadog CEO Olivier Pomel initiates informal acquisition discussions with Pierre Betouin.
- **February 11, 2021** — Datadog signs definitive agreement to acquire Sqreen. Sqreen has 800+ customers and 85 employees. MarketScreener reports acquisition price of ~$220M (unconfirmed officially). <sup>[[1]](https://www.marketscreener.com/quote/stock/DATADOG-INC-65956839/news/Datadog-Inc-completed-the-acquisition-of-Sqreen-SAS-33444339/)</sup>
- **April 12, 2021** — Datadog completes acquisition of Sqreen. Financial terms not officially disclosed. Jean-Baptiste Aviat joins Datadog. <sup>[[19]](https://www.datadoghq.com/about/latest-news/press-releases/datadog-completes-acquisition-of-sqreen/)</sup>

## What They Built

Sqreen's product was built around a single architectural insight: security belongs inside the application, not in front of it.

The core component was a microagent — a lightweight library that developers added to their application in a few commands, without modifying application code. Once installed, the agent instrumented the application's internal execution: it hooked into database calls, HTTP request handlers, authentication flows, and other critical code paths to observe what was actually happening at runtime. <sup><a href="https://bestofshowhn.com/yc-w18/sqreen">[20]</a></sup> The agent supported six languages: Ruby, Node.js, PHP, Go, Java, and Python — covering the majority of modern web application stacks. <sup><a href="https://bestofshowhn.com/yc-w18/sqreen">[21]</a></sup>

This architecture enabled two capabilities that traditional tools could not provide. First, Runtime Application Self-Protection (RASP): because the agent lived inside the application, it could detect an attack in the context of the specific code being executed — not just by inspecting network traffic patterns — and block it before it caused damage. A SQL injection attempt, for example, could be caught at the moment the malicious query was about to be executed, with full knowledge of the application's intent. Second, an in-app Web Application Firewall (WAF): unlike a network-layer WAF that inspects raw HTTP traffic, Sqreen's WAF understood the application's parsed request context, dramatically reducing false positives. <sup><a href="https://www.datadoghq.com/about/latest-news/press-releases/datadog-signs-definitive-agreement-to-acquire-sqreen/">[22]</a></sup>

The Security Hub, launched in early 2018 during the YC batch, was the product's most visible evolution. It presented security capabilities as modular, one-click-enable plugins — SQL injection protection, XSS protection, bot activity detection, account takeover protection, and more. TechCrunch's framing of it as "the IFTTT of web app security" captured the UX intent: security as composable, self-serve modules rather than a monolithic tool requiring a dedicated security team to configure. <sup><a href="https://techcrunch.com/2018/02/17/sqreen-wants-to-become-the-ifttt-of-web-app-security/">[14]</a></sup> Sqreen coined the category name "Application Security Management (ASM)" to describe this unified approach. <sup><a href="https://www.crunchbase.com/organization/sqreen">[23]</a></sup>

The developer experience was deliberately frictionless. A developer could add the Sqreen agent to a Ruby on Rails application, for example, by adding a single gem to their Gemfile and setting an environment variable with their API key. No infrastructure changes, no network reconfiguration, no security team involvement required. This stood in direct contrast to the incumbent approach: deploying a traditional WAF required routing traffic through a new network layer, configuring rules, tuning false positives, and ongoing maintenance by security specialists.

The product's central dashboard aggregated security events across all instrumented applications, surfacing attack timelines, blocked requests, anomalous user behavior, and vulnerability reports. This observability layer — a unified view of security signals across the application fleet — was the feature that most directly overlapped with what Datadog was building in its own platform.

What made Sqreen different from alternatives was not any single capability but the combination of deployment simplicity, runtime context, and developer-native UX. Contrast Security offered similar RASP capabilities but targeted enterprise security teams with a more complex deployment model. Traditional WAF vendors like Imperva and Cloudflare operated at the network layer and lacked application-internal context. Sqreen occupied the intersection of developer tooling and security capability — a position that was genuinely novel in 2015 but increasingly contested by 2020.

## Market Position

### Target Customers

Sqreen's primary customers were engineering-led companies — SaaS businesses, digital-native enterprises, and developer-forward organizations that shipped software continuously and could not tolerate the friction of traditional security tooling. The customer list at the time of the Series A included Algolia, BlaBlaCar, Front, Toptal, Triplebyte, Mindbody, and Le Monde. <sup><a href="https://techcrunch.com/2018/02/17/sqreen-wants-to-become-the-ifttt-of-web-app-security/">[24]</a></sup> These were companies with strong engineering cultures, often European in origin or with European roots, and typically in the 50–500 employee range — large enough to have real security concerns but small enough that a dedicated security team was not yet standard.

The buyer was the developer or engineering lead, not the CISO. This was a deliberate positioning choice: Sqreen's self-serve, agent-based model bypassed the traditional enterprise security procurement cycle. The tradeoff was that developer-led adoption, while faster to initiate, is harder to expand into large enterprise contracts where security budgets are controlled by security teams and procurement processes are formal.

### Market Size

The application security market was large and growing. Greylock's Sarah Guo, writing at the time of the Series A, characterized the incumbent market as "outdated and complex with approaches that don't work in production, slow down app development, and are expensive to use and maintain." <sup><a href="https://techstartups.com/2019/04/02/sqreen-startup-founded-apple-security-veterans-raises-14-million-series-round-protect-companies-using-asm-platform/">[25]</a></sup> The global WAF market alone was valued at several billion dollars by 2019, and the broader application security market — including RASP, DAST, SAST, and runtime protection — was larger still. Sqreen's self-defined category of Application Security Management was an attempt to consolidate multiple point solutions into a single platform, which, if successful, would have addressed a substantial portion of that spend.

The structural challenge was that the market was bifurcated: large enterprises bought from established vendors (Imperva, F5, Akamai) through security team procurement, while smaller companies often used nothing at all or relied on cloud provider defaults. Sqreen's developer-native approach was best suited to the middle — companies large enough to care about security but small enough that developers still controlled tooling decisions.

### Competition

Sqreen competed on two dimensions simultaneously: against legacy security vendors on product quality, and against observability platforms on distribution reach.

Against legacy vendors — Imperva, F5, Akamai, and Cloudflare on the WAF side; Contrast Security and Veracode on the RASP/application security side — Sqreen had a genuine product advantage. Its in-app architecture provided richer context, lower false positive rates, and dramatically simpler deployment. Greylock's investment thesis was built on this gap. The incumbents had distribution and enterprise relationships, but their products were architecturally mismatched to the developer-led, continuous-deployment world that Sqreen was built for.

Against observability platforms, the competitive dynamic was structurally different. Datadog, New Relic, and Dynatrace were already deploying agents into the same applications Sqreen was targeting. They had existing customer relationships, billing relationships, and agent distribution at scale. Adding security capabilities to an existing observability agent was a natural product extension — one that required no new deployment motion from the customer. Sqreen's entire go-to-market advantage (frictionless agent installation) evaporated the moment an observability platform added security to its existing agent.

This is the structural dynamic that made Sqreen's independent path difficult regardless of execution quality. The company was competing on a dimension — agent distribution — where observability incumbents had a compounding advantage: every new Datadog customer was a potential Sqreen customer that Datadog could capture without a separate sales motion. Sqreen needed to build its own agent distribution from scratch, customer by customer, while Datadog could extend security to its existing 14,000+ customers (at the time of the acquisition) with a product update.

The competitive map, in retrospect, had Sqreen positioned correctly on product depth but structurally disadvantaged on distribution reach — and in infrastructure software, distribution tends to win over time.

## Business Model

Sqreen operated as a SaaS subscription business, charging companies for access to the platform and its security modules. Pricing details were not publicly disclosed, and the company never released revenue figures directly.

The only available revenue estimate comes from GetLatka, which reported approximately $7.9M in revenue at the time of acquisition in early 2021. <sup><a href="https://getlatka.com/companies/sqreen">[26]</a></sup> This figure is low-confidence and unverified — GetLatka's methodology relies on founder interviews and estimates, not audited financials. It should be treated as directional only.

If the $7.9M figure is approximately correct, and Sqreen had 800 customers at acquisition, <sup><a href="https://www.ycombinator.com/companies/sqreen">[27]</a></sup> the implied average revenue per customer was roughly $10,000 annually. This is consistent with a mid-market developer tool sold on a per-application or per-seat basis, and suggests Sqreen had not yet successfully moved upmarket into large enterprise contracts where application security budgets are measured in six figures.

Estimating burn rate: with 85–120 employees at acquisition and a San Francisco office, annual operating costs were likely in the range of $12–18M (assuming average fully-loaded cost of $150K–$180K per employee, plus infrastructure and overhead). Against estimated revenue of ~$8M, this implies the company was burning $4–10M annually at the time of acquisition — a range consistent with a Series A company preparing to raise a Series B to fund growth. This is an inference from public headcount and industry cost benchmarks, not a reported figure.

The company never disclosed revenue publicly. The absence of revenue disclosure, combined with the decision to sell rather than raise a Series B, is consistent with a business that had strong product-market fit but had not yet achieved the revenue scale — typically $15–25M ARR — that would make a Series B straightforward in the 2020–2021 market.

## Traction

Sqreen's customer growth followed a consistent but not hyperbolic trajectory:

- **January 2016**: Fewer than a dozen non-paying beta customers. <sup><a href="https://alven.co/sqreen-a-journey-with-pierre-betouin-and-jean-baptiste-aviat/">[6]</a></sup>
- **End of 2017** (pre-YC): Approximately 100 paying customers. <sup><a href="https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/">[13]</a></sup>
- **April 2019** (Series A): 500+ companies protected. <sup><a href="https://www.globenewswire.com/news-release/2019/04/02/1794855/0/en/Sqreen-Closes-14-Million-Series-A-Funding-Round-Led-by-Greylock-Partners.html">[28]</a></sup>
- **February 2021** (acquisition): 800+ companies protected. <sup><a href="https://www.ycombinator.com/companies/sqreen">[27]</a></sup>

The growth from 500 to 800 customers over roughly 22 months (April 2019 to February 2021) represents a 60% increase — meaningful, but not the 3–5x growth that typically characterizes a Series B-ready SaaS company. The rate of net new customer additions appears to have slowed between the Series A and acquisition, though without churn data it is impossible to assess whether this reflects a demand problem or a deliberate shift toward larger, higher-value accounts.

The customer list was credible. Algolia, BlaBlaCar, Front, and Toptal were all well-regarded, engineering-forward companies — the kind of reference customers that validate product quality and developer adoption. <sup><a href="https://techcrunch.com/2018/02/17/sqreen-wants-to-become-the-ifttt-of-web-app-security/">[24]</a></sup> The European concentration of early customers (BlaBlaCar, Le Monde, Algolia) reflects the company's Paris origins and the delayed US market entry.

Sqreen's RASP module was described in the Series A press release as "the most broadly deployed in the world." <sup><a href="https://www.globenewswire.com/news-release/2019/04/02/1794855/0/en/Sqreen-Closes-14-Million-Series-A-Funding-Round-Led-by-Greylock-Partners.html">[29]</a></sup> This claim comes from a company press release and is unverified, but it is consistent with the product's developer-native, self-serve distribution model, which would naturally produce broader deployment than enterprise-only competitors.

Employee headcount grew from approximately 15 at YC (early 2018) to 85–120 at acquisition (early 2021). <sup><a href="https://www.ycombinator.com/companies/sqreen">[30]</a></sup> The discrepancy between the 85-employee figure in the Datadog press release and the 120-employee figure in the YC database likely reflects different measurement dates or methodologies.

## Post-Mortem

Sqreen was not a failed company in the conventional sense — it was acquired at a reported price that likely returned strong multiples to investors, and its technology became the foundation for a major product line at Datadog. But it did fail to achieve its stated ambition: to become the defining independent platform for application security management. Understanding why requires separating the company-level decisions from the structural market dynamics that constrained the independent path.

### Primary Cause: The Agent Distribution Problem

The most important structural constraint on Sqreen's independence was one the founders could not solve through better execution: they were building a product whose deployment model was identical to that of much larger platforms that were already inside their target customers.

Sqreen's go-to-market motion required convincing a developer to install a new agent in their application. Datadog's go-to-market motion for its security product required convincing an existing customer — one already running a Datadog agent — to enable a new feature. These are not equivalent sales motions. The first requires a new relationship, a new procurement decision, and a new deployment. The second requires a checkbox.

By the time Sqreen was preparing its Series B in 2020, Datadog had over 14,000 customers running its observability agent. Every one of those customers was a potential Sqreen customer that Datadog could reach with a product update. Sqreen had 500–800 customers and needed to grow that base organically, one developer at a time.

Pierre Betouin acknowledged this dynamic directly when explaining the acquisition decision: "We were also aware that we would do it much faster and more surely together than alone." <sup><a href="https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/">[31]</a></sup> The "more surely" is the telling phrase — it implies that the standalone path carried meaningful execution risk, not just timing risk.

Sqreen's attempted remedy was the YC bet: use the program to accelerate US market entry, build brand credibility, and establish a customer base large enough to defend against platform encroachment. The bet produced real results — the Series A, the US office, the credible customer list — but the pace of customer acquisition (roughly 300 net new customers over 22 months post-Series A) was not fast enough to establish the distribution moat that would have made Sqreen difficult to displace.

### Secondary Cause: Delayed US Market Entry

Sqreen was founded in Paris in 2015 and did not open a US office until 2019 — four years after founding. <sup><a href="https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/">[16]</a></sup> For a developer tool targeting the global SaaS market, this was a significant delay. The largest concentration of potential customers — US-based SaaS companies — was not the primary focus during the company's formative years.

The two-year product-only phase (2015–2017) was a deliberate choice that Betouin defended as preventing geographic and market bias. <sup><a href="https://frenchtechsf.org/news/one-hour-with-sqreen/">[5]</a></sup> The logic is coherent: building a sales motion before understanding the product's natural fit risks optimizing for the wrong customer segment. But the practical consequence was that Sqreen spent its most formative years building a European customer base in a market where the largest enterprise security budgets, the most influential developer communities, and the most important analyst relationships were all in the United States.

By the time Sqreen arrived in San Francisco in earnest — temporarily for YC in early 2018, permanently in 2019 — Datadog had already established itself as the dominant observability platform for US SaaS companies. The window for Sqreen to build a comparable distribution footprint in the US before observability platforms entered security was narrowing.

The attempted remedy was YC: Betouin moved half his team from Paris to San Francisco for the program, a signal of genuine commitment to the US market. <sup><a href="https://news.greylock.com/our-investment-in-sqreen-3e49856b54b3">[32]</a></sup> The Series A followed, and the US office was formalized. But the four-year head start that European-paced growth had given competitors in the US market was not recoverable in 18 months.

### Tertiary Cause: The Feature-vs-Platform Structural Risk

Sqreen's product was architecturally a feature of an observability platform, not a standalone platform in its own right. This is not a criticism of the product — it was a genuinely excellent feature, and the founders recognized the category they were creating. But the history of infrastructure software suggests that features which are most valuable when combined with other telemetry data tend to get absorbed by the platforms that own that telemetry.

Application security signals — attack attempts, anomalous user behavior, SQL injection patterns — are most actionable when correlated with performance data, error rates, and distributed traces. A developer investigating a security incident wants to see the attack in the context of the application's behavior at that moment. Sqreen's standalone platform could provide security context; Datadog's unified platform could provide security context plus everything else. The integrated product was structurally more valuable than the standalone product, and Datadog had the distribution to deliver it to customers who were already paying for the observability layer.

Jean-Baptiste Aviat's framing at acquisition was candid: "When we started Sqreen in 2015, an acquisition wasn't on the table. We were about to raise our Series B when a unique opportunity came through." <sup><a href="https://events.tech.rocks/summit-2021/en/speaker/b1045dd4-fdea-eb11-b563-a085fc3e7f45/jean-baptiste-aviat">[33]</a></sup> The "unique opportunity" language suggests the founders recognized that the convergence of observability and security — which they had identified as a market trend — made the Datadog offer more compelling than the Series B path, not because the company was struggling, but because the standalone path was becoming structurally harder as the market consolidated around unified platforms.

### What Worked

It is worth noting what Sqreen got right, because the post-mortem is not a story of poor execution. The founders built a technically superior product in a real market. They attracted credible investors (Greylock issued a term sheet in four days). They built a customer base of 800 companies including recognizable logos. They identified the convergence of observability and security before it became consensus. And they sold at a price that, if the $220M figure is accurate, represented a strong outcome for everyone involved. The failure was not to build a bad company — it was to build a company whose core value proposition was more powerful inside a platform than outside it.

## Key Lessons

- **Architectural similarity to a larger platform is both a validation signal and an acquisition signal.** Sqreen's microagent architecture was validated by the fact that it looked exactly like what Datadog was building for observability. But that same similarity meant Datadog could extend its existing agent to cover security without a new deployment motion — eliminating Sqreen's primary go-to-market advantage. When a startup's core architecture is a natural extension of an incumbent's existing infrastructure, the startup should treat that incumbent as both a potential acquirer and a potential competitor, and build distribution defensibility accordingly.

- **A two-year product-only phase in a European market delayed the US distribution race that ultimately determined the outcome.** Sqreen's founders spent 2015–2017 building product without sales or GTM, producing a technically excellent tool but a European-concentrated customer base. By the time Sqreen arrived in the US in earnest (2018–2019), Datadog had already established deep roots in the US SaaS developer community. The product-first strategy was defensible in isolation, but it meant Sqreen was fighting for US distribution at the same time observability platforms were beginning to enter security — the worst possible timing for a standalone application security company.

- **YC as a US market accelerant works, but the dilution math changes when you already have product-market fit.** Sqreen entered YC with $3M raised, 15 employees, and 100 customers — a company that had already demonstrated product-market fit. Selling 7% for YC access was a deliberate "go big or go home" bet on US market entry, not a seed-stage validation play. The bet produced a $14M Series A from Greylock within a year. But it also signals that the founders understood their organic growth rate was insufficient to win the US market before larger platforms arrived — a correct diagnosis, even if the remedy was ultimately not enough.

- **The convergence of observability and security was visible to Sqreen's founders before it was consensus — and they acted on it correctly by selling, not by fighting it.** Betouin and Aviat identified the market convergence between observability and security as a key factor in their acquisition decision. <sup><a href="https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/">[34]</a></sup> That convergence is now the defining trend in cloud-native security (CNAPP, unified security platforms). Founders who correctly read a structural market shift and position their company accordingly — even if that means selling rather than raising — demonstrate a form of strategic clarity that is undervalued in startup post-mortems that treat acquisition as failure.

- **In infrastructure security, the buyer's existing tooling relationships constrain the addressable market more than product quality does.** Sqreen's product was technically superior to what observability platforms offered natively in 2019–2020. But Greylock's own investment thesis acknowledged that the incumbent market "doesn't work in production." <sup><a href="https://techstartups.com/2019/04/02/sqreen-startup-founded-apple-security-veterans-raises-14-million-series-round-protect-companies-using-asm-platform/">[25]</a></sup> The problem was not that customers preferred inferior products — it was that customers who already had Datadog agents deployed faced near-zero switching costs to adopt Datadog's security features, regardless of how much better Sqreen's standalone product was. Product quality is necessary but not sufficient when distribution incumbents can match "good enough" at zero marginal deployment cost.

## Sources

1. [MarketScreener — Datadog completes acquisition of Sqreen SAS](https://www.marketscreener.com/quote/stock/DATADOG-INC-65956839/news/Datadog-Inc-completed-the-acquisition-of-Sqreen-SAS-33444339/)
2. [Jean-Baptiste Aviat LinkedIn profile](https://www.linkedin.com/in/jeanbaptisteaviat/)
3. [Y Combinator — Sqreen company profile](https://www.ycombinator.com/companies/sqreen)
4. [Alven Capital — Sqreen: A Journey with Pierre Betouin and Jean-Baptiste Aviat](https://alven.co/sqreen-a-journey-with-pierre-betouin-and-jean-baptiste-aviat/)
5. [French Tech SF — One Hour With Sqreen](https://frenchtechsf.org/news/one-hour-with-sqreen/)
6. [French Tech SF — One Hour With Pierre Betouin, Co-Founder & CEO of Sqreen](https://frenchtechsf.org/news/one-hour-with-pierre-betouin-co-founder-ceo-of-sqreen/)
7. [Best of Show HN — Sqreen YC W18](https://bestofshowhn.com/yc-w18/sqreen)
8. [TechCrunch — Datadog to acquire application security management platform Sqreen](https://techcrunch.com/2021/02/12/datadog-to-acquire-application-security-management-platform-sqreen/)
9. [Sqreen Blog — Sqreen in the Finals of TechCrunch Startup Battlefield](https://blog.sqreen.com/sqreen-in-the-finals-of-techcrunch-startup-battlefield/)
10. [TechCrunch — Sqreen wants to become the IFTTT of web app security](https://techcrunch.com/2018/02/17/sqreen-wants-to-become-the-ifttt-of-web-app-security/)
11. [Tracxn — Sqreen funding and investors](https://tracxn.com/d/companies/sqreen/__KpAYjTWlqDkptTv2Jjzj23rEc-Ia4YYVznfpd1jeWO8/funding-and-investors)
12. [GlobeNewswire — Sqreen Closes $14 Million Series A Funding Round Led by Greylock Partners](https://www.globenewswire.com/news-release/2019/04/02/1794855/0/en/Sqreen-Closes-14-Million-Series-A-Funding-Round-Led-by-Greylock-Partners.html)
13. [Greylock — Our Investment in Sqreen (Sarah Guo)](https://news.greylock.com/our-investment-in-sqreen-3e49856b54b3)
14. [Datadog — Datadog Completes Acquisition of Sqreen](https://www.datadoghq.com/about/latest-news/press-releases/datadog-completes-acquisition-of-sqreen/)
15. [Datadog — Datadog Signs Definitive Agreement to Acquire Sqreen](https://www.datadoghq.com/about/latest-news/press-releases/datadog-signs-definitive-agreement-to-acquire-sqreen/)
16. [Crunchbase — Sqreen organization profile](https://www.crunchbase.com/organization/sqreen)
17. [TechStartups — Sqreen raises $14M Series A (Sarah Guo quote)](https://techstartups.com/2019/04/02/sqreen-startup-founded-apple-security-veterans-raises-14-million-series-round-protect-companies-using-asm-platform/)
18. [GetLatka — Sqreen revenue data](https://getlatka.com/companies/sqreen)
19. [Tech.Rocks Summit 2021 — Jean-Baptiste Aviat speaker profile](https://events.tech.rocks/summit-2021/en/speaker/b1045dd4-fdea-eb11-b563-a085fc3e7f45/jean-baptiste-aviat)
20. [SiliconAngle — Datadog acquires Timber, Sqreen](https://siliconangle.com/2021/02/11/datadog-acquires-timber-sqreen-reports-lower-expected-guidance/)
21. [Blossom Capital — Sqreen portfolio](https://www.blossomcap.com/portfolio/squreen)
22. [CBInsights — Sqreen company profile](https://www.cbinsights.com/company/sqreen)
