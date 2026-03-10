# Launches

## Lantern - Postgres vector database 🏮

Hi! We’re Di and Narek. We’re building [Lantern](https://lantern.dev).

## About Lantern

Lantern is a Postgres vector database that is easy to use, cost-effective, and scales to billions.

Anyone using a standalone vector database such as Pinecone has to maintain a separate database for their other application needs. This adds complexity. With Lantern, you can run vector search in the database you already know and love, Postgres. In addition, Lantern is [orders](https://lantern.dev/pricing) of magnitude cheaper than Pinecone.

We recently released [product quantization](https://lantern.dev/blog/pq). This enables index compression so the index can use up to 90% less memory and cost an additional 90% less!

We support [embedding generation](https://lantern.dev/docs/develop/generate) with Open AI, Cohere, and open-source embedding models inside the database for one-off queries. For bulk transactions and managed columns, we support generating up to 2 million embeddings per hour.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79083&key=user_uploads/343105/9ef30a0c-40fe-4de5-b6e7-a64c313ed329)

We also support [external index creation](https://lantern.dev/blog/hnsw-index-creation), which offloads index creation to external machines to avoid expensive index creation processes causing downtime in production databases.

## Get Started

The easiest way to get started is with [Lantern Cloud](https://lantern.dev), our managed Postgres service. To self-host or explore our source code, check out our [GitHub repo](http://github.com/lanterndata/lantern).

If you are currently using another vector database provider or another Postgres provider, we have tools to make migration seamless.

We have multiple customers using Lantern in production, and we’d love to have you give us a try too! We’re happy to answer any questions or help you get set up - reach out at [support@lantern.dev](mailto:support@lantern.dev) or on X at [@diqitally](https://twitter.com/diqitally).

![](https://lh7-us.googleusercontent.com/olpVbw9LdPqQvlae8m2tpV7bEcDzlwVIuv0laDX55L0r130wsYWkV-lGIcsCletv4I6zgYADCQ_sHmjWtMNZNpJlUkM_g7Z6TpkZJtCO54acRTUMNAyTuPF4HQfT9Na2YWXWzWx19l4_jl5zNikU-bE)

## About Us

Before Lantern, [Narek](https://linkedin.com/in/ngalstyan) was a PhD student in distributed systems at Berkeley and worked at Timescale, a billion-dollar Postgres company. [Di](https://www.linkedin.com/in/di-qi/) worked at Y Combinator as a software engineer, co-founded a YC-backed 15-minute delivery startup, and worked at Facebook Ads Ranking.
