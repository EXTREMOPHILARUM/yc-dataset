# Research Report: Posterous

## Overview

Posterous launched in 2008 with a genuinely elegant premise: email any content to a single address, and the platform handles the rest—formatting, hosting, and cross-posting to every major social network.That simplicity drove 30% month-over-month growth in 2009 and 15 million monthly unique visitors by 2011.But Posterous never resolved the tension between its original identity as a frictionless publishing tool and its founders' ambition to become "synonymous with posting just like Google is synonymous with search." Feature accumulation eroded the product's clarity.

A late pivot to group sharing—Posterous Spaces—consumed runway and engineering focus without reversing the competitive slide.By March 2012, monthly visitors had collapsed from 15 million to 1.33 million.

Twitter acquired the company in an acqui-hire, and the product shut down exactly one year later.The core failure was strategic drift: Posterous won the simplicity war early, then abandoned its winning position to fight a social networking battle it was never equipped to win.

<report-gallery>
<media-image src="https://i.ytimg.com/vi/GlCKkOp6eZs/hqdefault.jpg" alt="This Week in Startups - Garry Tan, Co-Founder of Posterous - YouTube" caption="Garry Tan, co-founder and the design mind behind Posterous, speaks on This Week in Startups — a moment from the company's ascent, when 30% month-over-month growth made the dream of becoming 'synonymous with posting' feel entirely plausible."></media-image>
<media-image src="https://www.macotakara.jp/archives/2009/09/images/large-s1310284429.jpg" alt="Posterous投稿アプリ「PicPosterous」を試す | iPhone App Store | Mac OTAKARA" caption="PicPosterous, the iPhone app launched in August 2009, captured the product at its purest — point, shoot, email, done. It was the simplicity that drove 15 million monthly visitors, before feature creep and the pivot to 'Spaces' slowly dismantled everything that made it work."></media-image>
</report-gallery>

## Founding Story

Sachin Agarwal and Garry Tan had known each other since 2000 as fraternity brothers at Stanford's Phi Kappa Psi chapter. <sup><a href="https://www.quora.com/How-did-Posterous-co-founders-Garry-Tan-and-Sachin-Agarwal-begin-working-together">[1]</a></sup> Their paths diverged after graduation—Agarwal spent six years as a senior software engineer at Apple, while Tan became employee number ten at Palantir Technologies, where he was a founding member of the engineering team and designed the company's logo, before a stint at Microsoft. <sup><a href="https://thenextweb.com/insider/2012/03/12/twitter-has-acquired-shortform-blogging-company-posterous/">[2]</a></sup> <sup><a href="https://www.ycombinator.com/people/garry-tan">[3]</a></sup> The two reconnected when Agarwal came to Tan with a prototype.

The founding insight was deceptively simple. Agarwal had grown frustrated with the friction of existing blogging platforms—the login screens, the dashboards, the formatting decisions. He built a prototype that accepted content by email and published it automatically. Tan's reaction was immediate: "Email had a certain elegance to it, and nobody had really looked at it as THE way to post." <sup><a href="https://www.geekwire.com/2010/posterous-co-founder-garry-tan-on-getting-out-of-the-corporate-box/">[4]</a></sup>

Two of the product's most consequential design decisions were accidents. Agarwal routed all users through a single shared address—post@posterous.com—not as a deliberate UX choice, but because he did not know how to configure a mail server to assign individual addresses. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[5]</a></sup> A second accident followed: when someone without an account emailed that address, the system automatically created a blog for them on the spot. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[6]</a></sup> Both decisions—born of technical limitation—became viral growth mechanics. New users could publish their first post before they had even registered.

Agarwal and Tan co-founded Posterous in May 2008 alongside Brett Gibson, whose specific role and background are not well documented in the public record. <sup><a href="https://tracxn.com/d/companies/posterous/__9ktGghAfDSBQRGIvg8GPqtv0RE-02CLdK0eAtN_yLEM">[7]</a></sup> The team applied to Y Combinator's Summer 2008 batch, which provided early validation and network access. <sup><a href="https://www.ycombinator.com/blog/yc-founders-at-work-interview-posterous">[8]</a></sup> By December 2008, the company had closed a seed round of approximately $725,000 from XG Ventures, Felicis Ventures, and angel investor Guy Kawasaki. <sup><a href="https://tracxn.com/d/companies/posterous/__9ktGghAfDSBQRGIvg8GPqtv0RE-02CLdK0eAtN_yLEM">[9]</a></sup>

The early vision was expansive. Agarwal articulated a goal that would later prove to be a strategic liability: "Our goal is to become synonymous with posting just like Google is synonymous with search. Doesn't matter if it's for Twitter or a blog, private or public, group or individual—if you need it online, you go to Posterous." <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[10]</a></sup> That ambition was understandable in 2010. In retrospect, it telegraphed the identity crisis that would eventually consume the company.

---

## Timeline

- **May 2008** — Posterous founded by Sachin Agarwal, Garry Tan, and Brett Gibson in San Francisco <sup>[[7]](https://tracxn.com/d/companies/posterous/__9ktGghAfDSBQRGIvg8GPqtv0RE-02CLdK0eAtN_yLEM)</sup>
- **Summer 2008** — Posterous participates in Y Combinator Summer 2008 batch <sup>[[8]](https://www.ycombinator.com/blog/yc-founders-at-work-interview-posterous)</sup>
- **December 2008** — Raises ~$725K seed round from XG Ventures, Felicis Ventures, and Guy Kawasaki <sup>[[9]](https://tracxn.com/d/companies/posterous/__9ktGghAfDSBQRGIvg8GPqtv0RE-02CLdK0eAtN_yLEM)</sup>
- **2009** — Grows 30% month-over-month with only 4 employees <sup>[[11]](https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/)</sup>
- **June 2009** — Acquires Slinkset, a social news site creation tool <sup>[[12]](https://www.crunchbase.com/organization/slinkset)</sup>
- **August 2009** — Launches PicPosterous iPhone app; raises $750K angel round from Satish Dharmaraj and Eric Hahn <sup>[[13]](https://en.wikipedia.org/wiki/Posterous)</sup> <sup>[[14]](https://vator.tv/news/2009-08-21-the-fundraising-behind-posterous)</sup>
- **March 2010** — Raises $4.4M Series A led by Redpoint Ventures; reports 12M unique monthly visitors and 25M page views <sup>[[15]](https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/)</sup>
- **January 2011** — Launches Android app supporting 9 phone models <sup>[[16]](https://en.wikipedia.org/wiki/Posterous)</sup>
- **2011** — Reaches approximately 15 million monthly unique visitors (peak traffic) <sup>[[17]](https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network)</sup>
- **2011** — Garry Tan departs Posterous to become a part-time partner at Y Combinator <sup>[[18]](https://blog.ycombinator.com/welcome-sam-garry-emmett-and-justin/)</sup>
- **September 2011** — Raises $5M Series B from Redpoint and Jafco Ventures (total funding: $10.14M) <sup>[[19]](https://techcrunch.com/2011/09/16/back-to-our-regularly-scheduled-program-posterous-raises-5-million/)</sup>
- **September 2011** — Pivots and relaunches as "Posterous Spaces," a group and private sharing product <sup>[[20]](https://skatter.com/2011/09/posterous-pivots-into-spaces/)</sup>
- **March 12, 2012** — Twitter acquires Posterous in an acqui-hire; 36+ employees join Twitter; monthly visitors have fallen to 1.33M <sup>[[21]](https://techcrunch.com/2012/03/12/posterous-finds-a-home-in-the-arms-of-twitter/)</sup>

<media-hn url="https://news.ycombinator.com/item?id=3695407" title="Posterous acquired by Twitter" points="" comments=""></media-hn>

- **March 14, 2012** — Sachin Agarwal joins Twitter as product manager reporting to product chief Satya Patel <sup>[[22]](https://money.cnn.com/2012/03/14/technology/posterous_twitter/index.htm)</sup>
- **February 15, 2013** — Posterous announces shutdown effective April 30, 2013; Garry Tan simultaneously launches Posthaven <sup>[[23]](https://techcrunch.com/2013/02/15/posterous-will-shut-down-on-april-30th-co-founder-garry-tan-launches-posthaven-to-save-your-sites/)</sup>
- **April 30, 2013** — Posterous shuts down, approximately one year after Twitter acquisition <sup>[[24]](https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/)</sup>

---

## What They Built

Posterous solved a real problem with unusual elegance. In 2008, publishing anything online required navigating a content management system—logging in, choosing a post type, formatting text, uploading attachments, and hitting publish. Posterous eliminated every step except one: composing an email.

A user would write an email to post@posterous.com. The subject line became the post title. The body became the post content. Any attachment—a photo, an MP3, a PDF, a video file—was automatically formatted and hosted by Posterous. The platform then cross-posted the content to whatever social networks the user had connected: Flickr, Twitter, Facebook, and others. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[25]</a></sup> The entire process took as long as it took to write an email.

For first-time users, the experience was even more frictionless. If someone emailed post@posterous.com without an existing account, Posterous automatically created a blog for them and sent a confirmation. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[6]</a></sup> There was no signup form, no password selection, no onboarding flow. The first post was the onboarding.

The platform also included built-in Google Analytics integration and support for custom themes, giving more sophisticated users room to grow without requiring it of casual ones. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[25]</a></sup>

**Mobile expansion.** In August 2009, Posterous launched PicPosterous, an iPhone app optimized for photo posting. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[13]</a></sup> An Android app followed in January 2011, supporting nine phone models. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[16]</a></sup> These releases tracked the smartphone adoption curve and extended the email-first model to native mobile interfaces.

**The Slinkset acquisition.** In June 2009, Posterous acquired Slinkset, a tool for creating social news sites. <sup><a href="https://www.crunchbase.com/organization/slinkset">[12]</a></sup> This was the first signal that the company was thinking beyond personal blogging. Slinkset's social aggregation features were directionally different from Posterous's core use case—individual publishing—and the acquisition foreshadowed the product identity problems that would emerge later.

**Feature accumulation.** Between 2009 and 2011, Posterous added group sharing, private spaces, social following, and a range of content-type-specific features. Each addition made sense in isolation. Collectively, they created a product that new users could not parse. Agarwal later described the result plainly: "New users were confused between the photo sharing blog site and groups. They did not understand what the site did. In addition to that we had added so many new features to the interface that new users became lost. There was no one call to action, there were 50 buttons." <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[26]</a></sup>

**Posterous Spaces.** In September 2011, the company attempted to resolve this confusion with a full relaunch. Posterous Spaces reframed the product around group sharing and private collaboration—users could create distinct "spaces" for different audiences, with granular privacy controls. <sup><a href="https://skatter.com/2011/09/posterous-pivots-into-spaces/">[20]</a></sup> The pivot required a complete rebuild of the codebase, because years of accumulated technical debt made incremental improvement impractical. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[27]</a></sup> That rebuild consumed the engineering team's capacity for months at the precise moment Tumblr was compounding its lead.

What made Posterous different from alternatives was never the feature set—it was the absence of friction. Tumblr offered a richer social graph and a more curated aesthetic. WordPress offered more power and customization. Posterous offered speed. When it stopped being the fastest path from thought to published post, its differentiation collapsed.

---

## Market Position

### Target Customers

Posterous initially targeted individuals who wanted to publish content online without managing a blogging platform. The email interface made it accessible to non-technical users who found WordPress or Blogger intimidating, while the automatic cross-posting appealed to early social media adopters who maintained presences on multiple networks simultaneously.

The platform attracted a disproportionate share of early social media influencers. When prominent blogger Steve Rubel publicly announced he was moving his entire blogging activity to Posterous, it validated the platform's credibility with the tech-adjacent audience that drove early adoption. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[28]</a></sup> Many social media commentators at the time considered Posterous the leading free application for "lifestreaming"—the practice of aggregating one's digital activity into a single stream. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[28]</a></sup>

The Spaces pivot in 2011 attempted to expand the target customer to include teams and groups—a meaningfully different use case requiring different product decisions, different sales motions, and different retention mechanics. The company never demonstrated it had solved for this new customer before the acquisition ended the experiment.

### Market Size

The blogging and content publishing market in 2008–2012 was large but contested. WordPress.com, Blogger, and Tumblr each served tens of millions of users. The addressable market was effectively anyone with internet access who wanted to publish content—a category that was expanding rapidly as smartphone adoption accelerated.

Posterous's peak of approximately 15 million monthly unique visitors placed it in the top 200 sites on Quantcast. <sup><a href="https://nextbn.ggvc.com/podcast/s2-ep-19-garry-tan-of-initialized-saying-no-to-peter-thiel-engineer-turned-investors/">[29]</a></sup> That was a meaningful position in absolute terms. In relative terms, it represented a distant third place in a market where Tumblr and WordPress.com were each approaching 30 million monthly visitors by early 2012. <sup><a href="https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/">[30]</a></sup>

The photo-sharing sub-market—which Posterous touched with PicPosterous—proved to be the highest-growth segment of the period. Instagram launched in October 2010 and reached 10 million users within a year. Posterous had a mobile photo-posting product before Instagram existed, but never concentrated its resources on that use case.

### Competition

**Tumblr** was Posterous's primary competitor and ultimately its executioner. Founded in 2007, Tumblr built a stronger social graph—users could follow each other, reblog content, and discover new creators through a curated dashboard. This social layer created retention mechanics that Posterous lacked. By March 2012, Tumblr had 26 million monthly visitors against Posterous's 1.33 million—a roughly 20-to-1 advantage. <sup><a href="https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/">[30]</a></sup>

**WordPress.com** served the more serious end of the market—bloggers who wanted customization, plugins, and a professional-grade platform. WordPress.com had approximately 30 million monthly visitors by early 2012. <sup><a href="https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/">[30]</a></sup> It was not a direct competitor for Posterous's casual-publishing use case, but it captured the users who outgrew Posterous's simplicity.

**Instagram** represented the competitive threat Posterous never recognized in time. Posterous had launched a mobile photo-posting app in August 2009—more than a year before Instagram—but treated photo sharing as one feature among many rather than as a standalone product category worth dominating.

---

## Business Model

Posterous operated primarily as a free consumer product. The company deliberately kept consumer fees out of the product, prioritizing growth over monetization. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[31]</a></sup>

The company did generate some revenue. An early deal with Coca-Cola for a branded Posterous site demonstrated that enterprise or brand partnerships were a viable path. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[31]</a></sup> However, no public information indicates this became a repeatable revenue line or that the company built a sales function to pursue similar deals systematically.

Total venture funding reached $10.14 million across seed, angel, Series A, and Series B rounds. <sup><a href="https://techcrunch.com/2011/09/16/back-to-our-regularly-scheduled-program-posterous-raises-5-million/">[19]</a></sup> With 21 employees at the time of acquisition and no disclosed revenue figures, the company appears to have been operating on investor capital without a clear path to profitability. The acqui-hire outcome—rather than a strategic acquisition at a premium—suggests investors and founders alike concluded that an independent monetization path was not achievable.

---

## Traction

Posterous's early growth metrics were genuinely strong. In 2009, the company grew 30% month-over-month with just four employees. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[11]</a></sup> By March 2010, when Redpoint led the Series A, the platform had 12 million unique monthly visitors and 25 million page views. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[11]</a></sup> By 2011, monthly unique visitors had grown to approximately 15 million, placing Posterous in the top 200 sites on Quantcast. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[17]</a></sup> <sup><a href="https://nextbn.ggvc.com/podcast/s2-ep-19-garry-tan-of-initialized-saying-no-to-peter-thiel-engineer-turned-investors/">[29]</a></sup>

The platform attracted influential early adopters. Steve Rubel's public migration to Posterous generated press coverage and signaled credibility with the social media community. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[28]</a></sup>

The traffic trajectory then reversed sharply. Between 2011 and the March 2012 acquisition, monthly visitors fell from approximately 15 million to 1.33 million—an 91% decline. <sup><a href="https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/">[30]</a></sup> No public data clarifies whether this decline was driven by failure to acquire new users, accelerated churn among existing users, or both. The Spaces relaunch in September 2011 coincides with the beginning of this period, suggesting the pivot may have confused or alienated the existing user base without successfully attracting a new one.

At acquisition, Posterous had 21 employees. <sup><a href="https://money.cnn.com/2012/03/14/technology/posterous_twitter/index.htm">[32]</a></sup> The team remained small relative to the platform's peak reach, reflecting either disciplined capital efficiency or an inability to scale hiring—the public record does not clarify which.

---

## Post-Mortem

### 1. Identity Erosion: The Product Stopped Knowing What It Was

Posterous's original value proposition was singular and defensible: the fastest path from content to published post. That clarity drove 30% monthly growth in 2009 with four employees. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[11]</a></sup>

The erosion began with the Slinkset acquisition in June 2009. <sup><a href="https://www.crunchbase.com/organization/slinkset">[12]</a></sup> Slinkset was a social news aggregation tool—directionally different from personal publishing. Its acquisition signaled that Posterous was thinking about social content discovery, not just individual expression. Over the following two years, the team added group sharing, private spaces, social following, and a proliferating set of content-type-specific features.

Each addition was individually defensible. Collectively, they destroyed the product's legibility. By 2011, Agarwal acknowledged the result: "New users were confused between the photo sharing blog site and groups. They did not understand what the site did. In addition to that we had added so many new features to the interface that new users became lost. There was no one call to action, there were 50 buttons." <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[26]</a></sup>

The attempted remedy was Posterous Spaces—a September 2011 relaunch that tried to impose a coherent identity on the accumulated feature set by reframing the product around group sharing. <sup><a href="https://skatter.com/2011/09/posterous-pivots-into-spaces/">[20]</a></sup> But the pivot required a complete rebuild because years of accumulated technical debt made incremental refactoring impractical. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[27]</a></sup> The rebuild consumed the engineering team's capacity for months. Monthly visitors fell from 15 million to 1.33 million in the period following the relaunch. <sup><a href="https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/">[30]</a></sup> The pivot did not reverse the decline.

### 2. Fighting the Wrong Competitor While the Real Opportunity Passed

Posterous defined its competitive battle as Posterous versus Tumblr. That framing was understandable—Tumblr was the most visible rival in the microblogging space—but it was strategically costly.

<media-tweet url="https://x.com/garrytan/status/1987547384369557591" author="@garrytan" date="2025-11-09" text="This happened to us at Posterous. We thought we were trying to beat Tumblr. Tumblr didn't even want to be Tumblr. In the end there was no actual enduring value in that. What we really needed to do was be Instagram but it was too late. Too busy beefing with the littles to win."></media-tweet>

Posterous had launched PicPosterous, a mobile photo-posting app, in August 2009—more than fourteen months before Instagram launched in October 2010. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[13]</a></sup> The company had a head start in mobile photo sharing. It did not treat that head start as a strategic priority. Instead, it treated photo sharing as one feature among many and continued building toward the broader "synonymous with posting" vision.

Instagram reached 10 million users within a year of launch and was acquired by Facebook for $1 billion in April 2012—the same month Posterous was being absorbed into Twitter. The opportunity was real. Posterous had the technical capability and the early mobile presence to compete in that space. The team's attention was elsewhere.

Tan's 2025 reflection is the most candid post-mortem available: the team was "too busy beefing with the littles to win." Competing with Tumblr for the microblogging audience meant building social graph features, group sharing, and content discovery tools—all of which pulled resources away from the photo-sharing use case that was about to become the fastest-growing segment of consumer social.

### 3. Co-Founder Departure at a Critical Juncture

Garry Tan left Posterous to become a part-time partner at Y Combinator in 2011, before the Twitter acquisition. <sup><a href="https://blog.ycombinator.com/welcome-sam-garry-emmett-and-justin/">[18]</a></sup> TechCrunch noted his departure explicitly in its acquisition coverage. <sup><a href="https://techcrunch.com/2012/03/12/posterous-finds-a-home-in-the-arms-of-twitter/">[33]</a></sup>

Tan was the co-founder who had articulated the product's philosophical core most clearly. His 2010 statement—"Building the right product requires incredible creativity... On the other hand, it requires great restraint. You can't boil the ocean, and the only way you can get meaningful feedback is by shipping real software" <sup><a href="https://www.geekwire.com/2010/posterous-co-founder-garry-tan-on-getting-out-of-the-corporate-box/">[34]</a></sup>—reads in retrospect as a precise diagnosis of what Posterous failed to maintain. His departure in 2011 coincided with the Spaces pivot, the Series B raise, and the beginning of the traffic collapse.

No public explanation exists for why Tan departed when he did. What is clear is that the company lost a founding voice for restraint at the moment it most needed that restraint. The Spaces pivot—a full rebuild of a product that had accumulated too many features—was the opposite of the philosophy Tan had articulated.

### 4. The Acqui-Hire Outcome: Talent Extracted, Product Abandoned

By March 2012, the independent path was closed. Monthly visitors had fallen to 1.33 million against Tumblr's 26 million and WordPress.com's approximately 30 million. <sup><a href="https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/">[30]</a></sup> Twitter acquired Posterous on March 12, 2012, in a deal whose financial terms were never disclosed. <sup><a href="https://techcrunch.com/2012/03/12/posterous-finds-a-home-in-the-arms-of-twitter/">[21]</a></sup>

Over 36 Posterous employees joined Twitter—described at the time as Twitter's largest new hire class. <sup><a href="https://thenextweb.com/insider/2012/03/12/twitter-has-acquired-shortform-blogging-company-posterous/">[35]</a></sup> Agarwal joined as a product manager reporting to product chief Satya Patel. <sup><a href="https://money.cnn.com/2012/03/14/technology/posterous_twitter/index.htm">[22]</a></sup> No Posterous technology was publicly integrated into Twitter's product.

<media-hn url="https://news.ycombinator.com/item?id=5228997" title="Posterous will turn off on April 30" points="" comments=""></media-hn>

The Hacker News community read the acquisition as a talent extraction with no intent to preserve the product. <sup><a href="https://news.ycombinator.com/item?id=3695407">[36]</a></sup> That reading proved correct. On February 15, 2013, Posterous announced it would shut down on April 30, 2013, to "focus 100% of efforts on Twitter." <sup><a href="https://techcrunch.com/2013/02/15/posterous-will-shut-down-on-april-30th-co-founder-garry-tan-launches-posthaven-to-save-your-sites/">[23]</a></sup>

<media-tweet url="https://x.com/garrytan/status/302591116224651265" author="@garrytan" date="2013-02-15" text="Posterous Will Shut Down On April 30th, Co-Founder Garry Tan Launches Posthaven To Save Your Sites"></media-tweet>

On the same day as the shutdown announcement, Tan launched Posthaven—a paid, promise-to-never-sell blogging service designed to preserve users' Posterous sites. <sup><a href="https://techcrunch.com/2013/02/15/posterous-will-shut-down-on-april-30th-co-founder-garry-tan-launches-posthaven-to-save-your-sites/">[23]</a></sup> The simultaneous launch was an implicit acknowledgment that the acquisition had failed users and that the original product vision deserved a more principled steward. Posthaven's founding premise—a paid service that would never be sold—was a direct repudiation of the path Posterous had taken.

<media-hn url="https://news.ycombinator.com/item?id=5229229" title="Posterous cofounders create a replacement: Posthaven" points="" comments=""></media-hn>

### 5. Monetization Deferred Until It Was Too Late

Posterous kept consumer fees out of the product throughout its life. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-changing-posterous/">[31]</a></sup> The Coca-Cola branded site deal demonstrated that enterprise revenue was possible, but no evidence suggests the company built a repeatable sales motion around it. <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[31]</a></sup>

With $10.14 million in total funding and 21 employees at acquisition, the company had operated for nearly four years without establishing a durable revenue model. <sup><a href="https://techcrunch.com/2011/09/16/back-to-our-regularly-scheduled-program-posterous-raises-5-million/">[19]</a></sup> <sup><a href="https://money.cnn.com/2012/03/14/technology/posterous_twitter/index.htm">[32]</a></sup> When traffic collapsed in 2011–2012, there was no revenue base to sustain operations independently. The acqui-hire was not just a competitive failure—it was the only exit available to a company that had never built a business around its product.

---

## Key Lessons

- **Accidental product decisions can be your best ones—but you have to recognize them as such.** Posterous's two most powerful growth mechanics (the shared inbox and auto-account creation) were accidents born of technical limitation. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[5]</a></sup> <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[6]</a></sup> The founders did not fully recognize these as deliberate design principles to protect. When the company began adding features, it eroded the frictionlessness that had made those accidents work. Identifying *why* your early product works—and treating that as a constraint on future decisions—is harder than it sounds.

- **Defining your competitor defines your product.** Posterous framed its competitive battle as Posterous versus Tumblr and built social graph features, group sharing, and content discovery tools to compete on that terrain. That framing consumed resources that could have gone toward mobile photo sharing—a category where Posterous had a 14-month head start on Instagram. <sup><a href="https://en.wikipedia.org/wiki/Posterous">[13]</a></sup> The competitor you choose to fight determines which product you build. Choosing the wrong competitor can be as fatal as building the wrong product.

- **A full rebuild is a bet-the-company decision, not a product decision.** The Spaces pivot required a complete codebase rebuild because accumulated technical debt made incremental improvement impractical. <sup><a href="https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network">[27]</a></sup> That rebuild consumed the engineering team's capacity for months during the period when Tumblr was compounding its lead. Technical debt is not just an engineering problem—it is a strategic constraint that limits a company's ability to respond to competitive pressure at the moment it most needs to.

- **Expansive vision without a focused product is a liability, not an asset.** Agarwal's stated goal—to become "synonymous with posting just like Google is synonymous with search" <sup><a href="https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/">[10]</a></sup>—was ambitious enough to justify building almost anything. That ambiguity made it impossible to say no to features. The companies that won in adjacent spaces (Tumblr, Instagram) had narrower, more defensible identities. Posterous's vision was broad enough to rationalize every addition and specific enough to commit to none.

- **Posthaven's founding premise was the lesson Posterous learned too late.** Tan launched Posthaven as a paid service with an explicit promise never to sell. <sup><a href="https://techcrunch.com/2013/02/15/posterous-will-shut-down-on-april-30th-co-founder-garry-tan-launches-posthaven-to-save-your-sites/">[23]</a></sup> That structure—charging users directly, aligning incentives with longevity rather than acquisition—was the business model Posterous never built. A small recurring revenue base would have given the company options when traffic declined. Without it, the acqui-hire was the only available outcome.

<media-tweet url="https://x.com/garrytan/status/1681875067880329216" author="@garrytan" date="2023-07-19" text="The Posterous Boys are back"></media-tweet>

---

## Sources

1. [Quora: How did Posterous co-founders Garry Tan and Sachin Agarwal begin working together](https://www.quora.com/How-did-Posterous-co-founders-Garry-Tan-and-Sachin-Agarwal-begin-working-together)
2. [The Next Web: Twitter has acquired shortform blogging company Posterous (March 12, 2012)](https://thenextweb.com/insider/2012/03/12/twitter-has-acquired-shortform-blogging-company-posterous/)
3. [Y Combinator: Garry Tan profile](https://www.ycombinator.com/people/garry-tan)
4. [GeekWire: Posterous co-founder Garry Tan on getting out of the corporate box (September 8, 2010)](https://www.geekwire.com/2010/posterous-co-founder-garry-tan-on-getting-out-of-the-corporate-box/)
5. [ZURB Soapbox: Sachin Agarwal — Posterous from blog to social network](https://zurb.com/soapbox/sachin-agarwal-zurbsoapbox-posterous-from-blog-to-social-network)
6. [Tracxn: Posterous company profile](https://tracxn.com/d/companies/posterous/__9ktGghAfDSBQRGIvg8GPqtv0RE-02CLdK0eAtN_yLEM)
7. [Y Combinator Blog: YC Founders at Work interview — Posterous](https://www.ycombinator.com/blog/yc-founders-at-work-interview-posterous)
8. [Wikipedia: Posterous](https://en.wikipedia.org/wiki/Posterous)
9. [Vator.tv: The fundraising behind Posterous (August 21, 2009)](https://vator.tv/news/2009-08-21-the-fundraising-behind-posterous)
10. [TechCrunch: Redpoint invests $4.4 million in fast-growing Posterous (March 5, 2010)](https://techcrunch.com/2010/03/05/redpoint-invests-4-4-million-in-fast-growing-posterous/)
11. [TechCrunch: Back to our regularly scheduled program — Posterous raises $5 million (September 16, 2011)](https://techcrunch.com/2011/09/16/back-to-our-regularly-scheduled-program-posterous-raises-5-million/)
12. [Skatter: Posterous pivots into Spaces (September 28, 2011)](https://skatter.com/2011/09/posterous-pivots-into-spaces/)
13. [TechCrunch: Posterous finds a home in the arms of Twitter (March 12, 2012)](https://techcrunch.com/2012/03/12/posterous-finds-a-home-in-the-arms-of-twitter/)
14. [CNN Money: Posterous and Twitter (March 14, 2012)](https://money.cnn.com/2012/03/14/technology/posterous_twitter/index.htm)
15. [TechCrunch: Posterous will shut down on April 30th, co-founder Garry Tan launches Posthaven (February 15, 2013)](https://techcrunch.com/2013/02/15/posterous-will-shut-down-on-april-30th-co-founder-garry-tan-launches-posthaven-to-save-your-sites/)
16. [VentureBeat: One year after being acquired by Twitter, Posterous shuts it all down](https://venturebeat.com/social/one-year-after-being-acquired-by-twitter-posterous-shuts-it-all-down/)
17. [Crunchbase: Slinkset](https://www.crunchbase.com/organization/slinkset)
18. [Y Combinator Blog: Welcome Sam, Garry, Emmett, and Justin](https://blog.ycombinator.com/welcome-sam-garry-emmett-and-justin/)
19. [Grokipedia: Garry Tan](https://grokipedia.com/page/Garry_Tan)
20. [Next Big Network / GGVC Podcast: Garry Tan of Initialized — Saying no to Peter Thiel, engineer turned investor](https://nextbn.ggvc.com/podcast/s2-ep-19-garry-tan-of-initialized-saying-no-to-peter-thiel-engineer-turned-investors/)
21. [The American Genius: Posterous team and technology acquired by Twitter](https://theamericangenius.com/posterous-team-and-technology-acquired-by-twitter/)
22. [Vator.tv: Today's entrepreneur — Sachin Agarwal (January 18, 2011)](https://vator.tv/news/2011-01-18-todays-entrepreneur-sachin-agarwal)
23. [Hacker News: Posterous acquired by Twitter (March 2012)](https://news.ycombinator.com/item?id=3695407)
24. [Hacker News: Posterous will turn off on April 30 (February 2013)](https://news.ycombinator.com/item?id=5228997)
25. [Hacker News: Posterous cofounders create a replacement: Posthaven (February 2013)](https://news.ycombinator.com/item?id=5229229)
