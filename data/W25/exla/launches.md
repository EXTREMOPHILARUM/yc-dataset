# Launches

## Exla – Run datacenter models on edge devices

Hey YC! We’re Viraat and Pranav – cofounders of Exla.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88090&key=user_uploads/2212412/6f2a4f23-207a-4ba8-84dd-1be1039c46f7)

# **TL;DR**

The Exla SDK optimizes models for edge devices (e.g. NVIDIA Jetsons), **cutting memory usage by up to 80%, with 3-20x faster inference**. We’re focusing on optimizing and deploying **LLMs, VLMs, VLAs, and other CV models** on the edge.\
[Here’s Viraat showcasing our SDK](https://www.loom.com/share/d8fbb4faef87493c9806610fff6ff86c?sid=10b54831-159b-4157-95b7-8b9f7a5c8d8e)

# **‼️ The Problem**

**Frontier models are unlocking new applications on constrained edge devices** – Vision-Language Models in manufacturing defect detection, Vision-Language-Action Models to control robots via natural language, and LLMs to power in-car assistants are a few examples.

**But these** **models are now shy of a _trillion_ parameters**, and with the emergence of inference-time scaling, **they are more computationally demanding than ever**. This limits their adoption to edge devices with beefy GPUs and sufficiently large VRAM, and even then, a Jetson Orin Nano Super is completely saturated attempting to run a 13B model, leaving little room for other tasks.

# **🏎️ The Solution: The Exla SDK**

**We’re building mixed-precision low-bit quantization software** to dramatically cut the compute footprint of these models, leading to **80% less memory usage, 3-20x faster inference**, and reduced energy consumption.

**Today we’re starting with the Exla SDK** which applies our optimizations to a catalog of transformer-based and CV models, with growing support for your custom models. We’re primarily targeting deployment on NVIDIA Jetsons, followed by CPU-based platforms like Raspberry Pis and other embedded platforms.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88090&key=user_uploads/2212412/68c46641-ffb9-4dc9-a0a0-8facdba4e132)

Our roadmap includes building custom silicon that takes advantage of the quirks of low bit compute – which we expect to bring in another order of magnitude in compute savings. _We’re bringing frontier models everywhere._

# **🥷 The Team**

We met each other on the first day of college under questionable circumstances and have built several projects together since. Exla is the latest in that series!

[Viraat](https://www.linkedin.com/in/viraatdas/) graduated in 2.5 years and joined Amazon as machine learning engineer, where he worked on building personalized search and infrastructure to optimize models. In a previous life, he used to marathon around the world. Now he marathons at home, coding.

[Pranav](https://www.linkedin.com/in/pranavnair311/) previously worked at Apple as an OS engineer, hacking the iOS/macOS kernel to improve the sleep/wake experience for over a billion devices. In his non-existent free time, he tends to his 5 year old baby – an operating system he’s built from scratch.

# **🙏 Our Ask!**

Please reach out to [**founders@exla.ai**](mailto:founders@exla.ai) if you’re facing issues optimizing your models on Jetsons, other edge devices, or on-prem deployments! We’re happy to onboard you to our private beta.

We’re particularly looking to solve model optimization at companies working on robotics, manufacturing & industrial automation, and camera-based systems – your help would make a world of difference <3
