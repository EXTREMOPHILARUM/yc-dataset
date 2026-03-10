# Research Report: VOIQ

## Overview

Ricardo Garcia-Amaya and Jessica Taggart founded VOIQ in 2014 in San Francisco. Their backgrounds were unusual for a company that would eventually stake its identity on cutting-edge AI voice technology.

Garcia-Amaya's path to tech entrepreneurship ran through public policy. Before VOIQ, he worked as an Associate at the NYC Mayor's Office under Michael Bloomberg, where he helped develop the technology blueprint for New York City. He later served as campaign CTO for Angel Taveras, the first Latino mayor of Providence, Rhode Island. He holds an MBA from NYU Stern School of Business and an undergraduate degree in Politics from NYU. <sup><a href="https://www.founderlodge.com/round/ILUMA-raises-1500000-Pre-Seed-2023-09-26-Ricardo-Garcia-Amaya-MTU1NDg">[1]</a></sup> <sup><a href="https://wefunder.com/voiq">[2]</a></sup> Born in New York City but raised on a farm on the outskirts of Bogotá, Colombia, Garcia-Amaya brought a cross-cultural perspective to sales communication — a theme that would shape VOIQ's early product design. <sup><a href="https://contxto.com/en/startups/voiq-lands-us2-million-from-silicon-valley-investors-for-voice-ai-solution/">[3]</a></sup>

Taggart joined as COO. A third co-founder, Dana Spiegel, is listed by Tracxn as CTO, though his tenure, contributions, and departure from the company are entirely undocumented in public records. <sup><a href="https://tracxn.com/d/companies/voiq/__tKo1OmHbWDk2GxbHCcmo1rVql59e_E9-OKWYRymuO1U">[4]</a></sup> This gap matters: the technical leadership of a company building conversational AI is a critical variable, and its absence from the public record is a meaningful signal.

The founding insight was straightforward. Sales and marketing teams were spending enormous resources on outbound phone calls — cold outreach, lead qualification, appointment setting — that were repetitive, expensive, and inconsistent in quality. Garcia-Amaya's experience in political campaigns, where phone banking is a core organizing tool, likely sharpened his view of this problem. The initial solution was not AI at all: it was a labor marketplace that made human call agents available on demand, matched to leads using what the company called "psychoanalytic" trait analysis. <sup><a href="https://www.ycombinator.com/blog/voiq-yc-s15-provides-companies-with-call-center-services-on-demand/">[5]</a></sup>

VOIQ moved through two accelerators in rapid succession. It graduated from TechStars in 2014, then entered Y Combinator's Summer 2015 batch. <sup><a href="https://www.foundertherapy.co/clients/voiq">[6]</a></sup> <sup><a href="https://www.ycombinator.com/companies/voiq">[7]</a></sup> The double-accelerator path demonstrated strong pitch ability and network-building — but also a reliance on institutional validation at a stage when most companies are focused on customer development.

The original vision was to be the infrastructure layer for business phone calls — first with humans, then with AI. The pivot from human agents to AI voicebots was not a sudden strategic shift but a gradual migration that took roughly four years, from 2015 to 2019.

---

## Founding Story

### Timeline

- **2014** — VOIQ founded by Ricardo Garcia-Amaya and Jessica Taggart in San Francisco/Redwood City, CA. <sup>[[8]](https://techstartups.com/2019/11/05/ycombinator-backed-startup-voiq-secures-5m-funding-build-future-ai-voice/)</sup>
- **2014** — VOIQ graduates from TechStars accelerator. <sup>[[6]](https://www.foundertherapy.co/clients/voiq)</sup>
- **Summer 2015** — VOIQ participates in Y Combinator S15 batch with its "Uber for telemarketing" on-demand call center product. <sup>[[7]](https://www.ycombinator.com/companies/voiq)</sup>
- **August 2015** — VOIQ closes its first Seed funding round. <sup>[[4]](https://tracxn.com/d/companies/voiq/__tKo1OmHbWDk2GxbHCcmo1rVql59e_E9-OKWYRymuO1U)</sup>
- **2015–2018** — VOIQ pivots from human call center marketplace toward "virtualization of on-demand sales teams," then begins developing AI conversational voicebots. <sup>[[9]](https://www.foundertherapy.co/clients/voiq)</sup>
- **February 2019** — VOIQ launches its SaaS VoiceBot platform with 700+ customers at launch. <sup>[[10]](https://techstartups.com/2019/11/05/ycombinator-backed-startup-voiq-secures-5m-funding-build-future-ai-voice/)</sup>
- **November 2019** — VOIQ raises $2M additional funding led by LEAP Global Ventures, bringing total disclosed funding to $5M. Wefunder campaign claims $1M ARR, profitability, and customers including AB-InBev, Airbnb, and Aflac. <sup>[[11]](https://www.prnewswire.com/news-releases/5m-total-funding-for-ycombinator-backed-voiq-to-build-the-future-of-ai-voice-300952048.html)</sup>
- **March 2020** — LEAP Managing Partner Roman Leal publicly endorses VOIQ's conversational voicebot technology. <sup>[[12]](https://contxto.com/en/startups/voiq-lands-us2-million-from-silicon-valley-investors-for-voice-ai-solution/)</sup>
- **April 2020** — VOIQ pivots its call platform for COVID-19 response, offering free access to government officials and health and senior care organizations. <sup>[[13]](https://www.zoominfo.com/c/voiq-inc/374951657)</sup>
- **August 2020** — GetLatka reports VOIQ at $2.2M revenue, 700 customers, 21 employees. <sup>[[14]](https://getlatka.com/companies/voiq)</sup>
- **August 2021** — VOIQ launches a Fundraising Voice Assistant product. <sup>[[15]](https://www.owler.com/company/voiq)</sup>
- **November 2021** — VOIQ posts its last known public content (YouTube video). Company appears to wind down sometime after this date. <sup>[[15]](https://www.owler.com/company/voiq)</sup>
- **2022** — VOIQ shuts down. Blog displays farewell message thanking customers, investors, and employees. Listed as permanently closed on Crunchbase and deadpooled on Tracxn. <sup>[[16]](https://www.crunchbase.com/organization/voiq)</sup>
- **September 2023** — Ricardo Garcia-Amaya and Jessica Taggart co-found ILUMA, an AI copilot for C-level executives, raising a $1.5M Pre-Seed round. <sup>[[17]](https://www.founderlodge.com/round/ILUMA-raises-1500000-Pre-Seed-2023-09-26-Ricardo-Garcia-Amaya-MTU1NDg)</sup>

---

## What They Built

VOIQ built three distinct products over its eight-year life. Understanding the sequence matters because each pivot carried forward the customer relationships of the previous version while abandoning its technical architecture.

### Phase 1: On-Demand Human Call Center (2014–2018)

The original product was a labor marketplace, not an AI system. Businesses uploaded their lead lists and call scripts to VOIQ's platform. VOIQ's algorithm then matched each lead to one of thousands of trained remote call agents based on shared characteristics — language, geographic location, and what the company called "psychoanalytic" trait matching. <sup><a href="https://www.ycombinator.com/blog/voiq-yc-s15-provides-companies-with-call-center-services-on-demand/">[5]</a></sup> The pitch was that a better-matched agent would convert more leads. Early customers included Stanford University and Airbnb.

The structural problem with this model was unit economics. Every call required a human agent, which meant costs scaled linearly with volume. Quality control across a distributed workforce was difficult to enforce. The "Uber for telemarketing" framing was well-timed for the 2015 on-demand economy investment thesis, but the underlying business faced the same margin compression that plagued most labor marketplaces.

### Phase 2: AI VoiceBot SaaS Platform (2019–2021)

VOIQ launched its SaaS VoiceBot platform in February 2019, replacing human agents with AI-driven voice conversations. <sup><a href="https://techstartups.com/2019/11/05/ycombinator-backed-startup-voiq-secures-5m-funding-build-future-ai-voice/">[10]</a></sup> The product was a B2B SaaS tool that let sales, marketing, and customer service teams deploy automated phone calls at scale.

The core workflow was straightforward: a business connected its CRM (HubSpot, Salesforce, Outreach, or Zapier) to VOIQ's platform, uploaded a contact list, and configured a voicebot with a specific goal — scheduling a meeting, qualifying a lead, collecting a payment, or reminding a prospect of an upcoming demo. <sup><a href="https://www.producthunt.com/products/voiq?launch=voiq-voicebots-2">[18]</a></sup> The voicebot would then call contacts automatically, conduct a natural-language conversation, and either complete the task or transfer the call to a live human agent if the lead expressed strong interest.

VOIQ also offered a "VoiceBot for Web" product, which embedded a voice interface directly into a company's website, allowing visitors to speak with an AI rather than fill out a form. A "Clone-Your-Voice" feature let businesses record a human voice and use it as the basis for the AI's speech synthesis. <sup><a href="https://www.voiq.com/product/voicebot-for-web">[19]</a></sup>

What differentiated VOIQ from basic robocall systems was the claim of genuine conversational ability — the voicebot could handle interruptions, answer questions, and adapt to unexpected responses rather than following a rigid script. This was the technically demanding part of the product, and the part where execution quality mattered most.

### Phase 3: Opportunistic Extensions (2020–2021)

In April 2020, VOIQ repurposed its platform for COVID-19 community outreach, offering free access to government agencies and health organizations to conduct wellness check calls and information dissemination. <sup><a href="https://www.zoominfo.com/c/voiq-inc/374951657">[13]</a></sup> In August 2021, the company launched a Fundraising Voice Assistant aimed at nonprofit and political fundraising. <sup><a href="https://www.owler.com/company/voiq">[15]</a></sup> These extensions suggest the team was searching for use cases where the technology's limitations were less exposed — lower-stakes conversations where a rigid script was more acceptable.

---

## Market Position

### Target Customers

VOIQ's primary customers were B2B sales and marketing teams at mid-market companies that ran high-volume outbound call programs. The product was designed for teams that needed to make hundreds or thousands of calls per week — lead qualification, appointment setting, payment reminders — but could not afford to staff a full-time call center. Named customers from the Wefunder campaign included AB-InBev, Airbnb, and Aflac, suggesting VOIQ had penetrated enterprise accounts alongside smaller customers. <sup><a href="https://wefunder.com/voiq">[20]</a></sup>

The COVID-19 pivot briefly expanded the target customer to government agencies and healthcare organizations, though this appears to have been a free-access initiative rather than a revenue-generating segment.

### Market Size

The addressable market for outbound sales automation was large and growing. The global call center software market was valued at approximately $17 billion in 2019 and was projected to expand significantly as AI capabilities improved. Within that, the outbound sales automation segment — covering dialers, sequencing tools, and conversation intelligence — represented a multi-billion-dollar opportunity. VOIQ's Wefunder materials cited a $350 billion global call center market as the total addressable market, though the serviceable segment for an AI voicebot SaaS product was considerably smaller. <sup><a href="https://wefunder.com/voiq">[20]</a></sup>

The timing was theoretically favorable. Enterprise buyers were actively looking to reduce call center labor costs, and the 2019–2021 period saw significant investment in conversational AI across the industry. The problem was that market readiness for fully automated voice conversations — as opposed to human-assisted or text-based automation — lagged behind investor enthusiasm.

### Competition

VOIQ competed in a crowded and well-funded space. Its most direct competitors were:

**Conversica** — An AI sales assistant company that had raised over $90 million by 2019. Conversica focused primarily on email and text-based follow-up rather than voice, which gave VOIQ a potential differentiation angle, but also reflected the market's preference for text-based AI automation where the technology was more mature.

**Dialpad and Gong** — Conversation intelligence platforms that used AI to analyze calls made by human agents, rather than replacing agents entirely. These companies raised hundreds of millions of dollars and achieved significant scale, suggesting that the market preferred AI-augmented humans over fully automated voice agents in this period.

**Outreach and SalesLoft** — Sales engagement platforms that automated email and call sequencing. Both companies raised large rounds and achieved unicorn valuations, but neither attempted to replace human callers with AI voice — a telling signal about where enterprise buyers drew the line.

**Nuance Communications and Google CCAI** — Enterprise-grade conversational AI platforms with far greater engineering resources. These platforms targeted large contact centers rather than mid-market sales teams, but their existence set a quality benchmark that smaller players like VOIQ struggled to match.

The competitive landscape revealed a structural problem for VOIQ: the companies that succeeded in adjacent spaces either avoided fully automated voice (Conversica, Outreach) or had vastly more engineering resources (Nuance, Google). VOIQ was attempting to build production-quality conversational AI with a team of 21 people and $5 million in total funding.

---

## Business Model

VOIQ operated as a SaaS subscription business with usage-based components. The Wefunder campaign claimed 70% gross margins on every call, a customer acquisition cost of $1,000, and a lifetime customer value of $60,000 — implying a 60:1 LTV/CAC ratio that, if accurate, would represent an exceptionally efficient business. <sup><a href="https://wefunder.com/voiq">[21]</a></sup>

The platform was priced per voicebot or per call volume, with integrations into HubSpot, Salesforce, Outreach, and Zapier serving as the primary distribution channels. <sup><a href="https://www.producthunt.com/products/voiq?launch=voiq-voicebots-2">[18]</a></sup> The integration-led distribution strategy was sound: embedding into existing sales workflows reduced friction for adoption and created switching costs once customers had configured their voicebots.

By November 2019, the company claimed $1M ARR. <sup><a href="https://wefunder.com/voiq">[20]</a></sup> By August 2020, GetLatka reported $2.2M in total revenue with 700 customers and 21 employees. <sup><a href="https://getlatka.com/companies/voiq">[14]</a></sup> At that revenue level and headcount, the company was burning cash — $2.2M in revenue against a 21-person team in the Bay Area implied a monthly burn rate that would exhaust the $2M raised in November 2019 within 18–24 months, which aligns with the estimated 2022 shutdown date.

---

## Traction

VOIQ's traction figures come primarily from self-reported sources and carry meaningful uncertainty.

At the February 2019 SaaS launch, the company claimed 700+ customers — a figure that likely reflected conversions from its earlier human-agent platform rather than new SaaS acquisitions. <sup><a href="https://techstartups.com/2019/11/05/ycombinator-backed-startup-voiq-secures-5m-funding-build-future-ai-voice/">[10]</a></sup> The November 2019 Wefunder campaign claimed $1M ARR, profitability, 70% margins, and over 1 million voice conversations conducted through the platform. <sup><a href="https://wefunder.com/voiq">[20]</a></sup> <sup><a href="https://wefunder.com/voiq">[22]</a></sup>

By August 2020, GetLatka reported $2.2M in revenue, still 700 customers, and 21 employees. <sup><a href="https://getlatka.com/companies/voiq">[14]</a></sup> The flat customer count between February 2019 and August 2020 — 700 at both data points — is notable. It suggests either that VOIQ was not acquiring new customers at a meaningful rate, or that new customer acquisition was roughly offsetting churn. Neither interpretation supports the growth trajectory needed for a Series A.

The revenue figures across sources are inconsistent: $1M ARR (November 2019, Wefunder), $2.2M revenue (August 2020, GetLatka), with other sources citing figures ranging from $4.12M to $7M in total funding raised. <sup><a href="https://golden.com/wiki/Ricardo_Garcia-Amaya-K46X4J8">[23]</a></sup> The discrepancy between ARR and total revenue figures may reflect different measurement methodologies, but the inconsistency makes it difficult to construct a reliable growth curve.

VOIQ's Wefunder campaign cited partnerships with Salesforce, HubSpot, Outreach, and SalesLoft as distribution channels. <sup><a href="https://wefunder.com/voiq">[22]</a></sup> These integrations were real — the product was listed on the HubSpot App Marketplace and Zapier — but partnership listings do not translate automatically into customer acquisition.

---

## Post-Mortem

VOIQ's failure was not a single catastrophic event. It was a slow-motion mismatch between what the company promised and what its technology could deliver, compounded by engineering execution problems and a funding trajectory that ran out before the underlying AI infrastructure matured.

### Primary Cause: The Technology Was Not Ready, and VOIQ Could Not Build It

The central problem was that VOIQ's core product — a voicebot that could conduct genuinely natural, open-ended phone conversations — required capabilities that were at the frontier of commercially available AI in 2019–2021.

Building a production-quality conversational voicebot requires at least three distinct technical components working in real time: automatic speech recognition (converting spoken words to text), natural language understanding (interpreting intent and generating an appropriate response), and text-to-speech synthesis (converting the response back to natural-sounding audio). Each of these components had to perform reliably under real-world conditions — background noise, accents, interruptions, unexpected questions — with latency low enough that the conversation did not feel robotic.

In 2019, the best available speech recognition systems (Google, AWS, Azure) were good but not perfect. Natural language understanding for open-ended conversations was still a significant research problem. Text-to-speech synthesis had improved dramatically but still sounded artificial under close scrutiny. Companies with hundreds of engineers and billions in compute budgets — Google, Amazon, Microsoft — were working on these problems simultaneously. VOIQ was attempting to assemble a production system from these components with a team of 21 people and $5 million in total funding.

The gap between what was technically achievable and what VOIQ's marketing promised was significant. The company's materials described voicebots that could "handle interruptions, answer questions, and adapt to unexpected responses." In practice, conversational AI systems of this era worked well for narrow, scripted use cases — appointment reminders, payment collection — but degraded quickly when conversations went off-script. There are no documented customer complaints about voicebot quality in the public record, but the pattern of product pivots and the flat customer count between 2019 and 2020 are consistent with a product that worked well enough to attract customers but not well enough to retain them or generate referrals.

### Secondary Cause: Engineering Execution Broke Down Internally

FounderTherapy, a consulting firm that worked with VOIQ, documented a specific internal failure: the engineering team began to struggle, and the CEO had difficulty understanding where the problems were. The company required outside help to instill processes and practices for a 10+ person development team. <sup><a href="https://www.foundertherapy.co/clients/voiq">[24]</a></sup>

This is a meaningful signal. Garcia-Amaya's background was in public policy and strategy — not software engineering. Taggart's background was in operations. The CTO, Dana Spiegel, is entirely absent from the public record after the company's founding — no interviews, no LinkedIn activity associated with VOIQ, no documented departure. Whether Spiegel left early or remained throughout is unknown, but the absence of any technical co-founder voice in VOIQ's public narrative is striking for a company building one of the most technically demanding products in enterprise software.

The pattern of multiple pivots — human agents to virtualized sales teams to AI voicebots to COVID platform to fundraising assistant — may reflect not just market exploration but an inability to achieve technical depth in any single direction. Each pivot reset the engineering roadmap and diluted the team's focus. By the time VOIQ committed fully to AI voicebots in 2019, it had spent four years building a different product and had limited time to close the gap with better-funded competitors.

### Tertiary Cause: The Funding Trajectory Could Not Support the Required Investment

VOIQ raised approximately $5 million over eight years — a modest total for a company attempting to build frontier AI infrastructure. <sup><a href="https://www.prnewswire.com/news-releases/5m-total-funding-for-ycombinator-backed-voiq-to-build-the-future-of-ai-voice-300952048.html">[11]</a></sup> The November 2019 round of $2M was the last disclosed funding event. No Series A followed.

The four-year gap between the 2015 seed and the 2019 round implies either bootstrapped growth or undisclosed bridge financing during the pivot years. Either way, the company was operating with limited capital during the period when it was attempting to build its most technically ambitious product.

At $2.2M in revenue and 21 employees in August 2020, VOIQ's burn rate almost certainly exceeded its revenue. A 21-person team in the Bay Area, including engineers working on AI systems, would cost $3–4M annually in fully loaded compensation alone. The $2M raised in November 2019 would have been exhausted by late 2021 under these assumptions — consistent with the November 2021 last public activity date and the 2022 shutdown.

The failure to raise a Series A after November 2019 is the clearest investor signal. VOIQ had credible investors (YC, LEAP, 10XCapital) and a real customer base. The fact that none of them led a follow-on round suggests that the growth metrics — flat customer count, modest revenue relative to burn — did not support the valuation required for a Series A in the 2020–2021 market.

### Compounding Factor: Opportunistic Pivots Diluted Focus

The COVID-19 pivot in April 2020 and the Fundraising Voice Assistant launch in August 2021 are symptomatic of a company searching for a use case where its technology's limitations were less exposed. <sup><a href="https://www.zoominfo.com/c/voiq-inc/374951657">[13]</a></sup> <sup><a href="https://www.owler.com/company/voiq">[15]</a></sup>

The COVID platform was offered for free, which generated press coverage but no revenue. The fundraising assistant targeted a narrow vertical with different buying cycles and compliance requirements than the core B2B sales market. Neither extension addressed the fundamental problem: the core voicebot technology was not performing well enough to drive the retention and expansion revenue needed to sustain the business.

LEAP Managing Partner Roman Leal said at the time of the 2019 investment: "VOIQ is solving a problem that so many people believed unsolvable. Bringing human-like conversational voicebots to automate business calls is a game-changer for high-growth companies." <sup><a href="https://contxto.com/en/startups/voiq-lands-us2-million-from-silicon-valley-investors-for-voice-ai-solution/">[12]</a></sup> The investor's framing — "a problem that so many people believed unsolvable" — inadvertently captured the core risk. The problem was unsolvable at VOIQ's scale and funding level in 2019. It became more tractable after 2022, when large language models dramatically improved the natural language understanding component of conversational AI. VOIQ did not survive long enough to benefit from that infrastructure shift.

VOIQ's farewell message, posted to its blog before shutdown, read: "had a great ride. Thank you for letting us play a role in connecting you with your customers through the power of conversational AI Voice. We would like to thank our customers, investors and employees for all their hard work and support." <sup><a href="http://blog.voiq.com/author/jessica-taggart">[25]</a></sup> No explanation of the closure was offered.

---

## Key Lessons

- **Frontier AI products require frontier AI engineering capacity.** VOIQ attempted to build production-quality conversational voice AI — a problem that Google, Amazon, and Microsoft were simultaneously spending billions to solve — with a 21-person team and $5 million in total funding. The gap between the product's marketing claims and its technical reality was not a failure of vision but a failure to match ambition with resources. Companies building at the frontier of AI infrastructure need either deep technical co-founders or the capital to hire them before committing to a product roadmap that depends on capabilities not yet commercially available.

- **A business-heavy founding team building a technical product needs a documented technical leader.** VOIQ's CTO, Dana Spiegel, is entirely absent from the company's public narrative. When the engineering team began to struggle — as documented by FounderTherapy — the CEO lacked the technical background to diagnose the problems. <sup><a href="https://www.foundertherapy.co/clients/voiq">[24]</a></sup> For companies where the product is the technology, the technical co-founder's visibility, tenure, and engagement are leading indicators of execution risk.

- **Flat customer count is a more honest metric than revenue growth.** VOIQ reported 700 customers at its February 2019 SaaS launch and still reported 700 customers in August 2020. <sup><a href="https://techstartups.com/2019/11/05/ycombinator-backed-startup-voiq-secures-5m-funding-build-future-ai-voice/">[10]</a></sup> <sup><a href="https://getlatka.com/companies/voiq">[14]</a></sup> Revenue growth during that period (from $1M ARR to $2.2M) likely reflected expansion within existing accounts or pricing changes rather than new customer acquisition. Investors evaluating AI SaaS companies should weight net new customer acquisition and net revenue retention more heavily than headline revenue figures, particularly when the customer count is static.

- **Opportunistic pivots in response to market events signal a product that has not found its core use case.** The COVID-19 platform and the Fundraising Voice Assistant were launched when the core B2B sales voicebot product was not growing. Both extensions required engineering resources that could have been directed at improving the core product's quality. Companies that pivot toward adjacent use cases in response to external events — rather than in response to strong customer pull — often end up with a fragmented product and a diluted engineering roadmap.

- **The timing of infrastructure-dependent products is as important as the product itself.** VOIQ's core technology became significantly more viable after 2022, when large language models transformed the natural language understanding component of conversational AI. The founders' next company, ILUMA, is built on LLM-based text interfaces rather than real-time voice — a direct lesson applied. Companies building on AI infrastructure should assess not just whether the technology works today, but whether it will work well enough to retain customers before the company's runway expires.

---

## Sources

1. [TechStartups — VOIQ secures $5M funding (November 5, 2019)](https://techstartups.com/2019/11/05/ycombinator-backed-startup-voiq-secures-5m-funding-build-future-ai-voice/)
2. [Tracxn — VOIQ company profile](https://tracxn.com/d/companies/voiq/__tKo1OmHbWDk2GxbHCcmo1rVql59e_E9-OKWYRymuO1U)
3. [Y Combinator — VOIQ company page](https://www.ycombinator.com/companies/voiq)
4. [YCDB — VOIQ company profile](https://www.ycdb.co/company/voiq)
5. [FounderLodge — ILUMA Pre-Seed round / Ricardo Garcia-Amaya profile](https://www.founderlodge.com/round/ILUMA-raises-1500000-Pre-Seed-2023-09-26-Ricardo-Garcia-Amaya-MTU1NDg)
6. [Wefunder — VOIQ campaign](https://wefunder.com/voiq)
7. [Contxto — VOIQ lands $2M from Silicon Valley investors (March 19, 2020)](https://contxto.com/en/startups/voiq-lands-us2-million-from-silicon-valley-investors-for-voice-ai-solution/)
8. [FounderTherapy — VOIQ client profile](https://www.foundertherapy.co/clients/voiq)
9. [Y Combinator Blog — VOIQ (YC S15) Provides Companies With Call Center Services On-Demand](https://www.ycombinator.com/blog/voiq-yc-s15-provides-companies-with-call-center-services-on-demand/)
10. [PR Newswire — $5M Total Funding for YCombinator-backed VOIQ (November 5, 2019)](https://www.prnewswire.com/news-releases/5m-total-funding-for-ycombinator-backed-voiq-to-build-the-future-of-ai-voice-300952048.html)
11. [Product Hunt — VOIQ VoiceBots product page](https://www.producthunt.com/products/voiq?launch=voiq-voicebots-2)
12. [VOIQ — VoiceBot for Web product page](https://www.voiq.com/product/voicebot-for-web)
13. [ZoomInfo — VOIQ Inc. company profile (April 9, 2020)](https://www.zoominfo.com/c/voiq-inc/374951657)
14. [GetLatka — VOIQ company data](https://getlatka.com/companies/voiq)
15. [Owler — VOIQ company profile (August 29, 2021 / November 18, 2021)](https://www.owler.com/company/voiq)
16. [Crunchbase — VOIQ organization page](https://www.crunchbase.com/organization/voiq)
17. [SaaSworthy — VOIQ Voicebots listing](https://www.saasworthy.com/product/voiq-voicebots)
18. [VOIQ Blog — Farewell message (Jessica Taggart author page)](http://blog.voiq.com/author/jessica-taggart)
19. [Golden.com — Ricardo Garcia-Amaya profile](https://golden.com/wiki/Ricardo_Garcia-Amaya-K46X4J8)
20. [Jessica Taggart — Twitter/X profile](https://x.com/jttaggart?lang=en)
21. [Y Combinator Blog — Congratulations to the YC Summer 2015 Class](https://www.ycombinator.com/blog/congratulations-to-the-yc-summer-2015-class)
22. [VentureBeat — VOIQ's 'Uber for telemarketing' lets companies create on-demand call centers (August 2015)](https://venturebeat.com/business/voiqs-uber-for-telemarketing-lets-companies-create-on-demand-call-centers/)
23. [LEAP Global Partners Medium — Meet our founders: Ricardo Garcia-Amaya, CEO + Co-Founder of VOIQ](https://leapglobalpartners.medium.com/meet-our-founders-ricardo-garcia-amaya-ceo-co-founder-of-voiq-f79a0e6d6030)
24. [Hispanic Engineer & IT — Ricardo Garcia-Amaya: Top Latino Tech Leader](https://hispanicengineer.com/manage-new/ricardo-garcia-amaya-top-latino-tech-leader/)
25. [Wayback Machine — voiq.com archive index](https://web.archive.org/web/20191201000000*/voiq.com)
