# Research Report: Plasticity

## Overview

Plasticity began not as a planned startup but as a senior-year side project at the University of Pennsylvania's M&T (Management & Technology) program, a dual-degree program combining Wharton's business school with Penn Engineering. Alex Sands studied Computer Science and Management with a specialization in Entrepreneurship. His co-founder, Ajay Patel, had worked on natural language interfaces at Google; Sands had done the same at Apple, working on Siri. The two met through the M&T program itself.

Their founding insight came from a hackathon. At PennApps, Sands and Patel built GoogolPlex, a project that integrated third-party apps — Venmo, Spotify, Nest, Tesla — into Siri. The project attracted 25,000 users and coverage in Time, Forbes, and TechCrunch. <sup><a href="https://www.34st.com/article/2017/04/penn-10-alex-sands">[1]</a></sup> But the experience exposed a fundamental problem. As Patel later put it: "NLP in general is not robust" for handling complex commands and queries. <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[2]</a></sup> The existing tools, he noted, "really take a simplistic approach to understanding what a user says." <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[3]</a></sup> GoogolPlex was a proof-of-concept that the robustness problem was real — and that no one had solved it at the infrastructure level.

Sands described the origin plainly: "During my senior year, a friend and I started working on what was a side project at the time, which focused on a different approach to solving a particular problem in natural language processing." <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[4]</a></sup>

The conviction was strong enough that Sands turned down a return offer to Apple as an Engineering Product Manager to pursue Plasticity full-time. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[5]</a></sup> The pair applied to Y Combinator during their senior spring and were accepted into the Summer 2017 batch. Three days after graduating from Penn, both founders moved to San Francisco to begin the program. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[6]</a></sup>

During YC, the team considered building their own consumer personal assistant product — a natural extension of the GoogolPlex work — but explicitly decided against it. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[7]</a></sup> The choice to build infrastructure rather than a consumer product was strategically defensible: infrastructure compounds, consumer products compete on distribution. It was also, as it turned out, commercially harder.

Sands later described YC as "a crazy three month period when you're basically just heads down trying to figure out how to make your startup successful," adding that the biggest benefit was "how much it forces you to get done, and the network and the Demo Day are obviously invaluable." <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[8]</a></sup>

---

## Founding Story

### Timeline

- **2016** — Alex Sands and Ajay Patel begin working on Plasticity as a senior-year side project at Penn's M&T program <sup>[[9]](https://tracxn.com/d/companies/plasticity/__6PDhsM6I3ADrcacSWDcLrXLCumePg6ti7AE1YdmDW-4)</sup>
- **2016** — GoogolPlex hackathon project at PennApps attracts 25,000 users and coverage in Time, Forbes, and TechCrunch; reveals NLP robustness as a core unsolved problem <sup>[[1]](https://www.34st.com/article/2017/04/penn-10-alex-sands)</sup>
- **May 2017** — Plasticity accepted into Y Combinator Summer 2017 batch; Alex Sands turns down return offer to Apple <sup>[[5]](https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/)</sup>
- **June 2017** — Three days after graduating from Penn, both founders relocate to San Francisco to begin YC <sup>[[6]](https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/)</sup>
- **August 11, 2017** — TechCrunch covers Plasticity's public beta launch, describing their ambition to become a "centralized solution" for NLP <sup>[[10]](https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/)</sup>
- **August 19, 2017** — Founders publish Launch HN post; APIs move from private to public beta around YC Demo Day; seed round still not closed <sup>[[11]](https://bestofshowhn.com/yc-s17/plasticity)</sup>
- **August 22, 2017** — TechCrunch Demo Day roundup describes Plasticity as "the Twilio of NLP" and reports a signed letter of intent from DuckDuckGo worth $1.2 million
- **June 15, 2018** — Plasticity receives a $224,680 grant from the National Science Foundation <sup>[[12]](https://bouncewatch.com/explore/startup/plasticity)</sup>
- **2018** — Plasticity publishes "Magnitude: A fast, efficient universal vector embedding utility package" at EMNLP 2018 <sup>[[13]](https://ajayp.app/about/)</sup>
- **2018** — Plasticity pivots to focus primarily on government and Department of Defense customers <sup>[[14]](https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/)</sup>
- **September 24, 2020** — EX1 signs a definitive Stock Purchase Agreement to acquire Plasticity <sup>[[15]](https://www.newswire.com/news/executive-1-holding-company-to-acquire-plasticity-inc-21222689)</sup>
- **October 15–16, 2020** — Acquisition closes; Plasticity becomes a wholly-owned subsidiary of EX1; both founders retained <sup>[[16]](https://www.executive1holding.com/news/2020/12/7/executive-1-holding-company-completes-acquisition-of-plasticity-inc-furthering-investment-in-artificial-intelligence-and-natural-language-processing)</sup>
- **December 2021** — Alex Sands gives retrospective interview to Penn's Wharton M&T program describing the government pivot and acquisition <sup>[[4]](https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/)</sup>
- **2025** — Ajay Patel pursues a PhD at the University of Pennsylvania, returning to academic NLP research <sup>[[17]](https://ajayp.app/)</sup>

<media-hn url="https://news.ycombinator.com/item?id=15047929" title="Launch HN: Plasticity (YC S17) – APIs for human-like natural language interfaces" points="" comments=""></media-hn>

---

## What They Built

Plasticity built a three-part NLP API suite designed to give developers production-grade language understanding without requiring them to build their own models. The product was positioned as infrastructure — the plumbing that other applications would run on top of — rather than an end-user product.

<media-image src="https://techcrunch.com/wp-content/uploads/2017/08/gettyimages-638048690.jpg" alt="TechCrunch article header image for 'Plasticity wants to help chatbots seem less robotic'" caption="Header image from TechCrunch's August 11, 2017 article covering Plasticity's public beta launch. The article described Plasticity as using deep learning models trained on Wikipedia to help developers build more robust conversational interfaces."></media-image>

**Sapien Language Engine** handled low-level NLP tasks: named entity recognition (identifying people, places, organizations in text), syntax dependency parsing (mapping grammatical relationships between words), part-of-speech tagging, open information extraction (pulling subject-verb-object triples from sentences), and natural language generation (converting structured data back into readable text). <sup><a href="https://www.plasticity.ai/developers/">[18]</a></sup>

**Cortex Knowledge Graph** was a queryable graph of over 20 million real-world concepts, built from Wikipedia. Rather than returning keyword matches, Cortex understood natural language queries and returned structured relationships between entities — for example, understanding that "the CEO of Apple" and "Tim Cook" referred to the same entity in context. <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[10]</a></sup>

**Lingua Dialogue Engine** automated conversational dialogue flows, handling intent classification (figuring out what a user wants) and slot filling (extracting the specific parameters of that request). This was the layer that would power chatbots and voice interfaces. <sup><a href="https://www.plasticity.ai/developers/">[18]</a></sup>

The technical architecture reflected serious engineering investment. Open information extraction algorithms were written from scratch in C++, optimized for speed. <sup><a href="https://bestofshowhn.com/yc-s17/plasticity">[19]</a></sup> The team built a custom Wikipedia crawler to handle chunking and disambiguation — a decision that gave them control over their training data rather than relying on third-party datasets. <sup><a href="https://bestofshowhn.com/yc-s17/plasticity">[20]</a></sup> The base NLP layer used TensorFlow and Google's SyntaxNet module for dependency parsing. As Patel explained: "We use machine learning on the base to figure that out, and we use TensorFlow and Google's SyntaxNet module." <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[2]</a></sup>

Performance claims were aggressive. Plasticity's website stated the system could parse 6,000 sentences per second — described as over 80 times faster than competing solutions — and claimed top benchmark scores for open information extraction, coreference resolution, and slot filling. <sup><a href="https://www.plasticity.ai/">[21]</a></sup> These figures came from the company's own materials and were not independently verified.

What distinguished Plasticity from most competitors in 2017 was the depth of semantic understanding. Most NLP tools of the era used keyword matching or shallow pattern recognition. Plasticity built a graph of entities and their relationships within each sentence — a structural representation of meaning rather than a surface-level scan of words. <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[10]</a></sup> This approach would later be validated by the transformer revolution, but in 2017 it required custom infrastructure that most developers were not yet equipped to integrate.

The team also published academic research alongside the product. In 2018, Patel, Sands, and two Penn professors co-authored "Magnitude: A fast, efficient universal vector embedding utility package," presented at EMNLP 2018 — one of the top NLP conferences. <sup><a href="https://ajayp.app/about/">[13]</a></sup> The paper addressed a practical bottleneck in NLP pipelines: loading and querying word vector embeddings efficiently. This dual track of commercial product and academic research signaled genuine technical depth, though it also raised questions about where the team's primary focus lay.

---

## Market Position

### Target Customers

Plasticity's initial target was software developers building conversational interfaces — chatbots, voice assistants, and search tools — who needed NLP capabilities without building their own models. The pitch was developer-first: expose powerful NLP primitives through clean APIs, let developers compose them into applications. The analogy to Twilio was explicit in their Demo Day pitch: just as Twilio abstracted telephony infrastructure, Plasticity would abstract language understanding.

The company described serving "hundreds of companies in technology, law, and medicine" alongside government agencies. <sup><a href="https://www.linkedin.com/company/plasticityai">[22]</a></sup> This claim is undated and unverified, and it is unclear whether it reflects the commercial phase, the government phase, or both. The legal and medical verticals suggest the team recognized that structured information extraction — pulling entities and relationships from contracts, case law, or clinical notes — was a high-value use case where keyword matching clearly failed.

After the government pivot in 2018, the effective target customer shifted to federal agencies and Department of Defense contractors. Disinformation detection — using entity extraction and relationship mapping to identify coordinated inauthentic behavior — emerged as a concrete government application. <sup><a href="https://media.plasticity.ai/youtube-disinformation-report/">[23]</a></sup>

### Market Size

The NLP market in 2017 was growing but not yet mature for commercial API sales. The chatbot hype cycle of 2016–2017 had generated significant developer interest — Facebook had opened the Messenger platform to bots in 2016, and every major cloud provider was racing to release NLP services. But enterprise buyers were not yet deploying NLP at scale, and most developers were experimenting rather than paying for production-grade infrastructure. The market that Plasticity was targeting — developers willing to pay for high-quality NLP APIs — was real but small in 2017.

By 2023, the global NLP market was valued at over $18 billion and growing rapidly, driven by large language models and enterprise AI adoption. Plasticity's technical thesis — that semantic understanding mattered more than keyword matching — was correct. The market simply took longer to arrive than the company's runway allowed.

### Competition

The competitive landscape in 2017 was crowded at the surface but thin at the depth Plasticity was targeting. Google offered SyntaxNet (which Plasticity actually used as a component), AWS provided Comprehend and Lex, and IBM Watson had been marketing enterprise NLP for years. All three had larger distribution, brand recognition, and sales infrastructure than Plasticity could match.

The more direct competitive threat came from well-funded NLP startups: Wit.ai (acquired by Facebook in 2015), api.ai (acquired by Google in 2016), and Rasa (which raised $30 million by 2021). These companies competed on the dialogue layer specifically. Hugging Face, which would later dominate the NLP infrastructure space, was founded in 2016 but had not yet pivoted to its transformer-focused model hub strategy.

The chatbot hype cycle created a paradox: it generated developer interest in NLP but also flooded the market with undifferentiated tools, making it harder for Plasticity to stand out on quality alone. Most developers evaluating NLP APIs in 2017 were building simple intent classifiers, not the kind of deep semantic pipelines where Plasticity's advantages were clearest.

---

## Business Model

Plasticity operated as an API business, charging developers for access to its NLP endpoints. The model was usage-based — consistent with the Twilio analogy — where customers would pay per API call or per volume of text processed. No public pricing data is available from the commercial phase.

After the government pivot, the revenue model shifted to contract-based engagements. As Sands described it, government contracts offered structural advantages that commercial API sales could not: "The contracts are pretty large and once you get one you hold onto it for a while." <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[24]</a></sup> This is a fundamentally different business than a developer API platform — it is closer to professional services or systems integration, with revenue that is large, sticky, and opaque rather than small, recurring, and transparent.

Total disclosed VC funding was approximately $120,000 across three rounds. <sup><a href="https://tracxn.com/d/companies/plasticity/__6PDhsM6I3ADrcacSWDcLrXLCumePg6ti7AE1YdmDW-4">[25]</a></sup> The NSF grant of $224,680 in June 2018 was likely the largest single capital infusion the company received. <sup><a href="https://bouncewatch.com/explore/startup/plasticity">[12]</a></sup> No Series A was ever raised. The acquisition price by EX1 was not disclosed.

---

## Traction

Plasticity's most concrete traction data point comes from YC Demo Day in August 2017, when TechCrunch reported a signed letter of intent from DuckDuckGo worth $1.2 million — a significant early signal for a company that had just launched its public beta days earlier. This was a letter of intent, not a closed contract, and no follow-up reporting confirmed whether the deal closed.

The GoogolPlex hackathon project, which preceded Plasticity, had attracted 25,000 users and coverage in Time, Forbes, and TechCrunch. <sup><a href="https://www.34st.com/article/2017/04/penn-10-alex-sands">[1]</a></sup> This was a proof-of-concept for the founders' ability to build and distribute products, not a direct measure of Plasticity's API adoption.

The company's LinkedIn page described serving "hundreds of companies in technology, law, and medicine" alongside government agencies. <sup><a href="https://www.linkedin.com/company/plasticityai">[22]</a></sup> This figure is undated and unverified. No data on API call volume, developer signups, monthly active users, or commercial revenue is publicly available.

The NSF grant of $224,680 in June 2018 <sup><a href="https://bouncewatch.com/explore/startup/plasticity">[12]</a></sup> and the subsequent government contracts represent the clearest evidence of sustained revenue generation, though contract values were not disclosed. The fact that the company survived from 2017 to 2020 — a period when many better-funded NLP startups shut down — suggests the government pivot generated enough revenue to sustain operations, even if it did not generate venture-scale growth.

---

## Post-Mortem

Plasticity did not fail in the conventional sense — it was acquired, both founders were retained, and the technology continued operating under EX1. But the company's original mission — "making simple, powerful natural language processing technology open and accessible to companies, organizations, and developers" <sup><a href="https://www.plasticity.ai/blog/plasticity-joins-ex1/">[26]</a></sup> — was effectively abandoned. The developer platform never scaled. The acquisition was opportunistic rather than strategic. Understanding why requires examining four compounding failures.

### 1. The Commercial NLP Market Was Not Ready in 2017–2018

This is the primary cause of Plasticity's trajectory diverging from its original vision. Sands said it directly: "We found this niche in the government space and that allowed us to stay alive as a company, while other NLP companies would try to sell commercially when the market wasn't there and shut down." <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[27]</a></sup>

What specifically was missing: In 2017–2018, most enterprise buyers were not yet deploying NLP in production. The chatbot hype cycle had generated developer experimentation, but converting that experimentation into paid API usage required enterprise sales cycles that a two-person team could not run. The developers who were most interested in Plasticity's deep semantic capabilities — those building legal document analysis, medical record extraction, or intelligence analysis tools — were also the hardest to reach and the slowest to buy.

The attempted remedy was Demo Day and press coverage. TechCrunch covered the launch in August 2017, <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[10]</a></sup> and the DuckDuckGo LOI suggested the approach could work. But the seed round was still not closed as of Demo Day, <sup><a href="https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/">[28]</a></sup> and no evidence suggests the commercial pipeline materialized into sustained revenue. The market timing problem was structural, not solvable by better marketing.

### 2. Chronic Undercapitalization for an Infrastructure Play

Total disclosed VC funding was approximately $120,000 across three rounds from five investors. <sup><a href="https://tracxn.com/d/companies/plasticity/__6PDhsM6I3ADrcacSWDcLrXLCumePg6ti7AE1YdmDW-4">[25]</a></sup> Investors included Y Combinator, First Round Capital's Dorm Room Fund, and General Catalyst's Rough Draft Ventures — all credible names, but all pre-seed vehicles designed for student startups, not growth-stage infrastructure companies. <sup><a href="https://pitchbook.com/profiles/company/184718-89">[29]</a></sup> No Series A was ever raised.

The funding gap was structural. Building a competitive NLP infrastructure platform — with the engineering talent, sales motion, and compute infrastructure required to compete against Google, AWS, and well-funded startups — requires tens of millions of dollars. Plasticity was operating on hundreds of thousands. The NSF grant of $224,680 in June 2018 <sup><a href="https://bouncewatch.com/explore/startup/plasticity">[12]</a></sup> was likely larger than any single VC check the company received, and it came from a government agency rather than a growth investor.

The attempted remedy was the government pivot itself — using large, sticky government contracts as a substitute for venture capital to fund operations. This worked as a survival mechanism. Sands acknowledged the structural advantage: "The contracts are pretty large and once you get one you hold onto it for a while." <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[24]</a></sup> But government contract revenue is opaque, slow-growing, and unattractive to most VCs — meaning the pivot that kept the company alive also made it harder to raise the growth capital that would have been needed to return to the original developer-platform vision.

### 3. The Government Pivot Foreclosed the Original Mission

The pivot to government and DoD customers in 2018 was the right decision for survival but the wrong decision for the company's stated mission. It created a path dependency: once Plasticity's revenue was concentrated in government contracts, its product roadmap, hiring, and sales motion all oriented toward that customer base. The developer platform — the open, accessible NLP infrastructure that the founders had set out to build — became secondary.

The evidence is in the acquisition itself. EX1 is a federal IT holding company in Tysons, Virginia — the geographic center of the government contracting ecosystem. <sup><a href="https://www.newswire.com/news/executive-1-holding-company-to-acquire-plasticity-inc-21222689">[15]</a></sup> Patel's statement at acquisition focused entirely on EX1's federal customer base: "We're impressed with the large number of federal, Department of Defense, and commercial customers EX1 serves." <sup><a href="https://www.newswire.com/news/executive-1-holding-company-completes-acquisition-of-plasticity-ai-21236902">[30]</a></sup> There was no mention of the developer platform, the public APIs, or the open-access mission. The company that was acquired was a government NLP contractor, not the "Twilio of NLP" that had pitched on Demo Day.

The attempted remedy — maintaining both commercial and government tracks simultaneously — appears not to have worked. No evidence suggests the commercial developer platform continued to grow after the government pivot. The pivot was reactive, not strategic: Sands described it as "we found this niche," not as a deliberate repositioning. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[27]</a></sup>

### 4. Academic Research as a Competing Priority

Plasticity published "Magnitude: A fast, efficient universal vector embedding utility package" at EMNLP 2018, co-authored by both founders and two Penn professors. <sup><a href="https://ajayp.app/about/">[13]</a></sup> EMNLP is one of the top NLP conferences. Publishing there requires significant research investment — writing, experimentation, peer review — that competes directly with product development and sales.

This is a double-edged signal. The publication demonstrated genuine technical depth and contributed to the field. But for a two-person startup with no Series A, the opportunity cost of academic publishing is high. The time spent on Magnitude was time not spent closing commercial customers, building sales infrastructure, or raising growth capital.

The outcome is consistent with this tension: Ajay Patel returned to academic NLP research after the acquisition, pursuing a PhD at Penn. <sup><a href="https://ajayp.app/">[17]</a></sup> The academic track was not a detour from Plasticity — it was, in retrospect, the destination.

### The Acquisition: Opportunistic, Not Planned

Sands was candid about how the exit happened: "We didn't start the company with the idea that we were going to sell it — that part of it just happened. Throughout working on the company, we talked to other companies that were interested in acquisition of what we were working on." <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[31]</a></sup>

The acquisition price was not disclosed. Patel's subsequent return to academia suggests the financial outcome was not transformative. The company's original mission — open, accessible NLP for developers — was effectively closed when it became a wholly-owned subsidiary of a federal IT holding company. The technology survived. The vision did not.

---

## Key Lessons

- **Infrastructure businesses require growth capital, not just seed capital.** Plasticity raised approximately $120,000 in VC funding for a product competing against Google, AWS, and well-funded startups. <sup><a href="https://tracxn.com/d/companies/plasticity/__6PDhsM6I3ADrcacSWDcLrXLCumePg6ti7AE1YdmDW-4">[25]</a></sup> The NSF grant of $224,680 <sup><a href="https://bouncewatch.com/explore/startup/plasticity">[12]</a></sup> was likely the company's largest single capital infusion. Without a Series A, Plasticity could not hire the sales, marketing, or engineering talent needed to compete at scale. YC and Demo Day provided press and initial credibility but did not translate into the growth-stage funding an infrastructure play requires.

- **A survival pivot can foreclose the original mission.** The government pivot kept Plasticity alive when commercial NLP sales stalled, but it redirected the company's product roadmap, hiring, and sales motion toward a customer base that was incompatible with the original developer-platform vision. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[27]</a></sup> The acquisition by a federal IT holding company was the logical conclusion of that pivot. Founders should evaluate survival pivots not just on whether they generate revenue, but on whether they preserve optionality for the original mission.

- **Technical correctness is not sufficient for commercial timing.** Plasticity's core thesis — that NLP required semantic understanding rather than keyword matching — was validated by the transformer revolution that followed. But the commercial market for developer NLP tools was not mature enough in 2017–2018 to absorb what Plasticity had built. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[27]</a></sup> Being technically right too early produces the same outcome as being technically wrong: insufficient revenue to sustain the company through to market maturity.

- **Academic publishing and startup execution compete for the same resource: founder time.** Plasticity published at EMNLP 2018 while simultaneously trying to close commercial customers and navigate a government pivot. <sup><a href="https://ajayp.app/about/">[13]</a></sup> For a two-person team with no growth capital, the opportunity cost of research publication is high. The subsequent return of a co-founder to academic NLP research suggests the research track was a genuine competing priority, not a side project.

- **Government contracts are a viable survival mechanism but a poor substitute for venture trajectory.** Sands correctly identified that government contracts offered large deal sizes and high retention. <sup><a href="https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/">[24]</a></sup> But DoD-focused revenue is opaque, slow-growing, and unattractive to most growth-stage VCs — meaning the pivot that kept Plasticity alive also made it structurally incompatible with the venture funding model it would have needed to scale the developer platform.

---

## Sources

1. [Penn 34th Street — Alex Sands profile (April 2017)](https://www.34st.com/article/2017/04/penn-10-alex-sands)
2. [TechCrunch — "Plasticity wants to help chatbots seem less robotic" (August 11, 2017)](https://techcrunch.com/2017/08/11/plasticity-wants-to-help-chatbots-seem-less-robotic/)
3. [Wharton M&T Entrepreneur Feature — Alex Sands (December 2021)](https://fisher.wharton.upenn.edu/mt-for-life/mt-entrepreneur-feature-alex-sands-mt-class-of-2017/)
4. [Best of Show HN — Plasticity YC S17 Launch HN archive](https://bestofshowhn.com/yc-s17/plasticity)
5. [Tracxn — Plasticity company profile](https://tracxn.com/d/companies/plasticity/__6PDhsM6I3ADrcacSWDcLrXLCumePg6ti7AE1YdmDW-4)
6. [Y Combinator — Plasticity company directory](https://www.ycombinator.com/companies/plasticity)
7. [PitchBook — Plasticity investor profile](https://pitchbook.com/profiles/company/184718-89)
8. [BounceWatch — Plasticity funding data](https://bouncewatch.com/explore/startup/plasticity)
9. [Newswire — EX1 signs agreement to acquire Plasticity (September 24, 2020)](https://www.newswire.com/news/executive-1-holding-company-to-acquire-plasticity-inc-21222689)
10. [Executive 1 Holding Company — Acquisition completion announcement (October 2020)](https://www.executive1holding.com/news/2020/12/7/executive-1-holding-company-completes-acquisition-of-plasticity-inc-furthering-investment-in-artificial-intelligence-and-natural-language-processing)
11. [Newswire — EX1 completes acquisition of Plasticity AI (October 16, 2020)](https://www.newswire.com/news/executive-1-holding-company-completes-acquisition-of-plasticity-ai-21236902)
12. [Plasticity blog — "Plasticity Joins EX1"](https://www.plasticity.ai/blog/plasticity-joins-ex1/)
13. [Ajay Patel personal website](https://ajayp.app/)
14. [Ajay Patel — About/research page](https://ajayp.app/about/)
15. [Plasticity developers page (archived)](https://www.plasticity.ai/developers/)
16. [Plasticity homepage (archived)](https://www.plasticity.ai/)
17. [Plasticity demo page (archived)](https://www.plasticity.ai/demo/)
18. [Plasticity disinformation report](https://media.plasticity.ai/youtube-disinformation-report/)
19. [LinkedIn — Plasticity AI company page](https://www.linkedin.com/company/plasticityai)
20. [Hacker News — Launch HN: Plasticity (YC S17)](https://news.ycombinator.com/item?id=15047929)
21. [TechCrunch — YC S17 Demo Day 2 roundup (August 22, 2017)](https://techcrunch.com/2017/08/22/yc-demo-day-s17-day-2/)
22. [Wayback Machine — plasticity.ai archive index (2017)](https://web.archive.org/web/20171001000000*/plasticity.ai)
