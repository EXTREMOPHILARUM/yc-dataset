# Launches

## Distr – The Open Source Control Plane for Self-Managed, BYOC, and On-Prem Deployments

Hi everyone! We’re [Philip](https://www.linkedin.com/in/pmigat/) and [Louis](https://www.linkedin.com/in/louisnweston/), the co-founders of [Glasskube](https://glasskube.dev/) and we are excited to share Distr.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90349&key=user_uploads/1278777/8ef8adb5-e11a-40bf-9b04-efa9c19be58e)

**TLDR:** Distr is an Open source control plane for AI companies. Our customers plug us into their existing CI/CD pipeline to offer BYOC and self-managed in hours, not months.

**Distr is fully open source.** Check out our repository on [GitHub](https://github.com/glasskube/distr). (We'd appreciate a star 🌟)

### **“Self-managed is making a big comeback.” — Shay Banon, Founder of Elastic**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90349&key=user_uploads/1278777/33f877d3-6adf-49eb-aa00-add8dcbcdde3)

We spoke with Shay earlier this month, and I couldn’t agree more.

* Enterprises want control.
* Data is valuable
* Security concerns are rising
* Data sovereignty is now critical, especially in the age of AI.

This shift has been building for a while and is accelerating rapidly, particularly in Europe, Singapore, and regulated industries around the world.

If you're building AI tooling and selling to large customers, how often have you been asked: _“Can we run this inside our VPC?”_

### So why isn’t everyone offering self-managed?

Big players like ClickHouse, Snowflake, and Redpanda figured it out early. But for smaller teams, supporting self-managed deployments often feels out of reach. Too much effort, not enough return.

Self-managed often means:

* Too much complexity, too early.
* Every customer wants something different.
* Shipping updates is slow and painful.
* You’re flying blind, no usage insights.
* Troubleshooting without visibility is brutal.

### 

### Our Solution

Distr is your Open Source control plane for self-managed, BYOC, and on-prem deployments. It gives you everything you need out of the box to support self-managed customers without building a custom solution from scratch. Distr fits right into your existing stack and lets you onboard, update, and support self-managed customers in minutes, not months. Just connect your GitHub repo and you’re up and running.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90349&key=user_uploads/1278777/0a5b78df-5000-421a-8d6d-24a4f820b0db)

* **Simple GitHub integration:** Connect your repo and start shipping in minutes.
* **Works with your stack:** Supports Docker Compose, Terraform, Docker Swarm, and Kubernetes.
* **Deploys anywhere:** AWS, GCP, Azure, on-prem, and even air-gapped environments.
* **White-label customer portal:** Give your customers full control and visibility into their deployments.
* **Built-in OCI registry:** Track image downloads and updates at the user and tag level.
* **Advanced telemetry:** Collect detailed usage and performance metrics with OpenTelemetry.
* **Flexible licensing:** Restrict access to versions and features with our Open Feature-compatible licensing server.
* **API-first and automation-ready:** Fully integratable via API and SDK for custom workflows.

https://youtu.be/FkSWkudlHJw

### Coming soon:

* Built in CVE scanning and automated security checks for all artifacts
* HubSpot Integration
* Workflows with Slack Notifications

### First self managed customer?

Zero to one is the hardest. From your first PoC to a working Helm Chart and your first self-managed production deployment—we’ve done it all, many times over. That’s why we support you during your first self-managed customer and why using Distr is an unfair advantage.

### Our Ask

* [Try it for free](https://signup.distr.sh/signup.html) and give us feedback or
* [Book a Demo](https://cal.glasskube.com/team/gk/demo)

## Glasskube - Open source package manager for Kubernetes

Hi everyone! We’re [Philip](https://www.linkedin.com/in/pmigat/) and [Louis](https://www.linkedin.com/in/louisnweston/), the co-founders of [Glasskube](https://glasskube.dev/).

**TLDR:** Glasskube is an open source package manager for Kubernetes that makes deploying, updating, and configuring packages on Kubernetes **20x faster than** tools like **Helm or Kustomize.** Inspired by the simplicity of Homebrew and npm, our goal is to build enterprise-ready infrastructure software that can run mission-critical workloads across the more than 3 million Kubernetes clusters globally.

**Glasskube is fully open source.** Check out our repository on [GitHub](https://github.com/glasskube/glasskube). (We'd appreciate a star 🌟)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81592&key=user_uploads/1278777/b43af44c-5372-4995-a383-3a84cdc9941c)

# **The Backstory & Problem**

Kubernetes packages have been growing rapidly, from around 100 packages in 2016 to over 800 packages on the CNCF landscape today. With more than 7 million developers working with Kubernetes, Helm, an open-source tool created during a hackathon nine years ago, has become the go-to solution. However, Helm struggles to keep up with the increasing demand, leading to complex workflows and non-standardized solutions.

Over the past five years, writing and deploying packages on Kubernetes, we found ourselves defaulting to Helm despite its shortcomings due to a lack of alternatives. While working on other cloud-native projects, users consistently highlighted common pain points with Helm. This realization prompted us to tackle the larger issue of package management in Kubernetes, leading to the development of Glasskube.

# **What is Glasskube?**

Glasskube brings the experience of Homebrew or npm to your Kubernetes cluster. It simplifies installation, updates, and configuration, making it easier and faster to manage your packages.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81592&key=user_uploads/1278777/f1208e18-d6ab-40ca-ae88-9b1be886b50a)

**Focusing on simplicity and reliability with our CLI and UI**

Easily install packages in your cluster via the Glasskube UI, where all packages are conveniently located, eliminating the need to search for a Helm repository.

**Safe Package Updates**

Preview and perform pending updates to your desired version with a single click (or CLI command). All updates are pre-tested by the Glasskube test suite.

**Package configurations**

Configure packages with typesafe input values via the UI or interactive CLI questionnaire. Inject values from other packages, ConfigMaps, and Secrets easily. No more untyped and undocumented values.yaml files.

**GitOps Integration**

All Glasskube packages are custom resources, manageable via GitOps. We're also integrating with [renovate](https://github.com/renovatebot/renovate/issues/29322). \
\
Read also more about [dependency management](https://glasskube.dev/docs/design/dependency-management/), [multiple repositories and private packages](https://glasskube.dev/docs/design/repositories/) on our [website](https://glasskube.dev/).

Interested? Check out our [Demo.](https://youtu.be/aIeTHGWsG2c)

# **Our Vision**

Currently, we are focused on enhancing the user experience, aiming to save engineers as much time as possible by building on top of existing technologies. In the future, we plan to develop an entirely new packaging and bundling format for all cloud-native packages. This will provide package developers with a straightforward way to define how to install and configure packages, offer simple upgrade paths, and enable us to provide feedback, crash reports, and analytics to every developer working on Kubernetes packages, similar to how Android supports Play Store developers.

# **Presignup - Glasskube Cloud**

We are currently working on Glasskube Cloud, for which you can now [pre-signup](https://glasskube.cloud/signup.html). Key features include:

* Cloud Hosted Private Packages
* Security Alerts and Update Notifications
* Advanced GitOps Integrations (intelligent insights on upgrade success probability, smart config migration suggestions, enhanced open PRs showing detailed changes at manifest/resource level)

# **Our Asks**

We love talking to engineers and anyone interested in DevOps who uses Kubernetes. You can schedule a call with Louis and Philip [here](https://cal.glasskube.eu/team/founder/30min).

If you find this interesting and would like to try it out:

* Presignup for [Glasskube Cloud](https://glasskube.cloud/signup.html)
* Check out our repository [on GitHub](https://github.com/glasskube/glasskube).
