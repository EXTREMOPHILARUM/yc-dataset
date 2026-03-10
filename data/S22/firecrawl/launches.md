# Launches

## /extract by Firecrawl - Get structured website data with just a prompt

Hey everyone! We’re Eric, Caleb, and Nick from Firecrawl (S22). Today, we’re launching **/extract** — an endpoint that turns entire websites into structured data with a prompt.

**TL;DR**

With Firecrawls' new /extract endpoint, any website can be turned into structured data with a simple API call and prompt. We handle the complexity so you can focus on building your company.\
\
**The Problem.**

If you need to pull data from websites - maybe to enrich your CRM, track competitors, or onboard users - you're stuck with:

1. Manually researching and copy-pasting from multiple sources \\
2. Building and maintaining scrapers that break at the slightest site change
3. Stitching together scraping services and complex LLM pipelines with limited context windows\
   \
   Each approach wastes the engineering time you could spend shipping a product. :

## **Our Solution:**

/extract is an API that turns a prompt into structured web data.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=86973&key=user_uploads/1045172/62c44a11-9011-4ae0-82ac-8151a9c57c1b)

Here's how to use it: 

1. **Give us URLs + Prompt**\
   Write what data you want, and point us at websites. Use wildcards like [example.com/\*](http://example.com/\*) to scan entire sites.
2. **We Find Relevant Content**\
   Our crawler finds and ranks the pages that matter, automatically.
3. **AI Extracts Data**\
   Intelligent agents split, search and parallelize the work, handling sites of any size.
4. **Get Clean JSON**\
   Receive structured data ready to use - no post-processing needed.
5. **Integrate anywhere via API**\
   With our API, you can use firecrawl anywhere, whether its in your applications or no-code tools like Zapier

## **Why It Works**

* **Handle Any Website:** Built on proven scraping infrastructure that just works
* **Natural Language Input:** Describe what you want in plain English - we figure out the schema
* **No Size Limits:** Process massive sites by automatically splitting the work
* **Use It Anywhere:** Full API + ready-made integrations for Python, Node, and Zapier

## **Limitations - (and the road ahead)**

Let's be honest - while /extract is pretty awesome at grabbing web data, it's not perfect yet. Here's what we're still working on:

1. Big sites are tricky - It can't (yet!) grab every single product on Amazon in one go
2. Complex searches need work - Things like "find all posts posted after 2024" aren't quite there
3. Sometimes, it's a bit quirky - Results can vary between runs, though it usually gets what you need

But here's the exciting part: we're seeing the future of web scraping take shape. 

## **Get Started**

1. **Try the Open Beta**
   * For a limited time, get **500,000 free** tokens to get you started
   * Explore the [www.firecrawl.dev/playground?mode=extract](http://www.firecrawl.dev/playground?mode=extract) 
   * Read the docs => <https://docs.firecrawl.dev/features/extract>
2. **Join Our Community**
   * Star us on [www.github.com/mendableai/firecrawl](http://www.github.com/mendableai/firecrawl) - we're open-source!
   * Share your use cases and feedback.

Ready to turn web data into your competitive advantage? Get started in less than 5 minutes.

Get your API key at [www.firecrawl.dev/app](http://www.firecrawl.dev/app)

— Eric, Caleb, and Nick at Firecrawl 🔥

## Firecrawl 🔥: Open source crawling and scraping for AI-ready web data

Hey everyone! We're Caleb, Nick, and Eric, the founders behind [Firecrawl](https://www.firecrawl.dev/) - an all-in-one developer platform for crawling & scraping web data for AI applications.

**TLDR:** Firecrawl is an open source API that transforms any web data into a clean, LLM-ready format for RAG, agentic tasks, or training. Since launching in April we gained 8000 stars on GitHub ⭐️

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82563&key=user_uploads/1045172/59b29329-b168-42b9-9642-0e11f99699de)

\
**The Problem:** Our story began while building [Mendable.ai](http://Mendable.ai), one of the first managed RAG platforms used by companies like Coinbase, Snap, and MongoDB. We quickly discovered that web data was not only a popular source for AI applications but that its quality was crucial for successful deployments.

Building a reliable stack that worked for almost any URL presented numerous challenges, and as we expanded, we encountered countless edge cases. While some great tools existed, none handled the entire process reliably. We envisioned an API that could take a URL, crawl its pages, and provide up-to-date, easy-to-use markdown.

Conversations with industry peers revealed that they were rebuilding similar infrastructure. This inspired us to create Firecrawl— a developer-friendly solution we wish we'd had from the start.

We launched a cloud offering over a weekend in April, and in just three months, we've garnered over 8,000 GitHub stars and empowered thousands of developers to transform web content into AI-ready data.

**Our Solution:**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82563&key=user_uploads/1045172/14099b5d-73e8-4661-8ce4-65bb4623852f)

Our open-source, developer-focused platform simplifies scraping & crawling for AI apps by handling:

* Bypassing JavaScript rendering
* Enriching metadata
* Crawling without consistent sitemaps
* Parallel scraping jobs
* Hosting headless browsers and managing proxies
* Bot blocking
* Formatting LLM-friendly markdown

With Firecrawl, developers at companies like [Gamma](https://gamma.app/), [StackAI](https://www.stack-ai.com/), and [Zapier](https://zapier.com/) are delegating scraping to us so they can focus on their core tasks - be it RAG, agents, or data processing.\
\
Now scraping a whole website and retrieving the markdown is as simple as this:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82563&key=user_uploads/1045172/0c55112e-cd7a-4420-bd79-cbb07e4acaf3)

**Our Asks:**

* Give [Firecrawl](https://www.firecrawl.dev/) a try 🧑‍💻
* Explore our [GitHub repository](https://github.com/mendableai/firecrawl) and consider leaving a star ⭐️
* Drop me a line at [eric@firecrawl.com](mailto:eric@firecrawl.com) if you want to chat (we are super excited about collaborations) 🔥

## 🔍 Mendable - Embeddable chat powered search for your developer products

Hey YC!

It’s Garrett, Eric, Caleb, and Nick from SideGuide - Today we are launching Mendable, a chat-powered search tool embeddable in your docs, product, or community to answer developer questions and reduce their time to hello world. Check out our [live search demo with LangChain](https://hwchase17.github.io/langchainjs/docs/modules/indexes/document/) and shoot us a message at [garrett@sideguide.dev](mailto:garrett@sideguide.dev) if you want to chat! :)

**Problem:**

We’ve spent over a year in the developer experience space, building tools to make the lives of founders and developer relations folks easier. During this journey, we learned developers have a hard time navigating documentation and understanding the capabilities of a product in an efficient way. In response, developer communities and support forums become overloaded with questions, and dropoffs and onboarding times grow.

**Solution:**

We’re building [Mendable](https://www.mendable.ai/), a chat-powered search tool leveraging cutting edge LLM models to accelerate a developer’s time to hello world and improve developer experience. We ingest your company’s resources (documentation, support forums, community messages, etc.) and give developers custom responses to their questions with direct links to sources via a chat interface. This interface can be easily embedded anywhere via a javascript component or accessed via slack/discord, allowing our search to be put in your docs, product, community, or wherever else you see fit.

**What does it look like?**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69730&key=user_uploads/1045324/4b531b27-de01-4e68-abea-2014a4088e8c)

* **Continuous Improvements -** With our intuitive thumbs-up and down rating system and the ability for admins to edit answers, Mendable's search functionality continually learns and improves.
* **Integrates Everywhere -** Mendable offers a chat-powered search bar to add anywhere in your docs or website. Support for Discord, Slack, Github, and more is coming soon.
* **Resources Condensed** - Mendable’s generations are based on your resources - including docs, support Q/A, and community messages - condensed into powerful answers.

**The ask:**

Interested? Shoot us a message at [garrett@sideguide.dev](mailto:garrett@sideguide.dev) or schedule a meeting with us [here](https://calendly.com/garrett-sideguide)!

## 🚀 SideGuide - Let developers test-drive your API with an online editor

Hi YC!

It’s Eric, Caleb, Nick, and Garrett from SideGuide - We are building a lightweight, embeddable, online code environment that lets developers play with your API use cases and tutorials with zero setup. Interested? Check out our [live example with Hyperbeam here](https://app.sideguide.dev/hyperbeam/threejs/) and shoot us a note at [founders@sideguide.dev](mailto:founders@sideguide.dev) to chat :)

**Problem:**

During college, we started SideGuide as a B2C coding education platform, where we watched hundreds of developers struggle to learn from API documentation, then waste hours re-inventing the wheel instead of using an off-the-shelf solution. We found that API and SDK documentation is often, to be frank, not engaging. This leads to an incomplete understanding of the implementation process and product value, resulting in lost sales. Basically, developers forget your product instead of falling in love with it.

It’s 2022, developers and technical PMs should be able to quickly play with the real code before investing time and money in a product. That is why we built SideGuide.

**Solution:**

We are building SideGuide: a lightweight, embeddable, online code editor that lets developers play with your API without **setup.** Our format integrates guides directly into the editor, giving users the context they need to understand your use-cases while experimenting immediately. We give developers and technical PMs an easy way to test, understand and evaluate your products. As a bonus, we also provide analytics and insights from sessions so you can improve the implementation process and understand your customers.

**What does it look like?**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65638&key=user_uploads/1045172/1e47388e-3f04-4540-b374-1d1bad6b1dc2)

* **Fully interactive** - Our web-based sandbox makes it quick and easy for developers to try your examples out with minimal friction.
* **Integrated tutorial - Step-by-step instructions for different sections of the code.**
* **Trackable - See how users are interacting with your use-cases so you can identify avenues for improvement** 
* **Embed anywhere - Embed in your docs or send via link.**

Check out our updated website at <https://sideguide.dev> and the live example using Hyperbeam’s amazing API here: <https://app.sideguide.dev/hyperbeam/threejs/>

**The Ask:**

Interested? Shoot us a note at [founders@sideguide.dev](mailto:founders@sideguide.dev) or schedule a meeting with us [here](https://calendly.com/eric-ciarla)! We are looking for launch partners for demo day :)
