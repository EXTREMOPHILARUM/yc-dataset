# Research Report: Reverie Labs

## Overview

Reverie Labs was a Cambridge, Massachusetts-based AI drug discovery company founded in 2017 by Jonah Kallenbach, Ankit Gupta, and Connor Duffy. The company began as a B2B SaaS business selling machine learning tools to pharmaceutical companies, then pivoted twice — first to selling ML-designed drug candidates as a service, then to becoming a fully integrated drug developer with its own pipeline of brain-penetrant kinase inhibitors for oncology. It raised approximately $32 million across its lifetime and secured a marquee collaboration with Roche and Genentech in 2020.<sup><a href="https://www.prnewswire.com/news-releases/reverie-labs-raises-25m-series-a-round-to-broaden-impact-of-its-computational-kinase-drug-discovery-platform-301220854.html">[1]</a></sup>

Reverie failed as an independent company because its founding market assumption was empirically wrong: pharma's trillion-dollar R&D budget does not translate into large software purchasing budgets. The real addressable market for pharma software was tens of millions of dollars, not billions — a gap the founders discovered only after entering YC. The pivot to drug development solved the TAM problem but introduced a new one: clinical proof-of-concept timelines of five to ten years are structurally incompatible with venture capital return horizons.

In February 2024, Ginkgo Bioworks acquired Reverie's AI platform and four key team members for an undisclosed sum — a deal structure consistent with an acqui-hire rather than a pipeline acquisition.<sup><a href="https://www.prnewswire.com/news-releases/ginkgo-bioworks-acquires-reverie-labs-platform-enhancing-ai-driven-drug-discovery-capabilities-for-customer-programs-302073641.html">[2]</a></sup> With $3.53 million in RSUs granted to four employees, the total consideration almost certainly fell well below the $32 million raised, leaving investors with limited or no return.<sup><a href="https://www.prnewswire.com/news-releases/ginkgo-bioworks-provides-compensation-information-related-to-recent-acquisitions-302073672.html">[3]</a></sup>

<report-gallery>
<media-image src="https://specials-images.forbesimg.com/imageserve/636b1a417ce7b1fc3142ae51/416x416.jpg?background=000000&cropX1=0&cropX2=1080&cropY1=0&cropY2=1080" alt="Ankit Gupta, co-founder and CTO of Reverie Labs" caption="Ankit Gupta, co-founder and CTO of Reverie Labs — the Harvard ML researcher who would later write one of the most candid founder post-mortems in biotech, and eventually join YC as a General Partner."></media-image>
<media-image src="https://mma.prnewswire.com/media/2349066/Ginkgo_Bioworks__Image_header___logos.jpg" alt="Ginkgo Bioworks acquires Reverie Labs, February 2024" caption="The February 2024 press release announcing Ginkgo Bioworks' acquisition of Reverie Labs — a deal framed around AI infrastructure, not drug pipeline, signaling the quiet end of Reverie's independent ambitions."></media-image>
</report-gallery>

## Founding Story

Reverie Labs emerged from a Harvard dormitory friendship and a shared conviction that machine learning could fix one of the most expensive and failure-prone processes in modern science: pharmaceutical drug development.

Jonah Kallenbach and Ankit Gupta were college blockmates at Harvard, both earning joint BA/MS degrees in Computer Science in 2017.<sup><a href="https://medium.com/harvard-in-tech/harvard-in-tech-ai-edition-ankit-gupta-visting-partner-at-y-combinator-and-head-of-ai-at-ginkgo-2e494e66f121">[4]</a></sup> Gupta had published research at ICML, including a 2017 paper on dilated convolutions for modeling long-distance genomic dependencies that won the Speaker Award and Best Poster at the ICML Workshop on Computational Biology — an early signal of his interest in applying ML to biology.<sup><a href="https://villpress.com/ankit-gupta-joins-y-combinator-as-general-partner/">[5]</a></sup> Before founding Reverie, he had worked as a Research Engineer at Vicarious AI.<sup><a href="https://www.boringbusinessnerd.com/startups/reverie-labs">[6]</a></sup> Their third co-founder, Connor Duffy, brought a complementary profile: an MIT graduate with dual degrees in computer science and molecular biology, and prior experience as a Data Insights Engineer at Flatiron Health.<sup><a href="https://startupsventurecapital.com/9-my-5-favorite-startups-at-drf-19b80ed97cba">[7]</a></sup><sup><a href="https://www.crunchbase.com/person/connor-duffy">[8]</a></sup> Duffy was the team's closest link to biology as a discipline, though none of the three had deep medicinal chemistry or drug development industry experience before founding.

The founding insight was intuitive and, on the surface, compelling: pharmaceutical R&D is a multi-trillion-dollar industry plagued by high failure rates and decade-long timelines. Machine learning had recently demonstrated transformative results in image recognition, natural language processing, and genomics. Surely, the founders reasoned, a capital-intensive industry desperate for better tools would pay handsomely for software that could predict which molecules would become drugs.

The company's name — drawn from a pivotal detail in HBO's *Westworld* — captured the cultural moment: technically ambitious, pop-culture-inflected, and optimistic about AI's capacity to reshape physical-world industries.<sup><a href="https://techcrunch.com/2018/03/16/reverie-labs-uses-new-machine-learning-algorithms-to-fix-drug-development-bottlenecks/">[9]</a></sup> Reverie launched in 2017 with initial seed funding from Rough Draft Ventures and a plan to sell ML software to pharma companies, training models on customers' proprietary datasets inside their virtual private clouds for security.<sup><a href="https://tracxn.com/d/companies/reverie-labs/__KK9JD-uznpt71zyBuf4NJTLFLkO2_5-bi3zK_PZZf_k/funding-and-investors">[10]</a></sup><sup><a href="https://techcrunch.com/2018/03/16/reverie-labs-uses-new-machine-learning-algorithms-to-fix-drug-development-bottlenecks/">[11]</a></sup>

Y Combinator's Winter 2018 batch provided early validation, capital, and a network that would prove durable even after the company's independent run ended.<sup><a href="https://medium.com/harvard-in-tech/harvard-in-tech-ai-edition-ankit-gupta-visting-partner-at-y-combinator-and-head-of-ai-at-ginkgo-2e494e66f121">[12]</a></sup> But YC also reinforced a SaaS framing — recurring revenue, software margins, scalable distribution — that would prove structurally ill-suited to pharma's procurement culture. The founders would discover this mismatch before Demo Day, triggering the first of two major pivots that would define the company's trajectory.

Gupta later reflected on the founding with characteristic candor: "We began as a machine learning driven software company selling SaaS tools and consulting services to pharma companies, and at acquisition we were a pharmaceutical company, developing our own in-house pipeline of drug assets and advancing them."<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[13]</a></sup> The distance between those two sentences is the story of Reverie Labs.

## Timeline

- **2017** — Reverie Labs founded by Jonah Kallenbach, Ankit Gupta, and Connor Duffy after graduating from Harvard and MIT; initial seed funding from Rough Draft Ventures.<sup>[[14]](https://techcrunch.com/2018/03/16/reverie-labs-uses-new-machine-learning-algorithms-to-fix-drug-development-bottlenecks/)</sup>
- **2017** — Company launches as a B2B SaaS business, training ML models on pharma customers' proprietary datasets inside their virtual private clouds.<sup>[[11]](https://techcrunch.com/2018/03/16/reverie-labs-uses-new-machine-learning-algorithms-to-fix-drug-development-bottlenecks/)</sup>
- **January 2018** — Reverie Labs joins Y Combinator's Winter 2018 batch.<sup>[[12]](https://medium.com/harvard-in-tech/harvard-in-tech-ai-edition-ankit-gupta-visting-partner-at-y-combinator-and-head-of-ai-at-ginkgo-2e494e66f121)</sup>
- **March 2018** — Seed round raised from BoxGroup and 13 other investors; TechCrunch covers the company.<sup>[[15]](https://www.crunchbase.com/organization/reverie-labs/company_overview/overview_timeline)</sup> At YC Demo Day, Reverie pivots its pitch to "molecules as a service" after discovering the pharma software TAM is far smaller than assumed.<sup>[[16]](https://ankitg.me/blog/2025/01/06/unfair-coins.html)</sup>
- **July 8, 2020** — Reverie Labs announces multi-target, multi-year collaboration agreement with Roche and Genentech to advance next-generation kinase inhibitors using AI.<sup>[[17]](https://www.prnewswire.com/news-releases/reverie-labs-enters-multi-target-collaboration-agreement-with-roche-301089930.html)</sup>
- **August 25, 2020** — Reverie Labs raises $6.6 million from First Round Capital, Neo, Wireframe Ventures, and LifeForce Capital; profiled as a "virtual drug discovery company with no lab of its own."<sup>[[18]](https://www.synbiobeta.com/read/a-virtual-drug-discovery-company-with-no-lab-of-its-own-partners-with-roche-to-fight-cancers-in-the-brain)</sup>
- **February 3, 2021** — Reverie Labs closes $25 million Series A led by Ridgeback Capital Investments; Wayne Holman, M.D. joins the board. Total funding reaches approximately $32 million.<sup>[[1]](https://www.prnewswire.com/news-releases/reverie-labs-raises-25m-series-a-round-to-broaden-impact-of-its-computational-kinase-drug-discovery-platform-301220854.html)</sup>
- **December 2022** — Reverie Labs has approximately 27 employees, suggesting lean operations and limited headcount growth despite Series A capital.<sup>[[19]](https://tracxn.com/d/companies/reverie-labs/__KK9JD-uznpt71zyBuf4NJTLFLkO2_5-bi3zK_PZZf_k)</sup>
- **January 2023** — Reverie Labs recognized as one of "12 Boston Companies to Watch in Spring 2023" by Built In Boston.<sup>[[20]](https://www.linkedin.com/company/reverie-labs)</sup>
- **May 2023** — Pipeline status: RVL-101 at IND-enabling stage, RVL-102 at late discovery, RVL-103 at early discovery, plus undisclosed Roche/Genentech candidates.<sup>[[21]](https://www.boringbusinessnerd.com/startups/reverie-labs)</sup>
- **February 23, 2024** — Ginkgo Bioworks acquires Reverie Labs; four key AI team members join Ginkgo, including Ankit Gupta as Head of AI/ML Advancement. Acquisition price not disclosed.<sup>[[22]](https://www.prnewswire.com/news-releases/ginkgo-bioworks-provides-compensation-information-related-to-recent-acquisitions-302073672.html)</sup>
- **February 28, 2024** — Acquisition announced publicly; Ginkgo discloses $3.53 million in RSU grants to four Reverie employees.<sup>[[3]](https://www.prnewswire.com/news-releases/ginkgo-bioworks-provides-compensation-information-related-to-recent-acquisitions-302073672.html)</sup>
- **January 6, 2025** — Ankit Gupta publishes candid post-mortem blog post ("Unfair Coins") detailing the pharma software TAM miscalculation, the pivot history, and lessons learned.<sup>[[23]](https://ankitg.me/blog/2025/01/06/unfair-coins.html)</sup>
- **Late 2025** — Ankit Gupta joins Y Combinator as a General Partner.<sup>[[24]](https://www.ycombinator.com/blog/welcome-ankit)</sup>

## What They Built

Reverie Labs built a computational drug discovery platform centered on one of the most commercially validated but scientifically difficult target classes in oncology: kinase inhibitors. Kinases are enzymes that regulate cell signaling, and their dysregulation drives many cancers. Dozens of approved kinase inhibitor drugs exist, but most fail to penetrate the blood-brain barrier — making brain tumors and brain metastases particularly hard to treat. Reverie's specific niche was designing kinase inhibitors that were simultaneously potent, selective (hitting only the intended target), and brain-penetrant.<sup><a href="https://www.prnewswire.com/news-releases/reverie-labs-raises-25m-series-a-round-to-broaden-impact-of-its-computational-kinase-drug-discovery-platform-301220854.html">[25]</a></sup>

The platform's core function was predicting molecular properties using deep learning. Given a candidate molecule's chemical structure, Reverie's models could estimate how well it would bind to a target kinase (potency), whether it would hit unintended targets (selectivity), how it would behave in the body (ADMET: absorption, distribution, metabolism, excretion, and toxicity), and whether it could cross the blood-brain barrier. These predictions guided chemists toward promising candidates faster than traditional trial-and-error synthesis.<sup><a href="https://www.crunchbase.com/organization/reverie-labs">[26]</a></sup>

The platform evolved through three distinct phases:

**Phase 1 — SaaS tools (2017–2018):** Reverie's initial product was software sold directly to pharma companies. The technical approach was sophisticated: models were trained on each customer's proprietary experimental data, and the software ran inside the customer's virtual private cloud to protect data security.<sup><a href="https://techcrunch.com/2018/03/16/reverie-labs-uses-new-machine-learning-algorithms-to-fix-drug-development-bottlenecks/">[11]</a></sup> This architecture addressed pharma's legitimate data confidentiality concerns but created a deployment and sales complexity that slowed adoption.

**Phase 2 — Molecules as a service (2018 onward):** After the TAM realization at YC, Reverie shifted to selling outputs rather than tools — delivering ML-designed drug candidates to pharma partners rather than the software to design them. This model was more legible to pharma buyers, who understood paying for molecules, and it allowed Reverie to demonstrate value through chemistry results rather than software metrics.

**Phase 3 — Integrated drug developer (2020–2024):** Reverie ultimately became the pharma company it had originally tried to sell software to. It built an internal pipeline under the RVL designation, hired experienced drug hunters — including a VP of Chemistry from Blueprint Medicines, a VP of Preclinical Development from ROME Therapeutics, and a Head of Biology from Merck — and operated as a "virtual" drug discovery company with no physical laboratory of its own, relying on contract research organizations (CROs) for experimental validation.<sup><a href="https://www.boringbusinessnerd.com/startups/reverie-labs">[27]</a></sup><sup><a href="https://www.synbiobeta.com/read/a-virtual-drug-discovery-company-with-no-lab-of-its-own-partners-with-roche-to-fight-cancers-in-the-brain">[28]</a></sup>

The virtual model was a deliberate capital efficiency choice: by outsourcing wet lab work to CROs, Reverie avoided the capital expenditure of building laboratory infrastructure. The tradeoff was dependence on external partners for the experimental data that fed its models — a structural tension in a company whose core value proposition was learning from data.

By May 2023, the pipeline included RVL-101 at IND-enabling stage (the last preclinical step before human trials), RVL-102 at late discovery, RVL-103 at early discovery, and multiple undisclosed candidates from the Roche/Genentech collaboration.<sup><a href="https://www.boringbusinessnerd.com/startups/reverie-labs">[21]</a></sup> Reverie filed only one patent across its seven-year lifetime, suggesting the core intellectual property resided in data assets and model weights rather than novel chemistry.<sup><a href="https://www.cbinsights.com/company/reverie-labs">[29]</a></sup>

## Market Position

### Target Customers

Reverie Labs served two distinct customer types across its lifetime, and the tension between them reflects the company's strategic evolution.

In its SaaS phase, the target customer was the computational chemistry or informatics department at a large pharmaceutical company — a technical buyer with budget authority over software tools. In its molecules-as-a-service and integrated drug developer phases, the relevant counterparty shifted to business development executives and program leaders at large pharma, who evaluate external drug candidates for in-licensing or collaboration.

These are fundamentally different buyers with different evaluation criteria, different procurement timelines, and different definitions of value. Reverie's pivot from one to the other was not merely a product change — it was a complete repositioning of who the company needed to convince and how.

### Market Size

The pharma software TAM miscalculation is the central market-sizing lesson of Reverie's story, and Gupta's post-mortem is unusually precise about the error. The top-down logic was seductive: global pharmaceutical R&D spending exceeds $200 billion annually, and even a small software capture rate would imply a multi-billion-dollar market. The bottoms-up reality was different. Gupta calculated the actual market as "more like ~10s of companies to sell $100,000s of software to, and ~100s of companies to sell $10,000s of software to" — producing a TAM of "more like double digit millions instead of billions."<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[30]</a></sup>

The drug development market Reverie ultimately entered is large in aggregate — global oncology drug sales exceed $200 billion annually — but it is not a software market. It is a capital market, where value is created through clinical proof-of-concept and captured through licensing deals, partnerships, or acquisitions at clinical milestones. The capital requirements to reach those milestones are measured in hundreds of millions of dollars, not tens of millions.

### Competition

Reverie operated in a category that attracted significant capital and credentialed competitors during the AI-for-drug-discovery wave of 2018–2022. Its primary competitors included Recursion Pharmaceuticals, BenevolentAI, and XtalPi.<sup><a href="https://tracxn.com/d/companies/reverie-labs/__KK9JD-uznpt71zyBuf4NJTLFLkO2_5-bi3zK_PZZf_k">[31]</a></sup>

The competitive landscape is best understood along two axes: **balance sheet depth** and **platform breadth**. Recursion raised over $1 billion and built proprietary high-throughput biology infrastructure, giving it both a data moat and a capital cushion that Reverie could not match. BenevolentAI went public via SPAC in 2022 at a valuation exceeding $1.5 billion, providing access to public capital markets. XtalPi, backed by Alphabet and Tencent, focused on physics-based molecular simulation at scale.

Reverie's competitive position was defined by depth rather than breadth: a narrow focus on kinase inhibitors and brain penetrance, executed with a lean team and a virtual operating model. This was a scientifically defensible niche, but it made differentiation difficult to communicate to pharma partners who were simultaneously evaluating multiple AI drug discovery platforms. The company was not competing on distribution reach or data scale — the dimensions where well-capitalized incumbents had natural advantages — but on computational sophistication and chemistry execution speed. That advantage was real but not durable against competitors with orders-of-magnitude larger balance sheets.

The structural dynamic that made Reverie's position most precarious was not direct competition for deals, but the category-level skepticism that emerged as AI drug discovery companies struggled to translate computational predictions into clinical outcomes. As the broader sector faced scrutiny — BenevolentAI's lead program failed in Phase IIb in 2023 — the bar for demonstrating clinical differentiation rose precisely when Reverie needed to raise a Series B.

## Business Model

Reverie Labs attempted three distinct revenue models across its lifetime, none of which achieved the scale needed to sustain an independent company.

**SaaS licensing (2017–2018):** The initial model charged pharma companies for access to ML tools trained on their proprietary data. Revenue was never disclosed, and the model was abandoned before it could be validated at scale. The absence of any public revenue disclosure from this period is itself informative — if the SaaS business had generated meaningful revenue, it would likely have appeared in fundraising materials.

**Molecules as a service / partnership fees (2018–2020):** Reverie shifted to charging for ML-designed drug candidates, with revenue structured around upfront fees and milestone payments. The Roche/Genentech collaboration (July 2020) was the most significant deal under this model: Reverie received an undisclosed upfront payment and was eligible for preclinical, clinical, and regulatory milestone payments, plus tiered royalties on eventual drug sales.<sup><a href="https://www.scienceboard.net/index.aspx?sec=sup&sub=Drug&pag=dis&ItemID=1012">[32]</a></sup> Milestone-dependent revenue is structurally unpredictable — payments arrive only when programs advance, and programs can be deprioritized for reasons entirely unrelated to drug quality.

**Integrated drug developer (2021–2024):** In this phase, Reverie's "revenue" was effectively future option value — the potential licensing or acquisition value of its pipeline if candidates reached clinical proof-of-concept. This model requires patient capital and long timelines.

*Inferred burn rate:* With approximately $32 million raised and roughly 27–29 employees as of late 2022, a reasonable estimate for annual operating costs — including CRO expenses, salaries, and overhead — would be $8–12 million per year. At that rate, the Series A capital ($25 million, closed February 2021) would have been substantially depleted by early 2024, consistent with the acquisition timing. These are inferences, not disclosed figures.

## Traction

Reverie's most significant commercial milestone was the July 2020 collaboration with Roche and Genentech — one of the world's leading oncology companies — to advance next-generation kinase inhibitors across multiple targets over multiple years.<sup><a href="https://www.prnewswire.com/news-releases/reverie-labs-enters-multi-target-collaboration-agreement-with-roche-301089930.html">[17]</a></sup> The deal validated Reverie's scientific credibility at the highest level of the industry. Financial terms were not disclosed, and milestone payments were contingent on preclinical and clinical progress that takes years to achieve.

On the chemistry execution side, Reverie's internal metrics were strong. Gupta wrote that across approximately ten programs, the team consistently generated potent, selective inhibitors within the first two months of a program — a meaningful demonstration of the platform's lead generation speed.<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[33]</a></sup> The bottleneck was ADMET optimization — ensuring that promising molecules were also safe, metabolically stable, and bioavailable — which took months to years per program. This timeline mismatch between fast lead generation and slow optimization is a structural feature of drug discovery, not a Reverie-specific failure.

By May 2023, the pipeline had advanced to four candidates: RVL-101 at IND-enabling stage (the last preclinical hurdle before human trials), RVL-102 at late discovery, RVL-103 at early discovery, and undisclosed Roche/Genentech candidates.<sup><a href="https://www.boringbusinessnerd.com/startups/reverie-labs">[21]</a></sup> IND-enabling stage is meaningful progress — it represents years of preclinical work — but it is not the clinical proof-of-concept milestone that typically unlocks large Series B rounds or premium acquisition offers in the current biotech financing environment.

The company maintained a lean headcount of approximately 27–29 employees through late 2022 and into 2024, consistent with capital conservation rather than aggressive scaling.<sup><a href="https://tracxn.com/d/companies/reverie-labs/__KK9JD-uznpt71zyBuf4NJTLFLkO2_5-bi3zK_PZZf_k">[19]</a></sup><sup><a href="https://www.ycombinator.com/companies/reverie-labs">[34]</a></sup>

## Post-Mortem

Reverie Labs did not fail from a single catastrophic decision. It failed from the compounding of three structural problems: a market too small for the initial business model, a pivot to a capital-intensive alternative with timelines misaligned with venture returns, and a partnership structure that introduced irreducible uncertainty into the company's most important commercial relationship.

### Primary Cause: The Pharma Software TAM Was a Top-Down Illusion

The founding thesis rested on an inference that did not survive contact with the market. Gupta's post-mortem, published in January 2025, is unusually direct: "Our intuition was that pharma was a multi-trillion dollar industry that spends hundreds of billions on cutting-edge R&D... In reality, pharma — like other massive industries including video gaming — doesn't buy much software, at least not compared to the tech companies we had better intuitions about."<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[35]</a></sup>

The bottoms-up reality was a TAM of "double digit millions instead of billions."<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[30]</a></sup> This is not a rounding error — it is a difference of two to three orders of magnitude. A software business targeting a $50 million TAM cannot support venture-scale returns regardless of execution quality.

The team's attempted remedy was the first pivot: abandoning software sales and reframing as a "molecules as a service" company at YC Demo Day in March 2018.<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[16]</a></sup> This was the right directional move, but it did not resolve the underlying problem — it deferred it. Selling molecules rather than software still required pharma companies as customers, with all the procurement complexity and milestone-dependent revenue that entailed.

A contributing factor was the failure of standard ML validation metrics to resonate with pharma clients. R-squared scores — a standard measure of model fit — meant little to drug hunters evaluating whether a computational platform could actually deliver clinical candidates.<sup><a href="https://medium.com/harvard-in-tech/harvard-in-tech-ai-edition-ankit-gupta-visting-partner-at-y-combinator-and-head-of-ai-at-ginkgo-2e494e66f121">[36]</a></sup> The translation gap between what ML engineers could demonstrate and what medicinal chemists needed to see was a persistent friction that the team worked to close by hiring experienced drug hunters — but closing it took years and capital.

### Secondary Cause: Drug Development Timelines Are Structurally Incompatible With Venture Return Horizons

The pivot from software to drug development solved the TAM problem but introduced a new structural constraint. Drug development from lead candidate to clinical proof-of-concept typically takes five to ten years and costs hundreds of millions of dollars. Venture capital funds typically have seven-to-ten-year lifespans, with the expectation of returning capital within that window.

Reverie raised its Series A in February 2021 with a lead program "rapidly advancing towards the clinic."<sup><a href="https://www.prnewswire.com/news-releases/reverie-labs-raises-25m-series-a-round-to-broaden-impact-of-its-computational-kinase-drug-discovery-platform-301220854.html">[37]</a></sup> By May 2023 — more than two years later — RVL-101 had reached IND-enabling stage but had not yet filed an IND or entered human trials. The gap between "advancing towards the clinic" and "in the clinic" is where drug development companies most commonly exhaust their runway.

The virtual operating model — no physical laboratory, reliance on CROs for experimental work — was a rational capital efficiency choice that extended runway. But it also meant Reverie was dependent on external partners for the experimental data that validated its computational predictions, creating a feedback loop that was slower and less controllable than an integrated lab would have been.

The attempted remedy was the Series A itself: $25 million to extend runway and advance the pipeline. But $25 million is insufficient to carry a drug candidate from IND-enabling through Phase I and into Phase II — the clinical milestone that would have unlocked a premium Series B or partnership acquisition. The capital raised was enough to demonstrate preclinical progress, but not enough to generate the clinical data that commands premium valuations.

### Tertiary Cause: Pharma Partnership Dynamics Introduced Irreducible Uncertainty

The Roche/Genentech collaboration was Reverie's most important commercial relationship and its most significant validation. It was also a source of structural risk that the founders could not fully control.

Gupta wrote candidly about the information asymmetry inherent in pharma partnerships: "pharma companies decide not to proceed with molecules for reasons beyond drug properties, including competitive landscape, pricing signals, and trial costs."<sup><a href="https://ankitg.me/blog/2025/01/06/unfair-coins.html">[38]</a></sup> A startup cannot know why a large pharma company deprioritizes a program. The decision may reflect the quality of the molecules, or it may reflect a portfolio rebalancing, a competitive intelligence signal, or a change in therapeutic area strategy entirely unrelated to Reverie's work.

Milestone-dependent revenue is structurally unpredictable in this environment. Reverie was eligible for preclinical, clinical, and regulatory milestone payments from Roche, plus tiered royalties on eventual drug sales.<sup><a href="https://www.scienceboard.net/index.aspx?sec=sup&sub=Drug-and-Biotech/Pharma-News&pag=dis&ItemID=1012">[32]</a></sup> Whether any of those milestones were achieved before the acquisition is not publicly disclosed — the absence of any announcement of milestone payments is suggestive, though not conclusive.

The status of the Roche/Genentech collaboration at the time of the Ginkgo acquisition is unknown. Ginkgo's stated rationale for acquiring Reverie was the AI platform infrastructure, not the drug pipeline — suggesting the Roche candidates were either returned, lapsed, or transferred in a manner not publicly disclosed.

### Structural Industry Factor: The AI Drug Discovery Category Faced a Credibility Crisis

Reverie's failure cannot be fully explained by company-specific decisions. The broader AI drug discovery category experienced a credibility reckoning between 2022 and 2024 that made the financing environment for pre-clinical AI drug companies significantly more difficult.

BenevolentAI's lead program — baricitinib for atopic dermatitis — failed in Phase IIb in 2023, the first high-profile clinical failure of an AI-designed drug candidate. Recursion's stock declined more than 70% from its 2021 peak. The category-level narrative shifted from "AI will transform drug discovery" to "show us the clinical data." This shift raised the bar for Series B financing precisely when Reverie needed to raise one — and it did so in a rising interest rate environment that compressed biotech valuations broadly.

A company with RVL-101 in Phase I human trials in 2023 would have been in a materially different fundraising position than one with RVL-101 at IND-enabling stage. The difference between those two positions is approximately $50–100 million in additional capital and two to three additional years — resources Reverie did not have.

## Key Lessons

- **Bottoms-up TAM analysis is non-negotiable before committing to a software business model.** Reverie's founders estimated the pharma software market top-down — a trillion-dollar industry must buy software — and discovered only after entering YC that the real market was tens of millions of dollars, not billions. The bottoms-up calculation (roughly 10 large pharma companies buying $100K–$500K in software, plus 100 smaller companies buying $10K–$50K) would have revealed this before the company was built around the wrong model. The lesson is not generic; it is specific to industries where R&D spending is high but software procurement is low — a category that also includes defense, construction, and agriculture.

- **Pivoting from software to drug development solves one problem and creates a harder one.** Reverie's pivot from SaaS to integrated drug developer was the correct response to a small TAM, but it traded a revenue problem for a timeline problem. Drug development requires clinical proof-of-concept to command premium valuations, and clinical proof-of-concept requires more capital and more time than a typical venture fund can accommodate. Reverie raised $32 million and reached IND-enabling stage in seven years — meaningful progress, but not the Phase I data that would have unlocked a Series B in the 2022–2024 financing environment.

- **Pharma partnership revenue is not a substitute for owned pipeline progress.** The Roche/Genentech collaboration validated Reverie's science but did not provide the predictable revenue or the clinical milestones that would have supported independent financing. Milestone payments are contingent on decisions made by the partner for reasons the startup cannot observe or control. Reverie's post-mortem makes explicit what many AI drug discovery companies learned implicitly: partnership deals provide validation and upfront capital, but they do not de-risk the company's path to a Series B.

- **The virtual drug discovery model extends runway but slows the feedback loop.** Operating without a physical laboratory reduced Reverie's capital expenditure and allowed a team of 27–29 people to pursue a pipeline that would have required a much larger headcount in a traditional biotech. The tradeoff was dependence on CROs for experimental data, which slowed the iteration cycle between computational prediction and experimental validation — the core loop that improves the platform over time.

- **The most durable output of a failed startup may be human capital, not technology.** Ankit Gupta's trajectory — from Reverie CTO to Ginkgo Head of AI/ML to YC General Partner — suggests that the knowledge accumulated across seven years of building at the intersection of ML and drug discovery has compounding value that outlasted the company itself. Gupta's "Unfair Coins" post-mortem, published a year after the acquisition, is itself a form of value creation: a precise, evidence-based account of what went wrong that is more useful to the next generation of founders than most academic case studies.

## Sources

1. [Reverie Labs raises $25M Series A — PR Newswire, February 3, 2021](https://www.prnewswire.com/news-releases/reverie-labs-raises-25m-series-a-round-to-broaden-impact-of-its-computational-kinase-drug-discovery-platform-301220854.html)
2. [Ginkgo Bioworks acquires Reverie Labs platform — PR Newswire, February 28, 2024](https://www.prnewswire.com/news-releases/ginkgo-bioworks-acquires-reverie-labs-platform-enhancing-ai-driven-drug-discovery-capabilities-for-customer-programs-302073641.html)
3. [Ginkgo Bioworks provides compensation information related to recent acquisitions — PR Newswire, February 28, 2024](https://www.prnewswire.com/news-releases/ginkgo-bioworks-provides-compensation-information-related-to-recent-acquisitions-302073672.html)
4. [Harvard in Tech: Ankit Gupta profile — Medium, December 27, 2024](https://medium.com/harvard-in-tech/harvard-in-tech-ai-edition-ankit-gupta-visting-partner-at-y-combinator-and-head-of-ai-at-ginkgo-2e494e66f121)
5. [Ankit Gupta joins Y Combinator as General Partner — Vill Press, November 2, 2025](https://villpress.com/ankit-gupta-joins-y-combinator-as-general-partner/)
6. [Reverie Labs profile — Boring Business Nerd](https://www.boringbusinessnerd.com/startups/reverie-labs)
7. [9 Favorite Startups at DRF — Startups Venture Capital](https://startupsventurecapital.com/9-my-5-favorite-startups-at-drf-19b80ed97cba)
8. [Connor Duffy profile — Crunchbase](https://www.crunchbase.com/person/connor-duffy)
9. [Reverie Labs uses new machine learning algorithms to fix drug development bottlenecks — TechCrunch, March 16, 2018](https://techcrunch.com/2018/03/16/reverie-labs-uses-new-machine-learning-algorithms-to-fix-drug-development-bottlenecks/)
10. [Reverie Labs funding and investors — Tracxn](https://tracxn.com/d/companies/reverie-labs/__KK9JD-uznpt71zyBuf4NJTLFLkO2_5-bi3zK_PZZf_k/funding-and-investors)
11. [Reverie Labs company overview — Crunchbase](https://www.crunchbase.com/organization/reverie-labs/company_overview/overview_timeline)
12. [Reverie Labs raises $6.6M; virtual drug discovery company with no lab of its own — SynBioBeta, August 25, 2020](https://www.synbiobeta.com/read/a-virtual-drug-discovery-company-with-no-lab-of-its-own-partners-with-roche-to-fight-cancers-in-the-brain)
13. [Ankit Gupta, "Unfair Coins" post-mortem — ankitg.me, January 6, 2025](https://ankitg.me/blog/2025/01/06/unfair-coins.html)
14. [Reverie Labs company profile — Tracxn](https://tracxn.com/d/companies/reverie-labs/__KK9JD-uznpt71zyBuf4NJTLFLkO2_5-bi3zK_PZZf_k)
15. [Reverie Labs enters multi-target collaboration agreement with Roche — PR Newswire, July 8, 2020](https://www.prnewswire.com/news-releases/reverie-labs-enters-multi-target-collaboration-agreement-with-roche-301089930.html)
16. [Reverie Labs / Roche collaboration details — Science Board, July 8, 2020](https://www.scienceboard.net/index.aspx?sec=sup&sub=Drug&pag=dis&ItemID=1012)
17. [Ginkgo Bioworks forges three acquisition deals — Fierce Biotech, February 28, 2024](https://www.fiercebiotech.com/medtech/ginkgo-go-go-bioworks-company-forges-3-acquisition-deals)
18. [Reverie Labs company profile — YC](https://www.ycombinator.com/companies/reverie-labs)
19. [Reverie Labs company profile — Crunchbase](https://www.crunchbase.com/organization/reverie-labs)
20. [Reverie Labs company profile — CB Insights](https://www.cbinsights.com/company/reverie-labs)
21. [Reverie Labs company profile — LinkedIn](https://www.linkedin.com/company/reverie-labs)
22. [Ankit Gupta joins YC as General Partner — YC Blog, December 7, 2025](https://www.ycombinator.com/blog/welcome-ankit)
23. [Ankit Gupta on X — December 7, 2025](https://x.com/GuptaAnkitV/status/1966536311105343900)
24. [PitchBook profile — Reverie Labs](https://pitchbook.com/profiles/company/187996-42)
