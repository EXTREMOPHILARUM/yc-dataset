# Launches

## Hyrex - The Open-Source COLD Task Framework

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93335&key=user_uploads/1967655/4c6a3685-1d2e-4f71-8808-ffcbd2a920a8)

\
We’re Mark and Trevor, founders of [Hyrex](https://hyrex.io). We’ve written a lot of software over the years at Google, NASA, and multiple startups. As our focus has shifted to scalable web apps, we’ve come to appreciate the magic of asynchronous background task queues. They make it easy to build lightning-fast apps that can scale dynamically, while ensuring that essential tasks are completed with full confidence, in priority order. This distributed approach is more important than ever for building dynamic AI agents, indexers, and web-first apps.

Here’s a basic task orchestration architecture - you send tasks (i.e. function calls) to a queue, and workers pull them off and complete them in parallel.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93335&key=user_uploads/1967655/f29e6d7d-890b-4863-aa19-eea241e05714)

**The Problem**\
Unfortunately, none of the existing frameworks supported everything on our checklist. As we talked with developers working on startups, we learned that most shared the same experience. Some frameworks require extensive code rewrites, while others are difficult to configure and debug, or simply unmaintained. Most lack a deep commitment to open-source, and many require dependencies on outdated or niche technologies. As you can probably guess by now, we decided to build our own!\
\
**Our Approach**

We started with a few core creative constraints.

1. Only required dependency is a Postgres database.
2. Existing functions can be converted to tasks using just a decorator/wrapper. No changes to your core code that lead to lock-in.
3. Open-source first, with a higher-performance managed service with an identical SDK. Easy to switch back-and-forth.
4. Can be set up and tested in minutes.

And we ended up with Hyrex!

If you’ve used a task framework before, everything should work as you expect (and probably better)! If you’re new to task frameworks, everything you need to know is at [hyrex.io/docs](https://hyrex.io/docs)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93335&key=user_uploads/1967655/8472e657-3969-4e48-aa91-d4a8ecdc7f85)

\_(Hyrex Cloud in action)\_\
\
**What is COLD?**

Why do we call ourselves “the COLD task framework”? For each function you wrap as a Hyrex task, you get 4 properties needed for production-grade systems:

* **Controllable** - tasks can be sent from anywhere, anytime, with any configuration
* **Observable** - tasks status, results, logs, and metadata are easily available via a UI or programmatically
* **Large-scale** - workloads are horizontally scalable across any cloud infra (even multi-cloud)
* **Durable** - workers are fault-tolerant and self-healing, and tasks can’t be dropped once they’re in the system

With these built-in properties, your Python/TypeScript functions are ready to send with confidence. You can run them on schedules and easily chain them together into task trees to build products like Deep Research and dynamic AI agents.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93335&key=user_uploads/1967655/a9e116eb-a557-4687-8f6a-fd8242f72e3d)

Hyrex open-source requires only a Postgres database to run. Hyrex Cloud ([hyrex.io/cloud](https://hyrex.io/cloud)) provides higher throughput, GitHub integration with automatic deployments when you push changes, and built-in scalable worker pools. Both options use the same SDKs, so you can easily switch at any time!

**Hyrex Cloud pricing**

* $200/month - individual plan (1 project + 1 worker)
* $400/month - team plan (up to 5 members and 5 projects + 2 workers)

**Our ask:**

* Sign up for a 1:1 demo at [hyrex.io](http://hyrex.io)
  * We’d love to chat directly and help write your first Hyrex task!
* Try it out on your own!
  * Build your first Hyrex task in minutes using our quickstart guides: https://hyrex.io/docs/learn/getting-started
* Join our Discord ([discord.gg/hyrex](https://discord.gg/hyrex)) for questions and discussion

## Kura | The AI DevOps Copilot

**TL;DR:** [Kura](https://www.usekura.com/) integrates directly with services like AWS, helping software teams respond to incidents, provision infrastructure, and optimize complex cloud systems.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83339&key=user_uploads/1967655/a1945e14-3f49-4491-8e31-d40335e6f5ab)

Hello YC! We’re [Trevor](https://www.linkedin.com/in/trevorar) and [Mark](https://www.linkedin.com/in/markedwarddawson/), founders of Kura. After building distributed systems for a combined \~15 years at places like Google and NASA, we know the challenges and triumphs of cloud-based products. We started Kura with the core belief that recent AI advancements can unlock the potential of software teams building on the cloud.

# **What’s the problem?**

As web apps become increasingly core to the world, maintaining cloud infrastructure requires increasingly more time and resources.

* Distributed systems are getting more complex than ever
* Managed solutions trade off ease against control and cost
* Cloud infra engineers are few and far between, leaving much of the work to teams who may not have extensive cloud experience

# **What can Kura do?**

Kura is a chatbot and workspace that integrates directly with a live index of your cloud infra from services like AWS, GCP, and Azure.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83339&key=user_uploads/1967655/be157dd9-7ee9-48bf-af07-aca46efca63c)

**Kura can answer questions about your cloud system**, providing links and live information for queries like:

* “Is my main API cluster healthy?”
* “Which container version is running in prod?”
* “Can you help me deploy a new container via CDK?”

**Kura can run pre-packaged and user-defined “runbooks”** to proactively surface issues via notifications. For example:

* Scheduled checks for over/under-utilized computing resources
* Discovering and surfacing cost spikes and trends
* Searching for common security vulnerabilities

With Kura, software teams can build faster and more confidently on the cloud, all while maintaining full control of their critical infrastructure.

# **Our ask:**

* If your team is building on the cloud and would like to learn more or sign up as a pilot customer, please reach out to [founders@usekura.com](mailto:founders@usekura.com).
* If you know software teams or developers running into roadblocks due to cloud complexity, please send this post their way - we’d love to chat and learn more!
* Follow us at [@kura_labs](https://x.com/kura_labs) to follow along on the journey!
