# Launches

## highlight.io - Open-source session replay & error monitoring

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68975&key=user_uploads/241768/1b79410b-8b41-4e1e-8869-c4ccfe7d2130)

## **TL;DR:**

[highlight.io](http://highlight.io) is an open-source **session replay and error monitoring** tool that helps teams reproduce hard-to-crack issues and understand product usage. We enable developers to understand WHY bugs are thrown on their web apps to eliminate the noisy alerts they get from more traditional monitoring tools.

[highlight.io](http://highlight.io) is already being used in production by **2k+ developers and 80+ companies**. Get started for free at [app.highlight.io](http://app.highlight.io) and give us a ⭐️ at [github.com/highlight/highlight](http://github.com/highlight/highlight).

### **The Problem**

How many times have you gotten an alert from Bugsnag or Sentry, and dismissed it because you weren’t sure about what caused it? And how many of you have an endless backlog of errors that your team _should_ triage, but haven’t gotten to yet?

We’ve found that when debugging an issue or customer request, **the toolset that you use is responsible for delivering one thing only: context**. And if there’s any gaps in this context, engineers are left in the dark.

To solve this, at our last companies, we found a lot of value in instrumenting a session replay-like tool, (similar to Logrocket or Fullstory), paired with an error monitoring tool (like Bugsnag). In fact, we’ve built these sorts of tools ourselves to hackily solve the problem. Enter [highlight.io](http://highlight.io).

### **The Solution: Session Replay 🤝 Error Monitoring**

With a simple `yarn/npm` import in your frontend and an optional import in your backend, [highlight.io](http://highlight.io) gives you session replay and error monitoring out of the box. This means that you can:

* Replay exactly what a user was seeing at the time of an issue/bug.
* Reproduce the browser dev-tools for every user session, including the network requests, errors, and more.
* Access all of the errors and exceptions (both frontend and backend) thrown in your app, paired with session replay.

Lastly, given the privacy-sensitive nature of the product, we have a very powerful privacy API that you can take a look at in our docs [here](https://www.highlight.io/docs/session-replay/privacy).

## **💬 What’s Next?**

We’re just getting started! We have plans to go way deeper into your observability stack to give you ALL of the visibility you need; that means logs, traces and more! Join us on this journey:

* ⭐️ us on [GitHub](https://github.com/highlight/highlight) to keep up with releases and news.
* Join [our Discord](https://highlight.io/community)!
