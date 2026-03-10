# Launches

## PgDog: Scaling PostgreSQL

Hey YC,

I’m Lev and I invented time travel… for your database.

“Huh?”

**TLDR:** PgDog is a proxy for scaling PostgreSQL. It can load balance traffic and shard databases, without changes to app code or using database extensions. What does this have to do with time travel? Keep reading.

https://www.youtube.com/watch?v=trSVJel3gyc

# ❌ The Problem

Scaling Postgres is a full time job. Your app is writing data but the database can’t keep up. You’re adding more databases and thinking of breaking the app into services to spread the load.

PgDog is for you if:

* You had an outage caused by a bad query
* Your database is unpredictable; app latency and uptime are all over the place
* You know more about Postgres internals (like vacuum) than you’d like, and you just want it to work so you can go back to building your product

And you catch yourself day dreaming about the good old days, when you were pre-PMF and your DB was at 10% CPU.

# 👷 The Solution

Database problems should be solved at the database layer. PgDog is a load balancer, connection pooler, bouncer, and sharder. It speaks fluent SQL and understands every single Postgres query. It uses this knowledge to:

* Distribute queries between shards, horizontally scaling your relational database
* Load balance traffic between replicas
* Block or rewrite queries you don’t like, e.g. queries that forgot an index or are missing the customer_id and were about to leak data

With PgDog, your DB is young again and ready to grow 10x. Written in Rust, for security and performance, PgDog is fully tested and ready for production.

# 🙏 The Ask

If any of this sounds familiar, **get in touch!** I’m happy to come work for you to fix your DB. I’ll stay in the basement and make PgDog scale Postgres, while you work on your startup.

You’re my ideal design partner if:

* Postgres is your production database (naturally)
* Despite your troubles, you love it and want to do more with it
* You believe in first principles solutions to hard problems

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90596&key=user_uploads/989617/91f087f7-4175-47fe-9753-57ed4e9bda62)

Email [lev@pgdog.dev](mailto:lev@pgdog.dev), join our [Discord](https://discord.gg/CcBZkjSJdd), and give us a star on [GitHub](https://github.com/pgdogdev/pgdog). Everything we build is open source.

# 👬 The Team

I’m a second time technical founder (previously co-founded [PostgresML](https://github.com/postgresml/postgresml)) and started the Instacart storage infra team. I scaled 100TB+ databases when Instacart grew 5x in 3 months. This is my second pet-inspired project for scaling Postgres (have you heard of [pgcat](https://github.com/postgresml/pgcat)?)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90596&key=user_uploads/989617/86ff8181-b991-4bf9-bd05-8b0a387ed978)
