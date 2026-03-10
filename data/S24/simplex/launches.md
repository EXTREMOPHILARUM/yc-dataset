# Launches

## Simplex - enterprise-grade web agents

Simplex builds enterprise-grade web agents that companies use to integrate with legacy portals. We handle everything from building the web agents for you to integrating directly with your existing software stack like forward deployed engineers.

Customers use Simplex in production right now to:

* submit information from outbound calls into freight software
* edit and download their customers’ invoices
* fetch websites’ internal APIs
* and more.

https://youtu.be/97gX3I9PMZ0

# The Problem

Legacy portals aren’t well suited for web agent automation — portals are unintuitive to navigate and functionality is often broken.  Existing web agents like Operator lack fine-grained control over agent behavior and can’t consistently perform these critical legacy workflows.

A fully autonomous AI might fail to reach the desired page, get stuck pressing a broken button, or mistype critical information like an invoice amount or a shipping address. Without control over agent behavior and clear observability during workflows, web agents are blocked from being used during production in these critical scenarios.

# The Solution

Simplex is the production-grade web agent platform that enables AI agents to reliably do work on legacy portals at scale. You can see a live demo of Simplex below – the demo is at 1x speed.

https://youtu.be/4VSexxYptV4

We’ve engineered Simplex to give AI agent developers control, transparency, and reliability. With Simplex you can:

* easily **integrate with your existing stack** – pass the results from LLM calls, databases, your existing agents into Simplex
* **cache element actions** for speed and consistent performance
* build **strong evals** to stress-test your workflows at scale and emulate production conditions
* scale up to **100s of concurrent browser sessions** while handling CAPTCHAs, 2FA, and website authentication on your customers’ portals
* ensure **no incorrect actions** are taken — if you prompt our agents to click on elements that don’t exist on the page, we'll raise an exception
* debug with shareable **session replays** and **detailed agent logs**

# The Team

[Shreya Karpoor](https://www.linkedin.com/in/shreya-karpoor/) and [Marco Nocito](https://www.linkedin.com/in/marco-nocito/) are MIT grads who’ve spent years doing computer vision work at Waymo, Tesla, and within MIT labs. They’re excited to use their expertise to bring reliable web agents into widespread production.

# 

# Our Ask

* [Book a call here](https://cal.com/marco-nocito-kon7ng/30min) if you want to request API access.
* [Visit our website here](https://www.simplex.sh/) to see a live demo of Simplex.

## Simplex - Web automation for developers

**TL;DR:**

* Simplex is an API that allows you to automate manual workflows on the web. For example, a customer uses us to autonomously purchase materials from Amazon, poll their email inbox for tracking information, then update their internal documentation with that tracking info every six hours.
* Book [time with us here](https://calendly.com/simplex-interest/marco-chat) if we can help you automate your business.

Hi everyone, we’re [Shreya](https://www.linkedin.com/in/shreya-karpoor/) and [Marco](https://www.linkedin.com/in/marco-nocito/), two MIT grads building Simplex.

Teams are often burdened by manual tasks that have to be repeated thousands of times per month — for example, populating spreadsheets with information from recent emails. From our experience, we found that asking AI agents to solve these problems just didn’t work. They often didn’t follow the same path when we asked them to do the same thing twice, and we couldn’t control any of the actions they took when they made a mistake.

So we built Simplex to inject intelligence into repeatable, known workflows to help you automate your manual tasks.

With Simplex, writing a function to pull tracking information from your email is as easy as this:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87190&key=user_uploads/910356/27f7171e-7a04-408e-84f9-d7596b9a2e5b)

**Watch a quick demo here:**

<https://www.loom.com/share/9d99e4fdf9e14487ba340d5565c123a2?sid=1d3b2dd6-5e78-4370-bbca-1949fc72eb8e>

A few reasons customers love Simplex:

* **Straight-forward, reliable intelligence:** We break up your web workflows into smaller, more atomic actions (click, type, extract) to enforce while allowing you to leverage the intelligence of AI.
* **Extract anything on the web:** We’ve built our own vision system to more accurately extract small icons, text, images, or even entire sections of a page.
* **Run on any site, even internal tooling:** We store your credentials securely to handle website authentication, meaning you can use Simplex on any website or private tooling you have access to.
* **No need to deal with browser infrastructure yourself:** We handle all the infrastructure, hosting, and scheduling, letting you run these workflows asynchronously at scale.

People have requested Simplex to:

* **act as procurement software:** automatically order parts and update internal spreadsheets with delivery information across multiple vendors (Amazon, DigiKey, etc.)
* **scrape financial information for their hedge fund clients:** pull daily headlines and perform sentiment analysis across hundreds of financial websites for quantitative analysis research
* **autonomously update their internal database of products:** aggregate manufacturer marketing information for over 2,000,000+ retail products
* **do the work of an entire data collection team:** collect grant and award information from over 700 government websites
* and more…

## Our Ask

* We’re looking to onboard teams, especially those that are burdened by manual processes or need to scrape hundreds of thousands of websites. Book a [meeting with us](https://calendly.com/simplex-interest/marco-chat) for a demo and API access. We’re happy to write your first automation for you.

## Simplex: on-demand photorealistic vision datasets

**TL:DR;** Simplex creates photorealistic vision datasets rendered from 3D scenes for AI model training. Submit a request [on our website](https://simplex.sh/#data-request-form) to receive high-quality data and labels.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83077&key=user_uploads/1588677/826c7bea-8936-451d-97ff-895bc8ca6c38)

**Data request for the above sample:** _“Generate images and labels of a home kitchen with household objects on a center table. I need a variety of household objects in a variety of lighting conditions. Our desired labels are semantic segmentation and depth maps.”_

Hi everyone, we’re [**Shreya**](https://www.linkedin.com/in/shreya-karpoor/) and [**Marco**](https://www.linkedin.com/in/marco-nocito/), two MIT grads building Simplex.

Collecting vision data for model training is time-consuming, costly, and often unsafe. Shreya spent over 200 hours physically operating a robot to collect image training data during her research at MIT. Marco worked on machine learning for synthetic data at Waymo to solve this exact problem.

We realized data scarcity wasn’t just an issue in robotics – it affects any company training vision models. When fine-tuning foundation models or building a new dataset from scratch, teams must curate existing data or label and collect data themselves. 

We resolve the data scarcity problem by generating photorealistic ground truth labeled datasets for **any scenario**. We can generate **millions of varied images** **from 3D scenes** using our physics engine pipeline.

Here’s how you’d use Simplex:

1. Fill out our data request form [here](https://simplex.sh/#data-request-form) – it takes less than a minute. 
2. Give us feedback on a few sample image/label pairs that we generate. Repeat if necessary.
3. Once you’re satisfied, download your complete dataset.

We support semantic segmentation, captions, simulated LiDAR, depth maps, and bounding boxes. You can generate large volumes of randomized scenes or provide a CAD/phone scan model for more specific scenes.

# **Our Ask**

* If you or someone you know needs vision data, fill out our 30-second data request [form.](https://www.simplex.sh/#data-request-form) We’re taking a limited number of early customers.
* If you have a more complicated request or would otherwise like to contact us, email [shreya@simplex.sh](https://mailto:shreya@simplex.sh).

# **The Team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83077&key=user_uploads/1588677/d2e5778c-86c2-4c7b-bc75-3c73aefff883)

[**Shreya**](https://www.linkedin.com/in/shreya-karpoor/): Computer science (BS and MEng) at MIT, software engineer at Tesla and Viam. Built simulation pipelines for locomotion and dexterous manipulation research at MIT. \
[**Marco**](https://www.linkedin.com/in/marco-nocito/): Computer science (BS and MEng) at MIT, software engineer at Waymo, Bloomberg, and Viam. Built machine learning models to generate synthetic data at Waymo.
