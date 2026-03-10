# Launches

## SubImage: Software that maps your infrastructure

[SubImage](https://subimage.io) maps your infrastructure so that your security team can fix the most pressing risks first. It’s built on top of [Cartography](https://github.com/cartography-cncf/cartography), the open source security graph that we created and that 70+ companies use.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87887&key=user_uploads/1645462/579aac2a-8b0c-4987-a4f2-930369eda0e2)

## **Problem**

In security, attackers often have to be right just once, but defenders have to be right all the time. 

The scary thing is, given enough time, resources, and motivation, it is a near certainty that an attacker will break into your environment. You need to be ready with detections and controls to catch and evict them.

However, most companies, even huge ones, are nowhere near ready for that. They are either inundated with data and stuck deciding what to fix next, or worse, have **poor to no visibility** on high impact risks.

Further, modern businesses often rely on dozens of cloud and SaaS platforms, so it’s very easy to lose track and make mistakes in configuring access permissions, networking, and other areas to inadvertently introduce an attack path.

## **Solution**

We originally created Cartography in 2019 to help red teamers (professional corporate hackers) find the shortest paths to their targets. [At the time](https://news.ycombinator.com/item?id=19517977), there was nothing quite like it: other tools weren’t graph-based, didn’t cover the cloud, or weren’t open source.

The tool grew in popularity when defenders realized that **using an attacker’s mindset** to map out their infra was an immense boon to their work because it cut through the noise, exposing proven attack paths.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87887&key=user_uploads/1645462/030c8839-2635-45c8-beda-d6c9b11d1e32)

Cartography pulls metadata from multiple sources - SaaS, cloud service providers, a company’s internal services - and writes it to a graph database. This simple technique is incredibly powerful in finding otherwise unseen misconfigurations and attack paths in areas like access permissions, networking, and software vulnerabilities.

SubImage is our fully-hosted solution that picks up where Cartography leaves off: it lets security teams immediately see and take action on the attack paths to their organization’s most sensitive data and secrets without needing to set up or maintain the database and sync jobs behind it.

The specific fix-action varies: smaller companies may prefer executing AWS CLI commands from an admin session, whereas larger corporations often require automated pull requests within their infrastructure-as-code repositories.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87887&key=user_uploads/1645462/ec669a28-c877-4791-a571-aec027932afc)

## **Demo: My Stripe API key was stolen**

<https://youtu.be/RBCr35hb5Hk>

## **Demo: Hack my company**

One of the most effective ways to secure yourself from hackers is to put yourself in their shoes and think about how they would exploit your environment. So, let’s plan an attack on one of SubImage’s storage buckets; it’s kind of like planning to break into a bank vault.

<https://youtu.be/P_meu4_aIVA> 

The above demo shows that we also provide customers access to the underlying graph database so that they can see the internals of our schema and more deeply understand their infra.

## **Roadmap**

Our north star is for security engineers to stop needing to constantly monitor whether infrastructure, new or old, has introduced a risk – we will do it for them.

Specifically, we plan to

* Integrate with access management systems to **prune excessive permissions** and enforce that certain invariants are maintained
* Continuously **alert on and remediate** risky infrastructure changes
* **Show misconfigurations** in any cloud or SaaS based infrastructure, including vulnerability management

## **Asks**

1. If you’re a company that is building out your security team, we’d love to learn about your problems and work together. Let’s [meet](https://cal.com/team/subimage)!
2. If you are struggling with security visibility or if any of this sounds interesting to you, check out [Cartography](https://github.com/cartography-cncf/cartography/). We would love to get your feedback and have you as part of our community: join the CNCF Slack workspace [here](https://communityinviter.com/apps/cloud-native/cncf) and then join the #cartography channel.

## **Team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87887&key=user_uploads/89898/0f181717-ad90-4cd8-a86c-67debce4c790)

Hi! We’re [Alex](https://www.linkedin.com/in/alexchantavy/) and [Kunaal](https://www.linkedin.com/in/kunaals/), and we’ve been working together since 2020 when we met at Lyft. Alex was the lead engineer on Lyft’s vulnerability management program, led penetration tests for Microsoft’s Red Team, and worked on \[REDACTED\] at the NSA. Kunaal was a Staff Engineer at Lyft and Member of Technical Staff at Anthropic, and has spent his career solving large security problems like insider abuse, vulnerability management, and architecting SIEMs.
