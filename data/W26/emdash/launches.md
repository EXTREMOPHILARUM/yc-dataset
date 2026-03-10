# Launches

## Emdash - Open-source Agentic Development Environment (ADE)

Hey YC! 👋 We’re Arne and Raban the we’re building [Emdash](https://emdash.sh). An [open-source](http://github.com/generalaction/emdash) desktop app that lets you work with multiple coding agents at once. We’re calling it an Agentic Development Environment (ADE).

<https://youtu.be/jdIPf2cxf6w>

💬 **Problem**\
Every time we used a coding agent, we'd start a task and ... wait. We tried running multiple agents on the same repo and ended up with branch chaos and merge conflicts. When a new model dropped – Opus, Codex, Gemini flash, Kimi, whatever – we had no clean way to test it against our current setup on the same task. We were bouncing between terminals, GitHub, and our IDE.\
\
⏩ **Solution**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97799&key=user_uploads/1755188/dd08968b-2b60-4a85-b998-e8cc9d017dfc)

Emdash is an environment for agentic development that lets you run multiple agents side-by-side safely, review what each one did in one place, and create a PR when it looks right.

🔍 **How it works**

* Start a task → Emdash spins up a new git worktree so nothing touches your main directory
* Choose any agent, out of 20+ providers(incl. Claude Code, Codex, Gemini)
* Run multiple agents at once without conflicts
* Compare diffs, make quick manual edits if needed, and create a PR

🧰 **What’s included**

* Worktree isolation per agent
* Issue handoff from Linear / Jira / GitHub
* One place to review diffs and ship PRs
* Lifecycle scripts + CI/CD hooks
* Best-of-N comparisons
* Integrated file editor + browser preview
* Remote project access via SSH

We natively embed \~20 agent providers (including Claude Code, Codex, Continue, and Codebuff), so you can use the latest models inside the same workflow.

To get started run `brew install –cask emdash`or download directly from[ GitHub releases](https://github.com/generalaction/emdash/releases). We’re available on macOS and Linux.

**🙏 Our Asks**

1. Try [Emdash](https://emdash.sh/) - it’s free and open-source
2. Give us a star on [GitHub](http://github.com/generalaction/emdash) **🌟**

Questions or feedback? Join our [Discord](https://discord.gg/m9APwzK4qd) or email us at [founders@emdash.sh](mailto:founders@emdash.sh)

— Arne & Raban

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97799&key=user_uploads/1755188/b2b6adc8-60e6-4701-9643-fa622c4a5e96)
