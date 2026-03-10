# Launches

## Omnara: Run Claude Code from Anywhere 🤖

We’re Ishaan and Kartik, and we’re building **Omnara**, a web and mobile interface for Claude Code that lets you keep coding agents moving even when you’re away from your desk.

🎥 Demo:[ https://x.com/i/status/2014383431845839186](https://x.com/i/status/2014383431845839186)

## **❌ The Problem**

Coding agents can work independently for long stretches, but they still block on human input.

If an agent needs clarification while you’re away, everything pauses.\
If your laptop sleeps, long-running work stops.\
Most remote agent tools run in hosted environments instead of where your code actually lives.

Agents should fit around your schedule, not the other way around.

## **🛠️ The Solution**

**Omnara makes working with coding agents feel continuous instead of fragile.**

You can:

* Start agents locally and stay involved from anywhere using web or mobile
* Keep work moving even if your laptop goes offline
* Talk to agents using voice when typing isn’t convenient

## **🔒 Run agents in your environment, access them from anywhere**

With Omnara, your coding agent runs on your own machine, whether that’s your laptop or a remote VM you control.

You can access and interact with that agent from anywhere, securely, without SSH, port forwarding, or tunneling.

Your agent runs in your real environment, but you’re not tied to the machine it’s running on.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97081&key=user_uploads/2661368/81388baf-658a-4c43-94ac-1ce4e17a1605)

## **☁️ Keep agents running when your machine is off**

Agents shouldn’t stop just because your laptop does.

If your machine goes offline, Omnara can keep the agent running in the cloud so work continues. You can still interact from web or mobile, and when you’re back at your desk, you can pick up where things left off.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97081&key=user_uploads/2661368/098a8bf1-046d-4362-86b2-63d984e999dd)

## **🎙️ Talk to your coding agent**

Mobile typing works for quick replies, but it’s not great for longer back and forth.

Omnara includes voice so you can talk to your coding agent when typing isn’t convenient. Speaking tends to provide more context and makes it easier to iterate, especially while walking or multitasking.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97081&key=user_uploads/2661368/829c73b5-6a60-41e8-a9c3-0fa98de80d39)

## **💸 Pricing**

* Free: up to 10 agent sessions per month
* $20/month: unlimited sessions
* When agents run in your environment, you can use your existing Claude Pro or Max subscription

## **🙏 Our Ask**

If you use Claude Code or rely on long-running coding agents, we’d love your feedback.

👉 Try it: [omnara.com](https://www.omnara.com/)

[👉](https://www.omnara.com\)%F0%9F%91%89) Install in one line:\
curl -fsSL <https://omnara.com/install/install.sh> | bash

👉 Reach us: [founders@omnara.com](mailto:founders@omnara.com)

— Ishaan & Kartik

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97081&key=user_uploads/2661368/6ef3e27b-3742-4e1a-9d77-1ec8a6c5bc41)

## Omnara - The first command center for AI agents: terminal, web, and mobile

https://www.loom.com/share/03d30efcf8e44035af03cbfebf840c73

Start Claude Code in the terminal, then pick it up instantly on web or mobile with a seamless handoff between all three

### The Problem

Claude Code is incredible, but it chains you to your desk.\
Once an agent starts working, you’re stuck waiting in the terminal for it to ask you something. That could take 5–10 minutes, and if you’re away, progress halts. We’ve coded from our beds, on walks, in Ubers, while doing laundry… and yes, even on the toilet — but only after we built Omnara.

Existing solutions don’t solve this well:

* **Other Claude Code wrappers** (e.g., Crystal, Conductor) often replace the native experience but don’t let you jump between terminal, web, and mobile.
* **Terminal replication tools** (e.g., Vibetunnel, Termius) let you SSH in, but have no push notifications, clean diffs, or simple setup.

### What’s Omnara?

Omnara is the **first agent command center** — start an AI agent in the terminal, then continue the same session from our web dashboard or mobile app.

With Omnara, you can:

* Launch agents from terminal, web, or mobile.
* Switch between them instantly.
* Get **real-time push notifications** when agents need your input.
* Review logs, see Git diffs, and approve/reject changes with one tap.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93029&key=user_uploads/1391601/bf61f9ae-4f37-4377-90c8-fc2bed1d0866)

**How it works**\
We built a CLI wrapper that mirrors the native Claude Code experience — output, permissions, notifications, and mode switching — by parsing the session file at _\~/.claude/projects_ and terminal output in real time. All agent and user messages are streamed via SSE to the Omnara platform, where you can respond from anywhere.

It’s fully open source: [github.com/omnara-ai/omnara](https://github.com/omnara-ai/omnara)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93029&key=user_uploads/1391601/837e9af0-e038-4bb1-9f1c-1ebf152f8157)

### Why launch with Claude Code first?

Omnara works with any AI agent, but Claude Code users immediately “get” the value. It’s the perfect human-in-the-loop use case — and the one we use every day.

We’ve also used Omnara as a human-in-the-loop node in n8n workflows, e.g., for replying to emails. This is just the beginning.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93029&key=user_uploads/1391601/96e585a6-db46-4a20-8901-0ddbc7e409cf)

### Pricing

Free for up to 10 agent sessions/month.\
$9/month for unlimited.

### About Us

We’re **Ishaan & Kartik**, childhood friends since Montessori. We’ve spent years working in AI and AI infra at big tech and acquired startups and love building tools that remove friction for developers.

### Try it free

`pip install omnara && omnara`Then log in at [omnara.com](http://omnara.com) or download our iOS app: [Omnara on the App Store](https://apps.apple.com/us/app/omnara-ai-command-center/id674...)
