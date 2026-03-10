# Launches

## Continue: the easiest way to code with any LLM

Hi all! We’re Nate and Ty, co-founders of Continue.

## **🔥 TL;DR**

_Stop copy/pasting code from ChatGPT and take control of your development data 💪_

[Continue](https://bookface.ycombinator.com/company/28957) is the open-source autopilot for software development built to be deeply customizable and continuously learn from development data.

Our GitHub is <https://github.com/continuedev/continue>. You can watch a demo of Continue and download the extension at <https://continue.dev>.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73449&key=user_uploads/117092/248795a4-d22a-4f7d-a9fb-42c69d63a463)

---

## **💬 The Problem**

A growing number of developers are replacing Google + Stack Overflow with Large Language Models (LLMs) as their primary approach to get help, similar to how developers previously replaced reference manuals with Google + Stack Overflow.

Unfortunately, existing LLM developer tools are cumbersome black boxes. Developers are stuck copy/pasting from ChatGPT and guessing what context Copilot uses to make a suggestion. As we use these products, we expose our code and give implicit feedback that is used to improve their LLMs, yet we don’t benefit from this data nor get to keep it.

The solution is to give developers what they need: _transparency, hackability,_ and _control_. Every one of us should be able to reason about what’s going on, tinker, and have control over our own development data. This is why we created Continue.

---

## **⏩ The Solution**

At its most basic, Continue removes the need for copy/pasting from ChatGPT—instead, you collect context by highlighting and then ask questions in the sidebar or have an edit streamed directly to your editor.

But Continue also provides powerful tools for managing context. For example, type ‘@issue’ to quickly reference a GitHub issue as you are prompting the LLM, ‘@README.md’ to reference such a file, or ‘@google’ to include the results of a Google search.

And there’s a ton of room for further customization. Today, you can write your own

* slash commands (e.g. ‘/commit’ to write a summary and commit message for staged changes, ‘/docs’ to grab the contents of a file and update documentation pages that depend on it, ‘/ticket’ to generate a full-featured ticket with relevant files and high-level instructions from a short description)
* context sources (e.g. GitHub issues, Jira, local files, StackOverflow, documentation pages)
* templated system message (e.g. “Always give maximally concise answers. Adhere to the following style guide whenever writing code: {{ /Users/nate/repo/styleguide.md }}”)
* tools (e.g. add a file, run unit tests, build and watch for errors)
* policies (e.g. define a goal-oriented agent that works in a write code, run code, read errors, fix code, repeat loop)

Continue works with any LLM, including local models using ggml or open-source models hosted on your own cloud infrastructure, allowing you to remain 100% private. While OpenAI and Anthropic perform best today, we are excited to support the progress of open-source as it catches up (<https://continue.dev/docs/model-setup/select-model>).

When you use Continue, you automatically collect data on how you build software. By default, this development data is saved to .continue/dev_data on your local machine. When combined with the code that you ultimately commit, it can be used to improve the LLM used by your team.

You can read more about how development data is generated as a byproduct of LLM-aided development and why we believe that you should start collecting it now: <https://blog.continue.dev/its-time-to-collect-data-on-how-you-build-software/>

Continue has an Apache 2.0 license. We plan to make money by offering organizations a paid development data engine—a continuous feedback loop that ensures the LLMs always have fresh information and code in their preferred style.

---

## 🙏 **Our Asks**

1. [**Star our GitHub repo**](https://github.com/continuedev/continue)
2. Download for [**VS Code**](https://marketplace.visualstudio.com/items?itemname=continue.continue) & [**JetBrains**](http://plugins.jetbrains.com/plugin/22707-continue)
3. Join our [**Discord**](https://discord.gg/NWtdYexhMs) & [**newsletter**](https://continue.dev/?ref=blog.continue.dev#newsletter)

---

## **❤️ The Team**

We started working on Continue because LLMs rapidly got better and quickly became an important part of our development workflows. In 2021, Ty was helping the research team at Rasa use GPT-3 to create user simulators and Codex to generate Actions code for Rasa Open Source—projects that did not result in shipped products because LLMs were not good enough yet.

This changed in 2022. During the day, Nate wrote code at NASA, unable to use LLMs due to privacy concerns. But at night, the difference was stark as GitHub Copilot and ChatGPT completely changed how we built side projects.

We believe that the role of LLMs in software development is only beginning. In order to reach their full potential, developers need to to be able to tinker and unleash their creativity. Every developer must be able to try new things and push what's possible using LLMs without having to ask for permission.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73449&key=user_uploads/117092/98c7da9c-a397-4ec1-8727-f1dbc941df77)
