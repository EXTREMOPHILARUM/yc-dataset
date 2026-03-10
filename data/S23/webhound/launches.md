# Launches

## Webhound Reports: Deep research that scales with your budget

Hey everyone, Moe here.

We're building Webhound — AI research agents where you set a budget and the agent keeps researching until it runs out. More budget = more sources, more depth.

**How we got here:** We started with a product (now called Datasets) that builds structured tables from the web. It worked, but we hit a wall: as datasets got bigger, costs exploded and context became unmanageable. And for open-ended datasets, we never had a clean answer for "when should the agent stop?"

So we rebuilt everything around two ideas: costs that stay linear with time, and giving users direct control over depth.

The new architecture is a **Planner-Executor-Verifier loop**. Executors get fresh context each run. Planner and Verifier work from summaries and can search over what's accumulated. Runs until budget's out.

We tested it on traditional deep research as a sanity check. At $3-5, it beat the top result on DeepResearch Bench. At $15, it way outperformed it, even running on older models (gemini-2.5-flash). So we shipped it as Reports and put the same architecture into Datasets.

**We now have two products:**

* **Reports** = cited research docs (competitive analysis, market research, system design). Always uses the full budget—more budget means more sources and deeper coverage.
* **Datasets** = build structured tables from the web, or upload your own and enrich with new columns. We can access LinkedIn, YouTube, Reddit, and most other sites. Examples: lead lists with company info, competitor feature matrices, lists of VCs filtered by thesis, GTM leads with emails. Stops when complete, or at budget, whichever comes first.

**Asks:**

* **Try it** – [**webhound.ai**](http://webhound.ai), $5 free. Honest feedback welcome.
* **Spread the word** – if it's useful, share it with anyone you know doing a lot of research (investors, analysts, consultants)

– Moe

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97405&key=user_uploads/1444435/fceaddd4-53f4-438f-930d-a4bf18bf97ce)

(Demo Video for Reports: [**https://www.youtube.com/watch?v=eEGJBudvmsE**](https://www.youtube.com/watch?v=eEGJBudvmsE))

## Webhound: An AI Agent That Builds Datasets From the Web

Hey everyone,

We’re [Moe](https://www.linkedin.com/in/moe-khalil-73a2371a1/) and [Theo](https://www.linkedin.com/in/theodor-schmidt/), and we’re building [Webhound](https://webhound.ai).

# TL;DR

Webhound is an AI research agent that builds custom datasets from web research. Instead of spending weeks manually gathering data, simply describe what you need and Webhound automatically finds, extracts, and organizes it into structured datasets you can export.

Some examples are:

* “Find 100 AI/ML YouTubers with 50K-100K subscribers, their email addresses, and latest video view counts.”
* “Track pricing, features, and customer reviews from both Reddit and Youtube for 30 CRM competitors including Salesforce, HubSpot, and Pipedrive.”
* “Collect 500 vacation rental listings in Bali with photos, pricing, amenities, and guest reviews from multiple platforms to analyze market trends.”
* “Identify 200 early-stage e-commerce startups on Shopify or WooCommerce, along with founder names, contact emails, and product categories to build a lead list.”

https://www.youtube.com/watch?v=cG1SiKznpHs&pp=0gcJCcEJAYcqIYzv

# **❌ The Problem**

Data collection is painfully manual and slow. Need to research 100 competitors? That means visiting 100 different websites, copying information into spreadsheets, and repeating this process for every data point.

This creates two major problems:

* **High effort:** Hours of tedious manual work, clicking through sites, and organizing data
* **Slow speed:** What should be quick research turns into weeks of work

# **👷 Our Solution**

Webhound makes data collection effortless and fast.

**Effortless:** Simply describe what you need in plain English. Webhound handles everything in the background while you focus on other work.

**Fast:** A fleet of parallel search agents collect data simultaneously across multiple sources, turning weeks of manual work into hours.

Export clean, structured datasets as CSV, Excel, or JSON.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92035&key=user_uploads/1444435/a0229371-c973-42ca-8383-bf35d6bb99c7)

# **🙏 Our Ask**

Want to try Webhound? Access is currently limited to 5 datasets per week and one at a time, but if you're interested in higher limits to automate your research workflow, please reach out to us at [**team@webhound.ai**](mailto:team@webhound.ai).

# 👬 **The Team**

Moe and Theo have been friends for 6 years and were roommates in college (in the room where Evan Spiegel founded Snapchat).

Since graduating, Moe’s built a bunch of AI search tools, including Instaclass (turn any topic into a full search-backed course) and Remy (think Perplexity, but for video).

Theo went deep on data, building and scaling Quicklime, where he helped film studios and streaming services collect the info they needed to make smart bets.

## Remy: The chatbot that's seen every video on YouTube

![](https://www.ycombinator.com/media/?type=post&id=85709&key=user_uploads/1444428/e4dd006c-a312-4c90-9340-6b403f9bd17a)

The internet is filled with incredible video content, but finding the exact moments you're looking for can feel impossible. 

Currently, typical video search falls into one of two categories:

**1. Searching short-form video content**

* Search TikTok or YouTube Shorts for clips made by creators.
* Settle for recommended clips that don't quite match what you need.
* Get filtered back into _the algorithm_.

**2. Manually looking through long-form videos**

* Open ten tabs with the top results on YouTube to look through them all.
* Waste time scrubbing through long videos looking for the moments you want.
* Miss valuable insights buried in obscure content.
* Give up searching altogether.

### We built Remy to solve this.

Instead of treating videos as single units, [Remy](https://www.useremy.com/) understands what's happening inside every second of every video. It's like having a brilliant research assistant who's watched everything on the internet and can quickly find the exact moments you care about.

Think of all the knowledge trapped in hour-long podcasts, conference talks, interviews, and tutorials. Remy sets it free by building you personalized playlists that connects the dots across thousands of sources—turning an overwhelming sea of content into a clear story that matters to you.

<https://youtu.be/3n0zeaghQVs>

## **🔎 How Remy works:**

1. Tell Remy what you're curious about
2. Remy searches through the internet's video content
3. Remy curates a playlist of perfectly clipped moments for you to watch

## **✨ Perfect for:**

* 📚 Learning new skills: **"Gordon Ramsay explaining expert knife techniques"**
* 🎯 Product research: **"Professional skiers talking about best skis of 2025"**
* 🔍 Deep dives: **"070 Shake talking about the music scene in New Jersey"**
* 📰 News & updates: **"What does Sam Altman think about what's happening with AI regulation?"**

## **🤨 What makes Remy different:**

* Real-time search across billions of videos
* Smart clipping that captures full context
* Conversational interface for natural discovery
* Playlists that make sense for your search, not just random clips

As your searches evolve, Remy understands the context and narrows down results in real time, finding clips that otherwise might be buried deep within hours-long videos. Have questions about a clip it found? Just ask in the chat and get answers rooted in the content Remy found for you.

### Give Remy a try today to discover videos you never knew existed.

<https://www.useremy.com/>

## Instaclass: Make a masterclass on literally anything

[Instaclass](https://myinstaclass.com/) lets you make a masterclass on anything you want, using the best content that's already on the internet.

We’ve spent the last year building and launching in the AI content consumption space, from games to podcasts to news to videos. What we’ve learned is that we don’t need AI to create content for us. Everything you could possibly need or want to consume has probably already been created; _it’s just hard to find, and you don’t always know what to look for_. Instead of using AI to create content, we believe AI should play a role in curating human-made content.

On the back of all of this work and these insights, we have built [Instaclass](https://myinstaclass.com/).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80492&key=user_uploads/1444428/f9dbfab3-e0c1-4518-ae87-ba05f3caf9b5)

[Instaclass](https://myinstaclass.com/) lets you build classes on anything you want, no matter how niche, doing the hunter-gatherer portion of research for you so you don't need to spend a day trawling through the internet looking for good content to learn with.

We use Instaclass daily to learn about [_brewing better coffee_](https://myinstaclass.com/home/0510f5fd-420c-4023-b394-39c3c6074c1e/f4157ffb-def7-44b8-bb6a-80c933ed3054)_, _[_the Fallout universe and lore_](https://myinstaclass.com/home/0c315ab0-a562-46d5-94e5-8013f3be40d3/3b0fdf63-c6a6-4feb-a883-b8f207409810)_, _[_the French Revolution_](https://myinstaclass.com/home/0cf5ac0a-025b-455b-9e17-344d221cec2f/347c6edc-6b41-43c8-8a0b-2ec32471f6a8)_, and _[_cooking tips from Gordon Ramsay_](https://myinstaclass.com/home/0510f5fd-420c-4023-b394-39c3c6074c1e/acbcc328-a9a1-4158-a892-2a04b8d5c830)_._ We’ve joked that this would have been really helpful in the early days of each of our previous pivots - if you know us, then you’d know this one on [_how to build video games_](https://myinstaclass.com/home/1d5a2b90-86c1-471a-933c-6903d1f93206/443c077a-34bc-400a-abc3-6284d6a3e1e7) would have been worth its weight in gold.

_Users have done everything from learning _[_how to give a sales pitch for an interview_](https://myinstaclass.com/home/8ee4cb8a-0ab4-4d88-83c2-50d582fe1adb/9be936bd-c058-4ad8-be2d-f292bd1059e9)_ to _[_how to be nice to your boyfriend_](https://myinstaclass.com/home/1db8a552-515d-4029-9eba-68c807329668/299d2703-4b49-4743-a83a-d9168cbc3874)_._

[Instaclass](https://myinstaclass.com/) pulls in information from across the web on a particular topic and puts it in a course format so you can go in with no idea about a topic and come out decently well-informed.

Try it out, and let us know what you think! We are limiting free credits at the moment, so if you run out, join the waitlist, and we’ll email you when more become available. Looking forward to seeing what you all make!
