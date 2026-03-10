# Research Report: Tydo

## Overview

Tydo was a direct-to-consumer analytics platform founded in 2020 by Manav Kohli and Scott Sonneborn under the legal entity PolyOps, Inc. Operating out of the Y Combinator S20 batch, the company built a no-code dashboard that consolidated fragmented DTC data — Shopify orders, Facebook Ads spend, Klaviyo email metrics, Amazon sales — into a single interface for lean brand teams that lacked in-house data engineers. Over four years, it cycled through at least three distinct product identities: PolyOps, Tydo, and finally Tydo.ai, each representing a repositioning attempt in an increasingly crowded market.

Tydo failed because it built an aggregation layer on top of platforms that had strong commercial incentives to absorb exactly that functionality natively. The no-code analytics dashboard was a real product solving a real problem, but it was structurally exposed: every data source Tydo connected to was also a potential competitor, and the DTC macro environment that created Tydo's initial tailwind reversed sharply in 2022–2023.

Y Combinator lists Tydo as inactive. <sup><a href="https://www.ycombinator.com/companies/polyops">[6]</a></sup> Co-founder Manav Kohli has since moved to Ribbit Capital. <sup><a href="https://www.linkedin.com/in/manavkohli/">[24]</a></sup> No acquisition or acqui-hire has been publicly disclosed, and no founder post-mortem has been published. The company appears to have wound down quietly, its runway exhausted without a path to a Series A.

<report-gallery>
<media-image src="https://saaslandingpage.com/wp-content/uploads/2022/06/tydo-380x475.png" alt="Tydo SaaS landing page screenshot" caption="Tydo's landing page circa 2022 — the clean, no-code positioning that attracted 500+ DTC brands before platform consolidation eroded the value proposition."></media-image>
</report-gallery>

## Founding Story

Manav Kohli and Scott Sonneborn both attended Claremont McKenna College, a connection that almost certainly predates the company and provided the trust foundation for a co-founder relationship. <sup><a href="https://wellfound.com/company/tydo/people">[4]</a></sup> <sup><a href="https://wellfound.com/company/tydo/people">[5]</a></sup>

Kohli came to the company with a technical background. He had worked as a software engineer at Intuit and then as a senior software engineer at Thanx, a loyalty and customer engagement platform for restaurants and retailers. <sup><a href="https://wellfound.com/company/tydo/people">[4]</a></sup> That experience at Thanx — a company that sat at the intersection of consumer data, merchant analytics, and retention — appears to have shaped Kohli's understanding of how fragmented and inaccessible data was for operators of consumer brands. He was not a domain specialist in DTC e-commerce, but he understood the data infrastructure problem from the merchant side.

Sonneborn brought a different profile: Goldman Sachs for financial rigor, Equinix for enterprise operations exposure, and then Pawp — a pet health startup where he served as co-founder and head of strategy and operations. <sup><a href="https://wellfound.com/company/tydo/people">[5]</a></sup> Pawp gave Sonneborn direct experience building a DTC brand from scratch, including the operational pain of stitching together data from multiple platforms to understand customer acquisition costs and retention. That firsthand frustration with fragmented analytics is the most plausible origin story for Tydo, though neither founder has published a detailed account of the founding insight.

The company was incorporated as PolyOps, Inc. in Delaware, with an initial San Francisco address. <sup><a href="https://app.tydo.com/legal_customer_terms.pdf">[2]</a></sup> The PolyOps name suggests the original framing was broader — "poly operations," covering multiple operational data streams — before the team narrowed to the Tydo brand and a more specific DTC analytics identity. The TYDO trademark was formally filed on March 11, 2021, roughly seven months after the YC batch, indicating the rebrand happened during or shortly after the program. <sup><a href="https://trademarks.justia.com/905/73/tydo-90573303.html">[3]</a></sup>

The timing of the founding was not incidental. The YC S20 batch ran during the early months of COVID-19, a period when e-commerce adoption accelerated dramatically and DTC brands were scaling faster than their operational infrastructure could support. Shopify's GMV grew 96% in 2020. <sup><a href="https://www.ycombinator.com/companies/polyops">[1]</a></sup> The problem Tydo was solving — helping lean DTC teams understand their data without hiring a data team — was acutely felt by a rapidly expanding customer base. YC's backing provided not just capital but access to a portfolio of DTC-adjacent companies that could serve as early customers and reference accounts.

No public founding interview or origin story from either Kohli or Sonneborn has been identified. The absence of a founder narrative is itself notable: companies that achieve strong product-market fit tend to generate founder storytelling. Tydo's silence on this front is consistent with a company that found partial but not durable fit.

## Timeline

- **2020** — Tydo founded by Manav Kohli and Scott Sonneborn as PolyOps, Inc. <sup>[[0]](https://www.ycombinator.com/companies/polyops)</sup>
- **August 2020** — Participates in Y Combinator S20 batch; seed funding round closes (amount undisclosed). <sup>[[1]](https://www.ycombinator.com/companies/polyops)</sup> <sup>[[13]](https://tracxn.com/d/companies/tydo/__m9fVwxgJUbFMfCTR5GCgNTDfwE8ncLWxDHodt6y7xKY)</sup>
- **March 11, 2021** — TYDO trademark filed by PolyOps, Inc., formalizing the brand transition from PolyOps to Tydo. <sup>[[3]](https://trademarks.justia.com/905/73/tydo-90573303.html)</sup>
- **April 2021** — Apple releases iOS 14.5, introducing App Tracking Transparency. Facebook Ads attribution data — a core Tydo data source — is materially degraded across the DTC industry.
- **Late 2021** — Third-party YC directory records a venture round, with total funding reported at approximately $12.05M (unconfirmed, low confidence). <sup>[[17]](http://www.ycombinatorcompanies.com/company/polyops)</sup>
- **2022** — DTC sector correction begins: rising customer acquisition costs, post-iOS 14.5 signal loss, and pullback in DTC venture funding compress the addressable market.
- **October 1, 2022** — Tydo raises a second seed round from Sugar Capital and Unpopular Ventures (amount undisclosed). <sup>[[14]](https://www.bouncewatch.com/explore/startup/tydo)</sup>
- **2023** — Tydo launches GA4 integration, indicating active product development through Google's Universal Analytics sunset. <sup>[[28]](https://www.tydo.com/)</sup> Product repositioned as Tydo.ai, adding AI-powered personalization agents.
- **2024** — YC lists Tydo as "Inactive." <sup>[[6]](https://www.ycombinator.com/companies/polyops)</sup> Manav Kohli joins Ribbit Capital. <sup>[[24]](https://www.linkedin.com/in/manavkohli/)</sup>

## What They Built

Tydo's core product was a no-code analytics dashboard for direct-to-consumer brands. The central problem it addressed was fragmentation: a typical DTC brand in 2020–2022 ran its storefront on Shopify, acquired customers through Facebook and Instagram ads, retained them via Klaviyo email campaigns, and sold on Amazon as a secondary channel. Each platform produced its own metrics in its own interface, with no native way to see a unified view of profitability, customer acquisition cost, or return on ad spend across all channels simultaneously.

Tydo solved this by connecting directly to each platform's API and pulling the data into a single dashboard. <sup><a href="https://www.tydo.com/">[10]</a></sup> The integrations covered Shopify, Amazon, Facebook Ads, Klaviyo, SMS platforms, and loyalty apps. <sup><a href="https://www.tydo.com/">[25]</a></sup> Critically, the setup required no developers and no custom integrations — a brand operator could connect their accounts and see consolidated metrics within minutes. <sup><a href="https://www.datanyze.com/companies/polyops/540386537">[8]</a></sup>

The specific metrics Tydo surfaced were chosen for operational relevance rather than vanity. Order-level and SKU-level profitability in real time let operators see which products were actually making money after ad spend. Automatic CAC (customer acquisition cost) and ROAS (return on ad spend) reporting eliminated the manual spreadsheet work that most lean teams were doing weekly or monthly. <sup><a href="https://www.datanyze.com/companies/polyops/540386537">[8]</a></sup>

A distinctive product feature was "Report Cards by Tydo" — automated performance summaries delivered via email on a daily, weekly, or monthly cadence. <sup><a href="https://www.crunchbase.com/organization/polyops">[11]</a></sup> This was a clever distribution mechanism: rather than requiring operators to log into another dashboard, Tydo pushed the insights to where operators already were. It reduced activation friction and created a habit loop that kept the product top-of-mind without requiring active engagement.

The product evolved in two meaningful directions over time. First, "Tydo Custom" emerged as a higher-touch offering: bespoke data warehouse setup, custom reports, and AI-powered insights tailored to specific brand needs. <sup><a href="https://www.crunchbase.com/organization/tydo">[12]</a></sup> This was a services-adjacent product that suggested the core SaaS offering was not sufficient for larger or more complex customers. Second, the final repositioning as Tydo.ai moved the product from analytics (reporting what happened) toward action (recommending or automating what to do next), including personalization agents for commerce. <sup><a href="https://www.tydo.com/">[9]</a></sup>

The GA4 integration launch — timed to Google's forced migration from Universal Analytics — demonstrated that the team was tracking platform changes and shipping product in response. <sup><a href="https://www.tydo.com/">[28]</a></sup> But it also illustrated the fundamental dynamic: Tydo's product roadmap was perpetually reactive to decisions made by the platforms it depended on.

What made Tydo different from alternatives in its early period was the combination of DTC-specific metric design, no-code setup, and the Report Cards delivery mechanism. General-purpose BI tools like Looker or Tableau required data engineering to configure. Shopify's native analytics were Shopify-only. Tydo's value was the cross-platform synthesis, delivered without technical overhead.

## Market Position

### Target Customers

Tydo's primary customer was the lean DTC brand: a company doing meaningful e-commerce revenue — likely $1M to $20M annually — but without a dedicated data analyst or data engineer on staff. <sup><a href="https://www.zoominfo.com/c/polyops-inc/540386537">[27]</a></sup> The client list confirms this positioning: Buck Mason (menswear), Salt & Stone (skincare), Madhappy (streetwear), and New Era (headwear) are all DTC-native or DTC-forward brands with recognizable consumer identities but lean operational teams. <sup><a href="https://www.tydo.com/">[19]</a></sup>

This customer profile had a specific pain point — fragmented data, no engineering resources — and a specific willingness to pay: SaaS subscription pricing in the range where a single analyst hire would cost more annually than the tool. The customer testimonial from Ornella Siso of idyl — "I'm saving at least 15 to 20 hours a week with Tydo" — captures the value proposition precisely. <sup><a href="https://www.linkedin.com/company/tydo">[21]</a></sup> The product was replacing manual spreadsheet work, not competing with enterprise data infrastructure.

### Market Size

The DTC analytics market was large and growing in 2020–2021, driven by the broader e-commerce acceleration. Shopify alone processed over $175 billion in GMV in 2021. The addressable market for analytics tooling serving that ecosystem was substantial. However, the specific segment Tydo targeted — brands too small for enterprise BI but too sophisticated for native platform analytics — was narrower and more volatile than the headline numbers suggested.

The DTC sector correction of 2022–2023 compressed this market materially. Rising Facebook advertising costs (partly driven by iOS 14.5 signal loss), increased competition from Amazon, and a pullback in DTC venture funding caused many of Tydo's target customers to reduce headcount and cut software subscriptions. The brands most likely to churn from a $500–$2,000/month analytics tool are exactly the lean, growth-stage DTC brands that Tydo served.

### Competition

Tydo operated in a structurally difficult competitive position. Tracxn identified 721 active competitors in the DTC analytics space, including established players like Nielsen and Marin Software. <sup><a href="https://tracxn.com/d/companies/tydo/__m9fVwxgJUbFMfCTR5GCgNTDfwE8ncLWxDHodt6y7xKY">[26]</a></sup> But the more important competitive dynamic was not horizontal — other analytics startups — but vertical: the platforms Tydo depended on for data.

Shopify, Klaviyo, and Meta each had strong incentives to expand their own analytics capabilities. Shopify's native analytics improved substantially between 2020 and 2023, adding cohort analysis, customer lifetime value reporting, and attribution features that directly overlapped with Tydo's core offering. Klaviyo, which went public in 2023, built out its own revenue attribution and cross-channel reporting. Meta's Ads Manager, despite iOS 14.5 disruption, continued to invest in its own measurement tools.

The competitive map along the axes that mattered most — distribution reach versus product depth — was unfavorable for Tydo. Shopify had distribution to every Shopify merchant by default; Tydo had to acquire each customer individually. Klaviyo had deep email data that no third party could replicate with the same fidelity. Tydo's product depth was real but not defensible: any feature it built on top of a platform's API could be replicated by the platform itself, with better data access and zero marginal distribution cost.

Point-solution competitors like Triple Whale (founded 2021) and Northbeam (founded 2019) also targeted the same DTC analytics buyer with better-funded, more focused products. Triple Whale raised $25M in 2022 and built a larger brand following in the DTC community. These competitors had similar structural vulnerabilities but more capital to sustain the fight.

## Business Model

Tydo operated as a SaaS subscription business, charging DTC brands a recurring fee for access to its analytics dashboard and integrations. The company never publicly disclosed its pricing tiers, making precise unit economics analysis impossible.

The "Tydo Custom" offering — bespoke data warehouse setup and custom reporting — suggests a second revenue stream that was services-adjacent rather than pure SaaS. <sup><a href="https://www.crunchbase.com/organization/tydo">[12]</a></sup> This is a common pattern for analytics companies that struggle to scale the self-serve product: high-touch engagements generate revenue but compress margins and distract engineering resources.

The company never disclosed revenue publicly. The $2M ARR figure comes from a single LinkedIn profile of a team member, not a press release or investor statement, and is undated. <sup><a href="https://wellfound.com/company/tydo/people">[20]</a></sup> Third-party revenue models from Growjo and Datanyze estimate $1.3M–$1.7M, which is lower than the $2M ARR claim — suggesting either the $2M figure was a peak that subsequently declined, or the third-party models are understated. <sup><a href="https://growjo.com/company/Tydo">[29]</a></sup>

*Inferred burn rate (labeled as estimate):* If total funding was approximately $5M (the Tracxn figure, which is the most conservative and arguably most credible for a company that never raised a Series A) <sup><a href="https://tracxn.com/d/companies/tydo/__m9fVwxgJUbFMfCTR5GCgNTDfwE8ncLWxDHodt6y7xKY">[15]</a></sup> and the team peaked at 14 employees <sup><a href="https://www.ycombinator.com/companies/polyops">[22]</a></sup>, annual burn at a San Francisco/LA blended rate would be approximately $2.5M–$3.5M per year. At $2M ARR and that burn rate, the company was likely consuming $500K–$1.5M in net cash annually — a runway problem that a Series A would need to solve. No Series A was raised.

## Traction

Tydo achieved meaningful early traction by the standards of a seed-stage SaaS company. The platform served 500+ brand clients, including recognizable DTC names: Buck Mason, Salt & Stone, New Era, and Madhappy. <sup><a href="https://www.tydo.com/">[19]</a></sup> These are not placeholder logos — they are brands with real consumer followings and operational sophistication, suggesting Tydo's product cleared a genuine quality bar.

The $2M ARR milestone, reported by a team member on their professional profile, represents real but modest scale for a company that raised institutional capital from Greylock and YC. <sup><a href="https://wellfound.com/company/tydo/people">[20]</a></sup> <sup><a href="https://www.ycombinator.com/companies/polyops/jobs/hfgLB6f-senior-data-analyst">[18]</a></sup> At $2M ARR with 500+ brands, the implied average revenue per customer is approximately $4,000 annually — consistent with a mid-tier SaaS subscription but not with the kind of expansion revenue that drives efficient growth.

Customer testimonials indicate genuine product value. The 15–20 hours per week time savings cited by one founder-customer is a credible and specific claim, not a generic endorsement. <sup><a href="https://www.linkedin.com/company/tydo">[21]</a></sup> This suggests the product worked for users who adopted it — the failure was not product quality but retention, expansion, and competitive durability.

The gap between these traction signals and ultimate inactivity points toward a unit economics problem: the company could acquire customers and deliver value, but could not retain them at sufficient rates or expand revenue per customer fast enough to reach the scale needed for a Series A.

## Post-Mortem

### Primary Cause: Platform Dependency Without a Defensible Moat

Tydo's fundamental structural problem was that it built its entire product on top of APIs controlled by companies with strong incentives to absorb its functionality. Every data source Tydo connected to — Shopify, Facebook Ads, Klaviyo, Amazon — was simultaneously a partner and a latent competitor. <sup><a href="https://www.tydo.com/">[10]</a></sup>

This is not a novel failure mode, but it played out with particular force in DTC analytics. Shopify's native analytics improved substantially between 2020 and 2023. By 2022, Shopify had added cohort analysis, customer LTV reporting, and multi-channel attribution features that directly overlapped with Tydo's core dashboard. Klaviyo, which filed for IPO in 2023, built out cross-channel revenue attribution as a core product feature — the same functionality Tydo was charging separately for. Meta's Ads Manager, despite the iOS 14.5 disruption, continued investing in its own measurement suite.

The competitive dynamic along the axis that mattered most — distribution — was structurally unfavorable. Shopify reached every Shopify merchant by default, with no customer acquisition cost. Tydo had to find, convince, and onboard each customer individually. When Shopify added a feature that covered 70% of what Tydo did, the marginal value of Tydo's subscription dropped for every Shopify merchant simultaneously. There was no equivalent event that could expand Tydo's distribution at scale.

Tydo attempted to address this by moving up the value chain — from reporting (what happened) to action (what to do), culminating in the Tydo.ai repositioning with personalization agents. <sup><a href="https://www.tydo.com/">[9]</a></sup> This was directionally correct: the further a product moves from data aggregation toward proprietary insight and automated action, the harder it is for platforms to replicate. But the pivot came late, was underfunded relative to AI-native competitors entering the same space in 2023, and required a fundamentally different product and go-to-market motion than the dashboard business Tydo had built.

### Secondary Cause: Macro Deterioration of the Core Customer Segment

Tydo's target customer — lean DTC brands without in-house data teams — was acutely exposed to the macro deterioration of 2022–2023. The DTC sector correction was driven by three compounding forces: rising customer acquisition costs on Facebook and Instagram, the iOS 14.5 privacy changes that degraded attribution data across the industry, and a pullback in DTC venture funding that caused brands to cut software subscriptions.

The iOS 14.5 change, released in April 2021, is particularly relevant to Tydo's specific product. Facebook Ads attribution — a core data source that Tydo aggregated and reported on — became materially less reliable after iOS 14.5. Brands that had relied on Facebook ROAS data to make spending decisions found that the numbers were increasingly noisy. If Tydo's CAC and ROAS reporting was built on degraded Facebook data, the perceived value of that reporting declined even if Tydo's product itself was unchanged.

The company raised its second seed round in October 2022 — a difficult fundraising environment — suggesting investors still believed in the thesis at that point. <sup><a href="https://www.bouncewatch.com/explore/startup/tydo">[14]</a></sup> But the DTC correction was already underway, and the brands most likely to churn from a recurring analytics subscription are exactly the growth-stage DTC companies that Tydo served. There is no public data on Tydo's churn rate, but the combination of a deteriorating customer base and a commoditizing product makes elevated churn the most plausible explanation for the gap between the $2M ARR milestone and ultimate inactivity.

### Tertiary Cause: Insufficient Revenue Scale to Justify a Series A

Tydo raised at least two seed rounds and had a credible investor roster — YC, Greylock, Alt Capital, Sugar Capital. <sup><a href="https://www.ycombinator.com/companies/polyops/jobs/hfgLB6f-senior-data-analyst">[18]</a></sup> But no Series A was ever announced. The $2M ARR figure, if accurate, represents a real but insufficient milestone for a Series A in 2022–2023, when the bar for growth-stage SaaS had risen substantially. <sup><a href="https://wellfound.com/company/tydo/people">[20]</a></sup>

The "Tydo Custom" services offering — bespoke data warehouse setup and custom reports — is a signal that the core SaaS product was not generating sufficient revenue on its own. <sup><a href="https://www.crunchbase.com/organization/tydo">[12]</a></sup> Services revenue is harder to scale, compresses margins, and is typically a symptom of a product that hasn't found a repeatable, self-serve growth motion. If Tydo was supplementing SaaS revenue with consulting engagements, the effective ARR multiple on the business would have been lower than a pure SaaS company, making a Series A raise harder.

The October 2022 seed round likely provided 12–18 months of runway, which would exhaust sometime in mid-to-late 2024 — consistent with the YC "Inactive" designation. Without a Series A, the company had no path to the scale needed to compete with better-funded point solutions like Triple Whale or to fund the AI pivot that might have created a defensible position.

### Structural Industry Explanation: DTC Analytics Is a Feature, Not a Company

The deepest lesson from Tydo's failure is structural rather than executional. DTC analytics aggregation — pulling Shopify, Facebook, and Klaviyo data into a single view — is a feature that every major platform in the DTC stack has an incentive to build natively. It is not a standalone business category with durable winner-take-all dynamics. The category rewards the company with the best distribution (Shopify), the best data (Klaviyo), or the most capital (Triple Whale, which raised $25M to out-market competitors). Tydo had none of these advantages at sufficient scale.

The three product pivots — PolyOps to Tydo to Tydo.ai — reflect a team that understood this problem and tried to solve it by moving up the value chain. <sup><a href="https://www.tydo.com/">[9]</a></sup> The AI pivot was the right strategic instinct: proprietary AI models trained on cross-brand data could create a defensible position that pure aggregation cannot. But executing that pivot required capital, time, and a customer base willing to share data at scale — none of which Tydo had in sufficient quantity by 2023.

## Key Lessons

- **Building on platform APIs without a data moat is a structural trap, not just a strategic risk.** Tydo's entire product was built on APIs controlled by Shopify, Meta, and Klaviyo — companies that had both the incentive and the capability to absorb Tydo's functionality natively. When Shopify expanded its analytics suite between 2021 and 2023, it didn't need to acquire Tydo; it simply shipped features that reduced Tydo's marginal value to every Shopify merchant simultaneously. Any analytics company building on top of a dominant platform needs a proprietary data layer — cross-brand benchmarks, predictive models, or network effects — that the platform cannot replicate from its own data alone.

- **The "no-code for lean teams" positioning is a customer acquisition strategy, not a retention strategy.** Tydo's no-code, no-engineer-required pitch was effective at attracting DTC operators who were drowning in spreadsheets. But lean teams are also the most price-sensitive and most likely to churn when the macro environment deteriorates or when the platform they're already paying for adds a "good enough" native feature. Tydo's customer testimonials showed genuine time savings, but time savings alone don't create switching costs. A stickier product would have embedded itself in the customer's data infrastructure — owning the warehouse, not just the dashboard.

- **A services revenue stream (Tydo Custom) is a warning sign, not a growth strategy.** When Tydo launched "Tydo Custom" — bespoke data warehouse setup and custom reports — it was signaling that the core SaaS product couldn't serve more complex customers without human intervention. This is a common pattern in analytics startups: the self-serve product works for simple use cases, but the customers with the most willingness to pay require customization that doesn't scale. Tydo's attempt to serve both segments likely diluted engineering focus without generating the ARR multiple needed for a Series A.

- **Macro tailwinds that create a market can reverse and destroy it.** Tydo launched into the COVID-era DTC boom of 2020, when Shopify GMV was growing 96% annually and lean DTC brands were proliferating. By 2022, the same customer segment was contracting: iOS 14.5 had degraded Facebook attribution data (a core Tydo data source), DTC venture funding had pulled back, and brands were cutting software subscriptions. Tydo's $2M ARR milestone — achieved during the boom — likely peaked and declined as the customer base contracted, leaving the company with insufficient revenue to justify a Series A in a tighter market.

- **The AI pivot was directionally correct but structurally too late.** Tydo's repositioning as Tydo.ai — moving from reporting to AI-powered personalization agents — was the right strategic response to commoditization pressure on the dashboard layer. Cross-brand AI models trained on unified DTC data could create genuine defensibility. But the pivot required capital, a larger customer data set, and time that Tydo didn't have by 2023, when well-funded AI-native entrants were entering the same space. The lesson is not that the pivot was wrong, but that the window for executing it had closed before Tydo had the resources to compete.

## Sources

1. [Y Combinator — Tydo/PolyOps Company Page](https://www.ycombinator.com/companies/polyops)
2. [Tydo Legal Customer Terms (PolyOps, Inc.)](https://app.tydo.com/legal_customer_terms.pdf)
3. [Justia Trademarks — TYDO Trademark Filing](https://trademarks.justia.com/905/73/tydo-90573303.html)
4. [Wellfound — Tydo Team Page](https://wellfound.com/company/tydo/people)
5. [Crunchbase — PolyOps/Tydo Organization](https://www.crunchbase.com/organization/polyops)
6. [Crunchbase — Tydo Organization](https://www.crunchbase.com/organization/tydo)
7. [Datanyze — PolyOps Company Profile](https://www.datanyze.com/companies/polyops/540386537)
8. [Tydo Website (archived)](https://www.tydo.com/)
9. [Tracxn — Tydo Company Profile](https://tracxn.com/d/companies/tydo/__m9fVwxgJUbFMfCTR5GCgNTDfwE8ncLWxDHodt6y7xKY)
10. [BounceWatch — Tydo Startup Profile](https://www.bouncewatch.com/explore/startup/tydo)
11. [PitchBook — Tydo Company Profile](https://pitchbook.com/profiles/company/439511-23)
12. [YC Companies Directory — PolyOps](http://www.ycombinatorcompanies.com/company/polyops)
13. [YC Job Listing — Tydo Senior Data Analyst (Investor List)](https://www.ycombinator.com/companies/polyops/jobs/hfgLB6f-senior-data-analyst)
14. [LinkedIn — Manav Kohli](https://www.linkedin.com/in/manavkohli/)
15. [LinkedIn — Tydo Company Page](https://www.linkedin.com/company/tydo)
16. [ZoomInfo — PolyOps, Inc.](https://www.zoominfo.com/c/polyops-inc/540386537)
17. [Growjo — Tydo Revenue Estimate](https://growjo.com/company/Tydo)
18. [SaaS Landing Page — Tydo Example](https://saaslandingpage.com/wp-content/uploads/2022/06/tydo-380x475.png)
