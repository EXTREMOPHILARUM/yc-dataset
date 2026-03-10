# Launches

## Tidepool 🌊 - Product analytics for AI apps

![uploaded image](https://bookface.ycombinator.com/media/?type=post&id=73360&key=user_uploads/486120/59d0da6d-3ebf-4b0c-a977-52e9dcd90847)

**TLDR: Excited to announce our new product,** [**Tidepool**](https://www.tidepool.so/)! Tidepool does product analytics for AI text interfaces. With Tidepool, product teams can find patterns in their user text interactions to help make better product decisions.

[**Check our our demo video here!**](https://youtu.be/Ss-zLj53OlM)

### **The Problem:**

LLM apps have introduced [**a new paradigm**](https://www.nngroup.com/articles/ai-paradigm/) for interacting with software, where users can work iteratively with the software via a natural language interface, generating user inputs and model responses consisting of unstructured text.

Traditional product analytics techniques don't deal well with large amounts of unstructured text - it's hard to summarize, it's hard to aggregate, and it's hard to effectively sample. AI developers resort to digging through a pile of hundreds to hundreds of millions of datapoints of unstructured text to understand how users interact with their product.

### **The Solution:**

[**Tidepool**](https://www.tidepool.so/) is a product analytics platform that solves these problems using **neural network embeddings**. After you upload user text interaction events, Tidepool will:

1. **Automatically group your data by similarity.** Tidepool runs embedding clustering on your users’ text interactions to surface interesting attributes: things like prompt topics, prompt languages, and common usage patterns that can be turned into shortcuts.
2. **Summarize common attributes in your data**, using LLMs to determine what each cluster “contains.” For example, understanding that the most common topics that users discuss are business, education, and art.
3. **Track attributes in production traffic**, allowing you to uncover how a specific attribute might be correlated to good / bad product outcomes. We utilize lightweight models running on foundation model embeddings to scalably extract these attributes from hundreds of millions of production interaction events.

### **About Us:**

Over the last few years, Aquarium has worked a lot with computer vision companies to help them curate labeled datasets and improve their fine-tuned models using our core embedding technology.

Our mission has always been to make it easier for people to build and improve production ML systems that solve real-world problems. When we saw the Cambrian explosion of LLM apps earlier this year, we realized that our core embedding technology and expertise was very useful for getting these new apps to product-market fit even faster!

### **Our Ask:**

* **Try it out!** [Sign up here to get started.](https://www.tidepool.so/)
* **Share this post with your friends!** We’d love to get exposure to as many different AI applications as possible.
* **Give us feedback!** [Join our Slack community](https://join.slack.com/t/tidepoolcommunity/shared_invite/zt-1zp4f82tc-78rxSFZ6E3eXguvH3pzdwQ) and leave your thoughts, or [schedule some time with us to talk](https://calendly.com/pgao/tidepool-demo).
