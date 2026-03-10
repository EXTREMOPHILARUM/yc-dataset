# Launches

## 🏰 Fortress – Manage isolated customer databases in your own cloud

**TL;DR: 🏰** [Fortress](https://fortress.build) is an orchestration platform for SaaS applications, allowing them to easily manage a multi-instance database architecture (a hybrid of dedicated and shared instances) in **their own cloud**. 

If you are a SaaS using (or migrating to) AWS/GCP/Azure for databases, [**_schedule a meeting!_**](https://calendly.com/david-fortress/30min)

# **🚩 Problem:**

As a SaaS grows, they follow these two trends:

1. They mature off 3rd party managed database platforms and move into their own cloud (onto an AWS/GCP/Azure) for cost, latency, and more control of their data.
2. They move from a single shared database architecture to a multi-instance database architecture for performance, compliance, and due to data isolation requirements of enterprise.

These result in headaches for SaaS startups.

Existing cloud-native database services not only have complex docs and SDKs, but orchestrating separate database instances requires additional DevOps: deployments, schema migrations, connection pooling, versioning across instances, etc.

# **🏰 Introducing… Fortress**

A database orchestrator that simplifies DevOps of managing a multi-instance database architecture on your private cloud. 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeM89ZIOfe5fzfqrvvZR8QZeJT4VFxf-l8RkWKi2xhFmmA4xXoQv4Am8mqR_VJX0hZJEpkA0r_ThT4KFt5Fiyzp5QIJmgX0QmhytMyXt0Y58WePtvdi8-KCypPNLxQCOi1JvWuYpHkkNoAxOrJohjYBDDfF?key=9YIQrtfvHKcEq_yzYYr_RQ)

* **☁️ In your own cloud:** Host your database instances in your own cloud for security and reduced vendor lock-in (and use your cloud credits!). _We also have a fully-managed service!_
* **🛠️ Simplified DevOps**: Global schema migrations and rollbacks, versioning, and managed connection routing
* **👥 Tenant Management**: APIs/SDKs to support easy provisioning of a dedicated instance for larger enterprise clients and easily add smaller clients to shared instances. 
* **✨ Developer-friendliness:** Easy-to-use client SDKs and ORM integrations. CLI and UI for admin.
* **🚀 Flexible Deployment**: Deploy the database instance closer to your customer or to a specific region for compliance or reduced latency. 
* **🔒 Security**: Managed network isolation, custom Role-based Access Control for each database, encryption in transit and at rest, by default, simplified compliance audits, and easy tenant data deletion.
* **🧤 White glove migration**: For now, we will do white glove migration to our platform (it’s fairly simple if you already use AWS/Azure/GCP for databases)

 

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXft6jhnrN1J9uZE177D6tv2SI0qcWg1GNRv2kkBnAiGjzXjr_wYgsDvYDVzL1OpdiNM1tV8DdMiGw186fGzUJnAk8fUk_wd1dijEkE6WL2Vf6XrbVsEh90LhdZz_5-Y6wvd0v8wVLmjpMj8UsphUgPP-GrQ?key=9YIQrtfvHKcEq_yzYYr_RQ)

_Easily manage tenants, see their estimated usage, and what databases their data is in_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd9unp3fr994hjsN-JNeqKPVClbgUW4L_f0YU7rMk-OWVi54qo59PsYegIvfiEPGWgo6V-_8Sv1IlC-qr-S-PLZFNdmR7SnnnqnqB3eylgHOTVDJg8DGXlcPptDBsCC20KUNvw0JTlaWD9giMIYaGFI6ok?key=9YIQrtfvHKcEq_yzYYr_RQ)

_Group databases by schemas to propagate schema migrations across groups (we handle rollbacks)_

# **🌟 Future plans?**

* Schema Branching (branch current schema states and or freeze them for development)
* Zero-downtime schema migrations
* Experimental: Storage-compute separation to allow scaling to near 0 with Postgres **in your own cloud**

# ❓ **Ask:**

1. If you work with customers who require dedicated db instances, chat with us! We'd like to learn more about your experiences with DevOps.
2. Let us know if you know any CIOs and CISOs! Would love to [chat](https://calendly.com/david-fortress/30min)! 
3. [Try our early access?](https://calendly.com/david-fortress/30min) We are easy to set up if you use a cloud-native managed service!

## **🙌 The Team: Recent Brown CS grads + open-source wiz.**

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXctX4mvcWdjP5D92rRncPsy8x0jSPrWal_YVuVfT18YYBP49Ab3z3wHex33NUj1alZgm2ZQcA8tl0-9S_cdVttkbRp_12gQX-PG7kGLM4SBgFmnG_uF6XypCC-bn8vyunrVzj0Wee2lUkyoI68qWI7Xx61L?key=9YIQrtfvHKcEq_yzYYr_RQ)

[John](https://www.linkedin.com/in/john-finberg) + [Will](https://www.linkedin.com/in/willothy/) have been building software since 14

John + [David](https://www.linkedin.com/in/dchu17/) were CS buddies @ Brown
