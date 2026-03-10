# Launches

## Autumn: Stripe for AI Startups

[Autumn](https://useautumn.com) is a layer over Stripe that makes it 10x easier to setup your app’s free / paid plans, and manage them as you grow.

### **The Problem**

* Stripe is low level and it’s hard to build AI pricing. There’s 5 different functions to manage subscriptions, 5 different brittle webhooks and a bunch of DB tables you need to maintain (gate features, track usage etc)
* When you change pricing (which AI companies do A LOT), everything needs to be ripped out, replaced with different product/price IDs and migrated. This really sucks.

### **What’s Autumn?**

Autumn is your app’s DB for your customer’s subscription state, feature permissions and usage tracking. You make queries to us and we’ll tell you if a customer can access something:

1. Model your pricing plans in our dashboard / CLI (set pricing, feature limits, usage-billing, credits etc)
2. **/checkout** to handle billing. Use the same function for new subs, upgrades/downgrades, add-ons etc
3. **/track** usage events when a customer does something (eg uses a credit)
4. **/check** for feature access to handle usage limits / paywalls. Autumn tells you yes/no in realtime.

We built the integration so that it can be reused no matter the pricing model (including org / centralized billing). When you want to change pricing, just update your dashboard / config file, migrate any customers you need to and everything’s done. You can also set custom pricing for enterprise customers in a similar way.

https://youtu.be/0IBujDkuieE

It’s open source, used in prod by 100s of developers, and by YC startups that are processing millions.

“The only thing I regret is not moving onto Autumn sooner” (one YC founder we work with)

### **About us**

We were in the F24 batch building software for banks, before pivoting the day before demo day. We pivoted around for a few months before stumbling on this. Now we’re raising with S25.

**Ayush** — I was a PM at a company called checkout .com (Stripe competitor)

**John** — I studied computer engineering at Imperial College London, and have been building things / devtools for 6 years.

(and we do really ❤️ Stripe)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92737&key=user_uploads/642208/a6c05ab4-5544-41ea-9366-debe2aa4f636)
