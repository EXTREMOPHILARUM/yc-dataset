# Launches

## TensorPool: the easiest way to use GPUs 🌊

Hi Everyone! We’re [Joshua](https://bookface.ycombinator.com/user/969804), [Hlumelo](https://bookface.ycombinator.com/user/1709047), and [Tycho](https://bookface.ycombinator.com/user/2359695) - cofounders of TensorPool!👋

**TLDR;** Our CLI makes ML model training effortless - just describe your job, and we handle GPU orchestration and execution at half the cost of major cloud providers.

[Get setup in 3 minutes](https://github.com/tensorpool/tensorpool)

Here’s a quick demo of how easy it is to train ML models with TensorPool!

[**TensorPool Demo -- Fine-Tuning DeepSeek**](https://youtu.be/RqqLIVzP780)

# **Problem**

Since high school, when we trained our first ML models, **accessing remote compute has always been a massive hurdle**. As the years went by and we moved further into academia/industry, a good solution never came. Whether it was AWS EC2’s absurd amount of configuration, or Google Colab’s inability to run jobs without your computer being on, nothing left us satisfied. We talked to our co-workers and friends and they all felt the same. We wanted using GPUs to be as easy as programming locally.

# **Solution**

We got together and built a way to **access industry-scale compute from your IDE**. No more SSHing. No more massive data migrations. No more ML Ops headache. Just a simple CLI. \[We also **cut your costs by 50%** which will be explained below :)\]

# **How It Works**

TensorPool has 2 main advantages:

1. **Ease of Use:** 
   * **Don’t leave your IDE:** TensorPool deploys your code directly to GPUs and ships the results back, just as if you were developing locally. 
   * **Intuitive CLI & Configuration:** With TensorPool you can run your job with a single command, kick off several experiments with different tp.config.toml configurations, and version control training jobs with your code.
2. **Price Advantage**
   * **Multi-cloud integration:** We’ve developed technology to do a real time analysis of all available GPU cloud providers, and put your job on the cheapest one.
   * **Spot node resummation tech:** We’ve created a way to give users the price advantage of spot nodes with the reliability of on-demand instances. This leads to \~50% savings!

# **Our ask**

We’re currently giving away $5/week of **free compute** to early users, and would love for you all to **try us out**! Whether your start-up needs an ML infra upgrade or you love messing around with models in your free time – reach out to us we’d love to chat ([team@tensorpool.dev](mailto:team@tensorpool.dev))! You can find all the information to get started [on our GitHub](http://github.com/tensorpool/tensorpool) (**drop us a star while you’re there** 😊) or [our website](https://tensorpool.dev).

**We would also love intros to enterprises** that you believe could benefit from cheaper / easier access to GPUs.

# **Try TensorPool today!**

Below is a quick start:

After completing [the prerequisites](https://github.com/tensorpool/tensorpool?tab=readme-ov-file#prerequisites), we create a “tp.config.toml” ([explained here](https://github.com/tensorpool/tensorpool?tab=readme-ov-file#configuration)), either manually with: 

```
tp config new
```

Or auto-generate one with natural language: 

```
tp config <describe your task>
```

To then deploy and run your job – simply run:

```
tp run
```

and that’s it! Your model is training on cloud GPUs! 

# **About Us**

Joshua, Tycho, and Hlumelo all met their freshman year at Stanford where they got placed on the same dorm floor. Since then, they’ve taken all their classes together and have worked at companies like Apple, Blackstone, DeepMind, Nextdoor, CZI, and PIMCO.
