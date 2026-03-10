# Launches

## Opslane – Making on-call suck less

**TL;DR**

Our [Slack bot](https://github.com/opslane/opslane) classifies your Datadog alerts and flags noisy alerts, reducing alert fatigue.

Additionally, we generate insights based on all your alerts to give you a picture of your overall alert hygiene.

### The Problem

**Picture this:** It's 3AM, and you're woken up by a page. It's an error you've seen before, and you know it wasn't worth waking up for.

Anyone who's been on-call knows the infamous middle-of-the-night unactionable alert all too well.

Even with modern tools, it's still tough to determine when something has actually gone wrong, the user impact, and how to fix it quickly.

**Why are existing solutions not cutting it?**

* Lack of context - it's really hard to understand the customer and business impact from looking at an alert.
* Alerts are noisy and not actionable.
* Debugging requires context switching between multiple siloed tools.

### Our solution

We're starting with our open source Slack bot that reduces alert noise.

Once you add our bot to your Slack channel, we pull your alert history from Datadog.

We analyze your alert history across various parameters:

* Alert frequency
* How quickly have the alerts resolved in the past
* Alert priority
* Alert response history

Based on these, we classify your alert as actionable or noisy.

![User-uploaded](https://slabstatic.com/prod/uploads/s97i19pj/posts/images/6P01k6pFnPq5repaabLC5_-G.png)

In addition, we generate a report on your team's overall alert health, pinpointing which noisy alerts are prime candidates for tuning or disabling.

![User-uploaded](https://slabstatic.com/prod/uploads/s97i19pj/posts/images/1e4X0_iAo7eLJh7PLEo1oZoS.png)

Our vision is to stitch together all the relevant context engineers need to debug incidents in one place and automate root cause analysis.

### Team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82453&key=user_uploads/6530/ba62e789-6ccf-4b5c-a555-90e5c932d81c)

We ([Amaresh](https://linkedin.com/in/amareshray/) and [Abhishek](https://linkedin.com/in/abhishek-ray-29210145)) have firsthand experience dealing with the challenges of on-call and alert fatigue at companies like Robinhood and Atlassian. With Opslane, we’re reducing the alert fatigue that overwhelms on-call engineers and leads to millions in lost productivity and downtime.

### Ask

🔥 Are noisy alerts a hair-on-fire problem for your company or someone you know? We'd love to hear from you - email [founders@opslane.com](mailto:founders@opslane.com) or [schedule a call](https://cal.com/team/opslane/demo) with us.

⭐ Please star us on Github: <https://github.com/opslane/opslane>
