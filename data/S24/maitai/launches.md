# Launches

## Maitai - Reliable AI without the heavy lift

**TL;DR:** Maitai is an ultra-lightweight layer between your app and LLM providers, ensuring reliability and passive continuous improvement.

[Try Maitai](https://portal.trymaitai.ai)

# The Problem:

Getting LLMs into production is complex and time-consuming. Teams today spend much of their time-fighting hallucinations, suboptimal output, and mitigating problems plaguing their providers. Though this is necessary for a production-ready application, it can be a massive distraction from building and expanding the core product, not to mention a sizable investment. Hallucinations can quickly deteriorate the user experience and are difficult or impossible to fully fix. Model outages or degraded performance make any meaningful traffic a nightmare. Consistent response times are usually only solved today with dedicated compute environments, which can be too costly for most companies to consider. The more you make progress on these issues, the more you become locked into a provider.

# The Solution: A Dependable Middleman

Maitai integrates seamlessly between the application and model providers to handle the heavy lifting behind the scenes. The result? Higher quality, reliable model output with passive incremental improvement - without any new code. We leverage our robust real-time evaluation engine to build a deep understanding of the customer's application, as well as the capabilities of all major models, in order to deliver consistent, dependable results. This abstraction layer is essential as the AI landscape evolves and new models emerge.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83311&key=user_uploads/213922/d9d0ba25-8ae2-48c4-b5ae-6a9f891d493c)

**Real-time Evaluations**

For each application, we build an understanding of the expectations that the user has for each request. We then evaluate all model output to ensure it adheres to these expectations, in under 200ms. Detected faults can be surfaced to the user in a callback or webhook. Users can also allow Maitai to leverage these evals to autocorrect any faulty output we find, ensuring clean, reliable responses.

_Example:_ One of our customers is a voice-ordering company for restaurants. They use Maitai to ensure the model always requests consent from the customer before sending a text message. Failure to do so would put them out of compliance with the Telephone Consumer Protection Act, resulting in heavy fines and lawsuits. Maitai has prevented this from happening 14 times.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83311&key=user_uploads/213922/858792ed-11e9-40b8-92c2-d46c244ae91b)

**Highly-available Inference**

As AI adoption grows, all providers are having trouble keeping up with the demand. As we continuously profile all models we support, we see this manifest as outages and degraded performance many times throughout each day. Maitai uses our model health data to preemptively fall back to a similar model if we notice degraded performance or an outage. Avoid failed responses and get more consistent response times without shelling out hundreds of thousands of dollars on dedicated compute.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83311&key=user_uploads/213922/d10bbf2a-7fd4-47c3-8788-1a8aeffdeb0b)

_Our health checks on gpt-4o from us-west2 show consistent performance only \~90% of the time, with frequent spikes to 400%+ usual response times._

**Passive Incremental Improvement**

With Maitai, you gain access to models that are higher quality than GPT-4o, 5x faster, and 10x cheaper — tailored specifically for your application. Our evaluation data not only allows us to immediately improve output quality and reliability, but also lends way to passively building application-specific models that are higher quality, more performant, and cost less than closed-source alternatives. Access the best models for your application, with updates as often as every few days.

**Actionable Alerts**

Get briefed on problems as they occur to quickly remedy a bad situation. Maitai surfaces real-time faults or session summaries right in Slack, then allows you to chat with your data to explore deeper. Never miss a chance to improve a potentially negative customer experience ever again.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83311&key=user_uploads/213922/c93ad111-9921-4213-a32e-4c13fcf00573)

**Micron Thin**

We've invested heavily in making our presence as light as possible. Maitai adds <30ms to each request (and improving!). Get all the benefits of using Maitai without any drawbacks.

# Our Ask:

* If you're building with LLMs, let us help. It takes 2 minutes to integrate, and you can bring your own keys. We can even do it for you while you browse Slack/Reddit/HN. [Get Started](https://portal.trymaitai.ai)
* Host LLMs or experts at fine-tuning? Let's chat!
* Let us know your biggest problems building with LLMs.

[founders@trymaitai.ai](mailto:founders@trymaitai.ai)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83311&key=user_uploads/213922/06d87dd9-3243-4c88-b4bd-5430256d5e79)
