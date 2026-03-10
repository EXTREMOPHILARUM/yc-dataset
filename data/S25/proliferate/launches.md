# Launches

## Proliferate: the open source company coding agent

**TL;DR:** Local coding agents can't do real end-to-end work at your company. Proliferate is the open-source, self-hostable platform for building company-specific background agents that can. Agents get their own sandboxes with secure access to your internal services, trigger from any event, and expose a live, multiplayer preview so your team can verify the work together. MIT licensed.

**Star the repo:** <https://github.com/proliferate-ai/proliferate>

**Get started self-hosting:** <https://docs.proliferate.com/>

**Sign up for self-serve waitlist:** <https://proliferate.com/waitlist>

**The Problem**

Coding agents today hit a wall the second they need to do real work. Fixing an actual bug means querying your staging database, reading internal Datadog logs, hitting proprietary APIs. You can't hand those keys to a generic cloud SaaS agent.

So you run agents locally. But that ties up your machine, forces you to babysit a terminal, and traps all the context on your laptop where nobody else can see it.

The most forward-looking engineering orgs- Stripe, Ramp, coinbase- spent months building custom infrastructure to solve this. Some are now merging 50+% of their PRs with agents.

Proliferate open-sources that infrastructure so every team can do the same.

**What teams use Proliferate for:**

* **On-call triage:** Sentry exception fires → agent reproduces the issue in a cloud sandbox → writes a fix → shares a live preview link in Slack for the team to verify.
* **Flaky test sweeps:** Cron job runs overnight → agent isolates flaky CI tests by running them 1,000x → PR is waiting by morning.
* **Mass migrations:** Bump React versions or internal API contracts across 50 microservices and fix the resulting breaking changes- automatically.
* **Team verification:** Agent gets a feature 80% done. Instead of reading the diff, the team clicks a live preview URL. A developer jumps into the shared terminal to fix the last failing test. Feature is merged.

**Demo: [https://youtu.be/H84HrOJx4QM](https://youtu.be/H84HrOJx4QM)**

**What makes it different**

Every agent gets its own sandbox with your Docker containers running, secure access to your internal services via our action catalog, and can be configured to respond to any trigger. Your code and data stay in your control- fully self-hostable, MIT licensed.

Another large difference comes with how your team interacts with the work. Reading AI-generated code is tedious. So every session produces a live UR. Sessions are multiplayer. Anyone on the team can jump in, check logs, or steer the agent in real-time.

**Our ask:** ⭐ Star the repo- we just open-sourced it. <https://github.com/proliferate-ai/proliferate>

If you're tired of handholding local agents and want to move them to the background with real infrastructure access, reach out. We're working closely with a handful of teams to help improve their engineering velocity and adoption of AI. [Book a demo](https://cal.com/team/proliferate/demo) or email [pablo@proliferate.com](mailto:pablo@proliferate.com).
