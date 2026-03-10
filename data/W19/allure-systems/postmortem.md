# Research Report: Allure Systems

## Overview

Gabrielle Chou arrived at Allure Systems with a track record that few first-time founders can match. She had already built and sold two companies: ChinaLOOP, a digital marketing platform she sold to Acxiom (NASDAQ: ACXM), and MOOD BY ME, which she exited in 2015.<sup><a href="https://shanghai.nyu.edu/academics/faculty/directory/gabrielle-chou">[1]</a></sup> That background in data-driven marketing and consumer behavior gave her a specific lens on the fashion eCommerce problem: brands were spending enormous sums on photography that still failed to convert shoppers, particularly those outside the narrow size range that traditional model shoots represented.

The market gap Chou identified was both quantifiable and underserved. According to Y Combinator's own batch writeup, 67% of Americans wear a size 12 or above, yet 90% of online fashion catalogs do not represent these women.<sup><a href="https://blog.ycombinator.com/17-companies-from-the-yc-w19-batch-part-4/">[2]</a></sup> This was not merely a social equity observation — it was a commercial inefficiency. Brands were leaving conversion on the table by showing garments only on a single body type, and the cost of fixing that through traditional photography (hiring models across size ranges, booking studios, coordinating shoots) was prohibitive at scale.

To solve the technical side of that problem, Chou partnered with Jeremy Chamoux, a specialist in generative AI, deep learning, and computer vision.<sup><a href="https://www.ycombinator.com/companies/allure-systems">[3]</a></sup> The pairing was classically complementary: a business-oriented serial founder with fashion and retail industry relationships alongside a technical co-founder with the machine learning expertise to build the core product. The two founded Allure Systems in 2017 — the canonical date supported by Y Combinator, PitchBook, and CBInsights, though Tracxn disputes this with a 2015 date that is likely an artifact of Chou's prior venture activity.<sup><a href="https://www.crunchbase.com/organization/allure-systems">[4]</a></sup>

From the start, the company operated across two geographies. Allure Systems Corp was headquartered in Brooklyn, New York, at 37 Greenpoint Avenue, while a fully owned French subsidiary — Allure Systems Research France — handled R&D in Paris.<sup><a href="https://www.cbinsights.com/company/allure-systems">[5]</a></sup><sup><a href="https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/">[6]</a></sup> This dual structure likely reflected Chamoux's technical network and access to European computer vision talent, while the US headquarters positioned the company for enterprise sales to American and global fashion retailers. It also proved strategically useful for accessing French luxury industry relationships — a market where Allure would eventually find its most significant customer validation.

On her personal website, Chou describes the founding mission in direct terms: building "a generative AI solution that produces images for the fashion industry thanks to architectures based on the CNN and GAN algorithms."<sup><a href="https://www.gabriellechou.net/about">[7]</a></sup> The company's selection into Y Combinator's Winter 2019 batch marked a major inflection point, prompting Chou to relocate to the United States for approximately three years to pursue the American enterprise market.<sup><a href="https://shanghai.nyu.edu/academics/faculty/directory/gabrielle-chou">[8]</a></sup>

## Founding Story

### Timeline

- **2015** — Gabrielle Chou sells MOOD BY ME, her second company, completing her second exit before founding Allure Systems<sup>[[9]](https://shanghai.nyu.edu/academics/faculty/directory/gabrielle-chou)</sup>

- **2017** — Allure Systems founded by Gabrielle Chou and Jeremy Chamoux; Allure Systems Research France established as a fully owned subsidiary<sup>[[10]](https://www.crunchbase.com/organization/allure-systems)</sup>

- **September 2017** — First funding round closes; Tracxn reports $3.57M seed (dates and amounts conflict across databases)<sup>[[11]](https://www.cbinsights.com/company/allure-systems/financials)</sup>

- **January 2019** — Allure Systems appears at NRF 2019 (National Retail Federation trade show) in New York, unveiling virtual mannequin size personalization; Gabrielle Chou quoted: "67% of returns are due to sizing errors"

- **March 2019** — Allure AR Fashion iOS app published by Allure Systems Research France, demonstrating AR/3D product capability<sup>[[12]](https://appadvice.com/app/allure-ar-fashion/1386760359)</sup>

- **March 2019** — Allure Systems participates in Y Combinator W19 batch; Chou relocates to the US<sup>[[13]](https://www.ycombinator.com/companies/allure-systems)</sup>

- **March 13, 2019** — Second funding round closes; CBInsights reports $0.15M (amounts conflict across sources)<sup>[[14]](https://www.cbinsights.com/company/allure-systems/financials)</sup>

- **March 2019** — YC W19 Demo Day 2: Allure Systems pitches $1.4M ARR and 14% conversion rate lift to investors; TechCrunch covers the pitch

- **November 2020** — Mark Cuban Companies portfolio page for Allure Systems archived, confirming Cuban's investment<sup>[[15]](https://markcubancompanies.com/companies/allure-systems/)</sup>

- **2021** — Gabrielle Chou appointed Associate Professor of Practice at NYU Shanghai, teaching AI-driven business models<sup>[[16]](https://shanghai.nyu.edu/academics/faculty/directory/gabrielle-chou)</sup>

- **December 20, 2021** — Farfetch (NASDAQ: FTCH) acquires 100% of Allure Systems Corp and Allure Systems Research France in a cash transaction; acquisition price undisclosed<sup>[[17]](https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/)</sup>

- **January 2022** — Farfetch files 20-F with the SEC for fiscal year ending December 31, 2021, referencing the Allure Systems acquisition<sup>[[18]](https://www.sec.gov/Archives/edgar/data/1740915/000156459022008640/ftch-20f_20211231.htm)</sup>

- **March 21, 2023** — The Fashion Law publishes analysis of Farfetch's SEC filing, surfacing acquisition rationale and technology description<sup>[[19]](https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/)</sup>

## What They Built

Allure Systems built a platform that eliminated the most expensive and logistically complex part of fashion eCommerce: the model photography shoot.

The traditional process required a brand to ship physical garments to a studio, book models (typically one or two body types), hire photographers and stylists, and wait days or weeks for edited images. For a retailer with thousands of SKUs across multiple seasons, this process cost tens of millions of dollars annually. Fashion brands collectively spent approximately $8 billion per year on models and photographers — a figure Allure Systems cited directly in its YC Demo Day pitch.<sup><a href="https://techcrunch.com/2019/03/19/here-are-the-88-companies-that-launched-at-ycs-w19-demo-day-2/">[20]</a></sup>

Allure Systems' core product replaced that workflow with a three-step process. A brand submitted a single flat photograph of a garment — a standard product shot taken against a white background. The platform's algorithms, built on convolutional neural networks (CNNs) and generative adversarial networks (GANs), analyzed the garment's texture, drape, and structure.<sup><a href="https://www.gabriellechou.net/about">[21]</a></sup> The system then composited that garment onto a virtualized model — a photorealistic digital representation of a human figure — producing a final image indistinguishable from a traditionally photographed on-figure shot.<sup><a href="https://www.linkedin.com/company/allure-systems">[22]</a></sup>

The key differentiator was scale across body types. From a single garment photograph, a brand could generate images showing that item on model representations ranging from petite to plus-size, instantly and without additional shoots.<sup><a href="https://blog.ycombinator.com/17-companies-from-the-yc-w19-batch-part-4/">[23]</a></sup> This directly addressed the size representation gap that Chou had identified as both a commercial and social problem.

The product also incorporated proprietary hardware alongside the software stack — a component mentioned in company materials but never publicly described in detail.<sup><a href="https://www.linkedin.com/company/allure-systems">[24]</a></sup> Whether this hardware represented a competitive moat or a cost burden is unclear from available sources. What is clear is that the system produced more than static images: it also generated 3D and AR-ready content, extending the utility of each asset beyond a single eCommerce listing.<sup><a href="https://www.linkedin.com/company/allure-systems">[25]</a></sup>

The AR capability was shipped as a standalone consumer-facing product in March 2019. The Allure AR Fashion iOS app, published by Allure Systems Research France, allowed shoppers to scan a QR code and view garments on virtual models in augmented reality, walking around the figure to see all angles.<sup><a href="https://appadvice.com/app/allure-ar-fashion/1386760359">[26]</a></sup> This was a direct product artifact from the French R&D team, demonstrating that the company was building toward volumetric, interactive fashion content — not just flat image replacement.

By the time of the Farfetch acquisition in December 2021, the technology had matured to what Farfetch described as "360-degree renderings" — suggesting the product had evolved from flat compositing toward volumetric representation capable of showing a garment from any angle.<sup><a href="https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/">[27]</a></sup> The company filed one patent during its operating life, providing some degree of proprietary defensibility, though the specific claims are not publicly documented.<sup><a href="https://www.cbinsights.com/company/allure-systems">[28]</a></sup>

## Market Position

### Target Customers

Allure Systems sold to fashion brands and apparel retailers that operated eCommerce storefronts and faced the recurring cost and logistical burden of model photography. The company's YC profile describes its customers as "leading fashion retailers and luxury industry leaders."<sup><a href="https://www.ycombinator.com/companies/allure-systems">[29]</a></sup> No specific named clients appear in any public source — a notable gap in the public record, likely the result of enterprise NDAs standard in luxury retail.

The customer profile that emerges from available evidence skews toward mid-to-large retailers with high SKU counts, where the cost savings from eliminating per-garment photography are most significant. The NRF 2019 appearance — the National Retail Federation's annual trade show, attended primarily by enterprise retail buyers — confirms that Allure Systems was pursuing large accounts through a direct enterprise sales motion rather than a self-serve or SMB model. French press coverage from January 2019 noted that the company had already signed two major US retailers at the time of NRF, suggesting meaningful enterprise traction before the YC Demo Day.

The luxury segment was a particular focus. Investors included La Maison des Startups, the LVMH Group's startup accelerator, which provided direct access to some of the world's most prominent luxury fashion houses.<sup><a href="https://www.cbinsights.com/company/allure-systems">[30]</a></sup> Whether this relationship translated into commercial contracts with LVMH brands prior to the Farfetch acquisition is not documented in available sources.

### Market Size

Allure Systems framed its addressable market around the $8 billion that fashion brands collectively spend annually on models and photographers — a figure cited at YC Demo Day and in TechCrunch's coverage of the pitch.<sup><a href="https://techcrunch.com/2019/03/19/here-are-the-88-companies-that-launched-at-ycs-w19-demo-day-2/">[31]</a></sup> This framing positioned the product as a direct cost replacement for existing photography spend, making the ROI calculation straightforward for enterprise buyers.

The broader eCommerce fashion photography market extends beyond direct photography costs to include image management, catalog production, and the downstream cost of returns driven by poor product representation. Chou's NRF 2019 quote — "67% of returns are due to sizing errors" — pointed to a second, larger market: the estimated $550 billion in annual eCommerce returns globally, a significant portion of which is attributable to fit and appearance mismatches that better imagery could reduce.

The size inclusivity angle opened an additional market dimension. Brands that could show garments on a full range of body types without incremental photography cost could reach the 67% of American women who wear size 12 or above — a segment that was systematically underrepresented in online catalogs and therefore underserved as a commercial audience.<sup><a href="https://blog.ycombinator.com/17-companies-from-the-yc-w19-batch-part-4/">[32]</a></sup>

### Competition

In 2019, the competitive landscape for AI-generated fashion imagery was nascent. The primary competition was not other AI startups but the incumbent workflow: traditional photography studios, model agencies, and the internal creative teams that managed them. The switching cost was behavioral and organizational as much as financial — brands had established vendor relationships, internal processes, and quality standards built around traditional photography.

Within the AI fashion imagery space, companies including Syte, Vue.ai, and various computer vision startups were attacking adjacent problems (visual search, product tagging, recommendation) but not the specific on-figure image generation problem that Allure Systems targeted. The closest direct competitors were virtual try-on platforms, but these were primarily consumer-facing (showing shoppers how a garment would look on them) rather than B2B catalog production tools.

The competitive dynamic shifted significantly after 2022, when diffusion-based generative AI models (Stable Diffusion, Midjourney, DALL-E) made high-quality AI image generation broadly accessible. By 2023, dozens of startups were offering AI fashion photography tools. Allure Systems' 2021 acquisition by Farfetch positioned it ahead of this wave — the company was acquired before the market became crowded, and its proprietary training data, hardware integration, and luxury industry relationships represented moats that would have been harder to maintain in the post-2022 environment.

## Business Model

Allure Systems operated as a B2B SaaS and services company selling to fashion brands and retailers. The specific pricing structure — whether per-image, per-SKU, subscription, or enterprise license — is not documented in any available public source. The company's $1.4M ARR at YC Demo Day in March 2019, combined with a team of 17–23 employees at the time of the December 2021 acquisition, is consistent with a mid-market enterprise SaaS model with relatively few large accounts rather than a high-volume, low-ACV self-serve product.<sup><a href="https://www.ycombinator.com/companies/allure-systems">[33]</a></sup>

The value proposition to buyers was framed as cost replacement: brands were already spending on photography, and Allure Systems offered to deliver equivalent or superior output at lower cost and higher speed, with the added benefit of size-inclusive imagery that traditional shoots could not produce at scale. The 14% conversion rate lift cited at Demo Day provided a revenue-side ROI argument to complement the cost-reduction case.<sup><a href="https://techcrunch.com/2019/03/19/here-are-the-88-companies-that-launched-at-ycs-w19-demo-day-2/">[34]</a></sup>

The dual US-France structure also suggests a potential geographic revenue split, with the French subsidiary potentially serving European luxury clients while the US entity handled American retail accounts.

## Traction

At YC W19 Demo Day in March 2019, Allure Systems reported $1.4M in ARR — a meaningful baseline for a two-year-old AI company that had not yet completed its accelerator program.<sup><a href="https://techcrunch.com/2019/03/19/here-are-the-88-companies-that-launched-at-ycs-w19-demo-day-2/">[35]</a></sup> The company also cited a 14% conversion rate lift for retail clients using its imagery, a commercially specific metric that signals the team was measuring and communicating outcomes in the language enterprise buyers care about.<sup><a href="https://techcrunch.com/2019/03/19/here-are-the-88-companies-that-launched-at-ycs-w19-demo-day-2/">[36]</a></sup>

Getlatka, which sources revenue data from founder interviews, reports approximately $3M in revenue for Allure Systems — suggesting meaningful growth between the March 2019 Demo Day and the December 2021 acquisition, though this figure carries low confidence and is unverified by any secondary source.<sup><a href="https://getlatka.com/companies/allure-systems">[37]</a></sup> If accurate, it implies a roughly 2x revenue increase over approximately 2.5 years, consistent with a company growing steadily through enterprise sales rather than scaling rapidly.

CBInsights notes that Allure Systems' technology "was adopted by luxury industry leaders," culminating in the Farfetch acquisition.<sup><a href="https://www.cbinsights.com/company/allure-systems">[38]</a></sup> No specific named clients appear in any public source. The NRF 2019 appearance produced at least two signed US retail contracts per French press coverage, and the company's investor base — which included La Maison des Startups (the LVMH accelerator) — suggests relationships with major luxury houses, though commercial terms are undocumented.

At acquisition, the company employed 17–23 people, with a Paris-based tech team of 10 developers and computer vision engineers who continued operating post-acquisition in collaboration with Farfetch's R&D team in Portugal.<sup><a href="https://www.linkedin.com/company/allure-systems">[39]</a></sup> This team retention is a strong signal that Farfetch valued the human capital alongside the technology.

## Post-Mortem

Allure Systems did not fail. It was acquired by Farfetch on December 20, 2021, in a cash transaction that validated its technology, retained its team, and provided a positive exit for founders and investors.<sup><a href="https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/">[40]</a></sup> What follows is not a failure analysis but an acquisition analysis — an examination of what worked, what the acquisition revealed about the company's strategic position, and what the subsequent fate of its acquirer means for the technology's legacy.

### What Drove the Acquisition

Farfetch acquired Allure Systems as part of a stated strategy to "accelerate the digitization of the global luxury industry."<sup><a href="https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/">[41]</a></sup> The specific rationale disclosed in Farfetch's SEC 20-F filing was to "provide an enhanced customer experience on Farfetch Marketplace and drive efficiency in our operational processes." In practical terms, Farfetch was acquiring the ability to generate high-quality on-model imagery at scale for the thousands of luxury brands listed on its marketplace — eliminating the photography bottleneck that slowed catalog updates and limited size representation.

The technology fit was precise. Farfetch's marketplace model depends on brands uploading product imagery, and the quality and consistency of that imagery directly affects conversion. Allure Systems' platform could standardize and accelerate that process across Farfetch's entire brand portfolio, while the 360-degree rendering capability described in the SEC filing pointed toward richer, more interactive product experiences.<sup><a href="https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/">[42]</a></sup>

The timing also mattered. The acquisition closed in December 2021, before the generative AI wave of 2022–2023 made AI image generation a commodity. Farfetch was acquiring proprietary technology, trained models, and a specialized team at a moment when those assets were genuinely scarce.

### Capital Efficiency as a Strategic Asset

Allure Systems raised approximately $3.57M–$3.85M in total across its operating life — a lean capital structure for a company combining hardware, AI research, and enterprise sales.<sup><a href="https://pitchbook.com/profiles/company/226549-72">[43]</a></sup> This capital efficiency appears to have been a deliberate choice rather than a fundraising constraint. Gabrielle Chou's background as a serial entrepreneur with two prior exits suggests she understood how to build toward an acquisition rather than toward a venture-scale outcome requiring a Series A and beyond.

The investor mix reinforced this orientation. YC provided credibility and network access. CapHorn Invest and Calao Finance provided French VC backing aligned with the Paris R&D operation. La Maison des Startups provided direct access to LVMH's brand portfolio. Mark Cuban provided US investor validation and likely introductions to American retail buyers.<sup><a href="https://markcubancompanies.com/companies/allure-systems/">[44]</a></sup> Plug and Play provided global accelerator network access. This was a deliberately assembled coalition of strategic investors, not a pure financial return-seeking syndicate.

### The Dual US-France Structure as a Competitive Advantage

The decision to operate with a US commercial entity and a French R&D subsidiary proved strategically valuable in multiple ways. The Paris team gave Allure Systems access to European computer vision talent and proximity to the French luxury industry — the home market of LVMH, Kering, and the brands that dominate Farfetch's marketplace. The Brooklyn headquarters positioned the company for American enterprise sales and YC participation.

Post-acquisition, Farfetch retained the Paris tech team of 10 developers and computer vision engineers, integrating them with Farfetch's own R&D team in Portugal.<sup><a href="https://www.linkedin.com/company/allure-systems">[45]</a></sup> This retention confirms that the French R&D operation was a core asset of the acquisition, not a liability to be wound down. The dual-geography structure that might have appeared as operational complexity during the startup phase became a feature at exit.

### The Unresolved Question: What Happened After Farfetch?

The most significant open question in Allure Systems' story is not about the company itself but about its acquirer. Farfetch, which had been valued at over $20 billion at its peak, entered financial distress in late 2023 and was acquired by South Korean eCommerce giant Coupang in January 2024 in a rescue deal that wiped out most of Farfetch's equity holders.

The fate of Allure Systems' technology, team, and intellectual property within this sequence of events is entirely undocumented in available sources. The Paris R&D team that Farfetch retained in December 2021 may have been retained by Coupang, laid off in restructuring, or dispersed. The 360-degree rendering technology that Farfetch described as central to its marketplace strategy may have been integrated, shelved, or sold. None of this is knowable from public sources.

This creates an unusual epilogue: a successful acquisition outcome for Allure Systems' founders and investors, followed by the collapse of the acquirer, followed by a second acquisition that may or may not have preserved the technology's intended purpose. The Allure Systems story ends cleanly for its founders. What happened to what they built is a different, unresolved question.

### The Founder's Clean Exit

Gabrielle Chou's transition to academia following the acquisition is a notable data point. She became an Associate Professor of Practice at NYU Shanghai in 2021, teaching AI-driven business models — a role that directly applies the experience she accumulated building and selling Allure Systems.<sup><a href="https://shanghai.nyu.edu/academics/faculty/directory/gabrielle-chou">[46]</a></sup> This is a clean, deliberate exit: a founder who built a company, sold it, and moved to the next chapter rather than staying on in an operational role at the acquirer.

Jeremy Chamoux's post-acquisition activities are not documented in available sources.

## Key Lessons

- **A focused vertical AI product can achieve acquisition without venture scale.** Allure Systems raised approximately $3.7M, employed fewer than 25 people, and reached an estimated $1.4M–$3M in ARR before being acquired by a NASDAQ-listed company.<sup><a href="https://pitchbook.com/profiles/company/226549-72">[47]</a></sup> The company never raised a Series A. This outcome is only possible when the product solves a specific, measurable problem for a well-defined buyer — in this case, the photography cost and size representation gap for luxury eCommerce retailers. Founders building B2B AI tools in defined verticals should consider whether an acquisition-oriented capital strategy (smaller raise, strategic investors, enterprise traction) is more appropriate than a venture-scale growth strategy.

- **Mission alignment and commercial metrics are not mutually exclusive.** Allure Systems' size inclusivity framing — 67% of Americans wear size 12+, yet 90% of catalogs don't represent them — was simultaneously a social equity argument and a conversion rate argument.<sup><a href="https://blog.ycombinator.com/17-companies-from-the-yc-w19-batch-part-4/">[48]</a></sup> The 14% conversion rate lift cited at Demo Day gave enterprise buyers a financial justification for a decision that also happened to be the right thing to do. Founders who can find the intersection of mission and metrics — where doing good and driving revenue point in the same direction — have a more durable sales narrative than those relying on either argument alone.

- **Strategic investor composition can substitute for revenue scale in acquisition outcomes.** Allure Systems' investor base included La Maison des Startups (the LVMH accelerator), which provided direct access to the luxury brands that Farfetch serves.<sup><a href="https://www.cbinsights.com/company/allure-systems">[49]</a></sup> This relationship likely accelerated Farfetch's awareness of and confidence in the technology. Founders building B2B products for specific industries should treat accelerator and corporate venture programs in their target vertical as strategic assets, not just capital sources — the introductions and credibility they provide can be worth more than the check.

- **Acquirer stability is a risk that founders cannot fully control.** Allure Systems achieved a successful cash exit in December 2021. Farfetch, the acquirer, collapsed into financial distress within two years and was acquired by Coupang in early 2024. The technology and team that Allure Systems built may or may not have survived that transition intact. This is not a failure of Allure Systems' strategy — the founders and investors received their exit. But it illustrates that the post-acquisition fate of a startup's technology is often determined by forces entirely outside the founding team's control, and that acquisition price and structure matter as much as the identity of the acquirer.

- **Timing a vertical AI acquisition before a technology wave is a durable exit strategy.** Allure Systems was acquired in December 2021, before diffusion-based generative AI models made AI fashion photography broadly accessible in 2022–2023. By the time Stable Diffusion and its successors arrived, Allure Systems' technology, training data, and team were already inside Farfetch. Founders building proprietary AI products in specific verticals should monitor the generative AI landscape closely — the window between "proprietary advantage" and "commodity capability" is compressing, and the optimal acquisition timing may be earlier than traditional venture timelines suggest.

## Sources

1. [Gabrielle Chou Faculty Profile — NYU Shanghai](https://shanghai.nyu.edu/academics/faculty/directory/gabrielle-chou)
2. [17 Companies from the YC W19 Batch, Part 4 — Y Combinator Blog](https://blog.ycombinator.com/17-companies-from-the-yc-w19-batch-part-4/)
3. [Allure Systems — Y Combinator Company Profile](https://www.ycombinator.com/companies/allure-systems)
4. [Allure Systems — Crunchbase](https://www.crunchbase.com/organization/allure-systems)
5. [Allure Systems — CBInsights](https://www.cbinsights.com/company/allure-systems)
6. [Farfetch Sheds Light on M&A, AI Tech, Resale Ambitions in New SEC Filing — The Fashion Law](https://www.thefashionlaw.com/farfetch-sheds-light-on-ma-ai-tech-resale-ambitions-in-new-sec-filing/)
7. [Gabrielle Chou Personal Website — About Page](https://www.gabriellechou.net/about)
8. [Allure AR Fashion — AppAdvice App Listing](https://appadvice.com/app/allure-ar-fashion/1386760359)
9. [Allure Systems — CBInsights Financials](https://www.cbinsights.com/company/allure-systems/financials)
10. [Mark Cuban Companies — Allure Systems Portfolio Page](https://markcubancompanies.com/companies/allure-systems/)
11. [Farfetch 20-F SEC Filing, Fiscal Year Ending December 31, 2021](https://www.sec.gov/Archives/edgar/data/1740915/000156459022008640/ftch-20f_20211231.htm)
12. [Here Are the 88 Companies That Launched at YC's W19 Demo Day 2 — TechCrunch](https://techcrunch.com/2019/03/19/here-are-the-88-companies-that-launched-at-ycs-w19-demo-day-2/)
13. [Allure Systems — PitchBook](https://pitchbook.com/profiles/company/226549-72)
14. [Allure Systems — Getlatka](https://getlatka.com/companies/allure-systems)
15. [Allure Systems — LinkedIn Company Page](https://www.linkedin.com/company/allure-systems)
16. [Allure Systems — Crunchbase Financials](https://www.crunchbase.com/organization/allure-systems/company_financials)
17. [Allure Systems crée des mannequins virtuels pour les sites e-commerce — EcommerceMag.fr](https://www.ecommercemag.fr/Thematique/management-1225/Breves/Allure-Systems-cree-mannequins-virtuels-sites-commerce-326390.htm)
18. [NRF 2019: Allure Systems propose la personnalisation des tailles avec des mannequins virtuels — EcommerceMag.fr](https://www.ecommercemag.fr/Thematique/retail-1220/Breves/nRF2019-Allure-Systems-propose-personnalisation-tailles-mannequins-virtuels-336461.htm)
19. [Allure Systems — YCDB](https://www.ycdb.co/company/allure-systems)
20. [Wayback Machine — alluresystems.com Archive](https://web.archive.org/web/20210101000000*/alluresystems.com)
