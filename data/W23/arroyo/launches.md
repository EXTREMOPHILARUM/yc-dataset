# Launches

## Arroyo - Serverless stream processing

Hey everyone, we’re Micah and Jackson, and we’re building Arroyo. Arroyo is the easiest way to build powerful streaming ⚡️ data pipelines. Just connect your Kafka, then you can filter, aggregate, window, and join your event data in real time with sub-second results. We fully manage the infrastructure, autoscale with your data, and charge based on usage with no fixed costs.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69175&key=user_uploads/61370/f468f5b0-8088-4982-abd8-a45e143f02a8)

## **💥 The problem: real-time data processing is too hard.**

Many companies have adopted Kafka to collect and route their event data. But if they want to actually _do_ anything complex with that data, their options today are to use a complex solution like Flink or dump it in a data warehouse for batch processing.

## **⚡️ The solution**

After leading streaming teams at Lyft and Splunk, we’ve seen how critical real-time data can be. At Lyft this infrastructure was vital to the operation of the product, powering features like dynamic pricing, ETAs, safety, and fraud. We’re working to bring it to everyone by solving the hard infrastructure and UX problems of existing solutions.

It’s three steps to get started writing real-time queries:

1. Tell us how to connect and authenticate against your Kafka cluster
2. Configure the source and sink topics
3. Write SQL

From there, our system will compile your query into an efficient dataflow program that responds to events within milliseconds and pushes results to Kafka. We charge purely on usage (based on data in, query complexity, and window sizes) with no minimums. Our system automatically scales with your data volume, and there’s no need to manage clusters or provision fixed infrastructure.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69175&key=user_uploads/61370/8789103e-9032-4cf3-bc1e-3f9bcf03a026)

## **What can you use this for?**

* Compute real-time ML features
* Detect fraud and abuse as it happens
* Turn your daily analytics jobs into real-time queries
* Filter/redact/aggregate your logs before indexing, or turn them into metrics
* Reduce costs in your data warehouse by pre-aggregating before ingestion

## **The backstory**

Micah spent four years at Lyft and Splunk building streaming platforms on top of Apache Flink and Kubernetes. Teams shipped impactful features backed by that infrastructure, but it still wasn’t easy enough for non-experts to adopt. Users wanted the same UX they had for batch: just write SQL, don’t worry about operations, scale, or the nuances of the infra. But the underlying tech wasn’t good enough.

We started Arroyo because we believe this goal is now achievable, but it requires looking beyond existing technology like Flink. That’s why we’re building a new, cloud-native stream processing engine in Rust. We’ve designed it from the ground up for near-instant rescaling and recovery even with very large windows (something that can take hours with Flink!) by separating storage and compute. And by leveraging WASM for user-defined functions, we can run user code efficiently and securely.

## **Get in touch!**

If you use a stream processing system like Flink or Spark Streaming, or would like to make use of your event data in Kafka, we’d love to talk! We’re excited help you solve your real-time data problems or turn an existing batch workflow into a streaming pipeline. Reach us at [founders@arroyo.systems](mailto:founders@arroyo.systems).
