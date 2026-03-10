# Research Report: OneGraph

## Overview

## Founding Story

Sean Grove arrived at OneGraph with a résumé that read like a tour of developer infrastructure. He had co-founded Bushido, a developer tools company in Y Combinator's S11 batch, then worked at Sauce Labs — a cross-browser testing infrastructure company — and built PayGarden, a gift card payment platform.<sup><a href="https://www.riseos.com/">[3]</a></sup> Each stop gave him direct exposure to the same recurring problem: integrating a product into third-party SaaS APIs was painful, repetitive, and never got easier regardless of how many times you did it.

Daniel Woelfel brought complementary engineering depth. The two founders do not appear to have published a detailed account of how they met, and no public record documents the specifics of their early working relationship or division of responsibilities. What is documented is the shared experience that drove them to build: "At different startups over the years, both of us had to integrate our products into dozens of other services, like GitHub, Salesforce, Stripe, Marketo, Clearbit, etc."<sup><a href="https://www.onegraph.com/blog/post/1/introducing-onegraph">[4]</a></sup>

The founding insight was precise and structural. Grove and Woelfel observed that the world's SaaS data was not actually connected — the connections between services like GitHub, Twitter, Salesforce, and Hacker News were all implicit, buried in individual API documentation, authentication schemes, and rate-limiting rules. GraphQL, they argued, could make those connections declarative: "there is no explicit graph connecting the world's data."<sup><a href="https://www.onegraph.com/blog/post/1/introducing-onegraph">[4]</a></sup> OneGraph would be that explicit graph.

They applied to Y Combinator's Summer 2018 batch and were accepted — Grove's prior YC experience with Bushido likely gave him pattern recognition on what the application process required and what YC partners would find compelling in a developer tools pitch. The company incorporated in 2018 and launched publicly on Hacker News on July 27, 2018, just weeks into the batch.<sup><a href="https://news.ycombinator.com/item?id=17602951">[5]</a></sup>

The initial vision was broad: a unified API layer for all of the internet's services. There was no explicit pivot in the founding narrative, but the product's evolution — from a general-purpose GraphQL aggregator to a Jamstack-aligned auth and API layer — represents a meaningful strategic narrowing that happened gradually between 2018 and 2021. The team remained at exactly two people throughout the company's independent life.<sup><a href="https://www.ycombinator.com/companies/onegraph">[6]</a></sup>

## Timeline

- **July 2018** — OneGraph founded by Sean Grove and Daniel Woelfel; company enters Y Combinator S18 batch.<sup>[[1]](https://www.ycombinator.com/companies/onegraph)</sup>

- **July 18, 2018** — Founders publish "Introducing OneGraph" blog post, articulating the founding thesis and describing early customer use cases including a fire-tracking drone company.<sup>[[4]](https://www.onegraph.com/blog/post/1/introducing-onegraph)</sup>

- **July 27, 2018** — OneGraph launches on Hacker News ("Launch HN: OneGraph (YC S18) – Build API Integrations with GraphQL"), announcing support for "a couple dozen APIs."<sup>[[5]](https://news.ycombinator.com/item?id=17602951)</sup>

<media-hn url="https://news.ycombinator.com/item?id=17602951" title="Launch HN: OneGraph (YC S18) – Build API Integrations with GraphQL" points="342" comments="187"></media-hn>

- **August 21, 2018** — OneGraph presented at Y Combinator S18 Demo Day 2 at the Computer History Museum.<sup>[[7]](https://techcrunch.com/2018/08/21/all-59-startups-that-launched-today-at-y-combinators-s18-demo-day-2/)</sup>

- **2019** — Seed round closed with SignalFire and Perceptual Networks as investors; exact amount undisclosed.<sup>[[8]](https://www.crunchbase.com/organization/onegraph)</sup>

- **March 10, 2020** — Sean Grove interviewed on Software Engineering Daily podcast discussing OneGraph's GraphQL tooling and engineering challenges.<sup>[[9]](https://softwareengineeringdaily.com/2020/03/10/onegraph-graphql-tooling-with-sean-grove/)</sup>

- **April 2020** — Screenshare demo published featuring Grove and developer advocate swyx, demonstrating OneGraph replacing manually-built Next.js API routes with GraphQL integrations — signaling alignment with the Jamstack/Next.js ecosystem.<sup>[[9]](https://softwareengineeringdaily.com/2020/03/10/onegraph-graphql-tooling-with-sean-grove/)</sup>

- **November 17, 2021** — Netlify acquires OneGraph for an undisclosed amount, simultaneously with Netlify's $105M Series D at a $2B valuation. Both founders join Netlify to lead API ecosystem engineering. First product: Netlify API Authentication.<sup>[[10]](https://www.crunchbase.com/acquisition/netlify-acquires-onegraph--96e9ed82)</sup>

- **November 19, 2021** — The Register publishes analysis of the acquisition, noting limitations of the initial Netlify API Authentication beta and flagging dependency on third-party provider cooperation for full realization.<sup>[[11]](https://www.theregister.com/2021/11/19/netlify_onegraph/)</sup>

- **2022** — Sean Grove serves as Principal Architect at Netlify, leading API ecosystem and Jamstack architectural initiatives.<sup>[[12]](https://www.riseos.com/)</sup>

- **2023** — Sean Grove joins OpenAI's post-training and alignment team, working on model-spec infrastructure and deliberative-alignment techniques.<sup>[[1]](https://www.ycombinator.com/companies/onegraph)</sup>

- **2024** — Sean Grove founds Linzumi, a serverless ML APIs platform.<sup>[[1]](https://www.ycombinator.com/companies/onegraph)</sup>

## What They Built

OneGraph's core product was a single GraphQL endpoint that sat in front of dozens of third-party SaaS APIs and presented them as a unified, queryable graph. Instead of a developer writing separate integration code for Salesforce, Stripe, GitHub, and Gmail — each with its own authentication scheme, rate limits, data format, and error handling — they could write a single GraphQL query that touched all four simultaneously.<sup><a href="https://news.ycombinator.com/item?id=17602951">[13]</a></sup>

The practical mechanics worked like this: a developer would point their application at OneGraph's endpoint, authenticate once, and then write queries that spanned multiple services. OneGraph handled the fan-out — parallelizing requests to upstream APIs where possible, queuing them where rate limits required, and caching responses to reduce redundant calls.<sup><a href="https://www.crunchbase.com/organization/onegraph">[14]</a></sup> The result was that a query fetching a user's GitHub repositories, their Stripe subscription status, and their Salesforce account data could be expressed in a single declarative statement rather than three separate API calls with three separate auth flows.

At launch, OneGraph supported "a couple dozen" APIs including Salesforce, Stripe, Twitter, Twilio, Google Cloud Platform, GitHub, Clearbit, Gmail, Intercom, and Zendesk.<sup><a href="https://www.programmableweb.com/news/onegraph-wants-to-make-api-integrations-easier-graphql/brief/2018/07/26">[15]</a></sup>

The backend was built in ReasonML — a statically typed functional language that compiles to JavaScript — with some code generation written in Clojure. The graphiql-explorer, a visual query-building interface embedded in the product, was written in Reason and BuckleScript.<sup><a href="https://www.onegraph.com/blog/post/1/introducing-onegraph">[4]</a></sup> This was a technically distinctive stack: ReasonML offered strong type safety and performance characteristics, but it was a niche choice that likely constrained the pool of potential hires and community contributors.

<media-image src="https://opengraph.githubassets.com/1/OneGraph/graphiql-explorer" alt="OneGraph graphiql-explorer GitHub repository" caption="OneGraph's open-source graphiql-explorer repo — the visual query builder that spread across the GraphQL ecosystem into Hasura, Apollo, PostGraphile, and Gatsby, becoming the company's most widely adopted contribution."></media-image>

The graphiql-explorer became OneGraph's most consequential open-source contribution. It allowed developers to visually browse available fields and build queries by clicking rather than typing — a significant usability improvement over the standard GraphiQL interface. The explorer was adopted by Hasura, Apollo, PostGraphile, Gatsby, and other major GraphQL tools, spreading OneGraph's code across the ecosystem. This was either a deliberate developer acquisition strategy or a goodwill release; the founders never publicly explained the decision.

The product's second major component was AuthGuardian, a free service that let developers add third-party sign-in to client-side applications and visually describe authentication and authorization rules, generating signed JWTs for use in frontend apps.<sup><a href="https://github.com/OneGraph/onegraph-blog/issues/7">[16]</a></sup> AuthGuardian represented a meaningful strategic shift: it was aimed squarely at frontend developers building serverless and Jamstack applications, not backend engineers doing enterprise integrations.

<media-youtube id="4NaRQ3B-3fg" title="OneGraph screenshare demo with Sean Grove and swyx — replacing Next.js API routes with GraphQL integrations (April 2020)"></media-youtube>

The April 2020 screenshare demo with swyx illustrates the product's late-stage positioning clearly. Grove demonstrates swapping out manually-built Next.js API routes for OneGraph's premade GraphQL integration with Dev.to, including handling user authentication without managing API keys directly. The target user in this demo is a Jamstack developer — exactly the constituency Netlify was building its platform around.

OneGraph's GitHub organization, now archived as "OneGraph (acquired by Netlify)," contains repositories including `auth-guardian-next-js-starterkit`, `authguardian-nextjs-starter`, and `authguardian-react-starter` — confirming a deliberate late-stage pivot toward the Next.js and React developer audience.<sup><a href="https://github.com/onegraph">[17]</a></sup>

## Market Position

### Target Customers

OneGraph's initial target was backend developers at startups and mid-size companies who needed to integrate their products into multiple SaaS platforms simultaneously. The founding blog post cited integrations into GitHub, Salesforce, Stripe, Marketo, and Clearbit as the canonical pain — the kind of work that consumed engineering time at every B2B SaaS company.<sup><a href="https://www.onegraph.com/blog/post/1/introducing-onegraph">[4]</a></sup>

The actual customer base that emerged was more heterogeneous. Early documented customers included a fire-tracking drone company using OneGraph to control YouTube live streaming and retrieve elevation data, and companies building omni-search across SaaS applications.<sup><a href="https://github.com/OneGraph/onegraph-blog/issues/1">[18]</a></sup> These use cases validated the product's flexibility but also suggested a long-tail customer base with highly varied needs — a profile that makes repeatable sales motions difficult to build.

The founders discovered an unexpected split: "We initially thought OneGraph would be useful for back-end developers doing integrations into their product, but we've found we have a pretty even split between people using us on the backend, and people using us purely from the frontend with no server."<sup><a href="https://www.onegraph.com/blog/post/1/introducing-onegraph">[4]</a></sup> This observation, made in the founding blog post, foreshadowed the eventual pivot toward frontend and Jamstack developers — a pivot that took roughly two years to fully execute.

### Market Size

The API integration market is large but diffuse. Zapier, which addresses a related problem for non-technical users, reached a $5B valuation by 2021. MuleSoft, which addresses enterprise API integration, was acquired by Salesforce for $6.5B in 2018. The developer-facing GraphQL aggregation niche that OneGraph occupied was a subset of this market — smaller, more technically sophisticated, and less proven as a standalone business category. No public market sizing specific to OneGraph's exact positioning was ever published.

### Competition

OneGraph competed along two axes simultaneously: the depth of its GraphQL abstraction and the breadth of its API coverage. On both dimensions, it faced structural disadvantages that became more pronounced over time.

**The integration platform incumbents** — MuleSoft, Boomi, and Workato — had enterprise distribution, existing customer relationships, and sales teams. They were not building GraphQL-native products, which gave OneGraph a genuine technical differentiation, but they were selling to the same enterprise buyers who needed multi-API integration. OneGraph's developer-first, self-serve positioning meant it was not directly competing for enterprise contracts, but it also meant it was not capturing enterprise pricing.

**The Jamstack platform providers** — Netlify, Vercel, AWS Amplify, and Azure Static Apps — were the more structurally significant competitive threat. By 2021, these platforms were in an active land grab for the frontend cloud layer, each racing to add capabilities that would make their platform the default deployment target for modern web applications.<sup><a href="https://www.theregister.com/2021/11/19/netlify_onegraph/">[19]</a></sup> API integration and authentication were natural adjacencies. Any of these platforms could absorb OneGraph's core functionality — and Netlify ultimately did.

**The open-source GraphQL ecosystem** — Hasura, Apollo Federation, and PostGraphile — offered overlapping capabilities for specific use cases. Hasura in particular provided a GraphQL layer over databases and REST APIs, competing for the same developer attention. The graphiql-explorer's adoption by these tools is a double-edged data point: it demonstrated OneGraph's technical credibility, but it also meant OneGraph's most visible contribution was freely available inside competing products.

The most structurally important competitive dynamic was platform dependency. OneGraph's value was entirely contingent on the continued availability and stability of third-party APIs it had no control over. Each API change, deprecation, or authentication update required maintenance work from a two-person team. As the number of supported APIs grew, so did the maintenance burden — without a corresponding increase in headcount. This is a model that scales poorly without either significant automation or a large engineering team.

## Business Model

OneGraph never publicly disclosed its pricing model, revenue figures, ARR, MRR, or any unit economics. The absence of this data is itself a signal: companies with strong revenue growth typically publicize it, and the complete silence across three-plus years of operation suggests the business had not reached a scale worth announcing.

The product's structure implied a usage-based or tiered SaaS model — API call volume, number of connected services, or seat count are the natural pricing levers for a product of this type. AuthGuardian was explicitly free, which suggests the company was using it as a top-of-funnel acquisition tool rather than a revenue driver. The starter kits for Next.js and React on GitHub reinforce this interpretation: they are developer acquisition assets, not monetization mechanisms.

With a two-person team and a seed round from SignalFire and Perceptual Networks (amount undisclosed), the company's burn rate was structurally low. Two engineers in San Francisco in 2019-2021 would have cost roughly $400K-$600K per year in fully-loaded compensation, plus infrastructure costs for running API proxies at scale — likely another $50K-$150K annually depending on volume. This is an inference based on market compensation data and typical infrastructure costs for API proxy services, not disclosed figures.

The low burn rate is a double-edged characteristic: it extended runway but also meant the company lacked the sales, marketing, and partnership resources needed to grow beyond its organic developer audience. A two-person team cannot simultaneously maintain dozens of API integrations, build new product features, run developer relations, and close enterprise contracts.

## Traction

OneGraph never disclosed user counts, API call volumes, revenue, or growth metrics across its entire independent operating life. The only public traction signals are qualitative.

The Hacker News launch in July 2018 generated meaningful developer community engagement — the post attracted hundreds of comments and points, consistent with a well-received developer tool launch. The graphiql-explorer's adoption by Hasura, Apollo, PostGraphile, and Gatsby demonstrates that OneGraph's open-source work reached a large developer audience, though adoption of a free tool does not translate directly to paying customers.

The Software Engineering Daily podcast appearance in March 2020 and the swyx screenshare demo in April 2020 suggest active developer relations work through the company's middle years. These are founder-led activities, not evidence of a growth team.

The founding blog post's observation about an even split between backend and frontend users — made in July 2018 — suggests the product found real users quickly after launch. The fire-tracking drone company and omni-search use cases are documented as actual customers, not hypotheticals.<sup><a href="https://github.com/OneGraph/onegraph-blog/issues/1">[18]</a></sup> But no customer count, retention data, or revenue figure was ever attached to these anecdotes.

The acquisition by Netlify at a moment of significant strategic investment — simultaneous with a $105M Series D — implies Netlify believed the technology and team were worth acquiring. Whether that judgment was based on OneGraph's demonstrated traction or purely on the founders' technical vision and the strategic fit of the technology is not publicly documented.

## Post-Mortem

### Primary Cause: A Two-Person Team Running a Many-Person Problem

The most fundamental constraint on OneGraph's independent viability was structural: maintaining live integrations with dozens of third-party APIs is a labor-intensive, ongoing operational burden that scales with the number of integrations, not with revenue.

Every API provider that OneGraph supported could change its authentication scheme, deprecate endpoints, alter rate limits, or modify data formats at any time. Each such change required OneGraph to detect the breakage, diagnose the cause, update its integration layer, test the fix, and deploy — all without disrupting existing customers. With "a couple dozen" APIs at launch and presumably more added over time, this maintenance surface area was substantial.<sup><a href="https://www.programmableweb.com/news/onegraph-wants-to-make-api-integrations-easier-graphql/brief/2018/07/26">[15]</a></sup>

A two-person team cannot simultaneously handle this maintenance load, build new API integrations, develop new product features (AuthGuardian, the graphiql-explorer, starter kits), run developer relations, and pursue sales. The team appears to have prioritized product and developer relations — the right choices for early-stage developer tools — but this meant the sales and partnership functions were effectively unresourced.

The attempted remedy was to keep the team small and burn rate low, extending runway while the product found its market. This worked as a survival strategy but not as a growth strategy. There is no public evidence that OneGraph attempted to raise a Series A to hire the engineering and sales capacity needed to scale the integration maintenance model.

### Secondary Cause: The Open-Source Contribution Dilemma

The graphiql-explorer was OneGraph's most widely adopted product contribution — and it was free. The explorer spread into Hasura, Apollo, PostGraphile, Gatsby, and other major GraphQL tools, giving OneGraph significant ecosystem presence and developer goodwill. But it also meant that the most visible demonstration of OneGraph's technical quality was available inside competing products at no cost.

This is a common tension in developer tools: open-source contributions build community credibility and top-of-funnel awareness, but they can also commoditize the differentiators that would otherwise justify a paid product. OneGraph never publicly explained whether the graphiql-explorer release was a deliberate developer acquisition strategy with a planned conversion funnel, or a goodwill contribution without a monetization plan attached.

The AuthGuardian product — also free — follows the same pattern. A free visual auth builder for client-side apps is a compelling developer acquisition tool, but only if there is a paid product downstream that free users convert into. No public evidence documents whether such a conversion funnel existed or what its conversion rate was.

### Tertiary Cause: Platform Dependency Without Platform Partnership

OneGraph's entire value proposition depended on the continued availability and cooperation of third-party API providers. This created a structural vulnerability that the company could not resolve independently.

The Netlify CEO's post-acquisition statement made this dependency explicit: "It will be important that we can allow external providers to plug into our platform and extend it, to live up to its full potential."<sup><a href="https://www.theregister.com/2021/11/19/netlify_onegraph/">[20]</a></sup> If Netlify — with $105M in fresh capital and a $2B valuation — acknowledged that realizing OneGraph's full value required third-party provider cooperation, then OneGraph as a standalone two-person startup had no realistic path to achieving that cooperation independently.

The initial Netlify API Authentication beta launched with a notable limitation: developers could only use their own credentials and could not proxy site visitor credentials.<sup><a href="https://www.theregister.com/2021/11/19/netlify_onegraph/">[11]</a></sup> This constraint — present even after the acquisition — suggests that the technology required significant additional work and ecosystem cooperation to reach its full potential. A standalone OneGraph would have faced this same limitation without Netlify's platform leverage to negotiate with API providers.

### Structural Factor: The Feature-vs-Product Resolution

The deepest structural explanation for OneGraph's outcome is that API aggregation at the developer infrastructure layer is more naturally a platform feature than a standalone product. The companies that succeeded in adjacent spaces — Stripe for payments, Twilio for communications, Plaid for financial data — did so by owning a specific, high-value API category deeply, not by aggregating across many categories shallowly.

OneGraph's approach — broad aggregation across dozens of APIs — created a product that was useful to many developers for different reasons, but not indispensable to any specific developer segment. A fire-tracking drone company and an omni-search startup have almost nothing in common as customers, making it difficult to build a repeatable sales motion, a focused product roadmap, or a compelling category narrative.

By contrast, embedding OneGraph's technology inside Netlify's platform — where the target customer is already defined (Jamstack developers deploying to Netlify), the distribution is already built (Netlify's existing user base), and the adjacent products are already present (Netlify Functions, Netlify Identity) — resolves the distribution and focus problems simultaneously. The technology was more valuable as a platform feature than as a standalone product, and the acquisition was the market's mechanism for reaching that resolution.

The pivot toward Jamstack and Next.js developers that OneGraph executed between 2019 and 2021 was directionally correct — it aligned with where developer tooling investment was concentrating. But executing that pivot as a two-person team, without the distribution of a platform, meant the company was competing for the same developer attention as Netlify, Vercel, and AWS Amplify without their scale advantages.

<media-image src="https://opengraph.githubassets.com/1/OneGraph/onegraph-blog/issues/1" alt="OneGraph founding blog post on GitHub" caption="OneGraph's founding blog post, hosted on GitHub — the document that introduced the company's thesis that 'there is no explicit graph connecting the world's data,' and described early customers including a fire-tracking drone company."></media-image>

## Key Lessons

- **Maintaining dozens of third-party API integrations is an operational burden that scales with headcount, not revenue — and OneGraph never hired for it.** OneGraph launched with "a couple dozen" APIs and a two-person team. Each additional API integration added ongoing maintenance surface area: authentication changes, endpoint deprecations, rate limit adjustments. The business model required either significant automation of integration maintenance (which OneGraph did not publicly develop) or a much larger engineering team (which the company never hired). The result was a ceiling on how many APIs could be supported reliably, which in turn capped the product's value proposition.

- **Free open-source contributions build ecosystem presence but require a deliberate conversion funnel to generate revenue — OneGraph never publicly demonstrated one.** The graphiql-explorer's adoption across Hasura, Apollo, PostGraphile, and Gatsby gave OneGraph significant developer mindshare. AuthGuardian gave frontend developers a free auth tool. But neither product had a documented path to paid conversion. Contrast this with companies like Stripe, which gave away excellent documentation and SDKs while charging clearly for transaction processing. OneGraph's free contributions were technically excellent but strategically incomplete without a visible monetization layer.

- **API aggregation businesses face a structural ceiling as standalone products: the value scales with API provider cooperation, which a small startup cannot compel.** Netlify's CEO acknowledged post-acquisition that realizing OneGraph's full potential required third-party providers to actively plug into the platform. OneGraph as a standalone company had no leverage to secure those partnerships. The technology needed platform distribution to reach its potential — a dependency that made acquisition by a platform the most likely exit path from the beginning.

- **OneGraph's pivot toward Jamstack developers was correct in direction but arrived without the distribution needed to capitalize on it.** The 2020 screenshare demo with swyx and the Next.js starter kits in the GitHub org confirm that OneGraph identified the Jamstack developer as its target customer roughly two years before the acquisition. But Netlify and Vercel were simultaneously building the same audience with platform-level distribution advantages. A two-person team with a seed round cannot out-distribute a platform with tens of millions in funding and an existing user base — the pivot needed to happen earlier, or with more resources, to matter independently.

- **The absence of any public revenue or growth metrics across three-plus years of operation is itself a diagnostic signal.** OneGraph never disclosed ARR, MRR, user counts, or API call volumes. Developer tools companies with strong growth metrics publicize them — it is a standard fundraising and recruiting tool. The complete silence suggests the business had not reached a scale that made disclosure advantageous. This does not mean the product was bad; it means the business model was not converting product quality into measurable commercial traction at a rate that justified independent scaling.

## Sources

1. [Y Combinator — OneGraph company profile](https://www.ycombinator.com/companies/onegraph)
2. [Wikipedia — Netlify](https://en.wikipedia.org/wiki/Netlify)
3. [Sean Grove — Riseos profile](https://www.riseos.com/)
4. [OneGraph — Introducing OneGraph (founding blog post)](https://www.onegraph.com/blog/post/1/introducing-onegraph)
5. [Hacker News — Launch HN: OneGraph (YC S18)](https://news.ycombinator.com/item?id=17602951)
6. [TechCrunch — All 59 startups that launched at YC S18 Demo Day 2](https://techcrunch.com/2018/08/21/all-59-startups-that-launched-today-at-y-combinators-s18-demo-day-2/)
7. [Crunchbase — OneGraph organization profile](https://www.crunchbase.com/organization/onegraph)
8. [Software Engineering Daily — OneGraph GraphQL Tooling with Sean Grove (March 10, 2020)](https://softwareengineeringdaily.com/2020/03/10/onegraph-graphql-tooling-with-sean-grove/)
9. [Crunchbase — Netlify acquires OneGraph](https://www.crunchbase.com/acquisition/netlify-acquires-onegraph--96e9ed82)
10. [The Register — Netlify acquires OneGraph analysis (November 19, 2021)](https://www.theregister.com/2021/11/19/netlify_onegraph/)
11. [ProgrammableWeb — OneGraph wants to make API integrations easier with GraphQL (July 26, 2018)](https://www.programmableweb.com/news/onegraph-wants-to-make-api-integrations-easier-graphql/brief/2018/07/26)
12. [OneGraph blog — AuthGuardian announcement](https://github.com/OneGraph/onegraph-blog/issues/7)
13. [OneGraph GitHub organization](https://github.com/onegraph)
14. [OneGraph blog — Introducing OneGraph (early customers)](https://github.com/OneGraph/onegraph-blog/issues/1)
15. [Netlify — Netlify acquires OneGraph announcement (November 17, 2021)](https://www.netlify.com/blog/2021/11/17/netlify-acquires-onegraph-a-powerful-graphql-platform-for-connecting-apis-and-services/)
16. [Sean Grove — LinkedIn post on acquisition](https://www.linkedin.com/posts/segrove_netlify-acquires-onegraph-a-powerful-graphql-activity-6866752371188346880-4sif)
17. [YCDB — OneGraph company profile](https://www.ycdb.co/company/onegraph)
