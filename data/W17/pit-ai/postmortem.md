# Research Report: Pit.AI

## Overview

Yves-Laurent Kom Samo arrived at Pit.AI with credentials that were unusual even by YC standards. He spent two years at Goldman Sachs as an Equities Algorithmic Trading Strategist beginning in 2010, then moved to JPMorgan Chase as an FX Quant Trader in 2012. <sup><a href="https://contactout.com/Yves-Laurent-SAMO-83532239">[1]</a></sup> In 2013, he left finance to pursue a PhD in Machine Learning at the University of Oxford, where he was a Google Fellow in Machine Learning and affiliated with the Oxford-Man Institute of Quantitative Finance—an academic center specifically focused on applying quantitative methods to financial markets. <sup><a href="https://www.robots.ox.ac.uk/Ylks/">[2]</a></sup>

That combination—practitioner experience at two of the world's largest investment banks, followed by three years of frontier ML research at an institution purpose-built for quantitative finance—gave Kom Samo a specific and pointed view of what was broken in the industry. Traditional quant funds, in his framing, required a human to first postulate a trading hypothesis before machine learning could be applied to test it. The hypothesis-generation step was the bottleneck: it was slow, biased, and limited by human intuition. His insight was to eliminate it entirely.

Kom Samo completed his PhD in 2016 and participated in Entrepreneur First's Batch 7 before joining Y Combinator's Winter 2017 cohort. <sup><a href="https://golden.com/wiki/Pit.AI_Technologies-NMGKGN9">[3]</a></sup> The dual accelerator path—EF followed by YC—suggests he was actively seeking institutional validation and network before launch, a pattern consistent with someone building toward a regulated financial product rather than a consumer app.

Pit.AI Technologies was formally incorporated on December 12, 2016. <sup><a href="https://golden.com/wiki/Pit.AI_Technologies-NMGKGN9">[4]</a></sup> The founding vision was explicit: use AI to build what Kom Samo called "AI-Quants"—systems that generate trading hypotheses directly from data—and charge limited partners no management fees, collecting only carry on performance. <sup><a href="https://www.ycombinator.com/companies/pit-ai">[5]</a></sup> As he described it: "I am the Founder and CEO of Pit.AI Technologies, a Silicon Valley AI startup (hedge fund) backed by Y Combinator aiming at solving intelligence for investment management, and getting rid of hedge fund management fees." <sup><a href="https://www.robots.ox.ac.uk/Ylks/">[6]</a></sup>

The ambition was structural, not incremental. Pit.AI was not trying to build a better quant tool for existing funds. It was trying to replace the human judgment layer of the entire asset management industry.

<media-tweet url="https://x.com/Dr_YLKS" author="@Dr_YLKS" date="2017-06-11" text="Founder & CEO @kxytechnologies | Prev: PhD Fellow in ML @GoogleAI | @ycombinator alumn | PhD in ML @UniofOxford | Quant @GoldmanSachs"></media-tweet>

---

## Founding Story

### Timeline

- **2010** — Yves-Laurent Kom Samo joins Goldman Sachs as Equities Algorithmic Trading Strategist <sup>[[1]](https://contactout.com/Yves-Laurent-SAMO-83532239)</sup>
- **2012** — Moves to JPMorgan Chase as FX Quant Trader <sup>[[1]](https://contactout.com/Yves-Laurent-SAMO-83532239)</sup>
- **2013** — Begins PhD in Machine Learning at University of Oxford as a Google Fellow; affiliates with Oxford-Man Institute of Quantitative Finance <sup>[[2]](https://www.robots.ox.ac.uk/Ylks/)</sup>
- **2016** — Completes Oxford PhD; participates in Entrepreneur First Batch 7 <sup>[[2]](https://www.robots.ox.ac.uk/Ylks/)</sup>
- **December 12, 2016** — Pit.AI Technologies formally founded <sup>[[4]](https://golden.com/wiki/Pit.AI_Technologies-NMGKGN9)</sup>
- **January 2017** — Pit.AI joins Y Combinator Winter 2017 batch <sup>[[7]](https://www.ycombinator.com/companies/pit-ai)</sup>
- **March 21, 2017** — Pit.AI presents at YC W17 Demo Day 2; TechCrunch covers the company; seed round of ~$120K from Y Combinator and Zillionize closes <sup>[[8]](https://pitchbook.com/profiles/company/178851-88)</sup>

<media-hn url="https://news.ycombinator.com/item?id=13960911" title="Pit.ai – Automatically mining trading strategies (YC W17 Demo Day)" points="null" comments="null"></media-hn>

- **March 21, 2017** — Founder publicly states models are running without real money and projects live trading within one year <sup>[[9]](https://techcrunch.com/2017/03/21/aihedgefund/)</sup>
- **June 2017** — Founder joins Twitter (@Dr_YLKS) during the YC batch period
- **July 2018** — Pit.AI launches Research Paper Series on Medium, articulating philosophy on AI in finance <sup>[[10]](https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12)</sup>
- **March 6, 2020** — Founder publishes Medium post on "finance-first machine learning research," citing noise in financial data and cultural obstacles as core challenges <sup>[[10]](https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12)</sup>
- **January 2021** — Founder's tenure at Pit.AI ends (inferred); KXY Technologies founded by Kom Samo <sup>[[11]](https://www.zoominfo.com/p/Yves-laurent-Samo/-1035690918)</sup>
- **2021** — Pit.AI Technologies listed as permanently closed by Crunchbase; YC lists status as Inactive <sup>[[12]](https://www.crunchbase.com/organization/pit-ai-technologies)</sup>

---

## What They Built

Pit.AI's core product was an AI-powered trading system designed to automate the entire research pipeline of a hedge fund—from data ingestion to strategy generation to portfolio construction—without requiring a human analyst to propose a hypothesis first.

<media-image src="https://techcrunch.com/wp-content/uploads/2017/03/gettyimages-530446329.jpg" alt="TechCrunch article header image for Pit.AI coverage — stock market trading floor" caption="TechCrunch's March 21, 2017 article 'Pit.ai puts a financial twist on reinforcement learning to outperform hedge funds' — the primary press coverage of Pit.AI at YC W17 Demo Day."></media-image>

The technical architecture centered on a variant of reinforcement learning (RL). In standard supervised machine learning, a model is trained to predict a specific output—say, whether a stock will go up tomorrow. Pit.AI's approach was different. Rather than predicting per-state returns, its RL system evaluated trading strategies holistically, optimizing directly for portfolio-level metrics like the Sharpe ratio (a measure of risk-adjusted return) and maximum drawdown (the largest peak-to-trough loss). <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[13]</a></sup> The system treated strategy selection as a sequential decision problem: the agent learned which actions to take across time to maximize a reward function defined in terms of real investment performance metrics.

This was a meaningful technical distinction. Most quant funds—even those using machine learning—still rely on human researchers to generate the initial trading idea. A researcher might hypothesize that momentum in one asset class predicts reversals in another, then use ML to test and refine that hypothesis. Pit.AI's pipeline was designed to skip that step entirely. Its "AI-Quants" were meant to surface trading hypotheses directly from large-scale data, without human priors. <sup><a href="https://www.ycombinator.com/companies/pit-ai">[14]</a></sup>

To train and validate these models, Pit.AI participated in the Fintech Sandbox program, which gave early-stage fintech startups access to institutional-grade financial data. <sup><a href="https://www.fintechsandbox.org/startup/pit-ai/">[15]</a></sup> The specific data sources used are not publicly documented, but Fintech Sandbox partnerships typically include market data, alternative data, and historical tick data from providers like Bloomberg, Nasdaq, and ICE.

The business model innovation was as central to the pitch as the technology. Pit.AI planned to charge limited partners no management fees—the standard 2% annual fee on AUM that hedge funds collect regardless of performance—and instead collect only carry, meaning a percentage of profits. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[16]</a></sup> The argument was that management fees misalign incentives: they reward funds for growing AUM, not for generating returns. A carry-only structure would only pay Pit.AI when its investors made money.

By July 2018, the company launched a Research Paper Series, publishing on Medium under the Pit.AI Technologies publication. The series articulated the company's philosophy on AI in finance and argued against what the founder called "dogmatic modeling paradigms" in the industry. <sup><a href="https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12">[10]</a></sup> This shift toward open research publication—roughly 16 months after Demo Day—was the last significant public output from the company before its closure.

---

## Market Position

### Target Customers

Pit.AI's target customers were institutional and high-net-worth limited partners—the investors who allocate capital to hedge funds. The company was not selling software to existing funds; it was positioning itself as a fund, competing directly for LP allocations. This meant its customers were endowments, family offices, fund-of-funds, and accredited individual investors who would commit capital to Pit.AI's strategy in exchange for a share of returns.

The secondary audience, implicit in the Research Paper Series, was the quantitative finance research community. By publishing on AI methodology in finance, Pit.AI was also building credibility with institutional allocators who evaluate funds partly on the intellectual rigor of their investment process.

### Market Size

The global hedge fund industry managed approximately $3.2 trillion in assets under management as of 2017, with quantitative and systematic strategies representing a growing share of that total. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[17]</a></sup> The specific segment Pit.AI was targeting—AI-native, systematic long/short equity or multi-asset strategies—was nascent but attracting significant institutional interest following the success of firms like Two Sigma and Renaissance Technologies.

The fee compression trend was real and measurable. Average hedge fund management fees had declined from approximately 1.6% in 2008 to 1.4% by 2017, and performance fees from 19.2% to 17.4% over the same period, as LPs pushed back on the traditional 2-and-20 structure. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[17]</a></sup> Pit.AI's carry-only model was a direct response to this trend.

### Competition

Pit.AI's competitive landscape had two distinct layers.

The first was established quantitative hedge funds: Renaissance Technologies, Two Sigma, D.E. Shaw, and AQR. These firms had decades of track records, billions in AUM, and hundreds of researchers. They were not direct competitors in the LP market—no institutional allocator would compare a pre-AUM two-person startup to Renaissance—but they defined the performance benchmark that Pit.AI's models would eventually need to clear.

The second layer was the emerging class of AI-native hedge fund startups, several of which were better-capitalized and further along. Numerai, founded in 2015, had already built a novel crowdsourced model structure and raised institutional backing. Sentient Technologies had raised over $100 million to apply evolutionary algorithms to trading. Aidyia, a Hong Kong-based AI fund, had launched live trading by 2017. Each of these competitors had either more capital, a live track record, or a differentiated go-to-market strategy that avoided the direct LP fundraising problem Pit.AI faced.

Pit.AI's technical differentiation—assumption-free RL applied to strategy-level optimization rather than return prediction—was genuine. But differentiation at the model architecture level is difficult to communicate to LP allocators, who evaluate funds primarily on audited returns, risk controls, team size, and operational infrastructure. On all of those dimensions, Pit.AI was at a structural disadvantage relative to both incumbents and better-funded peers.

---

## Business Model

Pit.AI planned to operate as a hedge fund, generating revenue exclusively through performance fees (carry) on LP capital. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[16]</a></sup> The company explicitly rejected management fees, which are typically charged as an annual percentage of AUM regardless of performance.

This model had a fundamental cash flow problem for a pre-AUM startup. Management fees exist partly because they cover operating costs—salaries, data, infrastructure, compliance—during periods when a fund is not generating performance. A carry-only fund earns nothing until it has LP capital deployed and generating positive returns. For Pit.AI, that meant the company needed to raise LP capital, deploy it, generate auditable returns, and then collect carry—all before its $120,000 in seed funding ran out. <sup><a href="https://pitchbook.com/profiles/company/178851-88">[8]</a></sup>

No evidence suggests Pit.AI ever raised a subsequent funding round or secured LP commitments. The company remained at two employees throughout its operating life, <sup><a href="https://www.ycombinator.com/companies/pit-ai">[18]</a></sup> suggesting it never reached the operational scale required to run a compliant fund management operation.

---2f:T538,At YC W17 Demo Day in March 2017, Pit.AI's models were running on paper—without real money—and the founder projected live trading within one year. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[9]</a></sup> That projection was apparently never met. No evidence of a live fund launch, LP capital raise, or AUM figure appears anywhere in the public record.

The company raised a single seed round of $120,000 from Y Combinator and Zillionize in March 2017. <sup><a href="https://pitchbook.com/profiles/company/178851-88">[8]</a></sup> No subsequent funding rounds were recorded on Crunchbase, PitchBook, or CB Insights. <sup><a href="https://www.cbinsights.com/company/pitai/financials">[19]</a></sup>

The team remained at two employees for the entirety of its known operating life. <sup><a href="https://www.ycombinator.com/companies/pit-ai">[18]</a></sup> The company's official Twitter account, @PitAITech, was created in July 2018—more than a year after Demo Day—and published zero tweets before the company closed. The account had 39 followers at the time of its last known state.

The Research Paper Series launched in July 2018 was the company's most substantive public output. No published academic papers, institutional partnerships, or commercial outcomes linked to the series have been identified.

---30:T1986,

## Traction

Pit.AI closed quietly in early 2021, approximately four years after its YC Demo Day, with no public shutdown announcement, no post-mortem, and no investor statement. <sup><a href="https://www.crunchbase.com/organization/pit-ai-technologies">[12]</a></sup> The founder moved on to found KXY Technologies and later joined Google as a Senior Staff Machine Learning Engineer. <sup><a href="https://www.zoominfo.com/p/Yves-laurent-Samo/-1035690918">[11]</a></sup> The absence of any public explanation makes definitive causal analysis impossible, but the evidence points to several compounding failures.

### The Business Model Required LP Capital Before It Could Generate Revenue

The most structurally fatal decision Pit.AI made was to operate as an actual hedge fund rather than as a software or data company. This choice meant the company's entire revenue model depended on first raising LP capital, then deploying it, then generating auditable returns, and only then collecting carry. Every step in that chain required clearing a bar that a two-person, $120K startup was not equipped to clear.

Institutional LP allocators—endowments, family offices, fund-of-funds—require a minimum track record before committing capital. The industry standard is typically 12–24 months of audited live returns, a compliance infrastructure (SEC registration or exemption, a prime broker relationship, an administrator), and a team large enough to handle operations, risk management, and investor relations separately from portfolio management. Pit.AI had none of these at Demo Day, and its $120,000 in seed funding was insufficient to build them. <sup><a href="https://pitchbook.com/profiles/company/178851-88">[8]</a></sup>

The carry-only fee structure compounded this problem. Management fees—the 2% annual charge that Pit.AI explicitly rejected—exist in part because they fund operations during the pre-performance phase. By eliminating them, Pit.AI removed the only revenue stream available to a fund before it starts generating returns. The company had no bridge between its seed capital and its first dollar of carry. No evidence suggests the team attempted to address this by raising a larger seed round, seeking a strategic partnership with an existing fund, or pivoting to a software licensing model.

### The Technical Timeline Was Underestimated

The founder himself provided the clearest articulation of the second failure in a March 2020 Medium post: "financial markets are noisy, much noisier than physical systems, so much so that overall, for the same model complexity, one would need a lot more financial data than physical data to achieve the same level of accuracy." <sup><a href="https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12">[20]</a></sup>

This is a precise statement of a well-known problem in quantitative finance: the signal-to-noise ratio in financial data is extremely low. A reinforcement learning system trained on physical systems—robotics, game-playing, logistics—can iterate quickly because the environment is relatively stationary and the reward signal is dense. Financial markets are non-stationary (the relationships between variables change over time), adversarial (other participants adapt to and arbitrage away any detectable pattern), and sparse in signal (a strategy that works 52% of the time is exceptional). Building an RL system that reliably outperforms on these dimensions requires far more data, far more compute, and far more iteration time than the YC 3-month batch cycle assumed.

The March 2017 projection of live trading within one year was almost certainly optimistic given this constraint. The Research Paper Series launched in July 2018—16 months after Demo Day—may represent the team's recognition that the models were not ready for live deployment and that publishing research was a way to build credibility while continuing to iterate. But no evidence suggests the research series attracted LP interest or accelerated the technical timeline.

### The Market Was Not Ready to Trust an AI-Native Fund Without a Track Record

Kom Samo identified a third obstacle in the same 2020 post: "cultural and social obstacles" to an AI revolution in finance, including "noise from AI hype and dogmatic modeling paradigms." <sup><a href="https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12">[21]</a></sup> This is a candid acknowledgment that the institutional finance community was skeptical of AI-native investment approaches in 2017–2020, and that the hype cycle around AI was actively working against credibility with sophisticated allocators.

LP allocators in 2017 had seen a wave of AI-in-finance pitches and were increasingly skeptical of claims that were not backed by live returns. The very language Pit.AI used—"solving intelligence for investment management"—was the kind of framing that sophisticated institutional investors had learned to discount. The company's response was the Research Paper Series, which positioned Pit.AI as a serious research organization rather than a hype-driven startup. But publishing on Medium, without peer-reviewed academic papers or institutional co-authors, was unlikely to move the needle with the endowments and family offices that Pit.AI needed to convince.

### Team Size Made Execution Impossible

Pit.AI remained at two employees throughout its operating life. <sup><a href="https://www.ycombinator.com/companies/pit-ai">[18]</a></sup> Running a hedge fund—even a small one—requires simultaneous execution across model research, data engineering, compliance, investor relations, legal, and operations. A two-person team cannot staff these functions. The founder's Oxford academic page included a March 2017 hiring announcement, suggesting he recognized the team needed to grow. But no evidence of successful hires appears in the public record, and the company's headcount never increased above two.

The $120,000 seed round was the binding constraint. At San Francisco salary levels in 2017, $120,000 covered roughly three to four months of a single senior engineer's compensation, let alone the compliance infrastructure, data costs, and legal fees required to launch a registered fund. Without a follow-on raise—which would have required demonstrating progress toward live trading—the team could not grow, and without team growth, the company could not make progress toward live trading. The loop was closed.

---

## Post-Mortem

### Key Lessons

- **Operating as a regulated financial product requires a different capital structure than a software startup.** Pit.AI raised $120,000 to build a hedge fund—a product category that requires audited track records, compliance infrastructure, prime broker relationships, and LP relations before generating a dollar of revenue. <sup><a href="https://pitchbook.com/profiles/company/178851-88">[8]</a></sup> Startups entering regulated financial services need to either raise enough capital to clear the compliance threshold or find a go-to-market path (licensing, white-labeling, B2B SaaS) that generates revenue before the regulatory burden is fully loaded.

- **Fee model innovation that eliminates operating revenue is a structural liability for pre-revenue companies.** Pit.AI's carry-only model was intellectually coherent and LP-friendly, but it removed the management fee revenue that traditional funds use to cover costs during the pre-performance phase. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[16]</a></sup> A startup with no AUM and no management fees has no bridge between seed capital and first revenue. Innovative fee structures need to be paired with a financing plan that accounts for the gap.

- **The signal-to-noise problem in financial ML is a genuine technical constraint, not a marketing challenge.** The founder's own acknowledgment that financial data requires "a lot more data than physical data to achieve the same level of accuracy" <sup><a href="https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12">[20]</a></sup> points to a timeline mismatch between the pace of ML research iteration and the pace of LP fundraising. Companies building ML systems for financial markets should plan for longer research cycles and more capital than comparable ML applications in other domains.

- **Credibility-building through research publication is a slow substitute for live returns.** The Research Paper Series launched in July 2018 was a reasonable response to the credibility gap, but institutional LP allocators evaluate funds on audited performance, not Medium posts. <sup><a href="https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12">[10]</a></sup> For an AI-native fund, the fastest path to LP credibility is a small live track record—even with a friends-and-family fund or a prop trading account—not open research contribution.

- **The YC batch model is poorly suited to businesses that require regulatory approval and LP fundraising before launch.** YC's 3-month cycle and Demo Day format are optimized for software products that can show user growth or revenue within weeks. Pit.AI's product required 12–24 months of live returns before it could raise LP capital. <sup><a href="https://techcrunch.com/2017/03/21/aihedgefund/">[9]</a></sup> The mismatch between the accelerator's feedback loop and the fund's launch timeline left Pit.AI in a permanent pre-launch state that its seed funding could not sustain.

---

## Sources

1. [ContactOut – Yves-Laurent Kom Samo profile (career history)](https://contactout.com/Yves-Laurent-SAMO-83532239)
2. [University of Oxford – Yves-Laurent Kom Samo academic homepage](https://www.robots.ox.ac.uk/Ylks/)
3. [Golden.com – Pit.AI Technologies wiki entry](https://golden.com/wiki/Pit.AI_Technologies-NMGKGN9)
4. [Y Combinator – Pit.AI company directory listing](https://www.ycombinator.com/companies/pit-ai)
5. [TechCrunch – "Pit.ai puts a financial twist on reinforcement learning to outperform hedge funds" (March 21, 2017)](https://techcrunch.com/2017/03/21/aihedgefund/)
6. [TechCrunch – YC W17 Demo Day 2 full roundup (March 21, 2017)](https://techcrunch.com/2017/03/21/demo-day-y-combinator/)
7. [PitchBook – Pit.AI Technologies company profile](https://pitchbook.com/profiles/company/178851-88)
8. [CB Insights – Pit.AI Technologies financials](https://www.cbinsights.com/company/pitai/financials)
9. [Fintech Sandbox – Pit.AI startup profile](https://www.fintechsandbox.org/startup/pit-ai/)
10. [Medium / KXY Technologies – "The Case For Finance-First Machine Learning Research" by Yves-Laurent Kom Samo (March 6, 2020)](https://medium.com/kxytechnologies/the-case-for-finance-first-machine-learning-research-91cdc8492c12)
11. [ZoomInfo – Yves-Laurent Kom Samo profile](https://www.zoominfo.com/p/Yves-laurent-Samo/-1035690918)
12. [Crunchbase – Pit.AI Technologies organization page](https://www.crunchbase.com/organization/pit-ai-technologies)
13. [Wellfound (AngelList) – Pit.AI Technologies company profile](https://wellfound.com/company/pitaitechnologies)
14. [Medium – Yves-Laurent Kom Samo author page](https://medium.com/@Dr_YLKS/about)
15. [Hacker News – "Pit.ai – Automatically mining trading strategies (YC W17 Demo Day)"](https://news.ycombinator.com/item?id=13960911)
