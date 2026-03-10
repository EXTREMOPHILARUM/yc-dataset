# Launches

## OpenMeter.io: Real-time and scalable OSS metering

[OpenMeter.io](http://OpenMeter.io) is an open-source real-time usage metering solution to power SaaS, Billing, and IoT use cases. OpenMeter can collect and meter millions of events per second. It integrates seamlessly with cloud infrastructure components, making it an ideal solution for DevTool, AI, and IoT applications with Usage-Based-Pricing (UBP) or event-driven analytics requirements.

Check out [OpenMeter on GitHub](https://github.com/openmeterio/openmeter)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72230&key=user_uploads/1163072/fb0d1720-b48f-4e25-bf33-03306006f9c7)

### **Why does it matter?**

As the PLG (Product-Led Growth) motion gains momentum and the macroeconomic landscape limits growth potential with seat-based pricing, many companies are adopting usage-based pricing models, requiring accurate metering. Looking ahead, it is expected that the majority of SaaS products will offer AI capabilities. To effectively cover costs and generate revenue, these companies must meter AI usage and attribute it to their customers.

[See common OpenMeter Use Cases](https://openmeter.io/use-cases?utm_source=newsletter&utm_medium=email&utm_campaign=yc)

### **The Metering Challenge**

Usage metering requires accurately processing **large volumes** of events in **real-time** to power billing use cases and modern data-intensive applications like DevTool, AI, and IoT.

It’s challenging for engineers to balance out scale, accuracy, latency, and cost as:

* [🎈](https://emojipedia.org/balloon/) Monitoring systems fall short in terms of accuracy and consistency necessary for billing
* 💸 Scaling databases to handle large volumes of writes and real-time queries can be expensive
* [⏳](https://emojipedia.org/hourglass-not-done/) Warehouses processing leads to stale usage data and longer feedback cycles
* [💼](https://emojipedia.org/briefcase/) Building out streaming aggregation requires experience in handling idempotency and failures

Companies need to extract usage data from various cloud infrastructure components (Kubernetes, AWS, etc.), vendors (OpenAI, Twilio, etc.), and hardware components to attribute metered usage to their customers.

### **The Solution: OpenMeter**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72230&key=user_uploads/1163072/c04f742b-747e-4490-b2b4-57f162d55f4b)

[Watch the demo video](https://www.loom.com/share/bc1cfa1b7ed94e65bd3a82f9f0334d04)

A real-time, open-source, and infrastructure-first metering solution that you can start quickly and grow with rapidly:

* **Real-time Metering**: Instant aggregations and queries
* **Scalable Ingestion**: Handles millions of usage events per second
* **Accurate**: Precise metering for billing and industry use-cases
* **Fault Tolerant**: Built-in idempotency, event backfills, and meter resets
* **Infrastructure plugins**: Usage ingestion plugins for Kubernetes, AWS, etc.
* **RevOps plugins**: Integrations for Billing (Stripe), CRM, and data warehouses

We aim to make OpenMeter the standard to collect and share usage across many solutions and providers.

[Check out OpenMeter on GitHub](https://github.com/openmeterio/openmeter)

### **About the Tech**

Under the hood, OpenMeter harnesses the power of Kafka to deliver billing-grade and scalable metering. Its idempotent event ingestion uses the CloudEvents specification managed under CNCF. The usage metering aggregations are configurable, which allows tracking specific event properties on various time windows. OpenMeter is available on GitHub (published under the Apache 2.0 Open Source license).

[Check out the OpenMeter Examples](https://github.com/openmeterio/openmeter/tree/main/examples)

### **Join the OSS Community**

* [Follow OpenMeter on GitHub](https://github.com/openmeterio/openmeter)
* [Check out the Roadmap](https://openmeter.io/?utm_source=newsletter&utm_medium=email&utm_campaign=yc#roadmap)
* [Contact Us](https://us10.list-manage.com/contact-form?u=c7d6a96403a0e5e19032ee885&form_id=fe04a7fc4851f8547cfee56763850e95)

OpenMeter is built with ❤️ by Tailfin and experience from Netflix, Banzai Cloud, and Stripe.

## Tailfin - Maximize revenue with usage-based pricing

B2B SaaS companies see up to 25% revenue increase by adopting usage-based or hybrid pricing models, but realizing this potential requires the right tools and insights. This is where [Tailfin](https://tailfin.cloud?utm_source=bookface&utm_medium=post&utm_campaign=launch1) has you covered.

This is Andras and Peter - coming from Stripe, Netflix, Banzai Cloud, and Cisco; we understand that unlocking the full revenue potential requires to:

* Identify revenue opportunities and forecast over-usage to start the sales cycle early
* Find customers ready to be converted to enterprise plans
* Forecast usage and revenue to price deals accordingly

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69167&key=user_uploads/112934/0aa156bf-ec1b-48b3-a713-639a51217424)

## 💸 The Challenge

With the rise of Product-Led-Growth (PLG), pay-as-you-go is becoming the dominant pricing model, but unfortunately, many SaaS companies miss out on revenue opportunities. For example, enterprise customers often underestimate their usage and pre-purchase too little credit, leaving you with the dilemma of offering your service for free or renegotiating the deal. Moreover, self-serve customers may outgrow their plans without you knowing, and customer success and support may not prioritize users according to their spending and future potential.

## 🐬 Our Solution

Tailfin is a monetization platform explicitly designed for usage-based pricing. We help businesses to maximize revenue by providing insights about customers and highlighting opportunities so your sales and customer success teams can be data-driven.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69167&key=user_uploads/112934/92610c86-d525-4e40-9e52-cf924668dcac)

Tailfin provides:

* Subscription predictions like detecting overage before it happens so you can outreach and start the sales process in time.
* Price simulations to calculate historical and future revenue based on usage and different pricing models.
* Accurate metering with high-frequency event aggregation; can include events such as API calls, disk storage usage, or other product-related actions that could result in charges.
* Real-time dashboard and APIs to extract usage and revenue data

## [🐋](https://emojipedia.org/whale/) Sign up

Don’t leave revenue on the table. Ask for a demo today:

<https://calendly.com/tailfin-cloud/founders>  or email me at [peter@tailfin.cloud](mailto:peter@tailfin.cloud)

[https://tailfin.cloud](https://tailfin.cloud/?utm_source=bookface&utm_medium=post&utm_campaign=launch1) 

Best,

Tailfin Founders, Andras & Peter
