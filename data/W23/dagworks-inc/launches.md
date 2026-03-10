# Launches

## DAGWorks: Avoid Machine Learning Pipeline horror stories 😱

👋 Hi, Stefan & Elijah here from [DAGWorks](https://dagworks.io).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69876&key=user_uploads/1208898/cf51f7bb-c9a2-495e-91d8-afb1ddfc0192)

### **TL;DR:**

(1) At DAGWorks Inc. our goal is to make Machine Learning (ML) initiatives more human capital efficient. (2) Our solution is an open source SaaS platform for Data Science teams to build and maintain model pipelines, plugging into as much of your existing MLOps and data infrastructure as you want. (3) Star our open source project [Hamilton on github](https://github.com/dagworks-inc/hamilton) and get started with it via [tryhamilton.dev](https://www.tryhamilton.dev).

### **❌ The Problem:**

Ask a Data Scientist whether they like inheriting someone else’s ML pipelines. 99% of the time, they’ll say no. Why? Getting ML to production is easy when you’re small, but when your team and codebase start to grow, maintaining these pipelines becomes challenging:

* 😕 understanding code you didn’t write
* 🐛 debugging production issues
* 🏗️ migrating to new infrastructure
* 🥼 handling personnel changes

This causes teams to spend far more time keeping existing ML pipelines afloat than innovating and driving their business forward.

To get out of/avoid such a mess, you need a high (and expensive) software engineering skill set, but for many that’s not an option. In our experience, this phenomenon is the biggest blocker to leveraging machine learning in your business as it grows.

### **✨ Our Solution**

(1) We leverage our open source project [Hamilton](https://github.com/dagworks-inc/hamilton), which is an opinionated way to write python code (akin to what DBT did for SQL), that naturally helps teams follow software engineering best practices.

(2) Using the DAGWorks Client on top of Hamilton, we can give you full insight into how your pipelines operate on the DAGWorks Platform, including:

A **catalog of functions** - feature catalog anyone?

![](https://lh5.googleusercontent.com/lDX_3El7R6_OdBZg_tfBekfl--qUUmsmm10wBFcZcE59wrTn01e2_U8Ns-LC73fCfsJ1kmGirfbZ6XT_T_uqniK7SyJsPPZt6BXb8byJCq_C6HNlFhsdOLdiPdyVWAwS18x4D2bAQhN19AVX4Ouga6w)

**Lineage** - see upstream and downstream dependencies:

![](https://lh5.googleusercontent.com/-EwfBtPJB1OkF3JtS_JATLshDFHTnudGU5qyn9TqZJ3i29LcZGw0pU4Xed3Yb-apaRETO2HqQY_mDCD1ucOt8MQA5VH0D7Q_uCW99uh90c72nbKEeY8dvn5ppH5zhM0i-PtKJHDfxEYwaojPezU1ZlE)

**Debugging insights** - e.g. know exactly what code failed given an airflow task failure:

![](https://lh3.googleusercontent.com/j6gqllKW9oDbC9r8KC4_TRusN3MxSemIySmHq8PhSZnwOYGDwQ5ckwe-LIW4MFdtKtRfjpyCXlE_qTpQTT5boMbIDNfMgOz9huOG01UK0RuGQLFxTIR7YMuEAy5OfDuQJc-qDqdaGFLUy_9NR4nl3mo)

And more like **data observability**, and **links with materialized artifacts** (like data sources, models, features, etc.).

(3) The DAGWorks Platform becomes your ML Pipeline control plane. Use it to manage integrations with your existing infrastructure, as well as providing any reporting and compliance insights you need.

### **⚙️ How it works**

With [Hamilton](https://github.com/dagworks-inc/hamilton), users logically express what should happen, which helps avoid vendor and infrastructure lock in. Then with the DAGWorks Platform & Client, we make your Hamilton code run on your existing infrastructure, providing out of the box connectors to common systems, and provide insights post execution. By building on a solid foundation that clearly decouples concerns, we can avoid the problems that plague traditional ML Pipelines. This enables Data Science teams to move faster and do more themselves, making ML projects more human capital efficient.

**👪 Founding Team**

[Stefan](https://www.linkedin.com/in/skrawczyk/) and [Elijah](https://www.linkedin.com/in/elijahbenizzy/) worked together at Stitch Fix where they built the self-service ML Platform for over 100 data scientists. They learned firsthand the troubles that occur building and maintaining ML Pipelines over a diverse set of modeling disciplines. Their work has been recognized by industry and included in books, newsletters, and was even the topic of a lecture at Stanford. Previously Stefan built data and ML systems at Nextdoor and LinkedIn and graduated from the Stanford CS Masters program with a Distinction in Research. Elijah built tools for quants at Two Sigma and studied Math and CS at Brown.

### **🙏 Asks**

1. Start with Hamilton open source today!
   * ⭐️ Star [Hamilton on Github](https://github.com/dagworks-inc/hamilton)! Download it from [PyPI](https://pypi.org/project/sf-hamilton/).
   * Checkout out [www.tryhamilton.dev](http://www.tryhamilton.dev) for an in browser overview of Hamilton. A common use case is to start using it for feature engineering.
   * Don’t know how to leverage Hamilton – [book time](https://calendly.com/stefan-dagworks/15-minute-intro-call-with-stefan) and we’ll walk you through it!
2. We’re looking for more leads to larger organizations that have ML Pipeline struggles, in particular if they have compliance/auditing needs for them. Know someone, or perhaps you’re the right person? Please email us - [founders@dagworks.io](mailto:founders@dagworks.io) or book [15 minutes here](https://calendly.com/stefan-dagworks/15-minute-intro-call-with-stefan).
3. We’re still currently in closed beta for the DAGWorks Platform, but you can sign up for early access via [www.dagworks.io](http://www.dagworks.io).
4. Follow us on Twitter for updates:
   * [DAGWorks](https://twitter.com/dagworks)
   * [Hamilton_OS](https://twitter.com/hamilton_os)
