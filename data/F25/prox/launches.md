# Launches

## Prox: digital co-workers for logistics operations

Greg and Dima here - childhood friends, grew up in our families’ warehouses - now YC founders building Prox.

**launch video:** https://www.youtube.com/watch?v=9Ywl-K7ncj0

---

**tldr:**

[**Prox**](https://www.prox.inc/) builds digital workforce for third-party logistics and fulfillment providers. We deployed our first agents at [**ShipBob**](https://www.linkedin.com/company/shipbob) (unicorn 3PL handling 100+ million packages per year) to automate carrier claims for lost-in-transit packages. **They're now live in production, processing hundreds of claims in parallel and on track to recover millions in carrier refunds annually.**

**what is 3PL?**

third-party logistics companies (3PLs) are the invisible infrastructure behind e-commerce brands: they warehouse inventory, fulfill orders, manage returns, and negotiate with carriers so brands don't have to.

**the problem:**

40,000+ 3PLs in the US all do the same thing: throw people at operational bottlenecks.

❌ Claims processing done manually, one by one \
❌ Invoice reconciliation eating hours of labor \
❌ Compliance paperwork blocking growth \
❌ Every increase in package volume = more back-office hires

That's the margin trap. Logistics companies stuck at 3-5% margins because headcount scales linearly with volume of packages. You can't compound when labor costs are linear.

**what we built:**

We developed an n8n-inspired agent building platform - native to logistics infrastructure. It integrates with Salesforce, warehouse & transportation management systems, carrier portals, Microsoft Teams, and email → then executes SOPs end-to-end.

With this platform, we can deploy agents in production in a matter of days.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95414&key=user_uploads/3066807/dc3e69b6-c3f6-476d-94c5-578b3a02d9de)

**use case: ShipBob Carrier Claims Automation**

Here’s an example of how our agents handle lost package claims for [ShipBob](https://shipbob.com/), one of the biggest 3PLs in the US.

> first demo at ShipBob HQ in Chicago
>
> ![uploaded image](https://www.ycombinator.com/media/?type=post&id=95414&key=user_uploads/3066807/cd110709-17ec-410e-90c8-e3c0d7db72f5)


When a package goes missing - our agent orchestrates resolution: pull order data, calculates refund amounts, files with carriers, monitors responses, parses updates, syncs internal systems, escalates exceptions - hundreds running in parallel.

Our agents do not stop at task execution - we designed them to own outcomes. If a carrier doesn't respond, the agent follows up. If documentation is missing, it fetches it. Each agent has one objective: get the claim resolved.

**about us:**

[**Gregory Makodzeba:**](https://www.linkedin.com/in/gregory-makodzeba/)

* Founded Rektoff: built blockchain security infrastructure protecting $100B+ in crypto assets (clients: Solana Foundation)
* Led Developer Relations at Runtime Verification, working with NASA, Boeing, and Ethereum Foundation on formal verification for mission-critical systems
* Grew up implementing ERP and WMS systems in the family distribution business

[**Dima Yanovsky:**](https://www.linkedin.com/in/yanovsk/)

* MIT grad: Computer Science + Electrical Engineering
* Robotics research at MIT CSAIL under Prof. Pulkit Agrawal on manipulation policies;
* Built internal and customer-facing AI agents at Pulley (YC W20) during early GPT era
* Spent childhood automating warehouse operations and business processes

We both grew up in our parents' warehouses. When we weren't moving boxes around, we were doing the mundane back-office work every warehouse has (filing claims, reconciling invoices, chasing carriers). This was the pre-LLM era, so we had no choice but to grind through manual workflows. We saw firsthand how coordination became the biggest constraint on growth - and how no software could actually handle it end-to-end.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95414&key=user_uploads/3066807/68380300-ee0e-4379-98de-de1b551b269e)

We deeply understand the ontology of logistics operations. That's why we can ship integrations in days, not months. We're building the digital workforce we wish existed back then.

If you're running logistics operations at a 3PL, fulfillment center, or freight forwarder, or know someone who is - reach out: [founders@prox.inc](mailto:founders@prox.inc)

---
