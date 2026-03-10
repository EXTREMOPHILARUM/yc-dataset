# Launches

## Pluralith - Automated Terraform Infrastructure Visualization & Documentation

Hi we are Dan and Phi…

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/00d3f03c-7be2-4245-be6a-b1ac5931d882)

… and we are building Pluralith!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/f7d9a731-4769-423f-9dfd-7bdf920137e6)

### **TL;DR**

Title says it all. Pluralith lets you generate instant infrastructure diagrams from your Terraform codebase, locally (for development) and in CI (for documentation). [**Try it out here!**](https://docs.pluralith.com)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/9884a243-92d0-46ea-92f7-7dcd0cedb91c)

### **Watching > Reading**

So here’s a [freshly baked demo](https://youtu.be/Jbbil9kA-EE) just for you!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/42257960-a912-40f1-acb6-f089d4da1153)

### **The Problem(s)**

**Problem 1**: Infrastructure documentation is super important and often even required for proper compliance, but can be really time intensive and nobody wants to do it. So you’ve got two options:

→ Stay compliant and have good docs **BUT** loads of dev hours spent on them

→ No/few dev hours spent on docs **BUT** break compliance and no docs when you need them

**Problem 2**: Terraform is awesome, but can become quite messy and intransparent at scale. Understanding what is actually going on requires digging through loads of code and terminal output. Again, lots of dev hours lost here.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/1fc7af56-e700-4227-bcb9-0fc872b49446)

### **The Solution: Enter Pluralith**

**_Pluralith completely automates problem 1 away._**

Run it in CI, automate parts of your compliance process and always have up-to-date infra diagrams whenever you need them. We throw them into PR comments and have a dedicated markdown integration so you can plug it straight into your existing docs (ReadMes, Confluence etc.). We do change highlighting, drift detection, cost calculations and compliance checks (coming soon) and keep a history of all this stuff in your Dashboard for you so you have a perfect record on how your infra changes over time.

**_Pluralith alleviates problem 2._**

Replace miles of terminal output on a terraform plan with a comprehensive diagram that shows you what your infrastructure looks like, how it’ll change on apply, how much it’ll cost and wether it breaks compliance (coming soon). All you have to do is run `pluralith plan` instead.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/079e25e0-225e-443b-b052-3eaab564aa50)

### **How It Works**

**Locally**: Download our desktop app and follow it’s setup guide. In a minute you should be able to run `pluralith plan` in any of your Terraform project directories and get a diagram instantly.

**In CI**: The illustration below says it all. Set up Terraform in your pipeline, run Pluralith and there you go. Right now we have dedicated integrations for _GitHub Actions_ and _Gitlab CI._ (Many more to come)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/42ca4f68-1bff-48c5-a0c0-e9b1c3786746)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/0f6a5cbc-52d6-4a6c-bfdf-bb4672190d94)

### **Help Us Out?**

→ [**Give it a run**](https://docs.pluralith.com) (either in CI or locally) and let us know all the ways our stuff broke through the emails below!

→ Our open source CLI is looking for some stars. [**Give it a star!**](https://github.com/Pluralith/pluralith-cli)

→ If you are a DevOps professional → [**Pick any slot on here!**](https://calendly.com/dantheputzer/meet) We’d be stoked to chat about the infra landscape!

If there are any questions or anything else we can assist with, shoot us an email at [dan@pluralith.com](mailto:dan@pluralith.com) or [phi@pluralith.com](mailto:phi@pluralith.com)!

Cheers,

Dan and Phi

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65103&key=user_uploads/690046/952c66c1-40c8-41b8-a31c-50dbbacb5c7b)
