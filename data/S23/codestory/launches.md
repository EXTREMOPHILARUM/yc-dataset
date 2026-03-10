# Launches

## Aide — The Open Source IDE to solve hard problems

Hey all! We’re Sandeep and Naresh from CodeStory. Aide (<https://aide.dev>) is the IDE for engineers to solve hard problems where changes are not limited to a single file but require iteration across multiple files. We are also open source at <https://github.com/codestoryai>. The main repositories are the:

* [IDE](https://github.com/codestoryai/ide) (the VSCode fork)
* [Sidecar](https://github.com/codestoryai/sidecar) (our rust binary the AI brains)

Check out the [editor in action](https://youtu.be/M82aLgBzdmk):

When we started building CodeStory last year, we were set on building the best chat and autocomplete experience in the editor, which we believed to be the best use of LLM for code generation.

We quickly (after 6 months) realised that with the increasing trend of LLM coding capabilities, the UX around chat and copilot felt limiting to the real abilities of these LLMs to help the developer accomplish more. 

In March this year, while debating what to focus our energy on, we decided to experiment with the idea: “What if LLMs could make edits across multiple files without breaking the logic?” So after a month of hacking, we tested our framework against [SWE-Bench Lite](https://www.swebench.com) and were very surprised (and kind of shocked) that Aide became the SOTA, resolving 43% of the issues.

We instantly knew we had to build the multi-file editing experience into the editor and do it well. 

We decided NOT to put energy into building a better “copilot autocomplete” or “chat,” but rather go all in on shipping a better “multi-file editing flow.”

While multi-file edits allow for larger units of work to be done, they have their set of problems:

1. Lack of control to granularly iterate when there is a small issue within a large change
2. Inability to roll back to older states when using over a long coding session.
3. Changes to the local scope, especially when context is not provided exhaustively, break the codebase globally
4. Context about edits made in a previous editing session is not kept around

To start in this direction, we forked VSCode 15 months ago as the most rock solid foundation to build an editor on top of and put quite a lot of work into solving some of the above stated issues with multi-file editing:

1. We built a proactive agent which looks at the linter errors (Language server and your own feedback) and proactively comes back with fixes and suggestions for improvements.
2. Special UX and integration with models for always breaking down changes into small, logical units that are easy to understand and have live previews using decorations in the editor, so changes can be applied easily, in parts or all at once.
3. Native support for checkpoints and rollbacks: We couldn’t use git, of course, so we hooked into the TextModel implementation in VSCode (which is its in-memory representation of a file) to keep track of file versions across AI changes, while also preserving the undo stack. These checkpoints are exposed in the UI, letting you easily move back and forth when needed without having to worry about uncontrolled changes.
4. Integrate tightly with the Language Server API on the editor to gather diagnostics from the whole codebase when changes occur, to ensure unintended breakages are quickly caught and propose fixes. For instance, the LLM changing a function signature should also fix the entire call stack.
5. Maintain a continuous, long session context. Because our editor works entirely locally (no intermediary server interaction, just LLM calls directly from your machine!), the Rust binary shipped with the editor listens to all events and changes made by both the developer and AI to keep a continuous context, so subsequent changes are always better informed.

Though, we, of course, didn’t just stop with multi-file edits.

1. Even with single-file changes, our Rust binary leverages tree-sitter to structurally understand a file and use a combination of Search-And-Replace style editing with tight editor integration to edit multiple locations within a file in parallel to make faster edits, especially useful in large files. And threw in AST navigation for developers to move faster around them.
2. To gather context for codebase-wide queries, rather than try to maintain lossy embeddings, the binary builds a repo map to let the LLMs filter down the most useful parts of the codebase per query.
3. Wherever possible, use the new prompt caching capabilities (also exposed as a first-class citizen in the editor to give developers more control) to cache the most relevant files in a coding session — which largely speeds up response times.
4. Build a macOS Spotlight style widget to quickly send our edit instructions for the agent to pick up and work while you focus on the code front and centre.

Since everything runs locally on your machine, this is also a more privacy-friendly approach and gives the optional benefit of using your keys & contracts with cloud model providers — and we’re more than happy to speak with companies that are interested in setting this up. If you are someone who loves tinkering with LLMs, all the requests & responses are just stored on a SQLite DB on your machine (and nothing at our end), which is data that could perhaps be used in the longer run to fine-tune or build features to improve AI performance over time within teams.

There is still a ton to do in terms of robustness and capabilities. Despite all the progress, we still feel we’ve only explored about 1% of what coding with AI could look like. For now, we’d love for you to try out Aide at <https://aide.dev>. To keep things simple, we have a standard subscription plan with a 2-week trial to try out the editor. We’d love to hear your feedback and ideas!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85305&key=user_uploads/89898/ac8a2779-6f50-4489-bd96-b7739eb66724)

## CodeStory ✨ is an AI-powered mod of VSCode.

TLDR: CodeStory ✨ is an IDE for engineers of the future. CodeStory enables deep integration for AI assistants with your development environment, so your pair programmer can complete complex tasks and get it right.

### The problem ⚙️

As programmers, we like to break down our tasks into small chunks that can be executed independently. Consider the simple task of **adding a widget to show sales numbers on your website** which can involve multiple steps:

* Database queries to fetch the data on the backend
* Exposing an API route to make the data available for the frontend
* Frontend UI and API integration to complete the task

Even within a single codebase, such a task requires finding and making the right changes in multiple parts and connecting them together. Though this can be done independently and in parallel, there is only so much an engineer can do at a time.

We thus decided to build CodeStory, **a next-generation code editor that is AI-first, where humans assist powerful AI agents instead of the other way around!** We have started with a VSCode extension in order to prototype the capabilities.

### Watch CodeStory debug and build itself! 🤯

It would be a shame if CodeStory couldn’t debug or build itself... so we put it to work!

Here we asked CodeStory to do proper dependency injection (you can see it using references, searching for symbols using ripgrep and cmd+click on a symbol like a true programmer!)

<https://youtu.be/pY4QWEqG8Es>

In the following video, we asked CodeStory to fix an annoying bug with a race condition happening in our async codebase and write a test to make sure the issue does not repeat again.

<https://youtu.be/-5LH9W-XHC4>

### How we are solving it? ✨

To be effective as software engineers, we need access to tools. We realized early on that even our editor is full of features that aid in writing code and debugging it.

To make CodeStory effective as an engineer, we gave it the following powers 🔋:

* Language Server integration 📝
  * CodeStory can ask for references of a symbol or cmd+click to a symbol to investigate more
* Terminal access 🖥️
  * CodeStory can freely run commands on the terminal when required in a sandbox environment.
* Code Graph of the whole codebase 〽️
  * CodeStory knows how different classes and modules are linked to each other, so it can search your whole codebase semantically (both natural language)

### The future 📡

We love AI-powered development and envision a future where humans are gluing AI agents to work together.

### The team 👥

Hi all! We are Naresh and Sandeep, co-founders of [CodeStory.ai](http://CodeStory.ai) and close friends for over a decade. We met in our freshman year at University and since then Sandeep worked as Tech leads for Testing Infrastructure at Meta and building out devtooling for engineers, and founding engineers at startups (YC backed!) and fintech.

### Our ask 🙏

We are currently on-boarding users for CodeStory slowly to gather detailed feedback. If you’d love to try CodeStory, we are active on [discord](https://discord.gg/Cwg3vqgb) or [twitter](https://twitter.com/codestoryAI), and would be happy to help you onboard and answer any questions.

You can also reach out to us directly at [founders@codestory.ai](mailto:founders@codestory.ai) to talk more about the future of AI-powered coding. We are very, very excited about this!
