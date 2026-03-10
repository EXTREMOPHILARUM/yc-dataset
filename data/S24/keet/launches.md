# Launches

## Keet - APIs for any website

**TLDR:** [Keet](https://trykeet.com/) provides APIs for any website. Developers use us to connect their customers’ accounts and perform actions on their behalf.

## **Why does this exist?**

It is difficult to build automations with web platforms, especially those that require authentication.

We make seamless and stable integrations your competitive advantage.

## **Who is this for?**

You want to be able to take actions on your users’ behalf.

Imagine if you could easily…

* Call an endpoint to submit a form instead of writing a Playwright automation
* Book Ubers based on your user’s calendar and location
* Track activity on properties for future homeowners on Redfin

Without…

* Storing your end user’s credentials
* Dealing with MFA
* Writing playwright automations that break when a page gets updated

**There are some other solutions out there. How are we different…**

1. No Chrome extension is necessary for your users to authenticate
2. We maintain your users’ authenticated sessions
3. Many of our API abstractions don’t rely on playwright or browser automations

## **How does it work**

1. Link your end user’s account using a Plaid style link component (Web + iOS supported)

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=83560&key=user_uploads/867482/0854c800-24b5-4ace-9ac1-8c8c0dc4dbb1)

2. Call our API endpoints for their connected platforms:

```
keetClient.integrations.venmo.getTransactions()
```

## **Our Asks**

If you have any custom integrations you want built, reach out!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83560&key=user_uploads/867482/cdedbf8d-008c-4822-820a-ff4b5310256f)
