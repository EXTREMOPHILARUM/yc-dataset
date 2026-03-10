# Launches

## Hegel AI: Open source tools for language model evaluation

**TL;DR** [Hegel AI](https://hegel-ai.com/) is building developer tools for LLM and prompt evaluation and continuous testing, with over a thousand downloads per week since launch. We’re a team of ex-PyTorch engineers from Meta and Google.

# The Problem

_Is Llama 2 really better? Is GPT-4 getting worse?_ Developers building with language models are constantly facing challenges with (1) model drift (2) new models and (3) insufficient evaluation systems. Besides academic metrics and “eyeballing it”, there’s no existing solution for continuous LLM regression testing or experimentation.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73501&key=user_uploads/1324508/f9481110-9296-4fb1-b5ab-68ce35d6bdfc)

What’s more, the complexity of LLMs and related tools like vector databases make it hard for developers to set up honest apples-to-apples comparisons for their use case.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73501&key=user_uploads/1324508/e7dc639a-27c3-4849-8245-9bda29648954)

# Our Mission

We want to make high quality evaluation and testing systems available to everyone, which is why we’re building an open source platform for language model evaluation. Developers can use our product to [monitor GPT-4 regressions](https://github.com/hegelai/prompttools/blob/main/examples/notebooks/GPT4RegressionTesting.ipynb), audit models for safety, and [measure performance of vector databases](https://github.com/hegelai/prompttools/blob/main/examples/notebooks/ChromaDBExperiment.ipynb). 

# How it works

Developers come to our product with some test cases, and an idea of the models or vector databases they want to evaluate. We handle all of the testing infrastructure to help them (1) set up experiments across models/DBs in notebooks and (2) scale those experiments into reusable test suites. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73501&key=user_uploads/1324508/da633110-74ba-449b-b4f1-017ad8ec6ffd)

\
We support multiple strategies for evaluation: auto-eval by another model, systematic evaluations like structured output validation or semantic similarity to an expected output, or even through gathering human feedback with our notebook UI.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73501&key=user_uploads/1324508/13b7aa5e-e9d8-43de-b191-6d5c5fc1f04a)

# The Team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73501&key=user_uploads/1324508/6dbe38e4-9070-464e-b06b-55ac3d21be7f)

[Kevin Tse](https://www.linkedin.com/in/kevin-tse-35051367/) and [Steven Krawczyk](https://www.linkedin.com/in/steventkrawczyk/) met 9 years ago when we started our undergraduate studies at the University of Chicago. We crossed paths again years after graduation when we were both working on [PyTorch](https://github.com/pytorch/pytorch), an open-source deep learning library, at Meta and Google. We worked on the core library, data loading, and the XLA compiler library. Prior to that, we worked at Amazon and Bridgewater Associates.

# Testimonials

_It’s hard to convince senior management that investing in LLMs is worth it, without doing expensive experimentation on my own._

* _Soma Szabo, Data Science Manager at McMaster-Carr_

_If you are doing anything remotely related to prompting, you'd know how frustrating & inefficient it is to compare between prompts. I, for one, am using it to make my life easier in building Watto AI._

* _Rishabh Panwar, Co-Founder & CEO, Watto AI_

# Asks

* Install the [Python library](https://pypi.org/project/prompttools/) and try it yourself!
* Give us a star on [GitHub](https://github.com/hegelai/prompttools) and [join our Discord community](https://discord.gg/72a9xh5Z7P).
* [Contact us](mailto:team@hegel-ai.com) if you want enterprise support for experimentation or early access to our hosted UI and observability tools
