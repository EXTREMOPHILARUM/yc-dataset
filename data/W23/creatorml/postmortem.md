# Research Report: CreatorML

## Overview

CreatorML was a New York-based B2B SaaS company founded in 2022 by Charles Weill, a former Google Research machine learning lead, that used ML models to help YouTube creators predict how many views a title or thumbnail change would generate before publishing.Accepted into Y Combinator's Winter 2023 batch and backed by ~$500K from YC, Amino Capital, Goodwater Capital, and Pioneer Fund, the company built a technically sophisticated product suite targeting YouTubers with over 100,000 subscribers.

Despite landing credible enterprise customers and generating what appears to be meaningful early revenue, CreatorML was listed as inactive on YC's platform by 2024, with founder Charles Weill subsequently joining xAI as a Member of Technical Staff.The company's failure reflects a structural mismatch between the capital required to sustain an ML-infrastructure-heavy product and the ceiling imposed by a deliberately narrow target market.

<report-gallery>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/4ae1530922f24f10b74c13bc79afe2ba17da15c1.jpg" alt="CreatorML: Foundation Model for Human Attention | Y Combinator" caption="CreatorML's Y Combinator profile photo — the company's official face during its Winter 2023 batch, when founder Charles Weill brought his Google Research pedigree to bear on a deceptively simple question: could an ML model tell a YouTuber whether their thumbnail would flop before they ever hit publish?"></media-image>
<media-image src="https://files.atlas.so/IljbezPQuiLiYGUP6xfQ_Screenshot%20(1050).png" alt="Understanding Your Subscription Plan | CreatorML" caption="A screenshot from CreatorML's subscription management interface — a glimpse of the product in its final form, built for creators with 100K+ subscribers who were willing to pay for algorithmic certainty in an uncertain platform economy. The polished UI belied the structural tension underneath: an ML-heavy product chasing a market too narrow to sustain it."></media-image>
</report-gallery>

## Founding Story

Charles Weill founded CreatorML in 2022 under the legal entity Antifragile Research Inc., incorporated in New York. <sup><a href="https://www.ycombinator.com/companies/creatorml">[1]</a></sup> <sup><a href="https://creatorml.com/register/">[2]</a></sup> He came to the company as a solo founder — a deliberate choice, though the rationale for not recruiting a co-founder was never publicly stated.

Weill's credentials were exceptional for this specific problem. He spent seven years as a technical lead in applied machine learning at Google Research, working directly on Cloud AutoML, Ads, Search, and YouTube algorithms. <sup><a href="https://www.ycombinator.com/companies/creatorml">[3]</a></sup> He also held an M.Eng in Computer Science from Cornell University. <sup><a href="https://www.crunchbase.com/person/charles-weill">[4]</a></sup> Few people in the world had deeper institutional knowledge of how YouTube's recommendation engine actually worked — and Weill was building a product designed to help creators game exactly that system.

The founding insight did not come from a whiteboard exercise. It came from Twitter. Weill had been posting analyses of YouTube analytics data as a side interest, and he noticed that some of the platform's largest creators began following him. As he later described it: *"I realized that I found a pain point when I began tweeting about simple analyses of YouTube analytics data, and many of the biggest YouTubers in the industry began following me."* <sup><a href="https://www.ycombinator.com/companies/creatorml">[5]</a></sup> This organic signal — major creators seeking out a random ML engineer's analytics posts — suggested genuine, unmet demand rather than a manufactured hypothesis.

Weill was also a part-time YouTube creator himself, which gave him first-hand exposure to the anxiety that drives creator behavior: the uncertainty of not knowing whether a title or thumbnail will perform before committing to it. <sup><a href="https://www.ycombinator.com/companies/creatorml">[6]</a></sup> That dual perspective — insider knowledge of the algorithm and lived experience of the creator workflow — shaped the product's initial design.

The early period was financially precarious. Weill's LinkedIn activity references waking up to a $15,000 bill on his personal credit card while self-funding the startup, describing it as "the thanks I get for self funding my startup." <sup><a href="https://www.linkedin.com/in/cweill/">[7]</a></sup> He bootstrapped through this period before securing institutional backing.

CreatorML was accepted into Y Combinator's Winter 2023 batch, providing both capital and validation. <sup><a href="https://www.ycombinator.com/companies/creatorml">[8]</a></sup> The company's Twitter account had launched in September 2022, and the core view-prediction product was already live before the YC batch began — meaning Weill entered the program with a working product and early customer signals rather than a pitch deck.

---

## Timeline

- **2022** — Charles Weill founds CreatorML (incorporated as Antifragile Research Inc.) in New York after discovering creator demand through YouTube analytics tweets <sup>[[1]](https://www.ycombinator.com/companies/creatorml)</sup>

- **September 2022** — CreatorML's Twitter/X account (@CreatorML\_) is created, marking the company's first public presence <sup>[[9]](https://x.com/CreatorML_)</sup>

<media-tweet url="https://x.com/CharlesWeill/status/1547047030949912579" author="@CharlesWeill" date="2022-07-12" text="Ever wished you could predict how many Views a video would get before you upload to YouTube? 📈🤔 Well, you asked for it, so as of today CreatorML can now predict Views over a 28 day period! 🎉 Try it out for yourself: http://creatorml.com"></media-tweet>

- **November 18, 2022** — CreatorML launches its Chrome Extension, which tracks title and thumbnail changes and shows their effect on views directly on YouTube <sup>[[10]](https://x.com/CreatorML_)</sup>

- **Early 2023** — CreatorML participates in Y Combinator's Winter 2023 batch <sup>[[8]](https://www.ycombinator.com/companies/creatorml)</sup>

<media-hn url="https://www.ycombinator.com/launches/IEp-creatorml-ml-powered-predictive-analytics-for-youtube-creators" title="Launch YC: CreatorML – ML-Powered Predictive Analytics for YouTube Creators" points="" comments=""></media-hn>

- **January 31, 2023** — Weill promotes the CreatorML Chrome Extension to the YC community and broader audience

<media-tweet url="https://twitter.com/CharlesWeill/status/1620478528352555009" author="@CharlesWeill" date="2023-01-31" text="Get the CreatorML Extension"></media-tweet>

- **April 1, 2023** — CBInsights records a Seed VC funding round with Pioneer Fund as investor <sup>[[11]](https://www.cbinsights.com/company/creatorml/financials)</sup>

- **April 14, 2023** — Third-party YC W23 batch analysis published, describing CreatorML's value proposition to the broader startup community <sup>[[12]](https://chris-takes.beehiiv.com/p/ycombinator-w23-ai-startups)</sup>

- **May 5, 2023** — LinkedIn records CreatorML's last funding round as a Pre-Seed, closing the known fundraising history of the company <sup>[[13]](https://www.linkedin.com/company/creatorml)</sup>

- **December 27, 2023** — Third-party directory listing references CreatorML with named customers including Promoting Sounds and Astralis R6, suggesting the product remains active <sup>[[14]](https://ytcreator.tools/directory/creatorml/)</sup>

- **February 8, 2024** — CreatorML's pinned tweet promotes a 7-day free trial — the last confirmed public-facing commercial activity <sup>[[9]](https://x.com/CreatorML_)</sup>

- **July 24, 2024** — Charles Weill publicly announces the shutdown of CreatorML on X

<media-tweet url="https://x.com/CharlesWeill/status/1816062407547981885" author="@CharlesWeill" date="2024-07-24" text="I'm shutting down @CreatorML_"></media-tweet>

- **2024** — YC lists CreatorML as "Inactive"; Charles Weill joins xAI as a Member of Technical Staff <sup>[[15]](https://www.ycombinator.com/companies/creatorml)</sup> <sup>[[16]](https://github.com/cweill)</sup>

---

## What They Built

CreatorML's core product was a machine learning-powered view predictor. Before a creator published a video — or before they changed the title or thumbnail of an existing one — the tool would forecast how many views that specific combination of title, thumbnail, and topic would generate over a 28-day window. <sup><a href="https://www.linkedin.com/company/creatorml">[17]</a></sup> This was the central value proposition: replacing the guesswork of packaging decisions with a quantified prediction.

For a YouTube creator, the practical workflow looked like this. A creator would input a proposed video title and thumbnail into CreatorML's interface. The system would analyze those inputs against its model — trained on historical YouTube performance data — and return a predicted view count. The creator could then iterate on the title or thumbnail, comparing predicted outcomes before committing to any version. The same logic applied to existing videos: a creator could test whether retitling or re-thumbnailing an older video would recover or boost its performance.

The product suite expanded beyond the core predictor into several adjacent tools. The Title Generator produced title suggestions calibrated to a creator's niche and audience. The YouTube Video Idea Generator surfaced topic ideas based on trending and high-performing content in a creator's category. <sup><a href="https://www.crunchbase.com/organization/creatorml">[18]</a></sup> The Predictor tool allowed creators to simulate different combinations of title, thumbnail, and video length before recording began — pushing the decision support earlier in the production process. <sup><a href="https://www.crunchbase.com/organization/creatorml">[19]</a></sup> The Outlier-Video Database gave creators access to a curated set of videos that dramatically outperformed their channel's baseline, serving as inspiration and benchmarking data.

The Chrome Extension, launched November 18, 2022, was the most strategically interesting piece of the product. <sup><a href="https://x.com/CreatorML_">[10]</a></sup> Rather than requiring creators to visit a separate dashboard, the extension embedded CreatorML's data directly into the YouTube interface creators already used daily. It tracked when creators changed a video's title or thumbnail and displayed the measurable effect on views — creating a feedback loop that made the value of the product visible in real time, inside the creator's existing workflow.

The explicit target customer was YouTubers with over 100,000 subscribers, for whom CreatorML offered custom onboarding for the view predictor. <sup><a href="https://www.ycombinator.com/companies/creatorml">[20]</a></sup> This was a deliberate ICP choice: larger channels have more historical data to train against, more to lose from a bad packaging decision, and more budget to pay for optimization tools.

The stated long-term vision was a "complete predictive ecosystem" guiding creators through every step of the creative process — from initial topic selection through title and thumbnail optimization. <sup><a href="https://www.ycombinator.com/companies/creatorml">[21]</a></sup> The individual tools were positioned as a wedge into a broader platform, not as standalone utilities.

What differentiated CreatorML from generic analytics tools was the specificity of the prediction. YouTube's native Studio analytics show historical performance but do not forecast future outcomes for untested configurations. CreatorML's model was designed to answer a counterfactual question: *what would happen if I changed this?* That capability — built by someone who had spent seven years working on YouTube's own algorithms — was genuinely novel at the time of launch.

---

## Market Position

### Target Customers

CreatorML targeted YouTube creators with over 100,000 subscribers. <sup><a href="https://www.ycombinator.com/companies/creatorml">[20]</a></sup> This segment is characterized by creators who have already validated their content format and audience, generate meaningful ad revenue, and face real financial consequences from underperforming videos. For these creators, a single video that fails to reach its potential can represent thousands of dollars in lost ad revenue — making optimization tools economically rational purchases.

Named customers included The Infographics Show (13.8M+ subscribers), Promoting Sounds (2.9M subscribers), and Astralis R6's content strategist. <sup><a href="https://www.linkedin.com/company/creatorml">[22]</a></sup> <sup><a href="https://ytcreator.tools/directory/creatorml/">[14]</a></sup> This customer profile — large, professionally managed channels with dedicated content strategy resources — suggests CreatorML was successfully reaching the upper tier of its target segment.

### Market Size

The 100K+ subscriber threshold creates a structurally bounded addressable market. Estimates of channels at this scale globally range from approximately 50,000 to 100,000. Even at the high end, this is a small absolute number for a SaaS business. If CreatorML charged $100–$500 per month per customer (pricing was never publicly disclosed), capturing 1,000 customers would generate $1.2M–$6M in annual recurring revenue — a ceiling that limits the company's attractiveness to growth-stage investors expecting venture-scale returns.

The broader creator economy tooling market was growing rapidly in 2022–2024, with platforms like TubeBuddy, VidIQ, and Spotter serving the long tail of smaller creators. But CreatorML's deliberate positioning at the top of the subscriber distribution — where the product's ML predictions would be most accurate and most valuable — meant it was not competing for the mass market. This was a defensible niche strategy, but it came with a hard ceiling on total addressable market.

### Competition

CreatorML's most direct competitors were TubeBuddy and VidIQ, both of which offered keyword research, title suggestions, and thumbnail A/B testing tools for YouTube creators. Both had significantly larger user bases, established distribution through the YouTube creator community, and broader feature sets targeting creators at all subscriber levels. Neither, however, offered the specific capability that CreatorML was built around: a forward-looking view prediction model trained on YouTube performance data by someone with direct institutional knowledge of the platform's algorithm.

The competitive risk that materialized during CreatorML's operating period was the rapid expansion of general-purpose AI tools into content optimization. By 2023–2024, large language models were being integrated into creator tools at scale, compressing the differentiation window for specialized ML products. YouTube also continued improving its native Studio analytics, potentially reducing the perceived gap between free first-party tools and paid third-party solutions. No direct evidence confirms that either of these dynamics was the proximate cause of CreatorML's shutdown, but both represent structural headwinds the company would have faced in sustaining differentiation.

---

## Business Model

CreatorML operated as a B2B SaaS product with a free trial entry point. The company's Twitter account promoted a 7-day free trial as late as February 2024, <sup><a href="https://x.com/CreatorML_">[9]</a></sup> suggesting a freemium or trial-to-paid conversion model. Specific pricing tiers were never publicly disclosed.

The company targeted larger channels (100K+ subscribers) for custom onboarding of the view predictor, <sup><a href="https://www.ycombinator.com/companies/creatorml">[20]</a></sup> suggesting a tiered structure where enterprise or high-subscriber accounts received white-glove treatment — likely at higher price points — while smaller creators may have accessed the tool through self-serve tiers.

The Chrome Extension served as a distribution mechanism rather than a direct revenue driver, embedding CreatorML's value into the YouTube interface to generate awareness and conversion. Revenue would have flowed from paid subscriptions to the core prediction and analytics platform. No information is available on pricing, average contract value, or the ratio of free to paid users.

---

## Traction

CreatorML's most concrete traction signal was its enterprise customer roster. The Infographics Show, with 13.8M+ subscribers, was a named customer — a credible reference account that validated the product's appeal at the top of the creator market. <sup><a href="https://www.linkedin.com/company/creatorml">[22]</a></sup> Promoting Sounds (2.9M subscribers) and Astralis R6's content strategist were also named, suggesting a pattern of mid-to-large creator adoption rather than isolated wins. <sup><a href="https://ytcreator.tools/directory/creatorml/">[14]</a></sup>

Weill's LinkedIn activity references bootstrapping to $50K MRR as a solo founder with one enterprise customer and three more in the pipeline. <sup><a href="https://www.linkedin.com/in/cweill/">[23]</a></sup> If this figure refers to CreatorML — the context suggests it does, though this cannot be confirmed with certainty — it represents meaningful early revenue for a pre-seed stage company. $50K MRR implies $600K in annualized recurring revenue, which would exceed the company's total recorded funding.

The Twitter/X account had 1,298 followers as of its last active period, and the pinned post dated February 8, 2024 was still promoting a 7-day free trial — indicating the product remained commercially active into early 2024, roughly 18 months after launch. <sup><a href="https://x.com/CreatorML_">[9]</a></sup>

Employee count data is inconsistent across sources: YC lists 6 employees, PitchBook records 3. <sup><a href="https://www.ycombinator.com/companies/creatorml">[24]</a></sup> <sup><a href="https://pitchbook.com/profiles/company/523185-31">[25]</a></sup> The discrepancy likely reflects different snapshot dates rather than a data error, suggesting the team grew modestly after the YC batch.

---

## Post-Mortem

CreatorML shut down in July 2024, approximately two years after founding. Charles Weill announced the closure in a single tweet: *"I'm shutting down @CreatorML\_"* <sup><a href="https://github.com/cweill">[16]</a></sup> No public post-mortem, investor statement, or detailed explanation followed. What can be reconstructed from available data points to a combination of capital constraints, market ceiling limitations, and the structural difficulty of sustaining an ML-infrastructure-heavy product as a solo founder.

### Insufficient Capital for the Product's Requirements

CreatorML raised approximately $500K in total funding from YC, Amino Capital, Goodwater Capital, and Pioneer Fund, with the last recorded funding event in April–May 2023. <sup><a href="https://pitchbook.com/profiles/company/523185-31">[26]</a></sup> <sup><a href="https://www.linkedin.com/company/creatorml">[27]</a></sup> No follow-on round was raised after the YC batch concluded.

For a product built on ML infrastructure — requiring ongoing model training, data pipeline maintenance, and compute costs — $500K represents extremely limited runway, particularly for a team that appears to have grown to at least three to six people. The financial pressure was evident even before institutional funding arrived: Weill's LinkedIn references a $15,000 personal credit card bill from self-funding the startup's early months. <sup><a href="https://www.linkedin.com/in/cweill/">[7]</a></sup>

The absence of a Series A or meaningful seed extension after the YC batch is the most significant structural signal in the company's history. YC's Demo Day in Spring 2023 would have been the natural moment to raise a follow-on round. The fact that no such round materialized — despite a credible founder, a working product, and named enterprise customers — suggests either that the revenue trajectory did not support a growth-stage valuation, or that investors were not convinced the market ceiling justified venture-scale investment.

Without additional capital, Weill would have faced an impossible allocation problem: maintaining ML infrastructure, acquiring new customers, supporting existing enterprise accounts, and continuing product development simultaneously, on a budget that could not sustain all four.

### A Structurally Small Addressable Market

CreatorML's deliberate choice to target YouTubers with 100K+ subscribers created a high-quality but numerically small customer pool. <sup><a href="https://www.ycombinator.com/companies/creatorml">[20]</a></sup> Globally, the number of YouTube channels at this subscriber threshold is estimated in the range of 50,000 to 100,000. Even assuming aggressive penetration of this segment, the revenue ceiling for a SaaS product in this niche is difficult to scale to venture-scale outcomes.

This was not a strategic error per se — targeting the highest-value customers first is a rational wedge strategy. But it created a fundraising problem. Investors evaluating a Series A would have needed to believe that CreatorML could either expand downmarket (serving smaller creators, where the ML model's accuracy would be lower and the willingness to pay would be reduced) or expand the product scope significantly (moving beyond YouTube, or into adjacent creator monetization tools). Neither path was clearly articulated in the company's public positioning, and neither would have been easy to execute with the existing capital base.

The $50K MRR figure referenced on Weill's LinkedIn, if accurate, represents a real business — but not one that grows to a $50M ARR company without either a much larger addressable market or a significant expansion of the product's scope. <sup><a href="https://www.linkedin.com/in/cweill/">[23]</a></sup>

### Solo Founding Under ML Infrastructure Demands

Building and maintaining a machine learning product requires ongoing investment in data pipelines, model retraining, infrastructure reliability, and feature development — work that typically requires a team. Weill was a solo founder with exceptional technical credentials, but the operational demands of running an ML SaaS product while simultaneously managing sales, customer success, and fundraising are difficult to sustain for any individual over an extended period.

The YC company page lists 6 employees, and PitchBook records 3 — suggesting Weill did hire, but the team remained small relative to the product's infrastructure requirements. <sup><a href="https://www.ycombinator.com/companies/creatorml">[24]</a></sup> <sup><a href="https://pitchbook.com/profiles/company/523185-31">[25]</a></sup> With ~$500K in total funding and a small team, the company had limited capacity to absorb the compounding demands of enterprise customer support, product development, and model maintenance simultaneously.

### Competitive Compression and Platform Risk

By 2023–2024, the creator tools market was experiencing rapid consolidation and feature expansion from well-funded incumbents. TubeBuddy and VidIQ were integrating AI-powered features into their existing large user bases. General-purpose LLMs were being deployed for title and thumbnail optimization at near-zero marginal cost. The specific capability that made CreatorML distinctive — a forward-looking view prediction model built by a former YouTube algorithm engineer — became harder to defend as the broader market caught up on AI-powered content optimization.

Additionally, any product that depends on YouTube's data ecosystem carries platform risk. Changes to YouTube's API access policies, rate limits, or data availability could degrade the model's accuracy or the Chrome Extension's functionality without warning. No evidence confirms that a specific API change harmed CreatorML, but this structural dependency represents a risk that would have been visible to any investor evaluating the business.

### The Exit Signal

Weill's move to xAI as a Member of Technical Staff after the shutdown indicates a clean, voluntary exit rather than an acqui-hire or distressed sale. <sup><a href="https://github.com/cweill">[16]</a></sup> The product does not appear to have been acquired or open-sourced. The company wound down quietly, with no public post-mortem and no announcement beyond a single tweet. This pattern — a technically strong founder with a working product and real customers, shutting down without a public explanation and moving to a high-profile AI role — is consistent with a founder who concluded that the path to scale was not available with the capital and market conditions at hand, rather than one who ran out of money unexpectedly.

---

## Key Lessons

- **Founder-market fit is necessary but not sufficient for venture-scale outcomes.** Weill was arguably one of the most qualified people in the world to build this specific product — seven years working on YouTube's algorithms, combined with first-hand experience as a creator. <sup><a href="https://www.ycombinator.com/companies/creatorml">[3]</a></sup> That credential set helped him build a technically credible product and land enterprise customers. It did not resolve the structural ceiling imposed by a small addressable market or the capital constraints of a $500K raise. Domain expertise accelerates product development; it does not substitute for market size or capital adequacy.

- **Deliberately narrow ICPs require a credible expansion path to attract growth-stage capital.** Targeting 100K+ subscriber YouTubers was a rational quality-over-quantity decision that produced credible early customers. <sup><a href="https://www.ycombinator.com/companies/creatorml">[20]</a></sup> But without a publicly articulated path to expanding the addressable market — downmarket to smaller creators, across platforms, or into adjacent creator economy tools — the strategy that won early customers may have been the same strategy that prevented a Series A. Niche wedge strategies need a visible second act.

- **ML infrastructure products require capital proportional to their maintenance burden.** A view prediction model trained on YouTube data requires ongoing retraining, data pipeline maintenance, and compute costs that do not scale linearly with revenue. <sup><a href="https://pitchbook.com/profiles/company/523185-31">[26]</a></sup> Raising ~$500K for a product with these characteristics created a structural mismatch between the capital available and the operational demands of keeping the product competitive. Solo founders building ML products need either significantly more capital or a much simpler infrastructure footprint.

- **Distribution embedded in existing workflows is a strong signal, but conversion to paid revenue is what matters.** The Chrome Extension strategy — putting CreatorML's data directly inside YouTube's interface — was a smart approach to reducing friction and demonstrating value in context. <sup><a href="https://x.com/CreatorML_">[10]</a></sup> Whether that distribution translated into paid conversions at sufficient rates to sustain the business is unknown, but the gap between a useful free tool and a recurring revenue business is where many creator economy products have stalled.

- **Platform dependency is a structural risk that compounds over time.** Any product whose core value proposition depends on a single platform's data, API access, or algorithm behavior is exposed to unilateral changes by that platform. YouTube's continued investment in its own native analytics tools, combined with potential API policy changes, created a risk surface that would have been difficult to hedge without significant product diversification — which, in turn, would have required more capital than CreatorML raised.

---

## Sources

1. [YC Company Page – CreatorML](https://www.ycombinator.com/companies/creatorml)
2. [CreatorML Registration Page (Antifragile Research Inc.)](https://creatorml.com/register/)
3. [Crunchbase – Charles Weill](https://www.crunchbase.com/person/charles-weill)
4. [CreatorML LinkedIn Company Page](https://www.linkedin.com/company/creatorml)
5. [Charles Weill LinkedIn Profile](https://www.linkedin.com/in/cweill/)
6. [CreatorML Twitter/X Account (@CreatorML\_)](https://x.com/CreatorML_)
7. [CBInsights – CreatorML Financials](https://www.cbinsights.com/company/creatorml/financials)
8. [PitchBook – CreatorML Profile](https://pitchbook.com/profiles/company/523185-31)
9. [Crunchbase – CreatorML Organization](https://www.crunchbase.com/organization/creatorml)
10. [ytcreator.tools – CreatorML Directory Listing](https://ytcreator.tools/directory/creatorml/)
11. [Chris Takes Newsletter – YC W23 AI Startups Analysis](https://chris-takes.beehiiv.com/p/ycombinator-w23-ai-startups)
12. [Charles Weill GitHub Profile](https://github.com/cweill)
13. [Datanyze – CreatorML](https://www.datanyze.com/companies/creatorml-yc-w23/1323054233)
14. [YC Launch Page – CreatorML](https://www.ycombinator.com/launches/IEp-creatorml-ml-powered-predictive-analytics-for-youtube-creators)
15. [Charles Weill Tweet – View Prediction Launch (July 12, 2022)](https://x.com/CharlesWeill/status/1547047030949912579)
16. [Charles Weill Tweet – Shutdown Announcement (July 24, 2024)](https://x.com/CharlesWeill/status/1816062407547981885)
17. [Charles Weill Tweet – Chrome Extension Promotion (January 31, 2023)](https://twitter.com/CharlesWeill/status/1620478528352555009)
