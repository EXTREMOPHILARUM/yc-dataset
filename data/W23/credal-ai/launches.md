# Launches

## Credal.ai: The Security-First Multi-Agent Collaboration Platform

Ravin & Jack here from [Credal.ai](http://Credal.ai). Proud to announce the world’s only multi-agent platform in production at Enterprises that lets Agents collaborate across Enterprise systems like GSuite, Salesforce, and Slack while respecting the permissions of the end users across those tools. We’re in production at amazing Enterprise customers like Mongodb, Wise, Checkr, Lattice, and even at traditional Enterprises like Comcast, the US Federal Government (HHS), and the IFRS — and we’re now excited to bring it to the world.\
<https://youtu.be/hNhfq0vfei0>

## The Problem

AI can understand enterprise data and provide marginal productivity gains, but we know that “Chat with your data” doesn’t scale—especially in complex operations.

Getting users to adopt AI for simple tasks, like improving email wording or summarizing meeting notes, is easy. But these small wins don’t fundamentally change how an organization operates. It’s no surprise that 74% of companies still struggle to achieve tangible value from generative AI in 2025; most companies remain stuck in the proof-of-concept phase.

AI is not truly transformative at the enterprise level, and we at Credal want to change that. To solve for this problem, AI agents must integrate into enterprise operations—communicating with internal systems, other agents, and subject matter experts while ensuring security, governance, visibility, and ultimately real business impact.

## 💡 Our Solution

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88742&key=user_uploads/89898/75296e1a-0363-4079-9f82-0c5a9d786d1b)

Credal enables enterprises to deploy secure, specialized AI Agents that collaborate to handle complex, multi-step workflows.

Each Agent is designed by subject matter experts—your employees—for specific tasks like:

* Researching a prospect and personalizing outreach
* Conducting KYC and AML checks
* Answering HR and IT helpdesk questions
* Completing security and compliance questionnaires
* Analyzing trends in revenue and churn and suggesting the next best action for Customer Success Managers or Account Executives.

When a user or API call invokes an Agent, it can autonomously call other Agents for assistance, all while enforcing enterprise-grade governance, risk, and compliance (GRC) policies. This composability moves beyond single-agent AI, allowing for scalable, controllable, and secure AI adoption across complex workflows in the enterprise. AI can at last operate seamlessly across your systems while respecting permission boundaries.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88742&key=user_uploads/89898/2c33a821-eabf-402e-a866-a552b5ca4590)

## How it Works

Every user request follows this pattern:

The request gets routed to a primary agent which decides whether to call any actions or other Agents based on:

* The instructions you provide in the background prompt and feedback from previous interactions
* The provided tools and agents, with their descriptions and associated RBAC settings
* Access Controlled Data from Enterprise systems like Salesforce, Confluence, GDrive, Slack and Sharepoint.

The primary agent then:

* Notifies the user of any actions it is calling
* Parallelizes the submission of all relevant actions
* Polls for responses
* Notifies the user when responses come back

## ⚙️ Use Cases

✅ End-to-end Know Your Business (KYB) workflows:

* Validate document authenticity
* Cross-check business addresses
* Detect politically exposed persons (PEPs)
* Ensure company services comply with internal policies

✅ Go-To-Market Automation

* Deep research on prospects and target accounts
* Identify intent signals and the right buyers
* Automate personalized outreach and seller training
* Suggest Next Best Actions and upsell opportunities

✅ Security Questionnaires

* Automate security and compliance questionnaire responses no matter what tool you have to upload your response in
* Ensure regulatory alignment with minimal manual effort

✅ HR & Performance Management

* Draft and refine self-reviews
* Validate manager reviews for consistency and bias

…and much more, including vendor contract analysis, government agency rule-making, corporate standards setting, customer support automation, training across teams, and general-purpose “ask-anything” AI assistants.

## Next Steps

With Credal, enterprises can finally operationalize AI at scale—securely, efficiently, and with full control.

Ready to power your business with intelligent AI Agents?

Let’s talk. Contact us at [sales@credal.ai](mailto:sales@credal.ai) or book a demo at [credal.ai/get-started](http://credal.ai/get-started).

## Credal: Control how AI uses your data

Hi there! Ravin and Jack here from [Credal.ai](http://Credal.ai)

**TL;dr:**

Credal protects your sensitive data across all AI apps. We give everyone at your company access to the latest AI models via our secure Chat UI, integrated with your data, whilst management gets granular control over what data is shared with each provider.

⚔️ **The Problem:**

CEOs of every company from Microsoft to our YC W23 batchmates understand the massive productivity gains available through AI applications. But huge concerns exist over adopting these tools at the enterprise: what’s happening to our data once we hand it over to AI providers? The landscape of providers is already large and fast-growing. Many have terms of service that permit training general models on your data. As the usage of these tools explode, businesses risk losing control over what data has been shared with whom, when, and what technical and contractual safeguards are in place to protect that data from inadvertently ending up in the hands of competitors via an AI model’s training dataset.

⚡ **Solution:**

Credal is the gatekeeper for your data, ensuring that all data sent to AI is protected by 3 layers of security:

1. Credal identifies sensitive data using our (self-hosted) detection models alongside your existing data classifications and lets you automatically redact, anonymize, block, or simply warn the user, if sensitive data is about to be sent over to a provider.
2. For the major endpoints like chat or text completion, Credal allows you to seamlessly switch between providers: letting you take advantage of the latest models, or highest privacy models as they are released, without locking your company into a single vendor.
3. Finally, Credal protects you with standardized Terms of Service and MSAs that ensure you have total control over your data. Credal links your audit logs to the specific provider associated with each request, allowing full transparency into both the technical and contractual safeguards that govern how any cut of data could be used.

Our secure chat UI can automatically route your request to the best AI for your question (or you can specify manually)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70320&key=user_uploads/1038471/53a41cac-1a2c-4bc6-9441-cc87ed0ef0d3)

With granular audit logs on each request, per data source, including what was redacted:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70320&key=user_uploads/1038471/fb382a2e-54de-47ec-b03e-93cc332981a9)

**Who needs this, and why did we build it?**

Our current customers are security-conscious companies trying to use AI to get an edge in their operations and product. We noticed early on building AI applications that customers were really nervous about handing data over to AI models they didn’t fully understand. Many enterprises were turning ChatGPT off entirely, or banning its use on anything remotely sensitive. Today, our customers use Credal for a range of problems, from basic things like using ChatGPT for summarizing meeting notes, to using complicated combinations of AI (like Claude + GPT 4) to automatically structure company documents. Either way, Credal is giving our customers the confidence they need to use cutting-edge AI on sensitive data.

**Meet the Team:**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70320&key=user_uploads/1038471/77898790-6a46-477b-8832-df0f5cecd528)

Jack and I met in 2019 when we co-led Palantir’s engagement with a multibillion-dollar Life Sciences conglomerate, steering it from an initial pilot to an enterprise deal so critical to their business that Palantir going bankrupt was mentioned as a risk on the customer’s S1 filing.\
\
I started my career at Google, and since then have been both in the trenches and leading teams at THG at Series A, GoCardless at Series A, and Palantir. Jack started his career at H1 (at pre-seed), before joining Palantir. We’ve both led highly acclaimed teams at Palantir: _Atlantic_ Magazine called the output of work I led for 18 months: “America’s most reliable pandemic data”\[1\] and the _Washington Post_ said of a team Jack led for a year: “With these systems aiding brave Ukrainian troops, the Russians probably cannot win”\[2\]

We’re bringing a wealth of expertise in handling the most sensitive data imaginable, into what we see as one of the central problems of our time: building trust in AI.

**Interested?**

If you are an enterprise with sensitive data, but you want to be able to use that data with AI  - [grab time to chat with us](https://calendly.com/jack-fischer-credal/credal-ai-intro). Enterprises that sign up before Demo Day (April 5th) are eligible for 50% off!\
\
Footnotes:

\[1\] <https://www.theatlantic.com/health/archive/2021/01/hhs-hospitalization-pandemic-data/617725/> (The article discusses whether the Biden administration would keep paying for the ‘vital system’ that HHS had procured under Trump. In case you’re wondering what happened, it did and even expanded the contract.

\[2\] <https://www.washingtonpost.com/opinions/2022/12/19/palantir-algorithm-data-ukraine-war/>
