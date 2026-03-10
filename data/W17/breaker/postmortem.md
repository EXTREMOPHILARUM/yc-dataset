# Research Report: Breaker

## Overview

Breaker's founding team was unusually credentialed for a consumer app startup. Erik Berlin had co-founded 140 Proof, a social advertising company that was later acquired by Acuity, and had worked at SoundCloud—a platform that had already demonstrated how social layers could transform audio consumption.<sup><a href="https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/">[1]</a></sup> Leah Culver brought an equally relevant background: she had founded Pownce and Grove, co-authored the OAuth and oEmbed web standards, and had worked at both Dropbox and Twitter.<sup><a href="https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/">[2]</a></sup> These were not first-time founders experimenting with a new medium—they were operators who had built social products and understood audio platforms from the inside.

The founding insight came from two directions converging. Berlin, during his time at SoundCloud, had become convinced that podcasting had significant room to grow and was underexploited as a social medium.<sup><a href="https://www.templarbit.com/blog/2018/07/16/the-engineering-hangout-with-erik-berlin-turning-a-side-project-into-a-social-podcasting-company/">[3]</a></sup> Culver arrived at the problem from a listener's frustration. As she described it: "I started listening to podcasts when I was running. I was kind of happy with the existing players but I was having a hard time with discovery. I didn't find the existing directories of podcast to be particularly relevant to me."<sup><a href="https://www.ycombinator.com/blog/founder-stories-leah-culver-of-breaker">[4]</a></sup> When Culver reached out to Berlin about building a podcasting app, the two founders' complementary perspectives—platform growth and listener experience—aligned naturally.

The founders made one significant and correct pivot before launch. Their original plan was to build tools for podcasters—a creator-side product. Customer discovery killed that thesis quickly. As Culver explained: "Our initial direction wasn't the direction we ended up going in. I was interested in building tools for podcasters. Then when we started talking to podcasters we realized that podcasters just want listeners and data about those listeners. Just providing good tools didn't really solve that problem."<sup><a href="https://www.ycombinator.com/blog/founder-stories-leah-culver-of-breaker">[5]</a></sup> The team redirected toward the listener side of the market—a pivot that demonstrated genuine customer discovery discipline before the product was built.

Execution was deliberately capital-light from the start. The founders built the MVP as a weekend side project without leaving their day jobs. Berlin later described the approach: "if you do it the way Leah and I did we didn't even quit our day jobs... it basically cost us nothing, just our time to build that first version of the product."<sup><a href="https://www.templarbit.com/blog/2018/07/16/the-engineering-hangout-with-erik-berlin-turning-a-side-project-into-a-social-podcasting-company/">[6]</a></sup> Culver echoed the philosophy: "Build things on the side. Honestly mostly build Breaker on Sundays. We iterated on the product for months before leaving our jobs. You don't have to quit your job to do a startup."<sup><a href="https://www.ycombinator.com/blog/founder-stories-leah-culver-of-breaker">[7]</a></sup>

Breaker entered Y Combinator's Winter 2017 batch, receiving early funding and the YC network's validation.<sup><a href="https://www.ycombinator.com/companies/breaker">[8]</a></sup> The company launched publicly in March 2017.

<media-hn url="https://news.ycombinator.com/item?id=13925418" title="Founder Stories: Leah Culver of Breaker (YC W17)" points="" comments=""></media-hn>

---

## Founding Story

## Timeline

- **2016** — Erik Berlin and Leah Culver found Breaker in San Francisco, building the MVP as a weekend side project without leaving their day jobs.<sup>[[6]](https://www.templarbit.com/blog/2018/07/16/the-engineering-hangout-with-erik-berlin-turning-a-side-project-into-a-social-podcasting-company/)</sup>

- **2016** — Founders pivot initial thesis: original plan to build podcaster tools is abandoned after customer discovery reveals podcasters want listeners and data, not tools. Pivot to listener-side social discovery app.<sup>[[5]](https://www.ycombinator.com/blog/founder-stories-leah-culver-of-breaker)</sup>

- **January 2017** — Breaker enters Y Combinator's Winter 2017 (W17) batch, receiving early funding.<sup>[[8]](https://www.ycombinator.com/companies/breaker)</sup>

- **March 2017** — Breaker launches publicly as "the social podcast app" for iOS, with episode likes, comments, friend activity feeds, and social sharing.<sup>[[9]](https://podnews.net/update/breakertwitterfuntimes)</sup>

- **March 2017** — At YC Demo Day, Breaker reports a 67% one-month retention rate for beta users.<sup>[[10]](https://www.ycombinator.com/companies/breaker)</sup>

- **2017** — Breaker raises Seed funding; round size and investors not publicly disclosed.<sup>[[11]](https://pitchbook.com/profiles/company/178889-77)</sup>

- **July 2018** — Erik Berlin gives engineering interview describing the side-project founding approach and the social podcasting vision.<sup>[[6]](https://www.templarbit.com/blog/2018/07/16/the-engineering-hangout-with-erik-berlin-turning-a-side-project-into-a-social-podcasting-company/)</sup>

- **August 2019** — Breaker launches Android beta, ending over two years as an iOS-exclusive product.<sup>[[12]](https://yourstory.com/2020/01/breaker-social-podcast-app-instagram-google-play-store-product-hunt)</sup>

- **January 4, 2021** — Twitter announces acqui-hire of Breaker team (Berlin, Culver, and head of design Emma Lundin) to build Twitter Spaces. App scheduled to shut down January 15, 2021. Price undisclosed.<sup>[[13]](https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/)</sup>

- **January 5, 2021** — Erik Berlin publishes acquisition blog post reframing Breaker's journey and announcing the Twitter Spaces mission.<sup>[[14]](https://www.tubefilter.com/2021/01/05/twitter-spaces-acquires-podcast-app-breaker/)</sup>

- **January 12, 2021** — After a 72-hour negotiation, Maple Media acquires Breaker's app assets, preventing shutdown. Price undisclosed.<sup>[[15]](https://dot.la/breaker-podcast-2649943995.html)</sup>

- **2021** — Maple Media strips all social features from Breaker and relaunches it as a reskin of Player FM, effectively ending the social podcasting product.<sup>[[16]](https://www.tapsmart.com/apps/review-breaker-podcasts/)</sup>

---

## What They Built

Breaker was a full-featured podcast player with a social layer built on top. The core listening experience was functionally equivalent to established apps: users could search for any of the hundreds of thousands of podcasts available through public RSS feeds, subscribe to shows, download episodes for offline listening, and control playback speed. That baseline was table stakes. The differentiation lived in what happened around the listening.

<media-image src="https://techcrunch.com/wp-content/uploads/2021/01/breaker-app.jpg" alt="Breaker social podcast app interface screenshot from TechCrunch acquisition article" caption="TechCrunch's header image from the January 2021 article covering Twitter's acquisition of Breaker, showing the app's social podcast interface."></media-image>

The social features worked as follows. Users created profiles and could follow friends, public figures, or anyone else on the platform. When a user listened to an episode, that activity appeared in their followers' feeds—similar to how Spotify's friend activity sidebar shows what someone is currently playing. Users could "like" individual episodes and leave timestamped comments on specific moments within an episode, creating a lightweight annotation layer on top of audio content. New podcast discovery happened through this social graph: if three people you follow all liked the same episode of an obscure show, that signal surfaced in your feed as a recommendation.<sup><a href="https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/">[17]</a></sup>

The product also included a monetization tool called "Upstream"—described as a Gumroad-style pay platform for podcasters. Upstream allowed creators to sell access to premium episodes individually or bundle them into a subscription. Breaker's own business model included a $6-per-month subscription tier for exclusive content deals the company signed directly with podcasters.<sup><a href="https://www.ycombinator.com/companies/breaker">[18]</a></sup> The company also provided podcast hosting, sharing tools, and listener analytics for creators.<sup><a href="https://www.tubefilter.com/2021/01/05/twitter-spaces-acquires-podcast-app-breaker/">[19]</a></sup>

<media-image src="https://www.androidpolice.com/wp-content/uploads/2019/08/breaker-android-screenshots.jpg" alt="Breaker Android beta app screenshots showing Home, Library, Search, Activity, and Profile tabs" caption="Screenshots of Breaker's Android beta (2019) from Android Police, showing the five-tab navigation bar, social features including episode likes and comments, and the playback screen."></media-image>

The app launched on iOS in March 2017 and remained iOS-only for more than two years. An Android beta arrived in August 2019.<sup><a href="https://yourstory.com/2020/01/breaker-social-podcast-app-instagram-google-play-store-product-hunt">[12]</a></sup> This platform gap was a meaningful constraint: Android accounts for the majority of global smartphone users, and the social features that defined Breaker's value proposition required a critical mass of users on the same platform to function. A friend network split across iOS and Android—where Android users couldn't participate—directly undermined the social discovery flywheel.

The product was frequently described externally as "the Instagram of Podcasts."<sup><a href="https://www.businessofbusiness.com/articles/what-is-twitter-spaces-fleets-breaker-acquisition-explained-podcast-audio/">[20]</a></sup> The analogy captured the aspiration but also exposed the core structural tension: Instagram's social layer is the content. A photo exists only within the app where it was posted. Breaker's social layer sat on top of content—podcast audio—that was freely and identically accessible in Apple Podcasts, Spotify, Overcast, Pocket Casts, and dozens of other apps. The underlying content created no lock-in.

---

## Market Position

### Target Customers

Breaker targeted podcast listeners who were already active consumers of the medium but frustrated by discovery. The ideal user was someone who listened regularly, had friends who also listened, and wanted to share and discuss shows the way they might share articles or music. The secondary customer was the podcaster seeking listener data and a monetization channel beyond advertising—addressed through the Upstream platform and analytics tools.

The social discovery thesis required a specific type of user: one who was willing to make their listening activity public and engage with others' listening activity. This is a narrower behavioral profile than simply "podcast listener." Heavy podcast consumers—who often listen during commutes, workouts, or household tasks—are not necessarily inclined to engage socially around that consumption. The product needed users who were both active listeners and active social participants, a Venn diagram intersection that may have been smaller than the founding team anticipated.

### Market Size

The podcasting market was genuinely growing when Breaker launched. The broader thesis—that podcasting was underexploited and had room to expand—was correct. Spotify's aggressive acquisitions beginning in 2019 (Anchor, Gimlet, Parcast) validated that major platforms saw significant value in the space. By the time of Breaker's acquisition in January 2021, the podcast market had attracted hundreds of millions of dollars in investment and platform attention.

However, market growth benefited incumbents with distribution advantages more than it benefited a standalone social app. Apple Podcasts was pre-installed on every iPhone. Spotify was already the dominant music streaming platform and could cross-promote podcasts to its existing user base. The growing market raised the competitive bar rather than creating an opening for a social-first challenger.

### Competition

Breaker competed against a set of opponents with structural advantages it could not overcome.

Apple Podcasts was pre-installed on every iPhone and required no download decision. It was free, functional, and the default choice for the majority of iOS podcast listeners. Overcast and Pocket Casts competed on audio quality features—smart speed, voice boost, chapter support—and had established user bases with strong retention among power listeners. Spotify entered podcasting aggressively from 2019 onward, acquiring Anchor (podcast creation and hosting), Gimlet (premium content), and Parcast (true crime), giving it both a creation-to-consumption pipeline and the ability to cross-promote podcasts to hundreds of millions of existing music subscribers.

By early January 2021, Breaker had accumulated 4,210 App Store ratings—a 9% increase over 2020. Anchor, owned by Spotify, had 83,000 reviews. Audible had 3.2 million.<sup><a href="https://www.businessofbusiness.com/articles/what-is-twitter-spaces-fleets-breaker-acquisition-explained-podcast-audio/">[21]</a></sup> These numbers are not a direct measure of active users, but they indicate relative scale. Breaker never achieved the user density that its social features required to function as intended. A social feed populated by a small number of friends who are also Breaker users is a weak discovery signal. The network effect that would have made Breaker's social layer valuable required a scale the company never reached.

---

## Business Model

Breaker pursued two revenue streams, neither of which achieved disclosed scale.

The primary model was a $6-per-month subscription that gave users access to exclusive podcast content the company licensed directly from creators.<sup><a href="https://www.ycombinator.com/companies/breaker">[18]</a></sup> This positioned Breaker as a premium content destination rather than a pure utility—a meaningful strategic choice, since exclusive content could theoretically create switching costs that free social features could not.

The secondary model was Upstream, a creator monetization platform that allowed podcasters to sell individual episodes or subscription access to their content directly through Breaker.<sup><a href="https://www.tubefilter.com/2021/01/05/twitter-spaces-acquires-podcast-app-breaker/">[19]</a></sup> Upstream functioned as a marketplace, with Breaker presumably taking a transaction fee. This model required both a listener base willing to pay for podcast content and a creator base willing to distribute premium content through Breaker rather than through their own RSS feeds or established platforms.

No revenue figures, subscriber counts, or transaction volumes were ever publicly disclosed for either model. The company raised a Seed round in 2017, with PitchBook recording $150K in total funding—likely reflecting only the YC check.<sup><a href="https://pitchbook.com/profiles/company/178889-77">[11]</a></sup> The team remained at approximately five employees through the acquisition.<sup><a href="https://pitchbook.com/profiles/company/178889-77">[22]</a></sup>

---

## Traction

The clearest traction data point available is from YC Demo Day in March 2017: Breaker reported a 67% one-month retention rate among beta users.<sup><a href="https://www.ycombinator.com/companies/breaker">[10]</a></sup> This was a strong early signal—retention above 60% at one month is competitive for a consumer app—but it reflected a small, self-selected beta cohort rather than a general market.

By January 2021, Breaker had indexed 700,000 shows on its platform.<sup><a href="https://dot.la/breaker-podcast-2649943995.html">[23]</a></sup> This was a catalog metric, not a user metric—podcast RSS feeds are publicly available and indexing them requires no user engagement. The 4,210 App Store ratings accumulated over nearly four years of operation provide the most honest proxy for relative scale.<sup><a href="https://www.businessofbusiness.com/articles/what-is-twitter-spaces-fleets-breaker-acquisition-explained-podcast-audio/">[21]</a></sup> The 9% growth in ratings during 2020—a year when podcast consumption broadly increased due to pandemic-driven behavior changes—suggests the product was not accelerating meaningfully even in a favorable macro environment.

No monthly active user figures, social feature engagement rates (likes per episode, comments per episode), or revenue metrics were ever disclosed publicly. The absence of disclosed metrics across nearly four years of operation is itself informative: companies that achieve meaningful scale typically share those numbers.

---

## Post-Mortem

### The Social Layer Required Network Density It Never Achieved

The foundational problem was structural. Breaker's social features—friend activity feeds, episode likes, comments—only delivered value when a user's social graph was also on Breaker. A podcast recommendation from a friend you follow is a high-quality signal. A podcast recommendation from an algorithmic directory is a weaker one. That was the correct insight. But it required that friends be on Breaker in the first place.

Breaker launched in March 2017 into a market where Apple Podcasts was pre-installed on every iPhone and Overcast had already established a loyal base of power listeners. Convincing a user to switch podcast apps is a meaningful ask—it requires migrating subscriptions, rebuilding listening history, and changing a habitual behavior. Convincing that user's entire social graph to make the same switch simultaneously is exponentially harder. Without a dense friend network on the platform, the social feed was sparse. A sparse social feed made the app's core differentiator feel inert. The product needed scale to deliver its value proposition, but couldn't deliver its value proposition without scale—a classic cold-start problem that Breaker never solved.

By January 2021, the 4,210 App Store ratings accumulated over nearly four years indicated the company had not broken through to mainstream adoption.<sup><a href="https://www.businessofbusiness.com/articles/what-is-twitter-spaces-fleets-breaker-acquisition-explained-podcast-audio/">[21]</a></sup> No user growth figures were ever disclosed, which is consistent with a product that did not achieve the scale its founders had hoped for.

### Podcast Listening Resisted Social Ritualization

Even if Breaker had achieved greater user density, a deeper behavioral problem remained. Podcast listening is structurally different from the media types where social layers have succeeded.

Music listening has natural social contexts: shared playlists, concert culture, real-time listening with friends. Video has established reaction and commentary culture—YouTube comments, live streaming, watch parties. Podcasting is predominantly a solitary, mobile, background activity. People listen while running, commuting, cooking, or doing household tasks. These are not contexts that invite simultaneous social engagement. The asynchronous nature of podcast consumption means that even if two friends both listen to the same episode, they likely do so days apart, in different contexts, with no natural moment of shared experience to anchor a social interaction.

The Every.to post-mortem articulated this problem precisely: Breaker's social features "felt more like sprinkles than cake, or even icing"—useful but not indispensable—and "people don't seek out recommendations for more content as often as they want to talk to friends."<sup><a href="https://every.to/divinations/a-post-mortem-for-social-podcast-discovery">[24]</a></sup> Social content recommendation apps face a fundamental frequency problem: the behavior they're trying to amplify (seeking new content) happens less often than the behavior that makes pure social apps sticky (communicating with people you know). Breaker needed users to engage socially around podcast content regularly enough to make the social graph feel alive. The underlying consumption behavior didn't support that frequency.

### Two Years of iOS Exclusivity Constrained the Addressable Network

Breaker launched on iOS in March 2017 and did not release an Android beta until August 2019—a gap of over two years.<sup><a href="https://yourstory.com/2020/01/breaker-social-podcast-app-instagram-google-play-store-product-hunt">[12]</a></sup> For a social app, platform exclusivity is a direct constraint on network density. Android accounts for the majority of global smartphone users. More importantly, a social app's value is determined by who is on it, not just how many people are on it. If a user's friends included Android users—which, statistically, most users' friend groups did—those friends were excluded from Breaker's social graph entirely.

This was not an insurmountable problem for a utility app. For a social app whose core value proposition depended on friend networks, it was a significant self-imposed constraint during the period when the company most needed to grow its network. The team's decision to remain iOS-only likely reflected resource constraints—a team of approximately five people building and maintaining two native mobile apps simultaneously is a significant engineering burden—but the cost to the social flywheel was real.

### The Commodity Substrate Eliminated Switching Costs

Breaker's social features sat on top of content that was freely and identically available in every competing app. Podcast audio is distributed via open RSS feeds. Any app can access any podcast. There is no content exclusivity in the standard podcast ecosystem.

This meant Breaker had no content moat. A user who wanted to listen to a specific podcast could do so in Apple Podcasts, Spotify, Overcast, or Pocket Casts without any degradation in the listening experience. The only reason to use Breaker was the social layer—and the social layer only worked if your friends were also on Breaker. The company attempted to address this through exclusive content deals and the $6-per-month subscription model, but no details about the scale of those deals or subscriber counts were ever disclosed, suggesting they did not achieve meaningful traction.<sup><a href="https://www.ycombinator.com/companies/breaker">[18]</a></sup>

The Maple Media outcome is the most direct evidence of this dynamic. When Maple Media acquired Breaker's app assets in a 72-hour negotiation to prevent shutdown, it immediately stripped all social features and relaunched the app as a reskin of its existing Player FM product.<sup><a href="https://www.tapsmart.com/apps/review-breaker-podcasts/">[16]</a></sup> A company that acquires podcast apps for their user bases and infrastructure concluded that Breaker's social layer had no value worth preserving. The underlying podcast player—the commodity substrate—was worth keeping. The differentiation was not.

### The Acqui-Hire as Verdict

<media-tweet url="https://x.com/leahculver/status/1346213711237640192" author="@leahculver" date="2021-01-04" text="In work news, I'm joining Twitter to help build @TwitterSpaces! 🥳 While I'll very much miss @breaker, I'm so excited to help create the future of audio conversations."></media-tweet>

Twitter's acquisition of the Breaker team on January 4, 2021 was structured as an acqui-hire—a purchase of talent and technology, explicitly not a purchase of the podcast product or user base.<sup><a href="https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/">[13]</a></sup> TechCrunch described the price as "modest" and noted the deal "fits the general narrative that podcasting services and podcasting content only has so much value."<sup><a href="https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/">[25]</a></sup>

Berlin, Culver, and head of design Emma Lundin joined Twitter to build Twitter Spaces—a live audio product, not a podcast product.<sup><a href="https://www.tubefilter.com/2021/01/05/twitter-spaces-acquires-podcast-app-breaker/">[26]</a></sup> Berlin's acquisition statement reframed the journey: "When we started Breaker, podcast apps were productivity apps, similar to feed readers and to-do lists. Breaker added a social community element with features such as liking and commenting on episodes. We're now inspired to go even further re-imagining how we communicate with each other, beyond the scope of traditional podcasts."<sup><a href="https://www.tubefilter.com/2021/01/05/twitter-spaces-acquires-podcast-app-breaker/">[14]</a></sup>

The pivot from recorded podcast discovery to live audio conversation is telling. Twitter Spaces—like Clubhouse, which launched in 2020—is a synchronous, real-time audio product. It addresses the core behavioral problem that Breaker could not: live audio creates a shared temporal experience that naturally generates social engagement. The founders' skills in building social audio experiences were genuinely valuable. The specific thesis—that social features could transform asynchronous podcast consumption—was not.

---

## Key Lessons

- **Social features require behavioral frequency to sustain network effects.** Breaker's social layer depended on users regularly sharing, liking, and commenting on podcast episodes. But content discovery is a lower-frequency behavior than communication. Users seek new content occasionally; they communicate with friends constantly. Social apps that succeed—Twitter, Instagram, WhatsApp—are built around high-frequency communication behaviors. Breaker tried to build a social network around a low-frequency discovery behavior, which produced a feed that felt sparse even when the user base was growing.

- **Platform exclusivity is a network tax for social apps.** Breaker's two-year iOS exclusivity was a manageable constraint for a utility app but a significant structural problem for a social app. Every Android user in a potential Breaker user's social graph was an excluded node—a gap in the friend network that made the social feed less valuable. For consumer social products, the cost of platform exclusivity compounds: each missing user reduces the value of the network for every existing user.

- **A social layer on a commodity product does not create switching costs.** Breaker's social features sat on top of podcast content that was freely available in every competing app. When Maple Media acquired the app and stripped the social features, the underlying product remained functional—because the commodity substrate (podcast playback) had always been the actual utility. Differentiation that can be removed without degrading core functionality is not differentiation that creates lock-in. Successful social products make the social layer inseparable from the content itself.

- **Early retention metrics from self-selected cohorts can mislead.** Breaker's 67% one-month retention at YC Demo Day was a strong signal from a beta cohort of early adopters who had actively sought out the product.<sup><a href="https://www.ycombinator.com/companies/breaker">[10]</a></sup> That cohort was not representative of the general podcast listener market. Retention metrics from self-selected early users systematically overstate the product's appeal to the broader market, particularly for social apps where the value proposition degrades as the user base expands beyond the enthusiast core.

- **The correct founding pivot does not guarantee the correct product thesis.** Breaker's pre-launch pivot—from podcaster tools to listener discovery—demonstrated genuine customer discovery discipline and was the right call. But the second thesis (social discovery) also ultimately failed to achieve escape velocity. Good process in the early stage reduces but does not eliminate the risk of a wrong product thesis. The founders' instincts about social audio were validated by Twitter Spaces; the specific mechanism (asynchronous social podcast discovery) was not.

---

## Sources

1. [TechCrunch: Twitter acquires social podcasting app Breaker team to help build Twitter Spaces (January 4, 2021)](https://techcrunch.com/2021/01/04/twitter-acquires-social-podcasting-app-breaker-team-to-help-build-twitter-spaces/)
2. [Y Combinator: Breaker company profile](https://www.ycombinator.com/companies/breaker)
3. [PitchBook: Breaker company profile](https://pitchbook.com/profiles/company/178889-77)
4. [Templarbit: The Engineering Hangout with Erik Berlin — Turning a Side Project into a Social Podcasting Company (July 16, 2018)](https://www.templarbit.com/blog/2018/07/16/the-engineering-hangout-with-erik-berlin-turning-a-side-project-into-a-social-podcasting-company/)
5. [Y Combinator Blog: Founder Stories — Leah Culver of Breaker (March 22, 2017)](https://www.ycombinator.com/blog/founder-stories-leah-culver-of-breaker)
6. [Podnews: Breaker, Twitter, and fun times (January 5, 2021)](https://podnews.net/update/breakertwitterfuntimes)
7. [Tubefilter: Twitter Spaces acquires podcast app Breaker (January 5, 2021)](https://www.tubefilter.com/2021/01/05/twitter-spaces-acquires-podcast-app-breaker/)
8. [YourStory: Breaker — the social podcast app Instagram of podcasts on Google Play Store (January 2020)](https://yourstory.com/2020/01/breaker-social-podcast-app-instagram-google-play-store-product-hunt)
9. [The Business of Business: What is Twitter Spaces? Fleets, Breaker acquisition explained (January 6, 2021)](https://www.businessofbusiness.com/articles/what-is-twitter-spaces-fleets-breaker-acquisition-explained-podcast-audio/)
10. [dot.LA: Maple Media acquires Breaker podcast app (January 12, 2021)](https://dot.la/breaker-podcast-2649943995.html)
11. [Every.to: A Post-Mortem for Social Podcast Discovery](https://every.to/divinations/a-post-mortem-for-social-podcast-discovery)
12. [Crunchbase News: VCs like what they are hearing out of the podcasting sector (June 2018)](https://news.crunchbase.com/startups/vcs-like-what-they-are-hearing-out-of-the-podcasting-sector/)
13. [TapSmart: Review — Breaker Podcasts](https://www.tapsmart.com/apps/review-breaker-podcasts/)
14. [Leah Culver on X (January 4, 2021)](https://x.com/leahculver/status/1346213711237640192)
