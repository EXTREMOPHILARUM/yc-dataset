# Launches

## Hatchet - Background task orchestration and visibility platform

**tl;dr** - At a certain scale, all applications need a task queue - think Celery for Python, BullMQ for Node.js, and Sidekiq for Rails. [Hatchet](https://hatchet.run) is an [open-source](https://github.com/hatchet-dev/hatchet), managed task queue focused on scale, reliability, and improved developer experience. 

<https://youtu.be/3myPYVyaqwM>

**The problem**

Building a reliable application is difficult — network connections can fail or be interrupted, the application could run out of memory, or a bad commit on production can take down your entire service. To reduce the pressure on APIs, task queues are typically used to offload different parts of the application logic to other services in the system.

However, these queues introduce more points of failure — they require new infrastructure, a new set of integrations to monitor and debug your tasks, and are difficult to use in development. As applications begin to scale, application developers are forced to implement solutions to avoid queue overflow and overcrowding and to think about how to optimize their queues.

With LLM APIs — which are high latency and highly variable in response quality — these problems are even worse. It’s now typical to ingest, sync, vectorize, and index the entirety of multiple data sources on account creation, and as LLM systems get more agentic, developers need to chain together unreliable LLM calls to fulfill requests. These requests are often slow and without the right architecture delivering a responsive and reliable user experience is challenging.

**The solution**

Hatchet is an **end-to-end platform** for task orchestration. It includes a web UI for monitoring tasks, an API for interacting with tasks and workflows, and SDKs for Python, Typescript, and Golang.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79258&key=user_uploads/363082/1617c928-fc04-4482-9b13-98c342e14694)

Hatchet has all the features you’d expect — like **retries, timeouts**, and **cron schedules** — along with features that developers are usually asked to build, like handling different **fairness and concurrency patterns**, **durable execution**, and **result streaming**.

**The team**

We’re both ex-CTOs and founders of multiple YC-funded companies — [Alexander](https://linkedin.com/in/alexander-belanger-aa3974135) was co-founder and CTO at [Porter](https://porter.run) (S20) while [Gabe](https://linkedin.com/in/gruttner) was co-founder and CTO at [Clearmix](https://www.ycombinator.com/companies/clearmix) (also S20). Before that, Alexander got his Master’s in Physics from UPenn while Gabe got his Master’s in AI from Cornell.

Alexander started working on this after years of wrangling task queues and distributed systems at both Porter and [Oneleet](https://oneleet.com), where he experienced the issues of building complex task orchestration and workflows. Gabe came at this from another perspective, having spent the last few years working with ML and more recently LLM stacks, where he saw the architectural problems that many of these applications have.

We immediately bonded over our excitement about what infrastructure will look like as AI becomes core to nearly every business.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79258&key=user_uploads/363082/e77d894d-1e99-4128-9bff-65f905d97571)

**How do I get started?**

Hatchet is fully open source with an [invite-only cloud offering](https://hatchet.run/request-access). Feel free to request access or check out the [self-hosting Hatchet](https://docs.hatchet.run/self-hosting) docs.

If you’re dealing with observability problems in your queue, are running batch processing of documents for LLM workflows, or are experiencing queue fairness problems in multi-tenant apps, we’d love to chat.

And if you have any questions — or you’re just interested in distributed systems, task queues, and scheduling — we have a [public Discord](https://discord.gg/ZMeUafwH89). See you there!
