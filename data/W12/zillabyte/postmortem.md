# Research Report: Zillabyte

## Overview

Zillabyte was a San Francisco-based startup that graduated from Y Combinator's Winter 2012 batch with a bold pitch: bring Palantir-grade intelligence to sales teams.The company built a web-crawling platform that matched businesses with prospects by analyzing billions of web pages, then pivoted in August 2014 to become a cloud infrastructure platform for data analysis.

Neither product survived.The sales-leads application was outgunned by better-capitalized competitors including Infer, Lattice Engines, and Mintigo.

The infrastructure pivot landed Zillabyte directly in the path of Google Cloud Dataflow and Amazon Kinesis—hyperscalers with distribution advantages no seed-stage company could match.With only $1.5 million in confirmed funding, no disclosed revenue, and no acquisition, Zillabyte quietly closed around 2015. The company left behind no founder post-mortem, no shutdown announcement, and no documented acqui-hire—only a Crunchbase entry marked "permanently closed."

<report-gallery>
<media-image src="https://img-cdn.tnwcdn.com/image/tnw-blurple?filter_last=1&fit=1280%2C640&url=https%3A%2F%2Fcdn0.tnwcdn.com%2Fwp-content%2Fblogs.dir%2F1%2Ffiles%2F2013%2F03%2Flaunchfestival.jpg&signature=dfbc5f5b81bce373a88e5cfbdd1e94de" alt="The Next Web: Launch Festival 2013 winners — Zillabyte takes Enterprise prize" caption="Zillabyte's high-water mark: the 2013 LAUNCH Festival, where the startup walked away with the Best Enterprise 2.0 prize and the highest crowd-favorite score of any company at the event — 992,000 simulated points. Three months later, the $1.5M seed round would close. It was as good as it ever got."></media-image>
<media-image src="https://techcrunch.com/wp-content/uploads/2014/08/zillabyte.jpg?w=690" alt="TechCrunch article: Zillabyte Relaunches To Provide Infrastructure For Data Apps (August 2014)" caption="TechCrunch covers Zillabyte's August 2014 relaunch as a cloud infrastructure platform — a last-ditch pivot away from the crowded sales-leads market and directly into the crosshairs of Google Cloud Dataflow and Amazon Kinesis. The company would be gone within a year."></media-image>
</report-gallery>

## Founding Story

The founding of Zillabyte traces to a single weekend in July 2011, when Jake Quist and Roger Dean Huffstetler crossed paths at Renaissance Weekend, an invitation-only ideas festival for emerging leaders.<sup><a href="https://poetsandquants.com/2013/12/06/a-harvard-mba-co-founds-the-pandora-of-sales-leads/">[1]</a></sup> The pairing was unlikely on paper but coherent in practice: Quist brought deep engineering credentials, and Huffstetler brought sales experience and business training.

Quist had worked as a software engineer and tech lead at Google before leaving to start the company.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[2]</a></sup> He held an MS in Computer Science from the University of Utah.<sup><a href="https://www.slideshare.net/slideshow/zilladeck-public/16245275">[3]</a></sup> His founding insight was direct and personal. "When we left Google, we realized that data analysis outside the Googleplex kind of sucks. Big time," Quist said at the company's public debut in September 2011. "The tools available are so niche that only big enterprise can purchase them."<sup><a href="https://techcrunch.com/2011/09/30/ex-googlers-debut-zillabyte-to-let-users-easily-analyze-big-data/">[4]</a></sup>

Huffstetler arrived from a different angle. A US Marine Corps veteran who served in Iraq and Afghanistan, he earned his MBA from Harvard Business School before joining Twilio as a strategic sales manager.<sup><a href="https://poetsandquants.com/2013/12/06/a-harvard-mba-co-founds-the-pandora-of-sales-leads/">[5]</a></sup> His frustration with cold-calling at Twilio became the product's emotional core. "I used to work in sales for Twilio, and I know cold-calling sucks when you are selling technology," he said at the 2013 LAUNCH Festival. "We are taking an anecdotal understanding of sales and making it analytical."<sup><a href="https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/">[6]</a></sup>

Within two months of meeting, the pair had built enough to go public. Zillabyte debuted in September 2011 as a big-data-for-everyone platform, self-funded and in private beta.<sup><a href="https://techcrunch.com/2011/09/30/ex-googlers-debut-zillabyte-to-let-users-easily-analyze-big-data/">[7]</a></sup> The original pitch deck described the company as "the Business Genome Project"—a mission to structure the world's business information and make it actionable—and positioned the product as "the non-social complement to LinkedIn."<sup><a href="https://www.slideshare.net/slideshow/zilladeck-public/16245275">[8]</a></sup> The ambition was real, but the scope was vast enough to obscure what the company actually built first.

The team applied to Y Combinator and joined the Winter 2012 batch.<sup><a href="https://www.ycombinator.com/companies/zillabyte">[9]</a></sup> YC sharpened the pitch considerably. By Demo Day in March 2012, the sprawling "Business Genome" framing had been compressed into a single, high-concept tagline: "Palantir for salespeople."

<media-tweet url="https://twitter.com/rdhjr" author="@rdhjr" date="2016-04-21" text="Husband to @drhuffstetler. @USMC Veteran of Iraq & Afghanistan. @UnivWestGa and @HarvardHBS alum. Worked at @Twilio, founded Zillabyte."></media-tweet>

---

## Timeline

- **July 2011** — Jake Quist and Roger Huffstetler meet at Renaissance Weekend.<sup>[[1]](https://poetsandquants.com/2013/12/06/a-harvard-mba-co-founds-the-pandora-of-sales-leads/)</sup>

- **September 2011** — Zillabyte publicly debuts as a big-data analysis startup, self-funded and in private beta. Undisclosed seed round raised from Founder Friendly Labs.<sup>[[7]](https://techcrunch.com/2011/09/30/ex-googlers-debut-zillabyte-to-let-users-easily-analyze-big-data/)</sup>

- **January 2012** — Zillabyte joins Y Combinator Winter 2012 batch.<sup>[[9]](https://www.ycombinator.com/companies/zillabyte)</sup>

- **March 2012** — YC Demo Day: Zillabyte pitches as "Palantir for salespeople," describing a platform that identifies key sales leads across the web using human teams, machine learning, and big data.<sup>[[10]](https://techcrunch.com/2012/03/27/yc-demo-day-session-1/)</sup>

- **April 2012** — Second undisclosed seed round raised from Kevin Donahue and two other investors, post-Demo Day.<sup>[[11]](https://www.crunchbase.com/organization/zillabyte/company_overview/overview_timeline)</sup>

- **March 2013** — Zillabyte appears at LAUNCH Festival 2013, now pitching as "Pandora for sales leads" with a database of 2 billion pages and 11 million unique companies. Wins "Best Enterprise 2.0" award and achieves the highest crowd-favorite score of any startup at the event: 992,000 simulated points.<sup>[[12]](https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/)</sup>

- **June 2013** — Zillabyte raises a $1.5M seed round from boldstart ventures and three other investors—the company's largest and apparently final disclosed funding round.<sup>[[13]](https://www.crunchbase.com/organization/zillabyte/company_overview/overview_timeline)</sup>

- **August 2014** — Zillabyte officially relaunches as a cloud platform for data analysis, abandoning the sales-leads product. Google Cloud Dataflow and Amazon Kinesis are noted as direct competitors entering the same space.<sup>[[14]](https://techcrunch.com/2014/08/21/zillabyte-relaunch/)</sup>

- **2015** — Zillabyte ceases operations. Listed as permanently closed on Crunchbase. No acquisition confirmed.<sup>[[15]](https://www.crunchbase.com/organization/zillabyte)</sup>

- **2015** — Roger Huffstetler becomes Chief of Staff for US Congressman Seth Moulton. Jake Quist's subsequent activities are undocumented.<sup>[[16]](https://moulton.house.gov/news-stories/moulton-names-entrepreneur-and-marine-veteran-roger-dean-huffstetler-chief-of-staff/)</sup>

---

## What They Built

### Product Era 1: Sales Intelligence (2012–2014)

Zillabyte's first product solved a specific problem: sales teams waste time prospecting because they lack systematic ways to find companies that match their ideal customer profile. The solution was a web-scale matching engine.

The workflow was straightforward. A sales team described their ideal customer—industry, company size, technology stack, growth signals, or any other criteria. Zillabyte's platform then crawled the web, analyzed billions of pages, and surfaced a ranked list of companies that matched those criteria.<sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[17]</a></sup> An alert system notified users whenever a new matching prospect appeared—turning a one-time search into a continuous feed of warm leads.<sup><a href="https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/">[18]</a></sup>

By March 2013, the underlying database had grown to 2 billion crawled pages and 11 million unique company profiles.<sup><a href="https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/">[19]</a></sup> The pitch evolved from "Palantir for salespeople" at YC Demo Day in March 2012 to "Pandora for sales leads" at LAUNCH Festival a year later—the Pandora analogy emphasizing the continuous, personalized feed mechanic rather than the raw analytical power.

The original pitch deck framed the product more grandly as "the Business Genome Project"—a mission to structure all of the world's business information and make it actionable, positioned as "the non-social complement to LinkedIn."<sup><a href="https://www.slideshare.net/slideshow/zilladeck-public/16245275">[8]</a></sup> In practice, the product was a prospect-discovery tool for B2B sales teams.

What made it technically distinctive was the combination of web crawling at scale with machine learning to classify and rank companies—a combination that required building significant data infrastructure from scratch. That infrastructure investment would later become the rationale for the pivot.

### Product Era 2: Data Infrastructure Platform (2014)

In August 2014, Zillabyte relaunched as a cloud platform for data analysis, targeting what Huffstetler called "the lay developer."<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[20]</a></sup> The goal was to abstract away distributed computing infrastructure so that developers could focus on writing data models rather than managing clusters.

The platform supported Ruby, Python, and JavaScript, and offered pre-built algorithm "components" for common tasks: geocoding, fraud analysis, and web scraping.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[21]</a></sup> Users could work with both open datasets and their own private data. Critically, the platform included a crawled copy of the web as an off-the-shelf dataset—a meaningful technical asset that the team had already built for the sales product.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[22]</a></sup>

The backend, called "Motherbrain," was written in Java. The team open-sourced components including web domain crawlers and screenshot capture tools. The pivot was not a complete reinvention—it was a productization of internal tooling that already existed. But the market Zillabyte was entering had just been claimed by two of the most powerful technology companies in the world.

<media-image src="https://techcrunch.com/wp-content/uploads/2014/08/zillabyte.jpg?w=690" alt="TechCrunch article: Zillabyte Relaunches To Provide Infrastructure For Data Apps (August 2014)" caption="TechCrunch's coverage of Zillabyte's August 2014 relaunch as a cloud platform for data analysis — the company's final pivot away from sales leads, positioning itself against Amazon Kinesis and Google Cloud Dataflow."></media-image>

---

## Market Position

### Target Customers

In its first product era, Zillabyte targeted B2B sales teams at technology companies—specifically those selling to other businesses who needed a systematic way to identify and prioritize prospects. Huffstetler's own experience cold-calling at Twilio defined the archetypal user: a sales professional at a growth-stage tech company with a defined ideal customer profile but no efficient way to find matching companies at scale.

After the pivot, the target customer shifted to developers—specifically those who needed to run large-scale data analysis jobs but lacked the expertise or resources to manage distributed computing infrastructure themselves. Huffstetler described the goal as "empowering the lay developer to use distributed computing."<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[20]</a></sup> This was a broader and less defined audience than the sales-team use case.

### Market Size

The sales intelligence market was real and growing in 2012–2013. Companies were spending heavily on CRM software and increasingly on data enrichment and lead-scoring tools layered on top of it. The broader data analytics and business intelligence market was expanding rapidly as cloud infrastructure made large-scale data processing accessible to mid-market companies for the first time.

The developer infrastructure market that Zillabyte entered with its pivot was larger still—but it was a market being actively shaped by Amazon Web Services and Google Cloud Platform, both of which were investing billions in managed data services. For a seed-stage company with $1.5 million in confirmed funding, the addressable market was theoretically large but practically inaccessible without a defensible wedge.

### Competition

**Sales intelligence era:** By the time Zillabyte raised its $1.5M seed round in June 2013, the sales intelligence space had attracted significantly better-funded competitors. Infer, Lattice Engines, and Mintigo were all building predictive lead-scoring products with deeper CRM integrations and larger sales teams.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[23]</a></sup> These companies raised tens of millions of dollars—Lattice Engines alone had raised over $50 million by 2014. Zillabyte's $1.5M could not fund the data acquisition, sales team, and product development required to compete at that level.

**Infrastructure era:** The pivot brought Zillabyte into direct competition with Google Cloud Dataflow and Amazon Kinesis—both announced around the same period as the August 2014 relaunch.<sup><a href="https://www.crunchbase.com/organization/zillabyte">[24]</a></sup> Zillabyte's own Crunchbase profile acknowledged this, describing the company as "a direct competitor to these technologies." Competing with hyperscalers in managed data pipeline infrastructure—without proprietary data advantages, network effects, or switching costs—was structurally untenable for a company at Zillabyte's funding level.

---

## Business Model

Zillabyte never publicly disclosed its pricing model or revenue figures for either product era. The sales-leads product was presumably sold as a SaaS subscription to B2B sales teams, with pricing likely tied to the number of users, lead volume, or company size—consistent with how competitors like Infer and Lattice Engines structured their offerings.

The post-pivot infrastructure platform would logically have followed a consumption-based or seat-based pricing model, similar to cloud data services from AWS and Google. No pricing page, customer count, or revenue figure was ever disclosed publicly.

The company raised three rounds totaling a confirmed $1.5 million, with two earlier rounds of undisclosed size.<sup><a href="https://www.crunchbase.com/organization/zillabyte/company_overview/overview_timeline">[13]</a></sup> Investors included boldstart ventures, Mesa Ventures, Menlo Ventures, DFJ, and KEC Ventures, among others.<sup><a href="https://golden.com/wiki/Zillabyte-99B6K9G">[25]</a></sup> The absence of any Series A suggests the company either did not attempt to raise one or was unable to demonstrate the traction required to do so.

---

## Traction

Zillabyte's most concrete public validation came at the LAUNCH Festival in March 2013. The company won the "Best Enterprise 2.0" award<sup><a href="https://launch.co/blog/all-launch-festival-2013-winners-and-investment-prizes.html">[26]</a></sup> and achieved the highest crowd-favorite score of any startup at the event: 992,000 simulated crowdfunding points.<sup><a href="https://venturebeat.com/entrepreneur/and-the-winners-of-launch-are/">[27]</a></sup> A mid-festival VentureBeat report showed Zillabyte leading the leaderboard with 651,000 points before the final tally.

<media-image src="https://img-cdn.tnwcdn.com/image/tnw-blurple?filter_last=1&fit=1280%2C640&url=https%3A%2F%2Fcdn0.tnwcdn.com%2Fwp-content%2Fblogs.dir%2F1%2Ffiles%2F2013%2F03%2Flaunchfestival.jpg&signature=dfbc5f5b81bce373a88e5cfbdd1e94de" alt="The Next Web: Launch Festival 2013 winners — Zillabyte takes Enterprise prize" caption="The Next Web's announcement of the 2013 Launch Festival winners, with Zillabyte taking the top Enterprise 2.0 prize alongside Boxbee and Jawfish Games."></media-image>

Beyond festival performance, no customer counts, revenue figures, or usage metrics were ever disclosed for either product era. The $1.5M seed round closed in June 2013—three months after the LAUNCH Festival win—suggesting investors were encouraged by the public momentum. But the pivot announcement fourteen months later, in August 2014, implicitly confirmed that the sales-leads product had not achieved the commercial traction needed to justify continued investment in that direction.

The company's GitHub organization remained active through late 2014, with repositories for the Motherbrain backend, example applications, and web crawling components—evidence of continued engineering output after the pivot, but not of commercial adoption.

---

## Post-Mortem

Zillabyte's failure was not a single catastrophic event. It was a sequential compression: each strategic move that seemed rational in isolation left the company in a worse competitive position than before. Two distinct failure modes operated in series.

### Failure Mode 1: Undercapitalization in a Capital-Intensive Market

The core mechanic of Zillabyte's sales product—crawling and indexing the web at scale, then running machine learning models to match companies against customer profiles—required enormous and continuous infrastructure investment. By March 2013, the company had indexed 2 billion pages and 11 million unique companies.<sup><a href="https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/">[19]</a></sup> Maintaining and expanding that index while simultaneously building a sales application on top of it demanded resources that $1.5 million in confirmed funding could not sustain.

The team attempted to address this constraint by building their own infrastructure rather than licensing existing solutions—a decision that was economically rational given their capital position but strategically costly. Building proprietary web-scale infrastructure consumed engineering bandwidth that could have gone toward customer development, sales, and product refinement. It also created the conditions for the pivot: by the time the team recognized the competitive dynamics of the sales-leads market, they had already built a substantial infrastructure layer that felt more defensible than the application sitting on top of it.

The competitors Zillabyte was racing against—Infer, Lattice Engines, and Mintigo—had raised orders of magnitude more capital. Lattice Engines had raised over $50 million by 2014. These companies could afford dedicated sales teams, deeper CRM integrations, and more sophisticated data partnerships. Zillabyte could not match their go-to-market investment on a seed-stage budget.

### Failure Mode 2: Competitive Displacement in the Application Layer

By August 2014, Huffstetler acknowledged the competitive reality directly. The pivot announcement cited "well-funded competitors" in the lead-scoring space as a primary reason for abandoning the sales product.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[23]</a></sup> The team's response was to ask a different question: rather than competing against Infer and Lattice Engines, could Zillabyte power them?

The logic was coherent. The team had already built the infrastructure. Their backgrounds at Google and Twilio gave them genuine technical credibility in distributed systems. "We really knew our founder-market fit was in scaleable, easy-to-use infrastructure, given our backgrounds at Google and Twilio," Huffstetler said.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[28]</a></sup>

But the pivot was announced in August 2014—the same period in which Google Cloud Dataflow and Amazon Kinesis were entering the market as managed data pipeline services.<sup><a href="https://www.crunchbase.com/organization/zillabyte">[24]</a></sup> Zillabyte's own Crunchbase profile described the company as "a direct competitor to these technologies." Competing with Google and Amazon in developer infrastructure, without proprietary data advantages, network effects, or meaningful switching costs, was not a viable position for a company at Zillabyte's funding level. The hyperscalers offered comparable or superior functionality with the distribution advantage of existing cloud relationships, enterprise sales teams, and effectively unlimited infrastructure investment.

### Failure Mode 3: The Analogical Positioning Trap

Zillabyte cycled through three distinct product analogies in roughly two years: "the Business Genome Project" (2011), "Palantir for salespeople" (March 2012), and "Pandora for sales leads" (March 2013).<sup><a href="https://www.slideshare.net/slideshow/zilladeck-public/16245275">[8]</a></sup><sup><a href="https://techcrunch.com/2012/03/27/yc-demo-day-session-1/">[10]</a></sup><sup><a href="https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/">[19]</a></sup> Each analogy was compelling in isolation. Together, they suggest a product that was still searching for its identity two years into operation.

The "Palantir for salespeople" framing resonated with investors at Demo Day—it communicated ambition and referenced a known, high-status company. But Palantir's value proposition was built on proprietary data integrations, government contracts, and a forward-deployed engineer model that had no analog in Zillabyte's product. The analogy set expectations the product could not meet.

The shift to "Pandora for sales leads" a year later emphasized the continuous feed mechanic—a more accurate description of the alert system—but also signaled that the team was still refining how to explain what they had built. No paying customer count or revenue figure was ever disclosed publicly, raising the question of whether the festival wins and press coverage translated into commercial adoption at all.

### Failure Mode 4: The Infrastructure Retreat

The pivot from application to infrastructure is a recognizable pattern in startup failure: founders retreat to what they know how to build rather than what the market needs. Huffstetler's framing—"we really knew our founder-market fit was in scaleable, easy-to-use infrastructure"—is honest, but it also describes a decision driven by technical comfort rather than validated market demand.<sup><a href="https://techcrunch.com/2014/08/21/zillabyte-relaunch/">[28]</a></sup>

The post-pivot product was technically real. The GitHub repositories show active development of the Motherbrain backend, web crawling components, and example applications through late 2014. But no post-pivot customer count or revenue figure was ever disclosed. The company closed approximately one year after the relaunch, with no acquisition, no soft landing, and no public retrospective.

The absence of any documented outcome—no acqui-hire, no asset sale, no shutdown announcement—suggests the company wound down quietly rather than failing dramatically. Huffstetler's transition to Chief of Staff for Congressman Seth Moulton<sup><a href="https://moulton.house.gov/news-stories/moulton-names-entrepreneur-and-marine-veteran-roger-dean-huffstetler-chief-of-staff/">[16]</a></sup> marked a clean break from the startup world. Jake Quist's subsequent activities are entirely undocumented in available sources.

---

## Key Lessons

- **Analogical positioning can mask weak product-market fit.** Zillabyte's progression through "Business Genome Project," "Palantir for salespeople," and "Pandora for sales leads" produced compelling press coverage and festival wins but no disclosed revenue. When a company cycles through high-concept analogies faster than it cycles through customer cohorts, the analogies are doing work the product should be doing. The LAUNCH Festival win in March 2013 came 17 months before the pivot—peak public excitement preceded commercial failure.

- **Web-scale data infrastructure is a capital trap for seed-stage companies.** Building and maintaining a proprietary index of 2 billion web pages requires continuous infrastructure investment that $1.5 million cannot sustain competitively. Zillabyte's decision to build its own infrastructure rather than license existing solutions was economically rational given its capital constraints, but it consumed engineering resources that could have gone toward customer development and created a false sense of defensibility. The infrastructure became the pivot rationale rather than the competitive moat.

- **Pivoting from application to infrastructure is a high-risk retreat, not a strategic upgrade.** The decision to abandon the sales-leads product and sell infrastructure to competitors was framed as playing to founder strengths. In practice, it moved Zillabyte from a market where it had some differentiation (a proprietary web index, a specific use case) into a market dominated by Google and Amazon with vastly superior distribution. Founder-market fit in infrastructure is not sufficient when the infrastructure market is being claimed by hyperscalers at the moment of entry.

- **Festival wins are not commercial validation.** Zillabyte's 992,000 crowd-favorite points at LAUNCH 2013 and its "Best Enterprise 2.0" award generated press coverage and investor interest. They did not generate disclosed customers or revenue. Startup competitions reward pitch quality and product vision; they do not validate willingness to pay, sales cycle length, or retention. The gap between Zillabyte's public visibility and its commercial outcomes illustrates the difference between market enthusiasm and market traction.

- **Competing directly against hyperscalers without a defensible moat is structurally untenable.** Zillabyte's post-pivot product entered a market at the exact moment Google and Amazon were launching managed data pipeline services with existing cloud customer relationships, enterprise sales infrastructure, and effectively unlimited capital. Without proprietary data, network effects, or switching costs that those platforms could not replicate, there was no structural basis for survival at the seed stage.

---

## Sources

1. [Poets & Quants: A Harvard MBA Co-Founds the Pandora of Sales Leads (December 2013)](https://poetsandquants.com/2013/12/06/a-harvard-mba-co-founds-the-pandora-of-sales-leads/)
2. [TechCrunch: Zillabyte Relaunches To Provide Infrastructure For Data Apps (August 2014)](https://techcrunch.com/2014/08/21/zillabyte-relaunch/)
3. [Zillabyte Pitch Deck (SlideShare)](https://www.slideshare.net/slideshow/zilladeck-public/16245275)
4. [TechCrunch: Ex-Googlers Debut Zillabyte To Let Business Users Easily Analyze Big Data (September 2011)](https://techcrunch.com/2011/09/30/ex-googlers-debut-zillabyte-to-let-users-easily-analyze-big-data/)
5. [VentureBeat: These 4 Startups Are Leading the Pack at Launch 2013 (March 2013)](https://venturebeat.com/entrepreneur/these-4-startups-are-leading-the-pack-at-launch-2013/)
6. [Y Combinator: Zillabyte Company Profile](https://www.ycombinator.com/companies/zillabyte)
7. [TechCrunch: YC Demo Day Session 1 (March 2012)](https://techcrunch.com/2012/03/27/yc-demo-day-session-1/)
8. [Crunchbase: Zillabyte Funding Timeline](https://www.crunchbase.com/organization/zillabyte/company_overview/overview_timeline)
9. [Crunchbase: Zillabyte Organization Profile](https://www.crunchbase.com/organization/zillabyte)
10. [Congressman Seth Moulton Press Release: Moulton Names Roger Dean Huffstetler Chief of Staff](https://moulton.house.gov/news-stories/moulton-names-entrepreneur-and-marine-veteran-roger-dean-huffstetler-chief-of-staff/)
11. [Golden.com: Zillabyte Profile](https://golden.com/wiki/Zillabyte-99B6K9G)
12. [LAUNCH Festival 2013 Winners (launch.co)](https://launch.co/blog/all-launch-festival-2013-winners-and-investment-prizes.html)
13. [VentureBeat: And the Winners of Launch Are… (March 2013)](https://venturebeat.com/entrepreneur/and-the-winners-of-launch-are/)
14. [The Next Web: Launch Festival Winners Announced (March 2013)](https://thenextweb.com/news/launch-festival-winners-announced-zillabyte-jawfish-games-named-top-winners)
15. [Zillabyte GitHub Organization](https://github.com/orgs/zillabyte/repositories)
