# Launches

## Infra.new - AI Copilot for Cloud DevOps

**tl;dr**\
[**infra.new**](http://infra.new) is an AI DevTool that configures your cloud infrastructure for cost and security.

You can set up your entire infrastructure stack from scratch or import your GitHub repository to optimize your existing configuration.

Try it now at [**infra.new**](http://infra.new) – no signup required.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87449&key=user_uploads/808343/7e666222-a6d5-4cc8-887e-f341c3d8f10d)

---

---

—

---

Hey everyone,

We're excited to launch [**infra.new**](http://infra.new)—your AI Copilot for Cloud DevOps.

The cloud is complicated. Engineering teams waste countless hours configuring Infrastructure as Code, CI/CD pipelines, and other related DevOps tooling. Whether you’re setting up a new project or reconfiguring an existing one, manual configurations and unpredictable costs can slow you down.

We’re building an AI agent specialized in configuring the cloud so engineering teams can focus on shipping their product without sacrificing control or cost.

### **Problems with LLMs and DevOps**

* **Stale Documentation & Configuration Errors:**\
  LLMs often reference outdated docs and hallucinate fields that don’t exist, resulting in misconfigurations that can cost you time and money.
* **Hidden Cloud Costs:**\
  A single tweak can unexpectedly spike your expenses. Without clear visibility, planning your budget is a guessing game.
* **Lack of Context:**\
  General-purpose coding agents are great at updating application code, but often struggle to find the subtle connections between different configuration files.
* **Bad Training Data:**\
  LLMs will generate an average of the content they see online, but the average cloud configuration online is messy and filled with bugs. Most IaC on Reddit is related to junior devs asking about their configuration.

### **Our Solutions**

* **Fresh Documentation:**\
  The agent pulls the latest documentation for Terraform, GitHub Actions, and other tools before every change, ensuring your configurations are accurate and current.
* **Real-Time Cost Calculator:**\
  You can see a complete breakdown of your cloud costs update in real-time as your configuration changes, so you know exactly how much it will cost before you deploy.
* **Automated Error Detection & Fixes:**\
  A dedicated language server scans your configuration for issues and applies fixes automatically, reducing manual debugging.
* **Expert-Guided Best Practices:**\
  The agent has access to a corpus of expert human examples that it references to produce configuration that is optimized for performance and security.
* **Two-Way GitHub Sync:**\
  Import your existing Terraform, see what it currently costs, ask the agent to look for optimizations, then export any changes back to GitHub.

### **Demo**

Watch me use [infra.new](http://infra.new) to reduce our AWS bill from $400 to $150 with little to no effort in the video below

[Infra.new](http://Infra.new) [Demo - AWS](https://www.loom.com/share/3b7d85b25fd94cfd93ca19c39c188618?sid=f9ca58ca-6bd3-4b97-bd3b-46c842ea8160)

### **Contact Us**

If you have any questions or feedback, please feel free to reach out!

Email the founders at [founders@launchflow.com](mailto:founders@launchflow.com) or book some time to chat at <https://calendly.com/josh-from-launchflow/chat>

## LaunchFlow - A Terraform / Pulumi alternative for Python developers

[**LaunchFlow**](https://launchflow.com/) is an Infrastructure as Code Python SDK that extends OpenTofu with features like [**multi-environment support**](https://docs.launchflow.com/docs/concepts/environments), [**autoconfigured infrastructure clients**](https://docs.launchflow.com/docs/concepts/resources), and [**API release management**](https://docs.launchflow.com/docs/concepts/services).

![](https://bookface.ycombinator.com/media/?type=post&id=82326&key=user_uploads/808343/d6958b07-d5be-4547-b751-173b033339c5)

You can add GCP / AWS infrastructure to your app with a single line of code - all infrastructure types ship with built-in clients that automatically connect to your infrastructure across multiple environments. Includes integrations with [**FastAPI**](https://docs.launchflow.com/docs/framework-guides/fastapi), [**Flask**](https://docs.launchflow.com/docs/framework-guides/flask), and [**Django**](https://docs.launchflow.com/docs/framework-guides/django).

**Try it out**

It only takes 3 commands to launch your first app to GCP or AWS

1. install the Python SDK with pip

   ```
   $ pip install launchflow 
   ```
2. setup launchflow in any Python project

   ```
   $ lf init 
   ```
3. deploy everything used in your code to GCP / AWS

   ```
   $ lf deploy {env} 
   ```

Follow the [**Get Started Guide**](https://docs.launchflow.com/docs/get-started) to launch an example FastAPI app in a matter of minutes.

No account required.

**Easily collaborate with your team**

LaunchFlow Cloud is an optional service you can use to create collaborative cloud environments that automatically share infrastructure, configuration, and secrets with your team. You can also access preconfigured GitHub release pipelines, audit logs, RBAC security, and more.

![](https://www.launchflow.com/_next/image?url=%2Fhome%2Fconsole.png&w=2048&q=75)

You and a teammate can try LaunchFlow Cloud 100% free forever - signup at [**console.launchflow.com**](http://console.launchflow.com/) to get started.

**Contact us**

If you are interested in anything mentioned above, we would love to hear from you!

You can email us at [**team@launchflow.com**](mailto:team@launchflow.com) or book some time on [**my calendar**](https://calendly.com/josh-from-launchflow/chat).

Happy launching! 🚀

## LaunchFlow: A better developer experience on GCP and AWS

## **TLDR**

[**LaunchFlow**](https://www.launchflow.com/) manages cloud environments in your own GCP / AWS account that are secure, scalable, and cost-effective by default. Import Postgres, Redis, and other cloud resources in your Python code, then deploy everything to your cloud with a single command.

—

LaunchFlow is an [**infrastructure-from-code**](https://infrastructurefromcode.com/) tool that aims to dramatically improve your developer experience on GCP and AWS. We automatically deploy infrastructure to dedicated environments in your cloud as you use it in your code and ensure it's configured for both local development and production deployments.

## **The Problem**

We believe managing and using cloud infrastructure is far more complex than it should be. It's hard to set up deployment pipelines. It's frustrating to run your application locally. It's annoying to keep your cloud configuration in sync with your application code.

Most teams cobble together their own DevOps automations using a mixture of Terraform, Pulumi, custom scripts, and environment variables. These automations are great when they work but are often brittle and eventually become the main source of overall system complexity.

We believe there's a better way.

## **The Way**

![](https://lh7-us.googleusercontent.com/86TIu-MtInbRpmbfJWeL50XX54rQ0LV8KadWXaHHZJyZ9pmJ6ZMCKUwHoDLmDDukyiDubynyYQShtBsOLdrrdf08-ZYYEflSKKUIhrb7x9OY8YMNs_OBI_0ydBleeUpuU-jZqe2ycmB_N-PynbDzc7U)

Use LaunchFlow’s Python SDK to import Postgres, Redis, and other cloud resources in your Python code, then deploy everything to dedicated environments in your cloud with a single command.

Everything in the LaunchFlow ecosystem is fully configured for local development and cloud deployments by default.

**Environments**

LaunchFlow **deploys** and **manages** your infrastructure inside [**Environments**](https://docs.launchflow.com/docs/concepts/environments) that run in your own cloud account. These Environments satisfy most compliance requirements by default and are automatically configured for cost, security, and reliability.

![](https://lh7-us.googleusercontent.com/Qa6mHTluFv0JTJqD6JwWs9vzQHmZxtn5j54fqvXUTmieIg20B7nBtZIrTOJ3SquGLPJaYtHvGHUKMuHOmv1zLJge7zLy5KYr8pNzmeSX3abNorK2DQ3I2_2iV6qNP6bRMsh80d1jZFUpjUmAURGpLcY)

**Resources**

You can **create** and **connect** to cloud [**Resources**](https://docs.launchflow.com/docs/concepts/resources) in an Environment by simply importing them into your code. Our SDK provides ready-to-use client APIs for every Resource so you can immediately start using them in your application both locally and when deployed.

![](https://bookface.ycombinator.com/media/?type=post&id=80185&key=user_uploads/808343/085c12a5-8f53-44b9-8a97-1799f53ff2f4)

**Deployments**

You can **build** and **deploy** Python applications in the same environment as your resources with a single command. LaunchFlow [**Services**](https://docs.launchflow.com/docs/concepts/services) lets you deploy your APIs to GCP / AWS with all resource permissions and networking settings automatically configured. We will be adding Jobs and Notebook deployments in the next couple of months.

![](https://bookface.ycombinator.com/media/?type=post&id=80185&key=user_uploads/808343/b7c23093-c085-4a3d-97ac-60ebb78d92f5)

## **Works anywhere that Python runs**

LaunchFlow Resources manages its own configuration and can be plugged into any existing Python app. We’re framework-agnostic and work anywhere that Python runs - we also include a library of common utilities for building FastAPI, Flask, and Django apps on the cloud.

## **Why not just use Terraform / Pulumi?**

Tools like Terraform and Pulumi make it easy to automate cloud infrastructure, but there is still an added cost of maintaining a separate IaC tool and keeping it in sync with your application encode.

On top of this, these tools only help you create the infrastructure, but they don't help you actually _use_ it. Engineers can spin up infrastructure in a few minutes, but they'll often spend the rest of the day (or longer) stumbling through docs and blogs, trying to figure out how to actually connect it to their application.

Things only get worse once you add a release pipeline into the mix and now need to figure out how to structure your code to work across multiple environments.

This creates a tradeoff between automation and overall system complexity, which is why many teams put off IaC practices until they can afford a DevOps engineer/team to maintain the automations for the company.

## **Our ask**

We are looking for pilot users who would like to start using LaunchFlow today.

If you’re interested in using LaunchFlow, please email me at [**josh@launchflow.com**](mailto:josh@launchflow.com) or schedule a demo call using my [**Calendly**](https://calendly.com/josh-from-launchflow/one-on-one-with-josh-founder).

Happy launching! 🚀
