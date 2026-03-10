# Launches

## Buster - Open source, AI Digital Workers for analytics & data

Hey, this is [Blake](https://www.linkedin.com/in/cblakerouse/) & [Dallin](https://x.com/dalbentley) from [Buster](http://buster.so/).

**We're building AI Digital Workers for every part of your analytics & data stack.** You can think of our platform as a 24/7 team of AI data engineers & analysts.

Its modern, simple, & open source. You can watch a demo video [here](https://youtu.be/Sf4IHvkIUiQ).

### **what does Buster actually do?**

**If you’re a data professional or engineer…** Buster gives you a team of 24/7 AI Workers that monitor your data stack, suggest model improvements, & handle ad-hoc requests from users.

**If you’re an operator (or really anyone else)…** Buster serves as your personal AI Data Analyst. This AI Data Analyst can answer ad-hoc data questions, do deep dive analysis on your behalf, & build beautiful dashboards or reports for you.

### **problem**

Companies struggle to effectively leverage AI to get more value from their data. There are a few reasons for this.

1. **Data is siloed.** By default, company data siloed away in various places. To solve this, teams usually ETL their data into a warehouse, then perpetually build ad-hoc views or dbt models. In other words… they become a data stack Frankenstein with poor governance - making it impossible for LLMs to safely work with their data.
2. **Data modeling is broken.** The typical modeling workflow is: write a model → publish it → query it. It’s linear & makes it hard to create a feedback loop from the BI layer. This results in building hundreds of new models instead of improving existing models.
3. **Current BI tools aren’t code-based** (more to come on this).
4. **Current BI tools just aren’t great products.** This is a pretty [consensus idea](https://www.reddit.com/r/dataengineering/comments/1ai2d2z/bi_tool_rant/).
5. **LLMs weren’t performant enough, but now they are.** Prior to GPT-4o & 3.5 Sonnet, SOTA models just weren’t capable of accurately accomplishing data workflows (like text-to-sql). But now we are seeing consistent performance across dozens of workflows (see this [post from Garry Tan](https://x.com/garrytan/status/1849472361978105894) about our evals).

### **solution**

Here are some things that make the Buster platform unique & reliable.

1. **A single, shared data model**. We integrate and unify all of your company data into a single data model. This approach provides a strong foundation for AI workers to accurately utilize your data.
2. **Guardrails & AI safety.** Lets say a user requests some kind of analysis, but it introduces a new concept that isn’t clearly defined in the data model. Buster will identify this & flag the request. Then, an AI Worker will automatically create a branch & generate a suggested model update. You can review & merge it’s suggested update with one click.
3. **Everything in Buster is code-based**. Your model, dashboards, metrics, documentation, permissions, etc all live (as files) in your own Github Repo. This enables you to manage everything from your CLI & CI/CD pipeline. More importantly, **it enables AI Workers to do things like:**
   * Automatically ingest metadata from other tools & build your data model
   * Automatically generate & push improvements to your data model over time
   * Document key business logic or terminology
   * Fix impacted dependencies when there are breaking changes
   * Utilize git & can deploy via CI/CD
   * Integrate seamlessly with dbt & communicate with other tools you use
   * And much, much more
4. **Personal AI data analyst.** End users can just tell Buster the exact metric, dashboard, or analysis they want to create & Buster will just… do it. **It’s like v0 for business intelligence.** And, “It. just. works.”

### **why us**

Ultimately, we believe that the future of AI analytics is about helping engineers & data teams build powerful, self-serve experiences for their users. We think that requires a new approach to the analytics stack. One that allows for deep integrations between products & allows data teams to truly own the entire experience.

### **ask**

Get started with Buster [here](https://buster.so/). If you like what we’re building please star us on [GitHub](https://github.com/buster-so/buster-platform)!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=86747&key=user_uploads/699099/8bc8c03d-4586-4c23-b45b-c82c8568ca22)
