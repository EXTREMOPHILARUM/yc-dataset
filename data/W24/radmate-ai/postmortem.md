# Research Report: RadMate AI

## Overview

RadMate AI was a San Francisco-based healthcare AI startup founded in 2023 by Mohamed Khalifa and Adam Skrocki, two Cornell Computer Science alumni accepted into Y Combinator's Winter 2024 batch.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[1]</a></sup> The company built an AI copilot for radiologists — a workflow tool that listened to dictated findings and used large language models to generate structured, proofread radiology reports, reducing the volume of words radiologists needed to speak and the number of clicks required to produce a final report.<sup><a href="https://www.ycombinator.com/launches/KIh-radmate-ai-the-ai-copilot-for-radiologists">[2]</a></sup>

RadMate AI failed because it entered a capital-intensive, compliance-heavy enterprise market with $500K in pre-seed funding and a two-person team — a structural mismatch that made it nearly impossible to survive the 12–24 month sales cycles required to reach paying hospital customers.<sup><a href="https://pitchbook.com/profiles/company/593104-15">[3]</a></sup> A direct competitor, Rad AI, had already locked up distribution across a third of all U.S. health systems before RadMate AI presented at Demo Day.<sup><a href="https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai">[4]</a></sup>

No formal shutdown announcement has been made. By 2025, the company's website returned no content, its LinkedIn page had accumulated only 250 followers, and CEO Mohamed Khalifa's LinkedIn title had shifted to "Operator & Advisor | Y Combinator" — indirect signals that active operations had ceased.<sup><a href="https://www.linkedin.com/in/mohamed-taha-khalifa">[5]</a></sup><sup><a href="https://www.linkedin.com/company/radmate-ai">[6]</a></sup> No seed round was ever announced following YC Demo Day, and no acquirer or acqui-hire has been publicly documented.

<report-gallery>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/68ede46af83132984c874b91c6bccbe6bf6cb2c7.jpg" alt="Mohamed Khalifa, co-founder and CEO of RadMate AI" caption="Mohamed Khalifa, CEO of RadMate AI — his prior work building workflow tools for pathologists at PathAI directly shaped the product's design philosophy."></media-image>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/7cb3d76f50eede7d0fd64d4ac3e17ca53366eeb1.jpg" alt="Adam Skrocki, co-founder and CTO of RadMate AI" caption="Adam Skrocki, CTO of RadMate AI — his father's career as a radiologist gave the team firsthand access to the workflow pain points they set out to solve."></media-image>
</report-gallery>

## Founding Story

Mohamed Khalifa and Adam Skrocki met as Computer Science students at Cornell University.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[7]</a></sup> Their paths after graduation gave them complementary and directly relevant experience for what they would eventually build together.

Khalifa joined Amazon Web Services as a Customer Solutions Manager before moving to PathAI, a computational pathology company, where he worked as a Software Engineer building an image viewer platform designed to improve the workflow of pathologists.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[8]</a></sup> That role gave him a specific lens: he had seen firsthand how AI could be layered onto a clinical imaging workflow to reduce friction for specialists — not by replacing the clinician's judgment, but by automating the documentation burden around it.

Skrocki took a different route, joining Palantir as a software engineer on the AI Platform team, including its initial launch.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[9]</a></sup> His experience building enterprise AI infrastructure gave him a technical foundation for deploying LLM-based tools in complex organizational environments. But the founding motivation was more personal: Skrocki's father is a radiologist, and the daily friction his father experienced — dictating lengthy reports, correcting errors, navigating clunky software — became the product brief.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[10]</a></sup>

The insight the founders brought to Y Combinator was specific: radiology reporting was a documentation problem masquerading as a clinical problem. Radiologists were already expert image readers. What slowed them down was the translation of visual findings into structured written reports — a process that required dictating more words than necessary, manually formatting output, and then catching errors before submission. Khalifa's PathAI experience had shown him that this exact workflow bottleneck existed in pathology; radiology, with its higher report volumes and more standardized formatting conventions, was a larger and arguably more tractable version of the same problem.

The company was accepted into Y Combinator's Winter 2024 batch and publicly launched on February 5, 2024.<sup><a href="https://www.linkedin.com/posts/y-combinator_launch-yc-radmate-ai-the-ai-copilot-activity-7160346340202311681-e_0E">[11]</a></sup> No major product pivot has been documented — the company appears to have pursued its original thesis from founding through Demo Day without a significant change in direction.

One structural constraint was apparent from the start: the team was two people throughout the company's known operating life.<sup><a href="https://pitchbook.com/profiles/company/593104-15">[12]</a></sup> For a consumer software company, a two-person founding team is a feature. For a regulated healthcare enterprise product requiring EHR integration, security review, and clinical validation, it is a significant limitation.

## Timeline

- **2023** — RadMate AI, Inc. founded in San Francisco by Mohamed Khalifa (CEO) and Adam Skrocki (CTO), both Cornell CS alumni.<sup>[[13]](https://www.cbinsights.com/company/radmate-ai)</sup>
- **2023** — Company accepted into Y Combinator's Winter 2024 (W24) batch.<sup>[[14]](https://www.ycombinator.com/companies/radmate-ai)</sup>
- **February 5, 2024** — YC launch post published; RadMate AI publicly announces its AI copilot for radiologists.<sup>[[15]](https://www.ycombinator.com/launches/KIh-radmate-ai-the-ai-copilot-for-radiologists)</sup> Mohamed Khalifa's father posts on LinkedIn that the product is "getting a lot of attention from many radiology and healthcare institutions."<sup>[[16]](https://www.linkedin.com/posts/taha-khalifa-1530b52_launch-yc-radmate-ai-the-ai-copilot-activity-7160362420715073538-uofY)</sup>
- **April 2, 2024** — Mohamed Khalifa posts on LinkedIn that YC Demo Day is the next day.<sup>[[17]](https://www.linkedin.com/posts/mohamed-taha-khalifa_cant-believe-y-combinators-demo-day-is-activity-7181068150782803970-x3us)</sup>
- **April 3, 2024** — RadMate AI presents at YC W24 Demo Day; Pre-Seed / Convertible Note funding round announced, reflecting the $500K YC standard deal.<sup>[[18]](https://www.crunchbase.com/funding_round/radmate-ai-pre-seed--73a06648)</sup>
- **May 7, 2024** — Competitor Rad AI closes a $50M Series B, serving more than a third of all U.S. health systems — weeks after RadMate AI's Demo Day.<sup>[[19]](https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai)</sup>
- **January 2025** — Competitor Rad AI closes a $60M+ Series C, further cementing its market position.<sup>[[20]](https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai)</sup>
- **2025** — radmate.ai website returns no content; Mohamed Khalifa's LinkedIn title updated to "Operator & Advisor | Y Combinator," suggesting active operations have ceased.<sup>[[21]](https://www.linkedin.com/in/mohamed-taha-khalifa)</sup><sup>[[22]](https://www.radmate.ai/)</sup>

## What They Built

RadMate AI's core product was a dictation-to-report automation tool for radiologists. The workflow it targeted is one of the most repetitive in medicine: a radiologist examines a medical image (X-ray, CT, MRI), dictates their findings aloud, and that dictation is converted into a structured written report that becomes part of the patient's medical record. The problem is that this process is inefficient by design — radiologists dictate more words than the final report requires, the formatting is manual, and errors slip through at a rate the founders cited as exceeding 20%.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[23]</a></sup>

RadMate AI's product sat between the dictation and the final report. A radiologist would speak their findings while reviewing images, and the platform would use large language models to transform that raw dictation into a formatted, proofread report — applying the radiologist's personal templates and flagging potential errors before submission.<sup><a href="https://www.ycombinator.com/launches/KIh-radmate-ai-the-ai-copilot-for-radiologists">[24]</a></sup>

The key features, as described in the company's YC launch materials, were:<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[25]</a></sup>

- **Word reduction**: The system was designed to minimize the number of words a radiologist needed to dictate, inferring standard phrasing and structure from context.
- **Click reduction**: Report generation and submission required fewer manual steps, reducing the administrative overhead per report.
- **Auto-Report**: A named feature that generated full radiology reports from dictated findings using the radiologist's personal templates — the LLM equivalent of a smart macro.<sup><a href="https://www.crunchbase.com/organization/radmate-ai">[26]</a></sup>
- **Proofreading**: The system reviewed generated reports for errors before submission, targeting the >20% error rate the founders identified as a core market problem.<sup><a href="https://www.ycombinator.com/companies/radmate-ai">[27]</a></sup>

An important distinction: RadMate AI was not building a diagnostic AI. It was not attempting to read images and identify pathology — a task that requires FDA clearance and clinical validation at a level that would have been impossible for a two-person team. Instead, the product operated downstream of the radiologist's clinical judgment, automating only the documentation layer. This positioning was likely deliberate: by staying in the workflow/reporting layer rather than the diagnostic layer, the company could argue it was a software tool rather than a medical device, potentially avoiding the most burdensome regulatory requirements.

No product screenshots, demo videos, or EHR integration documentation have been publicly identified. Whether the product was ever deployed in a live clinical environment — even in a pilot capacity — is unknown. The absence of any customer announcement, case study, or press coverage beyond the initial YC launch is consistent with a product that remained in development or early pilot stages throughout the company's operating life.

The technology stack was LLM-based, consistent with the wave of GPT-4-era enterprise workflow tools that emerged in 2023–2024. The founders did not publicly describe their model architecture, fine-tuning approach, or data sourcing strategy — all of which would be material questions for any hospital evaluating the product for clinical use.

## Market Position

### Target Customers

RadMate AI's stated target was radiologists — specifically, the workflow pain points around report generation that affect radiologists at hospitals, health systems, and independent radiology practices. The company's problem framing (excess dictation words, report errors, burnout) applies most acutely to high-volume radiology environments where radiologists read dozens of studies per day. In practice, the most accessible early customers for a two-person team would have been independent radiology practices or smaller community hospitals, where procurement cycles are shorter and the decision-maker is closer to the end user. Whether the company pursued this segment or targeted larger health systems is not documented.

### Market Size

The global radiology AI market was valued at approximately $2 billion in 2023 and projected to grow significantly through the decade, driven by imaging volume growth and radiologist workforce shortages. The reporting and workflow automation sub-segment — RadMate AI's specific niche — represents a meaningful portion of that market, as report generation is a universal pain point across all radiology settings. No market sizing data specific to RadMate AI's positioning was found in public sources.

### Competition

RadMate AI entered a market where the competitive dynamics were already unfavorable for a new entrant.

The most direct competitor was Rad AI (a separate company, despite the similar name), which had built an AI-generated radiology report platform and, by the time of RadMate AI's Demo Day in April 2024, was already embedded in more than a third of all U.S. health systems and 9 of the 10 largest U.S. radiology practices.<sup><a href="https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai">[28]</a></sup> Rad AI closed a $50M Series B in May 2024 and a $60M+ Series C in January 2025 — a total capital base more than 100 times RadMate AI's known funding.<sup><a href="https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai">[29]</a></sup>

The competitive landscape maps poorly for RadMate AI along the two axes that matter most in enterprise healthcare AI: **distribution reach** and **clinical validation depth**. Rad AI had both. RadMate AI had neither, and its $500K funding made it structurally impossible to build either quickly.

Beyond Rad AI, the field included Cerebriu, Agamon Health, Smart Reporting, EnvoyAI, Inference Analytics, and Endimension — a crowded set of players competing across overlapping segments of the radiology AI workflow.<sup><a href="https://www.cbinsights.com/company/radmate-ai">[30]</a></sup> Many of these competitors had raised multi-million dollar rounds and had years of head start on EHR integrations and hospital relationships.

The structural problem was not just capital. Hospital procurement for AI tools involves a sequence of gates — security review, legal review, clinical validation, EHR integration testing, and often a formal pilot period — that can take 12 to 24 months even for well-resourced vendors. Incumbents with existing vendor relationships at a hospital can navigate these gates faster because they have already cleared the baseline trust and compliance requirements. A new entrant must clear every gate from scratch. For RadMate AI, with two employees and no documented hospital relationships, this process was effectively insurmountable within the runway provided by a $500K pre-seed.

The product's positioning as a workflow tool rather than a diagnostic AI may have been intended to reduce regulatory friction. But hospital procurement does not distinguish sharply between "workflow AI" and "diagnostic AI" when evaluating vendor risk — both require security review, data governance agreements, and clinical validation before deployment. The regulatory shortcut, if that was the intent, did not translate into a procurement shortcut.

## Business Model

RadMate AI never publicly disclosed a revenue model, pricing structure, or customer count. The absence of any revenue disclosure is itself a signal: companies that achieve early commercial traction in healthcare AI typically announce it, because paying hospital customers are a key proof point for seed fundraising.

The most likely intended model, based on the product category and competitive landscape, was a SaaS subscription charged per radiologist seat or per report generated — the standard model for radiology workflow software. Rad AI, the category leader, operates on a per-radiologist subscription basis, which provides predictable recurring revenue but requires a meaningful number of contracted radiologists to generate material revenue.

On unit economics: with $500K in total funding and two employees, RadMate AI's annual burn rate was likely in the range of $300K–$500K, depending on founder salaries, infrastructure costs, and any sales or compliance expenditures. At that burn rate, the company had approximately 12–18 months of runway from the April 2024 funding announcement — placing the likely exhaustion of funds in mid-to-late 2025 at the latest, and potentially earlier if the founders drew market-rate salaries. These are inferences from headcount and funding data, not confirmed figures.

To cover even a modest $400K annual burn through SaaS revenue, the company would have needed roughly 30–50 paying radiologist seats at $700–$1,000 per seat per month — a plausible target in isolation, but one that requires signed hospital contracts, which in turn require the procurement process described above. There is no evidence the company reached this threshold.

## Traction

The only available traction signal is a LinkedIn post from Mohamed Khalifa's father, Taha Khalifa, published on February 5, 2024 — the day of the YC launch — stating that the product was "already getting a lot of attention from many radiology and healthcare institutions."<sup><a href="https://www.linkedin.com/posts/taha-khalifa-1530b52_launch-yc-radmate-ai-the-ai-copilot-activity-7160362420715073538-uofY">[31]</a></sup> This is a low-confidence data point: the source is a family member, the claim is unquantified, and "attention" does not indicate signed contracts or revenue.

RadMate AI's LinkedIn company page had only 250 followers as of the most recent available data.<sup><a href="https://www.linkedin.com/company/radmate-ai">[32]</a></sup> For context, Rad AI's LinkedIn page has tens of thousands of followers. The 250-follower figure is consistent with a company that generated initial interest at YC launch but did not sustain public momentum.

No customer announcements, pilot agreements, case studies, press coverage beyond the initial launch, or revenue figures were found in any public source. The company did not appear in any healthcare AI trade press, radiology industry publications, or investor portfolio announcements after April 2024.

## Post-Mortem

### Primary Cause: Structural Capital Mismatch for Enterprise Healthcare Sales

The most important failure factor was not a product flaw or a strategic misstep — it was a fundamental mismatch between the resources required to sell into hospitals and the resources the company had.

Enterprise healthcare AI sales cycles are long by structural necessity. A hospital evaluating a new AI vendor must complete security and privacy reviews (HIPAA compliance documentation, data processing agreements, penetration testing), clinical validation (demonstrating the tool performs as claimed in the hospital's specific environment), EHR integration testing (ensuring the tool connects to the hospital's existing PACS and reporting systems), and legal review of the vendor contract. This process typically takes 12 to 24 months even for established vendors with existing hospital relationships. For a new vendor with no track record, it takes longer.

RadMate AI had $500K in total funding and two employees.<sup><a href="https://pitchbook.com/profiles/company/593104-15">[33]</a></sup><sup><a href="https://www.cbinsights.com/company/radmate-ai">[34]</a></sup> At a conservative burn rate of $35K–$40K per month, the company had roughly 12–14 months of runway from Demo Day. That runway was insufficient to close even a single enterprise hospital contract through a standard procurement process, let alone build the revenue base needed to justify a seed round from institutional investors.

The company appears to have attempted to raise a seed round following YC Demo Day in April 2024 — this is the standard YC playbook. No seed round was ever announced. The most likely explanation is that investors, evaluating the company against the backdrop of Rad AI's $50M Series B (announced just weeks later), concluded that the market had already produced a dominant incumbent and that RadMate AI lacked the differentiation or traction to compete.

### Secondary Cause: Incumbent Lock-In by a Well-Capitalized Competitor

Rad AI's market position at the time of RadMate AI's launch was not merely a competitive disadvantage — it was a structural barrier. By April 2024, Rad AI was already embedded in more than a third of all U.S. health systems and 9 of the 10 largest U.S. radiology practices.<sup><a href="https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai">[35]</a></sup> These are not customers who can be easily displaced: once a radiology AI reporting tool is integrated into a hospital's PACS and EHR workflow, the switching cost is high. Radiologists have learned the interface, templates have been customized, and the vendor has cleared the hospital's compliance requirements.

For RadMate AI to win customers, it would have needed to either displace Rad AI at existing accounts (extremely difficult given switching costs) or capture new accounts before Rad AI did (difficult given Rad AI's sales team and brand recognition). Neither path was accessible with two employees and $500K.

The capital disparity compounded this problem. Rad AI's $50M Series B funded a sales organization, compliance infrastructure, and integration engineering team that RadMate AI could not replicate. In enterprise healthcare AI, distribution is not just a go-to-market advantage — it is a product advantage, because a vendor with existing hospital relationships can deploy faster, iterate based on real clinical feedback, and build the validation data that future customers require.

### Tertiary Cause: Team Size Insufficient for a Regulated Product

Building a clinical workflow tool for hospital deployment requires more than engineering talent. It requires dedicated resources for regulatory affairs (even for non-diagnostic AI tools, hospitals require documentation of the product's intended use, data handling, and validation methodology), sales and customer success (hospital procurement requires sustained relationship management over months), and integration engineering (connecting to PACS systems and EHRs is a significant technical undertaking that varies by hospital).

A two-person team of engineers — however talented — cannot simultaneously build the product, manage hospital procurement processes, maintain compliance documentation, and conduct the sales conversations required to close enterprise deals. The team would have needed to hire before it had revenue, which required raising a seed round, which required demonstrating traction, which required closing customers. This circular dependency is common in healthcare AI startups, but it is survivable only with enough capital to hire ahead of revenue. RadMate AI did not have that capital.

### Structural Factor: The "Feature vs. Company" Problem in Radiology Reporting

At a category level, AI-assisted radiology report generation is a feature that large incumbents in the radiology software space — including existing speech recognition and reporting vendors like Nuance (now part of Microsoft) and Philips — could absorb into their existing products. Nuance's Dragon Medical One, already deployed across thousands of hospitals, added AI-assisted reporting capabilities during the same period RadMate AI was operating. A hospital already using Dragon Medical One had little incentive to evaluate a new vendor for a feature that its existing vendor was adding natively.

This "feature absorption" dynamic is a structural risk for any startup building workflow automation on top of an existing clinical process. The incumbents have the distribution, the existing compliance relationships, and the integration depth. A startup can win if it moves fast enough to establish a defensible position before incumbents catch up — but that requires capital and speed that RadMate AI did not have.

### What Was Not the Problem

The founders' domain expertise was genuine and relevant. Khalifa's PathAI experience building workflow tools for pathologists was directly applicable to radiology reporting. Skrocki's Palantir background in enterprise AI deployment was relevant to the sales and integration challenges ahead. The problem statement was well-quantified and real — radiology report errors and dictation inefficiency are documented pain points in the clinical literature. The product concept was sound. The failure was not a bad idea poorly executed; it was a structurally underfunded entry into a market that had already produced a dominant, well-capitalized incumbent.

## Key Lessons

- **$500K is not enough to close a single enterprise hospital contract, let alone build a company.** RadMate AI's total funding was structurally insufficient for its chosen market. Hospital procurement for AI tools requires 12–24 months of sustained sales effort, compliance documentation, and integration work — all of which require dedicated headcount. The YC standard deal funds a consumer app or a developer tool; it does not fund an enterprise healthcare sales cycle. Founders entering regulated healthcare markets should either raise a larger pre-seed before YC (using YC as a signal amplifier, not a primary funder) or target a customer segment — independent radiology practices, for example — where procurement cycles are measured in weeks rather than years.

- **Entering a market where the category leader has already locked up distribution is not a product problem — it is a market access problem that product quality cannot solve.** By April 2024, Rad AI was embedded in more than a third of all U.S. health systems. RadMate AI would have needed to displace an entrenched vendor with high switching costs, or race to capture the remaining accounts before Rad AI did — both requiring resources RadMate AI did not have. The lesson is not "don't compete with incumbents" but rather "map the distribution landscape before choosing a market, and size your funding to the competitive reality, not the product roadmap."

- **Personal domain access (a radiologist father) is a valuable but non-transferable asset.** Skrocki's father gave the team genuine insight into the radiologist workflow — a real advantage over founders who had never spoken to a radiologist. But that access did not translate into a paying customer, a clinical pilot, or a reference account. In healthcare enterprise sales, the decision-maker is rarely the end user: hospital procurement involves IT, legal, compliance, and finance stakeholders who are not moved by a founder's personal connection to the clinical problem. RadMate AI needed institutional access — a hospital system willing to run a formal pilot — not just informal domain expertise.

- **Positioning a product as "workflow AI" rather than "diagnostic AI" reduces regulatory burden but does not reduce procurement burden.** RadMate AI appears to have deliberately avoided the diagnostic AI regulatory pathway, positioning its product as a documentation tool. This was a reasonable choice. But hospitals do not have a fast lane for "workflow AI" — the same security reviews, data governance requirements, and clinical validation processes apply regardless of whether the AI is reading images or formatting reports. The regulatory shortcut did not produce a procurement shortcut, and the company's runway ran out before it could clear the standard procurement gates.

- **The absence of any post-launch press coverage is a leading indicator of failure in enterprise healthcare AI.** Companies that close hospital pilots announce them — because a signed hospital contract is the most credible signal available to seed investors in this category. RadMate AI generated no press coverage, no customer announcements, and no case studies in the 12 months following its YC launch. This silence, combined with the failure to announce a seed round, is consistent with a company that could not convert investor and institutional interest into signed contracts before its runway expired.

## Sources

1. [Y Combinator — RadMate AI company profile](https://www.ycombinator.com/companies/radmate-ai)
2. [YC Launch: RadMate AI — The AI Copilot for Radiologists](https://www.ycombinator.com/launches/KIh-radmate-ai-the-ai-copilot-for-radiologists)
3. [PitchBook — RadMate AI company profile](https://pitchbook.com/profiles/company/593104-15)
4. [Rad AI — $50M Series B announcement](https://www.radai.com/news/rad-ai-closes-50-million-to-empower-physicians-with-ai)
5. [Mohamed Khalifa — LinkedIn profile](https://www.linkedin.com/in/mohamed-taha-khalifa)
6. [RadMate AI — LinkedIn company page](https://www.linkedin.com/company/radmate-ai)
7. [Crunchbase — RadMate AI organization profile](https://www.crunchbase.com/organization/radmate-ai)
8. [CB Insights — RadMate AI company profile](https://www.cbinsights.com/company/radmate-ai)
9. [Crunchbase — RadMate AI Pre-Seed funding round](https://www.crunchbase.com/funding_round/radmate-ai-pre-seed--73a06648)
10. [LinkedIn — Y Combinator post announcing RadMate AI launch](https://www.linkedin.com/posts/y-combinator_launch-yc-radmate-ai-the-ai-copilot-activity-7160346340202311681-e_0E)
11. [LinkedIn — Taha Khalifa post on RadMate AI launch](https://www.linkedin.com/posts/taha-khalifa-1530b52_launch-yc-radmate-ai-the-ai-copilot-activity-7160362420715073538-uofY)
12. [LinkedIn — Mohamed Khalifa Demo Day post](https://www.linkedin.com/posts/mohamed-taha-khalifa_cant-believe-y-combinators-demo-day-is-activity-7181068150782803970-x3us)
13. [HireTop — RadMate AI profile](https://hiretop.com/blog2/radmate-ai-radiologists-copilot/)
14. [RadMate AI — website (inactive)](https://www.radmate.ai/)
15. [IDCrawl — Adam Skrocki profile](https://www.idcrawl.com/adam-skrocki)
