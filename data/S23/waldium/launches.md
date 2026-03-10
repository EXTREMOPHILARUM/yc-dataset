# Launches

## 📈 Structured - Single source of truth for key business metrics

### **The Problem: Inconsistent Metrics, Misaligned Decisions**

In the high-pressure world of growth and revenue, teams live or die by their data. Yet, too often, the very metrics that should guide decisions are inconsistent, poorly documented, or misunderstood across different teams. 

Imagine this: Your team is preparing for an important strategy meeting. They need to assess the impact of a new onboarding feature on user activation. Marketing has one definition of "activation," product has another, and sales uses a completely different set of metrics. Each team pulls data from the same warehouse – but interprets it differently, leading to conflicting reports and a confused leadership team. The result? This misalignment creates chaos, leading to conflicting reports, wasted resources, and missed revenue. Hours are wasted on reconciling data discrepancies instead of focusing on strategy, and missed opportunities to act on accurate insights.

But what if you could ensure that every team in your organization was always on the same page, with a single, accurate source of truth for all key metrics? What if your data was automatically documented, changes tracked, and alerts sent out when something significant changes? Enter Structured.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83717&key=user_uploads/1194855/8a5a8ddb-49b1-4d41-82f6-12ec24c16154)

### **The Solution: Structured Brings Clarity and Consistency**

Structured is designed to solve this exact problem. By integrating directly with your data warehouse (e.g., Snowflake, BigQuery) and your transformation tools (e.g., dbt), Structured automatically catalogs your data’s metadata and ensures that all metrics are consistently defined and documented across your organization.

1. **Connect Your Data Warehouse and dbt:**
   * Structured connects directly to your data warehouse—whether it’s Snowflake, BigQuery, Databricks, or Redshift—and integrates with dbt, the tool your data engineers already use to model and transform data.
   * The moment you connect, Structured starts cataloging your data, tracking every table, column, and transformation automatically.
2. **Auto-Generated Data Catalog and Documentation:**
   * Structured automatically generates a comprehensive data catalog, documenting every metric, entity, and relationship. AND—this documentation is instantly synced to Notion, a tool your business teams already know and love.
   * Now, whether you’re a data engineer or a revops analyst, you can easily access and understand how metrics are defined and where the data comes from. No more guessing, no more miscommunication—just clarity
3. **Summaries of Changes and Version History:**
   * Structured tracks every change made to your data models and metrics, automatically generating summaries that are easy to understand, even for non-technical users.
   * Every change is logged with version history, so you can see exactly how metrics have evolved over time. This means no more confusion over which version of a report to trust—everyone is working from the latest, most accurate data.
4. **Alerting on Metric Changes:**
   * Structured’s AI doesn’t just catalog your data—it monitors it over time. If a critical metric changes—say, your churn rate spikes or a key transformation in dbt is modified—Structured sends out alerts to the relevant teams to see what’s up
   * These alerts are designed to be easily understood by business users so everyone knows what’s happening and why it matters. This means faster, more informed decisions and no surprises in your strategy meetings.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83717&key=user_uploads/1194855/aeb49c87-18e9-4860-9bcb-04a54f96569b)

### **ROI: Real Results from Day One**

Structured delivers measurable value by:

* **50% Faster Reporting:** Teams can generate accurate reports in half the time, thanks to consistent, pre-documented metrics that are automatically synced to tools like Notion.
* **20% Reduction in Data Errors:** Structured reduces the risk of data discrepancies with automated metadata management and version tracking, ensuring that your reports are always based on the most accurate and up-to-date information.
* **30% Lower Operational Costs:** By automating the documentation and alignment of data, Structured reduces the manual effort required from your data teams, freeing them to focus on more strategic tasks.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83717&key=user_uploads/1194855/9751d79d-6c81-46c3-adb8-c9156653f0d6)

### **Get Started Today!**

Structured is here to help your teams make better decisions, faster. Visit [structuredlabs.com](http://structuredlabs.com) or reach out to Amrutha Gujjar: [amrutha@structuredlabs.com](mailto:amrutha@structuredlabs.com) to schedule a demo and see how Structured can help!

## ⭐ Structured - Semantic layer for reliable business metrics

Hello YC! We are Amrutha Gujjar and Shivam Singhal, the founders of Structured.

We’re excited to introduce **Structured**—a platform that helps businesses easily define, manage, and scale their most critical business metrics using a robust semantic layer.

### **The Problem**

In today’s data-driven world, businesses are increasingly relying on metrics to guide decision-making. However, we’ve seen countless organizations struggle with the inconsistency and complexity of defining and managing these metrics. Whether it’s “Revenue,” “Customer Acquisition Cost,” or “Churn Rate,” different teams within the same company often use different definitions, leading to misaligned decisions, wasted resources, and a lack of trust in the data.

Traditional BI tools fall short when it comes to ensuring that metrics are computed consistently across an organization. This problem is particularly acute in companies with large, complex datasets stored in cloud data warehouses like Google BigQuery. Maintaining consistency and governance over these metrics typically requires significant manual effort, deep technical expertise, and can lead to errors that compromise decision-making.

### **Scenario**

As the VP of Data at a rapidly scaling SaaS company, you're responsible for ensuring that the metrics used across the organization are accurate, consistent, and aligned. But despite your best efforts, discrepancies in critical metrics like Customer Acquisition Cost (CAC) and Monthly Recurring Revenue (MRR) continue to create challenges.

For example, your Marketing team reports a CAC of $130, calculated using data from HubSpot and Salesforce, where they focus on ad spend and campaign costs. They’re eager to demonstrate the efficiency of their campaigns, so they exclude overhead costs to present a leaner figure.

On the other hand, your Finance team calculates CAC at $210, pulling from NetSuite and incorporating a broader range of costs, including overhead and allocated expenses. Their approach is to capture the full financial impact, ensuring that nothing is overlooked.

Meanwhile, the Product team is responsible for tracking MRR, using data from Stripe. However, they include one-off setup fees in their MRR calculations, inflating the recurring revenue figure. When they report MRR as $1.2 million, you know the true recurring revenue is closer to $1 million when those fees are excluded.

These conflicting numbers lead to confusion and frustration at the executive level. The CEO asks for the real CAC and MRR to inform key strategic decisions, but the data from different teams doesn’t match up. You find yourself mediating between departments, trying to align definitions, and reconciling these differences. Your data team spends hours pulling reports, adjusting metrics, and validating numbers, just to arrive at a single source of truth.

This process isn’t just time-consuming; it’s draining your team’s resources and slowing down the decision-making process. The ongoing discrepancies and the manual effort required to resolve them create friction across departments, eroding trust in the data and undermining the confidence of the executive team in making data-driven decisions.

### **The Solution**

**Structured** is a powerful semantic layer that integrates directly with cloud data warehouses like Google BigQuery.

* **Onboarding and Setup**:
  * Your data team connects Structured to your Google BigQuery warehouse in one-click. 
  * **Define Standard Metrics**: Access a library of pre-built metric templates or create custom metrics tailored to your specific business needs. 
    * _Example_: Using Structured’s library, you define CAC and MRR with input from finance, marketing, and product. Everyone agrees on what costs are included in CAC and how MRR should be calculated.
    * Structured makes sure that these definitions are consistently applied across your organization.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73623&key=user_uploads/1194855/fe1a81fd-f235-4e41-9395-daeefe0b3daa)

* **Governance and Control**:
  * You assign ownership of these metrics to the finance team, but allow other departments to view and suggest changes. Structured’s version control means every change is tracked, so you can always revert if necessary.
  * Now, all departments are using the same metrics. When the CEO asks for the latest CAC and MRR, everyone is looking at the same, accurate numbers 
* **Proactive Alerts**: Structured’s AI-driven features monitor your metrics and flag any anomalies. For example, if CAC suddenly spikes, the platform can alert you before it becomes a bigger issue. These insights help you stay ahead of potential problems and make more informed decisions.
* **Data Request Tickets:** Structured offers an integrated ticketing system to manage data-related requests across your organization. Whether it's a request for a new metric, a data discrepancy, or additional analysis, your team can easily submit, track, and resolve these requests within the platform.
* **Knowledge Base**: Structured automatically generates documentation as an artifact of setting up and managing metrics. This documentation is a powerful, quick win for your data team, creating a shared reference point that everyone in the organization can trust. This instant clarity translates directly to business impact—empowering your teams to make aligned decisions faster.
* **ROI**:
  * Your team saves dozens of hours previously spent reconciling different versions of the same metric. Decisions are made faster and with more confidence.
  * By making data-driven adjustments to your customer acquisition strategies based on the standardized CAC, your company can focus on reducing the acquisition costs. The clarity around MRR helps optimize pricing strategies, contributing to increase in revenue.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73623&key=user_uploads/1194855/333b7409-baed-4975-ac28-e4d7a850ba1c)

### **Why Structured?**

We founded Structured because we believe that every business, regardless of its size or technical sophistication, should have access to reliable, consistent metrics that drive smarter decisions. We’ve experienced firsthand the frustrations of working with inconsistent data and the impact it can have on business outcomes.

We realized that the tools available today either require significant technical expertise or fall short in ensuring metric consistency across an organization. Structured was born out of a desire to create a solution that bridges this gap—providing a platform that is both powerful enough for data teams and simple enough for business users. By focusing on the specific challenge of metric consistency, we aim to empower companies to make better, data-driven decisions without the technical overhead.

### **Why Now?**

Businesses are generating and storing more data than ever before, particularly in cloud-based data warehouses. With this explosion of data comes the challenge of making sense of it—turning raw numbers into meaningful metrics that everyone in the organization can trust and use.

At the same time, the complexity of data environments is increasing. Companies are dealing with multiple data sources, complex data pipelines, and a growing need to make sure that metrics are not only accurate but also consistent across different departments and teams. Traditional BI tools are struggling to keep up with these demands, and businesses are increasingly looking for solutions that can provide a more streamlined, consistent approach to metric computation.

The market is ripe for a solution that can simplify the process of managing business metrics, reduce the reliance on specialized technical skills, and allow organizations to unlock the full potential of their data. Structured addresses this need head-on, providing a solution that is both timely and essential for the next generation of data-driven businesses.

### **Try Structured**

If you’ve ever struggled with inconsistent metrics or if you’re looking for a better way to manage and scale your business analytics, we’d love to connect with you. Check us out at [structuredlabs.com](http://structuredlabs.com) or drop us an email at [amrutha@structuredlabs.com](mailto:amrutha@structuredlabs.com) 

Looking forward to your feedback and insights!
