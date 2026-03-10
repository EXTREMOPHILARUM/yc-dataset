# Launches

## Parse - APIs for any website

# **Launch BF: Parse - Build APIs for any website that are 100x faster than headless browsers**

TLDR: [Parse](http://parse.bot/) reverse engineers websites and builds deterministic APIs for scraping and web automation. Instead of spinning up slow, expensive headless browsers, Parse makes deterministic APIs that use direct network requests that **cost fractions of a cent and return in milliseconds**.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95327&key=user_uploads/986516/c6b55ddc-9855-4030-84b7-a70e251330da)

**The Problem**

Headless browsers are the default for web scraping and automation, but they're painfully slow and unreliable at scale. Scraping thousands of dynamic pages with Playwright or Puppeteer takes hours, often failing halfway through due to timeouts or memory issues. Repeat tasks become absurdly expensive at scale due to the cost of managing hundreds of concurrent browsers.

**How Parse Works**

We reverse engineer the underlying network requests behind any action on a website and build a deterministic API to replicate it. Parse automatically handles dynamic values (session cookies, CSRF tokens, etc.), IP rotation, and antibot challenges.

Parse is able to build a set of endpoints to handle dynamic multi-turn interactions, such as getting the questions on a job application through one endpoint and submitting the job application through another endpoint, **even though every application has unique questions**.

Demo: https://youtu.be/UZGYkH2vAS4

All of this means that the APIs that Parse generates execute in seconds and cost fractions of a cent to run.

**Background**

I started coding at 12 to build bots to purchase limited edition sneakers in seconds. After leaving that scene, I led engineering at a trading card market platform and researched political botnets at Berkeley. No matter where I went, I realized how crucial live web data and interaction is and how slow current solutions are. I launched the first version of Parse in August and got to 35k users in a month.

**Asks**

* **If you're using headless browsers for scraping or automation, let's chat.** We're launching document downloading and auth handling in the coming weeks and want to hear your pain points. If you need custom solutions build out, please email me at [alex@parse.bot](mailto:alex@parse.bot)
* **Try Parse today** - [**Parse.bot**](http://Parse.bot)
