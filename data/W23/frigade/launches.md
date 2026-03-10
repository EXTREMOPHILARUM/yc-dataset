# Launches

## Frigade: Product onboarding that builds itself

Hey everyone, we are Eric and Christian, founders of [Frigade](https://frigade.com).

**TL;DR:** Frigade automatically learns your product and provides expert, in-product assistance to users. Now with Suggestions, Frigade can proactively teach your users in the context of the product itself.

https://youtu.be/FhHSj8YpR2U

# **🔴 The problem**

Many users never see the best parts of a product. Teams try to fix this but run into the same issues:

* Onboarding flows take too long to build
* Feature tours get stale as the product changes
* Users ignore help docs :( 
* Customer Success loses hours teaching users on Zoom
* Product teams rely on outdated screenshots, Looms, and Slack to explain the product

In-product guidance should be easy to create and maintain, but today it is neither.

# **🟢 The solution**

Frigade automatically learns your product by using it, and Suggestions create guidance directly inside your product from simple prompts.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95912&key=user_uploads/123251/af21223e-4d69-40f8-9cc3-c34827827206)

Write what you want users to learn:

“Show users how to use the new Calendar view in the Sales tab. Walk users through the key features.”

Frigade understands the latest version of your product and generates the experience directly from that context. You do not need a help center, articles, or any existing documentation for Frigade to work. It learns directly from the product itself.

No user flows. No element targeting. Nothing to wire up.

You can create:

* Onboarding for new signups
* Guided tours for new features
* Help for confusing parts of the UI
* Workflows for power users
* Role or plan specific nudges
* Contextual support at the right moment

Everything runs inside your real product and stays accurate as it evolves, without depending on any external help documentation or content.

# **🧪 Preview, refine, publish**

Instantly preview Suggestions to watch the experience run in your product. Tweak the prompt to adjust the tone or structure. Choose who should see it and publish. Users will see it at the right moment and can launch the experience instantly.

# **🧵 Who is using it today**

Teams across SaaS, AI, fintech, marketplaces, and more use Frigade to:

* Onboard users without a human in the loop
* Increase feature adoption
* Reduce support tickets
* Walk customers through complex workflows
* Educate users inside the product rather than sending them elsewhere

# **🚀 Try it out**

Frigade Suggestions are live today. Create your first in-product experience from a single prompt [**https://frigade.com**](https://frigade.com)

We’d love your feedback or questions: [founders@frigade.com](mailto:founders@frigade.com)

## Frigade AI: In-app support agent that adapts to your product automatically

**TL;DR: Frigade AI** is an in-app agent that keeps users moving forward with contextual, real-time guidance. It can generate step-by-step tutorials for complex workflows, highlight relevant features at the right moment, and even take actions directly on users' behalf to eliminate friction. Unlike traditional chatbots that rely on outdated help center documents, Frigade AI learns your product by actually using it and automatically adapts to every product update without any work from your team.

📅 Book a demo → [calendar](https://cal.com/forms/ed0e923f-6f00-4191-a08f-7bebba6636b6)

https://www.youtube.com/watch?v=8SjL4OfPs3I

### **The Problem**

Most onboarding tools assume users follow a perfect path. They don’t. Users skip steps, explore features early, and ask questions that don't fit your predefined paths.

Support teams can’t scale to handle every question. Engineering teams don’t have time to build and maintain hardcoded walkthroughs. And most AI chatbots fall short, offering generic responses based on outdated help center docs. 

What users actually need is guidance **in real time**, **in context**, and **on demand**. Not just during sign-up, but throughout their entire journey.

### **The Solution**

Today, we’re officially launching [**Frigade AI**](http://frigade.ai), a fully integrated agent that lives inside your product and helps users get personalized support instantly. 

Unlike traditional chatbots, Frigade AI learns your product by actually _using_ it. It explores your interface, navigates your workflows, reads your documentation, and builds a working model of how your product functions. Just like a real user would.

The goal? **Help users succeed from their first session** and keep them unblocked at every step.

It works alongside everything you’ve already built, like checklists, tours, help centers, and fills in the gaps with real-time support when your users need it most. Frigade AI:

* **Unblocks users instantly** with dynamic step-by-step guides for any workflow
* **Eliminates friction** by taking product actions directly for users
* **Answers open-ended questions** with contextual product support
* **Escalates seamlessly** to Zendesk, Intercom, and other live support tools
* **Gets running in under an hour** with minimal engineering effort
* **Stays current automatically** as your product evolves

https://www.youtube.com/watch?v=usspoSsWIb4 

The result is an AI agent that **turns every user into a power user,** removing confusion and guiding users to success.

### **See It in Action**

If you're building a web app and want to better support users at scale, without scaling your existing support team, we’d love to show you what we’re working on. 

🔗 Check out our website at [https://](https://frigade.ai)[frigade.ai](http://frigade.ai)\[\
\](https://frigade.ai) 📅 Book a demo → [calendar](https://cal.com/forms/ed0e923f-6f00-4191-a08f-7bebba6636b6)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92353&key=user_uploads/123251/ef0698cc-01a2-4f96-97e6-f0c2a151ec6e)

## Trench: Open Source Analytics Infrastructure 🌊

Hey everyone! We’re Christian and Eric from Frigade. [Trench](https://trench.dev) is open source analytics infrastructure for tracking events, identifying users, and querying data in real time.

It’s built on top of ClickHouse and Kafka for speed and scale, and it can be deployed with a single production-ready Docker image. Trench is a major part of Frigade’s infrastructure and powers our own in-product analytics and user targeting for millions of end users.

The code is MIT-licensed at <https://github.com/frigadehq/trench>. We just launched, and Trench gained over 1,000 GitHub stars ⭐ in less than a week.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85509&key=user_uploads/123251/443f6361-9b1a-45d5-921e-e79504ebdcea)

# **Demo:**

Check out our open source demo to see how to build your own version of a Google Analytics dashboard powered by Trench in less than 15 minutes.

<https://demo.trench.dev/>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85509&key=user_uploads/123251/049bc7b3-bd4a-4038-8128-faa2a8e2cc67)

# **🚨 The Problem: Postgres doesn't scale for tracking and querying millions of events at scale**

As we’ve scaled [Frigade](https://frigade.com) to millions of end users, our Postgres table we used for event tracking was quickly ballooning in cost and becoming a performance bottleneck. Many companies run into the same problem as us (e.g. [Stripe](https://brandur.org/fragments/events), [Heroku](https://brandur.org/fragments/events)). \
Engineers start by adding a basic events table to their relational database, which works at first, but breaks down as the user base scales. It's usually the biggest table in the database, the slowest one to query, and the longest one to back up. Postgres (or MySQL for that matter) simply isn't a good solution for tracking and querying events in real time at 1M+ end users scale.

# **The Solution: Fast, scalable, and affordable event tracking**

We knew we wanted to move to technologies like Kafka and ClickHouse that are purpose-built for ingesting and querying thousands of events per second. When we looked for existing solutions, all the existing OSS projects we found were either bloated with unnecessary features, UIs and spaghetti code, or simply antiquated. So we built Trench.\
With Trench, we've put together a single Docker image that provides a production-ready tracking event table that scales. When we migrated our tracking table from Postgres to Trench, we saw a 42% reduction in cost to serve on our primary Postgres cluster and eliminated all lag spikes from autoscaling under high traffic. We're happy with how Trench has solved event tracking for us, and now we’re excited to share that with other teams.

### **Core Features**

* Compliant with the Segment tracking specifications
* Can handle thousands of events per second on a single node
* Query tracking data in real-time with read-after-write guarantees
* Send data anywhere with throttled and batched webhooks
* Single production-ready Docker image
* Easily plugs into cloud-hosted ClickHouse/Kafka solutions

### **Use cases**

What can you build with Trench? There are many use cases:

1. **Real-Time Monitoring and Alerting** – Monitor your services and get alerts through tracking custom events like errors, usage spikes, or specific user actions, and send that data anywhere with webhooks.
2. **Event Replay and Debugging –** Capture all user interactions in real time for event replay services.
3. **A/B Testing Platform** – Capture events from different users and groups in real time. Segment users by querying in real time and serve the right experiences to the right users.
4. **Product Analytics for SaaS Applications** – Embed Trench into your existing SaaS product to power user audit logs or tracking scripts on your end-users' websites
5. **Build a custom RAG AI model** – Easily query event data and give users answers in real time. LLMs are really good at writing SQL.

# **Try it out and give us a star ⭐**

We hope you’ll find Trench useful if you’re facing or have ever experienced a similar problem with analytics at scale. Here are some links to get started:

* Trench website: <https://trench.dev>
* Quickstart guide: <https://docs.trench.dev/quickstart>
* Github repo: <https://github.com/FrigadeHQ/trench>
* Product demo: <https://demo.trench.dev>

## Frigade – Growth platform for modern software teams

# **tl;dr**

[Frigade](http://frigade.com) is a low-code tool for building product growth loops. It comes with pre-built React UI components, a web app, and flexible APIs. Our customers use Frigade to build product growth experiences similar to those used by companies like [Notion](https://www.productonboarding.com/notion-feature-announcement), [Github](https://www.productonboarding.com/github-embedded-promotions?view=components), and [Mercury](https://www.productonboarding.com/mercury-new-user-onboarding).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78903&key=user_uploads/123251/7ac8ec05-e94e-4f88-93c2-561aae34289d)

\---

# **Founding Story**

Our team first met at LinkedIn where we built internal tooling to help accelerate company growth. Turns out many of the best companies in the valley also had large growth teams dedicated to building the same powerful tooling.

These platforms made it easier to ship new experiences with functionality like user targeting, air traffic control, state management, admin tooling, and much more.

However, many companies lack the resources to develop this kind of tool. With Frigade, we are building the growth platform we wished we had everywhere we’ve worked since LinkedIn, and we’re making it available to all teams.

\---

# **What kind of experiences can Frigade power?**

* **Onboarding forms** — like Typeform, but native
* **Product checklists** for user activation
* **Guided tours** for feature adoption
* **Announcements** for engagement and adoption
* **House Ads** to nudge users toward upgrades and adoption
* **Surveys** for user research and account enrichment
* **Custom Flows** to power unique in-app experiences

\---

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78903&key=user_uploads/123251/cc206e9a-c6cf-4e23-ade4-d1a8b60e924a)

# **How does Frigade work?**

Frigade combines React components, an admin dashboard, and flexible APIs to allow teams to build growth loops, faster.

**React UI Components**

Frigade includes a library of beautiful, pre-built React UI components based on industry best practices. Our components are fully customizable to your brand and product so they feel seamless.

**Web App**

Frigade’s web app helps technical and non-technical users alike with user targeting, performance metrics, user and account progress, and more. Frigade integrations help you connect tools like Mixpanel and Segment with a few clicks.

**Flexible APIs**

The Frigade API is designed to give teams full control over their experience, unlike rigid no-code tools. Teams can even use our APIs to build fully custom Flows.

\---

### **Our asks:**

* **Sign up** for free at [frigade.com](http://frigade.com) to get started
* **Grab a demo** with our team [here](https://cal.com/team/frigade/frigade-demo) to discuss your use cases

## 💻 Frigade - The easiest way for developers to build product onboarding.

**_TL;DR_** _Frigade helps developers build best-in-class product onboarding and education_ faster. _Check us out at_ [_frigade.com_](http://frigade.com)_!_

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68103&key=user_uploads/123251/acaad972-6a2d-45b3-817c-00685b328449)

Hello everyone! We’re [Christian](https://www.linkedin.com/in/cmathies/) and [Eric](https://www.linkedin.com/in/ericbrownrout/). We’ve been working together since 2015 when we first met as interns at LinkedIn, and we’re excited to be building Frigade. Our goal at Frigade is to make it easy to build great product onboarding so developers can spend more time building their core product experiences.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68103&key=user_uploads/123251/c42721d4-9f20-4993-b0ce-cac1c7a69fe2)

### **🔴 Problem: Product Onboarding is Hard**

Product onboarding is essential to customer activation and retention, but building great onboarding is difficult and time consuming. We know because we experienced this problem firsthand at our previous startup where we spent enormous amounts of time building onboarding and education for our app through trial and error. Time that could’ve been spent developing our core product offering.

ㅤ

### **🟢 Solution: Powerful API and Open Source SDK**

Frigade’s API and open source SDK take the hard work out of building and scaling great product onboarding. With Frigade, developers can:

* 🛠️ Quickly build beautiful onboarding within their own app UI
* 🔄 Ingest onboarding data from our API into their backend
* ⚡ Make instant changes to copy, assets, and logic via API
* 🎯 Easily build user targeting (powered by Segment, MixPanel, etc.)
* 📚 Automatically leverage built-in industry best-practices

As a result, developers can spend less time building features for product adoption and more time building the product roadmap.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68103&key=user_uploads/123251/e768b350-e12d-4e11-976b-042f82f1def3)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68103&key=user_uploads/123251/52788266-214c-4314-a0a9-dc7d270afdde)

[_Frigade SDKs_](https://github.com/FrigadeHQ) provides beautiful, extensible boilerplate for critical flows.ㅤ

### **💻 Try it yourself**

Check out our [GitHub page](https://github.com/FrigadeHQ) and [website](https://frigade.com). We’re here to help! Feel free to contact us at [founders@frigade.com](mailto:founders@frigade.com) with any questions regarding implementation, feature requests, or to chat generally about your product onboarding needs. And if you’re in San Francisco, come say hey!

ㅤ

**Thanks!**

Eric and Christian
