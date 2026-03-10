# Launches

## BrowserBook - The Browser Automation IDE

Hey YC!

We’re [Chris](https://www.linkedin.com/in/cschlaep/) and [Jorrie](https://www.linkedin.com/in/jorrie/), cofounders of [BrowserBook](https://www.browserbook.com).

https://youtu.be/FkaGHhJWy1w

# **TLDR**

We make it trivial for developers to write reliable web automations.

# **Ok, but _what is it?_**

BrowserBook is an IDE that puts all the tools automators need in one place, so the iteration loop to write, test, debug, and deploy web automations is significantly reduced.  It combines:

* **A Jupyter-like coding environment** where developers can run code cells individually,
* **An inline browser** to run automation code against
* **A Playwright coding agent** that can write the automation for you
* **A bunch of built-ins** for taking screenshots, extracting data, and authentication

And, once you’re done writing your script, you can deploy it and trigger it via our public API.  It’s super easy!

# **But browser agents are a thing, right?**

Yes, and we’re not using them.  We built BrowserBook because of the shortfalls we experienced with browser agents and the pain of actually writing reliable scripts.  At a very high level, in the AI world you can take two approaches to web automation - write scripts, or use browser agents.

1. **Use browser agents:** ostensibly more flexible, but expensive, slow, and unreliable
2. **Write scripts:** fast and debuggable, but infamously brittle

Which leads us to…

# **The problem (and how we got here)**

**Sometimes we need machines to interact with web pages, which are made for humans.**

This is basically the whole challenge.  There’s a lot of reasons we might want machines to poke around on the web:

* Agents using a browser to interact with the web to perform actions like humans, especially when they can’t use APIs
* Scrapers to gather data that’s useful for our business
* UI tests that can interact with a website the way a human would to ensure everything’s working as intended
* Workflow automation via RPA

We tried **browser agents** in our pre-pivot days to automate healthcare workflows. They mostly didn’t work; they were an order of magnitude more expensive than scripts, slow because of all the context they needed, and tended to drift when workflows got complex.  When they did drift, fixing them was just tedious prompt-massage and trial-and-error.

We ended up giving the agent a library of scripts to execute, and came to realize scripting was simply the better solution for reliable enterprise workflows; they’re deterministic and therefore inherently debuggable, not to mention their cost and speed advantage.  They with a host of issues though:

* **Websites change often** causing scripts to break. We needed a way to quickly diagnose and iterate on our scripts.
* **Setting up browser and filesystem infrastructure** is not easy but very necessary in the web automation world.
* **It’s just annoying to write scripts** - if you’ve ever had to dig around for selectors, you know: it’s tedious and time consuming.

So we built BrowserBook to solve those issues.

# **How does it work?**

1. **Run code piecemeal** - if you’re fixing a breakage 2/3rds of the way through your script, you shouldn’t have to run the whole thing every time you test it.  We took inspiration from Jupyter notebooks and allow you to run code cells independently, while maintaining context and state:

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=96111&key=user_uploads/739375/f2203cd4-1533-402c-8b17-3147d3d21783)

2. **No more digging for selectors** - tell the coding assistant what to do and it’ll implement the automation logic in Playwright:

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=96111&key=user_uploads/739375/418daacd-b744-4359-84d3-23891d386676)

3. **Built-ins for the hard stuff** - want to take a screenshot?  Log in to a website with 2FA?  Extract data?  We’ve got built-ins for those, ready to go out-of-the-box.

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=96111&key=user_uploads/739375/2acfea26-9c65-4ba4-8983-8e351e75222a)

4. **Accessible via API** - if you need to execute your automation via an agent you’re building, scheduled via a cron job, or as a part of your application, you can trigger automations remotely and watch the playback in-app or via our artifacts API endpoint.

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=96111&key=user_uploads/739375/957ce254-3702-407f-890d-ed8c184824e7)


# **Our ask**

Try it out!  If you:

* Run browser automations
* Are building agents that need to interact with the web
* Need to write a one-off automation that will make your life easier

BrowserBook is available for download for Mac users [on our website](https://browserbook.com/), and if you’d like you can [book a demo here](https://browserbook.com/demo).

Additionally, if you know individuals, startups, or teams at larger companies working on browser automations, we’d love to meet them!

## Chorrie: turn your SMEs into SWEs

# **TL;DR**

We supercharge your subject matter experts by giving them the tools they need to eliminate errors in heavily manual processes.

**Our current mission:** empower healthcare practices to stop denials and under-billing on their claims before they happen.

# **The Problem**

Healthcare claims processing is an overly-complex, adversarial space. Insurance payers are constantly changing their policies, forcing billing teams to rely on:

* frequent and extensive retraining
* coding rules worksheets with hundreds of tabs
* esoteric tribal knowledge

With so much room for human error, it’s no wonder 73% of healthcare staff surveyed reported that they’re facing increasing denials on outgoing claims.

# **A turnkey solution for medical claims checks**

[Here’s where Chorrie comes in.](https://youtu.be/orI95bsgaio)

Chorrie uses AI to empower medical practices to turn their esoteric knowledge into automated checks, saving time, money, and mental effort. We take simple, deterministic instructions, and translate them into a code-based decision tree, which can be continuously run to automate correctness checks for complex rules systems.

Take the example in our video: we get a glimpse at how extensive these rules worksheets can become today, and see how quick & easy it is to automate a rule for claims from a particular location, containing a particular code, billed to a particular insurance payer with Chorrie.

# **Backstops-as-a-service**

Our approach of plaintext ➡️ decision tree ➡️ code generation is a scalable technique that can be used to provide backstop checks (and ultimately automate) high-leverage, deterministic manual processes that are prone to human error (think contract review for legal documents, trade confirmations, etc.).

To automate checks for these today, you’d need a team of engineers to write the logic into code, and keep them on staff to ensure that code can be updated when the rules change. **With Chorrie, you get:**

* A no-code solution: turn your SMEs into SWEs
* No hallucinations in your automated workflows
* Intrinsically deterministic & fully explainable conclusions

While the focus today is on reducing claims denials to 0% for our healthcare clients, we plan to explore use cases in other fields in the future.

# **About us**

We are Chris (the **Ch**) and Jorrie (the **orrie**), old friends who met in undergrad at MIT. We met back up years later at Google, where we worked on applied AI for content moderation before we decided it was time to move onto something new.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85580&key=user_uploads/739375/ce57cfdc-3b8c-41dc-a8bb-d4bccc866ab0)

After brainstorming on a number of projects, Jorrie’s wife, an ophthalmologist, gave us the idea of applying AI to the medical coding world and the rest is history!

# **Our ask**

Do you have any tedious or high-leverage manual processes where errors can cost your business money (Think heavy manual review processes, major transactions that need to be verified, etc.)? Or any contacts in the medical billing world? We’d love to chat.

📧 [**founders@chorrie.com**](https://mailto:founders@chorrie.com)
