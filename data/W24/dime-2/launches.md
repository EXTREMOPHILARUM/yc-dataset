# Launches

## ⚙️Dime: AI Data Engineer for Hardware Manufacturers

Hi 👋 We’re [Akash](https://www.linkedin.com/in/akashkumar2296/) and [Ashish](https://www.linkedin.com/in/ashish-bajaj1/), and we’re really excited to be launching [Dime](https://www.getdime.io/)!

Check out our [launch video](https://youtu.be/vO4smBwD-ow)!

**TL;DR**: [Dime](https://www.getdime.io/) enables manufacturers to utilize their telemetry data to anticipate and prevent equipment and hardware product failures. Our AI agent identifies patterns of key failure modes and builds ML models to prevent them.

# **What do we help?** 🤷‍♂️

Hardware manufacturers collect enormous amounts of data from their products and manufacturing lines—everything from customer feedback and operator logs to IoT sensor data, ERP records, and more. Manufacturing and Process Engineers tap into this data to root cause manufacturing and end-product failures. **So What’s the Problem?** ⚠️

Data Infra setup for Manufacturing and Process Engineers is a complex, time-consuming process. Here’s why:

1. **Cumbersome Data Collection:** Engineers need to gather massive volumes of real-time data from various sources and set up streaming pipelines
2. **Time-Consuming Data Preparation:** Parsing, transforming, and cleaning this data takes significant effort before any analysis can begin and must be done every time engineers run analyses.
3. **Complex Analysis Process:** Running relevant statistical and machine learning models requires specialized expertise, making it difficult to extract actionable insights quickly
4. **Difficult To Repeat:** Even after insights are gained, setting up a reliable production ML workflow is challenging, especially for those without data science or software engineering backgrounds

# **The Solution?** 🚀

**Dime's Data Studio** aggregates data across industrial systems and abstracts the infrastructure needed to reliably extract, transform, and use that data. Here are some potential use cases:

**Repair & Service Applications**

Hardware products generate tons of telemetry data in the field, which often gets stored in large warehouses. Retrieving and analyzing this data manually can be time-consuming, but with Dime, customers can set up automated workflows to spot issues as data streams in—no need for complex ETL pipelines. Dime’s custom models detect potential component failures and alert customers when repairs are due, helping products stay in customers' hands longer.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85508&key=user_uploads/1648308/f2d077fc-9948-467f-8787-75826373b671)

In this example, the user has numerous products streaming telemetry data to a Snowflake data warehouse. When these products come in for repairs, engineers often download the telemetry data and analyze it using tools like JMP or Excel, spotting patterns that help pinpoint specific component failures. Having identified these patterns, they wanted a way to automate the process to avoid manual analysis each time. With Dime, they can set up automated workflows effortlessly. Dime builds models based on patterns seen over hundreds of repairs and runs daily workflows to detect specific component anomalies, notifying the user instantly. This automation saves hours of diagnostic time and ensures faster, targeted repairs, reducing costs and downtime.

**Customer Feedback Escalation**

Hardware products often generate substantial customer feedback, like the classic "send to Apple” on your iPhone. This feedback typically lands in data warehouses, where product engineers must download it into Excel sheets and sift through it to identify areas for improvement. With Dime, workflows can be set up to automatically analyze all incoming customer feedback using LLMs, categorize it, and trigger the necessary escalation steps—ensuring faster action on critical issues.

**And more…**

# **About Us** 👥

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85508&key=user_uploads/1648308/c8ec332c-bd79-473e-8d83-3d2c1dd0db29)

We both grew up in Metro Detroit 🏎️ 🏎️ , so we’ve been surrounded by Manufacturing our whole lives. Akash spent almost every summer of his childhood at the factory where his dad worked and saw this problem firsthand. We became friends in high school and went to college together at the University of Michigan 〽️ .

After graduation, Akash pursued his Masters in AI/ML at Georgia Tech, where he was a research assistant to Dr. James Hayes, a pioneer in self-driving technology and staff scientist at Argo AI. Akash then spent four years as a Software Engineer on Snapchat’s AI Platform.

Ashish most recently led the Business Operations and Finance functions at a Series B company. Prior to that, he spent four years in Finance, first as an Investment Banker and then as an Investor at TPG.

**Our Asks** 🙏

Please connect us with any Hardware Manufacturers! We’d love to explore how Dime can elevate their workflows.

You can reach us at [founders@dimemanufacturing.com](mailto:founders@dimemanufacturing.com)

## ⚙️Dime: The operating system for factories

Hi 👋 We’re [Akash](https://www.linkedin.com/in/akashkumar2296/) and [Ashish](https://www.linkedin.com/in/ashish-bajaj1/), and we’re really excited to be launching [Dime](https://www.getdime.io/)!

**TL;DR:** Dime helps manufacturers manage their factories. Our customers use Dime to generate production plans and track their progress

**The Problem** ⚠️ - **Manufacturing processes have gotten increasingly complex and existing MRP systems haven’t kept up**

Manufacturers use Manufacturing Resource Planning (MRP) systems to manage factory workflows. These tools are the operational backbones of factories handling tasks such as taking in orders, ordering raw materials, scheduling production, and tracking inventory. However, existing platforms aren’t great due to a few key reasons:

1. Costly: Setting up an MRP requires significant upfront investment on consultants to configure modules that are only partially used
2. Rigid: Most MRPs enforce a fixed data schema, complicating the integration and management of external information. This necessitates expensive custom integrations to add data sources or alter data fields as business needs evolve
3. Inefficient: MRPs still require significant manual data entry and data extraction is dependent on inflexible reports that need additional processing for analysis

**The Solution** 👍

Dime is building a modern MRP, starting with automated production scheduling and inventory tracking.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79321&key=user_uploads/663445/6217060a-b611-4c43-92a0-a0a60db0ecf7)

Our production scheduler is schema-agnostic and takes order inputs from any format (PDF, CSV, EDI, etc.). It considers factory-specific capacity, setup, and labor constraints to automatically create an optimal schedule that tells plant managers which parts to create and when.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79321&key=user_uploads/663445/c172b269-b2de-42aa-a11d-024ae0aafb08)

Dime provides real-time updates on the production and shipment status of orders. Inventory can be traced from the production line, through quality control, and into the warehouse.

**The Team, The Team, The Team…** 〽️

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79321&key=user_uploads/663445/ecd6faf4-84d9-49a6-adb3-b5ffad452139)

We’re University of Michigan alumni and grew up in Metro Detroit 🚗🚗 , so we’ve been surrounded by Manufacturing our whole lives. Akash spent every summer of his childhood at the factory where his dad worked and saw firsthand how outdated manufacturing systems are.

After graduation, Akash pursued his Masters in AI/ML at Georgia Tech, where he was a research assistant to Dr. James Hayes, a pioneer in self-driving technology and staff scientist at Argo AI. Akash then spent four years as a Software Engineer on Snapchat’s AI Platform.

Ashish most recently led the Business Operations and Finance functions at Butler, a Series B company. Before that, he spent four years in Finance, first as an Investment Banker at Rothschild and then as an Investor at TPG.

**Our Ask**

1. If you are a manufacturer or know anyone who runs a manufacturing company, please visit our [website](https://getdime.io) and schedule a demo
2. If you have any feedback, reach out to us at [founders@dimemanufacturing.com](mailto:founders@dimemanufacturing.com)
