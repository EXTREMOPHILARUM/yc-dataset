# Launches

## Nango: Embed 600+ integrations from 400+ APIs in your SaaS

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88416&key=user_uploads/4587/c5bd7650-0750-4fc1-92cc-14148ceb7cbe)

([API catalog](https://www.nango.dev/api-integrations) / [Docs](https://docs.nango.dev/) / [Repo](https://github.com/NangoHQ/nango) / [Try it](https://app.nango.dev))

Two years ago, we launched Nango as an [open-source OAuth handler](https://news.ycombinator.com/item?id=34693233) that simplified authorization for 40 APIs. Since then, we’ve expanded to become a full product integration platform for developers. We now support 400+ APIs, 600+ pre-built integrations, and custom integrations-as-code.

Demo video: <https://www.youtube.com/watch?v=oTpWlmnv7dM>

Each API in our catalog comes with auth handling (OAuth, API keys, etc.), two-way syncing, retries, rate limit management, pagination, webhooks, observability, etc.

We also have pre-built integrations for common use cases like fetching HubSpot contacts, creating GitHub issues, syncing Salesforce data, and hundreds more.

If an API or integration you need isn’t supported yet, you can implement it yourself on Nango (or ask us to prioritize it).

Everything related to API authorization is free forever, and you can either self-host or use our cloud version.

([API catalog](https://www.nango.dev/api-integrations) / [Docs](https://docs.nango.dev/) / [Repo](https://github.com/NangoHQ/nango) / [Try it](https://app.nango.dev))

## 🔌 Nango: Get OAuth tokens for APIs. Fast & secure.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70266&key=user_uploads/4364/21c7fde9-a308-4c66-9cde-8eacfc4ce237)

## TL;DR

Pre-built OAuth flows & secure token management for 55+ APIs (and counting). 100% open source.

## The problem: OAuth sucks.

[OAuth is harder than it seems](https://www.nango.dev/blog/why-is-oauth-still-hard):

* Every API has specific quirks & nuances - forcing you to read endless docs pages
* OAuth libraries don’t solve redirects, adding callback endpoints, token storage, refresh logic etc.
* When something goes wrong debugging is hard: Unspecific errors, non-compliant behaviours, missing details and a million possible root causes

On top of this, SOC 2 compliance & GDPR make storing plain-text tokens in your DB no longer a viable option.

## The solution: Nango makes OAuth fast & secure.

Nango is a service that contains everything you need to work with APIs that use OAuth:

* A full OAuth dance for 55+ APIs - no backend work needed
* A tiny frontend SDK, with promises instead of confusing full-page redirects
* Secure token storage, with automatic refresh as needed
* Works with any API, programming language & framework

In your frontend easily trigger an OAuth flow with 1 line of code (full desktop & mobile support):

```jsx
nango.auth('salesforce', '<user-id>'); // Opens a modal for OAuth dance
```

Then get always fresh access tokens in your backend:

```jsx
let accessToken = nango.getToken('salesforce', '<user-id>'); // Refreshed & ready
```

That’s it.

## Trusted in production, by startups and established companies

Nango is used in production by companies like Typeform, Crowd.dev, AppraisalInbox, Trigger.dev (YC W23), Blocktool (YC W23) and others.

## Try it in 5 minutes

Nango is easy to try on your local machine (open source) or with our cloud option:

* Try it on your local machine: <https://github.com/NangoHQ/nango>
* Get started with [Nango Cloud](https://www.nango.dev)
