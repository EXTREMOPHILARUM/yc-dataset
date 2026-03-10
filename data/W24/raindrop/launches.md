# Launches

## Raindrop Deep Search

https://www.youtube.com/watch?v=pN82WxN-_G0

Today, we're excited to launch Raindrop Deep Search

It’s like Deep Research for your Production AI Data

Search for anything, and Raindrop automatically trains little models to accurately classify any topic or issue, across millions of events.

𝗧𝗵𝗲 𝗣𝗿𝗼𝗯𝗹𝗲𝗺

We’ve heard from thousands of AI engineers and they’re struggling to track issues with their agents.

Imagine a user reports a problem: your agent is saying it can’t search the web for documentation. You need to know if this is a one-off problem or a much bigger issue… but how? Keyword search, or even semantic search, doesn’t tell the full story.

𝗖𝗮𝗻’𝘁 𝘄𝗲 𝗷𝘂𝘀𝘁 𝘂𝘀𝗲 𝗧𝗿𝗮𝗱𝗶𝘁𝗶𝗼𝗻𝗮𝗹 𝗘𝘃𝗮𝗹𝘀?

Offline evals work well as unit tests. But since they’re running on preset data, you have no visibility into what’s actually happening in production.

Online evals just run these unit tests on a tiny sample of production data, leaving you blind to how widespread problems are.

𝗜𝗻𝘁𝗿𝗼𝗱𝘂𝗰𝗶𝗻𝗴 𝗥𝗮𝗶𝗻𝗱𝗿𝗼𝗽 𝗗𝗲𝗲𝗽 𝗦𝗲𝗮𝗿𝗰𝗵

That’s why we built Deep Search. It’s like Deep Research for your production data.

How Deep Search works:

1\. Describe the issue (eg. agent failing to search the web)

2\. Deep Search finds examples out of millions of events

3\. Refine search with feedback

4\. Start tracking the issue

Deep Search runs across all of your production data to give you an accurate metric of issue frequency.

Traditional classification systems require humans to manually label thousands of data points. So to achieve this, Raindrop Deep Search introduces a new research breakthrough, bespoke few-shot classifiers, which only need a few examples.

It’s essentially bootstrapping weaker systems from stronger systems, ultimately training custom small models that analyze millions of events a day. You can think of it like creating materialized views for natural language.

Once you start tracking the issue you can use Raindrop to dive into traces and tool calls to find the root cause. And you can quickly confirm whether your fixes are effective by monitoring issue frequency and receiving real-time Slack alerts.

You can try out Deep Search at [raindrop.ai](http://raindrop.ai). 

We’re excited to hear what you think!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91457&key=user_uploads/309605/b1eda0eb-8816-487f-a4f3-36bdaf02bb0b)

## Raindrop - Sentry for AI Products

[https://youtu.be/IS7akU_3AnI](https://youtu.be/IS7akU_3AnI?feature=shared)

Al products fail constantly—in ways both hilarious and terrifying.

Meet **Raindrop**: the first Sentry-like monitoring platform for Al products.

**The Problem**

Regular software throws exceptions. But Al products fail silently.

These issues can be serious:

* [Figma had to roll back their AI design product when it copied Apple’s designs, and they haven’t relaunched since](https://techcrunch.com/2024/07/02/figma-disables-its-ai-design-feature-that-appeared-to-be-ripping-off-apples-weather-app/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAM5aRTBjXhPXfaoMBpoQxL9si-7R3qfaTR4r-n_mdzKu31uB6rUYGjE31z0H4aHVY1LlchyZ7r76Pufga45IMGKwFz0IxZ7eo-g2z1sYsta94AVsSj5CYjf6NKRd3m43VgSGLrG_IfdqMKtlFDuBvimRfLyF_aqb19vPgl-8B7eD)
* [Air Canada got sued — and lost — when their chatbot incorrectly offered a customer a refund](https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/)
* [Virgin Money came under fire when their chatbot scolded customers for using the company name, ‘Virgin’](https://www.latintimes.com/virgin-money-forced-apologize-after-chatbot-threatens-cut-off-bank-customers-who-use-word-573885#:\~:text=Fintech%20commentator%20David%20Birch%20shared,reported%20by%20the%20Financial%20Times)

Don’t make the same mistake.

The current status quo is sifting through millions of logs and trying debug flaky evals. Evals are straightforward - like unit tests, they confirm your model got specific test cases right. But in the real world AI chatbots and agents encounter millions of unpredictable actions. AI companies need powerful monitoring to discover production issues so they can create reliable AI products that don’t just pass tests, but genuinely resonate with users.

**Solution**

Raindrop sends you alerts when your AI misbehaves and links straight to the events, so you can dig into the conversations or traces, understand the root cause, and fix it, fast.

Daily Alerts Include

* **Issues**: detects issues like Assistant Forgetting, Laziness, Task Failure, User Frustration, and more depending on the type of app
* **Wins**: surfaces what your product does well, so you can double down on those experiences and create evals

The Pro tier lets you go even further with:

* **Custom Issues / Topics**: define and track any issue or topic
* **Topic Clustering**: clusters data in real time to find your AI product’s most popular use cases, and what use cases have the most issues
* **Signals**: finds patterns in explicit signals like thumbs up / thumbs down
* **Deep Research:** deep research for your production data, letting you use natural language to search for any kind of behavior
* **Traces**: track every step of your AI call
* **Edge PII Redaction**: intelligently strip PII from any user and model messages
* **Dataset Creation**: create custom datasets out of any set of events

Companies like [Clay.com](http://Clay.com), Tolans, Websim, and more have been using Raindrop to improve their AI products. They’ve been able to quickly iterate on fixes, see how issue incidence rates decrease in production, and confidently ship changes.

“Raindrop has been invaluable as we've been growing quickly. It's critical for us to keep issue incidence below an acceptable threshold and become aware of any spikes. **It's like if we see an iOS crash report in Sentry, but for our AI capabilities.”** -Evan Goldschmidt, CTO Tolans

Learn more about how Tolan uses Dawn [here](https://www.raindrop.ai/case-studies/tolans), and check out case studies with [New Computer](https://www.raindrop.ai/case-studies/new-computer) and [Unstuck AI](https://www.raindrop.ai/case-studies/unstuck).

You can get started [here](https://www.raindrop.ai), excited to hear what you think :)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89925&key=user_uploads/309605/d77c5ea9-2b73-4455-96a6-db02c319651c)

## Dawn - Analytics for AI products

Hey everyone!\
\
I’m [Zubin](https://twitter.com/snarkyzk), from dawn. Excited to share what we’ve (me, [Ben](https://twitter.com/benhylak), & [Alexis](https://twitter.com/alexisgauba)) been building.

[Dawn](https://www.dawnai.com/) is analytics for AI products. We transform user inputs and model outputs into metrics you care about, letting you make meaning out of billions of tokens.

**AI Companies love us for**

* User Segmentation: automatically group users by behavior
* Understanding Churn: see how requests (or responses) cause users to churn
* Categorizing Search Requests: tag user requests + use categories in-app
* Content Moderation: identify + remove harmful content
* Flagging Bad Responses: track user requests that are vague, don’t match the source language, or anything else
* Track any use case: discover categories from unstructured data

_(It's not just for Al companies. Dawn can categorize just about anything! — _[_contact us_](https://wv6y9hc66q4.typeform.com/to/qHmrVeA3)_ to chat)_

**How it Works**

1. **3 lines to integrate:** with one line of code, you can start sending user data from your app to dawn (and even get back categorizations!)
2. **Define categories:** Dawn automatically discovers categories from your raw data. You can also define your own. You can delete, edit, reorganize, and create new categories at any time.
3. **Self-improving, on the fly:** Dawn constantly gets better at understanding your data.  A simple feedback interface gives your team visibility and control over categorization.
4. **Connects to your existing analytics:** we have plugins for Snowflake, Mixpanel, Slack, Amplitude, and more -- so you can track whatever you want, wherever you want.

\*\*What early users say about us:\*\*\
“I’m feeling a total a-ha moment with this. Truly cool to see.” - Gabriel Birnbaum, Can of Soup\
\
**Let’s work together**\
Reach out at [zk@dawnai.com](mailto:zk@dawnai.com), or sign up for a demo [here](https://wv6y9hc66q4.typeform.com/to/qHmrVeA3). We’d love to hear from you!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79667&key=user_uploads/1668573/86bc4a34-fc8f-469a-9d07-de695eb11bc3)
