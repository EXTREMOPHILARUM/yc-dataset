# Launches

## Hydra: Serverless Realtime Analytics on Postgres

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88443&key=user_uploads/54309/fc2a33f3-1607-4213-bee9-7fb9693b0f5f)

**Hydra is Serverless Realtime Analytics on Postgres.**

By separating compute from storage, Hydra enables compute-isolated analytics and bottomless storage. It is designed for low latency applications built on time series and event data.

# [**Try Now! (free)**](https://start.hydra.so/get-started)

<https://youtu.be/mib8ehnMmC8>

# **Enable in seconds**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88443&key=user_uploads/54309/42f17c01-89e7-47ae-ba01-f76bc23c864e)

Set up is simple. To unlock serverless realtime analytics on Postgres, run:

```
pip install hydra-cli
```

For setup

```
hydra
```

1. fetch your hydra token, paste in to enable Hydra
2. create analytics schema / tables and insert data ([**quickstart docs**](https://docs.hydra.so/intro/quickstart))
3. _voila_ - run queries, get insights in milliseconds

# **Problem**

For decades, there’ve been two core problems with analytics on Postgres:

**Slow** - aggregates and complex queries can take minutes to return results from large data sets.

**Resource Contention** - Expensive analytics queries hog Postgres’ RAM / CPU resources and impair transactional performance. In other words, the entire app slows down, which makes users unhappy.

# **Solution**

### **Fast**

Hydra returns analytics queries 400X faster than standard Postgres. Hydra uses duckdb to perform isolated serverless processing on these tables in Postgres. In fact, Hydra is faster than most specialized analytics databases.

If you’re running AWS RDS, AWS Aurora, Heroku Postgres, Supabase, Fly Postgres, Render Postgres, GCP Cloud SQL, etc.. you can improve expensive analytics queries by 400X by using Hydra.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88443&key=user_uploads/54309/3fb7dc1e-622a-4303-ba7a-f729f18ab019)

fun fact: the Snowflake instance (128x4XL) in the benchmark is $100k / month.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88443&key=user_uploads/54309/5db5d184-2a69-4811-b14e-5ad433f4038c)

These are results from clickbench which represents a typical workload in the following areas: clickstream and traffic analysis, web analytics, machine-generated data, structured logs, and events data. The table consists of exactly 99 997 497 records — rather small by modern standards but allows tests to be performed in a reasonable time.

### **Isolated, serverless processing**

Using Hydra there is no impact on Postgres’ RAM / CPU resources when reading from or writing to an analytics tables.

As a result, here are more cool things Hydra can do: zero-copy clones for scaling read replicas, automatic caching, write isolation, bottomless storage with high data compression, and more.

# **How it works**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88443&key=user_uploads/54309/8d8999aa-a370-4f0f-9d99-badfe4621c97)

Hydra integrates duckdb execution and features with Postgres using [**pg_duckdb**](https://github.com/duckdb/pg_duckdb), an open-source project we co-developed with the creators of DuckDB.

**FAQ:**

yes, you can join between an analytic table and a standard row-based table.

yes, you can write (insert & update) to analytics tables.

yes, Hydra is identical to using standard postgres.

yes, data inserted into an analytics table is automatically converted into analytics-optimized columnar format.

tell Hydra you are creating an analytics table by including the ‘using duckdb’ keyword - that’s it.

# **Hydra is best for**

Hydra is both a row and columnstore, so you can use it for standard Postgres work, like multitenant apps, as well as analytical work, like monthly reporting. Here are several cool Hydra use cases that blend both transactional & analytics — more in our [**use case docs**](https://docs.hydra.so/guides/usecase).

* time series, logs, events, traces
* monitoring & telemetry
* financial services
* observability & metrics
* cybersecurity & fraud detection
* web & product analytics
* iot
* realtime ml / ai

# **ok, but why use postgres instead of … \[insert favorite tech\]?**

It’s true, there are many specialized analytics databases. reviewing the benchmark above, the majority of analytics databases are actually _slower_ than Hydra. Regardless, isolated analytics databases produce their own set of challenges and costs.

### **data pipelines (etl)**

Traditionally, an analytics database is isolated, and in most cases, engineers must set up data pipelines for data movement and transformation between Postgres, S3, and the analytics db. Pipelines aren’t cheap. Also, there’s pipeline latency bottlenecking how stale the analytics are. And when pipelines break — because they do — you’re stuck with downtime and wrong results.

Hydra side-steps the latency and costs of data pipelines entirely with full support for inserts and updates on columnar files in analytics tables.

### **overweight design**

Many use cases don’t justify a heavy setup. From our time working at Heroku, we saw many transactional apps that only need a couple high level aggregates and a few complex analytical queries to return quickly. Hardly OLAP (online analytical processing) and not really HTAP (hybrid transactional and analytical processing) - just apps in need of a speed boost.

The most heavyweight option, data warehouses like BigQuery, are good at “big queries”, but not great at smaller, rapid analytics queries that’re more common with applications, rather than monthly reporting.

These traditional approaches are too heavy, can be brittle, and introduce extra costs and latency your startup doesn’t need.

# **do we have a hosted cloud offering?**

Yes, and [it’s awesome](https://start.hydra.so/get-started).

# [**Try now!**](https://start.hydra.so/get-started)

## **useful links**

[**website**](https://www.hydra.so/), [**docs**](https://docs.hydra.so/overview), [**local dev guide**](https://docs.hydra.so/guides/local_development), [**analytics guide**](https://docs.hydra.so/guides/analytics), [**architecture**](https://docs.hydra.so/intro/architecture), [**changelog**](https://docs.hydra.so/changelog/changelog)

If you’ve made it this far here’s a pic of me (joe) and my cofounder (jd) in hood river, oregon. Building Hydra has been a wild ride, but we found a way to have fun.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88443&key=user_uploads/54309/69da46c2-bfc2-48c6-8ed3-2364e71c34fd)
