# Research Report: Vizly

## Overview

Vizly was a Y Combinator-backed startup (S23) that built an AI-powered business intelligence tool allowing users to query and visualize data using plain English.Founded in 2023 by Ali Shobeiri and Sami Sahnoune, two McGill University graduates with directly relevant experience at Apple, Microsoft, NASA JPL, Splunk, and Plotly, the company's core thesis was that non-technical employees were bottlenecked waiting for data analysts to answer routine questions — and that a lightweight, on-premises AI layer could eliminate that bottleneck without exposing sensitive data to external APIs.

Vizly raised $500K from Y Combinator and never secured follow-on funding.It operated as a two-person team in one of the most crowded AI application categories of 2023, competing against Microsoft, Google, OpenAI, and a wave of well-funded vertical challengers.

By late 2024, co-founder Ali Shobeiri had joined Perplexity, the company's domain had been acquired by an unrelated firm, and YC listed both founders as "Former Founders." Vizly shut down quietly, with no public post-mortem.

<report-gallery>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/2bb513e0ff0b55132c5db0962ac5fcd9ccac7e6c.jpg" alt="Vizly: Data to insights in seconds | Y Combinator" caption="Vizly's official Y Combinator profile avatar — the face of a two-person startup that entered YC's S23 batch with $500K and a bold promise: let anyone query enterprise data in plain English, no SQL required."></media-image>
<media-image src="https://img.aipure.ai/image_vizly_0d85c1883866959b6ccc74c665e8885a.jpg" alt="Vizly: AI-powered data analysis: Reviews, Features, Pricing, Guides ..." caption="A product listing snapshot of Vizly at its most mature — supporting GPT-4, Claude 3.5 Sonnet, Snowflake, BigQuery, and a tiered subscription model. By mid-2024, the product had grown far beyond its Llama 2 roots, but the market had grown faster."></media-image>
</report-gallery>

## Founding Story

Ali Shobeiri and Sami Sahnoune had known each other for nearly a decade before founding Vizly. <sup><a href="https://www.fondo.com/blog/vizly-launches">[1]</a></sup> Both graduated from McGill University and had already co-built a product together: YouTube Party, a Chrome extension that synchronized YouTube video playback across multiple users and reached over 300,000 weekly active users before being sold. <sup><a href="https://www.ycombinator.com/companies/vizly">[2]</a></sup> That prior collaboration gave them a working template for how to build and ship together quickly.

Their professional paths after McGill took them into the exact domain Vizly would eventually address. Shobeiri worked as a Machine Learning Engineer at Apple, a ML Research Intern at Unity, and a Software Engineer at Microsoft. <sup><a href="https://www.ycombinator.com/companies/vizly">[3]</a></sup> Sahnoune built mission-critical data systems at NASA's Jet Propulsion Laboratory, architected data visualization libraries at Splunk, and worked at Plotly. <sup><a href="https://www.ycombinator.com/companies/vizly">[4]</a></sup> These were not peripheral roles — both founders were embedded in data infrastructure at organizations where data access was a daily operational constraint.

The founding insight came directly from those experiences. At NASA JPL, colleagues in cybersecurity would regularly approach Sahnoune with questions about datasets, creating a recurring bottleneck where a single data-fluent person became the gatekeeper for an entire team's analytical work. Shobeiri experienced the same dynamic at Apple, where non-technical colleagues were queued up waiting for him to answer data questions. <sup><a href="https://www.fondo.com/blog/vizly-launches">[5]</a></sup> The problem was not hypothetical — both founders had lived it from the analyst's side, fielding requests they believed should not have required their intervention at all.

The initial vision was to eliminate that bottleneck by letting non-technical users ask questions of their data in plain English and receive charts, summaries, and insights without writing a single line of SQL or Python. The on-premises deployment model — a deliberate architectural choice, not an afterthought — was designed to make the product viable for enterprises in regulated industries where data could not leave internal infrastructure.

The team began building before YC acceptance. Their first public prototype appeared on Hacker News in May 2023, <sup><a href="https://news.ycombinator.com/item?id=35766516">[6]</a></sup> months before the S23 batch officially launched. That early public test reflected a bias toward shipping that would characterize the company's product cadence throughout its short life.

---

## Timeline

- **May 2023** — Vizly founders post first "Show HN" on Hacker News, demonstrating an early prototype for querying and visualizing data using plain English — the earliest public proof of the product. <sup>[[6]](https://news.ycombinator.com/item?id=35766516)</sup>

<media-hn url="https://news.ycombinator.com/item?id=35766516" title="Show HN: Vizly – Query and visualize your data in seconds" points="" comments=""></media-hn>

- **August 2023** — Vizly officially launches and is covered by Fondo; founders Ali Shobeiri and Sami Sahnoune publicly identified as McGill graduates with ~10 years of shared history. <sup>[[1]](https://www.fondo.com/blog/vizly-launches)</sup>

- **August 2023** — Vizly participates in Y Combinator's Summer 2023 (S23) batch, raising $500K with YC as sole institutional investor. <sup>[[7]](https://tracxn.com/d/companies/vizly/__1ELe03Awi6hLUVmUNWyb7W9U8dh-6tplSVOp9S-IBPc)</sup>

- **August 31, 2023** — Vizly launches on YC's platform as an on-premises, AI-powered BI tool for enterprises, emphasizing data privacy and ease of deployment. <sup>[[8]](https://www.ycombinator.com/launches/JNS-vizly-ai-powered-data-analysis-for-enterprise)</sup>

- **September 2, 2023** — Second "Show HN" post announces an on-premises Mac application built on Llama 2 and llama.cpp, with all data staying local. <sup>[[9]](https://news.ycombinator.com/item?id=37315667)</sup>

<media-hn url="https://news.ycombinator.com/item?id=37315667" title="Show HN: Query your database using plain English, fully on-premises" points="" comments=""></media-hn>

- **August 2024** — A Medium review documents the mature product: support for multiple LLMs (GPT-4, GPT-4o, Claude 3 Opus, Claude 3.5 Sonnet), enterprise database connectors (Snowflake, Redshift, BigQuery), and a tiered pricing model ($19.99–$29.99/month). <sup>[[10]](https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3)</sup>

- **2024** — Vizly releases a Chrome extension to analyze Google Sheets with AI, suggesting an expansion toward a prosumer/consumer distribution channel. <sup>[[11]](https://chromewebstore.google.com/detail/vizly-analyze-google-shee/mggpeefbjkililmmelilhpegpcfeaeao)</sup>

- **2024** — Ali Shobeiri joins Perplexity, signaling his departure from Vizly. The company effectively ceases operations with no public announcement. <sup>[[12]](https://www.linkedin.com/in/ali-shobeiri/)</sup>

- **2024** — The vizly.ai domain is acquired by Aggregate Intelligence, a global data services company unrelated to the YC startup, confirming the domain was abandoned or sold. <sup>[[13]](https://vizly.ai/about-us)</sup>

- **2024** — YC company page lists both Ali Shobeiri and Sami Sahnoune as "Former Founders," the clearest institutional confirmation that Vizly is no longer active. <sup>[[14]](https://www.ycombinator.com/companies/vizly)</sup>

---

## What They Built

Vizly's core product was an AI-powered data analysis tool that let users ask questions about their data in plain English and receive charts, tables, and written summaries in response — without writing SQL, Python, or any other query language.

The workflow was straightforward. A user uploaded a file (CSV, Excel, SPSS, PDF, image, or JSON) <sup><a href="https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3">[15]</a></sup> or connected directly to an enterprise database — Snowflake, Redshift, BigQuery, SQL Server, or Postgres. <sup><a href="https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3">[16]</a></sup> They then typed a question — "What were our top five revenue-generating products last quarter?" or "Show me a trend of customer churn by region" — and the system generated the appropriate visualization or summary. The AI handled the translation from natural language to the underlying query, executed it against the data, and returned a result the user could read without any technical background.

The architectural choice that distinguished Vizly from most competitors was on-premises deployment. Rather than sending data to a cloud API, Vizly ran locally — the entire instance was designed to operate on a single MacBook, with one employee able to set it up and share a link with non-technical colleagues across the organization. <sup><a href="https://www.ycombinator.com/launches/JNS-vizly-ai-powered-data-analysis-for-enterprise">[8]</a></sup> Sensitive enterprise data never left the customer's own infrastructure. This was a deliberate positioning decision aimed at regulated industries — finance, healthcare, government — where data residency requirements or internal security policies would block cloud-based alternatives.

<media-tweet url="https://x.com/VizlyHQ" author="@VizlyHQ" date="2023-08-09" text="Analyze your data using the best AI models (GPT-4o, Claude and more)"></media-tweet>

The product evolved meaningfully over its roughly 18-month lifespan. The September 2023 version, announced in a second Hacker News post, <sup><a href="https://news.ycombinator.com/item?id=37315667">[9]</a></sup> ran on Llama 2 and llama.cpp — an open-source local LLM stack that was technically sophisticated for its time and predated widespread enterprise adoption of local model inference. By mid-2024, the product had expanded to support multiple frontier models: GPT-4 as the default, with user-selectable options including GPT-4o, GPT-4o mini, Claude 3 Opus, and Claude 3.5 Sonnet. <sup><a href="https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3">[17]</a></sup> This multi-model support reflected the team actively tracking a rapidly shifting model landscape rather than locking into a single provider.

Late in the company's life, Vizly also released a Chrome extension for analyzing Google Sheets using GPT-4o and Claude 3.5 Sonnet. <sup><a href="https://chromewebstore.google.com/detail/vizly-analyze-google-shee/mggpeefbjkililmmelilhpegpcfeaeao">[11]</a></sup> This represented a meaningful distribution shift — from enterprise on-premises software requiring IT involvement to a browser plugin any individual user could install in seconds. Whether this was a deliberate pivot toward a more accessible go-to-market channel or a parallel experiment is not documented publicly.

What separated Vizly from the wave of "chat with your data" tools that emerged in 2023 was the combination of local deployment and broad data source support. Most competitors required cloud connectivity. Vizly's on-premises model was a genuine technical differentiator — but one that came with a longer, more complex sales cycle than the product's pricing and team size could support.

---

## Market Position

### Target Customers

Vizly's stated target was enterprise organizations with non-technical employees who needed data insights but lacked the SQL or Python skills to retrieve them independently. <sup><a href="https://www.ycombinator.com/launches/JNS-vizly-ai-powered-data-analysis-for-enterprise">[8]</a></sup> The on-premises deployment model and enterprise database connectors (Snowflake, Redshift, BigQuery) pointed specifically toward regulated industries — financial services, healthcare, and government — where data residency and security requirements would disqualify cloud-based alternatives.

The pricing structure, however, told a different story. A free tier capped at 10 queries per month, a basic plan at $19.99/month, and a premium plan at $29.99/month with a 50% student and faculty discount <sup><a href="https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3">[18]</a></sup> are consumer and prosumer price points, not enterprise contract values. Enterprise software in the BI category typically sells on annual contracts ranging from tens of thousands to hundreds of thousands of dollars, with procurement cycles measured in months. Vizly's pricing was misaligned with the customer segment its architecture was designed to serve. The academic discount further suggested the team was experimenting with seeding adoption in universities — a slow-burn strategy that rarely converts to enterprise revenue quickly enough to sustain a startup on a tight runway.

The Chrome extension for Google Sheets analysis represented a third potential customer segment: individual knowledge workers who analyze data in spreadsheets. This prosumer audience is large, easy to reach, and willing to pay small monthly fees — but monetizes poorly at $19.99/month per user and requires massive scale to generate meaningful revenue.

### Market Size

The broader business intelligence and analytics software market was valued at approximately $29 billion globally in 2023, with the AI-augmented analytics segment growing rapidly. The "natural language query" or "chat with your data" subcategory attracted significant venture capital in 2023, with dozens of startups entering the space simultaneously. The addressable market for on-premises AI BI tools in regulated industries was a meaningful subset of this — large enough to build a business, but requiring enterprise sales infrastructure that a two-person team could not realistically deploy.

### Competition

The competitive environment Vizly entered in mid-2023 was among the most crowded in enterprise software. Competitors operated at three distinct levels.

At the platform level, Microsoft integrated Copilot directly into Excel and Power BI, giving hundreds of millions of existing users natural language data analysis without switching tools. Google launched Duet AI for Google Workspace, embedding similar capabilities into Sheets and Looker. These were not startups — they were distribution advantages that no small company could match.

At the dedicated BI tool level, Tableau (owned by Salesforce) launched Tableau Pulse with AI-driven natural language insights. ThoughtSpot had been building natural language search for enterprise data for years and was well-capitalized. Both had established enterprise sales teams and existing customer relationships.

At the AI-native startup level, Julius AI, Rows, and numerous other "chat with your data" tools launched in the same 2023 window as Vizly, competing for the same early adopters. OpenAI's Code Interpreter (later Advanced Data Analysis), released in July 2023, offered similar functionality directly inside ChatGPT — free for Plus subscribers — and required no setup whatsoever.

Vizly's on-premises, privacy-first positioning was a genuine differentiator against all of these competitors. None of the major platforms offered true local deployment. But exploiting that differentiator required reaching and closing enterprise security buyers — a sales motion that demands dedicated account executives, legal review cycles, and procurement relationships that a two-person founding team was structurally unable to execute at scale.

---

## Business Model

Vizly operated on a freemium SaaS subscription model with three tiers. <sup><a href="https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3">[18]</a></sup> The free plan allowed 10 queries per month — enough to demonstrate the product but insufficient for regular use. The basic plan at $19.99/month unlocked higher usage limits. The premium plan at $29.99/month added unlimited queries and priority support, with a 50% discount available to students and faculty.

This pricing structure was designed for individual users and small teams, not enterprise procurement. Enterprise BI software typically sells on annual contracts with per-seat pricing, volume discounts, and dedicated customer success resources — none of which were evident in Vizly's public-facing model. The gap between the product's enterprise-grade architecture (on-premises deployment, Snowflake and Redshift connectors) and its consumer-grade pricing ($29.99/month maximum) suggests the team had not yet resolved which customer segment to commit to, or was using the consumer tier as a top-of-funnel while pursuing enterprise deals through direct outreach. No revenue figures were disclosed publicly.

---2f:T1966,

## Post-Mortem

Vizly shut down quietly in 2024, with no public announcement, no founder post-mortem, and no explanation offered to customers or the broader startup community. The proximate signals — Ali Shobeiri joining Perplexity, <sup><a href="https://www.linkedin.com/in/ali-shobeiri/">[12]</a></sup> the vizly.ai domain acquired by an unrelated company, <sup><a href="https://vizly.ai/about-us">[13]</a></sup> and YC listing both founders as "Former Founders" <sup><a href="https://www.ycombinator.com/companies/vizly">[14]</a></sup> — point to a company that ran out of runway without finding a path to scale, rather than a single catastrophic failure event. Several structural factors contributed.

### Insufficient Capital for the Sales Motion Required

Vizly raised $500K from Y Combinator and never secured follow-on funding. <sup><a href="https://tracxn.com/d/companies/vizly/__1ELe03Awi6hLUVmUNWyb7W9U8dh-6tplSVOp9S-IBPc">[7]</a></sup> With two founders and no recorded hires, the burn rate was likely low — primarily LLM API costs and infrastructure — but $500K still implies a runway of 12 to 18 months at most, placing the probable end of funds in late 2024 to early 2025.

The core problem was that the product's most defensible positioning — on-premises deployment for regulated enterprises — required a sales motion that $500K cannot fund. Enterprise security software sales cycles routinely run six to twelve months, require dedicated account executives to navigate procurement, and demand legal and compliance review before any contract is signed. A two-person founding team cannot simultaneously build the product, respond to enterprise security questionnaires, manage proof-of-concept deployments, and close deals. The capital and headcount required to execute enterprise sales were never available.

The team appears to have recognized this constraint. The Chrome extension for Google Sheets <sup><a href="https://chromewebstore.google.com/detail/vizly-analyze-google-shee/mggpeefbjkililmmelilhpegpcfeaeao">[11]</a></sup> and the consumer-grade pricing model suggest an attempt to find a lower-friction distribution channel — one that did not require enterprise sales cycles. But the prosumer market for AI data tools was simultaneously being served for free by OpenAI's Code Interpreter, making it difficult to charge even $19.99/month for a standalone product.

### Rapid Commoditization of the Core Feature

The "chat with your data" capability that Vizly was built around became a standard feature of major platforms within months of Vizly's launch. OpenAI released Code Interpreter in July 2023 — the same month Vizly was in the YC batch — giving ChatGPT Plus subscribers the ability to upload files and ask questions in natural language, for free, with no setup required. Microsoft embedded Copilot in Excel and Power BI. Google launched Duet AI for Sheets and Looker. Tableau released Pulse.

Each of these releases eroded the novelty of Vizly's core value proposition for the prosumer segment. A user who could ask questions of their spreadsheet data directly inside Excel or Google Sheets had little reason to pay $19.99/month for a separate tool. The commoditization happened faster than a two-person team could respond to — not because the team was slow, but because the pace of platform-level feature releases in 2023 was unprecedented.

Vizly's on-premises architecture remained a genuine differentiator that none of these platform competitors replicated. But as noted above, monetizing that differentiator required enterprise sales infrastructure the company did not have.

### Pricing-Positioning Mismatch

The tension between Vizly's enterprise-grade architecture and its consumer-grade pricing was never resolved publicly. The on-premises deployment model, Snowflake and Redshift connectors, and data privacy guarantees were features that enterprise security buyers value — and that enterprise buyers pay enterprise prices for. The $19.99–$29.99/month pricing, free tier, and student discount were signals aimed at individual users and small teams.

This mismatch created a strategic ambiguity that is difficult to resolve without committing to one segment and building the corresponding go-to-market motion. Enterprise sales requires account executives, legal review, and customer success. Prosumer growth requires viral distribution, low friction, and either a freemium funnel that converts at scale or a price point that generates meaningful revenue per user. Vizly's pricing was too low for enterprise and too high relative to free alternatives for prosumers.

<media-tweet url="https://twitter.com/Ali_Shobeiri" author="@Ali_Shobeiri" date="" text="I used to call myself a professional prompt engineer as a way to get a cheap laugh."></media-tweet>

### No Follow-On Funding

Tracxn and Crunchbase record no follow-on investment in Vizly beyond the initial $500K YC round. <sup><a href="https://tracxn.com/d/companies/vizly/__1ELe03Awi6hLUVmUNWyb7W9U8dh-6tplSVOp9S-IBPc">[7]</a></sup> <sup><a href="https://www.crunchbase.com/organization/vizly">[19]</a></sup> Whether the founders attempted to raise a seed extension or Series A and were declined, or chose not to pursue additional capital, is not documented. The absence of follow-on funding in a category that attracted significant venture investment in 2023 — Julius AI, Rows, and ThoughtSpot all raised rounds during this period — suggests investors were not convinced Vizly had differentiated sufficiently from the competitive field or demonstrated enough traction to justify additional capital.

Without a follow-on round, the company had no path to hiring the sales, marketing, or engineering resources needed to compete at enterprise scale. The runway ran out, and the company wound down without a formal exit.

### Quiet Shutdown

The manner of Vizly's closure is itself informative. No shutdown announcement was made. No post-mortem was published. No customers were publicly notified. <sup><a href="https://www.ycombinator.com/companies/vizly">[20]</a></sup> This pattern — a "quiet shutdown" — is common among YC companies that do not achieve escape velocity and whose founders move on to other opportunities without a dramatic failure event to document. It is distinct from companies that fail loudly (fraud, public controversy, mass layoffs) and from companies that are acquired. It reflects a gradual exhaustion of runway and options, rather than a single decision point.

---

## Key Lessons

- **On-premises differentiation requires enterprise sales infrastructure to monetize.** Vizly's privacy-first, local deployment model was a genuine technical differentiator in a market where every major competitor required cloud connectivity. But that differentiator only creates value if the company can reach and close enterprise security buyers — a process that requires dedicated sales headcount, legal resources, and months-long procurement cycles. A two-person team with $500K cannot execute that motion. The lesson is not that on-premises was the wrong positioning, but that the capital raised must match the sales complexity of the chosen positioning.

- **Consumer-grade pricing and enterprise-grade architecture cannot coexist without a deliberate bridge strategy.** Vizly's $19.99–$29.99/month pricing was misaligned with its on-premises enterprise architecture. <sup><a href="https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3">[18]</a></sup> Companies that successfully bridge prosumer and enterprise markets typically use the prosumer tier as a bottom-up adoption mechanism — individual users bring the tool into their organizations, creating organic enterprise demand. That strategy requires the prosumer product to be meaningfully better than free alternatives. In 2023, OpenAI's Code Interpreter was free and required no setup, making the prosumer bridge difficult to build.

- **Category timing matters as much as product quality.** Vizly entered the "chat with your data" category at the exact moment it was being simultaneously attacked by Microsoft, Google, OpenAI, and dozens of well-funded startups. The founders had strong technical credentials and genuine founder-market fit — the failure was not a product quality problem. It was a structural problem: the category commoditized faster than a two-person team with 12–18 months of runway could respond to. Startups in rapidly commoditizing AI application categories need either a defensible moat (proprietary data, network effects, switching costs) or enough capital to outlast the commoditization wave. Vizly had neither.

- **The absence of a public post-mortem is itself a data point.** Vizly's quiet shutdown — no announcement, no founder reflection, no customer communication — is consistent with a company that ran out of runway without a clear narrative about what went wrong. Founders who experience a specific, learnable failure tend to document it. The silence here suggests the failure was diffuse: insufficient traction across multiple customer segments, no single moment of product-market fit, and a gradual exhaustion of options rather than a decisive pivot or shutdown decision.

---

## Sources

1. [Fondo: Vizly Launches](https://www.fondo.com/blog/vizly-launches)
2. [YC Company Page: Vizly](https://www.ycombinator.com/companies/vizly)
3. [YC Launch: Vizly AI-Powered Data Analysis for Enterprise](https://www.ycombinator.com/launches/JNS-vizly-ai-powered-data-analysis-for-enterprise)
4. [Tracxn: Vizly Company Profile](https://tracxn.com/d/companies/vizly/__1ELe03Awi6hLUVmUNWyb7W9U8dh-6tplSVOp9S-IBPc)
5. [Medium: Vizly AI-Enabled Data Analytics Review](https://rehoyt.medium.com/vizly-ai-enabled-data-analytics-d28e8c958ec3)
6. [Hacker News: Show HN – Vizly Query and Visualize Your Data in Seconds](https://news.ycombinator.com/item?id=35766516)
7. [Hacker News: Show HN – Query Your Database Using Plain English, Fully On-Premises](https://news.ycombinator.com/item?id=37315667)
8. [Chrome Web Store: Vizly – Analyze Google Sheets](https://chromewebstore.google.com/detail/vizly-analyze-google-shee/mggpeefbjkililmmelilhpegpcfeaeao)
9. [LinkedIn: Ali Shobeiri](https://www.linkedin.com/in/ali-shobeiri/)
10. [LinkedIn: Sami Sahnoune](https://www.linkedin.com/in/samisahnoune/)
11. [Vizly.ai (now Aggregate Intelligence)](https://vizly.ai/about-us)
12. [Crunchbase: Vizly](https://www.crunchbase.com/organization/vizly)
13. [X/Twitter: @VizlyHQ](https://x.com/VizlyHQ)
14. [X/Twitter: @Ali_Shobeiri](https://twitter.com/Ali_Shobeiri)32:T4d8,By 2026, Vizly returns as a compliance-first natural language query tool for regulated industries—healthcare clinics, financial services, and legal firms—where data never leaves the building. The product is a lightweight on-premises agent that connects to a single data source (PostgreSQL, Google Sheets) and translates plain English questions into SQL, with every query logged for audit. It ships as a Google Workspace add-on, so adoption is frictionless for teams already in Sheets.

The market shift is local LLM inference maturity. In 2023, running reliable inference on-premises was a liability; by 2026, it's table stakes for any enterprise handling sensitive data. HIPAA, SOC 2, and data residency requirements are no longer edge cases—they're deal-breakers. Incumbents like Microsoft and Google own the horizontal BI market, but they can't promise data stays local. Vizly owns that wedge.

Go-to-market targets IT managers at mid-market healthcare and financial services firms. The pitch: eliminate analyst bottlenecks without compliance risk. Distribution through Google Workspace Marketplace means no sales engineering required at launch. Land in one vertical, prove audit-log rigor, expand to adjacent regulated industries.33:T883,
