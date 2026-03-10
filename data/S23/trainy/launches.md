# Launches

## 🪐 Pluto – OSS experiment tracker for Neptune users

[**→ Try the live playground**](https://demo.pluto.trainy.ai/o/dev-org/projects/my-ml-project) – explore Pluto with real sample experiments, no signup required.

NeptuneAI is shutting down on March 5th after being acquired by OpenAI. We built Pluto so you can migrate safely without rushing.

---

### **👋 Who we are**

Hey YC, we're Roanak and Andrew! We founded Trainy to help AI teams efficiently manage and utilize GPU infrastructure. When we heard Neptune was shutting down, our customers started panicking about losing years of experiment history and having to rewrite their logging code on a tight deadline.

So we built Pluto.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97424&key=user_uploads/509361/6cbcdb3e-6f5f-4f7f-8855-58001d921c66)

### **🔥 The problem**

Neptune's March 5th shutdown is forcing research teams into one of the worst kinds of migrations: rushed, high-stakes, and hard to verify.

Most alternatives require you to:

* Rewrite your logging code
* Lose your historical runs (or spend days exporting and reformatting)
* Hope the new tool handles your multi-GPU workloads the same way

And you have to do all of this before March 5th or your data gets deleted.

### **🛠 How Pluto solves it**

**1. Dual-log to both platforms simultaneously**

[Add one import](https://docs.trainy.ai/pluto/neptune-migration), keep your existing Neptune code running, and Pluto logs side-by-side. Validate that everything matches on your real training workloads before you cut over.

**2. Export your Neptune history**

Pluto includes [a Neptune exporter](https://docs.neptune.ai/transition_hub/migration/to_pluto) that brings your old runs into Pluto. Years of experiment data, preserved.

**3. Built for the workloads Neptune users actually run**

We're optimizing for what Neptune users loved: UI responsiveness at scale, reliable logging throughput under multi-node/multi-GPU workloads, and the ability to track thousands of per-layer metrics without lag.

**Deployment options:**

* **Self-hosted** – for sensitive data or air-gapped environments, instructions in [server readme](https://github.com/Trainy-ai/pluto-server)
* **Hosted** – $250/seat/month (free for existing Trainy customers)

---

### **🙏 Our ask**

**If you're a Neptune user, please try Pluto with dual-logging before the March shutdown.**

We're specifically looking for feedback on:

* Anything that would block your cutover
* Features you rely on that we're missing
* UI/performance differences at scale

**Early Bird offer:** Start dual-logging in the next 2 weeks → **3 months hosted free**.

👉 Once you’ve made an account on [pluto.trainy.ai](http://pluto.trainy.ai), email [roanak@trainy.ai](mailto:roanak@trainy.ai) or [grab a time to chat](https://calendly.com/roanak/trainy-demo) and we’ll add seats/storage.

---

### **🔗 Links**

* [**Playground**](https://demo.pluto.trainy.ai/o/dev-org/projects/my-ml-project) – try it now
* [**Quickstart**](https://docs.trainy.ai/pluto/quickstart) – get running in 5 minutes
* [**GitHub**](https://github.com/Trainy-ai/pluto) – Apache-2.0 (client), AGPL-3.0 ([server](https://github.com/Trainy-ai/pluto-server)) ⭐

We're listed on[ **Neptune's official transition hub**](https://docs.neptune.ai/transition_hub/migration/to_pluto).

Thank you!

## 🚅 Trainy - Identify bottlenecks, boost training

**tl;dr** We help ML engineers training large models isolate performance bottlenecks during training. Trainy summarizes profiling information during large distributed training so that you know exactly what is limiting the speed of your model training.

Hello everyone, we are Andrew and Roanak, ML engineers from the bay. We’ve experienced firsthand the challenges of distributed training and getting the most out of your compute resources. That’s why we are building tools to help ML engineers training large models optimize training speed and take the guesswork out of estimating the time and cost of training.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72587&key=user_uploads/1404133/cde44cc9-7436-422f-b0fd-c7c3f2a94ff2)

# **The Problem**

Distributed training has enabled the training of ever-growing generative AI models. However, gains in speed are not simply proportional to the number of GPUs recruited and can quickly have diminishing returns depending on infrastructure and the model being trained. Tools now mainly focus on profiling a few GPUs, but become unwieldy the moment you scale beyond the 10 GPU mark.

# **Our Solution**

We created a dashboard to display timing information across many GPUs. It’s a graph interface built on top of Tensorboard and PyTorch Profiler, existing tools familiar to ML engineers.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72587&key=user_uploads/1404133/729377af-3ca9-499b-acf7-1e2f1f569940)

# **How it works**

We summarize profiling information over many GPUs in a few key views that help ML developers identify where in the ensemble of GPUs there are inefficiencies. Statistics about computation, communication, and memory operations across many GPUs isolate straggling GPUs. Distributed training can only proceed as fast as the slowest GPU participating. By isolating slow outliers, an ML developer can zoom in on the operations running on the straggling GPU and make optimizations to their code to balance timings across GPUs and lower resource idling.

# **The Ask**

We’d love for you to try out our profiler if you are training your own models. <https://github.com/Trainy-ai/nodify>

Also join our community if you want to stay up to date with the development of our tools. <https://discord.com/invite/d67CMuKY5V>
