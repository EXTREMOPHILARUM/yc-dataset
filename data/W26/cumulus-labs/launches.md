# Launches

## Cumulus Labs ☁️ | Supercharge Your Training & Inference

## **TL;DR**

Cumulus is a performant GPU cloud that preemptively optimizes your training and inference workloads across our global supply of multi-tenant clusters. The result: we **save you 50-70%** through charging by physical resources used, provide faster inference with ultra-low cold starts, and ensure zero time spent debugging infrastructure.

**Ask**: If you’re training models or serving inference workloads, frustrated with GPU costs and performance, let us optimize your **LLMs, LoRAs, vision models, and more.**

**Website:** <https://cumuluslabs.io>\
**Docs:** <https://docs.cumuluslabs.io>

Launch Video: <https://www.youtube.com/watch?v=duQwV50GKXc>

## **The Problem**

AI teams are bleeding money and time on GPU infrastructure:

* **Massive waste**: Teams pay for idle GPUs sitting at 30-40% utilization because scaling is unpredictable
* **Infrastructure hell**: Engineers spend weeks configuring Kubernetes, debugging OOM errors, and managing failovers instead of building models
* **Cold start latency**: Inference workloads take 10-30+ seconds to spin up, killing user experience
* **Vendor lock-in**: Once you commit to a cloud provider, switching costs make it nearly impossible to optimize for price or performance
* **Skyrocketing costs**: Companies burn through runway 2-3x faster than planned because GPU bills spiral out of control

Every hour debugging infrastructure is an hour not spent improving your models. Every dollar wasted on idle GPUs is a dollar not spent on growth.

---

## **The Solution**

**Cumulus is a GPU optimization layer that makes compute cheap, fast, and invisible.**

We aggregate compute from everywhere—big cloud providers, trusted data centers, individual hosts—into a single unified pool. Then we do three things no one else does:

# **1. Predictive Packing & Live Migration (Training/Fine-tuning)**

Your training jobs are intelligently packed alongside other workloads to maximize GPU utilization. As your job runs, we predict resource usage and **live-migrate you to faster or cheaper clusters** without interruption. No more paying for an entire H100 when you only need 40% of it.

# **2. Execution State Capture & Global CDN (Inference)**

We capture your model's live execution state (VRAM, memory, loaded weights) and replicate it across our global compute CDN. When a request comes in, we serve from the closest cluster with **ultra fast cold starts**—no more waiting 30 seconds for a job to spin up. We have tested with **LLMs, vision models, LORAs, and many others.**

# **3. Intelligent Scheduling & Auto-Recovery**

Our scheduler constantly monitors your jobs, diagnoses failures, and auto-recovers without manual intervention. The Cumulus prediction system learns your usage patterns over time and pre-allocates resources before you need them.

**The bottom line:** _You write 20 lines of config. We handle everything else._

Our Demo: <https://www.youtube.com/watch?v=J0KRFWE3-fg>

## **The Team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96856&key=user_uploads/3177002/fbef3bec-137d-4275-8433-8a1ccfad47a5)

(winning the science fair in 4th grade for a robot that solved Rubik’s cubes)

**Veer Shah** (Founder)\
Led a Space Force program and worked on ML workloads at an aerospace startup supporting NASA missions, where infrastructure needed to be both performant and secure. 

**Suryaa Rajinikanth** (Founder)\
Built custom GPU compute solutions at TensorDock, then moved to Palantir where he built critical infrastructure for the US Government. Deep expertise in distributed systems and resource optimization.

We met as third graders and have been building together our whole lives. We've seen the GPU infrastructure problem from both sides: Suryaa from the provider side at TensorDock, Veer from the customer side running mission-critical ML workloads. We started Cumulus Labs because we knew exactly what the industry needed—and no one was building it.

## **What We're Looking For**

**If you're training models or serving inference workloads**, frustrated with vendor lock-in, or simply paying too much for your GPUs, reach out.

**Know AI/ML teams experience any of these issues?** Connect them with us.

We optimize LLMs, LoRAs, vision models, and more.

We'd love your feedback on which features matter most.

---

## **Get In Touch**

Join the waitlist: <https://cumuluslabs.io>\
Contact us: [founders@cumuluslabs.io](mailto:founders@cumuluslabs.io)\
Book a demo: [Here](https://calendar.app.google/NepPaCiZxCTM9vyUA)

---

---

---

---

---

---

---

---

---

Huge thanks to partners, our batch-mates, and everyone who's helped so far.

Let's make AI infrastructure invisible.

— Veer, Suryaa, and the Cumulus team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96856&key=user_uploads/3177002/3045bccb-ce6f-4d07-b8dd-37c34772ce14)
