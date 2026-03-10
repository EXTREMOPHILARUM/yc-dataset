# Research Report: Call9

## Overview

Call9 was a Brooklyn-based healthcare startup that embedded paramedics and nurses inside skilled nursing facilities 24/7, connecting them via a proprietary telemedicine platform to remote emergency medicine physicians within one minute.Founded in 2015 by ER physician Timothy Peck, Stanford radiology fellow Celina Tenev, and Stanford computer scientist XiaoSong Mu, the company raised $34 million in venture capital and conducted more than 150,000 telemedicine encounters before shutting down in June 2019.

Its clinical results were peer-reviewed and genuine: an 80% reduction in unnecessary hospital transfers, saving an estimated $8 million per year per 200-bed facility.The company did not fail because its product failed.

It failed because Medicare's pre-COVID telehealth reimbursement rules capped revenue from urban nursing homes, a controlling investor pushed a fee-for-service strategy that contradicted the company's value-based care model, and the resulting strategic paralysis prevented a Series C from closing.Nine months after Call9 shut down, CMS removed the very restrictions that had made its business model unworkable.

<report-gallery>
<media-image src="https://techcrunch.com/wp-content/uploads/2016/01/call9_logo.png?w=738" alt="TechCrunch article: Call9 Raises $10 Million Series A Led by Index Ventures" caption="January 2016 — Call9 closes a $10M Series A led by Index Ventures, with backing from Anne Wojcicki and Joe Lonsdale. The company was riding high, its nursing-home telemedicine model drawing serious institutional money. Three years later, a Medicare reimbursement rule would unravel everything."></media-image>
<media-image src="https://techcrunch.com/wp-content/uploads/2015/07/callinterface.png?w=169" alt="Call9 Delivers On-Demand Doctors In Emergency Situations | TechCrunch" caption="The Call9 interface as it appeared at launch in July 2015 — a paramedic or nurse inside a skilled nursing facility could connect a frail elderly patient to a remote ER physician within sixty seconds, bypassing the 911 call that would otherwise guarantee a traumatic hospital transfer. The product worked. The reimbursement system didn't."></media-image>
</report-gallery>

## Founding Story

Timothy Peck spent years watching the same scene repeat itself in emergency rooms. Elderly nursing home residents — many with dementia, many already frail — would arrive by ambulance in acute distress, only to deteriorate further in the chaos of a busy ER. The hospital environment itself was making them worse. Peck, who had practiced emergency medicine at Beth Israel Deaconess Medical Center in Boston, became convinced that the problem was structural: the only tool nursing homes had in a medical emergency was a phone call to 911, which guaranteed a hospital transfer regardless of whether one was medically necessary.<sup><a href="https://medcitynews.com/2019/06/new-york-telemedicine-startup-call9-winding-down-operations/">[1]</a></sup>

Peck met Celina Tenev, a postdoctoral radiology fellow at Stanford, while both were working part-time at a now-defunct startup. They shared a conviction that the patient experience — specifically the hours spent waiting in an ER — was a solvable problem.<sup><a href="https://techcrunch.com/2019/07/01/venture-backed-telemedicine-startup-call9-is-shutting-down/">[2]</a></sup> XiaoSong Mu, a Stanford computer science graduate, joined as the technical co-founder. The combination of clinical credibility and engineering capability was deliberate: Peck understood that a product touching life-or-death decisions in nursing homes would need to earn trust from both patients and regulators.

<media-image src="https://techcrunch.com/wp-content/uploads/2015/07/call9-founders.jpg" alt="Call9 founders Timothy Peck, Celina Tenev, and XiaoSong Mu" caption="Call9 co-founders at launch in July 2015 — Timothy Peck (ER physician), Celina Tenev (Stanford radiology fellow), and XiaoSong Mu (Stanford CS grad). Photo from TechCrunch's original launch coverage."></media-image>

The team applied to Y Combinator in early 2015 with what was then just an idea, four months before their public launch.<sup><a href="https://techcrunch.com/2015/07/20/call9-delivers-on-demand-doctors-in-emergency-situations/">[3]</a></sup> Acceptance into the Summer 2015 batch provided early capital and institutional credibility. But Peck's most consequential pre-launch decision was not a pitch or a product sprint — it was moving into a nursing home. He lived on a cot inside a skilled nursing facility for three months, observing patient care around the clock, building relationships with staff, and establishing the company's first operational foothold.<sup><a href="https://www.cnbc.com/2019/06/25/call9-a-start-up-selling-digital-medical-services-to-nursing-homes-is-shutting-down-operations.html">[4]</a></sup> That immersion produced Call9's first client: Central Island Healthcare in Plainview, Long Island.

The client relationship had an immediate strategic consequence. Call9 was initially based in Palo Alto, the default home of YC companies. But serving nursing homes in the New York metro area from California was operationally untenable. The company relocated to Brooklyn, anchoring itself geographically to its market — a move that would define its entire commercial trajectory.<sup><a href="https://www.builtinnyc.com/articles/call9-silicon-valley-nyc-relocation">[5]</a></sup>

The founding vision was explicit from the start: replace the 911 call as the default emergency response tool in nursing homes, and eventually redefine emergency medicine more broadly. The YC batch gave the team a runway to test that thesis. What it could not give them was a Medicare reimbursement code that matched what they were building.

---

## Timeline

- **Early 2015** — Timothy Peck, Celina Tenev, and XiaoSong Mu found Call9; apply to Y Combinator with an early-stage idea<sup>[[3]](https://techcrunch.com/2015/07/20/call9-delivers-on-demand-doctors-in-emergency-situations/)</sup>
- **2015** — Peck lives in a nursing home for three months to understand patient experience and establish the company's first client relationship<sup>[[4]](https://www.cnbc.com/2019/06/25/call9-a-start-up-selling-digital-medical-services-to-nursing-homes-is-shutting-down-operations.html)</sup>
- **2015** — Accepted into Y Combinator Summer 2015 batch; initially based in Palo Alto<sup>[[6]](https://techcrunch.com/2015/07/20/call9-delivers-on-demand-doctors-in-emergency-situations/)</sup>
- **July 2015** — Call9 publicly launches out of YC S15, announcing the on-demand ER doctor platform for nursing homes<sup>[[6]](https://techcrunch.com/2015/07/20/call9-delivers-on-demand-doctors-in-emergency-situations/)</sup>

<media-hn url="https://www.ycombinator.com/blog/call9-yc-s15-dispatches-an-er-doctor-to-a-medical-emergency-within-1-minute/" title="Call9 (YC S15) Provides An ER Doctor To Assist In A Medical Emergency Within 1 Minute" points="" comments=""></media-hn>

- **2015** — Raises Seed round with Kapor Capital participating; relocates from Silicon Valley to Brooklyn, NY after signing first client (Central Island Healthcare, Long Island)<sup>[[7]](https://tracxn.com/d/companies/call9/__kGd0zB86icGGsHc9iy5PmR2EXRxCau3EMyk3mgPDATQ/funding-and-investors)</sup>
- **January 14, 2016** — Raises $10M Series A led by Index Ventures; operating in 3 nursing homes with 12 full-time employees and 130 doctors on standby; 55% ER trip prevention rate reported<sup>[[8]](https://techcrunch.com/2016/01/14/call9-raises-10-million-series-a-led-by-index-ventures/)</sup>

<media-image src="https://techcrunch.com/wp-content/uploads/2016/01/call9_logo.png?w=738" alt="TechCrunch article: Call9 Raises $10 Million Series A Led by Index Ventures" caption="TechCrunch's January 14, 2016 Series A announcement — Call9 raised $10M led by Index Ventures, with investors including Anne Wojcicki (23andMe), Joe Lonsdale (Palantir), and Ali Rowghani (YC Continuity Fund)."></media-image>

- **September 14, 2017** — Raises $24M Series B led by Redmile Group; Redmile's Rob Faulkner joins the board; Precision Health Economics study published showing 80% hospital visit avoidance rate<sup>[[9]](https://www.finsmes.com/2017/09/call9-raises-24m-in-series-b-funding.html)</sup>
- **February 2018** — CNBC publishes major profile on Peck's founding story (living in nursing home), one of the most-read stories about the company<sup>[[10]](https://www.cnbc.com/2019/06/25/call9-a-start-up-selling-digital-medical-services-to-nursing-homes-is-shutting-down-operations.html)</sup>
- **2019** — Company peaks at approximately 200 employees, 12 nursing homes, and 10 Medicare Advantage payer contracts<sup>[[11]](https://skillednursingnews.com/2019/06/once-backed-with-34m-skilled-nursing-telehealth-provider-call9-to-shut-down/)</sup>
- **2019** — Redmile Group holds >50% controlling interest; pushes fee-for-service strategy; strategic conflict with Peck's value-based care mission intensifies<sup>[[12]](https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback)</sup>
- **2019** — Series C fundraising process fails; no new round closes<sup>[[13]](https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback)</sup>
- **Spring 2019** — Call9's cash falls below its debt obligations to Western Technology Investment; WTI exercises lien rights in a "friendly foreclosure"<sup>[[14]](https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback)</sup>
- **June 25, 2019** — Call9 announces shutdown, laying off approximately 100 employees<sup>[[15]](https://www.cnbc.com/2019/06/25/call9-a-start-up-selling-digital-medical-services-to-nursing-homes-is-shutting-down-operations.html)</sup>
- **July 26, 2019** — Crain's New York reports Peck plans comeback under "Call9 Medical" name with WTI backing; Peck retains IP and branding rights<sup>[[12]](https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback)</sup>
- **2019** — Peck takes position at IDEO healthcare innovation practice<sup>[[16]](https://skillednursingnews.com/2020/05/as-cms-relaxes-rules-on-telehealth-skilled-nursing-startup-call9-sees-second-chance-at-success/)</sup>
- **March 2020** — CMS dramatically expands Medicare telehealth reimbursement rules in response to COVID-19, removing the rural-only restriction that had structurally undermined Call9's business model<sup>[[17]](https://skillednursingnews.com/2020/05/as-cms-relaxes-rules-on-telehealth-skilled-nursing-startup-call9-sees-second-chance-at-success/)</sup>
- **April 2020** — Peck founds Curve Health, rebuilding on Call9's technology platform<sup>[[18]](https://www.fiercehealthcare.com/tech/founder-shuttered-call9-started-a-new-telehealth-venture-here-s-why-he-thinks-curve-health)</sup>
- **October 29, 2020** — Curve Health raises $6M seed round led by Lightspeed Venture Partners, with Kapor Capital re-participating<sup>[[19]](https://skillednursingnews.com/2020/10/call9-founders-new-venture-curve-health-raises-6m-in-skilled-nursing-tech-push/)</sup>

---

## What They Built

Call9's core product was a telemedicine platform designed to replace the 911 call as the default emergency response tool inside skilled nursing facilities. When a nursing home patient showed signs of a medical emergency — chest pain, difficulty breathing, a fall — staff could activate the Call9 system and have a board-certified emergency medicine physician on a live video call within one minute, rather than waiting an average of 64 minutes for an ER physician after a 911 transfer.<sup><a href="https://www.ycombinator.com/blog/call9-yc-s15-dispatches-an-er-doctor-to-a-medical-emergency-within-1-minute/">[20]</a></sup>

The product had three interlocking components that made it operationally distinct from standard telemedicine.

**The On-Site Clinical Care Specialist.** The most expensive and most important element was a human being. Call9 embedded a paramedic, EMT, or nurse — branded internally as a "Clinical Care Specialist" — inside each nursing home 24 hours a day, seven days a week.<sup><a href="https://www.fiercehealthcare.com/tech/tech-startup-call9-shutting-down-operations-telehealth-services-to-nursing-homes">[21]</a></sup> This person was not a nursing home employee. They were a Call9 employee, trained to Call9's protocols, and their presence was what made the telemedicine encounter clinically meaningful. A video call without someone at the bedside who could perform procedures was insufficient for emergency medicine. The CCS was the hands of the remote physician.

**The Mobile Emergency Kit.** Call9 distributed physical equipment to each facility: an EKG machine, an ultrasound machine, and the tools necessary to perform bedside laboratory tests.<sup><a href="https://www.ycombinator.com/blog/call9-yc-s15-dispatches-an-er-doctor-to-a-medical-emergency-within-1-minute/">[20]</a></sup> Data from these devices uploaded to the cloud in real time, giving the remote physician the same diagnostic information they would have in an ER — without the patient leaving the building. This hardware layer was what separated Call9 from a simple video chat service. It also created significant per-facility capital costs and logistical complexity.

**The Telemedicine Platform.** The software connected the on-site CCS to a pool of remote emergency medicine physicians via video. The physician could see the patient, review real-time diagnostic data, and direct the CCS through examination and treatment steps. The platform also included communication tools for families and caregivers, consistent with the company's stated emphasis on patient-centered care.

The user experience for a nursing home was straightforward in concept: a staff member activated the Call9 system, the on-site CCS arrived at the bedside, the remote physician joined via video, and a treatment decision was made in real time. If the patient needed a hospital, the physician ordered the transfer. If not — and in 80% of cases, they did not — the patient was treated in place.<sup><a href="https://www.vcnewsdaily.com/call9/venture-capital-funding/tkfpqskyqf">[22]</a></sup>

What made Call9 different from alternatives was the combination of on-site clinical staff and diagnostic hardware. Pure telemedicine platforms of the era offered video access to physicians but no physical presence. Call9's model was closer to a mobile urgent care unit permanently stationed inside each facility. That distinction was clinically meaningful — and economically punishing. The company was, in practice, a staffing company and a hardware distributor as much as a software company, with cost structures to match.

The company also explored adjacent services: a partnership with Lyft for patient transportation and a community paramedicine division using its emergency doctor network.<sup><a href="https://www.failory.com/cemetery/call9">[23]</a></sup> These expansions suggest the team was testing whether the CCS workforce and physician network could generate revenue beyond the nursing home context, though neither line became a significant part of the business before the shutdown.

---

## Market Position

### Target Customers

Call9's primary customers were skilled nursing facilities (SNFs) — the roughly 15,000 licensed nursing homes in the United States that house approximately 1.3 million residents at any given time, the majority of whom are elderly Medicare or Medicaid beneficiaries. Within that universe, Call9 focused on facilities in the New York metropolitan area, expanding to the Albany region before shutting down.<sup><a href="https://skillednursingnews.com/2019/06/once-backed-with-34m-skilled-nursing-telehealth-provider-call9-to-shut-down/">[24]</a></sup>

The company's secondary customers were health insurers — specifically Medicare Advantage plans, which have financial incentives to reduce unnecessary hospitalizations. Call9 signed 10 payer contracts with Medicare Advantage plans including Anthem Blue Cross and Blue Shield, Aetna, UnitedHealthcare, and Healthfirst.<sup><a href="https://skillednursingnews.com/2019/06/once-backed-with-34m-skilled-nursing-telehealth-provider-call9-to-shut-down/">[25]</a></sup> These payers were theoretically aligned with Call9's mission: every avoided hospital transfer saved them money. In practice, the relationship was more complicated, as discussed in the Post-Mortem section.

The end beneficiaries — nursing home residents and their families — were not paying customers but were central to the product's value proposition. Call9's emphasis on including families in real-time communications was a deliberate differentiator from the standard nursing home emergency protocol, which typically involved a 911 call and a family notification hours later.

### Market Size

The financial opportunity in skilled nursing facility emergency care was substantial. Call9's own research, conducted by Precision Health Economics, estimated that its platform saved approximately $8 million per year for every 200-bed nursing home by avoiding unnecessary hospital transfers.<sup><a href="https://www.vcnewsdaily.com/call9/venture-capital-funding/tkfpqskyqf">[22]</a></sup> Scaled across the roughly 15,000 SNFs in the United States, the addressable savings — and thus the addressable revenue — ran into the tens of billions of dollars annually.

The more relevant market frame, however, was Medicare spending on avoidable hospitalizations from nursing homes. CMS data consistently showed that a significant fraction of nursing home hospital transfers were potentially avoidable, and that each transfer cost Medicare thousands of dollars in acute care spending. Call9 was positioning itself to capture a share of those savings through value-based contracts — a model that required Medicare's reimbursement infrastructure to support it.

The geographic concentration in New York was both a strength and a constraint. New York had a high density of large nursing homes, strong Medicare Advantage penetration, and proximity to the company's Brooklyn headquarters. But it also meant Call9 was operating almost entirely in urban markets — and CMS's pre-2020 telehealth rules restricted Medicare billing for telehealth to rural facilities only. The company's entire market was, by regulatory definition, ineligible for the reimbursement model it needed.

### Competition

Call9 had no direct competitor that combined on-site clinical staff, diagnostic hardware, and telemedicine software into a single nursing home emergency response product. The competitive landscape was fragmented across adjacent categories.

Traditional telemedicine platforms — Teladoc, American Well, and similar services — offered physician video access but no physical presence at the bedside. They were designed for outpatient consultations, not nursing home emergencies requiring hands-on assessment. Their cost structures were lower, but so was their clinical capability in acute situations.

The default alternative to Call9 was the 911 system itself — not a commercial competitor, but the incumbent behavior that Call9 had to displace. Nursing home staff calling 911 was free, familiar, and legally defensible. Convincing facility administrators to pay a subscription fee and change deeply ingrained emergency protocols required both clinical proof and administrative trust.

Larger hospital systems and health networks were beginning to explore telemedicine-in-SNF programs, but these were typically extensions of existing hospital relationships rather than standalone products. They lacked Call9's 24/7 on-site staffing model.

After Call9's shutdown, the space attracted new entrants — including Peck's own Curve Health — that benefited from the post-COVID CMS telehealth expansion. But during Call9's operating years, the company faced no direct commercial competitor with a comparable product. Its competitive problem was not losing customers to rivals; it was failing to generate sufficient revenue from the customers it had.

---

## Business Model

Call9 operated a multi-layered revenue model that proved strategically complex to execute.<sup><a href="https://techcrunch.com/2016/01/14/call9-raises-10-million-series-a-led-by-index-ventures/">[26]</a></sup>

Nursing homes paid a subscription fee for access to the Call9 platform and the embedded Clinical Care Specialist. This provided a predictable base revenue stream but was insufficient on its own to cover the cost of 24/7 on-site staffing and hardware at each facility.

The second revenue stream was fee-for-service billing to Medicare and Medicaid for each patient encounter the remote physician conducted. This was where CMS's telehealth restrictions created a structural ceiling: Medicare would only reimburse telehealth encounters at rural facilities, with weekly caps on billable interventions. Call9's New York nursing homes were urban, making this revenue stream largely inaccessible under pre-2020 rules.

The third and most strategically important revenue stream was value-based contracts with Medicare Advantage insurers. Under these arrangements, Call9 would share in the savings generated by avoided hospitalizations. This model aligned with the company's mission and its clinical outcomes data. It also required insurers to trust a small physician group with a novel care model — a trust that major payers like Aetna and UnitedHealthcare were unwilling to extend at Call9's scale.<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[27]</a></sup>

The result was a business that needed all three revenue streams to work simultaneously, and found each one constrained by a different external force.

---

## Traction

Call9's clinical outcomes were among the strongest of any telehealth startup of its era, and they were independently validated.

At the time of its Series A in January 2016, the company had prevented 55% of ER trips in the patients it had seen across three nursing homes, and reported saving three lives.<sup><a href="https://techcrunch.com/2016/01/14/call9-raises-10-million-series-a-led-by-index-ventures/">[28]</a></sup> By the time of its Series B in September 2017, a Precision Health Economics study showed the platform avoided hospital visits in 80% of patient encounters, saving an estimated $8 million per year for every 200-bed facility.<sup><a href="https://www.vcnewsdaily.com/call9/venture-capital-funding/tkfpqskyqf">[22]</a></sup> Peer-reviewed research published in eScholarship confirmed the 80% reduction in care escalation figure.<sup><a href="https://www.fiercehealthcare.com/tech/founder-shuttered-call9-started-a-new-telehealth-venture-here-s-why-he-thinks-curve-health">[29]</a></sup>

By the time of shutdown in June 2019, Call9 had conducted more than 142,000 telemedicine visits and treated more than 11,000 patients.<sup><a href="https://medcitynews.com/2019/06/new-york-telemedicine-startup-call9-winding-down-operations/">[30]</a></sup> Peck later cited the figure as more than 150,000 encounters, with the platform managing more than 5,000 patients daily and reducing hospital transfers by more than 50%.<sup><a href="https://www.prnewswire.com/news-releases/curve-health-raises-6m-seed-round-led-by-lightspeed-venture-partners-hires-top-50-healthcare-technology-ceo-rob-macnaughton-301163182.html">[31]</a></sup>

Commercial scale, however, remained limited. The company grew to 12 nursing homes and 10 Medicare Advantage payer contracts, concentrated in the New York metro area, despite raising $34 million over four years.<sup><a href="https://skillednursingnews.com/2019/06/once-backed-with-34m-skilled-nursing-telehealth-provider-call9-to-shut-down/">[11]</a></sup> At peak, Call9 employed approximately 200 people to serve those 12 facilities — a ratio that reflects the cost intensity of the embedded staffing model.<sup><a href="https://www.modernhealthcare.com/technology/after-shutdown-telemedicine-company-call9s-founder-plans-comeback/">[32]</a></sup>

The gap between clinical proof and commercial scale is the central tension of Call9's story. The product demonstrably worked. The business could not grow fast enough to survive.

---

## Post-Mortem

Call9 shut down in June 2019 after failing to raise a Series C and watching its cash fall below its debt obligations. The proximate cause was a cash crisis. The structural causes were more complex — and more instructive.

### 1. Medicare's Telehealth Rules Created a Revenue Ceiling the Company Could Not Break Through

The single most important structural cause of Call9's failure was a regulatory constraint that predated the company's founding and outlasted it by nine months.

Before March 2020, CMS restricted Medicare reimbursement for telehealth services to rural facilities only, with additional caps on the number of billable interventions per week. Call9's nursing home network was concentrated in New York City and its suburbs — urban markets by every regulatory definition. This meant the company could not bill Medicare for the majority of the telemedicine encounters its physicians conducted, eliminating what should have been its most scalable revenue stream.

Peck stated this directly: "Medicare itself didn't pay us well for what we were doing, and we couldn't make profits on treating Medicare patients with the previous telehealth regulations."<sup><a href="https://www.fiercehealthcare.com/tech/founder-shuttered-call9-started-a-new-telehealth-venture-here-s-why-he-thinks-curve-health">[33]</a></sup> The company attempted to address this through lobbying. Peck traveled to Washington D.C. to meet with CMS, CMMI, and members of Congress, and helped champion the RUSH Act (Reducing Unnecessary Senior Hospitalizations Act), which would have created value-based care incentives for telemedicine groups serving nursing homes.<sup><a href="https://skillednursingnews.com/2020/05/as-cms-relaxes-rules-on-telehealth-skilled-nursing-startup-call9-sees-second-chance-at-success/">[34]</a></sup> The bill never reached a full Congressional vote.

The lobbying effort was the right strategic response to a regulatory problem. It was also a multi-year process that a venture-backed startup with a 24/7 staffing cost structure could not afford to wait out. CMS expanded telehealth reimbursement dramatically in March 2020 in response to COVID-19 — removing the rural-only restriction entirely. Call9 had shut down nine months earlier.

### 2. A Controlling Investor Pushed a Strategy That Contradicted the Company's Business Model

The second major cause of failure was an investor conflict that created strategic paralysis at the worst possible moment.

Redmile Group led Call9's $24 million Series B in September 2017 and subsequently acquired a controlling interest of more than 50% in the company.<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[35]</a></sup> With majority control came board authority to direct the company's strategy. Redmile pushed Call9 toward a fee-for-service model — maximizing revenue from each patient encounter billed to insurers in the traditional way. This conflicted directly with Call9's value-based care mission, which was built around sharing in the savings from avoided hospitalizations rather than billing for individual services.

Peck later articulated the incompatibility clearly: "You can't lean into fee-for-service in order to maximize the amount of cash that you're getting in the short term, and keep the good graces of the payers and the world out there, who's trying to work with you toward being a value-based company. You have to decide one way or the other."<sup><a href="https://skillednursingnews.com/2020/10/call9-founders-new-venture-curve-health-raises-6m-in-skilled-nursing-tech-push/">[36]</a></sup>

The tension was not merely philosophical. Fee-for-service billing required Call9 to structure its clinical encounters in ways that satisfied insurer billing codes — "checking very specific boxes to make sure we got paid," as Peck described it — rather than optimizing for patient outcomes.<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[37]</a></sup> Meanwhile, the value-based payers that Call9 was trying to cultivate were watching the company operate in fee-for-service mode and drawing conclusions about its commitment to the model they were being asked to fund.

People with knowledge of the company's financing told Crain's New York that the troubled relationship with Redmile "brought Call9 to a screeching halt."<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[35]</a></sup> The specific mechanism — whether Redmile blocked the Series C, refused to bridge the company, or simply declined to support a strategic pivot — is not fully documented. What is documented is the outcome: the Series C never closed, and the company ran out of cash.

### 3. Major Insurers Refused to Create Value-Based Contracts at Call9's Scale

Even setting aside the Redmile conflict, Call9's value-based care strategy faced a market reality problem: the insurers it needed to partner with did not want to partner with it.

Aetna and UnitedHealthcare, both of which had relationships with Call9, declined to create value-based contracts with what they viewed as a small physician group.<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[27]</a></sup> These insurers preferred to reimburse in the traditional fee-for-service way, which meant Call9 was simultaneously trying to maintain value-based relationships with some payers while operating in fee-for-service mode for others. The split created operational complexity and undermined the company's ability to present a coherent model to either type of payer.

The company's response was to pursue both tracks — maintaining value-based contracts where it could while accepting fee-for-service reimbursement where it had to. Peck acknowledged this directly: "The cash flow of an early venture-backed value-based company is not going to be as much as a fee-for-service company."<sup><a href="https://medcitynews.com/2019/06/new-york-telemedicine-startup-call9-winding-down-operations/">[38]</a></sup> The strategic ambiguity was not a failure of execution; it was a rational response to conflicting pressures from investors, lenders, and payers. But it prevented the company from building the deep payer relationships that its value-based model required.

### 4. The Embedded Staffing Model Created a Cost Structure That Could Not Scale Fast Enough

Call9's most clinically important feature — the 24/7 on-site Clinical Care Specialist — was also its most expensive. Staffing a paramedic or nurse inside each nursing home around the clock meant that every new facility added a fixed labor cost before generating a single dollar of revenue. At peak, the company employed approximately 200 people to serve 12 nursing homes.<sup><a href="https://www.modernhealthcare.com/technology/after-shutdown-telemedicine-company-call9s-founder-plans-comeback/">[32]</a></sup>

This cost structure required rapid facility growth to achieve unit economics that could sustain the business. The company had projected serving 65 facilities by 2016 at the time of its Series A; it reached 12 by the time it shut down in 2019. The gap between projection and reality reflected the combined effect of regulatory constraints on revenue, payer resistance to value-based contracts, and the operational complexity of deploying hardware and staff into new facilities.

ArchCare CEO Scott LaRue, an early Call9 client, offered a candid assessment: "Their model wasn't able to move the needle sufficiently to justify the ongoing expense."<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[39]</a></sup> This was not a clinical judgment — it was an economic one. The product worked. The cost of delivering it, relative to the revenue it could generate under existing reimbursement rules, did not.

### 5. The Debt Obligation Became the Immediate Trigger

Western Technology Investment, a Silicon Valley venture lender, had provided debt financing as part of Call9's capital structure. In spring 2019, as the Series C process stalled, Call9's cash fell below what it owed WTI. The lender exercised its right to put a lien on the company's assets — what Peck described as a "friendly foreclosure."<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[14]</a></sup>

The foreclosure was the mechanism of shutdown, but not its cause. The cause was the combination of regulatory constraints, investor conflict, and payer resistance that prevented the Series C from closing. Rock Health managing director Bill Evans observed: "It's a hard lesson for the industry whenever something like that happens. My counsel to entrepreneurs is to be thoughtful of the timing of significant capital raises."<sup><a href="https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback">[40]</a></sup>

The timing of Call9's Series C attempt — mid-2019, with a cost-intensive staffing model, a controlling investor in strategic conflict with the founder, and a regulatory environment that capped its primary revenue stream — was as unfavorable as it could have been.

---

## Key Lessons

- **Regulatory timing is a startup risk that clinical validation cannot mitigate.** Call9 produced peer-reviewed evidence that its product worked, raised $34 million from sophisticated investors, and built a clinically meaningful business — and was still killed by a Medicare billing rule that changed nine months after it shut down. Healthcare startups whose unit economics depend on specific reimbursement codes must either have a credible path to regulatory change within their runway, or build a business model that generates sufficient revenue under existing rules. Call9 had neither.

- **Controlling investors with misaligned strategies are an existential risk, not a governance inconvenience.** Redmile Group's acquisition of a majority stake gave it the authority to push a fee-for-service strategy that contradicted Call9's value-based care model and its relationships with payers. The resulting strategic ambiguity made it impossible to optimize for either revenue model and likely deterred Series C investors who could not identify a coherent path forward. Founders accepting institutional capital should treat control provisions as carefully as valuation terms.

- **A hybrid fee-for-service and value-based care strategy satisfies neither payer type.** Peck's post-mortem insight was precise: operating in fee-for-service mode to generate short-term cash while pursuing value-based contracts for long-term sustainability signals to value-based payers that the company is not committed to their model. Major insurers like Aetna and UnitedHealthcare declined to create value-based contracts with Call9 in part because they observed it operating in fee-for-service mode. The strategic choice between the two models must be made early and held consistently.<sup><a href="https://skillednursingnews.com/2020/10/call9-founders-new-venture-curve-health-raises-6m-in-skilled-nursing-tech-push/">[36]</a></sup>

- **Embedded staffing models require a revenue structure that can support them from day one.** Call9's 24/7 on-site Clinical Care Specialist was the product's most important clinical feature and its most expensive operational commitment. The cost was fixed per facility; the revenue was variable and capped by regulation. This mismatch required rapid facility growth to resolve — growth that the regulatory and payer environment made impossible. Startups building products that require permanent on-site human presence should stress-test their unit economics against the worst-case regulatory scenario before scaling the staffing model.

- **The idea surviving the company is not a consolation — it is a data point.** Peck retained Call9's intellectual property, founded Curve Health in April 2020, and raised $6 million from Lightspeed Venture Partners within months of CMS's telehealth expansion.<sup><a href="https://skillednursingnews.com/2020/10/call9-founders-new-venture-curve-health-raises-6m-in-skilled-nursing-tech-push/">[19]</a></sup> The market validated the thesis; the timing and capital structure did not. Damo Consulting's Paddy Padmanabhan identified the core question that Call9 could never fully answer: "Who pays for the solution and how do they recover the investment?"<sup><a href="https://medcitynews.com/2019/06/new-york-telemedicine-startup-call9-winding-down-operations/">[41]</a></sup> That question must be answered with specificity — not in theory, but in signed contracts and working billing codes — before a company scales its cost structure.

---

## Sources

1. [MedCity News — "New York telemedicine startup Call9 winding down operations" (June 25, 2019)](https://medcitynews.com/2019/06/new-york-telemedicine-startup-call9-winding-down-operations/)
2. [TechCrunch — "Venture-backed telemedicine startup Call9 is shutting down" (July 1, 2019)](https://techcrunch.com/2019/07/01/venture-backed-telemedicine-startup-call9-is-shutting-down/)
3. [TechCrunch — "Call9 Delivers On-Demand Doctors In Emergency Situations" (July 20, 2015)](https://techcrunch.com/2015/07/20/call9-delivers-on-demand-doctors-in-emergency-situations/)
4. [CNBC — "Call9, a start-up selling digital medical services to nursing homes, is shutting down operations" (June 25, 2019)](https://www.cnbc.com/2019/06/25/call9-a-start-up-selling-digital-medical-services-to-nursing-homes-is-shutting-down-operations.html)
5. [Built In NYC — "Call9 reveals why they relocated to NYC"](https://www.builtinnyc.com/articles/call9-silicon-valley-nyc-relocation)
6. [Y Combinator Blog — "Call9 (YC S15) Provides An ER Doctor To Assist In A Medical Emergency Within 1 Minute"](https://www.ycombinator.com/blog/call9-yc-s15-dispatches-an-er-doctor-to-a-medical-emergency-within-1-minute/)
7. [Tracxn — Call9 Funding and Investors](https://tracxn.com/d/companies/call9/__kGd0zB86icGGsHc9iy5PmR2EXRxCau3EMyk3mgPDATQ/funding-and-investors)
8. [TechCrunch — "Call9 Raises $10 Million Series A Led by Index Ventures" (January 14, 2016)](https://techcrunch.com/2016/01/14/call9-raises-10-million-series-a-led-by-index-ventures/)
9. [FinSMEs — "Call9 Raises $24M in Series B Funding" (September 14, 2017)](https://www.finsmes.com/2017/09/call9-raises-24m-in-series-b-funding.html)
10. [Crain's New York — "After shutdown, Call9 founder plans comeback" (July 26, 2019)](https://www.crainsnewyork.com/health-care/after-shutdown-call9-founder-plans-comeback)
11. [Skilled Nursing News — "Once Backed With $34M, Skilled Nursing Telehealth Provider Call9 to Shut Down" (June 25, 2019)](https://skillednursingnews.com/2019/06/once-backed-with-34m-skilled-nursing-telehealth-provider-call9-to-shut-down/)
12. [Fierce Healthcare — "Tech startup Call9 shutting down operations, telehealth services to nursing homes" (June 26, 2019)](https://www.fiercehealthcare.com/tech/tech-startup-call9-shutting-down-operations-telehealth-services-to-nursing-homes)
13. [VC News Daily — Call9 Series B Coverage (September 14, 2017)](https://www.vcnewsdaily.com/call9/venture-capital-funding/tkfpqskyqf)
14. [Fierce Healthcare — "Founder of shuttered Call9 started a new telehealth venture — here's why he thinks Curve Health will succeed"](https://www.fiercehealthcare.com/tech/founder-shuttered-call9-started-a-new-telehealth-venture-here-s-why-he-thinks-curve-health)
15. [Modern Healthcare — "After shutdown, telemedicine company Call9's founder plans comeback" (July 25, 2019)](https://www.modernhealthcare.com/technology/after-shutdown-telemedicine-company-call9s-founder-plans-comeback/)
16. [Skilled Nursing News — "As CMS Relaxes Rules on Telehealth, Skilled Nursing Startup Call9 Sees Second Chance at Success" (May 19, 2020)](https://skillednursingnews.com/2020/05/as-cms-relaxes-rules-on-telehealth-skilled-nursing-startup-call9-sees-second-chance-at-success/)
17. [Skilled Nursing News — "Call9 Founder's New Venture Curve Health Raises $6M in Skilled Nursing Tech Push" (October 29, 2020)](https://skillednursingnews.com/2020/10/call9-founders-new-venture-curve-health-raises-6m-in-skilled-nursing-tech-push/)
18. [PR Newswire — "Curve Health Raises $6M Seed Round Led by Lightspeed Venture Partners" (October 29, 2020)](https://www.prnewswire.com/news-releases/curve-health-raises-6m-seed-round-led-by-lightspeed-venture-partners-hires-top-50-healthcare-technology-ceo-rob-macnaughton-301163182.html)
19. [Failory — "Call9 Startup Cemetery"](https://www.failory.com/cemetery/call9)
20. [Built In NYC — "How Call9 is scaling its platform by always putting the patient first"](https://www.builtinnyc.com/articles/spotlight-working-at-call9)
21. [Y Combinator — Call9 Company Profile](https://www.ycombinator.com/companies/call9)
