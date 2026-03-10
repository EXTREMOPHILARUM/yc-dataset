# Launches

## Sourcebot: The Code Understanding Platform

**TL;DR**: Sourcebot is an open source code understanding platform. It’s used by thousands of engineers in some of the largest companies in the world (including **NVIDIA, Red Hat, Wikimedia, and Arista Networks)** to help developers and AI agents understand massive codebases.

[https://youtu.be/YJIi-gcAM3g](https://youtu.be/YJIi-gcAM3g%5C)

\
**The problem:**

* Large engineering teams manage **millions of lines of scattered and undocumented code**.
* Individual engineers must regularly find and understand code across this complex environment to do their job. Existing tooling to do so is **inadequate, rudimentary, and often nonexistent.**
* **AI agents have this problem too.** They need this context to provide usable results within an enterprise environment

**The solution:**

Sourcebot solves this by providing the following tools:

* **Code Search -** instantly search across millions of lines of code. Supports regex, boolean logic, and repo/file/branch filters.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94687&key=user_uploads/1449228/70c891b0-cfec-4ff6-b070-fc1f212c29da)

* **Ask -** ask questions in natural language across thousands of repos. Like asking in Cursor, but across all your repos and in a web app with inline citations.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94687&key=user_uploads/1449228/b97e4beb-83cb-4d8d-b6b0-ed53a2a973c8)

* **MCP -** gives both of the above tools to AI agents, allowing them to fetch context from code across your organization.

Additional features:

* We integrate with any **code host** (e.g., GitHub, GitLab, BitBucket, etc.) as well as any **LLM model** (e.g., OpenAI, Anthropic, Bedrock, etc.). Bring your own LLM key.
* Sourcebot is **open source** and **self-hosted** - none of your code leaves your deployment. Deploy and index all your repos in minutes with a single docker container.
* We have a community edition that’s **free to use**, and a paid enterprise edition with advanced navigation features, analytics, and security/compliance features.

**Our story:**

Brendan and I met 10 years ago during our first week at McGill University 🇨🇦. We were both into game engines, which led us to work at Ubisoft Montreal on the largest game engines in the world. Afterwards, we worked on some of the most complex systems out there: Visual Studio at Microsoft, a cloud-first game engine at Google, VR operating systems at Meta, and cloud-streaming infrastructure at Xbox. Ramping up and understanding these systems was always a long, painful process - which is what led us to build tools to help developers understand this complexity.\
\
Learn more here: https://www.sourcebot.dev/

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94687&key=user_uploads/1449228/4ef682b8-0ac6-48a4-937d-8a64d62f34d3)
