# Launches

## Bracket - Sync Salesforce & Postgres: Heroku Connect alternative for any SaaS

**Tl;dr:** [**Bracket**](https://app.usebracket.com) syncs data bidirectionally between tools like Salesforce & databases like Postgres — think Heroku Connect between any SaaS tool and any database or warehouse. For companies that collect customer-relevant information in SaaS tools, Bracket is the simplest way for engineers to get this data in front of customers in real time.

—

Hey everyone! We’re Vinesh, Ian, and Kunal and we’re building Bracket.

![](https://lh5.googleusercontent.com/xrZwklibKE9wZuf_lyCSiei3Nt082k0IncnOuMZsmtUqwLV_JLbWEPilfCw1HJ41-GfqJg7XruoZP4cigIcN3RfnS7vKItZsqlzx8uyAMRBJs1dQItNfvU8E8f9I7qWzJZZHT1NhxwblRHAdUajPh4s)

### **The problem**

Companies often need a way to manually adjust the info that a lead or customer sees - think of the sales team of a software company that wants to customize a demo environment for a high-value lead, or the ops team of a car rental company that needs to manage which cars are available for customers to book. 

The job of designing, implementing, and championing a fix falls to engineering. Engineers can either build a custom UI for their teammates, or connect with the tools they already use, like Salesforce or Airtable. 

There are a few problems with this:

1. Custom UIs run against the grain of the tools that business teams already use and can even require double data entry on the part of those teams. This leads to low adoption. 
2. This leads most engineers to integrate with their business teams’ existing tools. However, setting up real-time two-way syncs is a highly technical challenge that can take entire quarters of implementation time.

In short, custom-built solutions lead to low adoption, and built-from-scratch integrations with business teams’ tools can take months of engineering effort.

### **How we solve it**

**Using two-way syncs, Bracket is the easiest way to keep data in sync between business teams’ existing tools, like Salesforce, and databases, like Postgres.** 

This creates a win-win-win. Using the Salesforce <> Postgres example:

* Engineering gets to build on top of Postgres and doesn’t have to deal with the Salesforce API (we do that for you). Engineering also meets business teams where they are, optimizing adoption.
* Customer-facing business teams (e.g. Sales, CX) continue to leverage Salesforce, a familiar, highly productive tool with tons of features and a strong community, and can trust that their data is fresh.
* Customers - seeing fresh, personalized data - get the best UX possible, increasing lead conversion and paid retention.

 

Our new web app works with Salesforce and Postgres along with other connectors (like  Airtable, Google Sheets, MySQL and more).

![](https://lh4.googleusercontent.com/plJHt6uWnEfHvqApcTBso-yoZ9penLWsS7gyG4usf8avqWinfSaNtFVRLwV4Hd7eFAcmJ-A-ueNFIgpiv33S4TlCZGBd_OyOzauJWPKPKRj3r_-PSyKQMxoqJqQ5T03cd7LPWWLlg_9DJ0marOEavuM)

### **Demo:**

[ ](https://www.youtube.com/watch?v=sRkaAa667T0)

### **Differences from Heroku Connect?**

1. **Built for your tech stack:** We support beyond just Heroku Postgres. Not only do we support any hosted Postgres, but we also have two-way syncs with other databases and warehouses.
2. **Active Development:** Heroku Connect hasn’t been updated in years and has no new features on their official roadmap. Bracket continues to develop around the modern stack.
3. **Uses cases across teams:** We’ve built two-way syncs for CRMs like Salesforce but also other products like Airtable, Google Sheets, and more.
4. **Price:** We’re far cheaper than Heroku Connect, which can run north of $50k / year.

### **Our ask:**

If you want to try this yourself, get started[ **here**](https://app.usebracket.com)

Otherwise, if you:

1. Are looking for two-way syncs between other tools and want us to build it
2. Know any data engineers at mid-market / enterprise companies to make an intro
3. Have any other questions, please reach out to [founders@usebracket.com](mailto:founders@usebracket.com)
