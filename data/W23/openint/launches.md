# Launches

## ⭐️ Evefan — Self-hosted Segment alternative — 99% savings w/ Cloudflare Workers (OSS)

**TLDR;** Evefan enables developers to privately capture, transform, and deliver customer events at internet scale. Evefan is open source and self-hosted on Cloudflare workers. It can be configured either via our Evefan Console or via Wrangler. With Evefan, organizations can save > 99% when scaling events.

**Need help scaling events**? Let’s talk! <https://cal.com/amadeo-evefan>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83175&key=user_uploads/702191/93a130d5-d424-4400-aa4b-cf7b7873e01c)

### ❌ Problem: Scaling Customer Events IS HARD

Before joining YC, I led a large portion of the Blockchain.com consumer product. At the time, we had the most popular crypto wallet with over 60M accounts. We only made money on a subset of users who used our ‘premium’ features. 

As a result, **we could not afford to understand how free users used our product**. We got seven-figure quotes (😱) from the top vendors in the Customer Data Platform (CDP) space and tried to self-host several alternatives. Imagine a PM team considering whether adding an event is worth XXXX dollars. Silly. 

All the products we self-hosted then fell over at our scale. We had to build our own, more narrow version for our use case. There’s a reason for it—you could even say that it’s a dark industry secret.

**😭 Self-Hosting Is Meant To Be Practical**

Existing OSS alternatives in the market are all built with massive multitenancy in mind. **They’re not meant to be practically self-hosted**. Most of them tell you in their docs to only self-host for toy projects or require overly expensive closed source ‘high availability’ add-ons that they can only configure for them to work correctly. That’s OK; they serve a different use case. 

Look at the architecture of the top self-hostable alternatives in the space. Imagine asking your SRE team to ‘simply’ set these up and keep them highly available (even with Docker & Kubernetes, it's not core work).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83175&key=user_uploads/702191/e695acc0-3cd3-4580-9e0e-38cfdcc543ac)

### ⭐️ The Solution: Evefan

1. **Segment compatible**: this means you can use the battle-tested Segment SDKs in your preferred programming language.
2. **Deploy to Cloudflare**: Configure Evefan instance via our console with your Cloudflare API key or yourself via Wrangler. Evefan will create a bundle with just your destinations small enough to run on Cloudflare. 
3. **Transform and Deliver To Your Destinations**: We’ve made Bigquery and Postgres work so far. We also added Mixpanel just for fun. We’ve reviewed the top data warehouses and are confident we will natively support them.

Over time, Evefan will become an indispensable part of your async events delivery infrastructure. Use cases like in-and-out webhooks, queues, pub-sub, and jobs are coming! 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83175&key=user_uploads/702191/6a355a35-8aa4-4410-8701-72aef7a364e0)

**😻 It’s 99% Cheaper Than Alternatives & Built For Scale**

Here’s why: We follow a Bring Your Own Compute (BYOC) model. When Evefan runs in your infra, it roughly incurs $70 of Cloudflare worker compute for every 100 million events processed. This is 99.5% cheaper than Segment and similar alternatives! Of course, price is not the only reason people self-host. In Finance and Healthcare, for example, it is often the only practical option.

### 🙌 Our Asks

1. **Please Star** our Github repo ⭐️<https://github.com/evefancom/evefan>   
2. **Let's Partner**: We’ve been working with our first two design partners and are searching for our next three! Does your organization process over 10M monthly events and struggle to scale? Let’s chat! <https://cal.com/amadeo-evefan>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83175&key=user_uploads/702191/2c6b777e-4227-4b61-b4b2-5d4e0b270ba1)
