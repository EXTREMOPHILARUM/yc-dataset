# Launches

## Polymath: training grounds for AI agents

## Tldr;

Polymath is building **world generation models and systems** to **automate and align** the creation of reinforcement learning environments.

## Problem

We’re at the very beginning of the agent era. The demand for AI is shifting from models that simply answer questions to agents that can operate autonomously over days and weeks. Models have become incredibly proficient at short tasks, but fail when asked to perform **long-horizon work** that requires proficiency with a **diverse set of tools**.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98237&key=user_uploads/2471616/0489f25a-b235-4d6f-ade3-86a0a5b4897c)

(source: <https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/>) 

Static datasets are no longer sufficient. To improve the performance of autonomous agents, they must be trained inside environments that reflect the real world.

**Today, RL environment generation is bottlenecked by human labor.** Companies hire contractors to hand-build tasks and artifacts one by one. This approach is expensive and doesn’t scale. Moreover, human data alone will never lead to superintelligence.

On the other hand, **purely synthetically generated environments are not aligned** with the real world and are untrustworthy.

## Solution

We’re developing **world generation models and environment factories** to automate and align the creation of RL environments, with humans in the loop. This allows for more complex and realistic worlds, and higher quality, scale, and diversity of tasks. This will be essential to unlock **RL scaling**.

## Horizon-SWE

We recently launched Horizon-SWE, a benchmark that drops frontier models into a simulated software company.

It consists of a **running application, real tools, and long-horizon tasks** covering the entire software development lifecycle (planning, coding, testing, deployment, monitoring).

The benchmark measures the ability of AI agents to perform **end-to-end SWE tasks**, as opposed to code generation alone. Leading models score around 25% on the benchmark.

Read more about our methodology here: <https://www.polymathlabs.ai/blog/horizon-swe>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98237&key=user_uploads/2471616/a86c29a4-fcff-4ae9-a7fe-53bdf6234300)

## Team

Polymath is a team of researchers and engineers from UC Berkeley, Hume AI, Plaid, and Amazon. We have years of experience post-training frontier models in industry, and building large-scale data systems. Now we’re building the foundation that will enable the next generation of autonomous agents.

\
If you work at a frontier lab and are interested in acquiring environments, or know someone who is, we’d love to chat! ([founders@polymathlabs.ai](mailto:founders@polymathlabs.ai))

<https://youtu.be/uqc3TCWJCto>
