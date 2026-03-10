# Launches

## Blacksmith: Run your GitHub Actions 2x faster, at half the cost

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79029&key=user_uploads/760850/813c2fd4-6f8b-4da0-a014-b91ac29f1a89)

**tl;dr**

[Blacksmith](https://blacksmith.sh/) helps companies run their GitHub Actions up to twice as fast, at half the cost. We do this by running their Github Actions on high-performance gaming CPUs on a software stack optimized for CI.

**What problem are we solving?**

More engineers writing more tests over time leads to quadratic growth of a company’s CI run time. On top of this, platforms like GitHub Actions have staggering markups while providing compute backed by decade-old server hardware. These platforms are disincentivized from investing in software optimizations to make CI faster since they bill by the minute.

**How is Blacksmith 2x faster?**

Blacksmith runs GitHub Actions on high-performance gaming CPUs. These machines offer significantly better single-core performance, ideal for tasks like code compilation, testing, and single-threaded runtimes like Node.js.

The hardware is only part of the puzzle. Blacksmith runs a software stack optimized for CI.

* We colocate warm caches with our GitHub Action runners resulting in [4x faster cache reads and writes](https://x.com/aayush_shah15/status/1759253159514374552?s=20)
* Local NVMe-backed filesystem for highly performant disk reads and writes
* Docker layers caching across all builds in a GitHub repository resulting in faster docker builds (coming soon)
* Shared volumes to turn every CI run into an incremental build (coming soon)

The numbers speak for themselves

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79029&key=user_uploads/760850/b996eba7-800c-42d5-9f1e-a9f42da2d7ef)

Here’s Blacksmith being used in a [public repo](https://github.com/axelarnetwork/axelar-amplifier/pull/271) by one of our customers, [Axelar.](https://axelar.network/)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79029&key=user_uploads/760850/6500f095-9553-4393-aa2c-0995ad7f5155)

\
**How would I switch from Github to Blacksmith?**

All you need to do is [install our GitHub app](https://app.blacksmith.sh/) and change one line of code in your workflow file.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79029&key=user_uploads/760850/a3def935-6370-472c-b6fe-da85c2839a26)

**Our vision**

We want to be the compute layer for CI (think AWS EC2 for CI). Although we are starting with GitHub Actions, in the future, we plan on expanding to other CI platforms such as BuildKite, GitLab, Jenkins, etc.

We are going after the $10B CI compute market currently captured by the hyperscalers (AWS, GCP, Azure).

**Our team**

We are a team of three engineers who met at the University of Waterloo eight years ago. [Aayush Shah](https://linkedin.com/in/aayushshah15) and [Aditya Maru](https://linkedin.com/in/maruaditya) were early engineers on CockroachDB, working on replication and disaster recovery, respectively. Aayush was then an early engineer at Superblocks, working on enterprise readiness. [Aditya Jayaprakash](https://linkedin.com/in/adijp) (JP) did research in theoretical computer science and later joined Faire (YC W17), where he worked on search infra and was a founding member of the ads team.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79029&key=user_uploads/760850/72125173-2a56-41a6-a286-194624a51db7)

If you’re using GitHub Actions, **we can help your team move a lot faster while reducing spend**. [**Try us out**](https://blacksmith.sh/) - we are a one-line change to integrate, no credit card required.

We love talking to companies about their CI infra. You can reach us at [hello@blacksmith.sh.](mailto:hello@blacksmith.sh)
