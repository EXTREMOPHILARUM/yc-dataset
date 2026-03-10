# Research Report: Lyrebird

## Overview

Lyrebird was a Montreal-based AI startup that built voice-cloning technology capable of replicating any person's voice from just one minute of audio.Founded in 2017 by three PhD students at MILA—one of the world's leading deep learning labs—the company commercialized its own academic research and generated enormous public attention with a viral launch demo.

Despite genuine technical achievement and early investor interest from top-tier firms, Lyrebird raised only $120K in total disclosed funding, never publicly launched the developer API that was its intended revenue engine, and was acquired by Descript in September 2019 for an undisclosed sum.The core thesis of failure: Lyrebird built a real technology with no product context to deploy it in.

Voice cloning as a standalone API had no clear killer use case in 2017–2019; voice cloning embedded inside a content creation workflow did.Descript provided that context, the capital to execute, and the distribution to reach paying users—none of which Lyrebird could assemble independently.

<report-gallery>
<media-image src="https://thepnr.com/wp-content/uploads/2021/11/Alexandre-Pic.jpg" alt="Alexandre de Brébisson, co-founder and CEO of Lyrebird" caption="Alexandre de Brébisson, the MILA PhD student who co-founded Lyrebird and watched its viral demo reach a million plays in a single day — before the hard work of finding a business model began."></media-image>
<media-image src="https://bookface-images.s3.amazonaws.com/avatars/70e7deda48fa1e0f98caba88e71035681f3bcd0e.jpg" alt="Lyrebird on Y Combinator" caption="Lyrebird's Y Combinator profile, circa Summer 2017 — the $120K seed check from YC would prove to be the only disclosed funding the company ever raised before its acquisition by Descript two years later."></media-image>
</report-gallery>

## Founding Story

Lyrebird emerged directly from the research labs of MILA, the Montreal Institute for Learning Algorithms, one of the world's premier deep learning research centers. The three co-founders—Alexandre de Brébisson, Kundan Kumar, and Jose Sotelo—were PhD students in artificial intelligence at the University of Montreal, working under the supervision of Yoshua Bengio, Pascal Vincent, and Aaron Courville, three of the most influential figures in modern deep learning.<sup><a href="https://www.edn.com/lyrebird-ai-is-a-new-site-that-will-allow-anyone-to-accurately-duplicate-someone-elses-voice/">[1]</a></sup> <sup><a href="https://www.ycombinator.com/companies/lyrebird">[2]</a></sup>

The founding team did not set out to build a startup in the conventional sense. Their voice synthesis research was academic in origin—part of the broader wave of neural network breakthroughs happening at MILA in the mid-2010s that would eventually reshape the field of speech synthesis. The decision to commercialize came from recognizing that the technology had crossed a threshold: one minute of audio was now sufficient to generate a convincing digital replica of a human voice, with emotional modulation and near-real-time generation speed.<sup><a href="https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/">[3]</a></sup>

The team bootstrapped development, continuing to work within the MILA lab infrastructure, and made a deliberate choice to ship a public demo before seeking external capital.<sup><a href="https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/">[4]</a></sup> This sequencing—demonstrate first, raise second—reflected both scrappiness and a research-lab orientation: prove the technology works, then figure out the business. Alexandre de Brébisson served as CEO, with Kundan Kumar and Jose Sotelo rounding out the technical founding team.<sup><a href="https://www.ycombinator.com/companies/lyrebird">[5]</a></sup>

The team was accepted into Y Combinator's Summer 2017 batch, receiving the standard $120K seed check.<sup><a href="https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg">[6]</a></sup> YC provided validation and a network, but the funding was thin for a company attempting to build and maintain a real-time voice synthesis API platform at commercial scale.

The founders described themselves in their YC launch post as "co-founders of Lyrebird and PhD students in AI at University of Montreal" building "speech synthesis technologies to improve the way we communicate with computers."<sup><a href="https://news.ycombinator.com/item?id=15185089">[7]</a></sup> The framing was deliberately broad—a platform vision rather than a specific product. That breadth would prove both a strength and a liability.

De Brébisson articulated the long-term vision with a prescient analogy: "The situation is comparable to Photoshop. People are now aware that photos can be faked. I think in the future, audio recordings are going to become less and less reliable [as evidence]."<sup><a href="https://www.edn.com/lyrebird-ai-is-a-new-site-that-will-allow-anyone-to-accurately-duplicate-someone-elses-voice/">[8]</a></sup> He was right about the trajectory. Being right about the future, however, did not solve the near-term problem of building a sustainable business in 2017.

---

## Timeline

- **January 2017** — Lyrebird incorporated in Montreal; founders accepted into Y Combinator S17 batch; raise $120K seed round from YC.<sup>[[9]](https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg)</sup>

- **April 25, 2017** — Lyrebird launches viral public demo using synthesized voices of Donald Trump, Barack Obama, and Hillary Clinton; receives 100,000 website visits and 1 million audio sample plays in a single day.<sup>[[10]](https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/)</sup>

- **April 27, 2017** — TechCrunch publishes "Lyrebird is a voice mimic for the fake news era"; founders publicly address ethical concerns and announce planned freemium API monetization model.<sup>[[11]](https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/)</sup>

- **May 24, 2017** — Lyrebird publicly articulates its ethical rationale for open release of the technology, arguing that transparency allows society to adapt rather than be blindsided by secret development.<sup>[[12]](https://singularityhub.com/2017/05/24/new-ai-mimics-any-voice-in-a-matter-of-minutes/)</sup>

- **September 8, 2017** — Lyrebird launches beta version of voice-cloning software on Hacker News (YC S17 launch post), allowing users to record one minute of audio to generate a personal voice model.<sup>[[13]](https://news.ycombinator.com/item?id=15185089)</sup>

<media-hn url="https://news.ycombinator.com/item?id=15185089" title="Launch HN: Lyrebird (YC S17) – Create a digital copy of your voice" points="" comments=""></media-hn>

- **April 2018** — Developer API remains unreleased—more than one year after the viral launch and seven months after the beta. The planned revenue engine has not shipped.<sup>[[14]](https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg)</sup>

- **September 18, 2019** — Descript acquires Lyrebird for an undisclosed price, simultaneously announcing a $15M Series A led by Andreessen Horowitz and Redpoint. Lyrebird becomes Descript's Montreal AI research division.<sup>[[15]](https://techcrunch.com/2019/09/18/descript-audio/)</sup>

- **September 18, 2019** — Lyrebird technology deployed as Descript's "Overdub" feature, enabling users to type text and generate audio in their own voice—the first concrete consumer application of the core technology.<sup>[[16]](https://voicebot.ai/2019/09/18/descript-acquires-lyrebird-and-lands-15-million-in-funding-from-andreessen-horowitz-and-redpoint/)</sup>

---

## What They Built

Lyrebird's core product was a voice-cloning system that could replicate a person's voice from as little as one minute of recorded audio. The underlying technology was a neural network trained to extract the acoustic characteristics of a speaker—pitch, cadence, timbre, and emotional inflection—and then synthesize new speech in that voice from arbitrary text input.<sup><a href="https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/">[17]</a></sup>

The performance benchmarks were remarkable for 2017. The system could generate 1,000 sentences in under half a second and could modulate the emotional tone of synthesized speech—producing the same sentence in a neutral, happy, or emphatic register.<sup><a href="https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg">[18]</a></sup> For context, competing text-to-speech systems at the time either required hours of recorded audio to produce a passable voice model or produced robotic-sounding output that was clearly synthetic. Lyrebird's one-minute threshold was a genuine technical leap.

<media-youtube id="ohmajJTcpNk" title="Original Lyrebird AI demo video — voice cloning technology in action, April 2017"></media-youtube>

The user experience in the September 2017 beta was straightforward: a user visited the Lyrebird website, recorded approximately one minute of audio by reading a provided script, and received a digital voice model. That model could then be used to synthesize new speech from text input. The entire enrollment process was designed to be self-service, with no human review required.<sup><a href="https://news.ycombinator.com/item?id=15185089">[19]</a></sup>

<media-hn url="https://news.ycombinator.com/item?id=14182262" title="Lyrebird – An API to copy the voice of anyone" points="" comments=""></media-hn>

The planned commercial product was a developer API. Third-party developers and companies would integrate Lyrebird's voice synthesis capabilities into their own applications—audiobook production, virtual assistants, accessibility tools, gaming, and content creation were the obvious use cases. The monetization model was pay-per-audio-sample: a freemium tier for low-volume usage and paid tiers for commercial-scale generation.<sup><a href="https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/">[20]</a></sup>

What distinguished Lyrebird from existing text-to-speech products was the combination of three factors: the brevity of the enrollment audio required, the naturalness of the output, and the emotional modulation capability. Google's WaveNet, published in 2016, had demonstrated that neural networks could produce highly natural speech, but WaveNet required substantial compute and was not yet a commercial product. Lyrebird's system was designed from the outset for API delivery at scale.

<media-image src="https://web.archive.org/web/20170929141709im_/https://lyrebird.ai/" alt="Archived Lyrebird.ai homepage from September 29, 2017" caption="Wayback Machine snapshot of the Lyrebird.ai homepage captured on September 29, 2017 — just weeks after the YC S17 beta launch. This is the product landing page as it appeared during the company's active period."></media-image>

The technology evolved after the acquisition. When Descript deployed it as the "Overdub" feature, the product added a critical consent-based constraint: the system would only clone a user's own voice, with safeguards preventing the use of pre-existing recordings of other people.<sup><a href="https://voicebot.ai/2019/09/18/descript-acquires-lyrebird-and-lands-15-million-in-funding-from-andreessen-horowitz-and-redpoint/">[21]</a></sup> This design choice addressed the most obvious misuse vector and made the technology commercially deployable to a mainstream audience.

<media-youtube id="VjE0Kdfos4Y" title="Lyrebird AI product walkthrough — demo video from around the time of the Descript acquisition, 2019"></media-youtube>

---

## Market Position

### Target Customers

Lyrebird's stated target was developers and companies who would build voice-enabled applications on top of its API. The envisioned customer segments included content creators producing audiobooks or podcasts, game developers needing dynamic voice generation, accessibility technology companies building tools for people with speech impairments, and enterprise software companies integrating voice interfaces into their products.

The beta product, however, was aimed at individual users—anyone who wanted a digital copy of their own voice. This created a gap between the consumer-facing beta and the developer-facing commercial product that was never publicly bridged. There is no documented evidence of enterprise sales conversations, signed customers, or a formal go-to-market motion targeting any specific vertical.

### Market Size

The voice synthesis market in 2017 was nascent and poorly defined. There were no established buyer categories for voice cloning specifically, no standard procurement processes, and no adjacent successful products proving willingness to pay for personalized voice generation at scale. The broader text-to-speech market existed—dominated by Nuance, Amazon Polly, and Google Cloud Text-to-Speech—but those products served a different use case: generic synthetic voices for IVR systems and accessibility applications, not personalized voice cloning.

The total addressable market for voice cloning as a standalone API product in 2017 was effectively zero in a commercial sense: there were no established buyers, no budget line items, and no procurement workflows. The market that would eventually emerge—AI voice generation for content creation, dubbing, gaming, and accessibility—was 3–5 years away from having the scale and buyer sophistication to support an independent API platform.

### Competition

The competitive landscape in 2017 was sparse but technically credible. Google's WaveNet (2016) had demonstrated state-of-the-art neural speech synthesis but was not yet a commercial product. Baidu's Deep Voice research (2017) was similarly academic. No direct commercial competitor was offering personalized voice cloning via API at the time of Lyrebird's launch, which was both an opportunity and a warning sign: the absence of competition often reflects the absence of a paying market, not just a technical gap.

By 2019, the competitive environment had shifted. Resemble AI, Replica Studios, and other voice synthesis startups had entered the market. More importantly, the major cloud providers—Amazon, Google, and Microsoft—were all investing heavily in neural text-to-speech, giving them the distribution and infrastructure advantages that a nine-person startup with $120K in funding could not match.<sup><a href="https://pitchbook.com/profiles/company/180241-48">[22]</a></sup> Lyrebird's window as a technically differentiated independent player was closing precisely as its API remained unshipped.

---

## Business Model

Lyrebird planned to monetize through a freemium developer API with pay-per-audio-sample pricing.<sup><a href="https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/">[23]</a></sup> Developers would integrate the API into their applications, paying for each audio generation request above a free-tier threshold. This model mirrors the pricing structures used by Twilio for communications APIs and AWS for cloud services—a usage-based infrastructure play targeting developers as the primary buyer.

The model was conceptually sound for a B2B infrastructure business. Usage-based pricing aligns cost with value, scales naturally with customer growth, and creates predictable revenue as API call volume increases. The challenge was execution: building a reliable, low-latency API capable of handling commercial-scale traffic requires significant engineering investment in infrastructure, reliability, and developer tooling—none of which $120K can fund.

There is no documented evidence that Lyrebird ever generated revenue. The API was still unreleased as of April 2018, more than a year after the viral launch.<sup><a href="https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg">[24]</a></sup> The company appears to have operated entirely on its seed capital from YC until the acquisition.

---2f:T5d8,

## Traction

## Post-Mortem

### Primary Cause: The API Never Shipped

The most concrete and consequential failure was operational: Lyrebird announced a developer API as its commercial product in April 2017 and had not publicly launched it by April 2018—a full year later, and seven months after the beta.<sup><a href="https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg">[29]</a></sup> For a company whose entire business model depended on API revenue, this delay was fatal.

The specific reasons for the delay are not documented. Three plausible explanations exist, and they are not mutually exclusive. First, the engineering challenge of converting a research-grade model into a production-grade API—with the latency, reliability, and scalability required for commercial use—may have been substantially harder than the team anticipated. Research models are optimized for accuracy; production APIs are optimized for speed, uptime, and cost efficiency. These are different engineering problems. Second, the ethical and legal exposure created by the technology may have introduced caution about what safeguards needed to be in place before opening the API to arbitrary third-party developers. Third, the team may simply have lacked the engineering headcount to execute both model improvement and infrastructure buildout simultaneously with nine employees and $120K in capital.

The attempted remedy was the September 2017 beta—a consumer-facing product that let individuals clone their own voice. This was a reasonable pivot to generate user data and demonstrate demand, but it was not the developer API that would generate revenue. The beta appears to have been a holding pattern rather than a commercial product. No evidence exists that the beta converted to a paid product or that it generated the developer pipeline needed to justify a follow-on raise.

### Secondary Cause: Critical Undercapitalization

Lyrebird raised $120K in total disclosed funding—the standard YC check at the time.<sup><a href="https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg">[30]</a></sup> Andreessen Horowitz, Redpoint Ventures, and SV Angel are listed as investors in PitchBook data,<sup><a href="https://pitchbook.com/profiles/company/180241-48">[31]</a></sup> but there is no evidence of a follow-on seed round or Series A at any point in Lyrebird's independent life. The same firms—a16z and Redpoint—led Descript's $15M Series A at the time of the acquisition,<sup><a href="https://techcrunch.com/2019/09/18/descript-audio/">[32]</a></sup> suggesting they had conviction in the technology but not in Lyrebird's ability to commercialize it independently.

The capital constraint was structural. Building a commercial API platform requires: engineering infrastructure for reliability and scale, developer relations to build a community and documentation, sales and marketing to convert developer interest into paying accounts, and ongoing model improvement to stay ahead of well-capitalized competitors. None of these functions can be staffed or executed on $120K. The company appears to have operated for approximately 2.5 years on its seed capital, which implies either extremely low burn (consistent with a small team in Montreal) or a runway that ran out well before the acquisition.

The failure to raise a follow-on round is itself informative. De Brébisson noted investor interest immediately after the April 2017 launch. If top-tier firms expressed interest but did not write checks, the most likely explanation is that the diligence process surfaced concerns about the go-to-market plan, the API delay, or the ethical/legal exposure of the technology—none of which the team had resolved by the time follow-on conversations would have occurred (mid-to-late 2017).

### Tertiary Cause: Viral Launch Attracted the Wrong Attention

The April 2017 demo was a deliberate viral strategy that succeeded on its own terms: 100,000 website visits and 1 million audio plays in a single day.<sup><a href="https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/">[33]</a></sup> But the choice to demonstrate the technology using synthesized voices of sitting political figures—Trump, Obama, and Clinton—framed the product as a misinformation tool before the team could frame it as a developer platform.

TechCrunch's headline—"Lyrebird is a voice mimic for the fake news era"—set the dominant media narrative.<sup><a href="https://nextnature.org/en/magazine/story/2017/lyrebird-api-copies-human-voice">[34]</a></sup> The Inquirer called it a "sinister startup." This framing was not neutral background noise. Enterprise buyers in financial services, media, and legal sectors—the segments most likely to pay for voice synthesis at scale—are acutely sensitive to reputational risk. A product that had been publicly labeled a fake news tool in its first week of existence faced a materially harder enterprise sales conversation than a product that had not.

The founders' response was principled: they argued for open release so society could adapt, and they engaged publicly with the ethical debate.<sup><a href="https://singularityhub.com/2017/05/24/new-ai-mimics-any-voice-in-a-matter-of-minutes/">[35]</a></sup> This was philosophically coherent and arguably correct as a long-term policy position. It did not, however, change the media record or make enterprise sales easier in 2017–2019. The Photoshop analogy de Brébisson offered—that society would eventually normalize synthetic audio the way it normalized photo editing—was accurate about the 10-year trajectory but unhelpful for closing deals in year one.<sup><a href="https://www.edn.com/lyrebird-ai-is-a-new-site-that-will-allow-anyone-to-accurately-duplicate-someone-elses-voice/">[36]</a></sup>

### Structural Cause: No Product Context for the Technology

The deepest failure was not operational or financial but strategic: Lyrebird built a technology without a product context that made its value obvious to a paying customer. Voice cloning as a standalone API in 2017 answered the question "can this be done?" but not "what specific problem does this solve for whom, and why will they pay for it today?"

The contrast with Descript's deployment is instructive. When Lyrebird's technology became Overdub inside Descript, the use case was immediately legible: a podcaster or video creator who misspoke a word could fix it by typing the correction, and the system would generate audio in their voice to replace the error. The value proposition was concrete, the workflow was familiar, and the willingness to pay was established by Descript's existing subscription base. None of those conditions existed for a standalone voice-cloning API in 2017.

Lyrebird's one patent filing<sup><a href="https://www.cbinsights.com/company/lyrebird">[37]</a></sup> further suggests the team did not invest heavily in building defensive IP around the core algorithm—a significant oversight for a company whose entire value was its proprietary model. As larger players developed competing capabilities, Lyrebird's technical moat narrowed without a product moat to compensate.

Kundan Kumar's post-acquisition summary captures the outcome without editorializing: "I started lyrebird.ai which pioneered voice cloning technology. Lyrebird.ai was sold to Descript, where I led AI for 5 years and shipped a bunch of AI features."<sup><a href="https://www.ycombinator.com/companies/lyrebird">[38]</a></sup> The technology found its context. The independent company did not.

---

## Key Lessons

- **Viral attention and commercial traction are different metrics, and confusing them is expensive.** Lyrebird's 100,000 launch-day visits and 1 million audio plays generated genuine investor interest and media coverage, but neither converted into the developer pipeline or enterprise relationships needed to justify a follow-on raise. A launch that generates press headlines but no paying customers or signed letters of intent provides weak evidence for product-market fit. The team should have treated the viral moment as a lead-generation event and measured success by how many developers signed up for API waitlists and converted to paid accounts—not by website traffic.

- **Horizontal API platforms require 10–50x more capital than a research-to-startup transition typically raises.** The freemium API model was the right instinct for a B2B infrastructure play, but executing it requires engineering infrastructure, developer relations, documentation, and sales capacity that cannot be staffed on $120K. Companies like Twilio and Stripe—the canonical API platform successes—raised $8.5M and $2M respectively in their first institutional rounds, and still took years to reach profitability. Lyrebird's capital structure was incompatible with its business model from the outset.

- **Ethical framing of a technology shapes its commercial trajectory, sometimes irreversibly.** The decision to launch with synthesized political voices was effective at generating attention but established a media narrative—fake news tool, sinister startup—that complicated enterprise sales for the company's entire independent life. The founders' principled response (open release, consent-based safeguards) was correct as policy but did not undo the first-impression framing. For technologies with obvious misuse potential, the launch strategy should be designed to establish the legitimate use case first, not the most dramatic demonstration of capability.

- **Technology without product context is an acquisition target, not a standalone business.** Lyrebird's technology was real and valuable—Descript's subsequent success with Overdub confirms this. But the technology needed a specific workflow, a defined user, and an established willingness to pay to become a product. Lyrebird never found that context independently. The lesson is not that the founders should have built a different technology, but that they should have identified a specific vertical application—audiobooks, accessibility, gaming—and built the product around that use case rather than waiting for developers to discover one through an API.

- **Academic pedigree accelerates technology development but does not substitute for commercial execution experience.** The MILA founding team had elite research credentials and genuine technical depth, but no documented prior experience building commercial products, managing developer communities, or executing enterprise sales. These are learnable skills, but they take time to develop—time that a company with $120K in runway and a closing competitive window does not have. Earlier recruitment of a commercially experienced operator or go-to-market lead might have accelerated the API launch and the follow-on fundraise.

---

## Sources

1. [EDN — "Lyrebird AI is a new site that will allow anyone to accurately duplicate someone else's voice" (April 27, 2017)](https://www.edn.com/lyrebird-ai-is-a-new-site-that-will-allow-anyone-to-accurately-duplicate-someone-elses-voice/)
2. [Y Combinator — Lyrebird company profile](https://www.ycombinator.com/companies/lyrebird)
3. [TechCrunch — "Lyrebird is a voice mimic for the fake news era" (April 25, 2017)](https://techcrunch.com/2017/04/25/lyrebird-is-a-voice-mimic-for-the-fake-news-era/)
4. [Tracxn — Lyrebird company profile](https://tracxn.com/d/companies/lyrebird/__ES5LYpHUoBobAxEBo1ta2jcXed-kpCamR207JkQzDBg)
5. [Hacker News — "Launch HN: Lyrebird (YC S17) – Create a digital copy of your voice" (September 8, 2017)](https://news.ycombinator.com/item?id=15185089)
6. [Hacker News — "Lyrebird – An API to copy the voice of anyone" (April 2017)](https://news.ycombinator.com/item?id=14182262)
7. [Singularity Hub — "New AI Mimics Any Voice in a Matter of Minutes" (May 24, 2017)](https://singularityhub.com/2017/05/24/new-ai-mimics-any-voice-in-a-matter-of-minutes/)
8. [TechCrunch — "Descript raises $15M, acquires Lyrebird" (September 18, 2019)](https://techcrunch.com/2019/09/18/descript-audio/)
9. [Voicebot.ai — "Descript Acquires Lyrebird and Lands $15 Million in Funding" (September 18, 2019)](https://voicebot.ai/2019/09/18/descript-acquires-lyrebird-and-lands-15-million-in-funding-from-andreessen-horowitz-and-redpoint/)
10. [Descript — Lyrebird page](https://www.descript.com/lyrebird)
11. [PitchBook — Lyrebird company profile](https://pitchbook.com/profiles/company/180241-48)
12. [CB Insights — Lyrebird company profile](https://www.cbinsights.com/company/lyrebird)
13. [Next Nature — "Lyrebird API Copies Human Voice" (2017)](https://nextnature.org/en/magazine/story/2017/lyrebird-api-copies-human-voice)
14. [Product Hunt — Lyrebird product launches](https://www.producthunt.com/products/lyrebird)
15. [Wayback Machine — Lyrebird.ai homepage, September 29, 2017](https://web.archive.org/web/20170929141709im_/https://lyrebird.ai/)
