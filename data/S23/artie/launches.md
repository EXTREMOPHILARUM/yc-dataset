# Launches

## 🐘 Artie for Enterprise - Data Replication at Petabyte Scale

# TL;DR

[Artie](https://www.artie.com/?utm_campaign=launch-week-q125&utm_source=yc-launch) streams data from databases to data warehouses in real-time and more reliably than traditional ETL solutions. Many companies are still running their ETL process every few hours, so their data warehouse is constantly out of date; with Artie, the data warehouse always has live production data.

Artie was founded to solve an enterprise data movement problem. Today, we’re launching Artie for Enterprise, for teams requiring high-volume, low-latency data replication that scales effortlessly. Whether dealing with massive volumes, strict security requirements, or mission-critical workloads, Artie ensures data is always live, accurate, and easy to manage. 🚀

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88730&key=user_uploads/89898/675b1398-6b54-40a0-888f-a3f4f487ffc3)

# Problem

Enterprises need real-time, reliable, and secure data replication—but existing solutions make this far more painful than it should be.

Traditional ETL pipelines often run on fixed schedules, updating data warehouses hours behind reality and leaving teams with outdated insights. Many replication tools try to brute-force data movement by running expensive, inefficient queries that **increase load on production databases**, slowing down applications and, in extreme cases, even **bringing them down entirely**. Scaling these systems across thousands of tables typically requires **manual, error-prone configurations**, forcing teams to spend countless hours debugging pipelines just to keep data flowing.

On top of that, many enterprises operate in highly regulated environments where data can’t be fully offloaded to the cloud. Traditional replication solutions struggle to support hybrid deployments, forcing teams to choose between security and ease-of-use.

# Artie for Enterprise provides reliable, secure, and high-volume data replication

### Terraform support

_“Um, we have thousands of tables to configure. Do I really need to click thousands of times on your dashboard to get connectors set up?”_ We hear this question a lot and our answer is “**Absolutely not”**, which is where our Terraform provider comes in. 

Just because your data volume is high does not mean management needs to be equally complex. No more endless clicks—just code it, deploy it, and go.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88730&key=user_uploads/1276059/ed2daad8-2763-4dfc-aaad-ea336ba4daf0)

### Multi-step merge

Merging large, frequently updated tables can be expensive and slow. We wanted to solve this problem without forcing customers to increase compute costs or scale up their virtual data warehouses.

With multi-step merge, Artie now loads data into a staging table in multiple bursts, allowing updates to accumulate before merging into the target table. This reduces latency and improves efficiency. Customers can now control how often data lands in the staging table before triggering a final merge—giving them real-time syncs with more flexibility and cost savings.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88730&key=user_uploads/1276059/0dcc6696-60c9-4ab8-a301-9764abbb5756)

### Hybrid deployment

Enterprise-grade replication means deployment flexibility is non-negotiable. There are many organizations out there that handle data containing sensitive information and are required to operate under strict regulations.

Our hybrid deployment model ensures the security of on-premise data processing with the ease of use of cloud services. What’s more? Artie’s fully-managed service allows for zero-maintenance, and removes the need to install and manage client-side agents.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88730&key=user_uploads/1276059/5464e25f-5c07-4bbc-8926-ea10fc6c48e1)

### MySQL Connector upgrade

We’ve made major improvements to our MySQL connector, making it enterprise-grade with improved performance, efficiency, and automation. These updates streamline database operations, reduce disk usage and I/O load, and automates data synchronization without complex configuration requirements and management overhead. 

Key improvements include full DDL and gh-ost migration support for seamless, non-disruptive schema changes, automatic fan-in for partitioned tables, and GTID support for reliable transaction replication.

### PostgreSQL CTID scanning

Backfills can be disruptive and resource-intensive. That’s why Artie is built to seamlessly recover from errors and avoid backfills unless absolutely necessary. 

However, in the event that backfills are required, how do we minimize disruption? Enter PostgreSQL CTID; an alternative backfill method that is **10-20x faster** than traditional methods.

### Datadog integration

At Artie, we’ve always been big on observability. What good are your data pipelines if nobody has visibility into them? We prioritize accurately monitoring your pipeline performance and making sure you know what’s up. 

With our Datadog integration, you can now track all Artie-exposed metrics directly from your Datadog dashboard. This allows you to **proactively monitor pipeline performance, set up custom alerts**, and build dashboards for deeper insights.

Stay on top of your data pipeline health—effortlessly.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88730&key=user_uploads/1276059/38889e0e-30ca-495f-b777-4af640e9aa3b)

# Curious to learn more?

Follow our journey on [LinkedIn](https://www.linkedin.com/company/artie-technologies), [X](https://x.com/artie_tech) and reach out to us [here](https://www.artie.com/contact?utm_campaign=launch-week-q125&utm_source=yc-launch) to see how you can benefit from enterprise-grade replication!

## Artie’s Analytics Portal - Real-time data pipeline observability

# TL;DR

[Artie](http://www.artie.so) is a real-time database replication solution. We leverage change data capture (CDC) and stream processing to perform data syncs in a more efficient way, which enables sub-minute latency and helps optimize compute costs. Today, we’re launching our Analytics Portal to provide visibility into our streaming pipelines and offer production-level monitoring for related system infrastructure out-of-the-box.

With the Analytics Portal, we hope to help alleviate some of the challenges that data teams face when running their data stack. By offering real-time observability into database pipelines and peripheral infrastructure, we hope companies can increase their understanding of how systems impact one another, reduce downtime/debug issues faster, and generate proactive alerts to maintain robust infrastructure. 

# **Visibility related to database replication is lacking**

The core of database replication is transferring data in a timely, accurate, and reliable manner. This is table stakes. In addition, there is a lot more happening in the peripheral, such as database monitoring, data pipeline visibility, data latency monitoring, and others. Data engineers need visibility to answer questions like: 

* How many rows have been synced in the past hour? How does that compare to the average/median/last month? 
* What is the data latency for our organization’s three most important tables? What are the factors that impact data latency and how are those metrics trending? 
* How are my systems performing?
  * Are there any database permission errors that may cause my data pipeline to go down? 
  * Are my databases sized correctly? How is CPU, memory, and storage utilization? 
  * Is my replication slot growing? By how much?

 

Setting up these metrics and monitors is important to help with debugging and maintaining a robust database replication solution. However, this requires expertise and domain knowledge that may not be accessible at every company. There is also no standardization of which metrics to track and what benchmarks to follow. To make matters worse, when it comes to adopting cloud solutions, database/pipeline visibility is severely limited. When pipelines break down, customers are often left in the dark, not knowing what broke, why it broke, and how to fix it. 

# **Artie’s Analytics Portal unlocks visibility & reduces MTTD**

We are extremely excited to announce our Analytics Portal to increase the visibility and observability of our streaming pipelines. This will provide insights into system-level infrastructure and help with monitoring database and pipeline health. When identifying and resolving issues, one of the most important metrics is to reduce MTTD (mean time to detection). With Artie’s streaming pipelines and periodic jobs like [Postgres Watcher](https://docs.artie.so/real-time-sources/postgresql#postgresql-watcher), metrics are being sent to our Analytics Portal in flight, as the underlying data is still being processed. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=76461&key=user_uploads/1276059/f4fe85ba-5ced-4892-9653-ed030638826d)

With the first iteration of our Analytics Portal, we are providing industry-standard telemetry to streaming pipelines and related infrastructure. Data teams will be able to observe the following: 

* Data ingestion latency by table and database/deployment
* Operation distribution by table and database/deployment
* Rows synced by table and database/deployment
* Database monitors that are related to and can impact pipeline performance: 
  * Permission errors that may interfere with data replication
  * Replication slot size
  * Free disk space\*
  * CPU utilization\*
  * Memory and Disk I/O (input/output)\*
  * Average transaction time\*
  * Existence of long-running queries\*

\*coming soon

# Production level monitoring out-of-the-box

The Analytics Portal initially comes with a set of pre-built charts and monitors. Customers are able to drill down to get deployment, database, and table-level statistics.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=76461&key=user_uploads/1276059/bcbbd68a-9808-48c5-92e5-1f61b53f9d86)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=76461&key=user_uploads/1276059/b5ec3d58-4f94-4af0-89d3-14ab920b2003)

The pre-built monitors that we are launching with include alerts for database permission errors and replication slot growth (for Postgres users). Over time, we will add alerting for the other monitors we mentioned above and more. This enables customers to have production-level monitoring set up out-of-the-box for their business-critical data. 

For example, an e-commerce company might be watching its `online transactions` table closely during the holidays. Let’s say they observe data ingestion latency going up for `online transactions`. They zoom out and realize it’s not just the `online transactions` table that is experiencing higher latency, but all tables under their Postgres connector are impacted and very few rows have been synced in the past 5 minutes. To troubleshoot this, they look over to the database monitors and realize their database’s replication slot has been growing and the culprit is a long-running query that has locked the table and is preventing Postgres from advancing the replication slot. After a quick Slack message to their internal DevOps team, the query is killed and the issue is resolved. 

# Making the Analytics Portal more actionable & customizable over time

Over time, we will make the data more actionable and customizable. In the near future, we plan to enable row-based monitoring such that customers can monitor custom business logic. In addition to the pre-built charts and monitors that we provide out-of-the-box, we want to allow customers to create custom charts and configure views based on metrics that matter to their business. 

For example, say you are working at a Fintech company that wants to monitor live transactions to detect fraud and abuse on your platform. You have a `transactions` table and this table is being synced to your Snowflake instance. You should be able to generate a chart to plot the average, median, p95, and max transaction sizes across various lookback periods (30 minutes, 1 hour, 24 hours, 7 days, etc). Then you can set up business logic monitors such as:

* Flag transactions that are 1.5 standard deviations above average coming from a merchant who signed up on the platform less than one week ago
* Flag key accounts where transaction volume has increased above or fallen below a certain threshold in the past hour

![uploaded image](https://www.ycombinator.com/media/?type=post&id=76461&key=user_uploads/1276059/1a22097c-f925-43c4-9fac-c5bf5035b55d)

Depending on how you’d like to be notified, Artie plans to support the following escalation channels:

* Email
* Slack
* Webhooks

In this example, the escalation channel is a webhook to your API server so you can then run a more rigorous machine-learning fraud model against a particular merchant account or transaction.

# **Contact us at **[**hi@artie.so**](http://www.artie.so)** to learn more!**

## Artie - real-time data streaming for databases ⚡

# _TL;DR_

_Artie is an open-source, streaming version of Fivetran - we transfer data from databases to data warehouses in real-time. Setting up a connector takes minutes and Artie leverages change data capture (CDC) to help companies reduce their data warehouse costs by 50%! We enable organizations to unlock real-time insights for better decision making. _[_Star us on GitHub_](https://github.com/artie-labs/transfer)_!_

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72536&key=user_uploads/1276059/60958f68-f519-4d78-bb98-c2c33974cb39)

Hi everyone, we are Jacqueline and Robin and we’re the team behind [Artie](https://www.artie.so/?utm_source=YC&utm_medium=newsletter&utm_campaign=launchYC&utm_id=launchYC). We’re on a mission to eliminate data latency and make it easy for every company to enable real-time data streaming!

Data is typically synced from production databases to the data warehouse once every X hour(s)/day(s) - this is a constraint that companies have lived with for decades. Robin personally felt the pain of not having access to production data in real-time and there were no easy to use out-of-the-box solutions, so we decided to build one! 

# **❌ The Problem**

Does your company sync data to the data warehouse every 6 hours, or worse, once a day? Are your analytics always lagged and filled with stale insights? **Why settle for a data platform that’s barely good enough when you can have real time data AND reduce your data warehouse costs?!** Not to mention you can have Artie set up in minutes!

Traditional ETLs are based on **batched processes** that operate on a cron schedule (DAGs, Airflow) and **cannot achieve real-time data syncs**.

Building and managing streaming data pipelines is hard. Most companies have a small team of data engineers and they often spend all day maintaining their data pipelines, which is not productive.

Factors companies should consider if they want to self-manage pipelines:

* Can the solution scale to multiple different data sources?
  * How easy is it to add new data sources?
  * How easy is it to manage across all the data sources?
* Can the solution scale to handle 1m+ queries per second?
  * Is the solution horizontally scalable?
  * Do workers require coordination? Or are they stateless and distributed?
* How do you ensure there are no out of order or missing events (even when the system crashes)?
* Can the solution handle schema evolution without creating breaking changes downstream?

# **🎉 Solution**

Artie leverages change data capture (CDC) and stream processing to achieve **sub-minute data latency (\~typically 10-20 seconds)**. Since we **only transfer changed data**, Artie is more efficient than traditional ETLs and can help you **cut down on your data warehouse cost by 50%!**

Setting up a connector requires no programming. Just follow the setup guide and deploy in minutes! After the initial snapshot, any changes in your database will be reflected in your data warehouse in real-time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72536&key=user_uploads/1276059/879c552d-7c8a-402e-9378-56f55380308a)

# **🎯 Who Needs Artie?**

**Engineers** that are exhausted stitching together Airflow + AWS Glue + Apache Spark + AWS Kinesis/Kafka + Apache Flink 😵‍💫

**Companies that are using traditional ETLs or batched processes**. Once you enable real-time, there is no going back (your data engineers/BI analysts won’t let you)! Think of all the previously unattainable use cases that you can now implement without data latency.

**Companies that have a cost cutting initiative.** Adopt Artie’s CDC streaming capabilities to reduce your data warehouse costs!

# **🙏 Ask**

Email [hi@artie.so](mailto:hi@artie.so) or sign up [here](https://artie.so/contact?utm_source=YC&utm_medium=newsletter&utm_campaign=launchYC&utm_id=launchYC) to try Artie today! 

Want to use open source? Install Artie at <https://github.com/artie-labs/transfer> (give us a ⭐!) and ping us on [Slack](http://artie.so/slack?utm_source=YC&utm_medium=newsletter&utm_campaign=launchYC&utm_id=launchYC), we’re happy to help you get started.
