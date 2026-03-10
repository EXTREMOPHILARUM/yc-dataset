# Launches

## SigNoz - Open source alternative to DataDog, New Relic

Hey folks 👋

We are thrilled to share SigNoz with the YC community today!

[SigNoz](https://signoz.io?utm_source=launchYC&utm_medium=homepage) is an open source alternative to DataDog, New Relic which helps developers monitor their applications, trouble shoot problems and get proactive alerts

We have quite an active dev community with **11,000+** github stars, **1800+** members in our slack community and **80+** contributors across our repos.

**😫 Problem**

* Engineering teams are frustrated with using different tools for different telemetry signals like metrics, traces and logs. Correlating across different tools is super critical for teams to get value out of their telemetry data and solve issues faster.
* Using proprietary vendor instrumentation code, locks you in to a vendor as it is difficult to change your instrumentation at a later stage.
* Sending all data to vendor cloud may have privacy and security concerns for some users esp. who have customer PII data or have to maintain a tighter security posture

**🚀 Why SigNoz?**

1. Single pane of glass for metrics, traces and logs in a single application. Ability to correlate across different telemetry signals very easily.
2. Natively based on [OpenTelemetry](https://opentelemetry.io) - and emerging open source standard for instrumentation and telemetry collection.
3. Uses OLAP datastore (ClickHouse) which makes aggregation queries 10x faster compared to traditional DBs. \
   More than 50-60% of observability related queries are aggregation queries like group by, sum, count where users want to aggregate their data
4. Can be self hosted easily. Keep all observability data in your own cloud.

💻 **Demo**

Here’s a quick demo of the product

[Demo Video](https://youtu.be/Tl3Cz8tz4R8)

💪 **Logs Performance Benchmark**

We also published a performance benchmark recently on how SigNoz logs product performs compared to other open source logs solutions like Elastic

[https://signoz.io/blog/logs-performance-benchmark/](https://signoz.io/blog/logs-performance-benchmark/?utm_source=launchYC&utm_medium=logs-benchmark)\
\
**🙏 Asks**

Try out SigNoz and share your feedback on how it can be improved. Here’s our github repo - <https://github.com/signoz/signoz>

Have any questions? Join our [slack community](https://signoz.io/slack?utm_source=launchYC&utm_medium=slack-community) and drop a note

😎 **What do we do for fun?**

We are a lean team constantly re-imagining the future of observability. Here’s a picture of our team from a recent workation at Goa

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68621&key=user_uploads/95650/4a4d8bd7-7975-4e43-bc1e-394c7859d63d)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68621&key=user_uploads/95650/02c70ae9-d6a7-4fc3-97d5-5edd635dc5b9)
