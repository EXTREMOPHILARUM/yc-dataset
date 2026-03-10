# Launches

## SF Tensor - Infrastructure for the Era of  Large-Scale AI Training ⚡

Hey everyone 👋 

We’re [Ben](https://www.linkedin.com/in/benkoska/), [Tom](https://www.linkedin.com/in/tomkoska/) and [Luk](https://www.linkedin.com/in/lukkoska/) - co-founders of SF Tensor. 

**TL;DR:** We let AI researchers forget about the infrastructure layer and focus on their research. 

We automatically optimize kernels to run faster, find the cheapest GPUs across every provider and migrate your jobs when spot instances fail. Training AI should be about AI, not DevOps. 

**_Ask:_** Know anyone training or fine-tuning AI models? We’d be grateful for an intro! Reach out to us at [founders@sf-tensor.com](mailto:founders@sf-tensor.com). 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95098&key=user_uploads/801244/994bfb29-1b66-4506-86bd-8b3d0197eff4)

## **The Problem**

Training AI should mean developing smarter architectures and finding better data. But right now, it doesn’t. Teams waste their time on everything but actual research: 

* Optimizing code so that training runs don’t drain the bank 
* Fighting cloud providers and scrambling for GPU availability 
* Making distributed training work with reasonable MFU (=cost efficiency).

This drives up costs, frustrates everyone and kills velocity. Infrastructure has inadvertently turned into the limiting factor for AI research labs, and it’s killing progress.

We experienced this first-hand developing our own foundation models – what we expected to be AI research, experimentation and iterative improvement turned out to be an ugly mix of writing CUDA, debugging driver mismatches and optimizing inter-GPU collective operations. That’s why we decided to solve the infrastructure layer, to allow other researchers to **focus on research, not infrastructure**.

## **Our Solution**

SF Tensor is the "set it and forget it" infrastructure layer for anyone training or fine-tuning AI models. Hook up your repo, pick your GPU count and budget, and we deal with the rest:

* Our automatic kernel optimizer analyzes your architecture and tunes execution for any hardware (NVIDIA, AMD or TPUs). No more having to drop down into custom CUDA because PyTorch doesn’t understand memory topology. 
* We find the cheapest available compute across all clouds for your specific requirements and launch your training run. 
* Automatic Distributed Training allows you to scale from 1 to 10,000 GPUs without having to change your code or killing your MFU 
* Everything else that you shouldn’t have to think about: Spot instance migration? Handled. Monitoring? Baked in. Logs and artifacts? Done.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95098&key=user_uploads/801244/89170605-19e4-4029-87dd-7a3fa85cc9df)

## **The Team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95098&key=user_uploads/801244/519e2798-579a-43e1-8c96-28f3be87a392)

We’re 3 brothers that have been working on Artificial Intelligence together for years, most recently training our own Foundational World Models. SF Tensor was born out of our own needs as AI researchers scaling up training runs to thousands of concurrent GPUs.

Ben has been publishing AI research since high school, solo-training models across 4,000 GPUs as co-PI on a 6-figure grant.

Tom and Luk (twins btw) have been doing AI research for years, from starting college in parallel to high school at age 14 to finishing their BSc in CS (at age 16).

## **Compute should be boring. Let’s make it boring.**

Try us right now at [sf-tensor.com](http://sf-tensor.com) or contact us at [hello@sf-tensor.com](mailto:hello@sf-tensor.com) to see how we can help with your infra pains.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95098&key=user_uploads/801244/3ca5b95d-168d-402c-a899-5a42965ee527)
