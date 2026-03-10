# Launches

## 🤖 SmartTests: AI powered Contract Testing

Hey everyone! We’re [Arjun](https://www.linkedin.com/in/arjun-iyer-916332/) and [Anirudh](https://www.linkedin.com/in/anirudhrx/), co-founders of [Signadot](https://www.signadot.com/) and we’re simplifying the lives of developers building distributed cloud native applications.

# **🎯tl;dr**

SmartTests automatically catch breaking API changes in microservices without writing contracts or maintaining mocks. AI compares your new code against baseline behavior using real traffic and only flags changes that actually matter.

Demo video: https://youtu.be/HHGgSKk2K_k

# ❗️Problem

Microservices break each other all the time. A team changes their API response format, and suddenly three downstream services start failing in production. The usual solution is contract testing, but here's the reality: most teams either skip it entirely or abandon it after a few months.

Why? Current tools put the entire burden on developers. You have to write consumer contracts for every API interaction, maintain mock servers, and keep updating tests every time contracts change. It's exhausting busywork that pulls focus from shipping features. Teams know they should do it, but the tooling makes it feel like a second job.

# **💡** Solution

SmartTests flip the script on contract testing. Instead of forcing developers to predict every possible breaking change, we observe real API interactions and automatically catch contract violations. Write a simple test in Starlark, and our AI compares baseline behavior against your changes to spot what actually matters.

No mock servers to maintain. No contract files to update. No noise about irrelevant changes. Just fast, accurate feedback in your PRs that tells you when you're about to break something downstream.

# 🏃How does it work?

When you push code, SmartTests spin up lightweight sandboxes in your Kubernetes cluster and run your test scripts against both the new version and the baseline. These aren't mocked interactions—they're real API calls hitting real services in isolated environments.

The magic happens in the comparison. Our AI analyzes the responses from both versions and figures out which differences actually matter. Did you add a new optional field? Probably fine. Did you change a required field's data type? That's going to break things. The AI surfaces only the changes that could affect downstream services, so you get signal instead of noise.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90673&key=user_uploads/47401/298831aa-1812-4117-8461-1a77db646e8c)

# **💯** Why did we build this?

We kept hearing the same story from engineering teams: "We tried existing tools, but it was too much work to maintain." When developers abandon tools that should make their lives easier, the tool is the problem, not the developers.

The breaking point was talking to a team at a Series B company who had spent three months setting up comprehensive Pact tests, only to disable them six months later because they couldn't keep up with the maintenance burden. That's when I realized we needed to completely rethink the approach—AI could handle the heavy lifting leaving developers to focus on what they do best: building great software.

# 👍 How do I get access?

Just sign up using https://www.signadot.com/ and try our [Quickstart](https://www.signadot.com/docs/tutorials/quickstart/contract-testing) guide. Feedback is much appreciated!

## Developer Environments built for Kubernetes

**tl;dr**: If you’re running microservices, you can now use Signadot to help developers ship features faster using lightweight dev environments. These environments spin up in seconds within a Kubernetes cluster **that you run** and scale well across hundreds of developers and microservices without incurring large infrastructure costs or maintenance burdens. These environments are built on top of “Sandboxes”, a new approach that is used in companies like [**Uber**](https://www.uber.com/blog/simplifying-developer-testing-through-slate/) and [**Lyft**](https://eng.lyft.com/scaling-productivity-on-microservices-at-lyft-part-3-extending-our-envoy-mesh-with-staging-fdaafafca82f) and we’re excited to make that available to everyone.

We launched about a year ago, with a focus on preview & test environments in Kubernetes. With our latest update, we’re adding the following new capabilities:

* Developers can now run the **dev version of a microservice on their laptop** and seamlessly connect it to a shared Kubernetes cluster and start testing as though the whole application were running locally. They get 10x faster feedback by testing their changes in a live Kubernetes environment during active development. 
* Multiple such dev environments can be combined together to **test different microservices with each other** as they're being developed. This means developers can collaborate and get a feature spanning different microservices working end-to-end long before their code gets merged or hits a staging/production environment.

### **How does it work?**

Just as before, we use request routing (using a Service Mesh like [**Istio**](https://istio.io/) or a sidecar-based system that we built) to isolate these environments from one another in a shared Kubernetes cluster.

![](https://ph-files.imgix.net/f5efe69b-ed3c-4306-af3e-c5d757877d7a.png?auto=compress&codec=mozjpeg&cs=strip&auto=format&fit=max)

Read more about our launch [**here**](https://www.signadot.com/blog/bridging-the-gap-local-testing-in-shared-kubernetes-clusters), or watch a video of how teams use these dev environments here: [**https://www.youtube.com/watch?v=HXUmPJTdwm0**](https://www.youtube.com/watch?v=HXUmPJTdwm0\*\*)

### **How do I get access**

Just sign up using [**https://www.signadot.com/signup**](https://www.signadot.com/signup\*\*) and try one of our [**quickstart**](https://www.signadot.com/docs/quickstart) guides. Feedback is much appreciated!

## Signadot: Ephemeral Test Environments built for Kubernetes

### 😎 **TL;DR**

We’re building a Kubernetes-based solution that enables environments, called Sandboxes, to test your microservices early in the development lifecycle. Unlike traditional environments, Sandboxes are lightweight and spin up in seconds. This makes it cost-effective to create test environments for every pull request, branch, and commit.

### 🤔 **The problem with traditional environments**

Most engineering teams use pre-production environments, called staging environments, to test against real-world conditions. However, testing on staging introduces the following challenges:

1. Staging environments are typically shared among engineering teams and regressions introduced here block other developers. This results in frequent roll backs to unblock others.
2. Since commits from various teams are co-mingled on staging, breakages take a long time to troubleshoot and fix. As the engineering team grows, this problem only gets worse and development slows down.

### **😅 Enter Signadot**

With Signadot, DevOps teams can set up lightweight environments, called Sandboxes, that can be used to test each pull request/commit. Teams run a suite of integration and end-to-end tests for each PR without impacting others. This helps find issues early that would otherwise be found in staging (or worse … in production!).

Our CLI/YAML integrates with CI pipelines to automate the testing of Pull Requests. As shown in the image below, Sandboxes encapsulate “services-under-test” connected to other dependencies running in Kubernetes. Sandboxes are lightweight to spin up and cost-efficient at scale.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65752&key=user_uploads/47401/edb398f0-819b-43f3-9152-9ba015164069)

### **🤓 How this helps your team:**

* Minimize rollbacks on staging and production
* Increase the frequency of production deployments
* Save on infrastructure costs using lightweight Sandboxes

### **🤩 Try us out!**

1. [**Sign up for free**](https://www.signadot.com?utm_campaign=Launch%20YC&utm_source=yc&utm_medium=launchyc) **to start testing your microservices today**
2. Join the discussion on testing strategies for microservices in our [Slack Community](https://signadotcommunity.slack.com/) or [GitHub Repo](https://github.com/signadot). You can also book a time to chat with one of our founders [here](https://calendly.com/signadot/demo).
