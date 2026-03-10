# Research Report: Brace

## Overview

Cole Krumbholz arrived at Y Combinator's Winter 2012 batch with a specific technical frustration and a track record of shipping consumer products. Before Backlift, he had founded Koduco Games, where he designed and built iOS games that accumulated over one million downloads. <sup><a href="https://clay.earth/profile/cole-k">[3]</a></sup> That experience gave him credibility as a builder but also exposed a recurring pain point: every new project required standing up server infrastructure before writing a single line of product code.

Krumbholz was one of YC's rare solo founders — a structural choice that would define both the company's agility and its eventual ceiling. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[4]</a></sup> He entered the batch with a product called Backlift, which he later described simply: "In 2012 I launched something called Backlift, which was a platform for single-page apps using Backbone.js." <sup><a href="https://sacra.com/research/cole-krumbholz-formspree-jamstack/">[5]</a></sup>

The insight behind Backlift was that front-end developers — people who wrote HTML, CSS, and JavaScript — were increasingly capable of building sophisticated web applications, but were blocked by the operational overhead of backend infrastructure. Setting up a server, configuring a database, managing deployments: none of this was front-end work, yet all of it was required before a front-end developer could ship anything. Backlift proposed to eliminate that overhead entirely. A Dropbox account and a text editor were all a user needed to get started. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[6]</a></sup>

The company was incorporated as Sendspree Inc. — a name that suggests an even earlier, undocumented product concept that predated Backlift. No public record explains the Sendspree name or what it was intended to become. By the time the company entered YC, it was operating entirely as Backlift.

After YC, Krumbholz also joined Heavybit, a San Francisco accelerator specifically focused on developer tools companies. <sup><a href="https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting">[7]</a></sup> The dual-accelerator path — YC for capital and network, Heavybit for developer-tools-specific mentorship — suggests Krumbholz was deliberate about positioning Backlift as infrastructure, not just a consumer product.

The initial vision was expansive. By May 2013, Krumbholz was articulating an ambition for Backlift to become "something akin to WordPress, where developers could use the service as a canvas to create new apps and make them available through a built-in repository." <sup><a href="https://techcrunch.com/2013/05/28/backlift-the-yc-backed-back-end-service-for-front-end-developers-launches-ab-testing-service/">[8]</a></sup> That vision never materialized. By late 2013, the company had rebranded to Brace and narrowed its focus significantly — from a platform for developers to a hosting service for designers. Two rebrands in roughly two years signal a founder in active strategic search, not one executing a clear roadmap.

---

## Founding Story

## Timeline

- **2012** — Cole Krumbholz enters Y Combinator Winter 2012 batch with Backlift. Company raises $120K seed from YC. Incorporated as Sendspree Inc. <sup>[[9]](https://tracxn.com/d/companies/brace/__3xHuH3sQMB_a9TqHRQpLohrSWOA8MCuce4fFQLKYX6s)</sup>

- **2012–2013** — Krumbholz joins Heavybit, a developer-tools-focused accelerator in San Francisco, alongside the YC program. <sup>[[7]](https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting)</sup>

- **April 10, 2013** — Backlift launches publicly as a free service. TechCrunch covers the launch. Automatic.com (a fellow YC company) cited as a notable early user. <sup>[[6]](https://techcrunch.com/2013/04/10/yc-backlift-launch/)</sup>

- **May 28, 2013** — Backlift launches Airfoil, an A/B testing service for landing pages, described as a showcase of the Backlift platform. Krumbholz articulates the WordPress-as-canvas vision publicly. <sup>[[8]](https://techcrunch.com/2013/05/28/backlift-the-yc-backed-back-end-service-for-front-end-developers-launches-ab-testing-service/)</sup>

- **September 15, 2013** — Brace beta surfaces publicly. Gizmodo covers it. Hacker News community notices a Backlift support email address in the Brace demo video, identifying the rebranding. <sup>[[10]](https://gizmodo.com/brace-aims-to-screw-up-proof-website-hosting-1318503087)</sup>

- **October 2013** — Brace enters beta. By the December launch, the service will have hosted more than 2,000 websites. <sup>[[11]](https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting)</sup>

- **October 21, 2013** — Krumbholz reaches out to DNSimple on Twitter to set up custom domain support for Brace.io, a real-time glimpse into the pre-launch product-building phase.

<media-tweet url="https://twitter.com/colevscode/status/392409605969412097" author="@colevscode" date="2013-10-21" text="@dnsimple How is this going? We'd love to set up a service for http://www.brace.io"></media-tweet>

- **December 12, 2013** — Brace officially launches as a Dropbox-powered static site hosting service with subscription pricing ($2.99–$49.99/month). <sup>[[11]](https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting)</sup>

- **November 17, 2014** — Squarespace acquires Brace in an acqui-hire. Service immediately stops accepting new users. Existing users given until January 19, 2015 to migrate. Free tools open-sourced. <sup>[[12]](https://vator.tv/news/2014-11-17-squarespace-scoops-up-website-building-service-braceio)</sup>

- **January 19, 2015** — Brace.io service shuts down completely. Paying customers receive refunds, three months of Site44 service, and one year of Squarespace Unlimited. <sup>[[13]](https://wiki.archiveteam.org/index.php/Brace.io)</sup>

- **July 2018** — Cole Krumbholz leaves Squarespace after nearly four years as Engineering Lead and then Product Manager on their developer platform. <sup>[[14]](https://contactout.com/Cole-Krumbholz-2624154)</sup>

- **2018** — Krumbholz co-founds Formspree, a form-handling API, building directly on the forms.brace.io tool created during the Brace era. <sup>[[15]](https://sacra.com/research/cole-krumbholz-formspree-jamstack/)</sup>

---

## What They Built

### Backlift (2012–2013)

Backlift's core premise was simple: front-end developers should be able to build and deploy web applications without touching a server. The product used Dropbox as its file system. A developer would install the Backlift client, drop their HTML, CSS, and JavaScript files into a designated Dropbox folder, and Backlift would handle everything else — syncing files, serving them over the web, and providing a live URL. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[6]</a></sup>

The product was technically sophisticated for early 2013. Backlift supported Backbone.js single-page app templates, AngularJS, CoffeeScript, Handlebars templating, Bootstrap-based layouts, and a Google Maps API integration. It also provided a basic data API — a lightweight backend that let front-end apps read and write structured data without a database — and an admin dashboard for managing app state. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[16]</a></sup>

In May 2013, Backlift launched Airfoil, a companion product for A/B testing landing pages. Krumbholz positioned Airfoil as a demonstration of what the Backlift platform could enable: "a great example of what you can do with Backlift." <sup><a href="https://techcrunch.com/2013/05/28/backlift-the-yc-backed-back-end-service-for-front-end-developers-launches-ab-testing-service/">[8]</a></sup> The launch of a monetizable side product within six weeks of the main product's public debut suggests Krumbholz was already searching for revenue paths that the free Backlift core wasn't providing.

<media-image src="https://techcrunch.com/wp-content/uploads/2013/05/plainlogo2-01.png?resize=1200,240" alt="TechCrunch article: Backlift, The YC-Backed Back-End Service For Front-End Developers, Launches A/B Testing Service — May 28, 2013" caption="TechCrunch's coverage of Backlift launching Airfoil, its A/B testing service for landing pages, in May 2013. The article features founder Cole Krumbholz discussing his vision for Backlift becoming 'something akin to WordPress.'"></media-image>

### Brace (Late 2013–2014)

The pivot to Brace narrowed the product's scope considerably. Where Backlift targeted developers building single-page applications, Brace targeted designers and digital agencies who needed to host static websites — HTML, CSS, and image files — without managing FTP credentials or server configurations. Krumbholz described the shift directly: "Then I transitioned to building Brace.io, which was a way to deploy static sites using Dropbox instead of FTP when people still used FTP to upload code." <sup><a href="https://sacra.com/research/cole-krumbholz-formspree-jamstack/">[17]</a></sup>

The Brace workflow was designed for simplicity. A user would connect their Dropbox account, place their website files in a designated folder, and Brace would serve them at a custom domain. The product maintained two parallel versions of every hosted site: a Draft version for iteration and client collaboration, and a Production version optimized for performance and scale via Amazon Web Services. <sup><a href="https://tracxn.com/d/companies/brace/__3xHuH3sQMB_a9TqHRQpLohrSWOA8MCuce4fFQLKYX6s">[18]</a></sup> The "Ship It" button — which promoted a Draft site to Production — became the product's signature interaction, noted explicitly in Gizmodo's beta coverage. <sup><a href="https://gizmodo.com/brace-aims-to-screw-up-proof-website-hosting-1318503087">[10]</a></sup>

Krumbholz articulated the designer-centric value proposition at launch: "We let you host your web design from the comfort of Dropbox. Designers need tools that help them see how a design works online, collaborate easily and publish in seconds. That's what Brace was designed to do." <sup><a href="https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting">[19]</a></sup>

Alongside the core hosting product, Brace built three free companion tools: forms.brace.io (a form submission handler), charts.brace.io (a data visualization tool), and data.brace.io (a lightweight data API). <sup><a href="https://wiki.archiveteam.org/index.php/Brace.io">[13]</a></sup> These tools extended Brace's utility for static sites that needed dynamic functionality — and, as it turned out, seeded the product that would become Krumbholz's next company.

<media-image src="https://web.archive.org/web/20140601120000im_/http://brace.io/" alt="Archived Brace.io homepage from mid-2014 showing Dropbox-powered static site hosting product" caption="Archived snapshot of the Brace.io homepage (circa mid-2014), showing the product's clean interface and Dropbox-based hosting pitch before the Squarespace acquisition in November 2014."></media-image>

What distinguished Brace from alternatives like GitHub Pages or Amazon S3 static hosting was the Dropbox integration and the designer-friendly workflow. GitHub Pages required command-line familiarity and Git knowledge. S3 required AWS credentials and bucket configuration. Brace required neither. The tradeoff was that Brace's entire value proposition rested on Dropbox's continued support for public folder hosting — a dependency that would prove structurally fragile.

<media-hn url="https://news.ycombinator.com/item?id=6393216" title="Brace – Host your website from Dropbox" points="" comments=""></media-hn>

---

## Market Position

### Target Customers

Backlift's initial target was front-end developers building single-page applications — specifically those using Backbone.js, AngularJS, and similar JavaScript frameworks in 2012–2013. This was a technically sophisticated but relatively small segment: developers who had outgrown simple HTML hosting but didn't want to manage Node.js or Rails backends. The Automatic.com designer's testimonial — "Backlift is a much easier, faster, and secure way of working on the site as we got it ready for launch and showed investors" <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[20]</a></sup> — suggests the actual use case skewed toward prototyping and pre-launch staging rather than production infrastructure.

Brace's pivot shifted the target customer to designers and digital agencies. These users were less technically demanding — they didn't need a data API or Backbone.js templates — but they were potentially more numerous and more willing to pay for workflow convenience. The $2.99–$49.99/month pricing tiers reflected an agency-oriented model: freelancers on the low end, studios managing multiple client sites on the high end. <sup><a href="https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting">[21]</a></sup>

### Market Size

The static site hosting market in 2013 was not yet a recognized category. The term "Jamstack" wouldn't be coined until 2015 (by Netlify's Mathias Biilmann). The addressable market Brace was competing for — designers and agencies who built static sites and needed hosting — was real but fragmented. Most designers used shared hosting providers (GoDaddy, DreamHost), FTP-based workflows, or WordPress. The market for "Dropbox-powered static hosting" was effectively the market Brace was trying to create, not one it was entering.

The broader web hosting market was large — estimated in the billions globally — but Brace was targeting a narrow workflow-specific niche within it. The professional web design services market in the US was estimated at roughly $38 billion in 2013, but Brace's addressable slice was the subset of that market using static site workflows, which was a fraction of total web design work at the time.

### Competition

In 2013, Brace's direct competition came from several directions:

**GitHub Pages** offered free static site hosting tied to Git repositories. It was free and technically capable, but required Git knowledge and command-line comfort — a meaningful barrier for the designers Brace was targeting.

**Site44** was Brace's closest direct competitor: a Dropbox-powered static site host with nearly identical positioning. Site44 launched in 2012 and was already operational when Brace entered beta. The fact that Squarespace gave departing Brace customers a coupon for Site44 service at acquisition <sup><a href="https://wiki.archiveteam.org/index.php/Brace.io">[13]</a></sup> is a telling acknowledgment that Site44 was the natural migration path — and had been competing for the same users throughout Brace's existence.

**Squarespace, Wix, and Weebly** offered fully managed website building with hosting included. These products targeted non-technical users rather than designers who wrote their own HTML, but they were capturing the broader "easy website" market that Brace was adjacent to. Squarespace's acquisition of Brace was partly a recognition that the developer/designer segment was a gap in their own product.

**Amazon S3** and **Rackspace Cloud Files** offered static file hosting for technically capable users. Cheaper than Brace but with no workflow tooling.

The competitive landscape was not crowded in 2013, but it was about to become so. Netlify launched in 2014 and would go on to define the Jamstack hosting category. Surge.sh launched in 2014 as a command-line static hosting tool. The market Brace was building toward would eventually support multiple well-funded companies — but not until after Brace had already exited.

---

## Business Model

Brace operated on a subscription SaaS model introduced at its December 2013 official launch — roughly 18 months after entering YC. The pricing structure had three tiers: a Prototyping plan at $2.99/month, a Personal plan at $12.99/month, and a Professional plan at $49.99/month. <sup><a href="https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting">[21]</a></sup> All plans included a free trial with no credit card required.

The Backlift phase (April–late 2013) was entirely free, with a vague promise of "premium features later." This deferred revenue validation for over a year after YC entry — a significant strategic cost given the $120K total funding. <sup><a href="https://tracxn.com/d/companies/brace/__3xHuH3sQMB_a9TqHRQpLohrSWOA8MCuce4fFQLKYX6s">[22]</a></sup>

The three free companion tools (forms, charts, data) were never monetized directly. They were positioned as value-adds for the core hosting product. When Squarespace acquired Brace, these tools were open-sourced rather than retained — suggesting they had not become revenue contributors and were treated as community assets rather than commercial products.

No revenue figures were ever disclosed. The generous exit compensation for paying customers (full refunds plus one year of Squarespace Unlimited) <sup><a href="https://wiki.archiveteam.org/index.php/Brace.io">[13]</a></sup> suggests the paying user base was small enough that this was financially immaterial for Squarespace.

---

## Traction

Brace's most concrete traction data point is the 2,000+ websites hosted during the October–December 2013 beta period. <sup><a href="https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting">[11]</a></sup> This is a meaningful early signal — 2,000 sites in roughly two months indicates genuine organic interest — but no conversion data, revenue figures, or post-launch growth metrics were ever disclosed.

During the Backlift phase, the most notable user was Automatic.com, a fellow YC-backed company whose designer used Backlift extensively during the pre-launch phase. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[20]</a></sup> This is a credible reference customer, but it also suggests adoption was concentrated within the YC network rather than spreading to the broader developer market.

The product received press coverage at each major milestone: TechCrunch at the Backlift launch (April 2013), TechCrunch again at the Airfoil launch (May 2013), Gizmodo at the Brace beta (September 2013), and BusinessWire, VentureBeat, The Next Web, and Vator at the official Brace launch (December 2013) and acquisition (November 2014). This coverage cadence indicates a founder who was effective at generating press attention — but press coverage and paying customers are different metrics, and only the former is documented.

The speed of the acquisition — less than 12 months after the official paid launch — and the structure of the exit compensation (full refunds were financially manageable for Squarespace) both imply a paying customer base in the hundreds, not thousands.

---

## Post-Mortem

Brace's failure was not a single catastrophic event. It was the compounding result of structural constraints, a deferred monetization strategy, a platform dependency that was never resolved, and a market that was real but not yet ready to pay for what Brace was selling. The primary cause was financial: a solo founder with $120K in total funding had approximately 12–18 months of runway to reach profitability, and the product's free-first strategy consumed most of that window before revenue validation began.

### Cause 1: $120K in Total Funding Left No Margin for Strategic Error

Brace raised only its $120K YC standard seed — no follow-on round was ever disclosed. <sup><a href="https://tracxn.com/d/companies/brace/__3xHuH3sQMB_a9TqHRQpLohrSWOA8MCuce4fFQLKYX6s">[22]</a></sup> For a solo founder building infrastructure products in San Francisco, this was an extremely tight constraint. Developer infrastructure companies typically require significant time to build trust, accumulate users, and convert them to paid plans. The $120K runway — even with minimal personal expenses — likely covered 12–18 months of operations at most.

Krumbholz spent the first 18 months of that runway building and iterating on a free product. Backlift launched in April 2013 with no monetization. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[6]</a></sup> The pivot to Brace introduced pricing only in December 2013 — roughly 20 months after YC entry. By the time Brace had a paid product in market, the runway was nearly exhausted. The acquisition came less than 12 months after the first dollar of revenue was ever charged.

There is no evidence Krumbholz attempted to raise a Series A or additional seed capital. The absence of any follow-on funding announcement — in an era when YC companies routinely raised $500K–$2M post-batch — suggests either that investors passed or that Krumbholz did not pursue it aggressively. Without additional capital, the company had no path to the scale needed to justify independent operation.

### Cause 2: The Dropbox Dependency Was a Structural Vulnerability, Not Just a Feature

Brace's entire product was built on Dropbox's public folder feature — the ability for Dropbox users to share files publicly via a web URL. This was the product's key differentiator and its most significant technical risk. Dropbox controlled whether the feature existed, how it performed, and whether it would continue to be supported.

Dropbox deprecated its public folder feature for new users in March 2017 and shut it down entirely in September 2017. Brace was acquired in November 2014 — before the deprecation — but the risk was inherent from day one. Site44, Brace's closest competitor, faced the same existential threat and ultimately shut down when Dropbox removed public folders.

At the time of Brace's operation, there is no public evidence that Krumbholz had a contingency plan for Dropbox deprecation or a migration path to a non-Dropbox architecture. The product's positioning — "host your website from the comfort of Dropbox" <sup><a href="https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting">[19]</a></sup> — was so tightly coupled to Dropbox that removing the dependency would have required rebuilding the core product. For a solo founder on minimal runway, that was not a viable option.

### Cause 3: Two Rebrands in Two Years Indicate Strategic Drift Without Resolution

The company operated under three names in roughly two years: Sendspree (incorporated), Backlift (YC entry through late 2013), and Brace (late 2013 through acquisition). Each rename represented a meaningful strategic shift, not just a cosmetic change.

The Backlift-to-Brace pivot narrowed the target customer from developers to designers and reduced the product's technical ambition from a full backend-for-frontend platform to a static site host. This was likely a rational response to weak developer adoption — the Backlift user base appears to have been concentrated within the YC network, with Automatic.com as the most prominent reference customer. <sup><a href="https://techcrunch.com/2013/04/10/yc-backlift-launch/">[20]</a></sup> But the pivot also abandoned the more defensible market position. Developer infrastructure products can build deep switching costs; static site hosting is a commodity.

The rebranding was not cleanly executed. The Hacker News community spotted a Backlift support email address in the Brace demo video at the 0:44 mark, surfacing the connection publicly before Krumbholz had communicated it. <sup><a href="https://gizmodo.com/brace-aims-to-screw-up-proof-website-hosting-1318503087">[10]</a></sup> Gizmodo covered the discovery. This is a minor operational detail, but it reflects the execution pressure of a solo founder managing product, marketing, and communications simultaneously.

The WordPress-as-canvas vision articulated in May 2013 — a platform where developers could build and distribute apps through a built-in repository <sup><a href="https://techcrunch.com/2013/05/28/backlift-the-yc-backed-back-end-service-for-front-end-developers-launches-ab-testing-service/">[8]</a></sup> — was never realized. It was too large a surface area for a solo founder on minimal runway. The pivot to Brace was a necessary narrowing, but it also represented the abandonment of the most ambitious version of the thesis.

### Cause 4: The Market Was Real But Not Yet Ready to Pay

Brace was building for the Jamstack paradigm before the paradigm had a name, a community, or a commercial ecosystem. The tools that would make static site development mainstream — Netlify (2014), Hugo (2013, mainstream by 2016), Gatsby (2015) — were either nascent or nonexistent during Brace's operational period. The developer community that would eventually pay for Jamstack hosting infrastructure was still using WordPress and shared hosting in 2013.

This is not a claim that Brace was "ahead of its time" in a vague sense. The specific missing conditions were: (1) a mature ecosystem of static site generators that made building static sites practical for non-specialists, (2) a developer community that had internalized the performance and security benefits of static hosting, and (3) a CI/CD toolchain that made deploying static sites from Git repositories standard practice. None of these existed at scale in 2013–2014.

Netlify, which launched in 2014 and raised $2.1M in seed funding in 2016, eventually built the category Brace was pointing toward — but with a Git-based workflow, a much larger team, and significantly more capital. Brace's Dropbox-based approach was a reasonable proxy for Git-based deployment in 2013 (when Git was less ubiquitous among designers), but it was a transitional solution rather than a durable architecture.

Krumbholz's own exit statement captures the tension: "While I wish we could have taken our vision further as an independent entity, I believe we can make a bigger impact at Squarespace." <sup><a href="https://wiki.archiveteam.org/index.php/Brace.io">[23]</a></sup> The phrasing "could have taken our vision further" implies the vision was correct but the resources to execute it were not available.

### Cause 5: Solo Founder Execution Limits

Every strategic and operational decision at Brace — product, engineering, marketing, fundraising, customer support — fell to one person. The Airfoil side product (May 2013), the Brace pivot (late 2013), the free companion tools (forms, charts, data), and the Squarespace acquisition negotiation were all executed by Krumbholz alone. <sup><a href="https://clay.earth/profile/cole-k">[24]</a></sup>

This is not a criticism of Krumbholz's capability — his post-Brace career at Squarespace and subsequent founding of Formspree demonstrate sustained technical and product competence. But infrastructure products require simultaneous investment in reliability, developer relations, sales, and product development. A solo founder on $120K cannot staff all four functions. The result was a product that worked, received press coverage, and attracted early users — but could not scale the sales and marketing motion needed to reach the paying customer density required for independent viability.

---

## Key Lessons

- **Platform dependency is a business model risk, not just a technical one.** Brace built its entire value proposition on Dropbox's public folder feature — a third-party capability that Dropbox deprecated in 2017. Any product whose core workflow depends on a feature controlled by another company is one product decision away from obsolescence. The lesson is not to avoid integrations, but to ensure the integration is either contractually protected or architecturally replaceable. Brace had neither.

- **Deferred monetization on minimal runway is a compounding mistake.** Backlift launched free in April 2013 and didn't introduce paid pricing until December 2013 — 20 months after YC entry and with only $120K in total funding. <sup><a href="https://tracxn.com/d/companies/brace/__3xHuH3sQMB_a9TqHRQpLohrSWOA8MCuce4fFQLKYX6s">[22]</a></sup> The free period consumed runway that could have been used to validate willingness to pay, iterate on pricing, and build a paying customer base before the clock ran out. For solo founders with limited capital, charging early — even imperfectly — is a survival mechanism.

- **Narrowing the product to survive can make it harder to raise.** The pivot from Backlift (developer infrastructure) to Brace (static site hosting) was a rational response to weak developer adoption, but it moved the product from a defensible infrastructure position to a commodity hosting market. Investors fund platforms; they are more cautious about hosting businesses. The pivot may have improved short-term user acquisition while simultaneously reducing the company's fundability — a trap that accelerated the path to acquisition.

- **The tools you build to support your product can outlast the product itself.** Brace's forms.brace.io tool — built as a free companion to the core hosting product — became the direct ancestor of Formspree, which Krumbholz co-founded in 2018 and which has become a successful independent business. <sup><a href="https://sacra.com/research/cole-krumbholz-formspree-jamstack/">[15]</a></sup> The lesson is that side tools built to solve adjacent problems for your users sometimes contain more durable value than the core product. Paying attention to which free tools get the most organic adoption can reveal the next product.

- **Correct market timing requires sufficient capital to wait for the market.** Brace identified the Jamstack paradigm in 2012–2013, roughly two to three years before it became a recognized category with commercial infrastructure. The thesis was right; the runway was not long enough to survive until the market caught up. Netlify raised $2.1M in seed funding and $12M in Series A before the Jamstack market reached scale. Brace had $120K. Being early to a correct insight is only valuable if you have the capital to remain operational until the market arrives.

---

## Sources

1. [YC Company Directory: Brace](https://www.ycombinator.com/companies/brace)
2. [Archive Team Wiki: Brace.io](https://wiki.archiveteam.org/index.php/Brace.io)
3. [Clay.earth: Cole Krumbholz profile](https://clay.earth/profile/cole-k)
4. [TechCrunch: Backlift Launch, April 10, 2013](https://techcrunch.com/2013/04/10/yc-backlift-launch/)
5. [Sacra: Cole Krumbholz / Formspree / Jamstack interview](https://sacra.com/research/cole-krumbholz-formspree-jamstack/)
6. [BusinessWire: Brace Official Launch Press Release, December 12, 2013](https://www.businesswire.com/news/home/20131212006328/en/Brace-Introduces-Designer-Friendly-Website-Hosting)
7. [TechCrunch: Backlift Launches Airfoil A/B Testing, May 28, 2013](https://techcrunch.com/2013/05/28/backlift-the-yc-backed-back-end-service-for-front-end-developers-launches-ab-testing-service/)
8. [Tracxn: Brace company profile](https://tracxn.com/d/companies/brace/__3xHuH3sQMB_a9TqHRQpLohrSWOA8MCuce4fFQLKYX6s)
9. [Gizmodo: Brace Beta Coverage, September 15, 2013](https://gizmodo.com/brace-aims-to-screw-up-proof-website-hosting-1318503087)
10. [Vator: Squarespace Acquires Brace.io, November 17, 2014](https://vator.tv/news/2014-11-17-squarespace-scoops-up-website-building-service-braceio)
11. [ContactOut: Cole Krumbholz career history](https://contactout.com/Cole-Krumbholz-2624154)
12. [VentureBeat: Squarespace Acquires Brace, November 17, 2014](https://venturebeat.com/business/squarespace-buys-dropbox-powered-site-builder-brace-to-expand-its-developer-tools/)
13. [The Next Web: Squarespace Acquires Brace, November 17, 2014](https://thenextweb.com/insider/2014/11/17/squarespace-acquires-brace-io-bolster-developer-tools/)
14. [Hacker News: Brace – Host your website from Dropbox](https://news.ycombinator.com/item?id=6393216)
