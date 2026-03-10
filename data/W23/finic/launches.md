# Launches

## Finic 🕵️‍♂️ - AI that investigates financial fraud

We’re Jason and Ayan, the founders of Finic. We help fintechs automate fraud investigations with AI agents.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85671&key=user_uploads/139135/4a8b26cc-6258-4e8a-93c7-1779e1768748)

## tl;dr

Finic lets fraud ops teams at financial institutions scale up their capacity by 10x without increasing headcount. We use intelligent automation to analyze structured data (SQL queries, risk scores) and unstructured data (customer support tickets, adverse media), allowing us to triage tickets and generate case notes twenty times faster and at 80% lower cost compared to tier 1 fraud analysts.

---

—

---

At Robinhood, we led the identity team. One of our key mandates was to prevent, detect, and investigate fraud, with a specific focus on identity fraud. We were able to reduce account takeover (ATO) fraud losses by 95%, but it took us 10 months and a lot of new hires to get there, largely due to **bottlenecks in the human review process.** We tried automating fraud SOPs, but weren’t able to arrive a compelling solution because at the time there wasn’t a way to automate the biggest bottle neck to fraud reviews - subjective reasoning.

Now, we’re building Finic to be the product we wish we had, with AI that now makes this possible.

## **Why is this important?**

Consumer financial fraud losses crossed $10bn for the first time in 2023, and is likely to keep growing as new technology also enables new attack vectors, most recently with synthetic identities created by GenAI.

The way financial institutions prevent fraud is usually split into three parts:

* **Prevention:** Find and closing loopholes that enable fraud in the first place.
* **Detection:** using ML or heuristic models (aka “rules engine”) to detect unusual activity.
* **Response:** Investigating cases of potential fraud, deciding on a course of action, and, in some cases, writing reports detailing the investigation.

Prevention is typically achieved through product improvements, and the market for data products that help with fraud detection is mature. However, **the way that companies respond to fraud is still mostly done by human review** by a combination of highly skilled onshore and low-skilled offshore analysts.

## **Problem**

Using humans as the front line of fraud investigations is not ideal for several reasons:

* **Humans make mistakes.** For CS tickets, mistakes mean frustrated customers. For fraud cases, mistakes can result in thousands or millions in losses and compliance headaches that last years.
* **Humans take a long time to train.** Fraudsters change tactics frequently. By the time a team of analysts is fully trained on a new fraud typology, fraudsters have already moved on to other strategies.
* **Humans are expensive to scale.** The average offshore agent costs $43,000 per year and has a throughput of about 250 cases per month. This means it costs companies $14 per case to investigate fraud, and that’s not even factoring in the period it takes to onboard and train new agents, which is a constant problem since turnover is so high.

Financial institutions aggressively overhire when fraud is bad, yet still find themselves unable to respond quickly to new fraud typologies, leading to **millions in preventable losses per quarter.** As a result, every fraud ops team I’ve worked with is either understaffed and overworked, or overstaffed and just waiting to be laid off.

## **Solution**

Finic allows fraud ops teams to build custom AI agents that execute SOPs autonomously, improving on the work of junior fraud analysts and allowing the team to scale capacity by 100x with the click of a button.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85671&key=user_uploads/139135/1211dd85-7c36-4f73-b1f8-5ab59a333550)

This gives fraud ops teams several superpowers:

* **Accuracy and explainability:** Finic agents document each step of their workflow, making it easy for senior analysts to audit, which means fewer mistakes. Case notes written by human analysts take much longer and are often inconsistent.
* **React faster to new fraud vectors:** Finic agents can be created, trained, and scaled to 1000s of cases per day in a matter of hours, something that would be impossible for a team of human analysts.
* **Scale capacity instantly:** Fraud ops can now scale capacity as easily as engineering can scale web services. Finic agents complete investigations in 1-5 minutes, compared to 1-2 hours for human analysts.

The Finic platform has three parts, all of which are built on top of a multimodal reasoning engine.

### **SOPs**

Each Finic agent is defined with a SOP, or list of actions they need to take in order to investigate a ticket. This can include data retrieval steps to build a profile of the customer’s activity, analysis steps to reason about whether fraud is taking place (and if so, what kind), as well as actions the agent can take once a decision is made, like escalating tickets for human review.

Customers can create an SOP on Finic from scratch or import an existing document to **automatically generate each action based on existing SOPs.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85671&key=user_uploads/139135/d3036616-7071-4c1a-a95d-9777fe9b412c)

### **Tools**

Fraud analysts need many tools to conduct an investigation, from internal dashboards to SQL tables to vendor data.

Finic uses intelligent automation to connect to any data source and use it the same way a human analyst would: through a browser.

Rather than waiting for the engineering team to build new APIs, all it takes to get started with Finic is a list of credentials for the tools they use, drastically **reducing the time it takes to get to ROI.**

### **Audit Logs**

Whether the investigator is an AI agent or a human analyst, keeping a trail of why decisions were made is just as important as making the right decision. In fact, several regulations mandate that financial institutions keep logs of not just transactions but also the reasons why transactions or accounts were flagged as fraudulent.

Finic agents “think out loud” and document each step in the SOP, including what data sources they used, how they arrived at their conclusions, and what steps they took afterward. This makes it easy for senior analysts to review agent activity to ensure compliance and is usually more comprehensive than the reports generated by junior analysts.

## Learn more

Here’s a list of some of the types of fraud we’re helping customers remediate:

* Identity Fraud: Reviewing KYC tickets to determine if new signups are using stolen/synthetic identities, or if the account is being used as a proxy by a malicious third party.
* Friendly Fraud: Reviewing account activity and dispute packages from third parties to determine if customer-reported issues like credit card chargebacks are legitimate.
* Account Takeovers (ATO): Reviewing accounts flagged with unusual login activity, and looking at device fingerprint, IP address, transaction activity and other signals to determine if the account has been compromised.

If you’re a fintech looking for ways to 10x the capacity of your fraud ops team without increasing headcount, **email me at **[**jason@finic.ai,**](mailto:jason@finic.ai)** and I’d be happy to show you a demo.**

## 🌱 Dealwise: an AI powered investment bank for startups

We’re Jason and Ayan from the W23 batch of YC, and we’re building **Dealwise, an AI powered investment bank for startups**

### **TL;DR:**

Dealwise helps founders sell their startup. We use AI to automate the back office work associated with dealmaking. This let us serve startups too small for traditional investment banks, while running an accelerated process that gets founders offers in half the time.

Contact me at [jason@godealwise.com](mailto:jason@godealwise.com) or visit [godealwise.com](http://godealwise.com) to learn more!

### Background

Before being founders, Ayan and I were each other’s PMs and software engineers at Robinhood. Around August 2023, we noticed a lot of interest in M&A activity from our founder friends, including one batchmate who we advised informally in the sale of his startup. We started learning about what it takes to get deals done, and that’s when we realized there was a massive gap in advisory services for founders who want to step off the venture path (or were never on it in the first place) that existing service providers don’t fill.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77023&key=user_uploads/139135/6ef79a46-b348-4364-b427-e798acfd74d7)

### **The problem**

Selling a company is hard. In fact, **over 90% of deals fall apart before the transaction closes!** Acquisitions are like babies - each one is a miracle, but somehow they still happen all the time. This difficulty is why the investment banking industry rakes in over $300bn per year. 

Given the high failure rates, founders must run an efficient process. They can’t afford to waste months or even years on a deal that never closes.

Unfortunately, if you’re the founder of a startup worth less than $50M, no reputable investment bank is going to work with you, as they won’t generate enough in fees for it to be worth their time.

This leaves founders with just a few options that, frankly, all suck.

**Traditional M&A Advisors**

There are many M&A advisors (sometimes called business brokers) in the lower end of the market that work with small businesses. However, selling a small company is just as much work as selling a much bigger one, so successful advisors tend to move upmarket. That means most advisors working with startups are either bad at their job, or very new and inexperienced. 

Due to the high failure rates in M&A, advisors sign as many clients as possible and lock them in to exclusivity agreements that ensure they get paid a fee if any client sells in the next 2 years, regardless of whether the advisor was involved. This is not an extreme case, **these predatory agreements are the norm** for M&A advisory firms.

Plus, traditional M&A advisors almost always come from a business background - few understand the software industry or have networks that are better than the founders they work with.

**Marketplaces**

Marketplaces like Flippa or Acquire.com are great for four, five and six figure transactions paid for in cash by individuals, but serious corporate and institutional buyers avoid these platforms.

For transactions that are seven figures and up, buyers usually need some combination of equity and/or debt financing, which means the bar is much higher for diligence. It also means founders expect a lot more support through the process than what they get listing on a public marketplace.

**DIY**

Given the alternatives, it’s no wonder most founders with between $1mm and $5mm revenue opt to DIY their acquisition process.

Unfortunately we see many founders who’ve gotten stuck in a viscous cycle of: spend time chasing buyers → get distracted → growth declines → selling gets harder → spend even more time chasing buyers → growth declines more → ultimately shut down.

The median founder sells 0 companies in their lifetime, so it makes no sense to become a M&A expert when you have a business to run.

### **The solution**

We started Dealwise in December 2023 to help startup founders get acquired. We use AI to automate the back office work, which means we get healthy margins on transactions that are too small for investment banks. More importantly, it allows us to **run a process in just 3 months** compared to the typical 6-12 months process for M&A advisors and investment banks. As a founder, it means you can get feedback sooner instead of wasting a year with an M&A advisor who’s stringing you along but not doing much work for you behind the scenes.

We’re new, but our track record is phenomenal. Traditional M&A advisors typically take a minimum of 6 months to close a deal, and 12 months or more if it’s their first deal. We went from launch → 7 figure deal closed in just 3 months, with several more under offer. Our record for clients was just 4 weeks from the start of our engagement to first offer submitted.

As we scale, we’ll apply our experience building LLM tooling at our previous startup to continue automating tasks like buyer prospecting, thesis generation, NDA signing, and data room creation so we can focus our time on supporting founders through their acquisition journey.

### **Why is this important?**

Patrick and John Collison sold a little known startup called Auctomatic in 2008 before founding Stripe. Sam Altman’s first company, Loopt, raised $30M from investors only to sell for a “modest” $40M. Before Uber, Travis Kalanick spent six years trying to make a startup called Red Swoosh work, at one point moving back in with his parents, before finally selling it in 2007. And Socialnet was considered a failure by its founder, Reid Hoffman, after being acquired for a “modest sum” in 2002.

For startups that struggle to hit escape velocity, sometimes the best option is to sell it so the founders can move on to greener pastures.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77023&key=user_uploads/139135/a9f2b058-74b2-404f-a8f0-eb8921afbc1a)

But selling a startup is a difficult, and often lonely process. We want to be there for founders when their VCs have stopped replying.

## **Our ask**

If you know a founder who are considering an exit, email me at [jason@godealwise.com](https://www.gsb.stanford.edu/experience/about/centers-institutes/ces/research/search-funds). We keep conversations 100% confidential and I’ll be more than happy to chat even if all they’re looking for is some advice and insights on the market.

The founders who will best fit for Dealwise have a few things in common:

* They sell software, or software-enabled services
* They have at least $1mm in ARR
* They are profitable or have a clear path to profitability
* They are motivated - if they had to choose between an exit and raising a round, they’d choose to exit
* They already have buyer interest and are looking to run a more competitive process

Learn more on [our website](https://godealwise.com/), or reach me at [jason@godealwise.com](https://www.gsb.stanford.edu/experience/about/centers-institutes/ces/research/search-funds) if you want to chat about acquiring or exiting a startup.
