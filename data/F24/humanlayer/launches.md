# Launches

## HumanLayer - Human-in-the-loop for AI Agents and beyond

Hi 👋 I’m Dex, and I’m building HumanLayer.

HumanLayer lets your software contact humans for feedback, input, and approvals. It’s perfect for

1. Implementing manual approval steps for software- and human-driven workflows
2. Oversight of autonomous AI agents
3. Managing the transition between the two

HumanLayer has clients for Python and Typescript and lets you manage approvals across Slack, SMS, email, and other channels. For AI agents, HumanLayer is designed to work with any framework + LLM.

You can try it today at [humanlayer.dev](https://humanlayer.dev).

<https://www.youtube.com/watch?v=5sbN8rh_S5Q>

> _Ever since I got hands-on with HumanLayer, I’m asking my whole team to think more about Agentic AI workflows - I used to think agents were not worth the effort to get them to production-grade reliability, but now I'm stoked on what is possible when you bring humans into the loop_
>
> _–_ Vaibhav Gupta _, Founder_ @ [Boundary](https://www.ycombinator.com/companies/boundary) _(YC W23)_

### Why HumanLayer

Before HumanLayer, I was building autonomous AI agents. Our idea for an MVP was an agent that would coordinate with humans in Slack and could do basic cleanup, like dropping any Snowflake/SQL table that hadn’t been queried in 90+ days. We had already built a platform to generate recommendations, but we wanted to push the limits of agent frameworks, **we wanted the agent to be able to actually do the work, not just generate the recommendations**.

Of course, we weren’t comfortable with an AI application running raw SQL unsupervised, especially if it had access to drop tables, so we wired in some basic human approval steps.

From there, I realized that **the most useful functions we can give to any software are also the most risky**. This is especially true for non-deterministic systems driven by LLMs. I realized that anyone who wants to build agents that do meaningful things will need tools for approval and oversight. So, I started hacking on HumanLayer to enable teams to safely build high-impact agents and put them to work [ambiently and autonomously](https://theouterloop.substack.com/p/openais-realtime-api-is-a-step-towards) in the background.

### Use Cases

Whether you’re hard-leaning into AI or not, HumanLayer helps you build impactful automation that you can ship with confidence because you have humans in the loop for the critical operations. Forget months of tuning or broken use cases on every iteration; **build confidence incrementally** as you observe and test your apps in production (safely!).

* **Internal Automations** - review/approve outbound emails or automated infrastructure changes
* **Dynamic Data Labeling** - think [RLHF](https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback) driven by the experts in your company - Use collected human feedback for **benchmarking** human vs. AI performance and for **fine-tuning** AI agents
* **Ship fast and iterate** - Roll out advanced AI features to customers without needing to get to “perfect.” Human review guarantees nothing bad can happen without needing to spend months on evals, tuning, and prompt engineering. Then, iterate based on how your agents behave in production.
* **Customer-facing** **control and visibility** - help your customers build trust in automations by giving them hooks to approve/review your app’s actions

> _Really enjoying playing with @humanlayer_dev - instead of the manual outreach grind, I just hang out in slack and give my agent feedback as it finds new leads_
>
> – Tom Granot, founder, <https://syntaxcinema.dev>

### 

### Quick Example

Integrate HumanLayer into your **python** or **typescript** app using a decorator or webhooks.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85104&key=user_uploads/1459029/2ea2f1d9-c06d-4e03-a64e-62c650e1743c)

To let AI apps contact a human for natural language feedback/input, just pass the `human_as_tool()` function into an AI agent’s tool set.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85104&key=user_uploads/1459029/4035e3d6-b850-4e14-b1b1-a64193cb5d75)

### Team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85104&key=user_uploads/1459029/f649e7e6-c37d-48d4-88ee-4d265c4983d4)

I’m [Dex](https://linkedin.com/in/dexterihorthy). I am obsessed with helping devs everywhere deliver safe + impactful AI agents.

I spent the last 7 years at <https://replicated.com> where I helped great developer teams like DataStax and H2O.ai build and launch the kubernetes-native versions of their self-hosted products. I worked on container orchestrators, led product teams, and founded the GTM org.

I can’t wait to build the future of AI Agents with y’all.
