# Launches

## 🤖 General Trajectory - A Foundation Model for Humanoid Robots

<https://youtu.be/iIdum8FrMIw>

## What is it?

A foundation model that helps humanoid robots pick up unseen objects and perform real-world work. It generalizes to novel objects and scenes, including cases where prior SoTA models achieve 0% success.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96524&key=user_uploads/1366241/6cbcabb4-44fe-4d86-8b20-4b5220709f58)

## The problem

Humanoid robots can do backflips and kung fu, but still struggle with economically useful work. Dexterous manipulation is the main bottleneck to useful physical labor.

## Our approach

We collect an efficient set of human demonstrations and train a reward model to improve the base model's grasps.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96524&key=user_uploads/1366241/86269800-22b9-4a15-bf3c-7d63285ea25d)

The result is strong generalization: up to 63% gains on difficult objects where the best baselines achieve 0%, while maintaining near-perfect performance on standard objects. Full details are available in our [technical post](https://www.generaltrajectory.com/technical-update).

The physical world is 80% of global GDP. We believe this research represents progress toward a future in which AI systems are not limited to computer work.

## Open-source

We open-sourced our teleop stack!

<https://github.com/GeneralTrajectory/dex-teleop>

It uses vision + wrist trackers instead of data gloves → about **$500** in hardware vs. **\~$5,000**.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96524&key=user_uploads/1366241/aeeb02d9-821a-44b5-bef0-f491af1fa15a)

## Call to action

If you are interested in AI for the physical world (scientific R&D, defense, etc.), please reach out!

* Website: <https://generaltrajectory.com>
* X: <https://twitter.com/gentrajectory>

## General Trajectory – Reasoning Models for Robotics

# **TL;DR**

We’re training models that can reason through physical tasks using chain-of-thought to automate traditionally difficult work in industrial environments like warehouses and manufacturing facilities.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88311&key=user_uploads/1366241/ed2288b5-baa9-4959-896d-cd75e4074858)

# How it works

We fine-tune vision-language models to output low-level robotic controls across primary tasks in logistics: mixed-sku palletization, item picking, sorting, and packing.

Before predicting the next action, our model is explicitly trained to `<think></think>` about its next step. This allows it to reason through long-horizon tasks.

<https://youtu.be/axgbhBkkuQQ>

# RL from Verifiable Rewards

Our fine-tuned model is then rolled out in Nvidia’s Isaac Sim where it generates reasoning + action traces that get scored using simple verifiers. This continues to improve the model using photorealistic data without any human in the loop.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88311&key=user_uploads/1366241/db7af549-6c06-433d-a8da-16d6dffd5737)

# Our ask

We see logistics as an entry point to even greater automation across industries. Soon you will be able to tell AI to do any physical tasks in the same way current systems can handle the cognitive ones.

If you have any tasks you’d like to automate or know of anyone interested in working on embodied AI, please reach out: [joshua@generaltrajectory.com](mailto:joshua@generaltrajectory.com)

# The Team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88311&key=user_uploads/1366241/ed970f7d-fd66-473d-9c72-17cc18dedb5d)

Joshua studied CS & neuroscience at the University of Chicago but spent most of his time outside of class doing ML research. He first joined NASA Ames Research Center and later worked at Caltech. His [research](https://scholar.google.com/citations?user=RoD9hE8AAAAJ&hl=en) focused on generally capable AI agents and reasoning.
