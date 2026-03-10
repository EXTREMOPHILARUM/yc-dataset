# Launches

## ReJot - Enterprise Synchronization Engine

Hey everyone, we're Wilco & Jan, co-founders of ReJot! We're building a sync engine that helps big companies share data across engineering teams. We increase developer velocity and, most of all, ensure companies are not forced onto Kafka when they don't actually need event streaming.

<https://www.youtube.com/watch?v=Ulxmwrp_N5Q>

# The Problem

Growing companies are forced to adopt micro-services as their desire to give engineering teams autonomy increases. The number one reported problem in this architecture paradigm is **data silos**. Silos create high coordination overhead when integrating data from other engineering teams, slowing down development and delaying product launches.

The industry has defaulted to event streaming platforms like Kafka to enable teams to share data asynchronously. As a result, enterprise software architectures are pushed into an event-driven model. However, events come with inherent complexity—they encode **something happening** rather than **something being** (i.e., state).

**We believe that events are used for no good reason other than the infrastructure forcing developers onto them.**

# Solution

ReJot is a **sync engine** that enables sharing data between back-end services without the need for APIs or event streaming. We break data silos without forcing a paradigm shift from state to events.

We do this in the following way:

* **Familiar Querying:** by syncing database-to-database, ReJot allows engineers to query data from other teams **directly from their own database**. Developers use what they know best: SQL queries.
* **Sharing Data:** We realize that internal database schemas are sacred, and they should never be public directly. ReJot provides strong **data-sharing primitives**, allowing data owners to control _what_ and _how_ data is shared. Simplicity is key—setting up data publications in ReJot is trivial.
* **Integration Flexibility:** Downstream teams don't necessarily need data in the same shape as the original source. SQL queries are used once more to transform the data to fit the integrating team's needs.
* **Data Catalog**: Integrating data is impossible without first understanding what data is available. Our system overview maps an enterprise's software architecture through its databases, allowing the user to explore and search schemas to uncover opportunities for deep integration between products.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88081&key=user_uploads/2356635/d80813fb-077e-4916-98f0-bae320ddd57c)

_\[This overview shows how accounts owned by the accounting team are made public and integrated into the banking database by means of the "Accounts Consumer" integration.\]_

# Launching Today

Today, we’re excited to launch the **open-source** Limited Access Preview of ReJot!

Our control plane doubles as a database catalog, providing a unified view of all data stores within your organization. Connect Postgres databases to document your system architecture.

In the coming weeks we'll be rolling out ReJot's synchronization functionality to select users. As we scale our infrastructure, more users will be onboarded.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88081&key=user_uploads/2356635/c2ee7761-283c-4064-af0e-44984f23320a)

# The Team

We met nearly 10 years ago in Amsterdam where we studied Computer Science together, and have been friends ever since.

* Wilco (CEO) worked as a software engineer on Adyen's banking infrastructure. During a period of high growth he worked on the internal ledgering system and a framework to sync bank account data throughout the company, which inspired ReJot. He also has a background in software maintainability research.
* Jan (CTO) was a data platform engineer for Adyen's big data platform. There, he managed infrastructure for 600+ ETL pipelines created by 50+ teams that produced hundreds of terabytes of data every week. Jan is a published AI researcher.

Through a shared passion of modern software technology and reducing complexity in enterprise systems we connected the dots to create ReJot's sync engine.

# The Ask

* _🔗_ Share this post! Do you know of any organizations struggling with their distributed architecture? Reach out to us at [founders@rejot.dev](mailto:founders@rejot.dev) —we’d love to help!
* ⭐️ Star us on [GitHub](https://github.com/rejot-dev/rejot), follow us on [X](https://x.com/rejotsync) & [LinkedIn](https://www.linkedin.com/company/rejot)
* 📧 Sign up for our [newsletter](https://rejot.dev/email-updates/)
* 🌐 Connect your databases & learn more: <https://rejot.dev>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88081&key=user_uploads/2356635/98e4ff65-8266-448c-a2c9-637da1065625)
