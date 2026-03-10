# Launches

## Terracotta AI - AI agents for Infrastructure as Code workflows

# **tl;dr**

Platform and DevOps teams are still catching Terraform issues after they break production. Terracotta AI brings AI-powered review directly into PRs, analyzing your code, state, and live cloud resources to prevent problems before any workflow triggers.

**Try Terracotta AI for free at [https://tryterracotta.com](https://tryterracotta.com)!**

https://www.youtube.com/watch?v=QyzyiJVeZqU

https://www.youtube.com/watch?v=GuSfvcYllZo&t

# **Problem**

Even the simplest Terraform changes can break production in unexpected ways and can take a significant amount of time to debug and fix.

Platform teams have developed sophisticated DevOps practices, including module catalogs, compliance policies, and continuous integration/continuous delivery (CI/CD) pipelines.

However, even with senior engineers reviewing pull requests (PRs), critical issues still slip through, including drift conflicts, hidden dependencies, and blast radius across services that you didn't know were connected.

The problem isn't a lack of processes. It's that humans can't consistently analyze Terraform changes against live cloud state, remote state, and downstream dependencies simultaneously. Traditional tools catch problems after the PR is approved or deployed, not before.

# **Solution**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91358&key=user_uploads/925045/89ae62a4-eb80-4d9e-95d5-e2af0684740a)

We created a purpose-built AI agent for Infrastructure as Code (IaC) workflows that seamlessly integrates into your IaC pipeline, contextualizing and providing real-time feedback directly within your pull requests.

Terracotta AI analyzes every Terraform change against the most critical contexts in your IaC deployment pipeline and provides accurate, contextual, actionable feedback inside of your PR:

* **Your IaC code** — syntax, structure, linting, and more
* **Local plan state** — what Terraform thinks will happen
* **Live remote state** — What should be deployed
* **Live cloud resources** — what actually is deployed

We instantly surface the issues that break production:

* Drift and state mismatches
* Threat vectors and misconfigurations
* Hidden blast radius and downstream risk
* Cost anomalies and compliance violations
* Cross-PR conflicts for resource modifications

Everything happens as soon as the PR opens, before any CI/CD workflow triggers, and serves as an early detection system for hidden risks and issues that might enter your production environment.

# **Traction**

We're working with platform engineering and DevOps teams at SupportLogic, LaminatedLabs, and others who are catching issues they would have missed and deploying with confidence rather than crossing their fingers.

"Terracotta has helped my DevOps team ship Terraform faster and with more clarity. It catches cost impacts, exposed secrets, potential threat vectors, and even cross-PR conflicts before we trigger our CI/CD pipelines. It's been a huge win for both speed and compliance and an overall boost in confidence in helping manage Terraform across all our environments." - **Tyler Pinckard - Head of Software Engineering, DevOps & Security at SupportLogic**

**SupportLogic Case study:** https://tryterracotta.com/case-study/supportlogic

# **Our ask**

If your team is tired of Terraform, OpenTofu, and CDK-TF surprises in production, let's show you a 15-minute demo or sign up for a free 14 day trial at https://tryterracotta.com.

Email us: [founders@tryterracotta.com](mailto:founders@tryterracotta.com)

## OpsBerry AI - Secure your identity sprawl

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/926203d7-e2a0-45cd-b97b-d38419a524b4)

**TL; DR** —[OpsBerry AI](https://d2lssd04.na1.hs-sales-engage.com/Ctc/ZW+23284/d2LsSd04/Jks2-6qcW69sMD-6lZ3lyVmsNqH4X0sgdW5TPVYB7bLMr0W6gCpW-7YVgsNW1bvyKV6VTFTXVcRKMB84G-_WW68Bq2C90_lXpW6_BGLs6C_-0yW4lQkxg4FflCWW8rtXpw1ppdmgW2NfKVX6P8tfhW5nXNYm10nsb3W4lyMqq6LVSVZV_cQzJ8LnY0rW5Vt27w62FFv5W2Q4pWc4Z67KLW3kFQKk6ZC34bW68q3RQ3jfwPVW1ztCL98bbKldW685KMM36rzGDW8SMnJ02zDZD_f5nZ8xj04) is an Identity Security Posture Management Platform that uses AI trained with the latest cybersecurity and compliance frameworks to help organizations proactively control, secure, and defend their human and non-human identity sprawl against identity-driven attacks. We help security and engineering teams quickly unify, analyze, and remediate critical vulnerabilities in their identity sprawl into a single pane of glass across central cloud, identity, and ZeroTrust providers.

# **The team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/f8edf5e2-f5ee-4acb-8df8-3284f47601f0)

[**Carlos**](https://www.linkedin.com/in/carlosfelicianoii/) is the company's CEO. He handles the business end, infrastructure, security, architecture, and technical operations. He has over 15 years of experience in Cloud infrastructure, architecture, and observability. Before Y Combinator, Carlos was Director of Solutions Architecture and technical customer success at [OpsRamp](https://opsramp.com), multi-cloud and hybrid observability, and ITSM (acq. by HPE), helping enterprises like Micron, Dolby, Epsilon, and others architect end-to-end observability across their multi-cloud environments. Before that, Carlos was an engineering and technical support manager for [LogDNA](https://mezmo.com) (YC S15).

[**Casey**](https://buildspace.so/) is the company's CTO. With over 16 years of experience architecting and shipping code for his business ventures, Casey started by building and selling Runescape bots when he was 12. This eventually led him into various software engineering roles at YC-backed startups like [Buildspace](https://buildspace.so) and Farmstead. Casey runs the product side of the house, handling UIUX design, software architecture, and development, and ultimately, shipping amazing enterprise code.

# **What is causing the rapid increase in identity-driven breaches and why?**

Identity security is often overlooked and underestimated, leaving organizations vulnerable to unauthorized access, data breaches, and compliance failures. User-based identities are steadily growing annually at a 30% rate, with most employees having two or more identities that allow access to critical business and engineering systems, which is only part of it. NHIs, or Non-Human identities (think OAuth apps, API keys, Service Accounts, etc.), are increasing even faster at 50%, or said otherwise, four or more NHIs per every employee.

In 2023 alone, 84% of organizations suffered at least one identity-based attack, which averaged $4.5 million in cost. The number of breaches has grown at a steady 50% yearly since 2020 (Source: ISDA). That's not all; unrealized fallout from these breaches after the fact tends to include legal repercussions, loss of customers, increased security costs, higher insurance premiums, reputational repair, loss of intellectual property, and more.

![](https://www.idtheftcenter.org/wp-content/uploads/2024/01/ITRC-DataBreachReport-2023-Infographic-H-1024x791.jpg.webp)

User identities are only one attack vector in your identity security posture; machine-based identities like API keys, OAuth apps, service identities, and other NHIs are critical attack vectors for businesses. Partially offboarded identities, orphaned human and non-human identities, identity privilege creep, overprivileged access, and shadow accounts that fly under the radar, like non-sso access, gen-AI tools, and other IT internal systems, eventually snowball out of control and exponentially increase the potential for identity-driven breaches across critical engineering and business environments.

For businesses struggling to maintain compliance and adhere to regulatory requirements, these unchecked identity issues lead to significant compliance and regulatory problems. Organizations face increased risks of failing audits, substantial fines, and even reputational damage due to their inability to manage and secure their identity sprawl effectively.

# **How does OpsBerry solve this with AI?**

OpsBerry AI defends against human and non-human identity breaches using AI to continuously discover, prioritize, and remediate vulnerabilities and risks in your identity sprawl. Our AI-powered identity security posture management platform, trained with popular cyber security and compliance frameworks, provides comprehensive visibility and contextualization across your user accounts, service accounts, API keys, OAuth apps, and more, keeping your organization safe from identity-driven attacks.

# **How it works**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/41846940-aa9e-44ae-948b-39ed31b48d7a)

👀 **Automated Identity risk assessments**—We automatically gather all information about each identity and generate in-depth risk assessments with AI, instantly surfacing gaps, vulnerabilities, and threats.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/019721bf-ba26-4e5d-abd6-af44511dabae)

👥 **Shadow identities**—let AI surface the identities that hide in the shadows and quickly identify “unknown unknown” identity risks in your identity secure posture. Quickly surface and remediate shadow accounts across human and non-human identities, such as non-sso user accounts, API Keys and tokens, service accounts, orphaned identities, unmonitored privileged accounts, and more. This is the quickest way to transform hidden risks into strategic cost savings.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/ecaaaa23-83bd-40d6-9f1e-d2c3a169e380)

**🌱 Lifecycle management and remediation** are the easiest ways to control and secure your human and non-human identity posture. Drop-and-drop no-code automation lets you build streamlined self-service workflows to quickly onboard and offboard identities, remediate risks, and defend against identity-driven breaches.

And much more in the works!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/968ba4e4-c7d3-4379-b992-3f6781f46563)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/dda6bfd7-7e40-42e1-aca1-1c14c25ec780)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82694&key=user_uploads/925045/119b7479-a979-48a4-ac8b-2d3b7c3a0fb0)

# **Our ask**

Need help wrangle your identity sprawl with an identity security platform that’s like having your very own in-house identity security expert? We’d love to work with you!

Regardless of your company size, industry, or role, if you’re serious about protecting against identity breaches and want to take real control of your identity sprawl, we’d love to chat and show you a demo! Email [carlos@opsberry.ai,](mailto:carlos@opsberry.ai) or you can even set a time on our [Calendly](https://calendly.com/opsberry/opsberry).

# Socials

[OpsBerry AI (Y S23)](https://opsberry.ai)

[X](https://x.com/opsberryai)

[Linkedin](https://www.linkedin.com/company/opsberryai)
