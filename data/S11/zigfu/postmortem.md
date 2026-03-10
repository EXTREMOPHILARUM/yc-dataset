# Research Report: Zigfu

## Overview

## Founding Story

Zigfu's origin story begins with a piece of consumer hardware and a founder who couldn't leave it alone.

When Microsoft launched the Kinect in 2010, Amir Hirsch started hacking it immediately. Before Zigfu existed, he had already built motion-based applications for teaching dance routines and military maneuvers — practical experiments that gave him a concrete sense of what gesture-controlled software could and couldn't do. <sup><a href="https://venturebeat.com/ai/zigfu">[2]</a></sup> Hirsch held bachelor's and master's degrees from MIT in mathematics and electrical engineering and computer science, and had previously founded Tinker Heavy Industries, building interactive characters and educational mobile apps for children. He had also worked as an engineer at Quickware, developing a PDP-11/70 replacement system to control nuclear power plants — a background that combined hardware fluency with software product experience. <sup><a href="https://news.mit.edu/2017/mit-alumnus-amir-hirsch-flybrix-lego-drone-kits-0803">[3]</a></sup> <sup><a href="https://grayarea.org/community-entry/amir-hirsch/">[4]</a></sup>

Hirsch co-founded Zigfu with Ted Blackman and the two entered Y Combinator's Summer 2011 batch together. <sup><a href="https://www.ycombinator.com/companies/zigfu">[5]</a></sup> The founding team's most significant early move came approximately one month into the YC program: Hirsch recruited Shlomo Zippel out of PrimeSense — the Israeli firm whose 3D sensor technology Microsoft had licensed to power the Kinect — using $150,000 from SV Angel and the Start Fund, plus an additional $50,000 from Romulus Capital. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[6]</a></sup> Zippel had led the applications and UX team at PrimeSense, giving Zigfu direct insider knowledge of the hardware stack it was building on. <sup><a href="https://thenewstack.io/author/shlomozippel/">[7]</a></sup> Zippel then convinced his PrimeSense colleague Roee Shenberg to relocate from Israel to join the team, completing the four-person founding group. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[8]</a></sup>

The founding thesis was straightforward: gesture control was going to become a mainstream computing interface, and the developer tooling layer was wide open. As Hirsch described it, the goal was to make Kinect development as accessible as possible — binding the OpenNI open-source framework to popular development environments so that any developer could build gesture-controlled applications without needing deep expertise in 3D sensor middleware.

The team's YC interview reportedly included making Paul Graham perform the hokey-pokey as a live demo — a detail that captures both the novelty of the technology and the showmanship required to sell it. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[9]</a></sup>

The team's composition was unusually strong for an early-stage hardware-adjacent startup. Two of the four founders had built the underlying sensor technology from the inside. The CEO had already shipped motion-based software products. The gap — which would prove consequential — was on the business and distribution side, where the team had no prior experience scaling a developer platform.

---

## Timeline

- **2010** — Microsoft Kinect launches; Amir Hirsch begins hacking it immediately, building motion apps for teaching dance routines and military maneuvers. <sup>[[2]](https://venturebeat.com/ai/zigfu)</sup>

- **2011** — Zigfu founded by Amir Hirsch and Ted Blackman; accepted into Y Combinator S11 batch. <sup>[[5]](https://www.ycombinator.com/companies/zigfu)</sup>

- **2011 (one month into YC)** — Zigfu receives $150K from SV Angel/Start Fund and $50K from Romulus Capital; recruits Shlomo Zippel from PrimeSense. Zippel recruits Roee Shenberg from Israel, completing the four-person team. <sup>[[6]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **2011-08-24** — YC S11 Demo Day; Zigfu named one of the "startups to watch." VentureBeat publishes first major press coverage describing the OpenNI/Unity3D bindings with skeleton and hand tracking. <sup>[[10]](https://venturebeat.com/ai/zigfu)</sup>

- **2011-09** — Hirsch tells Paul Graham he plans to raise $2.5M "in a month or two." Graham responds: "no way that's happening." Hirsch begins extensive VC fundraising process. <sup>[[11]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **Late 2011** — Zigfu pivots toward "Zig TV," a motion OS for smart TVs, seeking OEM licensing deals. <sup>[[12]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **2012-01** — Brad Feld of Foundry Group passes on Zigfu, characterizing it as a likely $20–50M acquisition target, not a venture-scale standalone business. <sup>[[13]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **2012-03-16** — Zigfu commercially launches the ZDK for Unity3D at $200/developer seat via a Show HN post — nearly a year after the product was ready to sell. <sup>[[14]](https://news.ycombinator.com/item?id=3711142)</sup>

<media-hn url="https://news.ycombinator.com/item?id=3711142" title="Zigfu Dev Kit for Kinect and Unity3D" points="null" comments="null"></media-hn>

- **2012-04** — SDK licensing and contracting revenue cannot sustain the four-person team. Zigfu has no runway left to build new products. Ted Blackman, the first co-founder, departs. <sup>[[15]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **2012-07** — Roee Shenberg and Shlomo Zippel take on outside contracting work and begin building FundersClub, effectively departing Zigfu. <sup>[[15]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **2012-10-01** — Amir Hirsch publishes "Fear and Loathing at Zigfu" post-mortem. He is the sole remaining full-time employee, sustaining himself on licensing and contracting revenue. <sup>[[1]](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)</sup>

- **2014-07-24** — Last commits to Zigfu's GitHub repositories (ZDKForUnity3D, ZigJS, OpenNIBrowserPlugin, Sushi-Warrior), marking the end of any active development. <sup>[[16]](https://github.com/zigfu)</sup>

- **2015** — Amir Hirsch co-founds Flybrix, building LEGO-based drone kits. <sup>[[17]](https://news.mit.edu/2017/mit-alumnus-amir-hirsch-flybrix-lego-drone-kits-0803)</sup>

---

## What They Built

Zigfu's core product was a software development kit that made it dramatically easier to build applications controlled by gesture and body movement. To understand what this meant in practice, it helps to understand the problem it solved.

The Microsoft Kinect used a depth sensor — technology originally developed by PrimeSense — to track a user's skeleton in three dimensions without any physical controller. Developers who wanted to build Kinect-powered applications in 2011 faced a fragmented tooling landscape: they needed to work with OpenNI (an open-source framework for depth sensors), PrimeSense NITE (a middleware layer that translated raw sensor data into recognizable gestures and skeleton positions), and then somehow connect all of that to whatever game engine or application framework they were using. <sup><a href="https://venturebeat.com/ai/zigfu">[18]</a></sup> Each layer required specialized knowledge, and the connections between them were manual and error-prone.

Zigfu collapsed that stack into a single, accessible SDK. As Hirsch described it at Demo Day: "We've bound OpenNI to the Unity game engine to provide high-quality cross-platform development. In Unity, we expose skeleton tracking and hand tracking; and on top of hand-tracking, we provide user interface components like menus, lists and feeds." <sup><a href="https://venturebeat.com/ai/zigfu">[19]</a></sup> A developer using Zigfu's ZDK (Zigfu Development Kit) could open Unity3D — the dominant game engine of the era — and immediately access skeleton tracking, hand gesture detection, and pre-built UI components without writing any sensor integration code.

<media-image src="https://venturebeat.com/wp-content/uploads/2011/08/kinect.jpg" alt="Microsoft Kinect sensor — the hardware platform Zigfu built its developer tools on top of" caption="VentureBeat's August 2011 article on Zigfu used this Kinect image to illustrate the hardware platform Zigfu was building on. The article, published the day of YC S11 Demo Day, was the company's first major press coverage."></media-image>

The product surface was broader than just Unity3D. Zigfu also built:

- **ZigJS**: JavaScript and HTML5 bindings that let web developers add gesture control to browser-based applications — a significant technical achievement given the complexity of bridging sensor hardware to a browser runtime.
- **OpenNI Browser Plugin**: A one-click browser plugin that enabled Kinect-controlled web experiences without requiring users to install complex drivers or middleware.
- **Sample apps and scenes**: Pre-built Unity3D scenes demonstrating skeleton tracking, hand gesture menus, and other interaction patterns that developers could use as starting points.
- **Sushi Warrior**: A gesture-controlled game the team began building as a content play — reasoning, as Hirsch put it, that "Valve didn't just start with Steam, they had Half Life first." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[20]</a></sup>

<media-image src="https://github.com/zigfu/ZDKForUnity3D/raw/master/doc/ZDK_screenshot.png" alt="Zigfu ZDK for Unity3D — GitHub repository screenshot showing the development kit structure" caption="Zigfu's ZDKForUnity3D GitHub repository — the open-source Kinect development kit for Unity3D, showing the project structure including skeleton tracking, hand gesture detectors, and sample scenes."></media-image>

The commercial ZDK for Unity3D launched in March 2012 at $200 per developer seat, with a watermarked trial version available for free. <sup><a href="https://news.ycombinator.com/item?id=3711142">[14]</a></sup> The product supported both the Microsoft Kinect and the ASUS Xtion depth sensor, making it hardware-agnostic within the depth-sensing category.

Microsoft's Channel9 developer platform featured the ZDK — a meaningful third-party validation that the tooling was production-quality. <sup><a href="https://channel9.msdn.com/coding4fun/kinect/ZDK--Zigfu-Development-Kit--Commercial-Kinect-Development-library-for-Unity3D-and-JavaScript">[21]</a></sup>

The product evolved through several strategic phases. The initial focus was the developer SDK. After Demo Day, the team pivoted toward "Zig TV" — a motion operating system for smart TVs that Zigfu would license to OEM hardware manufacturers. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[12]</a></sup> This represented a shift from selling to developers to selling to hardware companies — a fundamentally different sales motion with longer cycles and larger contract values. The Sushi Warrior game was a third strategic direction, attempting to build a content library that would justify a proprietary distribution platform.

What made Zigfu different from alternatives was primarily the depth of its founders' hardware knowledge. With two former PrimeSense engineers on the team, Zigfu could build integrations that competitors without that insider access could not easily replicate. The cross-platform approach — supporting Unity3D, JavaScript, and browser environments simultaneously — also differentiated it from narrower tools that targeted only one development environment.

---

## Market Position

### Target Customers

Zigfu initially targeted independent game developers and creative technologists who wanted to build gesture-controlled applications but lacked the expertise to work directly with depth sensor middleware. The Unity3D integration was a deliberate choice: Unity was the dominant engine for independent game development, and its developer community represented the most accessible early adopter pool for a new interaction paradigm.

The company's pivot toward "Zig TV" shifted the target customer to consumer electronics OEMs — smart TV manufacturers who might license a motion OS to differentiate their hardware. A third customer segment emerged organically: enterprise clients building interactive installations, kiosks, and digital signage. This B2B segment proved to be the most commercially durable, with Zigfu securing OEM licensing agreements with "a few large companies" for Kinect-controlled digital signage deployments. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[22]</a></sup>

The breadth of customer targets — indie developers, TV OEMs, enterprise signage buyers — reflected a team that had not yet found a single segment willing to pay at the scale needed to sustain a venture-backed company.

### Market Size

The gesture-control developer tools market in 2011–2012 was genuinely nascent. Microsoft had sold approximately 8 million Kinect units in the first 60 days after launch — a record-setting pace — but the installed base of Kinect-equipped developers was a small fraction of that number. <sup><a href="https://venturebeat.com/ai/zigfu">[23]</a></sup> Developer tool businesses require a large underlying hardware install base to generate meaningful revenue at a per-seat pricing model; at $200 per developer seat, Zigfu would have needed tens of thousands of paying developers to reach venture-scale revenue.

Brad Feld of Foundry Group articulated the market ceiling problem directly when he passed on the investment in early 2012: "This sounds like something that will sell to Google or Microsoft for $20–50M and I'm just not interested in that." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[13]</a></sup> Feld's framing — that the realistic exit was an acqui-hire or small acquisition, not an independent public company — reflected a consensus view among institutional investors that the market ceiling for gesture-control developer tools was insufficient to justify venture-scale capital deployment.

The digital signage and interactive installation market was more immediately monetizable but also more fragmented and project-based, making it difficult to build recurring revenue at scale.

### Competition

Zigfu's competitive landscape in 2011–2012 included several categories of potential rivals:

**Microsoft itself** was the most significant structural competitive threat. Microsoft controlled the Kinect hardware and had its own Kinect SDK (released in beta in June 2011, the same summer Zigfu entered YC). Microsoft's SDK was free and officially supported, which created a permanent pricing pressure on any third-party tooling. Zigfu's differentiation was cross-platform support (Microsoft's SDK was Windows-only) and the Unity3D integration, which Microsoft did not provide natively.

**OpenNI ecosystem tools** represented the open-source alternative. OpenNI itself was free, and developers willing to invest time in integration could build directly on it without paying for Zigfu's SDK. Zigfu's value proposition was time savings and abstraction quality — a real but soft competitive moat.

**Other Kinect hacking communities** — including the large community that had formed around the open-source libfreenect driver — represented a developer culture that was accustomed to free tools and DIY integration. Charging $200 for a developer seat in this community required overcoming a cultural resistance to paid tooling.

The competitive dynamics ultimately reinforced the market size problem: the developers most likely to pay for Zigfu's SDK were professional developers building commercial applications, but the commercial application market for Kinect was still too small in 2011–2012 to generate the revenue Zigfu needed.

---

## Business Model

Zigfu pursued three revenue streams across its operating life, none of which scaled to sustain the team.

The primary model was a per-seat SDK license: the ZDK for Unity3D sold at $200 per developer seat, with a free watermarked trial version. <sup><a href="https://news.ycombinator.com/item?id=3711142">[14]</a></sup> This is a standard developer tools pricing model, but it requires high volume to generate meaningful revenue at $200 per unit.

The second stream was OEM licensing: Zigfu signed agreements with "a few large companies" to embed its browser plugin in Kinect-controlled digital signage deployments. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[22]</a></sup> OEM licensing generates larger per-contract revenue but requires longer sales cycles and is difficult to scale without a dedicated enterprise sales function.

The third stream was project-based contracting: Hirsch and the team took on paid work building Kinect-powered interactive installations and kiosks for clients. This was the most immediately monetizable activity but the least scalable — it traded founder time directly for revenue.

By October 2012, the combination of passive SDK licensing and contracting revenue was sufficient to cover Hirsch's personal expenses, but not to pay a team. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[22]</a></sup> The business model worked as a lifestyle business; it never worked as a venture-scale company.

---

## Traction

Zigfu's traction was real but thin relative to venture expectations.

At YC S11 Demo Day in August 2011, Zigfu was named one of the "startups to watch" in the class — a signal of strong presentation quality and product differentiation, if not yet commercial scale. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[24]</a></sup>

CB Insights records that Zigfu "supported thousands of developers" with its cross-platform tools — a figure that, if accurate, represents meaningful developer adoption for a niche hardware platform. <sup><a href="https://www.cbinsights.com/company/zigfu">[25]</a></sup> However, no data is available on how many of those developers converted to paid SDK licenses.

Microsoft's Channel9 developer platform featured the ZDK, providing third-party validation from the hardware manufacturer itself. <sup><a href="https://channel9.msdn.com/coding4fun/kinect/ZDK--Zigfu-Development-Kit--Commercial-Kinect-Development-library-for-Unity3D-and-JavaScript">[21]</a></sup> This was a meaningful signal that Zigfu's tooling met professional quality standards.

On the commercial side, Zigfu secured OEM licensing agreements with multiple large companies for digital signage deployments. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[22]</a></sup> By October 2012, passive licensing revenue covered Hirsch's personal expenses — proof that the product had genuine market value, even if not at venture scale.

GitHub commits to Zigfu's repositories continued until July 2014 — nearly two years after the team had dissolved — suggesting a persistent developer community that continued using and contributing to the platform even after the company effectively ceased operations. <sup><a href="https://github.com/zigfu">[16]</a></sup>

<media-tweet url="https://twitter.com/zigfu" author="@zigfu" date="2011-08-01" text="ZigFu enables Kinect development in HTML5/JavaScript, Flash and Unity3D"></media-tweet>

---

## Post-Mortem

Zigfu's failure was not a single catastrophic event. It was a slow-motion collapse driven by a sequence of compounding decisions, each individually defensible, collectively fatal. The primary cause was a fundraising strategy that consumed the runway needed to build the commercial traction that would have made fundraising possible.

### Primary Cause: The Fundraising Trap

In September 2011 — one month after Demo Day — Amir Hirsch told Paul Graham that his goal was to raise $2.5 million "in a month or two." Graham's response was unambiguous: "no way that's happening." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[11]</a></sup> Hirsch proceeded anyway.

For the next several months, Hirsch spent the majority of his time pitching venture capital firms. The results were consistent: investors were interested in the technology but skeptical of the market size. Andreessen Horowitz committed to joining a seed round contingent on finding a lead investor — a conditional commitment that never converted because no lead materialized. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[26]</a></sup> Brad Feld passed in early 2012, explicitly citing the acquisition-scale ceiling. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[13]</a></sup>

Hirsch's own post-mortem is direct about the cost: "In retrospect, I wasted an incredible amount of valuable time showing these demos to investors trying to raise a seed round." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[27]</a></sup> The time spent in investor meetings was time not spent building the commercial product, acquiring customers, or generating the revenue metrics that would have made the fundraising conversations more productive.

The trap was self-reinforcing: without traction data, investors passed; without investment, the team couldn't build traction fast enough; without traction, the next investor passed.

### Secondary Cause: The Commercial Launch That Came a Year Too Late

The ZDK for Unity3D — Zigfu's primary commercial product — launched in March 2012. <sup><a href="https://news.ycombinator.com/item?id=3711142">[14]</a></sup> By Hirsch's own admission, the product was ready to sell nearly a year earlier: "In retrospect, we could have been selling this for nearly a year by the time we finally got around to it." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[28]</a></sup>

The twelve-month delay in launching a commercial product is the single most damaging execution failure in Zigfu's history — and the most recoverable one that wasn't recovered. Had the team launched the ZDK commercially in mid-2011, immediately after Demo Day, it would have had twelve additional months of revenue data, customer feedback, and traction metrics to show investors. The fundraising conversations that failed in late 2011 and early 2012 might have had different outcomes with a year of $200/seat SDK sales behind them.

Instead, the team spent that year pursuing strategic pivots (Zig TV, Sushi Warrior) and investor meetings, while the commercial product sat unlaunched. By the time the ZDK went on sale in March 2012, the team had approximately one month of runway left before the first co-founder departed.

### Tertiary Cause: Platform Dependency on Hardware Zigfu Didn't Control

Zigfu's entire product depended on hardware and middleware controlled by third parties: the Microsoft Kinect, the ASUS Xtion, OpenNI, and PrimeSense NITE. <sup><a href="https://venturebeat.com/ai/zigfu">[18]</a></sup> This created existential platform risk that sophisticated investors recognized and that ultimately materialized.

Microsoft controlled the Kinect hardware roadmap and released its own competing SDK for free. PrimeSense — the company whose technology powered the Kinect and whose engineers had co-founded Zigfu — was acquired by Apple in 2013, which subsequently shut down the OpenNI framework that Zigfu's SDK depended on. While this acquisition occurred after Zigfu's effective wind-down, it illustrates the structural fragility of building a developer platform on top of hardware and middleware you don't control.

Brad Feld's "acquisition target" framing was not just a market size observation — it was a recognition that Zigfu's strategic value was its technical expertise and relationships, not a durable competitive moat. A company whose core technology depends on a third party's hardware and middleware is always one product decision away from obsolescence.

### Quaternary Cause: Strategic Diffusion Across Too Many Pivots

Between Demo Day in August 2011 and the ZDK launch in March 2012, Zigfu pursued at least three distinct strategic directions simultaneously: the developer SDK, Zig TV (motion OS for smart TVs), and Sushi Warrior (a gesture-controlled game to bootstrap a distribution platform). <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[12]</a></sup> <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[20]</a></sup>

Each pivot represented a coherent strategic logic in isolation. Zig TV addressed the consumer market ceiling problem by targeting OEM licensing deals with larger contract values. Sushi Warrior addressed the chicken-and-egg problem of building a platform without content. But pursuing all three simultaneously with a four-person team and limited runway meant none received the focused execution needed to succeed.

The Zig TV pivot in particular represented a fundamental change in sales motion — from selling $200 SDK licenses to developers online, to negotiating OEM licensing agreements with consumer electronics manufacturers. These are entirely different businesses with different sales cycles, different buyer personas, and different organizational requirements. A four-person startup cannot execute both simultaneously.

### Team Dissolution: A Gradual Unraveling

By April 2012 — one month after the commercial ZDK launch — it was clear that SDK and contracting revenue could not sustain the team. Ted Blackman departed at the end of April 2012. In July 2012, Roee Shenberg and Shlomo Zippel took on outside contracting work and began building FundersClub. <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[29]</a></sup>

By October 2012, Hirsch was the sole full-time employee, operating Zigfu as a one-person licensing and consulting business. There was no formal shutdown announcement — the company simply ran out of people before it ran out of product. GitHub commits continued until July 2014, suggesting the developer community outlasted the company itself. <sup><a href="https://github.com/zigfu">[16]</a></sup>

<media-image src="https://web.archive.org/web/20120901120000im_/http://zigfu.com/" alt="Archived Zigfu homepage circa 2012 showing the Kinect developer platform landing page" caption="Wayback Machine snapshot of zigfu.com circa 2012 — the homepage for Zigfu's gesture-controlled developer platform, showing their Kinect SDK portal and app store."></media-image>

---

## Key Lessons

- **Launch the commercial product before raising the next round.** Zigfu had a sellable product in mid-2011 and didn't put a buy button on it until March 2012. The twelve-month gap between product readiness and commercial launch cost the company the revenue data it needed to raise a Series A. For unconventional products that don't fit standard investor pattern-matching, Hirsch concluded: "you need big potential revenue numbers and evidence of traction." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[30]</a></sup> Traction is a prerequisite for VC fundraising, not a parallel track.

- **Match your fundraising strategy to your investor type.** Zigfu spent most of its runway pitching venture capital firms who were structurally unable to invest in a company with a $20–50M acquisition ceiling. Hirsch's post-mortem conclusion: "I realized that I should have been working on getting influential private angel investors on board first before talking to venture capital firms." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[31]</a></sup> Angels bet on people and visions; VCs pattern-match to market size. Unconventional companies need unconventional investors.

- **Platform dependency on hardware you don't control is an existential risk, not just a business risk.** Zigfu's entire product surface depended on Microsoft Kinect, PrimeSense NITE, and OpenNI — all controlled by third parties. PrimeSense's 2013 acquisition by Apple, which shut down OpenNI, would have killed Zigfu's product even if the company had survived its fundraising challenges. Building a developer platform requires either controlling the underlying hardware or having contractual protections against platform changes.

- **Strategic pivots consume more runway than they appear to.** Each of Zigfu's pivots — from developer SDK to Zig TV to Sushi Warrior — was individually rational but collectively destructive. A four-person team with limited runway cannot execute three different business models simultaneously. The cost of each pivot is not just the engineering time; it's the sales motion, the customer relationships, and the investor narrative that must be rebuilt from scratch.

- **Co-founder financial runway is a strategic asset.** Hirsch identified personal financial independence as a structural enabler of better decision-making: "It helps if you and your co-founders have saved up enough money before you started so that you don't need a salary." <sup><a href="http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html">[32]</a></sup> Founders who need salaries make decisions under financial pressure that founders with personal runway do not. The ability to extend company runway without dilution — by not drawing salaries — is a meaningful competitive advantage in the early stages.

---

## Sources

1. [Amir Hirsch, "Fear and Loathing at Zigfu: My YCombinator Experience," October 1, 2012](http://fpgacomputing.blogspot.com/2012/10/fear-and-loathing-at-zigfu-my.html)
2. [VentureBeat, "Zigfu makes it easy to build Kinect apps," August 24, 2011](https://venturebeat.com/ai/zigfu)
3. [MIT News, "MIT alumnus Amir Hirsch builds LEGO drone kits with Flybrix," August 3, 2017](https://news.mit.edu/2017/mit-alumnus-amir-hirsch-flybrix-lego-drone-kits-0803)
4. [Gray Area Foundation, Amir Hirsch community profile](https://grayarea.org/community-entry/amir-hirsch/)
5. [Y Combinator, Zigfu company profile](https://www.ycombinator.com/companies/zigfu)
6. [CB Insights, Zigfu company profile](https://www.cbinsights.com/company/zigfu)
7. [The New Stack, Shlomo Zippel author profile](https://thenewstack.io/author/shlomozippel/)
8. [Tracxn, Zigfu company profile](https://tracxn.com/d/companies/zigfu/__qkaijUxhC_Ik7noxlz6Uc5xsXOPrQZlracHDrlHWUOs)
9. [Hacker News, "Zigfu Dev Kit for Kinect and Unity3D," March 16, 2012](https://news.ycombinator.com/item?id=3711142)
10. [GitHub, Zigfu organization](https://github.com/zigfu)
11. [The Org, Shlomo Zippel at Whisper.ai](https://theorg.com/org/whisper/org-chart/shlomo-zippel)
12. [Crunchbase, Zigfu organization](https://www.crunchbase.com/organization/zigfu)
13. [Microsoft Channel9, "ZDK – Zigfu Development Kit – Commercial Kinect Development library for Unity3D and JavaScript"](https://channel9.msdn.com/coding4fun/kinect/ZDK--Zigfu-Development-Kit--Commercial-Kinect-Development-library-for-Unity3D-and-JavaScript)
14. [Wayback Machine, zigfu.com archive](https://web.archive.org/web/20120601000000*/zigfu.com)
