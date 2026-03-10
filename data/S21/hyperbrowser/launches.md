# Launches

## HyperAgent: Open Source AI Browser Automation Framework

**TL;DR / Summary:**

Hyperagent is the AI-native browser automation framework - think Playwright supercharged with AI. No more brittle scripts, just powerful natural language commands.

HyperAgent gives you:

* 🤖 **AI Commands**: Simple APIs like [page.ai](http://page.ai)(), page.extract() and executeTask() for any AI automation
* ⚡ **Fallback to Regular Playwright**: Use regular Playwright when you don’t need AI
* 🥷 **Stealth Mode** – Avoid detection with built-in anti-bot patches
* ☁️ **Cloud Ready** – Instantly scale to hundreds of sessions via [Hyperbrowser](https://app.hyperbrowser.ai/)
* 🔌 **MCP Client** – Connect to external tools for full workflows (e.g. writing web data to Google Sheets)

⭐ **Check it out and give it a star on Github!**

<https://github.com/hyperbrowserai/HyperAgent>\
\
<https://www.youtube.com/watch?v=0bHC1i1aRhI>\
\
**Browser Automation Is Broken**

We built HyperAgent because **browser automation is broken.** We've all been there – spending hours writing scripts that shatter the moment a website changes. With AI agents becoming mainstream, we need automation that's as adaptive as they are, and doesn’t break every time a css class changes.

With HyperAgent, we’re adding AI to your existing toolkit, wrapping playwright in simple, natural language commands that just work. So you can have the best of both worlds - keep what you love about playwright and automate the rest with AI.

**HyperAgent Quickstart**

To use HyperAgent on an existing page, you can simply call [**page.ai**](http://page.ai):

```
await page.ai("Find a route from Miami to New Orleans, and provide the detailed route information.")
```

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89908&key=user_uploads/556017/f6d70ca6-70cf-4dff-a206-9263341cd681)

This will go to google maps, enter in the origin and destination, then return the route back.

To extract information from a page, call **page.extract:**

```
await page.extract(“find the major cities that this path goes through")
```

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89908&key=user_uploads/556017/2ca8cdba-b651-44e4-af20-9bdc7d1e0393)

**Built-in Stealth Mode**

HyperAgent comes with patches for stealth browsing so you don’t have to worry about getting blocked. For maximum stealth, use Hyperbrowser - it’s free to start.

**Infinitely Extensible with MCP servers**

Want to give HyperAgent access to custom tools or integrate with other apps? HyperAgent is an MCP client and offers infinite extensibility with any MCP server.

**Scale to 100s of Concurrent Agents**

Using HyperAgent on HyperBrowser you can scale to 100s of concurrent agent runs in seconds. No need to worry about the underlying infrastructure.

# Try It Today

🚀 GitHub: <https://github.com/hyperbrowserai/hyperagent>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89908&key=user_uploads/556017/6aa560db-eee6-4bb6-9a9c-38c51fadb03d)

## Hyperpilot: AI Browser Agent Playground by Hyperbrowser

# **TL;DR / Summary:**

AI Browser Agents are powerful but costly/hard to access. HyperPilot lets you try all the leading browser agents (CUA, Claude CU, Browser Use) for free. It's built on Hyperbrowser, our infra that lets you build agents with a free API key + 5 lines of code.

<https://www.youtube.com/watch?v=1AbjFhf2T0k>

**Why**

AI browser agents like OpenAI's CUA and Anthropic's Claude Computer Use promise to revolutionize web automation. But getting hands-on experience is tough. Tools are limited, complex, or expensive – OpenAI's Operator preview costs $200/month just to try. How can you explore this future without breaking the bank?

# **What**

We're launching [HyperPilot](http://pilot.hyperbrowser.ai): A free, easy-to-use playground where you can directly interact with and compare different AI browser agent models. See firsthand what they can really do.

HyperPilot isn't just a demo; it’s a fully functional browser agent playground that runs entirely on [Hyperbrowser](https://hyperbrowser.ai) - our robust and scalable browser infrastructure designed specifically for AI agents.

# **Who is this for? What should you do with it?**

### **Everyone**

Try it out for yourself. See what the future of Browser Agents actually holds. Check out Claude Computer Use, OpenAI’s CUA, and more. If you get inspired by what you see, we’d love to hear from you and help in any way we can! Reach out to us at [founders@hyperbrowser.ai](mailto:founders@hyperbrowser.ai)

_(Hyperbrowser booking Kendrick Lamar concert tickets)_

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89020&key=user_uploads/233736/c8e39379-b378-45a7-a97b-7caafc1df810)

### **Developers**

Use HyperPilot to rapidly prototype your agents, prompts, and automations. Everything you see in HyperPilot is powered by Hyperbrowser infrastructure along with OpenAI, Anthropic, and Google DeepMind’s models.

Want to build this magic into your own apps? With Hyperbrowser, you can get started using OpenAI’s CUA, Anthropic’s Claude Computer Use, and more with just a free API key and 5 lines of code.

Check out the docs here:

* [Claude Computer Use on Hyperbrowser](https://docs.hyperbrowser.ai/agents/claude-computer-use)
* [OpenAI CUA on Hyperbrowser](https://docs.hyperbrowser.ai/agents/openai-cua)

Get your free API key here: <https://hyperbrowser.ai>

_(Claude computer use on Hyperbrowser in 5 lines of code)_

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcqYG4wQaP9VTtLxvuXkLewpbDHxUCaWa2JU8rfhb9HYJBzLjuSViGyIoV-0jhpI8-w113eSxlPbYeQpQveCIKKX25CKV1DkgyCJ9DN1PTeoQf9cU1PX-T-QvuimhOskpAY1aIF?key=SWtClCBzkj7TSIatblqhIGY5)

# **Our Asks**

🆓 Try the leading AI browser agents for FREE on HyperPilot: [pilot.hyperbrowser.ai](http://pilot.hyperbrowser.ai)\
🛠️ Developers, get your free API key and start building: <https://hyperbrowser.ai>\
🔥 Share your favorite models and use cases with us on [LinkedIn](http://linkedin.com/company/hyperbrowser) and [X](http://x.com/hyperbrowser)

## Hyperbrowser MCP Server - Connecting AI to the Web 🌐 🤖

**TL;DR:**

Give your LLMs / IDEs superpowers by connecting them to the web with Hyperbrowser's MCP. Unlock deep research, coding with live documentation, data extraction, and browser automation capabilities in 2 minutes. Install in seconds with `npx -y hyperbrowser-mcp` and use with Claude Desktop, Cursor, Windsurf, or your favorite MCP client.

**ASK:** Building AI agents, developer tools, or research applications? Email us at [shri@hyperbrowser.ai](mailto:shri@hyperbrowser.ai) or [akshay@hyperbrowser.ai](mailto:akshay@hyperbrowser.ai)

<https://www.youtube.com/watch?v=HUA4uPwcS8U>

## ❌ The Problem

LLMs are powerful but isolated. They can't:

* Access real-time web information
* Interact with websites to complete tasks
* Generate code using up-to-date documentation (even OpenAI API calls are sometimes botched)
* Extract structured data from multiple sources in real-time

## 🛠️ Our Solution

Hyperbrowser MCP Server connects LLMs directly to the web through Anthropic's Model Context Protocol.

`$ npx -y hyperbrowser-mcp`

**Our MCP Server exposes 7 powerful tools:**

\- **Web data tools:** scrape_webpage, crawl_webpages, extract_structured_data, search_with_bing

\- **Browser automation:** browser_use_agent, openai_computer_use_agent, claude_computer_use_agent

Your favorite MCP client can use the web data tools to surf the web for real-time information and data + use the browser automation tools to take actions like ordering a pizza or commenting on a GitHub pull request.

## 💡 What You Can Build

* **Deep Research in Cursor:** Claude, Cursor, and Windsurf can use Hyperbrowser's MCP server to do extremely deep research on any topic. No need for $200/mo ChatGPT Pro.
* **Faster coding with AI:** Generate working code with current API docs, automate code reviews, build integrations
* **Extract Data:** Convert web content to structured datasets, right in your claude app
* **Automate Tasks:** Test applications, submit forms, automate UI tests

Check out this video of my cofounder vibe coding a whole game with Cursor and Hyperbrowser's MCP Server:

<https://www.youtube.com/watch?v=wT89pY6zW4o>

## 🙏 Our Asks

* **Try it out!** Get a free API key at [app.hyperbrowser.ai](http://app.hyperbrowser.ai) and install in your clients (instructions here - [github.com/hyperbrowserai/mcp](http://github.com/hyperbrowserai/mcp))
* **Share this post** with AI devs and researchers
* **Connect with us** at [shri@hyperbrowser.ai](mailto:shri@hyperbrowser.ai) and [akshay@hyperbrowser.ai](mailto:akshay@hyperbrowser.ai)
* **Follow us** at [x.com/hyperbrowser](http://x.com/hyperbrowser) and [linkedin.com/company/hyperbrowser](http://linkedin.com/company/hyperbrowser)
* **Join our community** on Discord - <https://discord.gg/zsYzsgVRjh>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88849&key=user_uploads/233736/98d7ef01-89f4-475b-af5b-90679a5f3097)

## Hyperbrowser - Web infrastructure for AI agents

## TL;DR

Hyperbrowser is AI's gateway to the web. We make it dead simple to give your AI agents reliable, scalable scraping and browser automation capabilities without getting blocked or dealing with infra headaches. One API call to HB gives you a browser session with built-in stealth mode, proxy rotation, automatic CAPTCHA solving, session management, session recordings etc. Hyperbrowser is the only browser platform that lets your agents spin up 100s of concurrent browsers with sub-second start times.

<https://www.youtube.com/watch?v=LZIPzjyEuGU>

## Why is this important? And why now?

The web wasn't built for AI—but AI needs the web. In 2025, Agents are finally here. We've met so many companies building web-based agents who keep running into the same problems:

* They keep getting blocked
  * Websites detect and shut down automation, making it hard to scale AI-driven browsing.
* Web automation at scale is a nightmare to manage
  * Managing browser infrastructure is expensive, slow, and unreliable—especially when running thousands of concurrent sessions
* High latency
  * High latency creates a terrible user experience and leads to frustration

The future is AI-driven agents that browse, transact, and take action. Hyperbrowser enables Agents to reliably interact with the web.

## Our Solution

**Core Infrastructure**

* Launch thousands of undetectable browsers in <1s
* Built-in anti-detection & stealth mode - bypasses anti-bot systems and fingerprinting
* Automated CAPTCHA solving
* Ultra-low latency globally distributed infrastructure

**Developer Experience**

* Multiple levels of abstraction:

```
// High-level API for instant results
const data = await client.scrape.startAndWait({
  url: "https://example.com",
  solveCaptchas: true
});

// Or fine-grained control when you need it
const session = await client.sessions.create();
const browser = await connect({ 
  browserWSEndpoint: session.wsEndpoint 
});
```

* Full compatibility with Puppeteer, Playwright, and Selenium
* Comprehensive session management and monitoring
* Live stream APIs for real-time session data
* Native integrations with LangChain, LlamaIndex, and more

**Infrastructure & Scaling**

* Instant browser session startup (<1s)
* Scale from 1 to 1000s of concurrent sessions
* Flexible pricing tiers to match your needs
* No infrastructure management required

## What People Are Building with Hyperbrowser

* Web research agents automating sales and marketing research
* AI agents booking flights and analyzing markets in real-time
* Testing teams running 500+ concurrent browser sessions
* Companies collecting training data for AI models at scale
* Automated KYC/KYB processes with built-in compliance

## Get Started

* Try it free at <https://hyperbrowser.ai> 
* Join our Discord - <https://discord.com/invite/zsYzsgVRjh>
* Follow us on X - [x.com/hyperbrowser](http://x.com/hyperbrowser)
* Follow us on LinkedIn - [linkedin.com/company/hyperbrowser](http://linkedin.com/company/hyperbrowser)
* Email us directly: [akshay@hyperbrowser.ai](mailto:akshay@hyperbrowser.ai) or [shri@hyperbrowser.ai](mailto:shri@hyperbrowser.ai)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87074&key=user_uploads/556017/8dc23770-3861-4ce3-8426-ef5be417d5d6)
