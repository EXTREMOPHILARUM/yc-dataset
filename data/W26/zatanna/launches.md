# Launches

## Zatanna | APIs for AI agents

Hey YC!

We’re [Rithvik](https://www.linkedin.com/in/rithvik-vanga-0824a5225/), [Alex](https://www.linkedin.com/in/alex-blackwell-506228206/), and [Tarun](https://www.linkedin.com/in/tarunvedula/), the team behind [Zatanna](https://www.linkedin.com/company/usezatanna/).

**TL;DR:** Today, most AI companies rely on slow, brittle, and unreliable computer-use agents to interact with software that has no API.  Zatanna solves this with faster, cheaper, and more reliable APIs for AI agents by reverse engineering requests and taking care of antibot infrastructure. 

[Video Link](https://www.youtube.com/watch?v=HUCOKVn-atM)

**The Problem:**

A huge amount of valuable business software still has no usable API. So when AI companies need their agents to interact with ERPs, PMS systems, portals, marketplaces, or other operational websites, they often fall back to browser automation.

That means the agent is stuck looking at screens, clicking buttons, waiting for pages to load, dealing with logins, handling UI changes, and breaking every time the workflow shifts. It is fine for showing that something is possible. It is terrible when the workflow actually matters.

Teams end up spending an absurd amount of engineering time maintaining brittle browser automations instead of building product and serving customers.

**The Solution:**

Zatanna runs these workflows at the request layer.

We observe how a workflow works once, reconstruct the underlying request sequence, and host it as a clean API that any agent can call. Instead of navigating a browser, the agent just hits an endpoint.

That makes the workflow:

* faster
* cheaper
* more reliable
* much easier to maintain at scale

We also handle the painful infrastructure required to keep these workflows alive in production:

* session and credential management
* request sequencing
* proxy networks and traffic distribution
* retries, monitoring, and recovery

Today we’re already supporting customers where either throughput or reliability is mission-critical, from high-volume consumer platforms to operationally sensitive industries like logistics.

**Where we’re seeing this most:**

* ERPs like SAP
* PMS / POS systems
* insurance/benefits/claims portals
* marketplaces(checkout flows)
* operational websites with no APIs
* basically anywhere the current solution is scraping or browser automation

**Why we’re doing this:**

We started in vertical AI and ran into this problem ourselves. The model layer kept getting easier. Software access was the real bottleneck. A huge amount of engineering effort went into keeping integrations alive instead of improving the actual agent.

So we decided to build the thing we wished we had.

**What we’re looking for:**

If you’re building something that depends on browser automation or computer-use agents for integrations, especially where reliability, speed, or cost matter, we’d love to take a look at the workflow.

Book a call [here](https://zatanna.cal.com/tarun/30min?user=tarun&overlayCalendar=true) or email [**tarun@zatanna.ai**](mailto:tarun@zatanna.ai)
