# Launches

## bumpgen - keep your code up-to-date with AI

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80578&key=user_uploads/89898/e210f386-2345-4c2e-ba0a-6133d756141a)

[**bumpgen**](https://github.com/xeol-io/bumpgen) generates fixes for breaking changes in version upgrades with AI

* 🧑🏼‍💻 `bumpgen <package> <new-version>` to get fixes to your version bump breaking changes
* 🔑 Bring your own **OpenAI API key**
* 🌐 Supports **Typescript** codebases

### Why build bumpgen?

Keeping your dependencies updated is a good security and engineering practice (just not too up-to-date, thanks xz 🙏🏼). But they can be a pain to actual perform because:

* **Major version bumps** have breaking changes and no one wants to fix them.
* **25% minor version bumps** have breaking changes as well (semver isn’t perfect)
* There can be a lot of version bumps from small packages to large frameworks

### How Does bumpgen work?

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80578&key=user_uploads/1279127/f06347b9-da03-4f95-aa1b-8f850576b262)

**bumpgen** is pretty straight forward:

* **BUMP** your dependency version then **GEN**erate the fixes for the breaking changes
* Quick to get started with `npm install -g bumpgen`
* Works on top of your Dependabot or Renovate to take care of those gnarly breaking changes

If you are curious how bumpgen identifies, fixes, then propagates the breaking change fix, we added bumpgen’s architecture and design decisions [**here**](https://github.com/xeol-io/bumpgen) 👈

### How to start?

* 🧑🏼‍💻 [**Try it out**](https://github.com/xeol-io/bumpgen), it’s 100% open source
* ⭐ [**Support**](https://github.com/xeol-io/bumpgen) the project with a star
* 📩 [**Get updated**](https://www.xeol.io/beta) on the GitHub app release

## 🌌 Xeol - Modern platform for software supply chain security

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73333&key=user_uploads/1279127/210f8a5b-d0c2-4f78-a504-dea9eb6669ca)

### TLDR

> Fortune 500 companies use Xeol to connect all their software dependencies into a contextual graph to ask questions like “am I affected by vulnerability X?” and enforce policies like “ensure all my docker images were signed by me?”

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73333&key=user_uploads/1279127/040b5865-0ba9-42f6-a893-bbf3f0eb3222)

We first met 6 years ago as early engineers at **Ada** leading backend, cloud infrastructure, and security. Right before founding Xeol:

* **Benji** was a Sr DevOps Engineer at **Datadog** leading its service catalog project with a near decade career in DevOps
* **ShiHan** was the Director of Engineering helping build 2 startups from early stage to 🦄

We have been in the startup world for many years and are now on our own journey to help AppSec engineers quickly identify, remediate, and enforce security risks.

### Problem. A New Attack Vector

Ask anyone on the street to plug in a random USB drive and they will scoff. They know it’s unsafe! But developers do this every day when they use open-source packages as part of their software supply chain. The typical npm package has **86 dependencies** and with supply chain attacks up **600%** over the past year alone, this attack vector is widening.

What’s not working?

* **Too much noise:** tools that show all possible CVEs without contextual runtime information make prioritization near impossible leading to alert fatigue
* **Attacks are more common:** generative AI enables malicious actors to easily launch attacks
* **Huge attack surface:** many actors involved including OSS maintainers and their code, CI/CD systems, container orchestrators, and in-house developers

### Solution. Complete Ontological Visibility

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73333&key=user_uploads/1279127/a7017029-25ff-45a2-b114-6386d949057d)

Xeol is an **agentless** solution that scans your software artifacts at **build** and **runtime** then creates a **contextual graph** of your software supply chain. This contextual graph allows AppSec engineers to:

**answer** questions like

* Where am I using package X?
* Which software are end-of-life?
* Which packages are missing SLSA attestations?
* Which software artifacts are produced from repo X?

**enforce** policies like

* Ensure all Docker images were built by my org from our CI pipeline
* Prevent software X, which is end-of-life, from being packaged in our Docker images
* Ensure sure all packages meet a minimum [OSSF](https://openssf.org/) score
* Prevent any dependencies using a GPL license

### Our Ask

**See** Xeol’s graph capabilities in action [here](https://dashboard.xeol.io/demo)

**Try** our open-source CLI [tool](https://github.com/xeol-io/xeol) to scan for end-of-life software

**Follow** us on [LinkedIn](https://www.linkedin.com/company/xeol), [GitHub](https://github.com/xeol-io), or [Twitter](https://twitter.com/xeol_io) to get the latest updates
