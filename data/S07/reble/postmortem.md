# Research Report: Reble

## Overview

## Founding Story

Nick Meyer came to Reble with an unusual credential for a first-time startup founder: he had already built a product used by hundreds of thousands of people. While still in high school, Meyer co-founded Kings of Chaos, a massively multiplayer online game that attracted hundreds of thousands of daily players at its peak.<sup><a href="https://www.startupgrind.com/events/details/startup-grind-boston-presents-nick-meyer-entrepreneur-in-residence-martin-trust-center-for-mit-entrepreneurship/">[4]</a></sup> That experience — building viral, socially networked consumer products before "social" was a product category — shaped the instincts he brought to Reble.

Meyer founded Reble in 2006 during his time at MIT.<sup><a href="https://startmit-2018.mit.edu/meyer/">[5]</a></sup> The founding insight was simple and experientially grounded: the music on your friends' hard drives is one of the best discovery surfaces available, and yet accessing it required either physically sitting at their computer or exchanging files through channels that were legally precarious. Meyer wanted to collapse that gap. As he put it at the time of Reble's public beta launch: *"Playing music on my friend's computer should feel just like playing a song on my hard-drive, and you should be able to add any of your friends' music to playlists."*<sup><a href="https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/">[6]</a></sup>

The legal architecture of the product was as deliberate as the social one. The file-sharing wars of the early 2000s — Napster's shutdown in 2001, the RIAA's litigation campaign against individual users — had made the music industry's posture toward P2P technology clear. Meyer's answer was to build a streaming product, not a downloading one. By transmitting audio in real time rather than transferring files, Reble argued it occupied a legal gray zone distinct from both traditional P2P file sharing and the internet radio royalty regime that burdened services like Pandora. The team engaged the music industry from the very beginning of the company's life, signaling awareness that legal clearance was a prerequisite, not an afterthought.<sup><a href="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/">[7]</a></sup>

Reble joined Y Combinator's Summer 2007 batch as a two-person team.<sup><a href="https://www.ycombinator.com/companies/reble">[8]</a></sup> The identity of the second team member is not documented in any public record. YC's backing was described as partial in Meyer's later biographical materials, suggesting the company did not raise a significant external round beyond the YC investment.<sup><a href="https://startmit-2018.mit.edu/meyer/">[9]</a></sup> The company operated out of San Francisco throughout its life.

## Timeline

- **2006** — Nick Meyer founds Reble while attending MIT, with the concept of legal P2P music streaming from friends' libraries.<sup>[[10]](https://www.ycombinator.com/companies/reble)</sup>

- **June 2007** — Reble joins Y Combinator's Summer 2007 batch as a two-person team; receives partial YC funding.<sup>[[11]](https://www.ycombinator.com/companies/reble)</sup>

- **August 16, 2007** — Reble presents at YC S07 Demo Day. TechCrunch covers the pitch, describing the legal streaming architecture and affiliate sales business model.

<media-hn url="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/" title="Y Combinator Demo Day: The Summer Startups (Reble Music featured)" points="" comments=""></media-hn>

- **August 17, 2007** — VentureBeat ranks Reble 9th (last) among the YC S07 Demo Day companies it covered, calling music "a very tough, crowded space."<sup>[[12]](https://venturebeat.com/business/the-y-combinator-list/)</sup>

- **February 5, 2008** — Reble launches into public beta. TechCrunch covers the launch, noting the Windows-only desktop client as a potential adoption barrier and flagging web-based competitors like Last.fm as already offering on-demand streaming without installation.<sup>[[13]](https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/)</sup>

- **~2009** — Reble.FM is acquired by Playlist.com, approximately three years after founding. Acquisition price, terms, and structure are undisclosed.<sup>[[14]](https://startmit-2018.mit.edu/meyer/)</sup>

- **2009** — Nick Meyer co-founds MileWise, a travel metasearch engine.<sup>[[15]](https://www.startupgrind.com/events/details/startup-grind-boston-presents-nick-meyer-entrepreneur-in-residence-martin-trust-center-for-mit-entrepreneurship/)</sup>

- **2013** — MileWise is acquired by Yahoo!, Meyer's second successful exit.<sup>[[16]](https://www.startupgrind.com/events/details/startup-grind-boston-presents-nick-meyer-entrepreneur-in-residence-martin-trust-center-for-mit-entrepreneurship/)</sup>

## What They Built

Reble's core product was a Windows desktop application that turned a user's social network into a music library. Once installed, the client connected to friends who also had Reble running, and allowed real-time audio streaming from their local music collections — iTunes libraries, Windows Media Player catalogs, or any other locally stored music files.<sup><a href="https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/">[17]</a></sup>

The user experience, as described at launch, worked roughly as follows: a user installed the Reble client on their Windows PC, connected it to their local music library, and added friends through the application. When a friend was online and running Reble, their library became browsable. A user could scroll through a friend's collection, click a track, and hear it play immediately — streamed in real time from the friend's machine, not downloaded to the listener's hard drive. Users could also build playlists that pulled tracks from multiple friends' libraries simultaneously, creating a shared listening experience across a social graph.

The networking layer was built on Jabber, the open-source instant messaging protocol (now XMPP) that underpinned services like Google Talk.<sup><a href="https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/">[18]</a></sup> This gave Reble a built-in IM layer alongside the music functionality, positioning the product as a social communication tool as much as a music player. The choice of Jabber was pragmatic: it provided a proven, decentralized peer-to-peer connection architecture without requiring Reble to build and maintain its own server infrastructure for routing audio streams.

The legal architecture was the product's most distinctive engineering decision. By streaming rather than transferring files, Reble argued it was not engaged in the kind of copying that had destroyed Napster and Grokster. The company also argued it fell outside the internet radio royalty framework — which required services like Pandora to pay per-stream royalties to SoundExchange — because the streams were private, person-to-person transmissions rather than broadcasts.<sup><a href="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/">[19]</a></sup> Whether this legal theory would have survived a challenge from the major labels was never tested; no litigation against Reble is documented in the public record.

The intended business model was music discovery leading to affiliate sales — when a user heard a track they wanted to own, Reble would surface a purchase link and earn a referral fee from the transaction.<sup><a href="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/">[20]</a></sup> No specific affiliate partners (iTunes Store, Amazon MP3, etc.) were named in public coverage. No Mac or Linux versions were announced or documented.

The product's differentiation from alternatives was real but narrow: it was the only service that let users access friends' actual local libraries, rather than curated playlists or algorithmically generated stations. The emotional resonance of hearing exactly what your friend was listening to — not a recommendation engine's approximation of it — was the core value proposition. The problem was that delivering that experience required both parties to install a Windows application and be online simultaneously.

## Market Position

### Target Customers

Reble's target user was a music-engaged, socially connected PC user who trusted friends' taste more than algorithmic recommendations and was willing to install a desktop application to access it. This was a real and identifiable segment in 2007 — the era of Last.fm scrobbling, MySpace music profiles, and early music blogs — but it was also a segment that web-based services were already serving with less friction. The requirement that both the listener and the source be running the Reble client simultaneously narrowed the addressable user base further: the product's value was zero until a user's social graph reached a critical mass of Reble installations.

### Market Size

The online music market in 2007–2008 was large in aggregate but structurally contested. Digital music sales in the U.S. reached approximately $2.9 billion in 2007, with iTunes commanding the dominant share of paid downloads.<sup><a href="https://venturebeat.com/business/the-y-combinator-list/">[21]</a></sup> The streaming market was nascent but growing rapidly — Last.fm had approximately 15 million registered users by 2007 when CBS acquired it for $280 million, and Pandora was approaching 1 million active listeners. Reble's addressable market was the subset of this audience willing to use a desktop P2P client — a segment that was shrinking, not growing, as browser capabilities improved. No market sizing data specific to Reble's pitch is available in the public record.

### Competition

Reble competed on two dimensions simultaneously: music discovery and social connectivity. On neither dimension did it hold a structural advantage over incumbents.

On music discovery, Last.fm had already built a massive dataset of listening behavior through its scrobbling technology, giving it recommendation depth that Reble's friend-library model could not match at small scale. Pandora had the Music Genome Project. Both were web-based, requiring no installation. iMeem and MySpace Music were building licensed streaming catalogs that didn't depend on friends having the right tracks in their local libraries.

On social connectivity, Reble's Jabber-based IM layer competed with AIM, MSN Messenger, and the emerging Facebook platform — all of which had vastly larger existing social graphs. Reble was asking users to rebuild their social network inside a new application rather than extending an existing one.

The most structurally damaging competitive dynamic was platform commoditization. By February 2008, when Reble launched its public beta, the direction of the market was clear: streaming was moving to the browser, catalogs were moving to the cloud, and the desktop client model was being abandoned even by incumbents. Spotify launched in Europe in October 2008 with a licensed catalog of millions of tracks, accessible via a lightweight desktop client that didn't require friends to be online simultaneously. The feature Reble was building — access to friends' music — became a social layer that Spotify, Last.fm, and eventually Apple Music added on top of complete catalogs, rather than a standalone product.

Reble's competitive position was weakest precisely where it needed to be strongest: distribution. A two-person team with partial YC funding could not acquire users at the rate needed to solve the cold-start problem before better-funded, web-based competitors made the desktop P2P model obsolete.

## Business Model

Reble's stated revenue model was affiliate sales: the service would function as a music discovery engine, and when users heard tracks they wanted to purchase, Reble would surface buy links and earn referral fees from the resulting transactions.<sup><a href="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/">[22]</a></sup> No specific affiliate partners were named publicly, and no revenue figures were ever disclosed — the absence of any revenue data in the public record is itself a signal that the company did not reach meaningful monetization before its acquisition.

The affiliate model had a structural problem independent of Reble's other challenges: it depended on users wanting to *buy* music they discovered through the service, at a moment when the music industry was shifting toward streaming subscriptions and away from per-track purchases. The iTunes download model that affiliate fees would have plugged into was already under pressure from streaming alternatives by 2008.

On unit economics: Reble received only partial YC funding — the standard YC S07 deal was approximately $15,000–$20,000 for a small percentage of equity, though the exact figure for Reble is not documented.<sup><a href="https://startmit-2018.mit.edu/meyer/">[23]</a></sup> With a two-person team operating in San Francisco from mid-2007 through approximately 2009, and no documented external fundraising, the company's total capital deployed was almost certainly under $500,000. This is an inference based on team size, location, and the absence of any funding announcements — not a documented figure. At that capital level, the runway to solve a cold-start problem in a crowded consumer market was structurally insufficient.

## Traction

No user counts, engagement metrics, or revenue figures for Reble are available in the public record. The company never disclosed beta user numbers following its February 2008 launch. The absence of any traction data in press coverage — TechCrunch covered the launch but reported no metrics — is consistent with a product that did not achieve meaningful adoption before its acquisition. VentureBeat's ranking of Reble last among YC S07 Demo Day companies at the pitch stage suggests investor skepticism was present from the beginning, which may have limited the company's ability to raise follow-on capital that would have enabled growth experiments.<sup><a href="https://venturebeat.com/business/the-y-combinator-list/">[24]</a></sup>

## Post-Mortem

### The Cold-Start Problem Was Structural, Not Solvable by Better Marketing

Reble's core value proposition — streaming music from friends' libraries — required both the listener and the source to have installed the Windows client and be online simultaneously. This is a bilateral network effect problem: the product delivered zero value to a new user until at least one of their friends was also a Reble user. Unlike social networks where a user can browse content even before their friends join, Reble's music streaming was entirely dependent on real-time peer availability.

The company launched its public beta in February 2008 — roughly 18 months after founding.<sup><a href="https://www.ycombinator.com/companies/reble">[25]</a></sup> No user acquisition strategy is documented in the public record. With a two-person team and limited capital, Reble had no mechanism to seed the network at the scale needed to make the product useful to early adopters. Kings of Chaos, Meyer's prior product, had solved a similar bootstrapping problem through viral game mechanics — but music streaming offered no equivalent viral loop. A user couldn't share Reble's value with a non-user; they could only invite them to install the client and hope they had compatible music taste.

No documented attempt to address this problem — seeded user groups, campus rollouts, integration with existing social graphs — appears in the public record. Whether such attempts were made and simply not covered by press, or were never made, is unknown.

### Windows-Only Desktop Client in a Web-First Market

At the time of Reble's public beta launch, TechCrunch explicitly flagged the Windows-only desktop download as a likely adoption barrier, noting the proliferation of web-based alternatives for music sharing.<sup><a href="https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/">[26]</a></sup> This was not a minor UX friction — it was a categorical mismatch with where consumer software was heading.

By February 2008, Last.fm offered on-demand streaming through a web browser with no installation required.<sup><a href="https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/">[27]</a></sup> iMeem had a web-based music player with social features. The browser was becoming the default application runtime for consumer products, and the desktop client model was associated in users' minds with the Napster-era P2P software that had attracted legal liability and security concerns.

Reble's choice of a desktop client was not arbitrary — the Jabber-based P2P architecture required local software to access local music libraries, and a browser-based version would have required either a browser plugin (itself a significant installation barrier) or a server-side architecture that would have changed the legal and cost structure of the product entirely. But the technical rationale for the desktop client was invisible to users who simply saw an installation requirement where competitors offered a URL.

No pivot toward a web-based architecture is documented before the acquisition.

### The Legal Strategy Had a Visible Hole

Reble's streaming-not-downloading legal theory was clever but incomplete. TechCrunch noted at Demo Day in August 2007 that stream-capture software was already widely available, meaning a determined user could convert Reble's streams into downloaded files — the exact outcome the music industry was trying to prevent.<sup><a href="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/">[28]</a></sup> This undermined Reble's argument that its architecture was meaningfully different from file-sharing from the labels' perspective.

The company engaged the music industry from the beginning of its life, suggesting awareness of this vulnerability.<sup><a href="https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/">[29]</a></sup> But no licensing deals, label partnerships, or formal legal clearances are documented in the public record. The absence of such agreements — which would have been newsworthy and useful for user acquisition — suggests the industry engagement did not produce the outcomes Reble needed. A two-person team with limited capital was not in a strong negotiating position with major labels that were simultaneously pursuing litigation against much larger companies.

The legal uncertainty created a ceiling on the product's growth: even if Reble had solved its cold-start problem, scaling a service that lacked formal licensing agreements would have invited the kind of label attention that had shut down Napster, Grokster, and LimeWire.

### Market Structure: The Feature, Not the Product

The deepest structural problem for Reble was that its core value proposition — social music discovery through friends' libraries — was a feature, not a product. It was a feature that larger, better-funded platforms could and did add on top of complete licensed catalogs.

Last.fm's "neighbors" feature showed users what people with similar taste were listening to. Spotify launched in Europe in October 2008 with social sharing built in, and later added friend activity feeds. Apple Music added friend-following features. Facebook integrated with Spotify to show what friends were listening to in real time. Each of these implementations delivered the social discovery experience Reble was building, but without the cold-start problem — because they were layered on top of catalogs that were already useful to individual users before any friends joined.

Reble's architecture inverted this: the social layer was the product, and the catalog was entirely dependent on friends' local libraries. This meant Reble was competing against the social features of platforms with complete catalogs, using a catalog that was incomplete by design. The market rewarded the catalog-first approach; Reble's social-first approach required a level of network density it never achieved.

### Outcome: Acquisition as Soft Landing

Reble.FM was acquired by Playlist.com approximately three years after founding, around 2009.<sup><a href="https://startmit-2018.mit.edu/meyer/">[30]</a></sup> Playlist.com was a web-based music service that allowed users to create and share playlists of licensed music — precisely the web-first, catalog-backed model that Reble's architecture had not been. The acquisition is confirmed by Meyer's YC career profile, which lists "Reble.FM (Playlist.com)" as a sequential entry.<sup><a href="https://www.ycombinator.com/companies/reble">[31]</a></sup> Tracxn also confirms the acquisition.<sup><a href="https://tracxn.com/d/companies/playlist/__WF_aaOZtBMJF5lblMJD7l8xtKbaApIoVquDLlilu_ns">[32]</a></sup>

Whether the acquisition was a talent acquisition, a technology acquisition, or a user base acquisition is unknown. The fact that Playlist.com — a web-based service — acquired a Windows desktop P2P client suggests the technology itself was not the primary asset. The most likely interpretation is that this was an acqui-hire or a soft landing that provided some return to YC and allowed Meyer to move on cleanly. This interpretation is an inference from the available evidence, not a documented fact.

## Key Lessons

- **Bilateral network effects require a seeding strategy proportional to the cold-start cost.** Reble's value was zero until both a user and at least one friend had installed the Windows client and were online simultaneously. Kings of Chaos had solved a similar bootstrapping problem through viral game mechanics — but Reble had no equivalent loop. A two-person team with partial YC funding and no documented seeding strategy (campus rollouts, seeded friend groups, integration with existing social graphs) could not generate the minimum viable network density needed to make the product useful to early adopters. The cold-start cost was high; the seeding investment was insufficient.

- **A legal workaround is not a competitive moat if it depends on a theory the industry hasn't accepted.** Reble's streaming-not-downloading architecture was designed to sidestep both copyright infringement and internet radio royalties. But the music industry's acceptance of that theory was never documented — no licensing deals, no formal clearances, no label partnerships appear in the public record. Stream-capture software already existed in 2007, undermining the theory's practical force. Reble was building on a legal foundation that had not been tested, in a market where the labels had demonstrated willingness to litigate. Contrast this with Spotify, which spent years negotiating licensing deals before launching in the U.S. — a slower path, but one that produced a defensible business.

- **Social discovery is a feature that catalog-first platforms can absorb; it is not a standalone product.** Reble's core insight — that friends' music libraries are a natural discovery surface — was correct. The market validated it repeatedly: Last.fm's neighbor recommendations, Spotify's friend activity feed, Apple Music's social features, Facebook's Spotify integration. But each of these implementations delivered social discovery on top of a complete catalog that was already useful to individual users. Reble's architecture required the social layer to carry the entire product, which meant it was competing against the social features of platforms with complete catalogs, using a catalog that was incomplete by design. The lesson is not that social music discovery was wrong, but that it needed to be a layer on top of a complete product, not the product itself.

- **Platform choice is a growth constraint, not just a technical decision.** Reble's Windows-only desktop client was a rational consequence of its P2P architecture, but it meant the product was inaccessible to Mac users, Linux users, and anyone unwilling to install software — a population that was growing rapidly as browser-based alternatives proliferated. By the time of Reble's February 2008 public beta, TechCrunch was already flagging the installation requirement as a likely adoption barrier. A startup with limited capital cannot afford to exclude large segments of its potential user base on platform grounds, particularly when competitors are offering zero-installation alternatives.

## Sources

1. [Y Combinator Company Profile — Reble](https://www.ycombinator.com/companies/reble)
2. [StartMIT 2018 — Nick Meyer Biography](https://startmit-2018.mit.edu/meyer/)
3. [Startup Grind Boston — Nick Meyer Event Profile](https://www.startupgrind.com/events/details/startup-grind-boston-presents-nick-meyer-entrepreneur-in-residence-martin-trust-center-for-mit-entrepreneurship/)
4. [TechCrunch — Y Combinator Demo Day: The Summer Startups (August 16, 2007)](https://techcrunch.com/2007/08/16/y-combinator-demo-day-the-summer-startups/)
5. [TechCrunch — Reble, Reble, I Like Your Playlist (February 5, 2008)](https://techcrunch.com/2008/02/05/reble-reble-i-like-your-playlist/)
6. [VentureBeat — The Y Combinator List (August 17, 2007)](https://venturebeat.com/business/the-y-combinator-list/)
7. [Tracxn — Playlist Company Profile (confirms Reble acquisition)](https://tracxn.com/d/companies/playlist/__WF_aaOZtBMJF5lblMJD7l8xtKbaApIoVquDLlilu_ns)
