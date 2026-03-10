# Research Report: PatientBank

## Overview

PatientBank was a San Francisco-based health technology company that automated the process of requesting, digitizing, and managing medical records from any U.S. doctor or hospital.Founded in 2015 by four Yale alumni and backed by General Catalyst, Khosla Ventures, and Y Combinator, the company built genuine operational infrastructure — a database of 2.5 million healthcare contacts, multi-channel submission systems, and a HIPAA-compliant records platform — and scaled to serve over 150,000 users before shutting down in January 2018.

The core thesis of failure was not a product problem or a demand problem.PatientBank's consumer-facing, per-record fee model could not generate sufficient revenue to offset the high operational costs of manually bridging a healthcare system still overwhelmingly dependent on fax and paper.

The company solved a real problem at real scale, but the unit economics of acting as a human-powered middleware layer between patients and an analog hospital infrastructure proved structurally unsustainable.

<report-gallery>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/1235b5282a7b310369c45a9a9405458dc281dc2b.jpg" alt="PatientBank: Get medical records online—from any doctor or hospital ..." caption="PatientBank's profile avatar from its YC S16 listing — the company's public face during the months it was processing thousands of medical record requests and pitching investors on the promise of finally dragging American healthcare out of the fax age."></media-image>
<media-image src="https://i0.wp.com/www.craftylife.net/wp-content/uploads/2017/03/PatientBank-1-1.png?fit=200%2C300&ssl=1" alt="Living With Invisible Illness: PatientBank Review" caption="A screenshot from a 2017 patient review blog, capturing PatientBank's mobile interface at its operational peak — the same year the company hit 14,000 record requests in a single month, even as the economics of manually bridging patients and paper-dependent hospitals were quietly becoming impossible to sustain."></media-image>
</report-gallery>

## Founding Story

The idea for PatientBank originated from a moment of personal absurdity. Paul Fletcher-Hill, a Yale Computer Science and Economics graduate, wanted to build a website that visualized his own medical data.<sup><a href="https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/">[1]</a></sup> He assumed accessing his records would be straightforward. Instead, he discovered he had to submit a fax request — and still did not receive his records within 30 days.<sup><a href="https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/">[2]</a></sup> That experience, which would be familiar to most Americans who have ever tried to transfer their own health history, became the founding insight.

Fletcher-Hill began building a solution in 2014.<sup><a href="https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6">[3]</a></sup> He assembled a team from his Yale network: Feridun Mert Celebi, Kevin Grassi (an MD who brought clinical credibility), and Graham Kaemmer. The combination of technical, medical, and business backgrounds gave the founding team a credible profile for a healthcare-adjacent problem that required navigating both software development and institutional healthcare bureaucracy.<sup><a href="https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/">[4]</a></sup>

The company was formally incorporated as Health Exchange Technologies, Inc. and began operating publicly as PatientBank in 2015.<sup><a href="https://www.crunchbase.com/organization/patientbank">[5]</a></sup> Its first institutional partner was the Yale-New Haven Health System, and that early relationship proved instructive. The team discovered that the records access problem extended far beyond individual patients — hospitals, researchers, and private practices all struggled with the same fragmented, paper-dependent infrastructure.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[6]</a></sup> This was an early signal of potential B2B scope that the company would later deprioritize.

The team applied to Y Combinator and was accepted into the Summer 2016 batch. That acceptance triggered a deliberate strategic pivot. Fletcher-Hill explained the reasoning: "We decided consumers represented the best way to expand quickly, as individuals often end up being the vehicle for collecting or sharing records between their doctors or other providers."<sup><a href="https://www.mobihealthnews.com/content/patientbank-gets-22m-online-medical-record-sharing-system">[7]</a></sup> The dual hospital-staff and patient focus was narrowed to a pure consumer play.

The YC period brought institutional validation and forced the team to sharpen its growth thesis. By Demo Day in August 2016, PatientBank had already processed 10,000 records from 2,300 hospitals — a concrete operational proof point that distinguished it from most early-stage healthcare startups still in the concept phase.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[8]</a></sup>

---

## Timeline

- **2014** — Paul Fletcher-Hill begins building a website to help people gather, manage, and share medical records after personally experiencing the difficulty of accessing his own records via fax.<sup>[[3]](https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6)</sup>

- **2015** — PatientBank (legal name: Health Exchange Technologies, Inc.) is formally founded by Paul Fletcher-Hill, Feridun Mert Celebi, Kevin Grassi (MD), and Graham Kaemmer — all Yale alumni. First hospital partner is Yale-New Haven Health System.<sup>[[4]](https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/)</sup>

- **October 2015** — PatientBank begins collecting medical records; by late 2016 will have processed 10,000+ records from 2,300+ hospitals since this date.<sup>[[9]](https://www.ycombinator.com/blog/patientbank/)</sup>

- **August 23, 2016** — Y Combinator invests in PatientBank as part of its S16 batch. Company pivots focus from dual hospital-staff/patient model to pure consumer focus.<sup>[[10]](https://tracxn.com/d/companies/patientbank/__SBQhvjHjBIHa_KW2LtG6p8xgOjtmk2Fu-wV35dhXQTE/funding-and-investors)</sup>

- **August 2016** — PatientBank launches publicly on Hacker News and Product Hunt as part of YC S16 Demo Day cycle.

<media-hn url="https://news.ycombinator.com/item?id=12263238" title="PatientBank (YC S16) Is Creating a Unified Medical Record System" points="" comments=""></media-hn>

- **December 13, 2016** — PatientBank closes $2.2M seed round co-led by General Catalyst and Khosla Ventures, with participation from SV Angel, Spectrum 28, and Data Collective. Company reports 11,000+ completed record requests across 2,500 hospitals.<sup>[[11]](https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/)</sup>

- **July 2017** — PatientBank processes 14,000 medical record requests in a single month — its highest recorded monthly volume.<sup>[[12]](https://www.prnewswire.com/news-releases/with-us-news-hospital-rankings-delayed-patientbank-releases-national-scorecard-to-evaluate-medical-records-departments-at-hospitals-across-the-us-300497507.html)</sup>

- **August 1, 2017** — PatientBank launches a national hospital scorecard evaluating medical records departments across the U.S. on speed, fees, fulfillment, and delivery. By this point the company has processed 60,000+ total requests across 6,900 hospitals.<sup>[[12]](https://www.prnewswire.com/news-releases/with-us-news-hospital-rankings-delayed-patientbank-releases-national-scorecard-to-evaluate-medical-records-departments-at-hospitals-across-the-us-300497507.html)</sup>

- **January 4, 2018** — Paul Fletcher-Hill publishes shutdown announcement on Medium, citing inability to find a sustainable business model despite helping 150,000+ people and interacting with nearly every U.S. hospital.<sup>[[13]](https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6)</sup>

- **January 12, 2018** — PatientBank product fully closes.<sup>[[13]](https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6)</sup>

- **May 8, 2019** — Paul Fletcher-Hill, now working on Veil (a prediction market platform backed by Paradigm and Sequoia), reflects on PatientBank in a Sequoia interview, citing over-iteration and chasing lagging success indicators as key mistakes.<sup>[[14]](https://articles.sequoiacap.com/2019-05-08-paul-fletcher-hill)</sup>

---

## What They Built

PatientBank's core product was a HIPAA-compliant medical records request and management service. The user experience was designed to abstract away the bureaucratic complexity that made records access so painful in the first place.

A user would log in, enter their healthcare history — the names of their doctors, hospitals, and testing facilities — and provide an electronic signature. PatientBank then generated the required HIPAA-compliant authorization forms automatically, submitted requests to each provider on the user's behalf, and digitized any records that came back into a centralized online account.<sup><a href="https://grokipedia.com/page/patientbank">[15]</a></sup>

<media-image src="https://web.archive.org/web/20161201000000im_/https://www.patientbank.us/" alt="PatientBank homepage archived by the Wayback Machine circa late 2016" caption="Wayback Machine snapshot of the PatientBank homepage (patientbank.us) around the time of their $2.2M seed round close in December 2016."></media-image>

The operational backbone of this product was less glamorous than the consumer interface suggested. PatientBank maintained a database of over 2.5 million U.S. healthcare office contacts, which it used to track down and route requests to the correct department at each provider.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[16]</a></sup> Requests were submitted via multiple channels — mail, electronic transfer, and fax — because different hospitals accepted different methods. The team had to purchase a physical fax machine to handle the volume of hospital requests.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[17]</a></sup>

That fax machine detail is not incidental. It reveals that PatientBank was not a pure software company. It was a hybrid operations-and-software business, with real per-transaction labor and infrastructure costs embedded in every record request. The company used Aptible, another YC company, to secure protected health information on its servers — a sensible choice for HIPAA compliance that also added to the cost structure.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[18]</a></sup>

<media-tweet url="https://twitter.com/patientbankhq/status/714886922934554624" author="@PatientBankHQ" date="2016-03-29" text="@PatientBankHQ is 3/3 retrieving old med records, spanning MD, MA, TX, 3 Docs, 3 insurers, across 6 years. Fingers X'd for 4/4."></media-tweet>

The product evolved over time beyond pure record retrieval. PatientBank added full-text search across uploaded documents and annotation tools, transforming the platform from a one-time request service into a persistent medical records management system.<sup><a href="https://medium.com/patientbank-blog/store-search-and-share-your-medical-records-with-patientbank-f60212eee2cb">[19]</a></sup> Users could search across their entire health history, annotate documents, and share records with new providers.

In August 2017, the company launched a national hospital scorecard that evaluated medical records departments across the U.S. on speed, fees, fulfillment, and delivery criteria.<sup><a href="https://www.prnewswire.com/news-releases/with-us-news-hospital-rankings-delayed-patientbank-releases-national-scorecard-to-evaluate-medical-records-departments-at-hospitals-across-the-us-300497507.html">[20]</a></sup> This was simultaneously a content marketing play, a PR asset, and a demonstration of the operational data PatientBank had accumulated — the company had now interacted with nearly every hospital in the country and had a unique dataset to show for it.

<media-image src="https://web.archive.org/web/20170801000000im_/https://www.patientbank.us/" alt="PatientBank website homepage archived August 2017, around the time of their national hospital scorecard launch" caption="Wayback Machine capture of PatientBank's homepage in mid-2017, when the company had processed over 60,000 medical record requests and launched its national hospital scorecard."></media-image>

What distinguished PatientBank from alternatives was its operational completeness. Competitors like ZweenaHealth, Mana Health, and PicnicHealth were working on adjacent problems, but PatientBank's 2.5 million contact database and multi-channel submission infrastructure represented a genuine operational moat — one that took years to build and was difficult to replicate quickly.<sup><a href="https://medcitynews.com/2016/12/patientbank-medical-records-retrieval/">[21]</a></sup> The company delivered records in approximately 10 days, roughly three times faster than the average request.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[22]</a></sup>

---

## Market Position

### Target Customers

PatientBank's primary customer was the individual patient — specifically, anyone who needed to consolidate records from multiple providers, transfer care to a new doctor, or simply understand their own health history. The consumer focus was a deliberate choice made upon entering YC, when the team narrowed from a dual hospital-staff and patient model to a pure consumer play.<sup><a href="https://www.mobihealthnews.com/content/patientbank-gets-22m-online-medical-record-sharing-system">[7]</a></sup>

The product was particularly relevant for patients with complex medical histories spanning multiple providers, states, or years — exactly the scenario the PatientBank Twitter account demonstrated in March 2016, retrieving records across Maryland, Massachusetts, and Texas, spanning three doctors, three insurers, and six years of history.

The company's early work with Yale-New Haven Health System had surfaced a broader potential customer base: hospitals, researchers, and private practices all struggled with the same records access problem.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[6]</a></sup> This B2B signal was noted but not pursued as the primary growth vector. In retrospect, that decision deserves scrutiny — individual patients are a high-acquisition-cost, low-lifetime-value customer segment for a service used infrequently, while institutional buyers might have offered larger contracts and more predictable revenue.

### Market Size

The total addressable market for medical records access and management was large in aggregate but difficult to monetize at the consumer level. The U.S. healthcare system generates billions of medical records annually across approximately 6,000 hospitals and hundreds of thousands of physician practices. Every patient transition of care — a new specialist, a second opinion, an emergency room visit in a different city — creates a records transfer need.

The structural problem underpinning the market was well-documented. Kevin Grassi, PatientBank's co-founder and CMO, stated it plainly: "95% of medical info is exchanged by fax or by hand. In 2016 it's ridiculous for faxing to be the main communication method, but faxing is HIPAA compliant, and it's been the backbone of medical information exchange."<sup><a href="https://www.cbinsights.com/company/patientbank">[23]</a></sup>

That infrastructure gap created the market opportunity PatientBank was addressing. But it also defined the ceiling on how efficiently the company could serve that market. Every record request required touching a system — the hospital's medical records department — that had not modernized. The market size was real; the cost of serving it was the problem.

### Competition

PatientBank operated in a nascent but active space. Direct competitors included ZweenaHealth, Mana Health, and PicnicHealth, all of which were attempting to solve adjacent versions of the medical records access problem.<sup><a href="https://medcitynews.com/2016/12/patientbank-medical-records-retrieval/">[21]</a></sup>

The broader competitive landscape included Electronic Health Record (EHR) vendors like Epic and Cerner, which were building patient portal products (MyChart, HealtheLife) that gave patients some access to records held within a single health system. The limitation of these portals was precisely the problem PatientBank was solving: they worked within one system but could not aggregate records across multiple providers.

The competitive dynamic that ultimately mattered most was not between PatientBank and its direct competitors — it was between PatientBank and the status quo. The company's real competition was the fax machine, the paper form, and the hospital medical records department that had no incentive to change its workflow. That competition proved insurmountable at PatientBank's scale and funding level.

---

## Business Model

PatientBank charged a per-record processing fee. Sources conflict on the exact price point — one source cited $30 per record at the time of YC Demo Day in August 2016, while another cited $9.99 per record — suggesting the fee structure changed over the company's life.<sup><a href="https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/">[24]</a></sup>

The model had a structural problem embedded in its design. Revenue was capped by consumer willingness to pay a one-time fee for a service most people use infrequently. Costs, meanwhile, were tied to the analog infrastructure of hospital counterparties — fax, mail, manual digitization, and the labor required to manage exceptions and follow up on unfulfilled requests. The per-record fee model required either very high volume or very high prices to generate meaningful revenue, and the consumer segment constrained both levers.

The addition of search, annotation, and sharing features represented an attempt to increase user stickiness and create a recurring value proposition beyond the initial record request. Whether a subscription model was ever tested is not documented in available sources. No revenue figures were ever publicly disclosed at any stage of the company's life.

---2f:T7d4,

## Traction

PatientBank's user growth was real and followed a steep trajectory. The company began collecting records in October 2015. By late 2016, it had processed over 10,000 records from more than 2,300 hospitals.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[9]</a></sup> By December 2016, at the time of the seed round close, that figure had grown to 11,000+ completed requests spanning 2,500 hospitals.<sup><a href="https://www.mobihealthnews.com/content/patientbank-gets-22m-online-medical-record-sharing-system">[25]</a></sup>

Growth accelerated sharply in 2017. By August of that year, PatientBank had processed over 60,000 total requests across 6,900 hospitals — a roughly 5x increase in total volume in under nine months.<sup><a href="https://www.prnewswire.com/news-releases/with-us-news-hospital-rankings-delayed-patientbank-releases-national-scorecard-to-evaluate-medical-records-departments-at-hospitals-across-the-us-300497507.html">[12]</a></sup> July 2017 alone saw 14,000 requests — the company's single highest monthly volume on record.<sup><a href="https://www.prnewswire.com/news-releases/with-us-news-hospital-rankings-delayed-patientbank-releases-national-scorecard-to-evaluate-medical-records-departments-at-hospitals-across-the-us-300497507.html">[12]</a></sup> The cause of that spike is not documented in available sources.

At shutdown in January 2018, PatientBank had served over 150,000 users and had interacted with nearly every hospital in the United States.<sup><a href="https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6">[13]</a></sup>

The operational quality of the service was also demonstrable. PatientBank delivered records in approximately 10 days, roughly three times faster than the average request fulfilled through traditional channels.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[22]</a></sup> The product worked. The users came. Revenue did not follow at the scale required to sustain the business.

---

## Post-Mortem

PatientBank's shutdown on January 12, 2018 was not a product failure or a demand failure. It was a business model failure — one that the founder acknowledged directly and that the company's operational history makes legible in retrospect.

### Primary Cause: The Per-Record Fee Model Could Not Cover Operational Costs

Fletcher-Hill's shutdown announcement was precise about the failure: "We've helped over 150,000 people request their medical records. And our system has been used to interact with nearly every hospital in the United States. We've meaningfully changed the way people access their medical records. However, throughout this journey we've struggled to find a sustainable business model."<sup><a href="https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6">[13]</a></sup>

The structural problem was this: PatientBank's cost base was tied to the analog infrastructure of its hospital counterparties, while its revenue was capped by consumer willingness to pay a per-record fee. Every record request required submitting forms via fax or mail, following up on unfulfilled requests, and manually digitizing paper documents that came back. These were not costs that declined with scale in the way software costs do. They were operational costs that scaled roughly linearly with volume.

At the time of YC Demo Day in August 2016, TechCrunch reported that PatientBank was generating approximately $4,000 in weekly revenue at $30 per record.<sup><a href="https://techcrunch.com/2016/08/23/yc-demo-day/">[26]</a></sup> That figure — roughly $208,000 annualized — was not sufficient to sustain a company with real infrastructure costs, a four-person founding team, and San Francisco overhead, even before accounting for the cost of the seed round's investor expectations. Whether the price point later dropped to $9.99 per record would have made the unit economics significantly worse at any given volume level.

The team's attempted remedy was to add product features — search, annotation, sharing tools — that might increase the perceived value of the service and justify either higher prices or a subscription model. The hospital scorecard launch in August 2017 was a parallel attempt to generate press coverage and potentially open B2B conversations. Neither move resolved the fundamental mismatch between operational costs and consumer revenue.

### Secondary Cause: Fax Dependency Was Not a Solvable Technical Problem

PatientBank could not change hospital behavior. The company's operational model required hospitals to respond to record requests — and hospitals had both structural inertia and a perceived rationale for maintaining fax-based workflows.

Fletcher-Hill told a reporter that hospitals cited security as a reason for their continued fax dependency, with many believing computer systems were easier to hack than fax machines.<sup><a href="https://www.bespacific.com/the-fax-is-not-yet-obsolete/">[27]</a></sup> Whether or not that belief was technically accurate, it was institutionally entrenched. Kevin Grassi had identified the problem clearly: "95% of medical info is exchanged by fax or by hand. In 2016 it's ridiculous for faxing to be the main communication method, but faxing is HIPAA compliant, and it's been the backbone of medical information exchange."<sup><a href="https://www.cbinsights.com/company/patientbank">[23]</a></sup>

PatientBank's attempted remedy was to build around the fax problem rather than through it — purchasing a fax machine, building a multi-channel submission system, and absorbing the operational cost of analog infrastructure as a cost of doing business.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[17]</a></sup> This worked as a product strategy but failed as a business strategy. The company could process fax-dependent requests at scale, but it could not do so profitably at consumer price points.

The fax problem was not unique to PatientBank. It was an industry-wide infrastructure failure that required either regulatory intervention (which came later, with the 21st Century Cures Act's interoperability rules in 2020) or hospital-level behavior change that no single startup could compel. PatientBank was operating in a market where the supply side — hospitals — had no financial incentive to modernize their records departments.

### Tertiary Cause: The Consumer Pivot Deprioritized a More Viable B2B Path

PatientBank's first institutional relationship was with Yale-New Haven Health System, and through that relationship the team identified that hospitals, researchers, and private practices all faced the same records access problem.<sup><a href="https://www.ycombinator.com/blog/patientbank/">[6]</a></sup> That was a B2B signal. The team chose not to pursue it as the primary growth vector upon entering YC, instead pivoting to a pure consumer focus.

The consumer segment has well-understood limitations for a service used infrequently. Individual patients request their medical records rarely — perhaps when changing primary care physicians, seeking a second opinion, or moving to a new city. This creates a low lifetime value per user and a high effective customer acquisition cost relative to revenue generated. The 150,000 users PatientBank served at shutdown represents genuine scale, but if most of those users made a single record request and never returned, the revenue per user was bounded by a single transaction fee.

The B2B path — selling to hospitals, health systems, or insurers who needed to process high volumes of records requests — would have offered larger contract sizes, more predictable revenue, and potentially a different cost structure. PatientBank's operational infrastructure (the 2.5 million contact database, the multi-channel submission system, the processing workflow) was exactly the kind of asset an institutional buyer might pay for. Whether the team explored this path before shutting down is not documented in available sources.

### Compounding Factor: Over-Iteration Without Finding the Monetization Lever

In a 2019 Sequoia interview, Fletcher-Hill offered a candid self-diagnosis of his execution at PatientBank: "As a founder, especially with our previous company, PatientBank, I think I overcompensated and shifted from too much optimization to too much iteration."<sup><a href="https://articles.sequoiacap.com/2019-05-08-paul-fletcher-hill">[14]</a></sup>

He elaborated on the broader lesson: "Know the difference between indicators of success and what I call lagging indicators of success, which are things like fundraising, PR efforts and getting a big office... the first priorities are the true indicators of success — product-market fit and users and revenue."<sup><a href="https://articles.sequoiacap.com/2019-05-08-paul-fletcher-hill">[14]</a></sup>

The product evolution at PatientBank — from record retrieval to search and annotation to the hospital scorecard — reflects a team cycling through features and content strategies without finding the monetization lever. Each addition was defensible in isolation: search increased stickiness, annotation added value, the scorecard generated press. But none of these moves addressed the fundamental unit economics problem. The $2.2M seed round, raised from credible investors at General Catalyst, Khosla, and SV Angel, may have created a false sense of validation that delayed the harder conversation about whether the consumer per-record model could ever generate sufficient revenue.<sup><a href="https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/">[11]</a></sup> With only $2.2M in total confirmed funding and high operational costs, the runway was structurally limited for a company that needed either to change hospital behavior or find an institutional buyer willing to pay for its infrastructure.<sup><a href="https://tracxn.com/d/companies/patientbank/__SBQhvjHjBIHa_KW2LtG6p8xgOjtmk2Fu-wV35dhXQTE/funding-and-investors">[28]</a></sup>

---

## Key Lessons

- **Consumer willingness to pay is a ceiling, not a floor, for operationally intensive services.** PatientBank's per-record fee model was bounded by what individual patients would pay for an infrequent service. The company's costs, meanwhile, were tied to analog hospital infrastructure that did not become cheaper at scale. Any business that acts as a human-powered middleware layer between consumers and institutional counterparties faces this structural tension. The question of whether the price point can ever exceed the operational cost per transaction must be answered before scaling.

- **Institutional traction signals should not be discarded in favor of consumer growth metrics.** PatientBank's first meaningful relationship was with Yale-New Haven Health System, and the team identified early that hospitals and researchers faced the same problem as individual patients. The pivot to pure consumer focus — driven by YC-style growth logic — deprioritized a B2B path that might have offered larger contracts, higher lifetime value, and a more defensible revenue model. When early institutional signals conflict with consumer growth narratives, founders should pressure-test both before committing.

- **Fundraising and press coverage are lagging indicators that can mask leading indicator failures.** PatientBank raised $2.2M from General Catalyst, Khosla Ventures, and SV Angel, and received coverage from TechCrunch, MobiHealthNews, and HIT Consultant. Fletcher-Hill later identified this dynamic explicitly: the company was succeeding on lagging indicators while the leading indicators — product-market fit and revenue — were not resolving.<sup><a href="https://articles.sequoiacap.com/2019-05-08-paul-fletcher-hill">[14]</a></sup> Institutional validation from investors and press can delay the moment when a team confronts whether its business model actually works.

- **Infrastructure-dependent startups need a theory for changing supplier behavior, not just consumer behavior.** PatientBank could change how patients requested records. It could not change how hospitals fulfilled those requests. The fax machine was not a technical problem PatientBank could solve — it was an institutional behavior problem that required either regulatory pressure or financial incentives that PatientBank was not positioned to provide. Any startup whose unit economics depend on a counterparty modernizing its infrastructure needs an explicit strategy for accelerating that modernization, or needs to build a business model that works despite it.

- **Product iteration without a monetization hypothesis is feature accumulation, not progress.** The evolution from record retrieval to search, annotation, sharing, and the hospital scorecard represented genuine product development. But each addition addressed user engagement rather than the revenue problem. Fletcher-Hill's own retrospective framing — "too much iteration" over "optimization" — suggests the team recognized this pattern in hindsight.<sup><a href="https://articles.sequoiacap.com/2019-05-08-paul-fletcher-hill">[14]</a></sup> Product decisions should be evaluated against their expected impact on the specific metric the business needs to improve, not just their impact on user experience.

---

## Sources

1. [HIT Consultant — PatientBank Lands $2.2M to Help People Request Medical Records Online (December 13, 2016)](https://hitconsultant.net/2016/12/13/patientbank-lands-2-2m-f/)
2. [Medium / PatientBank Blog — Saying Goodbye to PatientBank, by Paul Fletcher-Hill (January 4, 2018)](https://medium.com/patientbank-blog/saying-goodbye-to-patientbank-7456247851b6)
3. [Crunchbase — PatientBank company profile](https://www.crunchbase.com/organization/patientbank)
4. [Y Combinator Blog — PatientBank is Creating a Unified Medical Record System](https://www.ycombinator.com/blog/patientbank/)
5. [MobiHealthNews — PatientBank gets $2.2M for online medical record sharing system (December 15, 2016)](https://www.mobihealthnews.com/content/patientbank-gets-22m-online-medical-record-sharing-system)
6. [Token Summit — Paul Fletcher-Hill speaker profile](https://tokensummit.com/speaker/fletcher-hill-paul/)
7. [Tracxn — PatientBank funding and investors](https://tracxn.com/d/companies/patientbank/__SBQhvjHjBIHa_KW2LtG6p8xgOjtmk2Fu-wV35dhXQTE/funding-and-investors)
8. [Wikipedia — PatientBank](https://en.wikipedia.org/wiki/PatientBank)
9. [Grokipedia — PatientBank](https://grokipedia.com/page/patientbank)
10. [Medium / PatientBank Blog — Store, Search, and Share Your Medical Records with PatientBank, by Graham Kaemmer](https://medium.com/patientbank-blog/store-search-and-share-your-medical-records-with-patientbank-f60212eee2cb)
11. [PR Newswire — PatientBank Releases National Scorecard to Evaluate Medical Records Departments (August 1, 2017)](https://www.prnewswire.com/news-releases/with-us-news-hospital-rankings-delayed-patientbank-releases-national-scorecard-to-evaluate-medical-records-departments-at-hospitals-across-the-us-300497507.html)
12. [CBInsights — PatientBank company profile](https://www.cbinsights.com/company/patientbank)
13. [Sequoia Capital — Interview with Paul Fletcher-Hill (May 8, 2019)](https://articles.sequoiacap.com/2019-05-08-paul-fletcher-hill)
14. [MedCityNews — PatientBank medical records retrieval (December 16, 2016)](https://medcitynews.com/2016/12/patientbank-medical-records-retrieval/)
15. [BeSpacific — The Fax Is Not Yet Obsolete](https://www.bespacific.com/the-fax-is-not-yet-obsolete/)
16. [TechCrunch — YC S16 Demo Day coverage (August 23, 2016)](https://techcrunch.com/2016/08/23/yc-demo-day/)
17. [Hacker News — PatientBank (YC S16) Is Creating a Unified Medical Record System](https://news.ycombinator.com/item?id=12263238)
18. [Product Hunt — PatientBank product page](https://www.producthunt.com/products/patientbank)
