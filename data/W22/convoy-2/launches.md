# Launches

## Nohooks: Webhooks for platforms without webhooks

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72597&key=user_uploads/357104/239f25e6-9726-4a95-8100-b4e04df0405e)

Today, we are excited to share our new tool: [nohooks.io](http://nohooks.io). Nohooks is a service that offers webhooks functionality even on platforms that do not have native webhooks support. With Nohooks, developers can receive real-time notifications of events from the list of supported apps ([DigitalOcean](https://www.digitalocean.com/), [Notion](https://notion.so/) and [Render](https://render.com/) as of this [launch](https://getconvoy.io/blog/convoy-launch-week)).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72597&key=user_uploads/357104/c9767c6b-6fce-42dc-93d5-39b8bfdd658f)

Webhooks are a way for one application to notify another application when a specific event happens. By setting up a webhook, developers can receive real-time updates whenever a user takes a specific action, such as deploying a new service or adding a new contact to your CRM. However, not all platforms support webhooks, which can be a problem for developers who need to receive real-time updates.

Nohooks solves this problem by acting as an intelligent polling system, that retrieves resources from the public API of these apps, determines whether there was an update and generates a webhook event depending on the type of update. It uses [Convoy](https://getconvoy.io/) to power its webhooks delivery and debugging dashboard.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72597&key=user_uploads/357104/fab69289-51b5-4756-9536-5341f7139c15)

With Nohooks, you can link multiple Render accounts and Notion workspaces and multiple destination endpoints as well. To get started, create an account here, and watch this demo video to learn how to set up your account to receive events.

### **Use Cases**

1. With Render webhook events, you can hook into the lifecycle of your services and service deployments to perform post-deployment actions, trigger continuous delivery pipelines etc.
2. With Notion webhook events, you can sync any Notion Database to Airtable, Mailchimp, Intercom, or any CRM you choose. You can sync Notion Events to anything like Zapier or [Trigger.dev](http://Trigger.dev) for any kind of automation you desire.
3. With DigitalOcean webhook events, you can into the lifecycle of your droplets to carry out post-deployment automation similar to Render. We plan to support many more resources in DigitalOcean in subsequent releases.

That’s it, friends, go and automate. We can’t wait to see what you build with this!

If you need any help or want to see us support new services, you can email us at [support@nohooks.io](mailto:support@nohooks.io) or join our [Slack Community](https://join.slack.com/t/convoy-community/shared_invite/zt-xiuuoj0m-yPp\~ylfYMCV9s038QL0IUQ) to ask questions.

## Convoy: Open Source Webhooks Proxy

**TL;DR: Convoy provides a reliable webhooks proxy that can ingest webhooks from all your providers and replay them to your backend as well as publish webhook events from your systems to your customers.**

Hey YC 👋🏾

I am Subomi, and I am building [Convoy](https://getconvoy.io) alongside Emmanuel.

**The Problem**\
Today, webhooks power critical business workflows that, if broken, will have a direct impact on customers’ experience. Usually, developers spend time building reliable webhook ingestion services and reliable webhook dispatching services for API providers. This time is wasted effort that can be spent building necessary infrastructure instead of building your product. Secondly, the tooling becomes fragmented for dispatching and receiving webhook events. We are working on Convoy to solve precisely this using a consistent toolchain to receive, publish and debug webhook events.

**Our Solution**\
Enter Convoy, a service available as an open-source project and a cloud platform. There are two types of projects in Convoy; an incoming project and an outgoing project. In an incoming project, we provide a unique URL per provider to receive events, and in an outgoing project, we provide a REST API to receive events from your services and publish them to the outside world.

**How it works?**

You can see a demo [here](https://www.youtube.com/watch?v=DSIet81oBsg).

**Asks**

1. If you’re building an API that sends out webhooks and/or a service that relies on webhooks from third-party providers, you can get started for free by either [self-hosting](https://getconvoy.io/docs/deploy/overview) or using our [cloud platform](https://dashboard.getconvoy.io/signup).
2. If you have vast experience running webhooks infrastructure (either incoming or outgoing), please join us on [slack](https://convoy-community.slack.com/join/shared_invite/zt-xiuuoj0m-yPp\~ylfYMCV9s038QL0IUQ#/shared-invite/email). We’d love to learn from you!
3. If you have further questions and would love to learn more, you can book a meeting with the [founders.](https://calendly.com/subomioluwalana/30-minute-meeting)

Thank you!
