# Launches

## Lucid: Generative Simulations powered by Fast World Models

Hey YC! We’re **Alberto and Rami**, the founders of **Lucid**.

<https://youtu.be/fnoyvrGOwIA>

We’re building generative simulations powered by fast world models. Instead of using traditional game engines with hard-coded physics, our models **learn to simulate reality from pixels**, enabling **real-time interactive environments**. With it we will train robots in their own imaginations and make unbounded gaming experiences. We trained the fastest world model ever seen to simulate minecraft end-to-end (20+fps on a gaming GPU).

### **The Problem: Game Worlds Are Static & Expensive to Build**

Modern game development is **slow, expensive, and constrained**:

* **GTA V took 3 years, 1,000 employees, and $100M+** to build—AAA game budgets are skyrocketing and they’re not getting any better.
* Despite the price tag, these games are inherently **static**, with **predefined** environments, objects, and interactions.
* Players can’t truly shape the world—every door, street, and event is **pre-scripted**.

Meanwhile, **robotics** faces its own **bottleneck**—AI models trained in simulators (MuJoCo, Isaac Sim, Gazebo) **fail to generalize to the real world (Sim2Real gap)** because today’s simulations are **hand-coded approximations** of physics rather than learned from real-world data.

### **Our Solution: Generative World Models**

Lucid replaces **traditional game engines** with a **generative simulation engine** that **learns from data** rather than being manually programmed.

* **Every frame is generated in real-time**, conditioned on player actions.
* **Trained on video, not game scripts**—our models learn the rules of physics **directly from pixels** rather than hardcoded logic.
* **Infinite, dynamic game worlds**—players can generate and explore entirely new environments just from a text prompt or sample concept art.

### **A Neural Minecraft Simulator**

We trained a neural network to **simulate Minecraft end-to-end**—every pixel is generated in real-time, learned from **200 hours of gameplay.**

* **Runs at 20+ FPS on an NVIDIA 4090—5× faster than existing world models (Decart’s Oasis <4 FPS).**
* Aggressive latent compression—we utilize a VAE with 128x spatial compression allowing us to vastly reduce the amount of tokens needed to represent a single frame

### **What’s Next? Training on the Real World**

We’re now training our models on **real-world video data** to build a **general-purpose universe simulator** for:

* **Gaming:** The last game engine humanity ever needs—generating unique environments dynamically from simple text or multimodal prompts.
* **Robotics:** Simulations that actually **match reality**—training embodied AI models in diverse, realistic environments. A fully differentiable, learned simulation framework for reinforcement learning.

### **Want to learn more?**

* **Are you working on AI/robotics and need high-fidelity simulations?** We’re selecting early partners to **fine-tune** **LoRAs** on domain-specific data.
* **Want to explore the future of generative gaming?** Sign up for **early access to Lucid v2**

**Let’s connect!** Reach us at [**alberto@lucidsim.co**](mailto:alberto@lucidsim.co) or sign up at [lucidsim.co](http://lucidsim.co)
