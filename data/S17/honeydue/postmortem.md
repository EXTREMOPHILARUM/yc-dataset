# Research Report: Honeydue

## Overview

## Founding Story

Eugene Park and Thien Tran were not strangers when they started Honeydue. The two had attended the same high school and college simultaneously and had already built one startup together before turning their attention to personal finance.<sup><a href="https://www.wayup.com/i-Consumer-Services-j-Operations-Intern-20-hr-Honeydue-447515372050706/">[4]</a></sup> That prior collaboration gave them a working relationship most co-founders spend years developing — a meaningful structural advantage for a two-person team attempting to build a regulated fintech product.

Park brought serious technical credentials. He spent eight years at Flixster and RottenTomatoes.com, rising to Co-Head of Engineering — a role that required managing large-scale consumer data infrastructure and cross-platform mobile development.<sup><a href="https://www.businesswire.com/news/home/20210524005130/en/Mission-Lane-Acquires-Honeydue-to-Expand-Debit-and-Digital-Banking-Capabilities">[5]</a></sup> He holds a BS in Business Administration and a BA in Computer Science from UC Berkeley.<sup><a href="https://www.crunchbase.com/person/eugene-park-2">[6]</a></sup> Tran served as CTO, though his background and prior experience have not been publicly documented in detail.

The founding insight was personal and immediate. Both Park and Tran were living with their partners and experiencing the friction that comes with shared finances managed through separate tools. Park described the moment of clarity directly: "When we started this project both [of us] were living with our partners and arguing, from time to time, with our partners about money. And it sort of hit us — with all of these basic tools that are out there, if couples like us can't get on the same page with money then these tools really don't matter."<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[7]</a></sup>

The competitive gap they identified was structural, not marginal. Park noted that existing tools like Mint.com were "generally not collaborative in nature" — designed for individual users tracking individual accounts.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[8]</a></sup> Couples who wanted shared visibility had no purpose-built option. They had to share passwords, maintain spreadsheets, or simply argue.

The company was incorporated as WalletIQ, Inc. — a name that suggests an early vision broader than the couples niche, possibly encompassing general financial intelligence tools. The pivot to the Honeydue brand and couples positioning appears to have happened before public launch, though the precise rationale has not been disclosed.

Park and Tran validated their market hypothesis with a survey of 600 couples, finding that 75% reported co-managing some or all of their finances together.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[9]</a></sup> That data point — combined with the absence of any direct competitor — was enough to earn them a spot in Y Combinator's Summer 2017 batch. The $120,000 in YC seed funding would prove to be the only institutional capital the company ever raised.

Park also articulated a generational thesis: "Millennials are more likely to co-manage their finances together as opposed to my parents' generation, my generation (X)."<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[10]</a></sup> That demographic tailwind was real. What the founders underestimated was how difficult it would be to extract revenue from a user base that expected financial tools to be free.

## Timeline

- **2016** — Eugene Park and Thien Tran found Honeydue, incorporated as WalletIQ, Inc., motivated by personal experience arguing with partners about money.<sup>[[11]](https://tracxn.com/d/companies/honeydue/__fTO6sYPSc2ZUR6qZs2iTp7GMImdNEecnzvkMZh77inw)</sup>

- **January 2017** — Honeydue soft launches on iOS, integrating with approximately 9,000 US financial institutions. US-only at launch.<sup>[[12]](https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/)</sup>

- **March 2017** — Android app launches.<sup>[[12]](https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/)</sup>

- **Summer 2017** — Honeydue participates in Y Combinator S17 batch, raising $120,000 — its only institutional funding round.<sup>[[2]](https://tracxn.com/d/companies/honeydue/__fTO6sYPSc2ZUR6qZs2iTp7GMImdNEecnzvkMZh77inw)</sup>

- **August 7, 2017** — TechCrunch covers Honeydue at YC Demo Day. App has approximately 20,000 registered users. User base is 60% female. Bill splitting used by only ~5% of users.<sup>[[13]](https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/)</sup>

- **February 20, 2019** — Honeydue's Android app selected as Google Play Editors' Choice.<sup>[[14]](https://x.com/gethoneydue/status/1098369892527439872)</sup>

- **July 8, 2020** — Park speaks publicly about financial wellness and users struggling paycheck to paycheck, signaling a broadening product vision beyond couples budgeting.<sup>[[15]](https://streetfins.com/lessons-on-financial-wellness-and-entrepreneurship-from-honeydue-founder-eugene-park/)</sup>

- **May 24, 2021** — Mission Lane acquires Honeydue (WalletIQ, Inc.) for undisclosed terms. Honeydue has 500,000+ registered users across six countries in three languages. Park joins Mission Lane as Head of Product for Mission Money debit card.<sup>[[1]](https://www.businesswire.com/news/home/20210524005130/en/Mission-Lane-Acquires-Honeydue-to-Expand-Debit-and-Digital-Banking-Capabilities)</sup>

- **2021** — CNBC Select names Honeydue the best budgeting app for couples.<sup>[[16]](https://www.cnbc.com/select/honeydue-budgeting-app-review/)</sup>

- **September 1, 2023** — Honeydue Debit Card (Joint Cash) program closed for new enrollments and discontinued.<sup>[[17]](https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945)</sup>

- **2024** — Mission Lane divests Honeydue into Moneydue, Inc. App continues to operate under new entity with 1–10 employees.<sup>[[3]](https://www.honeydue.com/about)</sup>

## What They Built

Honeydue's core product was a shared financial dashboard for couples. The premise was simple: two people in a relationship could each link their individual bank accounts, credit cards, and investment accounts to a shared view — seeing each other's balances, transactions, and spending patterns in real time, with granular control over what each partner could see.

<media-image src="https://wealthpursuits.com/wp-content/uploads/2021/11/Honeydue-How-it-Works-300x140.png" alt="Honeydue app showing how couples link accounts and share financial data" caption="Honeydue's account-linking flow: each partner connected their individual accounts independently, then chose which balances and transactions to share with the other."></media-image>

**Account linking and shared visibility.** At launch, Honeydue integrated with approximately 9,000 US financial institutions via a third-party data aggregation provider (the specific provider — Plaid, Yodlee, or another — was not publicly disclosed).<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[18]</a></sup> By the time of the 2021 acquisition, that number had grown to over 20,000 institutions across five countries.<sup><a href="https://fortune.com/recommends/banking/honeydue-review/">[19]</a></sup> Each partner linked their accounts independently and set privacy controls — a user could share their checking account balance but hide a savings account, for example. This granularity addressed a real tension in couples finance: the desire for transparency without total exposure.

**Spending categories and budgets.** Transactions were automatically categorized, and couples could set shared monthly spending limits by category. When a category approached its limit, both partners received a notification. This was the feature that most directly addressed the "arguing about money" problem the founders had experienced personally.

**In-app messaging.** Honeydue included a chat feature tied to specific transactions — a partner could tap a charge and send a message asking about it, keeping financial conversations in context rather than migrating to text or email. This was a small but genuinely differentiated feature that no general-purpose budgeting tool offered.

**Bill splitting — the feature that flopped.** The founders expected bill splitting to be a core use case. It was not. Only approximately 5% of users engaged with it.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[20]</a></sup> Park's explanation was revealing: couples who co-manage finances tend to think in terms of shared pools of money, not individual debts to be settled. The bill-splitting mental model belongs to roommates and friends, not partners. This was an early signal that the founders' intuitions about couple behavior were not always accurate.

**No native payments.** Honeydue deliberately avoided building payment functionality. When couples needed to transfer money, the app linked out to Venmo or PayPal. Park was explicit about the reason: "Once you're getting into the business of helping people move money then we expose ourselves to another level of scrutiny."<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[21]</a></sup> This decision reduced regulatory risk but also foreclosed interchange revenue — the most natural monetization path for a product sitting between couples and their money.

**Joint debit card (late addition).** Honeydue eventually launched Honeydue Joint Cash, a joint VISA debit card issued by Sutton Bank and powered by Marqeta.<sup><a href="https://www.honeydue.com/joint-cash">[22]</a></sup> This was the product evolution that could have unlocked interchange revenue and a sustainable business model. It arrived too late — after the Mission Lane acquisition — and was discontinued for new enrollments on September 1, 2023.<sup><a href="https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945">[17]</a></sup>

What made Honeydue different from Mint or YNAB was not the underlying technology — account aggregation was a commodity by 2017 — but the collaborative layer on top of it. The product was designed for two users, not one. That design choice attracted a genuinely different user (more female, more relationship-oriented) and created a different engagement pattern (shared notifications, in-app messaging about specific transactions). The problem was that the collaborative layer was not, by itself, a monetizable feature.

## Market Position

### Target Customers

Honeydue's primary target was millennial couples who co-managed finances — a segment Park estimated at 75% of couples based on his own survey data.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[9]</a></sup> The product skewed toward couples who maintained separate accounts but wanted shared visibility, rather than couples who had already merged finances into a single joint account. The 60% female user base at launch was a meaningful signal: women in heterosexual couples disproportionately carry the mental load of household financial management, and Honeydue gave them a tool to share that burden.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[23]</a></sup>

Park also identified a secondary segment — users living paycheck to paycheck who needed financial wellness tools, not just budgeting dashboards.<sup><a href="https://streetfins.com/lessons-on-financial-wellness-and-entrepreneurship-from-honeydue-founder-eugene-park/">[15]</a></sup> This broadening of the target customer, articulated publicly in mid-2020, may reflect an attempt to expand the addressable market as the couples niche proved insufficient to support a venture-scale business.

### Market Size

The couples finance niche is structurally smaller than general personal finance. There are approximately 130 million adults in coupled households in the United States, but the subset actively seeking a shared financial management tool — rather than a joint bank account or a shared spreadsheet — is considerably smaller. Park's survey suggested 75% of couples co-manage finances, but co-management does not require a dedicated app. The total addressable market for a couples-specific budgeting tool, at any price point, is likely in the low tens of millions of users in the US — large enough for a sustainable business, but not large enough for a venture-scale outcome without either premium pricing or financial product revenue.

The broader personal finance app market was growing rapidly in 2017. Mint had approximately 20 million users by 2016. YNAB was generating meaningful subscription revenue from a smaller but highly engaged base. The market validated consumer appetite for financial tools; the question was whether the couples niche could be monetized at sufficient scale.

### Competition

Honeydue's competitive position is best understood along two axes: **collaborative depth** (how well the product served couples specifically) and **distribution reach** (how many users the product could acquire and retain).

On collaborative depth, Honeydue had a genuine lead. No major incumbent — Mint, YNAB, Personal Capital — had built a two-user collaborative layer. Honeydue's in-app messaging, per-partner privacy controls, and shared notification system were purpose-built for couples in a way that general tools were not.

On distribution, Honeydue was structurally disadvantaged. Mint had 20 million users and Intuit's marketing budget. YNAB had a loyal subscriber base and strong word-of-mouth. Personal Capital had wealth management revenue funding its free tool. Honeydue had $120,000 and organic growth.

The direct competitive set — Ivella, Tandem, Peas Technology, and Honeyfi (later rebranded as Firstly) — were all small startups attacking the same niche with similar product approaches.<sup><a href="https://tracxn.com/d/companies/honeydue/__fTO6sYPSc2ZUR6qZs2iTp7GMImdNEecnzvkMZh77inw">[24]</a></sup> Honeyfi/Firstly shut down its consumer app before Honeydue's acquisition — a data point that App Store reviewers explicitly noted as a warning sign for Honeydue's trajectory.<sup><a href="https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945">[25]</a></sup>

The most important competitive dynamic was not a direct competitor but a platform risk: the possibility that Mint, YNAB, or a major bank would add a collaborative feature and absorb the couples use case. This did not happen in a way that directly killed Honeydue — but it constrained the ceiling. Any investor evaluating a Series A had to weigh the risk that Intuit could add a "share with partner" button to Mint and eliminate Honeydue's core differentiation overnight. That ceiling risk, combined with the weak monetization model, made the Series A a difficult pitch.

## Business Model

Honeydue's revenue model was structurally inadequate for a venture-backed company from the start. The app was free to download and use, with two revenue mechanisms: in-app advertising and a voluntary "Tip Jar" where users could pay $1–$10 per month if they found the app valuable.<sup><a href="https://www.experian.com/blogs/ask-experian/honeydue-app-review/">[26]</a></sup>

The company never disclosed revenue figures. That absence is itself a signal — companies with strong revenue growth typically disclose it, especially when seeking follow-on capital. The inference is that revenue was either negligible or insufficient to support a Series A narrative.

**Inferring unit economics from available data:** Honeydue raised $120,000 total and operated for approximately five years (2016–2021). With two co-founders and a small team (the company had 1–10 employees as of 2024, suggesting it never scaled headcount significantly), annual burn was likely in the $200,000–$500,000 range — achievable only if the founders took minimal salaries and kept the team very small. At 500,000 registered users and assuming a 10–20% active user rate (50,000–100,000 monthly active users, a reasonable estimate for a consumer app with strong reviews but no disclosed engagement data), the tip model would need to convert at roughly 1–2% to generate $5,000–$20,000 per month — not enough to sustain even a two-person team at market salaries. These are inferences, not confirmed figures.

The decision to avoid native payments — explicitly to reduce regulatory exposure — foreclosed interchange revenue, which would have been the most natural path to sustainability. The joint debit card launched post-acquisition, suggesting the founders recognized this gap but could not execute on it independently. No subscription tier was ever introduced, despite YNAB demonstrating that couples and serious budgeters would pay $14.99/month for a premium tool.

## Traction

Honeydue's growth trajectory was real but modest relative to the consumer fintech category. At YC Demo Day in August 2017, the app had approximately 20,000 registered users — a reasonable number for a product that had been live for less than eight months with no paid marketing budget.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[13]</a></sup> By the May 2021 acquisition, that figure had grown to over 500,000 registered users across six countries in three languages — roughly 25x growth over four years.<sup><a href="https://www.businesswire.com/news/home/20210524005130/en/Mission-Lane-Acquires-Honeydue-to-Expand-Debit-and-Digital-Banking-Capabilities">[1]</a></sup>

The qualitative reception was strong. Apple featured the app nationally. Google Play awarded it Editors' Choice in February 2019.<sup><a href="https://x.com/gethoneydue/status/1098369892527439872">[14]</a></sup> Forbes listed it among "Best Tech Apps." CNBC Select named it the best budgeting app for couples in 2021.<sup><a href="https://www.cnbc.com/select/honeydue-budgeting-app-review/">[16]</a></sup> These are not vanity metrics — editorial features from Apple and Google drive meaningful organic downloads and signal genuine product quality.

The 60% female user base at launch was a meaningful traction signal.<sup><a href="https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/">[23]</a></sup> Personal finance apps historically skew male; Honeydue's gender split indicated it was reaching a genuinely different user than competitors, not just repackaging the same audience.

The critical caveat: 500,000 "registered users" is a ceiling metric, not a floor. Registered users include everyone who ever downloaded and created an account, regardless of whether they remained active. No data on daily active users, monthly active users, retention curves, or churn rates was ever disclosed. For a couples app — where both partners must link accounts and remain engaged for the product to deliver value — the active user count is likely a fraction of the registered figure. The absence of engagement data in the acquisition press release is notable; Mission Lane's announcement emphasized the user count and geographic reach, not engagement or revenue.

## Post-Mortem

### Primary Cause: A Monetization Model That Could Not Support the Business

The clearest explanation for Honeydue's outcome is not product failure — the product worked and users liked it. It is that the company chose a revenue model (free + voluntary tips + ads) that was structurally incapable of generating the cash needed to sustain a team, fund growth, or attract institutional capital.

The tip model was philosophically consistent with the founders' stated goal of eliminating fees and minimums that caused financial stress.<sup><a href="https://www.businesswire.com/news/home/20210524005130/en/Mission-Lane-Acquires-Honeydue-to-Expand-Debit-and-Digital-Banking-Capabilities">[27]</a></sup> Park said at acquisition: "When we founded Honeydue, we wanted to eliminate some of the issues that intimidated people about finance, so we worked to eliminate fees, minimums, and other requirements that caused stress and confusion." That philosophy was admirable and user-friendly. It was also incompatible with building a venture-scale business.

The math was unworkable. Even at 500,000 registered users, voluntary tips of $1–$10/month at a 1–2% conversion rate generate $5,000–$100,000 per month — a range that cannot support a San Francisco or New York fintech team at competitive salaries, let alone fund the engineering, compliance, and customer support infrastructure required to expand internationally and launch a debit card product. The company's $120,000 total raise and apparent lean headcount suggest the founders were aware of this constraint and managed burn aggressively — but aggressive burn management is a survival strategy, not a growth strategy.

No subscription tier was ever introduced. YNAB, the most direct comparable in terms of serious budgeting users, charges $14.99/month and has built a profitable, growing business on a fraction of Honeydue's registered user base. The couples niche — users who are, by definition, managing a shared financial life — is arguably more willing to pay for a premium tool than solo budgeters. Honeydue never tested that hypothesis.

### Secondary Cause: Regulatory Avoidance Foreclosed the Natural Revenue Path

The decision not to build native payments was rational in 2017 — money transmission licensing is expensive, slow, and state-by-state in the US. But it had a compounding cost. Interchange revenue from payments or a joint debit card was the most natural monetization path for a product sitting between couples and their financial accounts. By linking out to Venmo and PayPal instead of capturing that transaction flow, Honeydue gave away the revenue layer that could have funded the business.

The joint debit card (Honeydue Joint Cash, issued by Sutton Bank via Marqeta) was the right product — it arrived too late.<sup><a href="https://www.honeydue.com/joint-cash">[22]</a></sup> Had the debit card launched in 2019 or 2020, it could have generated interchange revenue, provided a reason to raise a Series A, and given the company a path to sustainability. Instead, it launched post-acquisition, under Mission Lane's ownership, and was discontinued in September 2023.<sup><a href="https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945">[17]</a></sup> The timing gap between recognizing the right product and executing on it — likely constrained by capital — was fatal.

### Tertiary Cause: The Niche Was Real but Structurally Small for Venture

Honeydue's couples finance niche was genuine and underserved. But it was also structurally limited. The total addressable market for a couples-specific budgeting app — at any price point — is bounded by the number of couples actively seeking a shared financial management tool, which is a subset of the already-niche "people who use budgeting apps" category.

Consumer fintech at venture scale requires either massive user counts (tens of millions, like Mint) or high revenue per user (lending, banking, or wealth management products). Honeydue achieved neither. At 500,000 registered users after four years, the growth rate — approximately 25x from 20,000 to 500,000 — looks impressive in percentage terms but modest in absolute terms for a consumer app with strong editorial coverage and no paid acquisition costs. Mint had 20 million users by 2016; Honeydue had 500,000 by 2021. The gap in scale reflects the gap in addressable market, not just execution.

The direct competitor Honeyfi/Firstly shut down its consumer app before Honeydue's acquisition — a data point that suggests the couples finance niche could not support multiple venture-backed companies simultaneously, regardless of product quality.<sup><a href="https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945">[25]</a></sup>

### Structural Factor: Consumer Fintech on a Free Model Requires Platform Scale

Building a consumer fintech app on a free model in 2017 required one of two things: massive scale (tens of millions of users, enabling meaningful ad revenue and data monetization) or a pivot to financial products (lending, banking, or insurance, where revenue per user is high enough to sustain a small team). Honeydue achieved neither at sufficient scale.

The broader consumer fintech landscape in 2017–2021 was moving toward embedded financial products — neobanks, BNPL, earned wage access — where the app was a distribution channel for high-margin financial products. Honeydue's deliberate avoidance of financial products (no payments, no lending, no banking until the late-stage debit card) left it in the worst position: a data aggregation app with no financial product revenue and no scale for ad revenue.

### Post-Acquisition Signals: A Deprioritized Asset

The post-acquisition trajectory confirms that Mission Lane acquired Honeydue for the team and the banking infrastructure knowledge, not the consumer product. Park joined as Head of Product for Mission Money — Mission Lane's debit card — not as a Honeydue product leader.<sup><a href="https://www.crunchbase.com/person/eugene-park-2">[28]</a></sup> App Store reviews noted that support went "completely dark," with no responses to support emails, and that the Tip Jar and Support Chat features were removed from the app.<sup><a href="https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945">[29]</a></sup> Google Play reviews flagged persistent bank syncing failures with no support response.<sup><a href="https://play.google.com/store/apps/details?id=com.honeydue.honeydue&hl=en&gl=US">[30]</a></sup> The debit card program was discontinued in September 2023. The app was divested into Moneydue, Inc. in 2024 — a 1–10 person entity that appears to be maintaining the product in a minimal-investment mode rather than growing it.<sup><a href="https://tracxn.com/d/companies/honeydue/__fTO6sYPSc2ZUR6qZs2iTp7GMImdNEecnzvkMZh77inw">[31]</a></sup>

Park's LinkedIn activity included a post warning founders: "Who you let on your cap table matters a lot. Get references before you take someone's check! Not all money is long-term aligned."<sup><a href="https://www.linkedin.com/in/eugenejohnpark/">[32]</a></sup> The specific context is ambiguous — YC was the only known institutional investor, and YC's alignment with founders is generally strong. The warning may refer to angel investors, the Mission Lane acquisition terms, or a situation that has not been publicly documented.

## Key Lessons

- **Honeydue proved that a free model cannot sustain a couples finance app at the scale it achieved.** At 500,000 registered users and a voluntary tip model generating an estimated $5,000–$100,000/month (at 1–2% conversion), Honeydue could not fund the team, compliance infrastructure, or product development needed to compete. YNAB, with a smaller but paying user base at $14.99/month, built a sustainable business. Honeydue never tested whether its users — who were, by definition, managing shared financial lives and had demonstrated willingness to engage deeply with the product — would pay for a premium tier.

- **Regulatory avoidance in 2017 foreclosed the revenue model that arrived too late in 2021.** Honeydue's decision to link out to Venmo rather than build native payments was rational given the cost of money transmission licensing. But it delayed the joint debit card — the product that could have generated interchange revenue — until after the acquisition. The Honeydue Joint Cash card launched under Mission Lane's ownership and was discontinued within two years. The lesson is not that regulatory risk should be ignored, but that fintech products built on data aggregation alone have no durable revenue model; the financial product layer must be planned from the start, even if it is built later.

- **The couples finance niche was real but structurally insufficient for venture scale without a financial product.** Honeydue grew from 20,000 to 500,000 registered users in four years on essentially zero marketing budget — a genuine product-market fit signal. But 500,000 registered users in a niche category, with no disclosed engagement data and a free model, cannot support a Series A. The niche rewarded Honeydue with editorial recognition and user loyalty; it did not reward it with the scale needed to raise institutional capital or sustain independent operations.

- **Honeydue's acqui-hire exit reflects the gap between product quality and business viability.** Mission Lane acquired Honeydue not to run a couples finance app but to hire a team with digital banking product experience. Park joined to lead Mission Money, not Honeydue. A product can be well-loved, editorially recognized, and genuinely useful — and still be worth more as a talent acquisition than as a going concern if the revenue model cannot support the team. The Honeydue outcome is a case study in the difference between product-market fit (real) and business model fit (absent).

- **The joint debit card was the right product, but the sequencing was wrong.** Honeydue's Honeydue Joint Cash — a shared VISA debit card for couples — was a logical extension of the core product and would have generated interchange revenue from day one. It required banking infrastructure (Sutton Bank, Marqeta) that was available to fintech startups by 2019–2020. Had Honeydue pursued this product in 2019 rather than post-acquisition, it would have had a fundable revenue model, a reason to raise a Series A, and a path to sustainability. The debit card arrived two years too late to save the independent company.

## Sources

1. [Mission Lane Acquires Honeydue — BusinessWire, May 24, 2021](https://www.businesswire.com/news/home/20210524005130/en/Mission-Lane-Acquires-Honeydue-to-Expand-Debit-and-Digital-Banking-Capabilities)
2. [Honeydue — Tracxn Company Profile](https://tracxn.com/d/companies/honeydue/__fTO6sYPSc2ZUR6qZs2iTp7GMImdNEecnzvkMZh77inw)
3. [Honeydue About Page — Honeydue.com](https://www.honeydue.com/about)
4. [Honeydue Operations Intern Listing — WayUp](https://www.wayup.com/i-Consumer-Services-j-Operations-Intern-20-hr-Honeydue-447515372050706/)
5. [Eugene Park — Crunchbase](https://www.crunchbase.com/person/eugene-park-2)
6. [Eugene Park — AngelList](https://angel.co/p/eugene-park)
7. [Honeydue is a money management app for couples — TechCrunch, August 7, 2017](https://techcrunch.com/2017/08/07/honeydue-is-a-money-management-app-for-couples/)
8. [Honeydue — Y Combinator Company Page](https://www.ycombinator.com/companies/honeydue)
9. [Honeydue Review — Fortune Recommends, December 11, 2024](https://fortune.com/recommends/banking/honeydue-review/)
10. [Honeydue Joint Cash — Honeydue.com](https://www.honeydue.com/joint-cash)
11. [Honeydue App Store Listing — Apple App Store](https://apps.apple.com/us/app/honeydue-couples-finance/id1157633945)
12. [Honeydue Editors' Choice Tweet — @gethoneydue, February 20, 2019](https://x.com/gethoneydue/status/1098369892527439872)
13. [Honeydue App Review — Experian](https://www.experian.com/blogs/ask-experian/honeydue-app-review/)
14. [Honeydue Best Budgeting App for Couples — CNBC Select](https://www.cnbc.com/select/honeydue-budgeting-app-review/)
15. [Lessons on Financial Wellness from Honeydue Founder Eugene Park — StreetFins, July 8, 2020](https://streetfins.com/lessons-on-financial-wellness-and-entrepreneurship-from-honeydue-founder-eugene-park/)
16. [Eugene Park — LinkedIn](https://www.linkedin.com/in/eugenejohnpark/)
17. [Honeydue Google Play Listing](https://play.google.com/store/apps/details?id=com.honeydue.honeydue&hl=en&gl=US)
18. [Honeydue Budgeting App Review — WSJ Buy Side](https://www.wsj.com/buyside/content-images/699a64cf-9b28-4f53-af01-4b8a57ee01b7)
