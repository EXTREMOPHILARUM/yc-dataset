# Launches

## Flowglad: the Open Source, Zero Webhooks Payments Provider

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96121&key=user_uploads/272109/b208b526-0dbf-4690-bd7b-416bc0c20ae2)

**Flowglad** is an open source payments provider that requires **zero webhooks**.

It’s designed so that your AI can **one shot payments with just copy, paste, enter** for virtually any pricing model.

https://youtu.be/sZkv1niV-Vc

# TL;DR

* We generate a **bespoke integration prompt** for your coding agent **based on your pricing model and codebase**, so you don’t need to deal with docs
* **Use Flowglad as the source of truth**: read what features and usage credits your customers have based on their billing state
* You don’t need to store any ids from us on your side
  * Refer to prices, features and meters using slugs
  * Refer to customers using their id in your DB

# Asks

* Try Flowglad out for your next project, get started [here](https://www.flowglad.com/)
* Check out our [Github](https://github.com/flowglad/flowglad/), where you can see all of our billing logic

# Problem

Even a minimal payments integration for a SaaS requires:

* Choreographing at least 16 individual server-client boundary crossings
* Maintaining mappings between your payment processor and your DB across at least 3-5 different entities (prices, plans / products, customers)
* Handling race conditions

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96121&key=user_uploads/272109/99803326-387d-4a8d-b4de-4755f6b12b63)

And that’s just to accept a payment. You then need to write a bunch more code to map what features your customers can access based on their subscription.

The result is a bunch of glue code that you have to maintain to keep your app’s DB in sync with what happened in your payment processor. You sync your DB through webhooks which are brittle, create race conditions, and often one of the hardest parts of your app to test.

And whenever you want to change your pricing, this code is the most liable to break.

# Solution

Flowglad gives you solid state payments. It eliminates glue code.

### 1. Source of truth

Like other payment providers, we handle the money movement for you. But unlike others, we also give you a source of truth for what your customers get access based on their billing state. You can check your customers’ access and create checkout sessions like so:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96121&key=user_uploads/272109/6beeac16-971d-4035-927e-9307a9bd8acf)

### 2. Docs-Free Integration

Flowglad generates a bespoke integration prompt specific to your pricing model and codebase, that you can give your AI coding agent.

When coupled with the Flowglad MCP server, your agent can integrate payments in one shot.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96121&key=user_uploads/272109/fac8f58b-1b15-4fd7-9123-ba961b3192b2)

### 3. Open Source = Code-as-Docs

Every billing engine has all kinds of edge cases. We built ours from scratch, and the code is fully open source. So you can clone it locally and have your AI agent scan our 130,000+ lines of test code to quickly tell you exactly what will happen across various scenarios. No more consulting vague or out of date docs.

## 🎨 NUMI - Your startup's design department

# **TL;DR**

[NUMI](https://numi.tech) gives your startup a design department on subscription, with a dedicated primary designer. We cover all your design needs, from product to web design, creative design, and even no code development.

[**See example designs**](https://www.figma.com/proto/AmRAnvyBxNrdPlRZFijTIB/Our-Work?page-id=0%3A1&type=design&node-id=3-3&viewport=1224%2C1072%2C0.18&t=nZ4pPtvomYvN1h1d-1&scaling=scale-down&starting-point-node-id=3%3A3&hide-ui=1)

![](https://i.gyazo.com/b3210ba3878b2702f4f9d80e4321e6e0.jpg)

# **Problem**

Good design is now a non-negotiable for startups.

But there isn’t a single person that can do **all** the kinds of design that startups need: product, brand, graphic, web, and site development.

This forces every founding team into freelancer management hell: they have to source, vet, and onboard designers for each discipline. Half of those designers quit, ghost, or are fired within 3 months.

The alternatives are either to spend $100k+ / year on white shoe agencies or full-time hires or go to freelancer platforms that commodify design (including the work they’ll do for you!).

# **Solution**

* **Unlimited design requests,** completed one at a time.
* **A dedicated primary designer with timezone overlap**. You’ll collaborate directly over Slack, video, and Figma
* **1:1 design office hours:** talk design strategy with cofounder Harrison (founding designer at Imgur, RISD alum), up to twice a month - while supplies last!
* **Full design coverage**: product, brand, web, and no code design / development—all included. If you ever need something outside of your primary designer’s skill set, we’ll match you with an additional designer
* **Guild of vetted pros:** our guild of designers is invite-only. Harrison and I personally vet every single designer before they join. Our acceptance rate is lower than 2%
* **Backed by community**: NUMI’s guild means that if your designer ever faces a challenge, there’s a whole community of world-class designers available to help unblock them
* **Satisfaction guarantee**: if you’re ever unhappy with your designer, we’ll match you with another one and handle their onboarding seamlessly

# **Backstory**

When we got into YC, our startup was growing fast and so was our design backlog. Even with my cofounder Harrison’s design prowess (RISD alum and founding designer of Imgur) in the design community, we were surprised by how much work went into building and maintaining our design capacity.

Since then, we’ve spoken with hundreds of startups who have the same problem. One YC founder told us “I sent personalized messages to over 300 designers but got no responses.”

We figured there had to be a better way.

# **Interested?**

**Special launch offer:** try us out with a two-week, $15 trial.

**If you’d like to give NUMI a shot, **[**book a call**](https://cal.com/team/numi/design-chat-15min)** with us**. We’ll personally walk through your design roadmap and help you prioritize the most impactful design work.

If you’re just design-curious, watch our podcast [**Bottom Line Design**](https://www.youtube.com/channel/UCDCuvx5TIrFjgUcSXp1ShKw) to see our interviews with design leaders from [YC and Instacart](https://www.youtube.com/watch?v=TMkkh2_3SLc), [Apple](https://www.youtube.com/watch?v=uE7nKvQ2T78), [Zapier](https://youtu.be/-sDsruRS-tE), and [Nike](https://www.youtube.com/watch?v=UhpzFDovsZM).
