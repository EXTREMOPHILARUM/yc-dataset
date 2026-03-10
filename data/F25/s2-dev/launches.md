# Launches

## s2.dev: Streams as a cloud storage primitive

Hi everyone! We are [Shikhar](https://www.linkedin.com/in/shikhrr/), [Stephen](https://www.linkedin.com/in/stephen-balogh-078a4995/), and [Dwarak](https://www.linkedin.com/in/dwarakgovindparthiban/), the co-founders of [s2.dev](http://s2.dev). S2 is the S3 for streams.

https://www.youtube.com/watch?v=8-mUPf4P_8g

Many of the most important features in products we love are powered by streaming data, from frontend UIs that go _brrr_ with real-time updates, to backends that store and process massive event flows. But building these sorts of real-time systems is really hard.

We are turning streams into a cloud storage primitive – just like object storage did for static files.

S2 is a completely serverless datastore, offering unlimited streams and configurable (even bottomless) data retention. Streams can be appended to and followed in real-time, and since all writes are durable, you can also read from anywhere in a stream’s history, indexed by sequence number or timestamp.

We basically took the core abstraction of Kafka – [the log](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying) – gave it a URI, and brought it online with a dead simple API. And none of the bloat. 😀

https://www.youtube.com/watch?v=2a1OdJ9l78A

## Why we’re building S2

We built large-scale ML infra at Etsy and Meta, and always felt the lack of a system like S2. Serverless infra for data at rest has been seamless for a long time (S3 launched 20 years ago!) – but the ecosystem around streaming data, in comparison, felt stuck in the stone age.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95319&key=user_uploads/235940/72f8cb1e-a550-4458-b57b-d5936dc98191)

When we [first introduced S2](https://news.ycombinator.com/item?id=42480105), we thought it would be most attractive to people already using streaming platforms like Kafka – but we’ve found that it resonates much more with builders in areas where these systems are entirely absent, who end up cobbling together general-purpose stores like Postgres and Redis and run into their limits.

We stand out on dimensions that are completely off the map for legacy systems: like the ability to have an unlimited number of streams backed by object storage, and to make them directly accessible [over REST](https://s2.dev/docs/rest/records/overview). This means S2 streams can be used as a serverless, reliable alternative to custom WebSocket or SSE infra.

## S2 radically simplifies streaming

If you are dealing with a **high-cardinality of data sources** – for example, code execution sandboxes or IoT devices – S2 is for you. Streams can be instantly created on-demand. You don’t have to buffer or batch, just pipe into S2.

https://www.youtube.com/watch?v=wsFiwxv_RY0

We recently [supercharged](https://news.ycombinator.com/item?id=45310294) read scalability to handle massive fanouts. You can broadcast a **real-time feed** with S2 such as market data without building any infra – publishing is just a matter of POST-ing to a stream’s URL.

If you are building **agents**, a common pain is **syncing** progress between the backend and frontend, while also being able to replay history. A lot of these agent state management challenges become simple with S2.

## Try it out

We should talk if [s2.dev](http://s2.dev) resonates with you! You can [sign-up](https://s2.dev/sign-up) and follow the [quickstart](https://s2.dev/docs/quickstart) to start streaming in seconds with free credits.

There is a lot more we are cooking, including an ⭐ open source self-hostable S2 https://github.com/s2-streamstore/s2 ⭐

## Talk to us

**email**: [founders@s2.dev](mailto:founders@s2.dev)

**discord**: https://discord.gg/JfTWJ5xxZ6

**twitter**: https://x.com/s2_streamstore

**bluesky**: https://bsky.app/profile/s2.dev

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95319&key=user_uploads/89898/8c2da77e-e2c6-4bb6-bba6-9da0a09f87ef)
