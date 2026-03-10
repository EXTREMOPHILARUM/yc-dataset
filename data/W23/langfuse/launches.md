# Launches

## 🪢 Langfuse - The Open-Source LLM Engineering Platform

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXdIAXpWtb7lK2NRs0-3d-GTPHW5YYMdHGsiSgqV4j4hVw8eb5PJXfszk16m2ROBoKOfyjOWlOtlk3adorGG4L49KTClDdTo5Yv6_k-iBdhbSFgnsKTQBa5e4Cp5kaDnmRlWccSKWQ?key=X_meTBjiqstYzDfMfZ-Cj7Hg)

[Langfuse](https://langfuse.com) is the open-source LLM engineering platform designed to help teams build production-grade LLM applications faster. We started building Langfuse in SF during Y Combinator's W23 batch - just when GPT 4 was initially released. \
**Today, Langfuse is used by tens of thousands of developers and is one of the **[**most popular LLMOps platforms globally**](https://langfuse.com/blog/2024-11-most-used-oss-llmops)**.**

### **🤯 The Problem**

Building production-grade LLM applications is challenging because of the probabilistic nature of LLMs and the multiple layers of scaffolding required to get complex workflows into production. \
Developers need to **debug** their applications because of increasingly complex abstractions like chains, agents with tools, and advanced prompts. Understanding how an application executes and identifying the root causes of problems can be arduous. Additionally, **monitoring costs and latencies** is crucial since LLMs can incur high inference expense and take time to respond to users, making it important to track model usage and costs across applications.

Assessing the **quality of LLM outputs** also poses challenges. Outputs may be inaccurate, unhelpful, poorly formatted, or hallucinated, complicating the process of ensuring reliability and accuracy. Quickly **identifying and debugging issues** in complex LLM applications is essential but often difficult. Furthermore, building high-quality datasets for fine-tuning and testing requires capturing the full context of LLM executions..

### **✅ Our Solution**

<https://www.youtube.com/watch?v=2E8iTvGo9Hs> 

Langfuse addresses these challenges by providing an open-source platform to debug and improve LLM applications. \
Langfuse captures the **full context of your application**, tracing the complete execution flow—including API calls, retrieved context, prompts, parallelism, and more. By enabling **hierarchical representations through nested traces**, Langfuse helps you understand complex logic built around LLM calls. Langfuse also offers **full **[**multi-modal**](https://langfuse.com/changelog/2024-11-20-full-multi-modal-images-audio-attachments)** support**, including audio, images, and attachments.

**Langfuse measures cost and latency**, breaking down metrics by user, session, feature, model, and prompt version, allowing for detailed analysis. To assess output quality, Langfuse facilitates the collection of **user feedback**, performs automated **LLM-as-a-judge evaluations**, and supports manual **data labeling** within the platform. It also offers [**prompt management**](https://langfuse.com/docs/prompts/get-started) features, allowing you to handle prompts effectively and perform [**prompt experiments**](https://langfuse.com/changelog/2024-11-22-prompt-experimentation) over new ideas and systematically track success.

For testing and experimentation, Langfuse supports **versioning your application** and running tests of **expected inputs and outputs** via curated **datasets**. This provides quantitative insights into the impact of changes, helping you understand and improve your LLM applications more effectively.

### **🎬 Getting Started (Tracing OpenAI with Langfuse):**

Below is a brief example highlighting how you can integrate with Langfuse. You can also try out Langfuse through our interactive live demo or our walkthrough video - more [here](https://langfuse.com/docs/demo)**.**

_(Not using OpenAI? Langfuse can be used with any model or framework through our _[_Python Decorator_](https://langfuse.com/docs/sdk/python/decorators)_ and _[_JS-TS SDK_](https://langfuse.com/docs/sdk/typescript/guide)_. Langfuse also natively integrates with popular frameworks such as _[_Langchain_](https://langfuse.com/docs/integrations/langchain/tracing)_, _[_LlamaIndex_](https://langfuse.com/docs/integrations/llama-index/get-started)_, _[_LiteLLM_](https://langfuse.com/docs/integrations/litellm/tracing)_ and _[_more_](https://langfuse.com/docs/integrations/overview)_. )_

#### Step 1: Create a New Project in Langfuse

1. Sign up for [Langfuse Cloud](https://cloud.langfuse.com) or [self-host](https://langfuse.com/docs/deployment/self-host) Langfuse OSS.
2. Create a new project within Langfuse.
3. Generate API credentials via the project settings.

#### Step 2: Log Your First LLM Call to Langfuse

The [@observe() decorator](https://langfuse.com/docs/sdk/python/decorators) makes it easy to trace any Python LLM application. In this quickstart, we use the Langfuse [OpenAI integration](https://langfuse.com/docs/integrations/openai) to automatically capture all model parameters such as cost and token usage.

```
%pip install langfuse openai
```

```
# Get keys for your project from the project settings page https://cloud.langfuse.com
os.environ["LANGFUSE_SECRET_KEY"] = "sk-lf-..."
os.environ["LANGFUSE_PUBLIC_KEY"] = "pk-lf-..."
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com" # 🇪🇺 EU region
# os.environ["LANGFUSE_HOST"] = "https://us.cloud.langfuse.com" # 🇺🇸 US region
```

```
from langfuse.openai import openai # OpenAI integration
from langfuse.decorators import observe

@observe() # Langfuse decorator
def story():
    return openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": "You are a great storyteller."},
          {"role": "user", "content": "Once upon a time in a galaxy far, far away..."}
        ],
    ).choices[0].message.content
 
@observe()
def main():
    return story()
 
main()
```

#### Step 3: See your Traces in Langfuse

![](https://lh7-qw.googleusercontent.com/docsz/AD_4nXfbJGtoDrEGUKAM8Kiim08yIkwLNR25bUtH6Mlr9H49lIdQUkwr9yVQhC1Q06Y8IMaGDte-likn20DUIo1_eGST64FC4RO1VREZdF24OxrTTV3yYL9EmV6xBxXmCiSN01ucH-_zPA?key=X_meTBjiqstYzDfMfZ-Cj7Hg)

Log into the [Langfuse UI](https://cloud.langfuse.com/) to view the created trace. You can now take it further by managing your prompts through Langfuse or by starting to test or evaluate your LLM executions (more below).

See this example trace in the Langfuse UI: [_https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/fac231bc-90ee-490a-aa32-78c4269474e3_](https://cloud.langfuse.com/project/cloramnkj0002jz088vzn1ja4/traces/fac231bc-90ee-490a-aa32-78c4269474e3)

### **🏃 Now what?**

After you are set up in Langfuse you can now:

* **Evaluate** the quality of your application through
  * [User feedback](https://langfuse.com/docs/scores/user-feedback)
  * [Data Labeling](https://langfuse.com/docs/scores/annotation)
  * [LLM-as-Judge Evals](https://langfuse.com/docs/scores/model-based-evals)
  * [Custom Evaluators](https://langfuse.com/docs/scores/custom)
* Run **Tests & Benchmarks** by
  * [Curating Datasets](https://langfuse.com/docs/datasets/overview)
  * [Conducting Prompt Experiments](https://langfuse.com/docs/datasets/prompt-experiments)
* **Analyze and collate statistics** on your app with
  * [LLM analytics](https://langfuse.com/docs/analytics/overview)
  * [Intent Classification](https://langfuse.com/docs/analytics/example-intent-classification)
  * [Posthog Integration](https://langfuse.com/docs/analytics/posthog)
* **Develop faster** by utilizing
  * [Prompt Management](https://langfuse.com/docs/prompts/get-started)
  * [Prompt Playground](https://langfuse.com/docs/playground)

### **👇 Interested in learning more?**

* ⭐️ Star us on [GitHub](https://github.com/langfuse/langfuse/) + follow along on [Twitter](https://twitter.com/langfuse) & [LinkedIn](https://www.linkedin.com/company/langfuse).
* 👨‍💻 [Getting Started](https://docs.langfuse.com/)
* [👷 How did we build Langfuse?](https://langfuse.com/blog/2024-12-langfuse-v3-infrastructure-evolution)
* PS: [We’re Hiring!](https://langfuse.com/careers)

## 🪢 Langfuse - Open-source product analytics for LLM apps

⭐ Star us on [**_Github_**](https://github.com/langfuse/langfuse/) & follow us on [**_Twitter_**](https://twitter.com/langfuse)

**_TLDR_**_: _[**_Langfuse_**](https://www.langfuse.com/?utm_source=LaunchYC)_ is building open-source product analytics (think ‘Mixpanel’) for LLM apps. We help companies to track and analyze quality, cost and latency across product releases and use cases._

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73214&key=user_uploads/1148936/d38a4a7c-edf5-469a-ad3f-7f7aef62a3a5)

Hi everyone, we’re Max, Marc and Clemens. We were part of the Winter 23 batch and work on [**Langfuse**](https://www.langfuse.com/?utm_source=LaunchYC), where we help teams make sense of how their LLM applications perform. 

### **🤯 Problem**

LLMs represent a new paradigm in software. Single LLM calls are probabilistic and add substantial latency and cost. Applications use LLMs in new ways via advanced prompting, embedding-based retrieval, chains, and agents with tools. Teams building production-grade LLM applications have new **product analytics** and **monitoring** needs:

* **Quality of outputs** is difficult to measure. Outputs can e.g. be inaccurate, unhelpful, poorly formatted, hallucinated or error.
* **Cost of compute** is a priority again given high inference costs.
* **Latency** of responses matters for synchronous use cases.
* **Debugging is challenging** due to increasingly complex LLM applications (chains, agents, tool usage).
* **Understanding user behavior** is difficult given open-ended user prompts and conversational interactions.

### **🧠 Solution**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73214&key=user_uploads/1148936/75e00e56-33fa-4484-bf63-4bdf0394049d)

Langfuse derives actionable insights from production data. Our customers use Langfuse to answer questions such as: _‘How helpful are my LLM app’s outputs? What is my LLM API spend by customer? What do latencies look like across geographies and steps of LLM chains? Did the quality of the application improve in newer versions? What was the impact of switching from zero-shotting GPT4 to using few-shotted Llama calls?’_

**Metrics**

* **Quality** is measured through user feedback, model-based scoring and human-in-the-loop scored samples. Quality is assessed over time as well as across prompt versions, LLMs and users.
* **Cost and Latency** are accurately measured and broken down by user, session, geography, feature, model and prompt version.

**Insights**

* Monitor quality/cost/latency **tradeoffs** by release to facilitate product and engineering decisions.
* **Cluster use cases** by employing a classifier to understand what users are doing.
* Break down **LLM usage by customer** for usage-based billing and profitability analysis.

**Integrations**

* Python and Typescript SDKs to easily monitor complex LLM apps
* Frontend SDK to directly capture feedback from users as a quality signal

_Langfuse can be self-hosted or used with a generous free tier in our managed cloud version._

### **🚧 Debugging UI**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73214&key=user_uploads/1148936/8d29b87f-8426-4eb1-be4e-6efbf9d4769f)

Based on the ingested data, Langfuse helps developers debug complex LLM apps in production:

* Inspect LLM app executions in a nested UI for chains, agents and tool usage.
* Segment by user feedback to find the root cause of quality problems.

### **🙏 Asks**

Star us on [**GitHub**](https://github.com/langfuse/langfuse/) + follow along on [**Twitter**](https://twitter.com/langfuse) & [**LinkedIn**](https://www.linkedin.com/company/langfuse).

* If you run an LLM app, go ahead and [**talk to us**](https://cal.com/marc-kl/langfuse-analytics), we’d love to see how we can be helpful.
* Please forward [**Langfuse**](https://www.langfuse.com/?utm_source=LaunchYC) to **teams building commercial LLM applications**.
