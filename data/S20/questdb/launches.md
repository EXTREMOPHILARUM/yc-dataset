# Launches

## QuestDB - Purpose built database for financial market data

### TL;DR

[QuestDB Enterprise](https://questdb.io/enterprise) is now Generally Available. Everything from high-performance QuestDB Open Source, with advanced security and access features. Scale the globe with multi-primary writes and highly-available fault tolerance. Tiered storage and open formats, with Parquet files stored on Azure Blow or AWS S3.

[Try the QuestDB Live Demo](https://demo.questdb.io/) with billions of rows!

QuestDB Bring Your Own Cloud is now in Beta. We’ll announce GA in the coming months.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72748&key=user_uploads/432980/3963b213-4696-40ad-8e23-69cb912138d5)

### The Problem

Existing time-series databases lack performance and store data in their proprietary format, leading to vendor lock-in.

None is tailored for financial market data, which requires low-latency ingestion protocols, fast queries, and a dedicated set of features and functions.

### The Solution

**How does it work?**

QuestDB is built from scratch for time series and financial market data. The data is natively indexed by timestamp and partitioned by time. Queries are multi-threaded and heavily optimized, leveraging modern CPU instructions (SIMD). QuestDB's ingestion speed can reach up to 4M rows/sec per instance.

Vendor lock-in is avoided since historical data is automatically transformed into Parquet format and stored on Object Store. QuestDB Enterprise can query real-time data and historical data seamlessly.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72748&key=user_uploads/432980/d26f7093-036a-41f3-9775-b19dff3c3cba)

Features that make QuestDB the best fit for trading/crypto applications include:

* Data deduplication that does not slow down ingestion
* Materialized Views (can be cascaded and chained)
* Native financial functions (vwap, order book fills, spread, weighted mid price etc…)
* Data compression with ZFS and Parquet
* Arrays to store order books (coming soon!)
* Apache Arrow (ADBC) for data scientists (coming soon!)
* Supports Postgres Wire and InfluxDB Line Protocol

# Production Deployments & Flagship Customers

OKX, B3 Exchange, Aquis Exchange (SIX Exchange), Mizuho Bank, Nomura (Laser Digital), One Trading, Energetech, AsiaNext, Airtel, XRP Ledger, Airbus, ABL Space Systems, Welwing Capital, Norlys Energy Trading, Beeks Group
