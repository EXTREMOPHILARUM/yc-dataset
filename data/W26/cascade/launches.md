# Launches

## Cascade: Evaluation Infrastructure to Run AI Agents Reliably

Hi YC! 👋

We’re Adam and Haluk - Co-founders of **Cascade**. We’re building evaluation infrastructure that makes AI agents work reliably in production.

**TL;DR:**

Companies are trying to deploy general-purpose AI agents onto highly specific workflows. They fail in subtle ways, teams can’t see the full scope of those failures, and the agents are vulnerable.

Cascade learns from real agent behavior in production and turns it into training signal, allowing the agent to continuously improve after deployment.

We believe every company will end up with its own operational intelligence - models and agents specialized to how that organization actually works and the data it uniquely produces.

🎬 **Launch Video:**

<https://youtu.be/MNVVHCZHwc4>

🚨 **The Problem:**

Right now organizations deploy generalist agents into custom processes. An agent that preforms well on benchmarks might fail terribly in production. Teams understand these pains: 

* Knowing the agent is failing but not understanding why
* Writing evals that cover an immensely large scope
* Hitting a performance plateau
* Getting prompt injected 

Teams inspect logs, tweak prompts, and write rubrics but they’re mostly guessing. As a result they can’t deploy agents where they matter most.

🚀 **Our Solution:**

Cascade treats agent execution as data.

We observe real production runs and train evaluator models that learn what correct behavior looks like inside a company’s workflows. We analyze reasoning steps, tool usage, and outcomes to detect failure modes, threats, and reliability issues automatically.

Those evaluations are then converted into structured feedback that can improve rubrics, prompts, and models.

👨‍💻 **The Team:**

We’re best friends from UC Berkeley who were working on different research problems around agents systems and reliability. Over time we realized both of our work was pointing to the same underlying issue, and almost everyone deploying agents would have the same problem. We gave up our return offers and paused PhD paths to build Cascade.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98179&key=user_uploads/2719107/02f486fa-196d-4058-a9b7-156e67a51372)

Haluk previously built production monitoring infrastructure and scaled agent systems at companies like Netflix and Amazon. His research at BAIR Lab covered long-horizon memory optimization and failure mode taxonomies for AI agents. Haluk studied Computer Science and Mathematics at UC Berkeley.

Adam previously conducted research at BAIR Lab, where his work focused on graph reasoning models, and agentic safety under some of the world's leading ML and AI safety researchers. He studied Computer Science at UC Berkeley.
