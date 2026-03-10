# Launches

## Pig 🐷 - Automate Windows apps with AI

# TL;DR

[Pig](https://pig.dev) is an API for automating Windows desktops with AI.

Teams can connect their own Windows machines to Pig, open up a chat, and instruct an AI to perform workflows on that computer, over the internet.

Pig’s agent operates computers as humans would, performing high-value automations that were previously not possible. 

[Sign up here](https://www.pig.dev/login#auth-sign-up)

# The Problem

Many enterprise tools, from electronic health records to manufacturing supply-chain apps, are desktop-based and do not have a public API, preventing automation.

Traditional hardcoded RPA automations can be brittle. Subtle changes in the desktop apps, like popups or slow loading, can derail an automation. And complex workflows which require planning and judgment are not possible.

As a result, human office workers are employed to do highly repetitive tasks, often involving transferring text between different desktop apps, spreadsheets, and emails.

# Our Solution

<https://youtu.be/qC8WTFtKYOA>

In this example, we show what’s possible building on Pig. 

We first connect our own Windows machine using our open-source [Piglet](https://github.com/pig-dot-dev/piglet) computer driver

And then we start an AI chat powered by the [Claude Computer-Use](https://docs.anthropic.com/en/docs/build-with-claude/computer-use) model:

![Chat interface for automation](https://www.pig.dev/_next/image?url=%2FChatFeature.png&w=3840&q=75&dpl=dpl_GKdZd2HZi9eL2zCkbzmv3rzJACTW)

The AI is then given high-level tasks, and it begins to work, using Pig’s human-emulating APIs such as:

* Screenshotting the desktop screen
* Clicking at coordinates
* Entering keystrokes

All of which are enough to complete the task.

Pig also provides a developer SDK, allowing teams to build their own agents, manage their connected machines, and send automations to their desktops. Purpose-built agents can be incredibly powerful, so [contact us here](https://www.pig.dev/talk) to talk through custom implementation.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87161&key=user_uploads/265552/644dc367-8cac-45ba-b919-22e6664088b4)

Lastly, Pig includes tools for agents to pass control to human operators during critical operations, such as clicking send on important emails, inputting payment information, or solving captchas.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87161&key=user_uploads/265552/d4cec1ed-390a-4ba1-8c48-b5d5173e9668)

We intend to be the personal computers for AI, and the embeddable observability window for managers.

# Use Cases

Killer use-cases of Pig involve the following factors:

* the workflow requires a Windows desktop app
* The app does not have a public API

I expect to be surprised by what people build on Pig, but I’m most optimistic for use of:

* Office Suite
* Electronic Health Record Software
* Claims Processing Software
* Factory Control Systems
* Lab Software

# Team & Background

I’m Erik, a second-time founder, with five years spent building cloud infrastructure.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87161&key=user_uploads/89898/6b51d5af-79d8-4d30-ad7e-f3e221dd3b53)

Most notably, I built [Banana](https://banana.dev), a serverless GPU product used by more than three thousand teams to host production inference jobs.

Prior to Banana, I built a cloud desktop product for accelerating 3D design apps. Following Banana, I had the privilege to work with our former competitor, [Modal](https://modal.com), on their serverless Python cloud.

Why am I building Pig?

Throughout 2024, I spent my time experimenting with new technologies and building up a thesis for what the future of AI tooling would be. After poking around a few wild ideas (such as data centers in space and internet-over-laser), I boomeranged back to the area that I know and love: compute infrastructure.

An AI founder friend called me up in Nov 2024, pitched me on this idea as something he needed to see in the world, and said, “Erik, you’re the single best founder to build this.”

And I agree. I am.

# How to become a user

Pig just launched open and free access to users self-hosting their machines.

Get started today at [**pig.dev/docs**](http://pig.dev/docs), or [**contact us**](https://pig.dev/talk) for help building custom agents and I’ll reach out!

And if you don’t need Pig, please tell at least one friend about it.

Oink!\
Erik

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87161&key=user_uploads/265552/70b01c11-9da9-4db0-976c-1162ca31f323)
