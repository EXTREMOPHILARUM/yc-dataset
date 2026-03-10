# Launches

## ZeroEval - Build self-improving agents

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93136&key=user_uploads/208921/328fd273-24d5-4307-9322-075a26467fe9)

Hey everyone, we're Sebastian and Jonathan - founders of ZeroEval.

### **TL;DR**

ZeroEval is a tool that helps you build reliable AI agents through evaluations that learn from their mistakes and get better over time.

https://www.youtube.com/watch?v=hSkpdHE7mCs

### **The problem**

Evaluating complex AI systems is hard and time consuming. The more complex your agents get, the harder this issue becomes. This is especially the case when building:

1. Long-running, multi-turn agents with dozens of intermediate tool calls 
2. Agents where you want to measure the quality of images, video, generated UI, audio, personality, taste, etc

**Current offline eval methods are high-friction**, a lot of work is needed to continuously curate labeled data and write experiments and evaluators. 

On the other hand, **current LLM judges are static and often have terrible performance**, they lack context on how they fail and the nuances of the task at hand. 

Your AI agents are as good as your evals. Without them, surpassing the quality threshold your product needs will feel like a never-ending task.

### **What we’re building**

A way to create **calibrated LLM judges** that get better over time the more production data they see and the more incorrect samples are labeled. The more you teach it on where it's failing, the more reliable it becomes.

Once you have a judge that matches the human preference baseline, you can continue using it on production data or in offline experiments.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93136&key=user_uploads/208921/f815b7cf-a84e-4285-974d-1ffc943889ad)

We’re also introducing **Autotune**, a way to do automatic evaluation on dozens of models and prompt optimization based on a few human samples.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93136&key=user_uploads/208921/954461b0-5b4a-42b9-b464-0a698c3f6fd0)

We envision a future where AI software improves based on human feedback, where developers define the evaluation criteria as a starting point and errors back propagate to find the optimal implementation.

### **The team**

We met during their first year of college in Mexico over 7 years ago. During that time they worked on side projects together, joined a leading fintech startup as first engineers and most recently built [llm-stats.com](http://llm-stats.com), a leading LLM leaderboard website that reached 60k MAU and  ⅓  million unique users since its launch a few months ago.

* **Sebastian** was founding engineer at Micro building the future of email (backed by a16z), as well as founding engineer at Atrato (YC W21).
* **Jonathan** was an early employee on the LLM observability team at Datadog. He did undergrad research on vision transformers for particle physics and RL for robotics.

Foundational models have transformed the world. We’re building the second line of offense to fill their capability gaps and create AI products that actually work. We are determined to build the engine behind self-improving software for the following decades. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93136&key=user_uploads/208921/b912b213-762c-42ba-8fe5-dd39de8dd748)

### **Our ask**

If you have AI agents in production and are struggling to measure their quality and/or achieve the reliability needed for your product's success, we’d love to chat!

We don't just deliver a tool, but will sit with you to understand your pain points and help you build high quality evals.

Feel free to reach out at [founders@zeroeval.com](mailto:founders@zeroeval.com) or [book a demo](https://cal.com/team/zeroeval/demo).
