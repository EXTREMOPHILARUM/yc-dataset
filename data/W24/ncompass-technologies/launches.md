# Launches

## nCompass - Optimize performance on GPUs, 10x faster

Hey everyone,

**tldr;**

I’m Aditya, co-founder of [nCompass Technologies](https://ncompass.tech). We’re building a developer tool that unifies profiling, trace collaboration and trace analysis of AI systems. We automate performance optimization of AI systems across all levels of the infrastructure stack.

Using this tool, we implemented a Hopper GEMM kernel that outperformed NVIDIA's CUTLASS GEMMs by 3%, within a day - this took us months before.

Checkout our product demo below. It’s free to use and you can get started today in **VS Code, Cursor or Claude Code** - [Quick Start](https://docs.ncompass.tech/quick-start)

<https://www.youtube.com/watch?v=Q3Pq-BPU2Ec>

**THE PROBLEM**

Identifying the root cause of performance bottlenecks is 4-8x slower than writing the code to fix them.

If you are optimizing a system like vLLM, you have to:

* Run a profile and then copy a giant trace file to your local machine just to view it.
* Spend hours identifying opportunities for performance improvement.
* If this involves writing a kernel, you profile the kernel, spend hours or days digging through ncu traces that are massive data dumps.
* Then you identify your bottlenecks and formulate a plan.

Running this loop till you have a performant system can take weeks, even months.

**OUR SOLUTION**

By building an AI agent that can analyze profiling data as well as interact with a bank of deep technical knowledge and expertise, we’re automating the process of identifying performance bottlenecks.

Now in a single VSCode interface, you can:

* Open and view trace files
* Use our novel tools like trace diffs to analyze them
* Generate share links to easily share traces with team members
* Feed source + profiling data to our AI agent and get back actionable analysis on how you can optimize the performance of your system.

This applies to both systems and GPU kernel level analysis and our agent integrates directly into Cursor / Claude Code, so you never have to leave your normal workflow!

**Anyone** can now write both correct and performant code with AI!

**ASKS**

**Install our VSCode extension** and start optimizing your systems performance!

* [Quick Start](https://docs.ncompass.tech/quick-start)
* [Detailed Docs](https://docs.ncompass.tech)

**We also offer FDE services** - if you would like us to step in and analyze your system’s performance and provide you with an analysis of how much we could improve it by - reach out at [hello@ncompass.tech](https://mailto:hello@ncompass.tech)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98338&key=user_uploads/1641909/fc628a90-5565-43db-8aff-7c61e476e976)

## nCompass Technologies: Reliable LLM API with no rate-limits

# **Tl;dr:**

We’ve built an AI model inferencing system that can serve requests at scale like no other and now we’re releasing it to the public as a **rate-limit-free API**. We serve any open-source LLM and can also deploy optimized versions of your custom fine-tuned LLM with cost-effective autoscaling. [Sign up here](https://console.ncompass.tech/login), create an API key, get $100 of credit on us, and run as many requests as you like!

# **The Problem**

Deploying AI models in production requires expensive infrastructure. Serving more than \~10req/s using open source inference engines like vLLM on a single GPU results in terrible quality of service. Time-to-first-token skyrockets to more than 10s, and end-to-end latency degrades even more!

**The common solution**: horizontally scale up GPUs.

**The problem**: GPU’s are expensive and hard to find.

# **Why should you care**

1. **API user:** These high infrastructure costs are the reason you suffer rate limits when using existing API providers.
2. **Deploying on-prem:** Your infrastructure costs might be the reason a PoC doesn’t move to production.

# **Our Solution**

We’ve built an AI inference serving system that can sustain 100s of requests per second while maintaining a time-to-first-token of <1s on \~30% fewer GPUs when compared to NVIDIA’s NIMs containers and up to **2x fewer GPUs** when compared to vLLM.

This enables us to provide a rate-limit-free API while maintaining a high quality of service. Alternatively, we can provide this as a cost-effective on-prem deployment solution, ensuring your infrastructure costs don’t blow up with requests served. We support any open source model and can host your custom fine-tuned model as an API with autoscaling enabled as well.

# **Tutorials**

* [**Sign Up**](https://www.loom.com/share/bac5c44a8e694b5783f3ba7c777ce40a?sid=6226613a-2cd6-45e6-bfc3-ac0381198b2a)
* [**Models and Pricing**](https://www.loom.com/share/f7dc12aefe304399a3975feef7e38938?sid=34c2a174-4050-40bc-b65a-844d3002e48c)
* [**Run Inference**](https://www.loom.com/share/0933dc3fa2ba442fa789286ef75e09b8?sid=74266aa3-f24e-46d7-bcce-1f3c61d7d82e)

# **Shout out**

To be able to build such a scalable and available system, we needed a top-quality hardware provider. We wanted to use this as an opportunity to shout out [Ori Global Cloud](https://www.ori.co/), a key partner in this journey, to enable a serverless Kubernetes platform for AI inference at scale. [Ori Serverless Kubernetes](https://www.ori.co/serverless-kubernetes) is an infrastructure service that combines powerful scalability, simple management, and affordability to help AI-focused startups realize their wildest AI ambitions. [Reach out to Ori](https://www.ori.co/gpu-request) for exclusive GPU cloud deals!

# **Asks**

* Use our self-serve console (<https://console.ncompass.tech/login>) to create an account and start running with $100 of credit.
* Book a demo (<https://calendar.app.google/3jRDwcstFQvsbqnR8>) if you would like to discuss an on-prem solution. YC deals apply!

Our pricing is transparent and can be found here: <https://console.ncompass.tech/public-pricing>

## nCompass Technologies: Realtime audio denoising

**tl;dr** nCompass has released the world’s first **Realtime Audio Denoising API** that can remove background voices from your audio stream in real time. Try it out for free on our website [here](https://www.ncompass.tech/about).

Today, the world is increasingly interacting with AI models using voice. Apps and tools that rely on voice input need to be able to successfully separate background voices from the main speaker’s voice. However, this is not the case with existing voice AI products such as Deepgram’s speech-to-text (STT) converter.

Check out this demo below that shows how using nCompass’s denoiser can enable transcription tools (such as Deepgram’s STT) to be used in previously unusable scenarios.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81420&key=user_uploads/1641909/61bc7f02-4a23-4ab2-b7fc-cd2a8ad3b01e)

We have two versions of this denoiser that you can try out for free on our [website](https://www.ncompass.tech/about).

1. [Offline denoising + transcription](https://www.ncompass.tech/cleaner_transcription/interactive_demo) mode, which generates cleaner transcriptions when paired with any speech-to-text provider.
2. [Realtime audio denoising,](https://www.ncompass.tech/realtime_denoising/interactive_demo) which can take in an audio stream and remove background voices in real time. You can now get the sound quality of a private booth, regardless of where you are!

## nCompass Technologies - Low-latency deployment of AI models made easy

**tl;dr** If unpredictable response times and rate limits of OpenAI are causing your tool’s user experience to suffer, [nCompass](https://ncompass.tech/) allows you to effortlessly tap into the world of open-source AI models while ensuring that the served models meet your target budget and performance requirements.

—

Hey all, we are [Diederik](https://linkedin.com/in/diederik-vink) and [Aditya](https://linkedin.com/in/adityarajagopal), the co-founders of [nCompass](https://ncompass.tech/), a platform for simplified hosting and acceleration of open-source and custom LLMs.

### **The Problem**

LLM-based products that use closed-source model providers like OpenAI suffer from slow response times and rate limits. 

Open-source models are a great alternative, but hosting a model yourself is a lot of extra work and maintenance which distracts you from your core business.

### **Our solution**

nCompass provides an API that allows you to integrate accelerated versions of any open-source or custom model of your choice into your AI pipeline. We support OpenAI style chat templates, work with all web frameworks, and have a time-based pricing model that results in a predictable compute cost for users.

### **How it works**

We serve models to users with a simple 3-step process:

1. Select your desired open-source / custom model
2. Provide your performance requirements
3. Set a budget you are not willing to exceed

We set up the deployment that meets these requirements and provide you with a single API Key that you can then use to integrate the model with a single line of code.

We support any model currently hosted on Hugging Face, with some highlights being: 

* **Mistral-7B :** 160ms Time-To-First-Token @ 86 tok/s
* **Mixtral-8x7B :** 300ms Time-To-First-Token @ 64 tok/s

### **Demo**

<https://www.youtube.com/watch?v=sdHVji8QGOg> 

Also, check out our [GitHub](https://github.com/nCompass-tech/nCompass) repository for code examples.

### **The team**

Since we met in undergrad (9 years ago) through to our PhDs at Imperial College London, we’ve worked on every project together. Our PhDs focused on hardware acceleration of large-scale machine learning models covering all levels of the stack from algorithms and compilers down to digital hardware design.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79124&key=user_uploads/1641909/8f0f2b1e-8c86-4269-828e-a90176159dd6)

### **Asks**

* Book a [demo](https://calendar.app.google/eLCRjByYErh9X2hh9) 
* **Warm intros** to anyone you know who requires accelerated and/or hosted versions of open-source models.

Our emails are [aditya.rajagopal@ncompass.tech](mailto:aditya.rajagopal@ncompass.tech) and [diederik.vink@ncompass.tech](mailto:diederik.vink@ncompass.tech)
