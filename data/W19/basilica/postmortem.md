# Research Report: Basilica

## Overview

Basilica was a San Francisco-based developer API company founded on December 15, 2018, and part of Y Combinator's Winter 2019 batch.<sup><a href="https://www.crunchbase.com/organization/basilica">[1]</a></sup><sup><a href="https://www.ycombinator.com/companies/basilica">[2]</a></sup> The company built an embedding API that converted images and text into high-dimensional numerical vectors — the mathematical representations that power machine learning classifiers — allowing developers without deep ML expertise to build accurate AI models using roughly 1,000 labeled examples instead of the 1 million typically required.<sup><a href="https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/">[7]</a></sup>

Basilica was killed by platform aggregation. The core value it offered — pre-trained neural representations accessible via a simple API — was absorbed for free by Google (BERT), OpenAI, and Hugging Face before Basilica could build the domain-specific moats or network effects it promised. The competitive clock started running before the company even entered YC: Google released BERT one month before Basilica's public launch.

Basilica raised only its YC pre-seed, estimated at approximately $150K,<sup><a href="https://www.apollo.io/companies/Basilica/5da3d42d2fc58300011d26f0">[16]</a></sup> and never disclosed a follow-on round. The company quietly wound down — no shutdown announcement, no post-mortem, no acqui-hire. Jorge Silva moved to Figma as a Senior Staff Software Engineer;<sup><a href="https://www.crunchbase.com/person/jorge-silva-ff75">[22]</a></sup> Eric Fung founded Colega AI, an AI startup for small business social media marketing in Asia;<sup><a href="https://thecoolpeople.substack.com/p/i-left-sf-to-build-in-asias-food">[23]</a></sup> Michael Lucy's post-Basilica trajectory remains unknown.

---

## Founding Story

Basilica was founded by Michael Lucy, Jorge Silva, and Eric Fung — though the exact team composition at any given moment is slightly ambiguous. The YC company directory lists only two team members,<sup><a href="https://www.ycombinator.com/companies/basilica">[3]</a></sup><sup><a href="https://www.ycombinator.com/companies/basilica">[4]</a></sup> while Crunchbase adds Fung as a third co-founder. Whether Fung was a co-founder from day one or joined and departed early is not documented in any public source.

The founders came from engineering backgrounds at recognizable institutions — Lucy from the University of Chicago,<sup><a href="https://www.crunchbase.com/person/michael-lucy">[4]</a></sup> Silva from the University of Puerto Rico,<sup><a href="https://www.crunchbase.com/person/jorge-silva-ff75">[5]</a></sup> and Fung from Penn State.<sup><a href="https://www.crunchbase.com/person/eric-fung-2fac">[6]</a></sup> Silva had prior engineering experience at MuleSoft, Runnable, and RethinkDB before Basilica — a background in developer infrastructure that directly informed the product's API-first design.<sup><a href="https://github.com/thejsj">[21]</a></sup> No prior ML research credentials are documented for any of the three founders, which is relevant context: Basilica was not a research lab spinning out novel model architectures. It was an engineering team building accessible infrastructure on top of existing deep learning advances.

The founding insight was practical and well-timed — at least in theory. By late 2018, pre-trained neural networks had demonstrated that the representations learned on large datasets (ImageNet, large text corpora) transferred remarkably well to new tasks with small amounts of labeled data. This "transfer learning" capability was real and powerful, but accessing it required ML expertise that most software developers lacked: setting up GPU infrastructure, selecting and loading model weights, writing inference pipelines. Basilica's bet was that there was a large market of developers who wanted the output of transfer learning — accurate classifiers from small datasets — without the infrastructure overhead.

The team was building in public before they even entered YC. On November 19, 2018 — nearly four months before Demo Day — they posted a "Show HN" on Hacker News, publicly launching the API and inviting developer feedback.<sup><a href="https://news.ycombinator.com/item?id=18346553">[26]</a></sup> The stated vision was ambitious: "word2vec for anything" — a universal embedding layer for every data modality, starting with images and text and expanding from there.<sup><a href="https://news.ycombinator.com/item?id=18346553">[8]</a></sup> The founders described their goal as making the power of deep learning accessible to any developer, regardless of ML background.

The early public launch was a double-edged move. It demonstrated genuine builder instincts and a desire for real-world validation over stealth development. But it also exposed the product to immediate competitive scrutiny at the worst possible moment: Google had released BERT just weeks earlier, and the Hacker News community was quick to point out the implications. The feedback the founders received on that November 2018 thread was, in effect, a preview of the market dynamics that would eventually end the company.

No founder has published a post-mortem or public reflection on what went wrong. The silence is itself informative.

---

## Timeline

- **November 2018** — Google releases BERT, providing state-of-the-art text embeddings for free — one month before Basilica's public launch.<sup>[[20]](https://news.ycombinator.com/item?id=18350270)</sup>
- **November 19, 2018** — Basilica posts "Show HN: Basilica – Word2vec for anything" on Hacker News, publicly launching the embedding API before entering YC. Commenters immediately flag BERT and GloVe 2B as free alternatives.<sup>[[26]](https://news.ycombinator.com/item?id=18346553)</sup>
- **December 15, 2018** — Basilica officially incorporated in San Francisco, California.<sup>[[1]](https://www.crunchbase.com/organization/basilica)</sup>
- **February 14, 2019** — Founders post on Hacker News that they are developing a face-specialized image embedding model, citing it as a common use case with small datasets.<sup>[[12]](https://news.ycombinator.com/item?id=19165200)</sup>
- **March 18, 2019** — Basilica pitches at YC W19 Demo Day 1. TechCrunch covers the pitch, noting the transfer learning network-effect moat claim. YC pre-seed round recorded.<sup>[[7]](https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/)</sup><sup>[[15]](https://www.crunchbase.com/organization/basilica)</sup>
- **June 6, 2019** — Basilica's R client documentation published, confirming support for both Python and R developers and a freemium API key model.<sup>[[13]](https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html)</sup>
- **December 5, 2019** — Python client documentation (v0.2.7) last published — the final recorded update to the primary client library, authored by Michael Lucy and Jorge Silva.<sup>[[24]](https://app.readthedocs.org/projects/basilica-client/downloads/pdf/latest/)</sup>
- **December 8, 2022** — Basilica's R client GitHub repository records its last update — the latest known activity from the company's technical infrastructure.<sup>[[25]](https://github.com/basilica-ai)</sup>
- **January 13, 2025** — Eric Fung described in a Substack profile as "former co-founder of Basilica (YC W19)," confirming the company is fully defunct.<sup>[[23]](https://thecoolpeople.substack.com/p/i-left-sf-to-build-in-asias-food)</sup>

---

## What They Built

Basilica's product was an embedding API: a hosted service that accepted images or text as input and returned dense numerical vectors as output. Those vectors — called embeddings — are the mathematical language of modern machine learning. They encode semantic meaning in a form that downstream classifiers can use to distinguish between categories, find similar items, or detect anomalies.

**The core mechanics.** A developer sent a JPEG image to Basilica's endpoint and received back a 2,048-dimensional vector — a list of 2,048 floating-point numbers that represented the image's content as understood by a deep neural network trained on millions of images.<sup><a href="https://basilica-client.readthedocs.io/en/latest/basilica.html">[9]</a></sup> For text, the API accepted sentences, phrases, or paragraphs and returned 512-dimensional vectors.<sup><a href="https://basilica-client.readthedocs.io/en/latest/basilica.html">[9]</a></sup> The text embedding was explicitly designed to operate at the sentence and paragraph level — capturing meaning across a full phrase rather than word-by-word, which was the limitation of earlier approaches like Word2Vec.<sup><a href="https://github.com/basilica-ai/basilica-r-client">[11]</a></sup>

**The transfer learning value proposition.** The embeddings were trained by deep neural networks on millions of data points across diverse tasks.<sup><a href="https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html">[10]</a></sup> The key insight was that these representations generalized: a network trained to recognize thousands of image categories learns visual features (edges, textures, shapes, objects) that are useful for entirely different classification tasks. A developer building a product defect detector or a medical image classifier could use Basilica's embeddings as a starting point, then train a simple classifier on top using only ~1,000 labeled examples — rather than the millions of examples needed to train a deep network from scratch.<sup><a href="https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/">[7]</a></sup>

**Developer experience.** Basilica shipped two official client libraries: a Python client (the primary interface for ML practitioners) and an R client (targeting data scientists and statisticians).<sup><a href="https://basilica-client.readthedocs.io/en/latest/basilica.html">[9]</a></sup><sup><a href="https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html">[13]</a></sup> The R client was an unusual choice for an ML API in 2019 — most ML tooling was Python-first — and suggests the team was deliberately targeting a data science audience that might be more comfortable with statistical modeling than deep learning infrastructure. The freemium model used a `SLOW_DEMO_KEY` for free-tier access, capped at 5,000 requests per week per IP address, with paid API keys available for production use.<sup><a href="https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html">[13]</a></sup>

<media-image src="https://opengraph.githubassets.com/1/basilica-ai/basilica-r-client" alt="Basilica R client GitHub repository — basilica-ai/basilica-r-client" caption="Basilica's R client repository on GitHub, taglined 'Word2vec for anything' — one of two official client libraries the team shipped. The repo's December 2022 last-update date is the latest known artifact of the company's technical activity."></media-image>

**Product roadmap signals.** As of February 2019, the team was developing a face-specialized image embedding model, citing it as a common use case where developers typically lack large labeled datasets.<sup><a href="https://news.ycombinator.com/item?id=19165200">[12]</a></sup> No public evidence confirms this model was ever released. The broader vision — embeddings for every data modality, described as "word2vec for anything"<sup><a href="https://news.ycombinator.com/item?id=18346553">[8]</a></sup> — was never realized beyond images and text.

**The proposed moat.** At Demo Day, Basilica claimed a network-effect defense: by aggregating embedding requests across clients in the same vertical, the system could fine-tune representations for domain-specific tasks, improving accuracy for each customer as the overall customer base grew.<sup><a href="https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/">[14]</a></sup> This was the right strategic instinct — domain specificity was the only position that free general-purpose models could not immediately replicate. But it required customer volume and time to validate, neither of which Basilica had in sufficient quantity before the competitive environment shifted decisively.

---

## Market Position

### Target Customers

Basilica targeted software developers and data scientists who needed to build machine learning classifiers but lacked the ML expertise, GPU infrastructure, or labeled data volume to train deep networks from scratch. The implicit customer profile was a full-stack developer at a mid-sized company — someone building a product feature that required image recognition or text classification, who could write API calls but could not configure a PyTorch training pipeline.

The R client suggests a secondary target: statisticians and data scientists working in R-heavy environments (academia, pharma, finance, government) who wanted to incorporate deep learning representations into their existing analytical workflows without switching toolchains. This was a potentially differentiated segment — R users were underserved by the ML tooling ecosystem in 2019 — but no evidence in the public record confirms whether this segment generated meaningful usage.

### Market Size

Basilica operated in the developer API and machine learning infrastructure market. The company did not publish market size estimates, and no investor materials are available. The addressable market was real: by 2019, demand for ML capabilities among non-ML-specialist developers was growing rapidly, and the "MLaaS" (Machine Learning as a Service) category was attracting significant investment. However, the market was bifurcating: large enterprises were building in-house ML teams, while the long tail of smaller developers was increasingly served by free, open-source tooling. Basilica's target — the middle segment willing to pay for a managed embedding API — was the segment most exposed to commoditization from both directions.

### Competition

Basilica's competitive position was structurally weak from the start, and the competitive landscape shifted against it faster than a two-person team with ~$150K in funding could respond.

**The free-model problem.** The most immediate competitive threat was not a direct competitor but a platform move: Google released BERT in October 2018, one month before Basilica's public launch.<sup><a href="https://news.ycombinator.com/item?id=18350270">[20]</a></sup> BERT provided state-of-the-art text representations for free, as open-source weights that any developer could download and run. Hacker News commenters flagged this on the day of Basilica's Show HN post, noting that GloVe 2B was also freely available and that BERT's performance would be difficult to beat.<sup><a href="https://news.ycombinator.com/item?id=18350270">[20]</a></sup><sup><a href="https://news.ycombinator.com/item?id=18351028">[21]</a></sup> The commenter framing was precise: for Basilica to be competitive, it would need to outperform free alternatives on domain-specific tasks — exactly the moat the company claimed but had not yet built.

**The distribution problem.** Basilica was competing on a dimension — general-purpose embedding quality — where incumbents had structural advantages in data volume, compute, and research talent. Google, AWS (SageMaker), and later OpenAI and Hugging Face could offer embedding APIs as loss leaders, bundled with broader cloud services that generated revenue elsewhere. A standalone embedding API had no comparable bundling leverage.

**The Hugging Face problem.** Between 2019 and 2022, Hugging Face built a model hub that made downloading and running pre-trained embedding models — including BERT, Sentence-BERT, and hundreds of domain-specific fine-tuned variants — trivially easy for any Python developer. The expertise barrier Basilica was solving (setting up inference infrastructure) collapsed as Hugging Face's `transformers` library abstracted it away. By 2022, a developer could run a high-quality sentence embedding model locally with four lines of Python, at zero marginal cost.

**The only viable position.** Basilica's network-effect argument — that cross-client fine-tuning would produce domain-specific embeddings that general models could not match — was the one competitive angle that incumbents could not immediately replicate. But it required Basilica to acquire enough customers in a given vertical to generate meaningful fine-tuning signal, then demonstrate measurably superior performance, then convert that performance advantage into pricing power. That sequence required time and capital that the company did not have.

---

## Business Model

Basilica's revenue model was a freemium API: a rate-limited free tier (5,000 requests per week per IP, accessed via a `SLOW_DEMO_KEY`) designed to drive developer adoption, with paid API keys for production use.<sup><a href="https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html">[13]</a></sup> No pricing information — per-request rates, tier structure, or enterprise contracts — was ever made public. The company never disclosed revenue figures, and the absence of any revenue data in the public record is itself a signal: companies that achieve meaningful revenue typically reference it in fundraising materials or press coverage.

**Inferred unit economics (labeled as estimates).** With a team of two to three people in San Francisco and estimated total funding of ~$150K,<sup><a href="https://www.apollo.io/companies/Basilica/5da3d42d2fc58300011d26f0">[16]</a></sup> Basilica's runway was extremely short. At a conservative San Francisco burn rate of $30–40K per month for a two-person technical team (salaries, infrastructure, office), the YC funding would have lasted three to five months without additional revenue or fundraising. The Python client's last update in December 2019 — nine months after Demo Day — suggests the team operated for roughly that window before active development ceased.<sup><a href="https://app.readthedocs.org/projects/basilica-client/downloads/pdf/latest/">[24]</a></sup> These are inferences from indirect evidence, not confirmed figures.

**The structural challenge.** A per-request API pricing model for embeddings faces a fundamental unit economics problem: inference compute costs scale with usage, but willingness-to-pay per request compresses as free alternatives improve. Without a high-margin enterprise contract layer or a proprietary model that demonstrably outperformed free alternatives, the path to sustainable revenue was narrow.

---

## Post-Mortem

### Primary Cause: Platform Aggregation Eliminated Willingness-to-Pay

The most important fact about Basilica's failure is that it was structurally anticipated before the company entered YC. When Basilica posted its Show HN on November 19, 2018, the top Hacker News comments immediately identified the core problem: Google BERT, released weeks earlier, provided world-class text embeddings for free.<sup><a href="https://news.ycombinator.com/item?id=18350270">[20]</a></sup> One commenter stated directly that for Basilica to be competitive, it would need to outperform free alternatives like GloVe 2B and do "domain-specific heavy-lifting."<sup><a href="https://news.ycombinator.com/item?id=18351028">[21]</a></sup>

This was not a prediction that proved wrong — it was an accurate diagnosis of the market structure Basilica was entering. The 2019–2022 period saw a systematic collapse of the expertise and infrastructure barriers that Basilica was monetizing:

- **2019**: Hugging Face releases the `transformers` library, making BERT and its variants trivially accessible to Python developers.
- **2020**: Sentence-BERT (SBERT) provides high-quality sentence-level embeddings — directly competing with Basilica's text embedding product — as open-source weights.
- **2022**: OpenAI releases its text-embedding-ada-002 API at $0.0001 per 1,000 tokens, backed by models trained on orders of magnitude more data than Basilica could access.

Each of these events further eroded the market for a standalone paid embedding API. Basilica's response — building domain-specific fine-tuned models through cross-client transfer learning — was the correct strategic answer, but it required customer volume to generate fine-tuning signal and time to demonstrate performance advantages. The competitive clock did not allow for either.

### Secondary Cause: The Moat Was Theoretical, Not Demonstrated

At YC Demo Day, Basilica's primary defensibility argument was a network effect: data from across its client base would improve embeddings for each vertical, creating a compounding advantage over generic models.<sup><a href="https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/">[14]</a></sup> This argument was structurally sound — domain-specific fine-tuning does improve embedding quality for specialized tasks — but it was entirely prospective. No evidence in the public record suggests Basilica ever had enough customers in any single vertical to generate meaningful fine-tuning signal, let alone demonstrate measurable performance improvements over free alternatives.

The attempted remedy was the Demo Day pitch itself: use the YC platform to attract enough customers to begin validating the network-effect thesis. But without a post-Demo Day funding round — and no seed round appears in any database<sup><a href="https://www.crunchbase.com/organization/basilica">[17]</a></sup> — the company lacked the runway to acquire customers at the scale needed to prove the moat. The absence of follow-on funding after Demo Day is the clearest external signal that investors did not believe the network-effect thesis was achievable with the resources available.

### Tertiary Cause: Resource Mismatch for the Chosen Battleground

Basilica was a two-to-three person team<sup><a href="https://www.ycombinator.com/companies/basilica">[4]</a></sup> with an estimated ~$150K in total funding,<sup><a href="https://www.apollo.io/companies/Basilica/5da3d42d2fc58300011d26f0">[16]</a></sup> attempting to build and maintain a production ML inference API competitive with Google, AWS, and eventually OpenAI. The infrastructure costs alone — GPU compute for inference, model storage, API reliability — would have consumed a significant fraction of the available capital. The team had no documented ML research background, meaning model improvements required engineering effort rather than novel research, further constraining the pace of differentiation.

The Python client's last update in December 2019 — nine months after Demo Day — marks the effective end of active development.<sup><a href="https://app.readthedocs.org/projects/basilica-client/downloads/pdf/latest/">[24]</a></sup> The R client repository shows a final update in December 2022,<sup><a href="https://github.com/basilica-ai">[25]</a></sup> which may reflect a minor maintenance commit rather than active product work — the evidence does not distinguish between the two. Either way, the pattern is consistent with a team that ran out of runway and quietly stopped building, rather than a dramatic failure event.

### Structural Factor: The Category Was Winner-Take-All on Distribution

The embedding API market was not a space where a small, well-executed product could find a durable niche. The category had two structural properties that favored incumbents:

First, **switching costs were low**. Embeddings are interchangeable at the API level — a developer switching from Basilica to OpenAI's embedding API needed to change one function call and reindex their vectors. There was no data lock-in, no workflow integration, no social graph. The only switching cost was retraining downstream classifiers, which was trivial given the small dataset sizes Basilica's customers were working with.

Second, **distribution was decisive**. Google, AWS, and OpenAI could offer embedding APIs as features within existing developer relationships — bundled with cloud compute, storage, and other services that developers were already paying for. A standalone embedding API had no comparable distribution leverage. Basilica needed developers to seek it out specifically; incumbents could surface their embedding products to developers already in their ecosystems.

These structural properties meant that even a technically superior Basilica product would have faced severe customer acquisition headwinds. The company's only viable path was deep vertical specialization — building embeddings for a specific domain (medical imaging, legal text, e-commerce product photos) where generic models underperformed and where customers had high enough willingness-to-pay to justify the infrastructure costs. Whether the team recognized this and attempted it, or ran out of time before reaching that conclusion, is not documented in any public source.

### The Silence as Signal

No founder published a post-mortem. No shutdown announcement was made. No acqui-hire was announced. The company simply stopped appearing in any public record after late 2019, with the founders moving on to other roles.<sup><a href="https://www.crunchbase.com/person/jorge-silva-ff75">[22]</a></sup><sup><a href="https://thecoolpeople.substack.com/p/i-left-sf-to-build-in-asias-food">[23]</a></sup> This pattern — a quiet wind-down with no public accounting — is consistent with a company that never achieved enough traction to generate a story worth telling, rather than one that failed dramatically after significant scale.

---

## Key Lessons

- **Basilica's core product was a feature, not a platform, and the incumbents proved it.** Basilica offered pre-trained embeddings via API — a capability that Google, OpenAI, and Hugging Face absorbed into their free offerings between 2018 and 2022. The lesson is not generic ("don't compete with big tech") but specific: when the primary value proposition is removing an infrastructure barrier, and that barrier is being removed simultaneously by well-resourced platforms as a loss leader, the standalone paid product has no durable position. Basilica's only escape was deep vertical specialization, which required customer volume it never achieved.

- **The network-effect moat argument requires proof before it becomes a fundraising story.** Basilica pitched cross-client transfer learning as its defensibility at Demo Day 2019, but the argument was entirely prospective — no customer data, no performance benchmarks, no vertical concentration.<sup><a href="https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/">[14]</a></sup> Investors apparently did not fund the company past the YC pre-seed, suggesting the thesis was not credible without evidence. For infrastructure companies claiming data network effects, the moat must be demonstrated with real customers in a specific vertical before it can anchor a fundraising narrative.

- **The R client was an underexplored go-to-market signal that deserved more attention.** Basilica shipped an R client in June 2019 — an unusual choice that implicitly targeted data scientists and statisticians rather than ML engineers.<sup><a href="https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html">[13]</a></sup> This segment was underserved by ML tooling in 2019 and had genuine pain around accessing deep learning representations. A focused go-to-market strategy targeting R users in specific high-value verticals (pharma, finance, academic research) might have generated the concentrated customer base needed to validate the domain-specific moat. Instead, the product appears to have targeted the general developer market, where free alternatives were strongest.

- **A two-person team with ~$150K cannot sustain a production ML inference API long enough to prove a network-effect thesis.** The resource mismatch between Basilica's ambition (embeddings for every data modality, cross-client fine-tuning at scale) and its capitalization (estimated $150K, team of two)<sup><a href="https://www.ycombinator.com/companies/basilica">[4]</a></sup><sup><a href="https://www.apollo.io/companies/Basilica/5da3d42d2fc58300011d26f0">[16]</a></sup> was severe. The Python client's last update nine months after Demo Day<sup><a href="https://app.readthedocs.org/projects/basilica-client/downloads/pdf/latest/">[24]</a></sup> reflects the inevitable outcome: the team ran out of runway before the competitive thesis could be tested. For infrastructure plays with long validation timelines, the funding required to reach proof points must be secured before the competitive window closes.

---

## Sources

1. [Crunchbase — Basilica organization profile](https://www.crunchbase.com/organization/basilica)
2. [Y Combinator — Basilica company directory](https://www.ycombinator.com/companies/basilica)
3. [Crunchbase — Michael Lucy profile](https://www.crunchbase.com/person/michael-lucy)
4. [Crunchbase — Jorge Silva profile](https://www.crunchbase.com/person/jorge-silva-ff75)
5. [Crunchbase — Eric Fung profile](https://www.crunchbase.com/person/eric-fung-2fac)
6. [TechCrunch — YC W19 Demo Day 1 coverage, March 18, 2019](https://techcrunch.com/2019/03/18/here-are-the-85-startups-that-launched-today-at-y-combinators-w19-demo-day-1/)
7. [Basilica Python client documentation (v0.2.7), ReadTheDocs](https://basilica-client.readthedocs.io/en/latest/basilica.html)
8. [Basilica R client documentation, rdrr.io](https://rdrr.io/github/basilica-ai/basilica-r-client/man/basilica.html)
9. [Basilica R client GitHub repository](https://github.com/basilica-ai/basilica-r-client)
10. [Hacker News — Show HN: Basilica (November 19, 2018)](https://news.ycombinator.com/item?id=18346553)
11. [Hacker News — Basilica competitive discussion thread](https://news.ycombinator.com/item?id=18350270)
12. [Hacker News — Basilica competitive discussion (GloVe/domain specificity)](https://news.ycombinator.com/item?id=18351028)
13. [Hacker News — Basilica face embedding model discussion (February 14, 2019)](https://news.ycombinator.com/item?id=19165200)
14. [Apollo.io — Basilica funding data](https://www.apollo.io/companies/Basilica/5da3d42d2fc58300011d26f0)
15. [GitHub — Jorge Silva profile (@thejsj)](https://github.com/thejsj)
16. [Basilica Python client PDF documentation, ReadTheDocs](https://app.readthedocs.org/projects/basilica-client/downloads/pdf/latest/)
17. [GitHub — basilica-ai organization](https://github.com/basilica-ai)
18. [The Cool People Substack — Eric Fung profile (January 13, 2025)](https://thecoolpeople.substack.com/p/i-left-sf-to-build-in-asias-food)
