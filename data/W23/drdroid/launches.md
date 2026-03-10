# Launches

## AlertOps Slack Bot by Doctor Droid — Identify poorly configured and noisy alerts

Hello everyone! At [Doctor Droid](https://drdroid.io/), we’re launching AlertOps Bot today.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/26f4c64e-4079-4ed5-8085-4d03726a9035)

**TL;DR** Add the bot to a channel and instantly receive reports about poorly configured and noisy alerts in the channel over the last 1 month / 3 months / 6 months. [**Signup URL.**](https://drdroid.io/)

**Context:** We built this tool for engineering teams that are too busy, have a bit of alert fatigue, and want to reduce the noise.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/c433733b-d223-49dc-8437-f04e97e79c8c)

Today, doing it requires manual time and energy.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/ab732135-c51b-496b-95db-3eefbab32e7b)

We have designed the bot such that the entire analysis now is presented to the engineers in seconds after adding the #Slack Bot.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/3b676a72-3eae-444c-a025-6d9209b9c4e2)

The bot provides immediate analysis of noisy alerts and insights around alerts that buzz too often.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/7028dd5e-2937-48da-b729-ab5b41aaf466)

We also extract other key tags from the strings. (like service_names, db_name, etc.). This helps do faster drill-downs of noise.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/e837fc17-e5d4-4bf6-9648-6482dfe1b809)

Our users include engineering teams at startups of all sizes and scales — from seed stage to unicorns.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/2ed51997-a5b2-40d0-a930-ad20c09721c8)

To get started, just [**sign up** on our](https://drdroid.io/) website and install the bot.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78159&key=user_uploads/1073547/c2206d71-88f5-40d4-a38c-fc6a4203d9e0)

If you have any specific comments or feedback to share, just let us know! ([**founders@drdroid.io**](mailto:founders@drdroid.io))

## Doctor Droid: Proactively detect issues before it impacts your customers

Hello everyone, Sid & Dipesh here from Doctor Droid!

Tl;dr: We help engineers track complex backend workflows that cannot be seen with just a single trace. Our stateful alerting system proactively looks for “missing states”, which means you’ll be alerted even when a certain task or event does not take place.

### Our Story

Dipesh & I are tinkerers who love to build products, and build them fast. Dipesh made a game one weekend that snowballed, and [then got acquired](https://www.linkedin.com/pulse/us-based-gaming-company-acquires-wordhurdle-dipesh-mittal/). I made a [volunteering website during COVID](https://mgiep.unesco.org/article/india-covidsos-online-volunteer-platform-wins-un-solidarity-award) to enable people to help others in their neighbourhood. These are apart from our full-time jobs, building products at Shadowfax - India’s leading last-mile delivery startup.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69760&key=user_uploads/1073547/55de2e46-57ef-4d85-97d3-6df1c76a3562)

As engineers, we were used to being called on-call when something broke, even though most of the times it wasn’t our code that actually caused the issue.

### **_The Problem_**

We had multiple critical products where monitoring the functioning of these products was not just about APIs because:

* A business use-case, when scattered across different APIs and batch processes, simply can't be connected together and viewed as a single flow to help find the leakage point
* You can only query and search over events/logs as individual data points, so I can't setup monitoring over deviations from my planned path for the user or an algorithm
* You cannot see a miniature / filtered version of your business behaviour and see irregularities in real-time
* The more properties you add in your events, the costlier storing and querying that data becomes

With Doctor Droid, we are making it super easy to detect and troubleshoot these complex products.

### **_How Doctor Droid Helps:_**

Doctor Droid gives you real-time visibility of how your products are performing, so you know where to intervene:

* **Workflow visualisation** of the critical product paths - easily detect steps of failure and monitor the data passing at each step
* Setup **stateful alerts** that span across multiple events
* Create **custom metrics** using the attributes directly or as an expression (without cardinality constraints)
* **Investigate** issues at a order, transaction or user level
* Setup automated actions (JIRA ticket, custom scripts) for known issues

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69760&key=user_uploads/1073547/9a0c9d88-f144-4b7b-b056-0337bf0145bd)

We have a simple SDK to ingest events (similar to your logging library), our documentation is available [here.](https://docs.drdroid.io/v2.0/docs)

### **_Try now -_** We are in private beta and are giving 100k events/month complimentary for first 100 beta sign ups (apart from personalised support to help detect issues faster for your business). Request access on our website to access our product or write to us at [founders@drdroid.io](mailto:founders@drdroid.io)
