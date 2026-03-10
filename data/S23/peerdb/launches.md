# Launches

## PeerDB - Modern ETL in minutes, with SQL

## **TL;DR**

PeerDB is a Postgres-compatible SQL interface to seamlessly integrate multiple data stores. It enables data engineers to sync, transform and query data across their stores using simple SQL commands. PeerDB takes a data store native approach in engineering — enabling 10x faster ETL/ELT.

## **Problem**

Existing ETL/ELT tools primarily focus on supporting a wide range of connectors at the expense of delivering high-quality ones. This becomes evident when your workloads need scale or have demanding feature requirements. While Sai was working at Microsoft, it was common to see large enterprise customers try out the existing ETL tools and fail – as the tools were not meeting performance and reliability SLAs or were lacking the required features. Customers spent significant time and resources to build and manage in-house data pipelines.

## **Our Solution**

### Data-store nativity at its core, enabling 10x faster ETL/ELT

PeerDB takes a data store-first approach to data movement. It supports highly adopted stores and implements multiple infrastructural and data store native optimizations – providing a blazing-fast and feature-rich ETL experience.

We are starting our journey by providing the world's best data integration/ETL experience for **PostgreSQL,** [one of most used and popular databases](https://db-engines.com/en/ranking_trend/system/PostgreSQL). For example, on Postgres we parallelize initial load for larger tables using CTID scans. This yields orders of magnitude speedups - Syncing 100s of GB reduces from days to minutes.

Our architecture is designed for real-time syncs, which enables 10x faster Change Data Capture with data freshness of a few seconds even at large throughputs (10k+ tps). For example, in a sync from Postgres to BigQuery or Snowflake, PeerDB is 10 times faster than other tools and provides <30s data-freshness guarantees.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72937&key=user_uploads/728174/dc134471-e0d0-48c5-bbda-6d2ec339c421)

### SQL as the ETL/ELT standard

The Postgres-compatible SQL layer for ETL makes the life of data engineers very easy. They can develop pipelines using a framework they are familiar with, without needing to deal with custom UIs and REST APIs. They can use [Postgres' 1000s of integrations](https://github.com/PeerDB-io/peerdb#postgres-compatible-sql-interface-to-do-etl) to build and manage ETL.

We extend Postgres' SQL grammar with a few new intuitive SQL commands to enable real-time data streaming across stores. As we evolve, we will make this grammar richer and the standard for ETL/ELT.

## **Our Asks**

If PostgreSQL is a critical component of your data stack and you are running into challenges moving data in and out of Postgres, reach out to us at [founders@peerdb.io](mailto:founders@peerdb.io) or join our waitlist at <http://peerdb.io/> We would love to collaborate!

Also check out PeerDB’s Open Source repo - <https://github.com/PeerDB-io/peerdb> (don’t hesitate to leave us a star!)

## **Finally, a bit about us**

We are Sai and Kaushik. We've been best buddies for the past 15 years now. We were roommates back in undergrad and actively collaborated since then. Now we have decided to start a business together! 🙂

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72937&key=user_uploads/728174/4795901c-d1ac-4e3e-b565-7113c9ef3ca0)

Prior to PeerDB, Sai worked at Microsoft leading Solutions Eng. for all PostgreSQL services on Azure. He was an early engineer at Citus Data (YC S11) and saw it through the Microsoft acquisition. Prior to PeerDB, Kaushik built operating systems and led data teams at Google, Safegraph and Palantir. He also represented India in ACM ICPC World Finals. With our diverse and complementary experiences, we are excited and confident to build the next-generation ETL/ELT!
