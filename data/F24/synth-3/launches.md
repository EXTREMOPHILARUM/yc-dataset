# Launches

## Synth: Automated Training for Vertical AI Agents

Hi, I’m Josh, founder of Synth.

**TL;DR**

We log what your agent is doing, identify where it’s coming up short, and fine-tune the AI models your agent uses to prevent those failures.

You add a few decorators to your code, run your agent, and get back fine-tuned models (via OpenAI or the provider of your choice) that perform better. Our product, when applied to SWE-Agent, an academic baseline, delivers a **33%** relative improvement on the [SWE-Bench agent benchmark](https://www.swebench.com) with just 100 training data points. [ ](https://www.youtube.com/watch?v=DwC8iBLpWdU&feature=youtu.be)

**Why is this important?**\
Teams want to deploy software that automates economically meaningful tasks over multiple steps. Iterating on those systems is hard: an agent taking 100 steps to complete a task will often create a newspaper’s worth of text data over just one task run, and reviewing a representative evaluation dataset can be daunting. Moreover, getting language models to demonstrate context-specific agentic behavior - such as following strong plans and making the best use of their environment - can be challenging, just with manual prompt tweaking. 

Working as an agent researcher at a startup automating accounting tasks, I struggled to parse through the reams of logs my systems would generate every time I wanted to test a potential improvement. Manually tweaking dozens of prompts and reasoning about how changes would propagate through the system was also difficult— and, for many problems, ineffective. As agents are deployed in more challenging applications and to more customers, these problems will grow. Agent developers need a tool that scales with their agent’s complexity and scope in order to build state-of-the-art systems.

**Our solution**\
Synth works in 3 steps

1. Communicate: We summarize your agent’s logs to help you understand how it’s performing at a glance.
2. Flag: We identify common failure modes your agent is demonstrating.
3. Address: We fine-tune base models your agent uses to address AI-related issues and suggest changes to your code when gaps in agent scaffolding are the root cause.

We worked with a startup that was working on automating code generation to increase their agent’s success rate at an editing task from ~**85% to 100%** on a representative evaluation set.

**Why Now?**\
Developers and researchers have been building AI agents with language models for years, but only somewhat recently have base models provided a strong enough foundation to enable the most ambitious applications.

Moreover, some of the most powerful and consistent approaches for tuning agents to address domain-specific challenges— the ones powering Synth— have only been published in the last year or so. The market is ready for our solution, as is the research literature.

**Team**\
I recently worked at [Basis](https://www.getbasis.ai), a startup automating accounting tasks with AI agents, as a researcher developing and maintaining pipelines and agents used to serve top accounting firms. While there, I had the opportunity to publish [academic research](https://arxiv.org/abs/2406.11695) on the topic of agent optimization at EMNLP, a respected AI conference.

Before Basis, I built a startup doing ML for cyber with some friends that got acqui-hired right out of the gate for a modest amount. Before then, I studied math and machine learning at Yale.

**Ask**\
Send folks building agents our way at [founders@usesynth.ai.](https://mailto:founders@synth.ai) We’d love to talk to anyone using AI agents to solve hard, multi-step tasks - the more ambitious and complex the approach, the better.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85819&key=user_uploads/89898/5d64c8db-48e1-423a-a020-f5ace9ea7b82)
