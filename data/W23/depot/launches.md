# Launches

## ✨ Depot: Managed GitHub Actions runners for AWS

Hey, we’re Kyle and Jacob, the founders of [Depot](https://depot.dev), a hosted container build service for Docker images, and we’re excited to launch our new product: [managed GitHub Actions runners for AWS](https://depot.dev/products/github-actions)!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79909&key=user_uploads/956934/99034910-f435-44ef-8301-3610146d56bd)

## The Problem

While GitHub Actions is one of the most prevalent CI providers, Actions is slow for a few reasons:

* GitHub uses underpowered CPUs.
* Network throughput for cache and the internet at large is capped at 125 MB/s.
* Total cache storage is limited to 10GB per repo.
* Larger runners are expensive and take a long time to start running jobs.

## The Solution

**Depot-managed runners solve this!** Rather than your CI jobs running on GitHub’s slow compute, Depot routes those same jobs to powerful EC2 instances. And not only is this faster, it’s also 1/2 the cost of GitHub Actions!

We do this by launching a dedicated instance for each job, registering that instance as a self-hosted Actions runner in your GitHub organization, and then terminating the instance when the job is finished.

We've also integrated the runners with our existing distributed storage cluster that we use for Docker image builds for up to 10x faster cache throughput! 💪

## Demo Video

<https://www.youtube.com/watch?v=VX5Z-k1mGc8>

## Tech Details

Using AWS as our compute provider has a few advantages:

* We launch fast `m7a` instances, which are typically 30%+ more performant than alternatives.
* Each instance has high-throughput networking of up to 1.5 GB/s, hosted in `us-east-1`, so interacting with artifacts, cache, container registries, or the internet at large is quick.
* Each instance has a public IPv4 address, so you’re not sharing any rate limits with anyone else.

By integrating the runners with the distributed cache system (backed by S3 and Ceph) that we use for Docker build cache, jobs automatically save/restore cache from this cache system, with speeds of up to 1.5 GB/s, and without the default 10 GB per repo storage limit.

Additionally, the runners are located in the same VPC as our [Docker build service](https://depot.dev), so for anyone using both, built containers are now able to `--load` back into CI for testing much faster than they would over GitHub’s default network.

We build our machine image from [GitHub's image definition](https://github.com/actions/runner-images), so all the same software you expect is pre-installed. Support for Arm runners, powered by Graviton instances, is in beta now.

## Getting Started

You can sign up at <https://depot.dev/sign-up> for a free trial if you’d like to try it out with your own workflows!

## ⚡ Depot - a faster way to build Docker images

Hey everyone! We’re Kyle and Jacob, and we’re excited to share [Depot](https://depot.dev/) with all of you.

[![uploaded image](https://www.ycombinator.com/media/?type=post&id=67759&key=user_uploads/600738/bc4dbd39-a0a3-4838-a4f5-20e6302c00b2)](https://depot.dev/benchmark/temporal)

Depot is a remote container build service that is 3-14x faster than building Docker images inside of generic CI providers. It’s much faster than existing solutions like GitHub Actions because we run BuildKit the right way with a persistent SSD cache. We launch both Intel and Arm VMs for each build, allowing you to build native multi-platform or Arm images without any slow emulation.

PostHog’s Docker builds [run around 5x faster with Depot](https://posthog.com/blog/speeding-up-posthog-builds-with-depot), reducing daily time spent on builds from 5+ hours to just an hour. We continuously benchmark several open-source projects, comparing `docker build` and `depot build`, including:

* [Temporal](https://depot.dev/benchmark/temporal) (\~14.5x faster, saving 7 hours over the last 10 builds)
* [Supabase](https://depot.dev/benchmark/supabase) (\~8.5x faster, saving 2 hours over the last 10 builds)

### Our background

As software and platform engineers, we absolutely hate slow CI builds. Everyone has their own internal timer for what classifies a slow build, our own is 5 minutes, if it takes longer than that we get annoyed. We have experienced first-hand the pain and challenge of keeping Docker container builds fast, optimizing/re-optimizing pipelines and Dockerfiles, and implementing custom runners for multi-platform builds. It’s all annoying, unnecessary, and a drain on developer happiness.

Overall, slow builds clog up the delivery pipeline and take time away from iterating on new ideas and fixing problems for users.

### Building Docker images is slow

Building Docker images in CI providers like GitHub Actions, CircleCI, etc. is slow:

* **Saving and loading layer cache is slow.** Transferring the cache over the network to the ephemeral CI runners eats away at any cache time savings.
* **Runner resources are constrained,** with limited CPUs, RAM, and disk space.
* **Multi-platform and Arm builds require emulation.** Emulation is orders of magnitude slower than native, and Arm is increasingly important with the rise of popularity with devices like MacBook M1, Graviton, etc.

### Our Solution

Depot provides managed VMs running BuildKit, the backing build engine for Docker. Each VM includes 4 CPUs, 8GB of memory, and a persistent 50GB SSD cache disk. We launch both native Intel and Arm machines on AWS. You can choose to have your builder VMs launch in our AWS account or in your own if you want to maintain total control over your data.

Our `depot` CLI is a drop-in replacement for `docker build` as we embed Docker `buildx` directly as a library. Anything you can build with Docker today, you can build with Depot on our remote VMs.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=67759&key=user_uploads/600738/79d72d22-c290-4d0f-87bc-2e2ae2527797)

### Signing up

We love having new folks try out Depot and throw new questions & feedback our way. It really is the fuel that keeps a new startup going.

If you’re annoyed by your slow Docker image builds today, we have a 14-day free trial that you automatically get when you sign up here: <https://depot.dev/sign-up>.
