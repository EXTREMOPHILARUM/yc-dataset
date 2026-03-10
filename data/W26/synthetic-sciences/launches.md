# Launches

## Synthetic Sciences – AI Co-Scientists for End-to-End Scientific Research

Hi! We’re Aayam and Ishaan, co-founders of [Synthetic Sciences](https://syntheticsciences.ai/).

# **TL;DR**

Synthetic Sciences is a platform where scientists delegate complex research tasks to AI co-scientists that handle the full research loop: **literature → hypotheses → experiments → results → paper drafts**.

Over the last year, AI has been showing some traction in math research. Math gets the coverage because it’s easy to measure. But there is a non-trivial unlock to be made in accelerating the rest of science – ML research, computational biology, proteomics - where the tooling hasn't caught up yet.

**Launch Video:** <https://www.youtube.com/watch?v=uHOmeCnV1HU>

# **The Problem**

Scientific research is a marathon of iterations. Read hundreds of papers. Form hypotheses. Design and run experiments. Wait. Analyze. Write. Revise. Submit. Each cycle compounds.

The existing tooling doesn't help. AI “literature review” tools surface papers but don't carry context forward into your code or experiments. Jupyter, W&B & others track runs but are siloed from your literature and writing. Writing happens in isolation, even though it could be steering decisions earlier.

Research is a long chain of context-dependent steps, and our tools treat each one like it’s isolated. Every iteration forces you to rebuild state: what you read, what you tried, why you chose this method, what failed, what changed.

A single research question becomes months of fragmented work scattered across tools, tabs, and time zones. And it's all on you. Every step requires your attention, your context, your time.

You can't parallelize yourself. If we could accelerate scientific research the way we’ve accelerated software engineering in the last 24 months we are guaranteed to see science breakthroughs that will massively benefit humanity.

# **Our Solution**

Point synsci at a research question, a repo, or a dataset. Our AI co-scientists autonomously:

* Search + synthesize literature grounded in your project
* Generate high-quality hypotheses + idea trees tied to prior work
* Design experiment plans + GPU job specs
* Write and run code (Python, R, ML pipelines) in containerized environments
* Launch and monitor experiments on serverless GPUs & GPU clusters
* Output publication-ready drafts: LaTeX, figures, slides

We’ve mostly tested synsci on ML research so far, but we’re rapidly expanding across domains. It’s already strong in computational biology research: on BixBench Verified, our biology mode achieves state-of-the-art performance (92%).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98217&key=user_uploads/1441373/0d71bacf-1ac6-4ee5-973e-42a543973d04)

# **Flywheel Mode: Own Your Models**

If you have users, you already have the rarest ingredient in AI: proprietary signal. Every correction, accept/reject, trace, and outcome becomes training data. Everyone has access to the same models and can buy the same tokens. Nobody else can buy your users, your logs, and your feedback loops. 

Strong open-weight models now make it possible to beat frontier performance on your specific tasks through post-training (SFT + RL). However, the problem is everything around the model: data plumbing, evals, deployment, and compute. That friction keeps most teams renting intelligence by the token instead of owning it.

Flywheel Mode makes the loop painless. We handle the glue code and ship the workflow end-to-end across 20+ compute providers and hundreds of built-in skills. Use your AI co-scientists to run the full loop: train, evaluate, deploy, iterate.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98217&key=user_uploads/1441373/ea6a1549-dd1f-40e3-bd36-ae627be085b0)

# **Our Story**

We met doing ML research at NUS, CMU and MIT CSAIL & published together at NeurIPS, ICML, and AAAI workshops. Ishaan came from competitive programming (top-ranked in India for IOAI Team Selection, USACO Platinum). Aayam previously built, patented & sold an AI orthopaedic sock and built COVID-19 infra serving 50k+ users daily. 

# **Our Ask**

* **Try it:**[ ](https://app.syntheticsciences.ai)[syntheticsciences.ai](http://syntheticsciences.ai) - $5 in free credits when you sign up!
* **If you’re a CTO / Head of R&D / research lead** and want to accelerate R&D with AI co-scientists, we’d love to talk.
* **RL environments for scientific research:** We're building LHRL environments to post-train models on ML research workflows. If you're an AI lab interested in process-oriented data, let's talk.
