# Research Report: Selfycart

## Overview

Selfycart was founded in June 2015 by Sahle Hashelit and Erick Lee, two operators with unusually direct domain experience for the problem they were attacking. Both had worked at PayPal and eBay — the intersection of payments infrastructure and consumer commerce — before turning their attention to offline retail. As Hashelit put it: "Both Erick and I have domain expertise in payments and mobile commerce. We worked at PayPal and Ebay." <sup><a href="https://blog.ycombinator.com/selfycart/">[1]</a></sup>

Hashelit's background was particularly well-suited to the enterprise side of the business. He had served as Head of Global Technical Service at eBay and PayPal, and had additional stints at Facebook and Symantec — a profile that combined payments operations with enterprise-scale technical management. <sup><a href="https://everipedia.org/wiki/lang_en/sahle-hashelit">[2]</a></sup> Lee brought a different kind of credibility: a whitehat security hacker and serial entrepreneur who had founded three startups before Selfycart, with prior PayPal experience giving him direct exposure to the payment rails the product would depend on. <sup><a href="https://www.zoominfo.com/c/selfycart-inc/373817703">[3]</a></sup>

The founding insight came from a frustration that anyone who has stood in a grocery checkout line will recognize. Lee articulated it bluntly: "The promise of self-checkout and the reality of self-checkout are two totally different things... there's kind of a line there, the machine doesn't really work and people don't know how to make it work." <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[4]</a></sup> The founders believed that the smartphone — already in nearly every shopper's pocket — was a better self-checkout terminal than the dedicated kiosks retailers had spent billions deploying. The phone already had a camera for scanning, a payment credential on file, and a screen the user already knew how to operate.

The company was accepted into Y Combinator's Summer 2016 batch, <sup><a href="https://www.ycombinator.com/companies/selfycart">[5]</a></sup> which provided the $120,000 seed check and the Demo Day platform that would define the company's fundraising window. The YC batch forced a product and go-to-market focus that culminated in a public launch on August 1, 2016 — the same day as the TechCrunch article that gave the company its widest press exposure.

No public account exists of how Hashelit and Lee first met, and the founding year is listed inconsistently across databases (2015 vs. 2016), though Hashelit's LinkedIn tenure beginning in June 2015 is the most reliable signal. <sup><a href="https://contactout.com/Sahle-Hashelit-2448334">[6]</a></sup> The company was headquartered in the Bay Area, with sources variously citing San Mateo, Santa Clara, and San Jose. <sup><a href="https://www.ycombinator.com/companies/selfycart">[7]</a></sup>

---

## Founding Story

## Timeline

- **June 2015** — Sahle Hashelit and Erick Lee co-found Selfycart, drawing on their shared PayPal and eBay backgrounds. <sup>[[8]](https://tracxn.com/d/companies/selfycart/__bsBV9GJxo-vEiWX8GRZBSkzCWaMeQzRKtWKhbNsnoNQ)</sup>

- **2016** — Selfycart is accepted into Y Combinator's Summer 2016 (S16) batch. <sup>[[5]](https://www.ycombinator.com/companies/selfycart)</sup>

- **August 1, 2016** — Selfycart launches publicly at Rainbow Grocery in San Francisco. iOS and Android apps go live simultaneously. Initial merchant partners are Rainbow Grocery and Zanotto's. The company is two people. TechCrunch publishes a dedicated launch article. <sup>[[9]](https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/)</sup>

- **August 23, 2016** — Selfycart presents at YC Demo Day 2 (Summer 2016), pitching a 2% retailer transaction fee model to investors and seeking a $2–3M seed round. <sup>[[10]](https://techcrunch.com/2016/08/23/yc-demo-day/)</sup>

- **August 24, 2016** — Selfycart closes a seed round of approximately $120,000, consistent with a standard YC batch investment of the era. <sup>[[11]](https://tracxn.com/d/companies/selfycart/__bsBV9GJxo-vEiWX8GRZBSkzCWaMeQzRKtWKhbNsnoNQ)</sup>

- **September 12, 2016** — Selfycart posts a job listing on Hacker News for a Senior Full Stack Software Engineer (Node.js/REST APIs), confirming the company is still operating and attempting to grow its team post-Demo Day. <sup>[[12]](https://news.ycombinator.com/item?id=12477379)</sup>

<media-hn url="https://news.ycombinator.com/item?id=12477379" title="Selfycart (YC S16) Is Hiring Sr. Software Engineer – Full Stack" points="" comments=""></media-hn>

- **Late 2016** — Twitter artifacts suggest expansion to Bianchini's Market. Discussions with Andronicos and Mollie Stones are reported but not confirmed as signed. <sup>[[13]](https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/)</sup>

- **Late 2016** — Selfycart is named a finalist in the 43North $5M startup competition, competing for a $1M prize at Shea's Performing Arts Center in Buffalo, NY — confirming continued activity after Demo Day.

- **December 28, 2016** — Wayback Machine captures a snapshot of Selfycart's website, confirming the company is still operational.

- **Early 2017** — CEO Sahle Hashelit tweets about Selfycart being used at Walgreens, suggesting expansion beyond the initial grocery store partners.

- **June 2019** — Sahle Hashelit's LinkedIn tenure at Selfycart ends, indicating the company wound down around mid-2019 after approximately four years of operation. <sup>[[6]](https://contactout.com/Sahle-Hashelit-2448334)</sup>

- **July 2019** — Hashelit joins Arena Analytics as Senior Product Manager, marking his formal departure from Selfycart. <sup>[[6]](https://contactout.com/Sahle-Hashelit-2448334)</sup>

---

## What They Built

Selfycart's core product was a mobile self-checkout application for brick-and-mortar grocery stores. The concept was straightforward: instead of unloading a cart at a register, a shopper opened the Selfycart app, scanned each item's barcode directly from the store shelf as they placed it in their basket, and paid on their phone before reaching the exit. On the way out, a store associate checked the shopper's digital QR code receipt — a deliberate loss-prevention step that distinguished Selfycart from fully autonomous concepts. <sup><a href="https://blog.ycombinator.com/selfycart/">[14]</a></sup>

Payment options at launch included credit card, Apple Pay, and PayPal. <sup><a href="https://blog.ycombinator.com/selfycart/">[14]</a></sup> The app was available on iOS at launch on August 1, 2016, with Android added the same day — an unusually fast cross-platform push that suggests the team prioritized breadth over depth heading into Demo Day. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[15]</a></sup>

<media-image src="https://techcrunch.com/wp-content/uploads/2016/08/selfycart.jpg" alt="Selfycart TechCrunch launch article header image" caption="TechCrunch coverage of Selfycart's August 1, 2016 launch at Rainbow Grocery — the company's first live deployment of its mobile self-checkout app."></media-image>

The product had two distinct customer-facing layers. For shoppers, the experience was designed to eliminate the average 7-minute grocery checkout wait, replacing it with what Hashelit claimed was a 15-second mobile checkout. <sup><a href="https://blog.ycombinator.com/selfycart/">[16]</a></sup> For merchants, Selfycart offered more than just a checkout replacement. The platform captured behavioral data — which items shoppers picked up and put back, dwell time in aisles, basket composition before abandonment — that traditional point-of-sale systems could not record. <sup><a href="https://blog.ycombinator.com/selfycart/">[16]</a></sup> This analytics layer was a secondary value proposition intended to create retailer stickiness beyond the checkout convenience alone.

Selfycart also offered a B2B API that allowed other apps to integrate its mobile checkout and payment capabilities, and supported merchants importing inventory from multiple sources. <sup><a href="https://tracxn.com/d/companies/selfycart/__bsBV9GJxo-vEiWX8GRZBSkzCWaMeQzRKtWKhbNsnoNQ">[17]</a></sup> This API layer suggested the founders were thinking about Selfycart as a platform, not just a consumer app — a positioning that would have required significantly more engineering resources than a two-person team could sustain.

The hardest technical challenge, per CTO Erick Lee, was not the consumer-facing app itself: "The mechanics of integrating the inventory and payment with an existing retailers system and making it work seamlessly for end-users. There [are] a lot of complexity to integrate all of these different platforms in a way that works great." <sup><a href="https://blog.ycombinator.com/selfycart/">[18]</a></sup> Every grocery store runs a different combination of inventory management software, POS hardware, and payment processing infrastructure — often legacy systems that predate modern APIs. Each new merchant integration was effectively a custom engineering project.

<media-tweet url="https://twitter.com/selfycart" author="@selfycart" date="2016-08-01" text="Never wait in line again! In App Store https://appsto.re/us/iCDv-.i"></media-tweet>

What differentiated Selfycart from the self-checkout kiosks already in stores was the absence of dedicated hardware. Retailers had invested heavily in self-checkout terminals that required maintenance, software updates, and dedicated floor space — and still generated long lines and user errors. Selfycart's model shifted the terminal to the shopper's existing device, eliminating the hardware cost entirely. The QR code exit check preserved loss prevention without requiring computer vision or RFID infrastructure.

<media-tweet url="https://twitter.com/selfycart" author="@selfycart" date="2016-09-01" text="@selfycart turns your phone into a self-checkout machine. pic.twitter.com/1VOL1XM9kj – at Bianchini's Market"></media-tweet>

---

## Market Position

### Target Customers

Selfycart pursued a two-sided market from day one. On the consumer side, the target was smartphone-equipped grocery shoppers — specifically those frustrated by checkout line wait times and comfortable with mobile payments. The launch at Rainbow Grocery, a San Francisco cooperative with a tech-forward, independent-minded customer base, was a deliberate choice to find early adopters who would tolerate a new checkout workflow. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[9]</a></sup>

On the merchant side, Selfycart initially targeted independent Bay Area grocers — Rainbow Grocery and Zanotto's at launch, with Andronicos and Mollie Stones in discussion. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[13]</a></sup> Independent grocers were a pragmatic beachhead: faster sales cycles than national chains, more willing to experiment, and less encumbered by enterprise procurement processes. The tradeoff was that independent grocers carry less weight as reference customers when pitching institutional investors who want to see national chain traction.

The Demo Day pitch implied an eventual move upmarket. Selfycart described itself as seeking capital to "support larger customers" and "expand to regional store locations" — language that pointed toward regional chains as the next tier. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[19]</a></sup> Whether that progression ever materialized is unknown; no confirmed partnerships beyond the initial independent grocers appear in any source.

### Market Size

The U.S. grocery market is one of the largest retail categories by volume, with consumers making frequent, high-frequency purchases that make checkout friction a recurring pain point rather than an occasional inconvenience. Selfycart did not publish a formal market size estimate in available sources, but the Demo Day framing — replacing "large checkout operations" with a 2% transaction fee — implied the company was sizing itself against the operational cost of checkout infrastructure across the grocery industry, not just the self-checkout kiosk market.

The broader mobile payments and retail technology market was growing rapidly in 2016, with Apple Pay launching in 2014 and Android Pay following in 2015. YC Partner Dalton Caldwell's endorsement captured the macro tailwind: "With the prevalence of smartphones and mobile payments, this technology is inevitable. Selfycart is something that consumers want and the time is now." <sup><a href="https://blog.ycombinator.com/selfycart/">[20]</a></sup>

### Competition

In 2016, Selfycart's most direct competitive frame was against the self-checkout kiosks already deployed in major grocery chains — machines that Lee described as fundamentally broken in practice. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[4]</a></sup> The kiosk market was dominated by NCR and Diebold Nixdorf, but Selfycart was not competing for the same hardware budget — it was arguing that the hardware model itself was wrong.

The more consequential competitive threat materialized in December 2016, when Amazon announced Amazon Go — a cashierless convenience store concept using computer vision, sensor fusion, and deep learning to track items without any scanning at all. Amazon Go opened to the public in January 2018. Amazon's approach did not require shoppers to scan anything; it simply tracked what they picked up and charged them automatically on exit. This leapfrogged Selfycart's barcode-scan model entirely, raising the bar for what "frictionless checkout" meant in the market's imagination — and almost certainly affected Selfycart's fundraising conversations with investors who were now comparing the company to Amazon's vision rather than to broken kiosk machines.

Other scan-and-go competitors included Walmart's Scan & Go (piloted in 2012, relaunched in 2018), and later Standard Cognition and Zippin, which pursued the computer vision approach. In 2016, however, the competitive landscape was sparse enough that Selfycart's barcode-scan model was a credible near-term solution rather than an obviously inferior one.

---

## Business Model

Selfycart operated a dual-revenue model with charges on both sides of its two-sided marketplace. Merchants paid an annual subscription of $19,800, billed in monthly installments, for access to the platform and its analytics dashboard. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[21]</a></sup> Shoppers paid a 2% fee per transaction — though the founders acknowledged this fee might need to be eliminated if it deterred app adoption. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[21]</a></sup>

The Demo Day pitch described the model slightly differently, framing the 2% as a charge to retailers rather than shoppers — positioning Selfycart as replacing the cost of "large checkout operations" with a variable transaction fee. <sup><a href="https://techcrunch.com/2016/08/23/yc-demo-day/">[22]</a></sup> This inconsistency between the launch-day TechCrunch description and the Demo Day framing suggests the business model was still being refined as the company sought investor feedback.

At $19,800 per store per year, Selfycart needed approximately 100 merchant locations to reach $2M in annual recurring revenue from subscriptions alone — a scale that required a sales and integration team far larger than two people could support.

---2f:T66a,

## Traction

Selfycart launched with two confirmed merchant partners — Rainbow Grocery and Zanotto's — both independent Bay Area grocers. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[13]</a></sup> Twitter artifacts from the @selfycart account show the app being used at Bianchini's Market as well, suggesting at least a third location was added in the months after launch. <sup><a href="https://twitter.com/selfycart">[23]</a></sup> CEO Sahle Hashelit's personal Twitter account shows the app being used at Walgreens in early 2017, though it is unclear whether this represented a formal partnership or an informal demonstration. <sup><a href="https://twitter.com/sahle">[24]</a></sup>

<media-tweet url="https://twitter.com/sahle" author="@sahle" date="2017-01-01" text="@selfycart for free just use it so I can spend more time with my family. pic.twitter.com/opDatbIUtF – at Walgreens"></media-tweet>

Selfycart reached the finalist stage at 43North, a major startup competition offering a $1M prize, confirming the company was still active and pitching well after YC Demo Day. <sup><a href="https://43north.org/governor-cuomo-announces-finalists-selected-for-4th-annual-43north-competition/">[25]</a></sup>

No data on app downloads, active users, transaction volume, or revenue is available from any source. The company never published metrics, and no investor or press source cited specific usage numbers. The absence of any quantitative traction data in coverage from a company that had TechCrunch attention and YC backing is itself a signal — companies with strong early numbers typically share them.

---

## Post-Mortem

Selfycart operated for approximately four years — from June 2015 to June 2019 — before quietly winding down. <sup><a href="https://contactout.com/Sahle-Hashelit-2448334">[6]</a></sup> No public shutdown announcement was ever made. No founder post-mortem was published. The company is listed as "Inactive" on YC's directory, "Dead" on YCDB, and "Out of Business" on PitchBook. <sup><a href="https://www.ycombinator.com/companies/selfycart">[26]</a></sup> <sup><a href="https://pitchbook.com/profiles/company/163497-52">[27]</a></sup> What follows is a reconstruction from available evidence.

### Primary Cause: The $2–3M Seed Round Was Never Raised

The most consequential event in Selfycart's history was not its launch — it was what did not happen after Demo Day. At the time of its August 1, 2016 launch, Selfycart was explicitly seeking a $2–3M seed round to expand to regional store locations, add features, support larger customers, and hire full-time employees. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[19]</a></sup> The company had approximately $120,000 in the bank — the YC check — and two people on the team. <sup><a href="https://tracxn.com/d/companies/selfycart/__bsBV9GJxo-vEiWX8GRZBSkzCWaMeQzRKtWKhbNsnoNQ">[11]</a></sup> <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[28]</a></sup>

No evidence in any source — Crunchbase, PitchBook, Tracxn, CB Insights, or press coverage — indicates that this round was ever closed. The $120,000 seed figure is consistent across the most reliable databases, and no follow-on funding announcement was ever published. <sup><a href="https://www.crunchbase.com/organization/selfycart">[29]</a></sup>

The attempted remedy was Demo Day itself — the YC platform is specifically designed to concentrate investor attention on batch companies in a compressed window. YC Partner Dalton Caldwell provided a public endorsement: "With the prevalence of smartphones and mobile payments, this technology is inevitable. Selfycart is something that consumers want and the time is now." <sup><a href="https://blog.ycombinator.com/selfycart/">[20]</a></sup> The 43North finalist selection in late 2016 suggests the team continued pitching for capital through alternative channels. Neither effort produced a disclosed round.

Why investors passed is not documented. But the evidence points to a combination of factors: two merchant partners (both independent grocers, neither a national chain), no published usage metrics, a two-person team with no engineering bench, and — by December 2016 — the looming shadow of Amazon Go's announcement, which reset investor expectations for what cashierless checkout could look like.

### Secondary Cause: Team Size Was Structurally Insufficient for the Problem

At launch in August 2016, Hashelit and Lee were the only two people working on Selfycart. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[28]</a></sup> The company was simultaneously managing consumer app development (iOS and Android), merchant integrations, enterprise sales, and fundraising — all with a team of two.

The integration problem alone was severe. Lee described it as "a lot of complexity to integrate all of these different platforms in a way that works great." <sup><a href="https://blog.ycombinator.com/selfycart/">[18]</a></sup> Every new grocery store ran a different combination of inventory management software, POS hardware, and payment processing infrastructure. Each integration was a custom engineering project. With two people, adding even one new merchant partner likely consumed weeks of engineering time — time that could not simultaneously be spent on fundraising or consumer growth.

The attempted remedy was the September 2016 Hacker News job posting for a Senior Full Stack Software Engineer with Node.js and REST API experience. <sup><a href="https://news.ycombinator.com/item?id=12477379">[12]</a></sup> Hiring one engineer would have helped, but the structural problem was that the company needed to hire before it had the capital to do so — and it needed the traction from more merchant integrations to raise the capital. This circular dependency is a classic early-stage trap, and Selfycart had no obvious way out of it without the $2–3M round closing first.

### Tertiary Cause: The Consumer Fee Created an Adoption Barrier With No Clear Resolution

Selfycart charged shoppers a 2% fee per transaction. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[21]</a></sup> The founders acknowledged this was a risk — the TechCrunch launch article noted the fee might be removed "if it deterred app adoption" — but no timeline or threshold for that decision was ever published.

A 2% fee on a $100 grocery basket is $2. That is not a large absolute amount, but it is a fee for a service that consumers already receive for free (checkout) and that competing self-checkout kiosks do not charge. The fee inverted the value proposition: instead of saving time for free, Selfycart was asking consumers to pay for the privilege of doing the store's checkout work themselves.

The attempted remedy — removing the fee if adoption suffered — was never executed publicly. Whether the fee was actually removed, whether it was the primary driver of low consumer adoption, or whether adoption was simply never measured in a way that surfaced the problem, is unknown. What is clear is that the business model description shifted between the launch-day TechCrunch article (2% from shoppers) and the Demo Day coverage (2% from retailers) — suggesting the team was still working out who should bear the transaction cost as late as August 23, 2016. <sup><a href="https://techcrunch.com/2016/08/23/yc-demo-day/">[22]</a></sup>

### Compounding Factor: Amazon Go Redefined the Category

Amazon announced Amazon Go in December 2016 — four months after Selfycart's Demo Day. The concept required no scanning at all: computer vision and sensor fusion tracked items automatically, and shoppers were charged on exit. Amazon Go opened to the public in January 2018.

Amazon's announcement did not kill Selfycart directly. But it fundamentally changed the investor conversation about what "frictionless checkout" meant. Before December 2016, Selfycart's barcode-scan model was a credible near-term solution to a real problem. After December 2016, every investor pitch had to address why Selfycart's approach was worth backing when Amazon was building something that eliminated the scanning step entirely. The specific technology that was missing from Selfycart's model — affordable, deployable computer vision at grocery store scale — was not missing from Amazon's. The gap was capital and infrastructure, not concept.

No source documents whether Amazon Go's announcement directly affected Selfycart's fundraising conversations. But the timing is notable: the company's most active public period (August–December 2016) coincides precisely with the window before Amazon's announcement, and the company's subsequent silence suggests the fundraising environment became significantly harder in 2017.

---

## Key Lessons

- **Beachhead customer selection must balance speed of partnership with investor signal value.** Selfycart's choice to launch with independent grocers (Rainbow Grocery, Zanotto's) was smart for speed — independent stores have shorter sales cycles and more flexibility to experiment. But independent grocers carry limited weight as reference customers when pitching institutional investors who want to see national chain traction. A parallel pilot with even one regional chain, even at a slower pace, might have changed the fundraising conversation materially.

- **Two-sided marketplaces with integration complexity require capital before traction, not after.** Selfycart needed engineers to add merchant integrations, needed merchant integrations to show traction, and needed traction to raise capital to hire engineers. This circular dependency is only breakable with either pre-committed capital or a dramatically simpler integration path. The company's $120,000 in funding was insufficient to break the loop, and the $2–3M round that would have broken it was never raised. <sup><a href="https://tracxn.com/d/companies/selfycart/__bsBV9GJxo-vEiWX8GRZBSkzCWaMeQzRKtWKhbNsnoNQ">[11]</a></sup> <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[19]</a></sup>

- **Consumer fees on utility-replacing products face a structural adoption ceiling.** Charging shoppers 2% to replace a free service (checkout) requires the time savings to be both real and consistently delivered. <sup><a href="https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/">[21]</a></sup> In a category where consumers already resent checkout friction, adding a monetary cost on top of a behavioral change (learning a new app) compounds the adoption barrier. The founders identified this risk but had no funded plan to resolve it.

- **Category-defining announcements from well-capitalized incumbents can freeze fundraising even for companies with real traction.** Amazon Go's December 2016 announcement did not invalidate Selfycart's product, but it changed the reference point investors used to evaluate the company. Startups operating in categories where Amazon, Google, or Apple might enter face a fundraising environment that can shift overnight — and without a closed round before that announcement, Selfycart had no buffer.

- **The absence of a public post-mortem is itself a data point.** Companies that wind down after four years of operation without publishing any explanation — no blog post, no tweet thread, no interview — typically do so because the wind-down was gradual and undramatic: not a single failure event, but a slow exhaustion of runway and momentum. Selfycart's four-year lifespan suggests the founders kept the company alive well past the point where the original thesis was clearly failing, likely through a combination of consulting, reduced burn, and continued merchant pilots. <sup><a href="https://contactout.com/Sahle-Hashelit-2448334">[6]</a></sup>

---

## Sources

1. [YC Blog — Selfycart Turns Your Smartphone Into a Self-Checkout Machine (August 1, 2016)](https://blog.ycombinator.com/selfycart/)
2. [Everipedia — Sahle Hashelit profile](https://everipedia.org/wiki/lang_en/sahle-hashelit)
3. [ZoomInfo — Selfycart Inc. company profile](https://www.zoominfo.com/c/selfycart-inc/373817703)
4. [TechCrunch — Selfycart launch article (August 1, 2016)](https://techcrunch.com/2016/08/01/selfycart-launch-y-combinator/)
5. [Y Combinator — Selfycart company directory](https://www.ycombinator.com/companies/selfycart)
6. [ContactOut — Sahle Hashelit LinkedIn data](https://contactout.com/Sahle-Hashelit-2448334)
7. [Tracxn — Selfycart company profile](https://tracxn.com/d/companies/selfycart/__bsBV9GJxo-vEiWX8GRZBSkzCWaMeQzRKtWKhbNsnoNQ)
8. [TechCrunch — YC Demo Day 2 Summer 2016 coverage (August 23, 2016)](https://techcrunch.com/2016/08/23/yc-demo-day/)
9. [CB Insights — Selfycart company profile](https://www.cbinsights.com/company/selfycart)
10. [Crunchbase — Selfycart organization profile](https://www.crunchbase.com/organization/selfycart)
11. [PitchBook — Selfycart company profile](https://pitchbook.com/profiles/company/163497-52)
12. [Hacker News — Selfycart (YC S16) Is Hiring Sr. Software Engineer – Full Stack (September 12, 2016)](https://news.ycombinator.com/item?id=12477379)
13. [43North — Governor Cuomo Announces Finalists for 4th Annual 43North Competition](https://43north.org/governor-cuomo-announces-finalists-selected-for-4th-annual-43north-competition/)
14. [@selfycart Twitter account](https://twitter.com/selfycart)
15. [@sahle Twitter account](https://twitter.com/sahle)
16. [AppRecs — Selfycart Mobile Self-checkout iOS app listing](https://apprecs.com/ios/1045813000/selfycart-mobile-self-checkout)
17. [Wayback Machine — Selfycart.com archived homepage, December 2016](https://web.archive.org/web/20161228000000/https://www.selfycart.com/)
