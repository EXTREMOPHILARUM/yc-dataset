# Launches

## Osmosis: Unlocking Real-Time Learning for AI Agents

What if AI agents could immediately learn from their mistakes?

## TL;DR

While AI agent capabilities continue to improve, the agentic workflows remain brittle since agents aren’t able to learn from tasks in real-time. Osmosis is a framework that helps your AI agents learn in real-time (similar to DeepSeek R1’s post-training loop) in order to make them better, faster, and more responsive.

On the first run, we scored 21.5% accuracy, which is 60% better than base 4o performance (16X more expensive!). **This means that even on a first run, we're 25X+ more cost effective than base 4o - and that would be significantly better on a second run.** We also averaged 7.5 steps per task while OpenAI Operator averaged 67 steps per task (faster and cheaper!).

If you’re building AI agents and want to make them better, faster, and more responsive, we’d love to chat! Email [kasey@gulp.ai](mailto:kasey@gulp.ai) or book time [here](https://calendly.com/kasey-gulp/).

## The Problem

AI agents still struggle with novel and complex (multi-step) tasks. Even OpenAI Operator (current state-of-the-art) just scores 58% accuracy on the WebArena benchmark. The worst part is that agents make the same mistakes again and again!

And even when agents can solve a task, there’s generally a lack of optimization in their process. This ends up negatively affecting performance while also driving up inefficient inference costs for users.

## The Solution

Osmosis builds and maintains a ‘library’ of an agent’s previous interactions. It’s a super simple two line addition in a developer’s agent infrastructure that:

* Ingests and understand a user’s prompt
* Queries a vector database to search for similar past scenarios
* Recommends a relevant plan of action for the task
* Quantifies an agent’s performance when it finishes, and embeds the assessment

Just like that, we have a flow that enables agents to learn in real-time with each successive task!

Here’s a head-to-head (Operator versus Claude 3.5 Sonnet + Osmosis):

<https://www.youtube.com/watch?v=uhFuT8VD9tk>

**Osmosis was 3X faster and 6X more efficient in the number of steps taken!**

## Our Ask

If you (or anyone you know) are building AI agents and struggling with accuracy, speed, or cost, we’d love to chat and see how we can help! Please reach out at [kasey@gulp.ai](mailto:kasey@gulp.ai), or book some time directly [here](https://calendly.com/kasey-gulp/).

## The Team

We’ve (Kasey and Andy) known each other for over a decade!

[Kasey](https://www.linkedin.com/in/kasey-zhang/) (CEO) previously co-founded and ran a gaming startup for two years before it was acquired. From there, he worked at various VC firms focusing on AI and data investments before deciding to jump back into building.

[Andy](https://www.linkedin.com/in/baiqingl/) (CTO) previously worked at TikTok, where he joined as an early member of the data infrastructure team and eventually became a tech lead, running data infrastructure for recommendations across the core TikTok app, Shop, Live, and more.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87475&key=user_uploads/695591/d662049a-cf42-4d21-bc5f-08643fd3be5e)
