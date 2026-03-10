# Launches

## Windmill: Turn scripts into internal apps and workflows

## Developer platform for APIs, background jobs, workflows and UIs

Windmill is an open-source developer platform to quickly build production-grade internal apps, workflows and integrations from scripts in Python, Typescript, Go, Bash, SQL.

Open-source alternative to Airplane and Pipedream. Simplified Temporal with automatic app generation. Usable as a self-hosted AWS Lambda.

Sync your scripts from your GitHub repo or write them directly on Windmill, have them be converted to apps and no-code modules automatically. Use those apps as standalone (triggered on demand, by webhook or schedule) or build powerful flows using those scripts. The experience is similar to no-code tools except that at any point, any module can have its code inspected and tweaked. Leveraging the open-source community, we will build an exhaustive library of scripts for all APIs and generic tasks on [hub.windmill.dev](https://hub.windmill.dev/).

You may also wrap Windmill with your own frontend to provide automation as a feature on top of your own SaaS.

Focus on your business logic for all kind of flows, Windmill is the platform to build, share and run them.

## Active Founders

**Ruben Fiszel**

Ruben was top of his class MSc in CS at EPFL, did research on compilers from Scala to Hardware at Stanford, built the first open-source library for reinforcement learning for Java, built distributed systems at scale at Palantir and ran the engineering team at a Multi-Party Computation startup. He is now building Windmill, an open-source alternative to Retool, Pipedream, Airplane that contains the infra to run it and that you can deploy at scale.

### The sweet spot between low-code and code from scratch

### Open-source and self-hostable alternative to Pipedream and Airplane. Simplified Temporal

To build internal apps for ops, integrations between services that cannot talk to each other directly, or to run background jobs that run your business logic and analytics, the two main options today are no-code solutions and old-fashioned, roll-your-own scripting. Both have problems, and our goal with Windmill is to find a new sweet spot between the two. No-code solutions are productive _if_ your problem matches the tool exactly - but if not, they are rigid, hard to extend and quickly become tech debt, annihilating their initial time advantage. Indeed, no-code is just code but made by an opinionated someone else and hidden as a blackbox with an UI.

The alternative is to do it the old-fashioned way, writing everything from scratch, both backend and frontend, perhaps deploying it on the latest flavor of serverless, and pray to never have to touch it again because that took way too much time and it has now became a burden that the ops and business team might poke you about regularly.

Furthermore, the landscape of SaaS is specialized tools for everything—alerting, data analytics, administration panels, support management, integration between services—when it feels like a few scripts and some SQL would have been as good or even better and spared you the need of depending on one yet another tool. This could be even further facilitated if there was a way to import the right bunch of scripts from a fellow community of engineers, tweak it and deploy it like you can do in communities where automation can be shared as simple JSON files, for instance in the node-red or home assistant community… That’s the idea of Windmill: to bring back the power of scripting in an easy but high-scale production-grade way.

## What are good use cases for Windmill

1\. The biggest pain we solve is to turn scripts that you would run on your own laptop as internal apps that you can share with your team.

2\. Avoid SQL queries to production in favor of templatized SQL made into apps instead (automatically!). Making live SQL queries is common in DevOps, support and ops in general. It can be very error-prone, stressful and inconvenient.

3\. Integrations between tools you already use but that are unable to talk to each other.

4\. Workflows, background jobs: code that runs very frequently to react to new events, transform data and run your business logic. Many companies are a frontend on top of a database, and that database is updated in the background. We make it possible to build those workflows from simple scripts so that you can build it faster, more reliable and easier to maintain.

5\. The last one only apply if you are a SaaS that wants to provide automation as a feature of your product, or a no-code tools yourself. Because we focused very much on the hard-engineering of orchestration and specs for workflows, you might simply want to wrap Windmill to offer it to your own clients.

### Where is the catch, how do you make money

We make money from support, dual licensing of commercial licenses (for SaaS wrapping Windmill or for clients requiring it) and the hosted solution. On self-hosted, our Enterprise plan embedds:

* SLA & Priority Support 24/7
* Design partners for roadmap (priority on feature requests)
* Enterprise-specific features (Audit logs, Distributed dependency cache backed by S3, SAML support etc.)

We are workflows experts and would be happy to support you to transition to clean code working on open-source software.

You can however self-host it for free forever as long as you do not go against the AGPL license (keep open-source or do not provide it as your service).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65264&key=user_uploads/229730/0fe6dab5-5378-4e2e-ad66-930378bbe8ac)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65264&key=user_uploads/229730/5d176de7-2303-49de-adb4-9bb98c559506)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65264&key=user_uploads/229730/e1d39016-bd36-4241-b0df-a5f7799ef4f5)

**Docs:** [https://windmill.dev](https://windmill.dev/)

**Hosted app:** [https://app.windmill.dev](https://app.windmill.dev/)

**Self-host (star us!):** <https://github.com/windmill-labs/windmill#how-to-self-host>

**Discord to chat with the team/community:** <https://discord.com/invite/V7PM2YHsPB>

**Schedule a demo:** <https://www.windmill.dev/book-demo>

**Windmill on HackerNews:**

* [Aug 9 2022, HN Launch](https://news.ycombinator.com/item?id=32400849)
* [May 12 2023, Before v2](https://news.ycombinator.com/item?id=35920082)
* [Nov 22 2023, Why Windmill is the fastest self-hostable workflow engine?](https://news.ycombinator.com/item?id=38383138)
