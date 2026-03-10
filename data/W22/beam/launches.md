# Launches

## Beam - Open Source Modal Alternative

**Hey all!**

**We’re [Eli](https://www.linkedin.com/in/mernit/) and [Luke](https://www.linkedin.com/in/luke-lombardi-2165968b/) – co-founders of [Beam](https://beam.cloud).** 

**TL;DR**

[Beam](https://beam.cloud) is an open source alternative to Modal for running AI apps. Coca Cola, Magellan AI, Shippabo, and Stratum use Beam for serverless inference, sandboxes, and background jobs. We're 100% open source and self-hostable.

https://www.youtube.com/watch?v=Itu_jCnyfJc

**The Problem**

If you're building an AI product, you need a fast serverless platform to run your code, whether that's GPU inference, background jobs, or sandboxes for agents. 

Existing cloud platforms either lock you in (Modal) or aren't optimized for serverless AI workloads (Lambda, SageMaker, Kubernetes). Various sandbox providers exist (e2b, Daytona) but don’t support a full range of AI compute workloads.

**Our Solution** 

Beam is your all-in-one serverless cloud for AI applications. You can run inference endpoints, background jobs, sandboxes, and more – all with a simple decorator in your Python or Typescript code. There’s no YAML and no configuration required. 

https://youtu.be/UxQ9O8pVVKk

This is possible thanks to a custom container runtime and distributed storage layer we built to run large container images with low cold start. We provide the security and isolation with gVisor, and build and launch new container images lightning fast.

Some of the features we support include:

* Fast image builds
* GPU support
* Memory/file system snapshotting
* GPU checkpoint restore (stop and resume sandboxes while preserving running processes)
* File system operations
* Run long sessions that last over 24h
* Open source and self-hostable

 **The Team**

Eli and Luke were college roommates and have been building products together pretty much since then.

Before starting Beam, Eli and Luke frequently attended hackathons and built a serverless framework to quickly ship web apps onto the cloud. When they started tinkering with AI, they realized that no serverless framework existed to make it easy to deploy AI models on the cloud. They decided to build it.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95756&key=user_uploads/313369/0bd4a323-556b-441a-ac00-7c61bf0c69c7)

**Our Ask**

* Try Beam here: [beam.cloud](http://beam.cloud)
* Star us on Github: https://github.com/beam-cloud/beta9

If this post resonated with you, we’d love to connect: [founders@beam.cloud](mailto:founders@beam.cloud)
