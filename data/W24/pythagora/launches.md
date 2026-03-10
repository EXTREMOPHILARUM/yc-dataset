# Launches

## Pythagora: All-in-one AI development platform

### **TLDR**

Pythagora is an all-in-one AI dev platform that is focused on building production-ready apps that you can deploy, use, and share.

[Video](https://www.youtube.com/watch?v=o1nEvwjKziw)

### **Problem**

We built Pythagora after seeing too many AI-generated projects either abandoned at the first sign of trouble or trapped in endless "fix it" loops with no visibility into what's actually happening. Without proper logs, breakpoints, or debugging tools, users were left guessing and rebuilding repeatedly.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91577&key=user_uploads/1047121/e2ca5b1e-9f0d-40ae-b6fc-30a24cf4abfe)

### **Another codegen tool?**

While other platforms focus on the initial "wow" of code generation, we've designed for the complete reality of software development. Every application will face challenges when it meets real users with real data.

Our key differences:

1. Overview: Clear overview of the project roadmap and your current progress.
2. End-to-end development: From project planning to deployment (our cloud backed by AWS or your own infra - take your code wherever)
3. Tools access - Easy access to app preview, logs, and knowledge base.
4. Real debugging tools: Breakpoints, logs, and database inspection when something inevitably breaks
5. Full-stack architecture: Proper backend, frontend, and database relationships, not just UI demos

### **Final thoughts**

We're most proud that Pythagora treats your applications as living projects, not disposable demos. The platform shines exactly where others fall short: when you need to fix, improve, and deploy what you've built.

Stop treating AI-generated apps as disposable. Start building applications worth maintaining, fixing, and deploying.

* **Explore apps built with Pythagora:** [pythagora.ai/examples](http://pythagora.ai/examples)
* Read case studies of users creating meaningful apps: [pythagora.ai/case-study](https://www.pythagora.ai/case-study)

### [**🙏**](https://www.pythagora.ai/case-study-medical-research) Ask

If you know a company that’s looking to build internal tools, please connect us. I’d be happy to give them a demo.

## 🧮 Pythagora - Build tools completely in natural language

TLDR; Pythagora is a VS Code Extension that writes all the code for the app you want to build and talks to you whenever it needs a creative decision or feedback. It is focused on building production-ready apps that you can deploy and use, so to achieve that, it keeps you, the human, in the loop throughout the entire development process. Pythagora manages the entire codebase and talks to you in natural language.

### **🤨 Problem**

Today, new AI dev tools come out almost weekly. While many showcase impressive demos, very few prove their worth in building real-world, production-level applications. We think that this is because they don’t put the human in the loop enough. There is a notion that apps can be built just by writing 2 sentences of what kind of an app you want, and then you just wait until AI comes back with a fully built application.

We believe that humans have to be involved in the entire process of app development to give timely feedback so that AI can make changes as it works on specific features.

### **💡 solution**

![](https://www.ycombinator.com/media/?type=post&id=79066&key=user_uploads/170713/2c530744-eaf9-4870-9e87-d4bfd806082d)

Pythagora talks to the user throughout the entire development process. First, it creates a plan for building the entire application. Then, it goes task by task, implementing each one, but before going on to the next one, it asks the user to test whether it’s working as intended. We noticed that very often, Pythagora implements a feature correctly, but users, once they see how a feature works, decide they want it to work differently.

* Watch the full crash course on how to use Pythagora here: [https://youtu.be/HIIHx0kErPc](https://www.youtube.com/watch?v=4g-1cPGK0GA)
* **Explore apps built with Pythagora:** [pythagora.ai/examples](http://pythagora.ai/examples)
* Read case studies of users creating meaningful apps: [pythagora.ai/case-study-medical-research](http://pythagora.ai/case-study-medical-research)

### [**🙏**](https://www.pythagora.ai/case-study-medical-research) **Ask**

If you know a company that’s looking to build internal tools, please connect us. I’d be happy to give them access to Pythagora v1 and do a demo.

## Pythagora - First complete AI developer that builds apps by talking to you

**TL;DR** [Pythagora](https://pythagora.ai/) is not a coding assistant or an autocomplete. It’s a true AI developer that takes your requirements, asks you questions, considers what technologies to use, and creates the development plan. Then, it breaks the plan into tasks, writes code, reads the CLI, fixes bugs, iterates, reviews the code, and asks you questions to make sure it’s on the right track.

### 🛤 **OUR JOURNEY**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79066&key=user_uploads/170713/273e17b6-e99a-464a-9faf-c5a223e81bb6)

[Senko](https://linkedin.com/in/senkorasic) and [Zvonimir](https://linkedin.com/in/zvonimirsabljic) met at a startup event in 2016. when Senko was looking for someone who would lead a side project that he started. Zvonimir accepted the challenge, we turned that project into a company, and 5 years later, in 2021, we sold the company to Miro.

[Leon](https://linkedin.com/in/leon-ostrez-b55494178) and Zvonimir have been best friends since starting college in 2009. After the Miro acquisition, we started learning ML together and playing with different ideas. In 2023, we created our first open-source project for generating automated tests, and it quickly gained 1.4k Github stars. After talking to users and observing how AI is evolving, we decided to pivot to GPT Pilot, which became one of the fastest-growing open-source projects, now with more than **22k Github stars**.

While we worked on the GPT Pilot, Senko explored a similar idea, so finally, in October 2023, we decided to join forces and build Pythagora together.

### **❌ The Problem**

Ok, let’s state the obvious - there’s still a huge demand for software development, which is still expensive. On the other hand, we have LLMs that are extremely good at writing code. They can write code snippets like a senior developer but if you ask them to build the full app, it will do a worse job than a junior developer. This is because building production-ready apps is not only writing code. It’s writing code, running it, debugging, iterating, changing requirements, refactoring, and many other mechanisms that developers do every day.

While LLMs are getting smarter every single day, they will always be answering machines—they won’t have the mechanics that allow humans to iteratively progress on building an app.

The good thing is that all these mechanisms are deterministic and repetitive.

### **🌟 Our Solution**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79066&key=user_uploads/170713/2c530744-eaf9-4870-9e87-d4bfd806082d)

Pythagora is a blueprint of what app development looks like. First, it takes your requirements and asks you questions to clarify how you want your app to look. Then, it thinks about what technologies should be used for your specific app and creates the development plan. Then, it breaks the plan into tasks, writes code, reads the CLI, fixes bugs, iterates, reviews the code, and refactors it. Before making each commit, it asks you questions to make sure that the app works exactly as you want. Finally, it proceeds this way to the next task until the entire app is finished.

Many AI copilots help developers write code faster, but Pythagora goes beyond the current developer experience — we’re reimagining how software development is done.

### **🙏 Asks**

If you know any company that’s looking to build internal tools, it would be amazing if you could connect us. I’d be happy to demo Pythagora to them.

Also, it would be amazing if you could share this launch on Linkedin or Twitter.

Finally, join us on [Discord](https://discord.gg/HaqXugmxr9)!
