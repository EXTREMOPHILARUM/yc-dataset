# Research Report: Enflux

## Overview

## Founding Story

Doug Hoang and Elijah Schuldt met as college roommates and stayed in contact as their careers diverged into complementary technical domains. Hoang built a career in precision mechanical engineering: he earned a mechanical engineering degree, worked as a manufacturing engineer at Harley-Davidson, and then served as Chief Engineer at Power Solutions International (PSI), where he designed V8 and V6 engines that generated $500 million in revenue and contributed to PSI's IPO.<sup><a href="https://www.getenflux.com/about-us/">[1]</a></sup> Schuldt's background was in electronics and embedded systems — the pairing that would eventually define Enflux's technical identity.

The founding insight was accidental and personal. Hoang and Schuldt had been building motion sensors for racecar analysis — measuring yaw, pitch, and roll to understand vehicle dynamics. When Hoang began training for a triathlon, he strapped the racecar sensors to his legs to collect running data. He got injured. The sensors told him why. "I had these motion sensors we developed, I could strap them to my legs that measure yaw, pitch and roll," Hoang said. "When I started training for triathlons it was like, 'this is the next big thing.'"<sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[2]</a></sup>

The founding team expanded to include Mickey Ferri, who held a PhD in economics from the University of Chicago where he studied the economics of technology adoption and market dynamics in sports and entertainment,<sup><a href="https://www.getenflux.com/about-us/">[3]</a></sup> and Pamela Lee, who served as VP of Soft Goods and brought textile manufacturing expertise critical to integrating sensors into washable athletic fabric. Ferri articulated the commercial vision clearly: "We're giving the everyday person access to Olympic-caliber coaching."<sup><a href="https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/">[4]</a></sup>

The company was founded in 2012, but Enflux did not appear in YC until Winter 2016 — a four-year gap that reflects the genuine engineering difficulty of the product.<sup><a href="https://www.ycombinator.com/companies/enflux">[5]</a></sup> The early phase involved strap-on sensor prototypes before the team committed to the harder problem of integrating sensors directly into clothing.<sup><a href="https://www.ycombinator.com/blog/enflux-yc-w16-makes-workout-clothes-that-doubles-as-a-personal-trainer">[6]</a></sup> That transition — from sensor rig to washable garment — multiplied the engineering complexity and the manufacturing cost structure simultaneously. The team was well-suited to solve the hardware problem. Whether they were equally equipped to navigate consumer distribution and retail channel development would prove to be a different question.

What prompted the YC application in 2016 specifically is not documented. The company was largely self-funded at that point, with founders having invested approximately $250,000 of their own capital.<sup><a href="https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/">[7]</a></sup> YC represented both capital and credibility — a signal to the market that the product was real.

## Timeline

- **2012** — Enflux founded by Doug Hoang and Elijah Schuldt; origin in racecar motion sensors applied to triathlon training injury prevention<sup>[[5]](https://www.ycombinator.com/companies/enflux)</sup>
- **2012–2015** — Extended R&D phase; strap-on sensor prototypes developed before integration into clothing; founders invest approximately $250,000<sup>[[6]](https://www.ycombinator.com/blog/enflux-yc-w16-makes-workout-clothes-that-doubles-as-a-personal-trainer)</sup>
- **January 2016** — Enflux participates in Y Combinator Winter 2016 batch; receives $120,000 standard YC investment<sup>[[7]](https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/)</sup>
- **February 24, 2016** — VentureBeat coverage; product publicly described as injury prevention and form coaching tool; bootstrapped status disclosed<sup>[[7]](https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/)</sup>
- **March 7, 2016** — Kickstarter campaign launches with $100,000 goal; TechCrunch coverage flags one-year shipping delay and competitive risk from Athos ($51M raised)<sup>[[8]](https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/)</sup>
- **March 8, 2016** — Digital Trends coverage; product tested on 500 people including fitness record holders; platform ambitions stated for VR, gaming, physical therapy<sup>[[9]](https://www.digitaltrends.com/wearables/enflux-kickstarter/)</sup>
- **March 11, 2016** — Kickstarter raises $50,000 in first 48 hours; $86,000 raised with 17 days remaining<sup>[[10]](https://startupbeat.com/enflux-raises-50k-first-two-days-kickstarter/21808/)</sup>
- **January 4, 2017** — CES 2017: Enflux demonstrates developer kit priced at $349; reports $120,000 in clothing sales and 50 platform partners including Hasbro and The Jim Henson Company<sup>[[11]](https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/)</sup>
- **January 2017** — Unity SDK copyrighted; active developer-facing product work confirmed through this date<sup>[[12]](https://github.com/efesurekli/EnfluxUnitySDK)</sup>
- **September 2017** — BackAlert product reportedly launched; pivot from full-body motion capture to single back-mounted posture sensor<sup>[[13]](https://www.crowdfunder.com/enflux)</sup>
- **April 2018** — Last funding round (Seed type, per one database); amount and investors unconfirmed<sup>[[14]](https://www.ycombinatorcompanies.com/company/enflux)</sup>
- **December 27, 2018** — Patent application filed (US 16/120390) for "Training Systems With Wearable Sensors"; Hoang and Schuldt still collaborating on IP<sup>[[15]](https://uspto.report/patent/app/20180369637)</sup>
- **December 2020** — Doug Hoang joins FightCamp in Supply Chain and R&D role; establishes latest possible date for Enflux's effective end<sup>[[16]](https://www.crunchbase.com/person/doug-hoang)</sup>
- **2020** — YC profile status listed as "Inactive" with team size of 2<sup>[[5]](https://www.ycombinator.com/companies/enflux)</sup>

## What They Built

Enflux's core product was a two-piece athletic outfit — a compression shirt and pants — with ten inertial measurement unit (IMU) sensors embedded directly into the fabric. Each IMU measured yaw, pitch, and roll: the three axes of rotational movement that together describe how any body segment is oriented in three-dimensional space.<sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[17]</a></sup> The sensors transmitted data via Bluetooth to a companion smartphone app, which processed the movement data and rendered a real-time 3D avatar of the wearer's body.

The user experience was designed to be immediate and actionable. A person performing a squat, for example, would see their avatar replicate the movement in real time. The app — trained on data from approximately 500 personal trainers who established baselines for correct form across weightlifting, plyometrics, and running<sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[18]</a></sup> — would flag deviations from proper form and provide corrective feedback. The stated goal was injury prevention through biomechanical coaching: catching the asymmetrical knee tracking or forward trunk lean that precedes injury before it causes damage.

<media-youtube id="yxnGzMkVl1w" title="Enflux motion capture clothing demo — CES 2017 product demonstration"></media-youtube>

The garment itself was made of a polyester-spandex blend and was machine washable — a non-trivial engineering achievement given the embedded electronics.<sup><a href="https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/">[19]</a></sup> The five sensors in each garment were integrated with each other by wire, creating a system that had to survive repeated washing, stretching, and compression. Battery life was approximately 14 hours of active use in the developer kit version demonstrated at CES 2017 — adequate for workout use but a meaningful constraint for continuous wear scenarios.<sup><a href="https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/">[19]</a></sup>

The product evolved significantly from its origins. Early prototypes used strap-on sensors — essentially the racecar sensors Hoang had applied to his triathlon training — before the team committed to full garment integration.<sup><a href="https://www.ycombinator.com/blog/enflux-yc-w16-makes-workout-clothes-that-doubles-as-a-personal-trainer">[6]</a></sup> That transition was the central engineering challenge of the company's first four years.

By CES 2017, Enflux had also built a developer-facing platform layer: an open API with 50 partners, a Unity SDK (copyrighted 2017), and integrations with entertainment companies including Hasbro and The Jim Henson Company.<sup><a href="https://www.ycombinator.com/companies/enflux">[20]</a></sup> The Kickstarter had explicitly framed the clothing as a "hardware platform" with ambitions spanning physical therapy, video games, dance, and virtual and augmented reality.<sup><a href="https://www.digitaltrends.com/wearables/enflux-kickstarter/">[21]</a></sup>

What distinguished Enflux from alternatives was price and form factor. Professional motion capture systems used in film and sports science cost tens of thousands of dollars and required controlled environments. Athos, the best-funded competitor, focused on muscle activation via electromyography (EMG) sensors rather than full-body positional tracking. Enflux's ten-IMU system offered something genuinely different: full-body 3D kinematics in a washable garment at a consumer price point. The developer kit was priced at $349 at CES 2017.<sup><a href="https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/">[11]</a></sup> No comparable system existed at that price.

## Market Position

### Target Customers

Enflux initially targeted fitness consumers — specifically athletes concerned with form and injury prevention across weightlifting, plyometrics, and running. The product was positioned as a personal trainer substitute: "We're giving the everyday person access to Olympic-caliber coaching," as co-founder Mickey Ferri put it.<sup><a href="https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/">[4]</a></sup> The Kickstarter early-bird pricing of $249.99 for a full shirt-and-pants set placed the product in the premium fitness technology segment — above a Fitbit, below a Peloton.

The BackAlert pivot shifted the target customer entirely: from fitness enthusiasts to office workers and laborers experiencing back pain, with enterprise buyers (employers, insurers, construction companies) as the likely channel. The Crowdfunder profile cited Microsoft and Bouygues Construction as customers<sup><a href="https://www.crowdfunder.com/enflux">[13]</a></sup> — a B2B occupational health positioning that had little overlap with the original consumer fitness thesis.

### Market Size

Enflux's Crowdfunder profile cited a target market exceeding $38 billion in injury prevention and rehabilitation.<sup><a href="https://www.crowdfunder.com/enflux">[22]</a></sup> The smart apparel segment specifically was smaller and less defined: analyst estimates in 2016 ranged widely, but the category was nascent enough that market size projections were largely speculative. The fitness wearables market was real and growing — Fitbit had gone public in 2015 — but the specific segment of full-body motion capture for consumer fitness had no established revenue base to reference.

The back pain management market that BackAlert targeted was large and well-documented: back pain is the leading cause of disability globally, and occupational back injury represents a significant cost to employers. Whether a single wearable sensor could capture meaningful share of that market — against physical therapy, ergonomic furniture, and pharmaceutical interventions — was a different question from whether the market existed.

### Competition

The competitive landscape for smart apparel in 2016 was structurally unfavorable for an underfunded entrant, for reasons that went beyond any individual competitor.

**Athos** was the most direct analog: smart athletic clothing with embedded sensors, consumer-facing, venture-backed. Athos had raised $51 million by the time Enflux launched its Kickstarter<sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[8]</a></sup> — roughly 200 times Enflux's confirmed external funding at that point. Athos focused on EMG (muscle activation) rather than IMU-based positional tracking, meaning the two products were technically differentiated. But Athos's funding advantage translated directly into manufacturing scale, retail distribution, and marketing reach that Enflux could not match.

**Platform risk** was the more structural threat. Apple Watch, launched in April 2015, was iterating rapidly toward health and fitness features. Garmin and Polar offered GPS-based running form analysis. As smartphone accelerometers and gyroscopes improved, the marginal value of dedicated IMU sensors in clothing narrowed. The question was not whether Enflux's sensors were more accurate — they were — but whether the accuracy premium justified the price and form factor complexity for a mass consumer.

**The category itself proved structurally difficult.** Athos, despite its $51 million in funding, eventually shut down — suggesting the smart apparel market timing problem was industry-wide. The combination of hardware complexity, consumer education requirements, and the difficulty of building recurring revenue from a physical product created a category where even well-funded companies struggled. Enflux was competing on product depth (full-body 3D kinematics, developer platform) against incumbents with distribution advantages (Garmin, Apple) and a direct competitor with 200x its capital (Athos). The axis that mattered most — distribution reach — was the one where Enflux was most disadvantaged.

## Business Model

Enflux's primary revenue model was direct hardware sales: the shirt-and-pants set at $249.99 (early-bird Kickstarter) rising to $349–$499 for the developer kit.<sup><a href="https://startupbeat.com/enflux-raises-50k-first-two-days-kickstarter/21808/">[23]</a></sup> The company never disclosed revenue beyond the $120,000 in clothing sales reported at CES 2017.<sup><a href="https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/">[11]</a></sup> Whether a software subscription layer was planned — common in fitness hardware — is not documented in public sources.

The unit economics were structurally challenging. A ten-sensor garment with Bluetooth connectivity, machine-washable construction, and a companion app required significant bill-of-materials cost. At $249.99 retail, the margin available after components, manufacturing, and fulfillment was likely thin. At low volumes — and $120,000 in total sales implies a few hundred units at most — there was no manufacturing scale to reduce per-unit costs.

**Inferred burn rate (labeled as estimate):** With confirmed external funding of approximately $370,000 ($120,000 from YC plus $250,000 founder investment)<sup><a href="https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/">[7]</a></sup> and a team that at peak likely included four to six people, annual burn was probably in the range of $400,000–$600,000 — implying the company was operating on runway measured in months, not years, from the moment of YC graduation. One database lists total funding of $227,621 across four rounds with a last round in April 2018,<sup><a href="https://www.ycombinatorcompanies.com/company/enflux">[14]</a></sup> though this figure conflicts with other sources and should be treated as directional only.

The company never disclosed revenue from its developer API or platform partnerships. The absence of any subscription or licensing revenue disclosure is itself a signal: if the 50 platform partners had been paying relationships, that figure would likely have appeared in press coverage.

## Traction

By January 2017, Enflux had generated $120,000 in clothing sales and signed 50 platform partners for its developer API, including Hasbro and The Jim Henson Company.<sup><a href="https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/">[11]</a></sup> The Kickstarter campaign raised over $86,000 with 17 days remaining against a $100,000 goal in March 2016,<sup><a href="https://startupbeat.com/enflux-raises-50k-first-two-days-kickstarter/21808/">[10]</a></sup> suggesting real consumer demand for the concept. The product had been tested on 500 people prior to launch, including fitness world-record holders, and the form coaching database was built with input from approximately 500 personal trainers.<sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[18]</a></sup>

In the BackAlert phase, the company's Crowdfunder profile claimed 800 systems shipped since September 2017, with customers including Microsoft and Bouygues Construction, and technology partnerships with MIT, NYU, and Virginia Tech.<sup><a href="https://www.crowdfunder.com/enflux">[13]</a></sup> These figures are sourced from founder-controlled crowdfunding profiles and should be treated as low-to-medium confidence. The Tampa Bay Buccaneers and US Olympic team were also cited as users.<sup><a href="https://www.crowdfunder.com/enflux">[24]</a></sup> No independent verification of these claims exists in the public record.

The $120,000 in clothing sales figure is the only independently verified revenue number. At $249.99–$349 per unit, this implies approximately 350–480 units sold — a meaningful proof of concept but far below the volume needed to validate manufacturing processes or achieve sustainable unit economics.

## Post-Mortem

### Primary Cause: Hardware Complexity at Software-Company Funding Levels

The fundamental problem was a mismatch between what Enflux was building and what it had to build it with. A ten-sensor garment with Bluetooth connectivity, machine-washable construction, and a real-time 3D rendering app required capital-intensive manufacturing development. Enflux had approximately $370,000 in confirmed external funding — $120,000 from YC and $250,000 from founders — against a competitor (Athos) that had raised $51 million.<sup><a href="https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/">[7]</a></sup><sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[8]</a></sup>

Hardware startups require capital in three distinct phases: R&D to achieve a working prototype, manufacturing development to achieve consistent yield at acceptable cost, and go-to-market to build distribution. Enflux spent four years and $250,000 of founder capital on the first phase. The YC investment of $120,000 was insufficient to fund the second phase for a product of this complexity. The result was a company that could demonstrate a working product at CES but could not manufacture it at scale.

Hoang's own comments at the Kickstarter launch reveal the tension. Asked about competitive risk from Athos, he said: "It's always gonna be like that, because we've failed often and they know the tech well. That's why we're putting this a year out — a year out of making small tests of every process we go through before we do the full order."<sup><a href="https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/">[2]</a></sup> The manufacturing-first caution was technically correct — rushing a complex hardware product to market produces defects and returns that destroy brand equity. But for a company with months of runway, a one-year shipping delay was existential. The team attempted to address the funding gap through the Kickstarter campaign and subsequent investor outreach, but the total raised across all rounds remained in the low hundreds of thousands of dollars.

### Secondary Cause: Platform Ambiguity Prevented Focused Go-to-Market

From the Kickstarter launch, Enflux described its clothing as a platform for fitness, VR, gaming, physical therapy, dance, and augmented reality.<sup><a href="https://www.digitaltrends.com/wearables/enflux-kickstarter/">[21]</a></sup> By CES 2017, the 50 platform partners included entertainment companies (Hasbro, The Jim Henson Company) alongside fitness and rehabilitation applications. A Unity SDK was built and published on GitHub.

This breadth was strategically understandable — the technology genuinely had applications across all these verticals — but it created a go-to-market problem. Each vertical required different channel relationships, different form factor optimizations, different pricing, and different customer education. A fitness consumer buying a $249 workout outfit has different purchase triggers than an enterprise VR developer buying a $499 developer kit. The team was attempting to serve both simultaneously with limited resources.

The 50 platform partners represent genuine traction, but the nature of those relationships is unclear. If they were unpaid developer integrations rather than revenue-generating contracts, they consumed engineering resources without contributing to the unit economics problem. The entertainment company partnerships (Hasbro, Jim Henson) suggest the team was pursuing B2B licensing as a revenue path — a pivot within a pivot that further diluted focus.

### Tertiary Cause: Category-Level Market Timing

The smart apparel category as a whole struggled during this period. Athos, despite raising $51 million and achieving broader distribution than Enflux, eventually shut down. OMsignal, another smart apparel company, was acquired and its consumer product discontinued. The category faced a structural problem: athletic clothing is a commodity market with razor-thin margins and high consumer price sensitivity. Adding $200–$300 of electronics to a garment that consumers expect to pay $50–$100 for required a value proposition strong enough to justify a 4–6x price premium — and that value proposition had to be immediately legible to a consumer in a retail environment.

The VR pivot angle placed Enflux in the 2016–2017 VR hype cycle. The Chinese VR investor backing cited in one database<sup><a href="https://tracxn.com/d/companies/enflux/__xaOaaJXEqO4L0pLUp_fsr7h1bE4d-8ZDHhqP-2Jevzg/funding-and-investors">[25]</a></sup> — if accurate — would have been secured at the peak of VR enthusiasm. The subsequent contraction of the consumer VR market in 2018–2019 would have eliminated that demand signal entirely.

### The BackAlert Pivot: Logical but Insufficient

The pivot to BackAlert — a single back-mounted posture sensor with AI coaching — was strategically coherent. It simplified the hardware from ten sensors across two garments to a single device, reducing manufacturing complexity and cost. It targeted a larger and more clearly defined problem (back pain affects 80% of adults at some point) with a more defensible B2B sales motion (selling to employers and insurers rather than individual consumers).

The pivot brought in a new CTO, Josh McCoy, suggesting a significant team restructuring.<sup><a href="https://www.fundable.com/enflux">[26]</a></sup> The Crowdfunder profile claimed 800 systems shipped and enterprise customers including Microsoft and Bouygues Construction.<sup><a href="https://www.crowdfunder.com/enflux">[13]</a></sup> These figures, if accurate, represent more commercial traction than the original product achieved.

But the pivot also abandoned Enflux's core technical differentiation. The full-body motion capture capability — ten IMUs, real-time 3D avatar, form coaching across the entire kinetic chain — was what no competitor offered at consumer price points. A single back sensor was a simpler product, but it was also a product that competed directly with established posture wearables (Upright, Lumo Lift) that had more funding, more distribution, and earlier market entry. The BackAlert pivot traded a defensible technical moat for a more crowded and better-funded competitive landscape.

The last confirmed funding activity was April 2018.<sup><a href="https://www.ycombinatorcompanies.com/company/enflux">[14]</a></sup> A patent application was filed in December 2018, suggesting the founders were still active.<sup><a href="https://uspto.report/patent/app/20180369637">[15]</a></sup> By December 2020, Hoang had joined FightCamp.<sup><a href="https://www.crunchbase.com/person/doug-hoang">[16]</a></sup> The company wound down quietly, without a public announcement, somewhere in that two-year window.

### Structural Observation: Smart Apparel as a Feature, Not a Category

The deepest structural problem may be that full-body motion capture clothing was never a standalone product category — it was a feature that larger platforms (Apple Health, Garmin Connect, sports science departments) would eventually absorb. The value of biomechanical coaching depends on longitudinal data, coaching expertise, and integration with training programs — all of which favor platforms with existing user relationships over standalone hardware companies. Enflux was building the sensor layer of a stack that required the coaching layer, the data layer, and the distribution layer to be valuable. With limited resources, it could only build one of those layers well.

## Key Lessons

- **Enflux's funding structure was incompatible with its product complexity from day one.** The company raised $120,000 from YC and $250,000 from founders to build a ten-sensor, machine-washable, Bluetooth-connected garment — a product that required manufacturing development capital an order of magnitude larger. When Athos raised $51 million for a comparable category and still failed, it confirmed that the problem was not Enflux's execution but the capital requirements of the category itself. Hardware startups building novel form factors need to either raise venture capital commensurate with manufacturing complexity or design products simple enough to be funded at seed levels; Enflux attempted neither.

- **Enflux's platform ambition (fitness, VR, gaming, physical therapy, dance) prevented the focused customer development needed to validate any single use case.** By CES 2017, the company had 50 developer partners spanning entertainment and rehabilitation — but only $120,000 in consumer clothing sales. The breadth of the platform strategy consumed engineering resources across multiple verticals simultaneously, while the consumer fitness core — the use case with the clearest purchase trigger and the most press coverage — never received the focused iteration needed to build retention data or word-of-mouth growth.

- **The BackAlert pivot simplified the hardware but eliminated the moat.** Enflux's ten-IMU full-body system had no direct consumer-priced competitor. The single back sensor that replaced it competed against Upright, Lumo Lift, and a growing field of posture wearables with earlier market entry and more funding. The pivot was rational given manufacturing constraints, but it traded a defensible technical position for a crowded market — and the company's crowdfunding-stage traction in the BackAlert phase was insufficient to overcome that competitive disadvantage.

- **A one-year shipping delay at Kickstarter launch, flagged explicitly by TechCrunch in March 2016, proved fatal for a company with months of runway.** Hoang's manufacturing-first caution — "small tests of every process" before the full order — was the correct engineering approach for a complex hardware product. But for a startup with $370,000 in total external funding, a twelve-month delay between campaign and delivery consumed the window in which Kickstarter momentum could have been converted into retail distribution relationships and follow-on investor interest. The caution that protected product quality also exhausted the runway.

- **The smart apparel category's structural failure (Athos shut down despite $51M; OMsignal discontinued its consumer product) suggests Enflux's outcome was partly determined by market dynamics independent of execution quality.** The combination of high hardware cost, consumer price sensitivity in the apparel category, and the difficulty of building recurring revenue from a physical product created conditions where even well-capitalized companies could not achieve sustainable unit economics. Enflux's failure was accelerated by underfunding, but the category itself rewarded no one.

## Sources

1. [Enflux About Us page — Doug Hoang and Mickey Ferri backgrounds](https://www.getenflux.com/about-us/)
2. [TechCrunch: "Enflux, A Smart Body-Tracking Workout Outfit, Launches On Kickstarter" (March 7, 2016)](https://techcrunch.com/2016/03/07/enflux-a-smart-body-tracking-workout-outfit-launches-on-kickstarter/)
3. [VentureBeat: "Enflux's smart fitness apparel tracks your movement to prevent injuries" (February 24, 2016)](https://venturebeat.com/business/enfluxs-smart-fitness-apparel-tracks-your-movement-to-prevent-injuries/)
4. [Y Combinator: Enflux company profile](https://www.ycombinator.com/companies/enflux)
5. [YC Blog: "Enflux (YC W16) Makes Workout Clothes That Double as a Personal Trainer"](https://www.ycombinator.com/blog/enflux-yc-w16-makes-workout-clothes-that-doubles-as-a-personal-trainer)
6. [TechCrunch: "Enflux captures body motion for fun and rehabilitation" (January 4, 2017)](https://techcrunch.com/2017/01/04/enflux-captures-body-motion-for-fun-and-rehabilitation/)
7. [StartupBeat: "Enflux Raises $50K in First Two Days on Kickstarter" (March 11, 2016)](https://startupbeat.com/enflux-raises-50k-first-two-days-kickstarter/21808/)
8. [Digital Trends: "Enflux Kickstarter" (March 8, 2016)](https://www.digitaltrends.com/wearables/enflux-kickstarter/)
9. [Enflux GitHub — Unity SDK (copyright 2017)](https://github.com/efesurekli/EnfluxUnitySDK)
10. [Enflux Crowdfunder profile — BackAlert traction claims](https://www.crowdfunder.com/enflux)
11. [Enflux Fundable profile — BackAlert pivot and Josh McCoy CTO](https://www.fundable.com/enflux)
12. [Tracxn: Enflux funding and investors](https://tracxn.com/d/companies/enflux/__xaOaaJXEqO4L0pLUp_fsr7h1bE4d-8ZDHhqP-2Jevzg/funding-and-investors)
13. [YCombinatorCompanies.com: Enflux funding rounds](https://www.ycombinatorcompanies.com/company/enflux)
14. [USPTO: Patent application US 16/120390 — "Training Systems With Wearable Sensors" (filed December 27, 2018)](https://uspto.report/patent/app/20180369637)
15. [Crunchbase: Doug Hoang — FightCamp role starting December 2020](https://www.crunchbase.com/person/doug-hoang)
16. [RocketReach: Doug Hoang — DockCharged CEO](https://rocketreach.co/doug-hoang-email_3715927)
