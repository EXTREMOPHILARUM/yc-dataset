# Launches

## Warrant - Open source application authorization and access control

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70447&key=user_uploads/234741/7662bcdc-8497-4a8c-a0c6-428ddc3bffe0)

Hey everyone! We’re Aditya and Karan! 👋

Warrant is an open source **authorization service** that **helps developers implement and enforce secure, compliant access control in their applications.** It abstracts away the complexity of building application authorization and access control so developers can instead focus on building core product features.

Our cloud-first, API-first approach has enabled us to build a highly-scalable and performant service that now processes millions of customer API calls per month. Today, we’re excited to announce that Warrant is officially [open source](https://github.com/warrant-dev/warrant)! ⭐️

### The Problem

Developers, we’ve all been there. What started as a simple _isAdmin_ flag to distinguish between internal and external users — just so you could release that _one_ internal-only feature — has grown into a nightmare to maintain. It’s now a hodgepodge of booleans, database flags, and a halfway built role based access control system that not only slows down your team’s day-to-day development velocity, but also opens up your company to a slew of [costly security vulnerabilities waiting to be exploited](https://www.hackerone.com/press-release/organizations-paid-hackers-235-million-these-10-vulnerabilities-one-year-4).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70447&key=user_uploads/234741/60544231-1dac-4013-8872-c97b83878da3)

What’s more? Your customers are now requesting the ability to self-manage their team’s roles and permissions, so you’ll be spending another 1-2 months building the APIs, UIs, etc. for this risky, non-differentiating feature.

In short, application authorization and access control is difficult to build and even trickier to maintain as a company’s product evolves and its needs change.

### The Solution

To help developers quickly build world-class access control, Warrant provides three things:\
(1) **A centralized datastore for storing your application’s authorization policies and related data.** Warrant’s management dashboard and APIs make it dead-simple to safely modify authorization policies globally or for a single user or tenant in real-time. With Warrant, updating policies for all users as your product changes becomes a breeze.

(2) **A real-time, low latency access control service for enforcing authorization policies in your application at runtime.** With official Warrant SDKs available for the most popular server-side languages and frontend frameworks, checking if a user has access becomes as easy as a call to Warrant’s _check_ method.

(3) **A library of thoughtfully designed, authorization-specific UI components** that help with building self-service permission management flows, granting/denying access to privileged pages/UIs, displaying audit logs to users, and more. These components are **customizable and _permission-aware_**, so developers can drop them into any application.

### What’s Next?

Join us on our journey to solve authorization and access control for all developers:

* Give us a 🌟 [on GitHub](https://github.com/warrant-dev/warrant) and tell us what you’d like us to build next
* Give us a follow [on Twitter](https://twitter.com/warrant_dev) to keep up with the latest Warrant features
* Come discuss everything authz/access control in our [Slack community](https://join.slack.com/t/warrantcommunity/shared_invite/zt-12g84updv-5l1pktJf2bI5WIKN4_\~f4w)
* Try out our managed cloud service, [Warrant Cloud](https://app.warrant.dev/signup)
