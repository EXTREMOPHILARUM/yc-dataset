# Launches

## Matano - Open source SIEM alternative for AWS

**👋** Hi YC! We’re Samrose & Shaeq and we are excited to launch [Matano](https://github.com/matanolabs/matano).

### TL;DR

**Matano is a high-scale, low-cost, zero-ops alternative to traditional SIEM (e.g. Splunk) that deploys a security data lake directly in your AWS account.** It lets you ingest petabytes of security and log data from various sources, store and query them in an open [Apache Iceberg](https://iceberg.apache.org/) data lake, and create Python detections as code for realtime alerting. Matano is fully serverless and designed specifically for AWS.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68262&key=user_uploads/785948/5ec8b84a-df7a-44d1-914b-2c30af3dc2fa)

### **Problem**

* Traditional tools used to analyze security data (SIEMs) don’t scale, and are too expensive and difficult to manage for security teams on the cloud.
* Security data is now a Big Data problem: collecting data from your network, SaaS, and cloud environments can exceed 100TBs of data. Security teams are forced to either not collect some data, leave data unprocessed, or build an in-house data lake to cost-effectively analyze large datasets.
* At scale, without a strategy to normalize data into a structured format, it is difficult to correlate across data sources & build effective alerts that don’t create many false positives. Traditional SIEM query-based rules fail to accurately identify threats.

### **Our Solution**

We’re leveraging our years of experience at AWS in Big Data and cloud technologies to build a modern alternative to SIEM designed from the ground up for efficiency, scalability, cost effectivity, and vendor neutrality.

![](https://www.matano.dev/assets/images/diagram-09d3bbd00cb55ab585125b7a7ec452c6.webp)

* **Security Data Lake** Matano normalizes unstructured security logs into a structured realtime data lake in your AWS account. All data is stored in optimized Parquet files in S3 object storage for cost-effective retention & analysis at petabyte scale.
* **No vendor lock-in** Matano lets you truly own your own security data. Cybersecurity vendors lock your data in proprietary formats which make it very difficult to use outside of their product. With Matano, all your data is in open Apache Iceberg tables that can can be directly queried from different tools (AWS Athena, Snowflake, etc.) without having to copy any data.
* **Detection-as-code** Matano gives you the flexibility of Python to implement realtime alerting on your log data and introduce a development lifecycle to detection by managing rules in Git (test, code review, audit).
* **Serverless** ​​Matano is a fully serverless platform built entirely on technologies like Lambda, S3, and SQS and is designed for zero-ops and unlimited elastic horizontal scaling. Matano uses Rust for blazing fast performance [🦀](https://emojiterra.com/crab/).
* **Open source** Matano is licensed as Apache 2.0 and always will be. Matano uses an open table format (Apache Iceberg) and common schemas ([Elastic Common Schema](https://github.com/elastic/ecs)), to give you full ownership of your security data.

### **Ask**

* If you’re a security team interested in using Matano, feel free to reach out over email at [founders@matano.dev](mailto:founders@matano.dev).
* Try out our project and star [⭐](https://emojipedia.org/star/) us on GitHub: <https://github.com/matanolabs/matano>.
* Join our [Discord community](https://discord.gg/YSYfHMbfZQ)!
