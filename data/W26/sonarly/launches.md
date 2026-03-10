# Launches

## Sonarly: The AI engineer for production

Hey! 👋 We're Dimittri and Alexandre and we're building Sonarly - an AI engineer that lives in your production stack, connecting to tools like Sentry, Datadog, and your user feedback channels. It triages alerts, investigates root causes, and ships fixes automatically.\
\
<https://www.youtube.com/watch?v=FPyswWvFhRU>\
\
**The Problem: The high cost of MTTR**\
\
Each bug in production is a frustrated user, and the longer the bug is there, the more likely the user is to churn. But if an issue is resolved fast, it can actually improve user happiness: they see that the team cares about them.

But this Time to Repair is inflated by two main bottlenecks:

1 - **Noisy alerts make it slower to find the real signal**. Alert fatigue is the first barrier.

2 - **The waiting game**. Once we have a clear signal, the longest step is fixing the bug. You have to find an on-call engineer, wait for them to wake up, or wait for them to finish another task. This time is precious and should be used to start the investigation. Once available, the on-call engineer has to dig through production logs and metrics, often going back and forth with Claude Code because the solution isn't obvious.

The core issue is that coding agents are very good at building software, but they struggle at run time because they lack context.\
\
**The Solution: The proactive coding agent with production context**\
\
We're building Sonarly to help you do one thing: make something people want. Right now, they want to use your product, but it's broken. We cut your resolution time so they can get back to using it.

Sonarly acts as an autonomous on-call engineer that works in the background 24/7. We're not replacing the on-call engineer, but we're helping them find the signal in the noise and saving them precious hours of investigation.

We connect to your entire monitoring stack, from Sentry & Datadog to user bug reports on Slack & Discord (+ many more integrations).\
\
**What it does**:

1- **Trust your alerts**: We triage signals together to group duplicates and filter false positives, sending only actionable alerts to your Slack or Email.

2 - **Fix with Context**: We run a coding agent in the background to investigate and fix bugs using the context of your whole production system: logs, traces, metrics, user feedback, and code.

3 - **Continuous Learning**: We update the representation of this system after every alert. This ensures the context is always up-to-date, so our agent understands your system better and fixes issues faster.

**The Ask: Let us cut your MTTR for free in minutes 🚀**\
\
We are launching access today!\
\
You can self-onboard and start fixing bugs in 3 minutes right now: <https://sonarly.com>

Have any questions or insights to share? Reach out to us at [dimittri@sonarly.dev](mailto:dimittri@sonarly.dev) or book a call with us to help you onboard! [https://cal.com/dimittri/demo](https://sonarly.com)
