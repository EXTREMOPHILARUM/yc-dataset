# Launches

## ShapedQL: The SQL engine for search, feeds, and AI agents

Hi everyone 👋\
\
I'm Tullie, the founder of [Shaped](https://www.shaped.ai/).\
\
**TL;DR**\
\
Today we’re launching ShapedQL, a new language purpose built for agents, feeds and search. We built ShapedQL because we realized that while retrieval has become easier (thanks to Vector DBs), ranking and relevance are still incredibly hard.\
\
Launch video: <https://www.youtube.com/watch?v=Owj_uSUPNaU>\
\
**Problem ❌**\
\
Most engineering teams we talk to are stuck maintaining a "Frankenstein" stack. To build a "For You" feed or give an AI Agent personalized memory, they have to glue together a vector database, a feature store (like Redis), a reranking service, and thousands of lines of Python spaghetti code.\
\
**Solution ✅**\
\
We built ShapedQL to turn that "house of cards" into a single interface.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97225&key=user_uploads/812951/eed67b43-7c3b-4b0f-819a-5bbd31db2732)

ShapedQL is a domain-specific SQL dialect that compiles down to a high-performance, multi-stage ranking pipeline. With a single query, you can define the four stages of modern relevance:\
**1. Retrieve:** Fetch candidates from multiple sources (Hybrid Search, Collaborative Filtering, Trending).\
**2. Filter:** Apply hard constraints (e.g., "in stock" or "within 50 miles").\
**3. Score:** Rank results using real-time ML models (optimizing for clicks, purchases, or watch time).\
**4. Reorder:** Enforce diversity so your users (or Agents) don't see the same 5 items repeatedly.

We're seeing teams reduce 2,000+ lines of maintenance code down to \~30 lines of ShapedQL, while shipping features like "Cart Upsell" or "Conversational Recommendations" in days instead of months.

If you're not a fan of SQL we also have Python or Typescript SDKs, perfect for a real-time production integration.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97225&key=user_uploads/812951/d3cc12cc-3c74-448b-adf0-ae65d9359b79)

**Ask 💬**\
\
**1.** We have a Product Hunt launch at this link: <https://www.producthunt.com/products/shaped>. Any support or and upvote would be greatly appreciated!\
\
**2.** Please try out our interactive demo at [playground.shaped.ai](https://playground.shaped.ai), we’d love to hear any feedback on the new language. Were you able to easily make a query? Do the docs make sense? What is it missing?\
\
**3.** If the problems above resonates and you’re struggling to get true relevance from your vector store or current retrieval system, please get in touch! Book on this calendar here: <https://www.shaped.ai/contact> and mention you’re from YC. I’ll make sure to jump on the call to help you out myself.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97225&key=user_uploads/812951/bb70b2b7-780a-4da6-a13f-511015e09776)

## Shaped — Value Modeling for Search and Recommendation Systems

# **TL;DR**

We’ve built Shaped Value Modeling, a framework that enables real-time optimization of recommendation and search ranking models for multiple objectives. It allows teams to blend different objectives (e.g. relevance, conversions, diversity) and dynamically run AB tests that drive business outcomes (with built in analytics tooling). Our community has seen awesome results, so we’re excited to bring this framework to the masses!

Watch our demo [here](https://youtu.be/gYLmtMR-N4I).

**Key Features:**

* **Multi-objective optimization:** Combine multiple models and signals (e.g., click prediction, purchase likelihood, content quality) into a single, customizable scoring function.
* **Dynamic ranking logic:** Define and adjust ranking objectives as your business needs change using a simple python DSL.
* **Real-time API:** Modify ranking scores on the fly with simple API calls, enabling rapid experimentation and A/B testing.
* **Easy to integrate:** Connect and deploy rapidly with direct integration to your existing data sources.
* **Explainability:** Gain insights into why certain items rank higher through interpretable scoring logic, and a built in analytics platform out of the box.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88281&key=user_uploads/857360/543b423e-521a-491d-808b-0bd914f06c23)

**Why This Matters:**

* Rapid iteration: Experiment with new ranking strategies and adapt to changing business needs without lengthy retraining cycles.
* Improved control: Fine-tune your ranking algorithms with precision and transparency.
* Better alignment: Optimize for multiple KPIs simultaneously, ensuring your recommendations drive both engagement and business value.

**How it Works:**

1.Train separate models for different objectives (e.g., LightGBM for click prediction, BERT4Rec for purchase likelihood).

2\. Define a "value model" that combines these models using mathematical expressions and custom logic. Let's say we have a lightgbm click-through-rate model called ctr_model and a transformerd based next purchase model called purchase_model, you can create an ensembled value model as follows:

```
value_model = 0.5 * ctr_model + 0.5 * purchase_model + log(item.quality_score)
```

3\. Dynamically adjust the value_model via API calls to optimize for different goals or user segments:

```
{
  "user_id": "83NSLX",
  "config": {
    "value_model": "0.3 * ctr_model + 0.7 * purchase_model"
  }
}
```

\
How our customers are using value modeling:

* **Marketplaces:** Dynamically mix personalized scores with a geo-location penalizer to connect users with nearby items.
* **E-commerce:** Balance purchase intent, engagement, and product quality.
* **Content platforms:** Implement time-decay, boost high-quality content, and personalize recommendations.
* **Social media:** Dynamically switch between personalized and trending models.

# **Our ask**

If you know decision-makers in any of these types of organisations, we’d be super grateful for an introduction at [daniel@shaped.ai](mailto:daniel@shaped.ai)

1. Marketplaces
2. E-commerce
3. Content platforms
4. Social Media

For more information see our website [here](https://www.shaped.ai/value-modelling) and developer docs [here](https://docs.shaped.ai/docs/model_creation_guides/value-modeling)

[Get a demo](https://meetings.hubspot.com/matt2900/meet-with-shaped-?uuid=4076ed73-5725-4ee7-ac01-2e1869237a18) if you’re interested in testing value modeling!
