# Research Report: Hipmob

## Overview

Hipmob was a Palo Alto-based mobile software company, founded in 2012 and part of Y Combinator's Winter 2012 batch, that built an SDK enabling iOS and Android developers to embed live customer support chat directly inside their apps.The company correctly identified that mobile apps lacked the customer communication infrastructure that web products like Olark and Zendesk had already built—and spent five years building a technically sound, feature-rich solution to that problem.

But the market it chose proved too narrow to sustain an independent company.Hipmob raised only its initial $120,000 YC seed check, never closed a Series A, and was acquired by U.K.-based social customer care platform Conversocial in March 2017 in an all-stock deal of undisclosed value.

The core failure was not execution but market selection: the founders built the right product for a niche that was too small, too cost-sensitive, and too susceptible to absorption by larger platforms to generate the growth investors required.

<report-gallery>
<media-image src="https://github.com/Hipmob.png" alt="Hipmob GitHub organization avatar/logo" caption="Hipmob's GitHub presence — 30+ public repositories spanning iOS, Android, and Cordova SDKs — a testament to the years of meticulous engineering the team poured into a market that would ultimately prove too narrow to sustain them."></media-image>
<media-image src="https://www.iculture.nl/wp-content/uploads/2012/07/hipmob-connecting.jpg" alt="Hipmob maakt live supportchat in iPhone-apps mogelijk" caption="A screenshot of Hipmob's live chat interface connecting inside an iPhone app, circa mid-2012 — the product that Ayo Omojola called 'Olark for mobile,' built to solve the support gap the founders had felt firsthand while shipping their own gaming app during YC W12."></media-image>
</report-gallery>

## Founding Story

Hipmob was founded in early 2012 by three co-founders: brothers Ayo Omojola and Femi Omojola, and Gaurav Namit. <sup><a href="https://app.dealroom.co/companies/hipmob">[1]</a></sup> Ayo served as CEO; Femi was the primary SDK engineer, with an extensive GitHub footprint across the company's iOS, Android, and cross-platform repositories; Gaurav's specific role is not documented in public sources. The team brought roughly five years of prior mobile product development experience to the founding, giving them genuine domain credibility in a space that most enterprise software founders had not yet taken seriously. <sup><a href="https://techmoran.com/2014/02/01/ceo-weekends-hipmob-wants-to-provide-killer-customer-support-to-your-mobile-customers/">[2]</a></sup>

The founding story is unusually clean: the idea did not emerge from market research or investor thesis-matching. It emerged from the founders' own frustration. While building a gaming app during the YC W12 program itself, the team realized there was no good way to communicate with users inside a mobile app—no equivalent of the live chat widgets that had become standard on e-commerce websites. <sup><a href="https://app.dealroom.co/companies/hipmob">[3]</a></sup> The gap was obvious to anyone who had shipped a mobile product and tried to handle support through email or app store reviews.

Ayo was direct about this on Hacker News in July 2012, when Hipmob posted its first major product announcement: the company was "built to scratch our own itch," and was focused exclusively on mobile, not web live chat. <sup><a href="https://news.ycombinator.com/item?id=4230700">[4]</a></sup> That authenticity gave the team credibility with developer audiences and shaped a product culture that was genuinely user-empathetic—but it also anchored the company to a problem definition that was narrower than the broader market opportunity in mobile customer engagement.

Hipmob participated in YC W12 alongside 65 other companies and presented at Demo Day at the Computer History Museum in Mountain View in March 2012. <sup><a href="https://www.ycombinator.com/companies/hipmob">[5]</a></sup> The batch was competitive, and Demo Day represented a strong launchpad—but it also set a fundraising bar that Hipmob would ultimately never clear again. The $120,000 YC seed check was the only institutional capital the company ever raised. <sup><a href="https://tracxn.com/d/companies/hipmob/__ZFGnH1pnlVa6nfsUbB9sRH_l2pZJSO_peSk1lq3ZIBU">[6]</a></sup>

What the founders lacked was not technical skill or work ethic. As Ayo later reflected, the team "cranked for years and worked so hard." The deficit was in the upstream decision of what to build toward. That realization would take five years to fully crystallize.

---

## Timeline

- **January 2012** — Hipmob founded; joins Y Combinator Winter 2012 batch. Founding idea emerges while building a gaming app during the program. <sup>[[5]](https://www.ycombinator.com/companies/hipmob)</sup>
- **January 2012** — Raises $120,000 seed round from Y Combinator—its only known funding. <sup>[[6]](https://tracxn.com/d/companies/hipmob/__ZFGnH1pnlVa6nfsUbB9sRH_l2pZJSO_peSk1lq3ZIBU)</sup>
- **March 27, 2012** — Presents at YC W12 Demo Day at the Computer History Museum in Mountain View alongside 65 other companies.
- **July 11, 2012** — Posts first major Show HN, positioning Hipmob as "Olark for mobile apps." Ayo Omojola confirms the product was "built to scratch our own itch." <sup>[[4]](https://news.ycombinator.com/item?id=4230700)</sup>

<media-hn url="https://news.ycombinator.com/item?id=4230700" title="Show HN: Hipmob is Olark for mobile apps. (Live support chat, now on Android)" points="" comments=""></media-hn>

- **September 2012** — Posts second Show HN showcasing peer-to-peer chat functionality for iOS and Android apps, engaging developer questions around privacy and device identifiers.

<media-hn url="https://news.ycombinator.com/item?id=4541195" title="Show HN: Easily add peer-to-peer chat to your iPhone/Android app (from Hipmob)" points="" comments=""></media-hn>

- **January 31, 2013** — TechCrunch covers Hipmob as "the premier in-app customer service tool," detailing the full feature set, pricing model, and CRM integrations. Ayo Omojola states: "Nobody has invented a full mobile support desk yet." <sup>[[7]](https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/)</sup>
- **February 2014** — TechMoran profiles Hipmob, confirming the team's mobile experience and customer support positioning. <sup>[[2]](https://techmoran.com/2014/02/01/ceo-weekends-hipmob-wants-to-provide-killer-customer-support-to-your-mobile-customers/)</sup>
- **March 21, 2017** — Hipmob acquired by Conversocial in an all-stock deal of undisclosed value. Hipmob brand fully absorbed. <sup>[[8]](https://techcrunch.com/2017/03/21/not-too-hip-to-be-acquired/)</sup>
- **2017** — Ayo Omojola joins Square as founding product lead on the Cash App banking team, where he co-creates the Cash Card. <sup>[[9]](https://www.lead.bank/team/ayokunle-ayo-omojola)</sup>
- **2017** — Ayo co-founds SquareAngels and the YC Alumni Syndicate; becomes active angel investor in Mercury, Modern Treasury, and Faire. <sup>[[10]](https://www.pinwheelapi.com/blog-post/ayokunle-ayo-omojola-joins-pinwheels-board-of-directors)</sup>

---

## What They Built

Hipmob's core product was a mobile SDK—a software package that iOS and Android developers could drop into their existing apps—paired with a web-based admin dashboard for support agents. <sup><a href="https://techmoran.com/2014/02/01/ceo-weekends-hipmob-wants-to-provide-killer-customer-support-to-your-mobile-customers/">[11]</a></sup> The analogy the founders used publicly was "Olark for mobile apps": Olark was the dominant live chat widget for websites, and Hipmob aimed to be its equivalent for the app ecosystem. <sup><a href="https://news.ycombinator.com/item?id=4230700">[4]</a></sup>

<media-image src="https://techcrunch.com/wp-content/uploads/2013/01/hipmob.png" alt="Hipmob in-app live chat interface shown on a mobile device, from TechCrunch's 2013 coverage" caption="TechCrunch's January 2013 feature on Hipmob: 'YC-Backed Hipmob Wants To Become The Premier In-App Customer Service Tool' — the article's hero image showing the Hipmob mobile chat UI."></media-image>

The user experience worked in two directions. For the end user—someone using, say, an e-commerce or gaming app—a support button appeared inside the app itself. Tapping it opened a live chat window without leaving the application, allowing them to type a message, send an image, or even record and send an audio clip. For the support agent on the other side, the web dashboard surfaced incoming conversations in real time, with full context about which app the user was in and what they had done. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[12]</a></sup>

The feature set by early 2013 was comprehensive for the category: live chat, a helpdesk ticketing layer, in-app feedback collection, push notifications, audio messages, and image sharing. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[12]</a></sup> This was not a minimal product—it covered the full surface area of in-app customer communication.

Integration was designed to minimize friction for developers. Embedding the SDK was engineered to take an experienced developer under one hour, and the library added less than 350 kilobytes to an app's binary—a meaningful consideration in an era when app size affected download conversion rates. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[12]</a></sup>

<media-image src="https://web.archive.org/web/20130201im_/http://www.hipmob.com/" alt="Archived Hipmob homepage from early 2013, showing the product landing page for in-app mobile live chat" caption="Wayback Machine capture of Hipmob's homepage circa early 2013 — shortly after the TechCrunch feature — showing how the team marketed their in-app live chat SDK to iOS and Android developers."></media-image>

Hipmob also built a substantial integration layer from early on. Conversations were automatically synced to Salesforce, Desk.com, Highrise, Campfire, HipChat, Shopify, and Zendesk after each chat session ended. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[13]</a></sup> This was a deliberate positioning choice: rather than asking enterprise customers to replace their existing CRM workflows, Hipmob slotted in as a mobile-native data source that fed those systems. It was a smart enterprise sales posture for a two-person team.

The team's developer-first culture is visible in their GitHub output. Hipmob maintained 30+ public repositories covering iOS and Android SDKs, Cordova and PhoneGap plugins, and sample applications—evidence of a team that understood its primary buyers were engineers who needed to evaluate the product by reading code, not marketing copy.

<media-image src="https://github.com/Hipmob.png" alt="Hipmob GitHub organization avatar/logo" caption="Hipmob's GitHub organization profile, which hosts 30+ public repositories including iOS and Android SDKs, Cordova/PhoneGap plugins, and sample apps — evidence of the team's prolific open-source developer tooling."></media-image>

What distinguished Hipmob from alternatives at launch was specificity: it was built exclusively for mobile, not ported from a web product. Olark and Zendesk's chat products existed for websites; Hipmob's SDK was native to iOS and Android from day one, which meant it handled mobile-specific behaviors—push notification fallback when a user left the app, device-appropriate UI patterns, audio messaging—that web-first tools could not replicate without significant engineering work.

---

## Market Position

### Target Customers

Hipmob's primary buyer was the mobile app developer or the product team behind a consumer or SMB-facing iOS or Android application. The go-to-market was developer-led: Show HN posts, GitHub repositories, and SDK documentation were the primary acquisition channels. The secondary buyer was the customer support manager at a company that had already shipped a mobile app and was struggling to handle support through email or app store reviews.

Notable early customers included Rackspace and Samsung SmartThings, as well as a taxi app in Mexico and various e-commerce companies. <sup><a href="https://www.lead.bank/team/ayokunle-ayo-omojola">[14]</a></sup> This customer list is instructive in what it reveals: the accounts were real and credible, but they were heterogeneous. Rackspace (enterprise cloud infrastructure), Samsung SmartThings (IoT platform), a Mexican taxi app, and e-commerce companies represent four entirely different use cases, buyer personas, and sales motions. The absence of a tight ideal customer profile suggests the team was taking customers where they could find them rather than executing a focused segment strategy.

### Market Size

The market Hipmob was addressing—in-app mobile customer support SDKs sold to app developers—was structurally constrained in ways that were not fully apparent in 2012 but became clear over time.

Ayo Omojola correctly identified in early 2013 that mobile customer support was underserved relative to web tools. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[7]</a></sup> The gap was real. But the addressable universe of mobile apps willing to pay a monthly subscription for embedded customer support was finite and, critically, cost-sensitive. App developers—especially indie developers and small studios—operate on thin margins and are accustomed to free or near-free developer tooling. Enterprise app teams (the Rackspaces and Samsung SmartThings of the world) had the budget but required enterprise sales infrastructure that a two-person team could not sustain.

The founder's own retrospective confirms the market size diagnosis. Ayo later said the team "hadn't chosen a large enough market"—a judgment that applies both to the absolute size of the in-app SDK category and to its structural ceiling. <sup><a href="https://review.firstround.com/finding-startup-ideas-and-building-in-heavily-regulated-spaces-lessons-from-cash-app-and-carbon-health/">[15]</a></sup>

### Competition

In 2012 and 2013, Hipmob had few direct competitors in the mobile-native in-app support SDK space—Ayo's claim that "nobody has invented a full mobile support desk yet" was largely accurate at the time. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[7]</a></sup>

The competitive threat that materialized was not from direct SDK competitors but from platform expansion by larger players. Intercom, founded in 2011, initially focused on web-based in-app messaging but progressively built out mobile SDKs and customer support features, backed by over $240 million in venture funding. Zendesk, already a dominant helpdesk platform, developed its own mobile SDK. These companies had the distribution, brand recognition, and capital to bundle mobile support into existing enterprise relationships at no marginal cost to the buyer. A standalone mobile support SDK at $25–$100 per seat per month became a harder sell when Zendesk could offer the same capability as a feature of a contract the customer already had.

The second competitive dynamic was platform commoditization. As mobile development frameworks matured and open-source chat libraries proliferated, the technical barrier to building basic in-app messaging dropped. The differentiation that Hipmob's SDK provided in 2012—native mobile UI, push fallback, audio messaging—became table stakes that any competent mobile engineering team could replicate or source from free libraries by 2015.

---

## Business Model

Hipmob charged on a hybrid per-seat plus per-volume basis. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[16]</a></sup> The entry-level plan was $25 per seat per month for one agent and up to 500 chats per month, without CRM integration. Higher-tier plans unlocked full CRM sync with Salesforce, Zendesk, and other platforms, at proportionally higher prices. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[16]</a></sup>

The pricing structure was reasonable for SMB customers but created a ceiling problem. At $25 per seat, a five-agent support team represented $125 per month—$1,500 annually. Even at 100 such customers, annual recurring revenue would be $150,000, barely enough to sustain a team of two in the Bay Area. Scaling to enterprise contracts required a sales motion the team was not resourced to execute. The "reach" component (chats per month) added a usage-based dimension that could theoretically scale with customer growth, but no public data exists on whether any customers reached volumes that generated meaningful revenue uplift.

---

## Traction

Hipmob's documented customer base included Rackspace and Samsung SmartThings as marquee accounts, alongside a taxi app in Mexico and multiple e-commerce companies. <sup><a href="https://www.lead.bank/team/ayokunle-ayo-omojola">[14]</a></sup> These names provided credibility for press coverage and enterprise sales conversations, but the customer list's heterogeneity suggests the company never achieved the repeatable sales motion that would have supported a Series A fundraise.

No public data exists on total SDK integrations, monthly active developers, chat volume, or revenue at any point in the company's five-year life. The YC company profile lists a team size of two employees and status as "Inactive." <sup><a href="https://www.ycombinator.com/companies/hipmob">[5]</a></sup> Operating for five years on a $120,000 seed round with a two-person team implies either near-breakeven revenue or extreme capital efficiency—but also that the company lacked the resources to invest in sales, marketing, or product expansion at the pace required to compete as the market matured.

The strongest signal on traction is the absence of a Series A. Investors who saw the company's metrics between 2012 and 2017 did not find sufficient evidence of growth to justify a follow-on investment. That judgment, made repeatedly over five years, is the most reliable proxy for the company's revenue trajectory.

---

## Post-Mortem

<media-image src="https://techcrunch.com/wp-content/uploads/2017/03/gettyimages-636760982.jpg" alt="TechCrunch article header image for Conversocial's acquisition of HipMob, March 2017" caption="TechCrunch's March 21, 2017 acquisition announcement: 'Conversocial buys live chat and in-app messaging startup HipMob to bolster customer care platform' — marking the end of Hipmob as an independent company after 5 years."></media-image>

Hipmob's acquisition by Conversocial on March 21, 2017 was an all-stock deal of undisclosed value, structured primarily around technology and platform rather than team retention. <sup><a href="https://techcrunch.com/2017/03/21/not-too-hip-to-be-acquired/">[8]</a></sup> Tracxn classifies the outcome as an acqui-hire. <sup><a href="https://tracxn.com/d/companies/hipmob/__ZFGnH1pnlVa6nfsUbB9sRH_l2pZJSO_peSk1lq3ZIBU">[17]</a></sup> The Hipmob brand was fully absorbed; no independent product line survived. <sup><a href="https://techcrunch.com/2017/03/21/not-too-hip-to-be-acquired/">[18]</a></sup> Five years of work ended without a disclosed return to investors or founders.

The failure has a single primary cause, confirmed by the founder himself, with several compounding factors.

### Primary Cause: The Market Was Too Small

Ayo Omojola's retrospective, delivered in a First Round Capital interview about his subsequent career, is the most direct primary source on what went wrong:

> "When I think back to my last company, I was co-founders with my brother and a friend. We picked a problem to tackle that we found really technically interesting. We cranked for years and worked so hard and it just didn't matter." <sup><a href="https://review.firstround.com/finding-startup-ideas-and-building-in-heavily-regulated-spaces-lessons-from-cash-app-and-carbon-health/">[19]</a></sup>

His diagnosis is unambiguous:

> "The lesson I took from it was that we had put so much effort into the actual work, and had not put nearly enough effort into choosing what to work on. That was a much bigger determinant to our outcome — we hadn't chosen a large enough market." <sup><a href="https://review.firstround.com/finding-startup-ideas-and-building-in-heavily-regulated-spaces-lessons-from-cash-app-and-carbon-health/">[15]</a></sup>

The in-app mobile customer support SDK market had a structural ceiling. The universe of mobile apps willing to pay a monthly subscription for embedded support tooling was finite. Cost-sensitive indie developers would not pay; enterprise teams required a sales infrastructure the company could not fund. The $25-per-seat entry price, while accessible, meant that even a healthy customer base of 200 accounts at average revenue of $75 per month would generate only $180,000 in annual recurring revenue—insufficient to raise a Series A in 2014 or 2015, when growth-stage investors expected $1M+ ARR with strong month-over-month acceleration.

The team's attempted remedy was to expand the feature set—adding audio messages, image sharing, peer-to-peer chat, and a growing integration ecosystem—to justify higher price points and attract enterprise buyers. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[12]</a></sup> This was the right instinct but insufficient: feature expansion cannot solve a market size problem when the ceiling is structural rather than competitive.

### Compounding Factor: No Follow-On Funding, No Growth Capital

Hipmob operated for approximately five years on a single $120,000 seed check. <sup><a href="https://tracxn.com/d/companies/hipmob/__ZFGnH1pnlVa6nfsUbB9sRH_l2pZJSO_peSk1lq3ZIBU">[6]</a></sup> The team size never grew beyond two employees. <sup><a href="https://www.ycombinator.com/companies/hipmob">[5]</a></sup> This capital constraint was both a symptom and a cause: investors passed because the growth metrics did not support a Series A, and the absence of capital prevented the company from investing in the sales, marketing, and engineering headcount that might have accelerated those metrics.

The specific mechanism of failure here is a feedback loop. Without a Series A, Hipmob could not hire a sales team to pursue enterprise contracts. Without enterprise contracts, revenue growth remained slow. Without revenue growth, a Series A remained out of reach. The company was trapped in a self-reinforcing constraint that the founding team's technical excellence could not break.

The attempted remedy was capital efficiency: keeping the team small, maintaining the product with two engineers, and relying on inbound developer interest through Hacker News and GitHub rather than outbound sales. This approach extended the company's runway but did not change its trajectory.

### Compounding Factor: Platform Absorption by Larger Competitors

Between 2013 and 2017, the competitive landscape shifted in a way that was structurally disadvantageous to Hipmob. Intercom, which had raised over $240 million by 2017, built out mobile SDKs and customer support features that directly overlapped with Hipmob's core offering. Zendesk developed its own mobile SDK. These companies could offer mobile in-app support as a bundled feature of existing enterprise contracts, effectively making Hipmob's standalone product redundant for any customer already using those platforms.

Hipmob's integration strategy—syncing conversations to Salesforce, Zendesk, and HipChat—was designed to position the product as a complement to these platforms rather than a competitor. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[13]</a></sup> In practice, this positioning made Hipmob dependent on the continued willingness of those platforms to leave the mobile support layer to third parties. When Zendesk and Intercom built their own mobile SDKs, Hipmob's integration partnerships became less valuable and its standalone case became harder to make.

The team had no effective remedy for this dynamic. Competing with Intercom or Zendesk on features required capital the company did not have. Differentiating on price would have further compressed already-thin margins.

### Compounding Factor: The Acqui-Hire as Soft Landing

Ayo Omojola's public statement at the time of acquisition framed the deal as validation: "Becoming a part of Conversocial's industry leading platform is testament to the power of multi-channel engagement." <sup><a href="https://www.prweb.com/releases/2017/03/prweb14166068.htm">[20]</a></sup> The framing is diplomatically positive but notably shifts the language from Hipmob's original mobile-first positioning to Conversocial's social customer care thesis—a reframing that signals the deal was driven by Conversocial's strategic needs rather than Hipmob's negotiating leverage.

An all-stock deal of undisclosed value, classified as an acqui-hire, is the standard structure for a below-expectations exit. The Hipmob brand was fully absorbed with no surviving product line. <sup><a href="https://techcrunch.com/2017/03/21/not-too-hip-to-be-acquired/">[18]</a></sup> The outcome was not a failure of character or effort—the founders worked for five years on a technically sound product—but it was a failure to generate a return commensurate with the opportunity cost of five years of founder time.

---

## Key Lessons

- **Market selection is a higher-leverage decision than product execution.** Hipmob's founders were technically skilled and worked hard for five years. The product was well-built, well-integrated, and well-received by the press. None of that mattered because the market ceiling was too low to support a venture-scale outcome. Ayo Omojola's own retrospective makes this explicit: effort and craft are necessary but not sufficient conditions for startup success. <sup><a href="https://review.firstround.com/finding-startup-ideas-and-building-in-heavily-regulated-spaces-lessons-from-cash-app-and-carbon-health/">[15]</a></sup> The decision of *what* to build is more consequential than *how well* you build it.

- **Developer-first go-to-market requires a large enough developer addressable market.** Hipmob's SDK distribution strategy—GitHub repositories, Hacker News posts, minimal-friction integration—was well-suited to reaching developers. But the universe of developers building apps that would pay for embedded customer support was smaller than the universe of developers generally. A developer-first GTM strategy amplifies reach within a segment; it cannot expand the segment itself. Companies like Stripe and Twilio succeeded with similar strategies because the underlying markets (payments, communications) were enormous. Hipmob's underlying market was not.

- **Integration partnerships with larger platforms are a double-edged strategy.** Hipmob's early integrations with Salesforce, Zendesk, and HipChat were smart positioning for a small team: they reduced friction for enterprise buyers and positioned Hipmob as a complement rather than a threat. <sup><a href="https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/">[13]</a></sup> But those same platforms eventually built the mobile capabilities Hipmob provided, converting a complementary relationship into a competitive one. Startups that build on top of or alongside larger platforms should model the scenario in which the platform absorbs their function—and have a plan for that outcome before it happens.

- **Authentic founder-market fit is necessary but not sufficient.** Hipmob's founding story—building a product to solve a problem the founders personally experienced—is the ideal origin story. It produced a technically credible product and a developer-empathetic culture. But authentic founder-market fit does not guarantee that the market is large enough to support a company. The "scratch your own itch" heuristic works best when the itch is shared by a very large number of people willing to pay to have it scratched.

---

## Sources

1. [Dealroom — Hipmob company profile](https://app.dealroom.co/companies/hipmob)
2. [TechMoran — CEO Weekends: Hipmob wants to provide killer customer support to your mobile customers (February 1, 2014)](https://techmoran.com/2014/02/01/ceo-weekends-hipmob-wants-to-provide-killer-customer-support-to-your-mobile-customers/)
3. [Y Combinator — Hipmob company profile](https://www.ycombinator.com/companies/hipmob)
4. [Hacker News — Show HN: Hipmob is Olark for mobile apps (July 11, 2012)](https://news.ycombinator.com/item?id=4230700)
5. [Hacker News — Show HN: Easily add peer-to-peer chat to your iPhone/Android app (from Hipmob)](https://news.ycombinator.com/item?id=4541195)
6. [Tracxn — Hipmob company profile](https://tracxn.com/d/companies/hipmob/__ZFGnH1pnlVa6nfsUbB9sRH_l2pZJSO_peSk1lq3ZIBU)
7. [TechCrunch — YC-Backed Hipmob Wants To Become The Premier In-App Customer Service Tool (January 31, 2013)](https://techcrunch.com/2013/01/31/yc-backed-hipmob-wants-to-become-the-premier-in-app-customer-service-tool/)
8. [TechCrunch — Conversocial buys live chat and in-app messaging startup HipMob (March 21, 2017)](https://techcrunch.com/2017/03/21/not-too-hip-to-be-acquired/)
9. [Lead Bank — Ayo Omojola team profile](https://www.lead.bank/team/ayokunle-ayo-omojola)
10. [Pinwheel — Ayo Omojola joins Pinwheel's Board of Directors](https://www.pinwheelapi.com/blog-post/ayokunle-ayo-omojola-joins-pinwheels-board-of-directors)
11. [First Round Review — Finding Startup Ideas and Building in Heavily Regulated Spaces: Lessons from Cash App and Carbon Health](https://review.firstround.com/finding-startup-ideas-and-building-in-heavily-regulated-spaces-lessons-from-cash-app-and-carbon-health/)
12. [PRWeb — Conversocial Acquires HipMob (March 21, 2017)](https://www.prweb.com/releases/2017/03/prweb14166068.htm)
13. [TechCrunch — YC W12 Demo Day Coverage (March 27, 2012)](https://techcrunch.com/2012/03/27/yc-demo-day-session-1/)
