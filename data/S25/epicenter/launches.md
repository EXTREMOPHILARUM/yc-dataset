# Launches

## Whispering: Local-First, Open-Source Speech to Text at Your Fingertips

Hey everyone! 👋 It's Braden, and I'm excited to introduce Whispering—a fully open-source, local-first speech-to-text app, and the first app in the Epicenter ecosystem. You can [give it a star](http://go.epicenter.so/github), install it [here](https://go.epicenter.so/install/whispering), and start using it today.

I use Whispering multiple hours daily for voice coding, writing, and thinking out loud. I churned from Wispr Flow and Superwhisper after I built it.

I think the ergonomics are quite delightful, and I hope you will too!

[Voice coding workflow](https://www.youtube.com/watch?v=tpix588SeiQ)

## **The Problem**

You use a transcription app, but you have no idea what happens to your data.

They’re not open-source. They might call themselves “local” or say “inference stays on device”—but you still can’t see the code. It’s a black box, and for all you know, _you’re the product_.

Your voice recordings might be sitting on their servers and sold to other providers. You're locked into their ecosystem. When they pivot, get acquired, or shut down, your workflow will break.

Many “AI transcription” startups are just API or local inference wrappers with subscription pricing. You speak into their app, they send your audio to a transcription API like Whisper, then charge you monthly for what you could run yourself. Some run locally, but none I found were open-source with the UX I needed.

## **The Solution**

Truly free and open-source transcription software that matches (or surpasses) the ergonomics of paid, closed-software alternatives. I think Whispering is now at that stage.

## **What makes us different:**

There are many other applications in the transcription landscape. Whispering offers some notable features:

* **Hands-free, voice-activated dictation**: One of our most ergonomic features so far. Press once to start the session, and it will automatically start and stop as you speak. No button-holding or toggling nonsense. Perfect for dictating when your hands are full
* **Custom AI transformations with any prompt, any model:** Design custom transformations that chain multiple AI models to fix grammar, translate, or refactor your transcribed text
* **Unbeatable price:**  Nothing beats free. If you bring an API key from [Groq Cloud](https://console.groq.com/keys), you’ll get nearly instantaneous transcription at $0.04/hour plus a generous free tier. And of course, if you run locally with Speeches, it’s completely free. We hope to expand our models soon.
* **Open-source**: MIT licensed. Fork it, examine it, roast it. We pride ourselves in our code quality.
* **Everything is local-first**: In Whispering, everything is local-first. Recordings are stored in IndexedDB, and settings are stored in local storage. Built with Svelte 5 and Tauri, and it's tiny (\~22MB) and fast.

## **Real Daily Usage**

* **Talking to Claude in my room** (3-4 hrs/day): I use dictation to prompt Claude Code significantly faster than typing. I have a custom post-processing transformation set up so that every text blob that I dictate is passed through a Gemini 2.5 Flash prompt, making the output more Claude-Code-friendly (bullet points, etc.). Once done, I paste into Claude Code.
* **While carrying pizza boxes back from the Y Combinator office:** My hands are full, so I’ll open the web app on my phone, turn on voice activated dictation, and then start yapping as thoughts come up. The words are waiting when I get back in my room
* **Other custom transformations**: I have a common writing workflow of speech → Transcribe (Groq) → Fix Grammar (Claude 4 Sonnet) → Format (Gemini 2.5 Flash).

## **Why This Matters**

Fundamental tools shouldn’t require trusting a black box. And they shouldn’t charge you rent for something you could run yourself.

We believe productivity apps should be open-source and transparent with your data, and we want to destroy their business models with open-source alternatives.

These alternatives will need to match them feature-by-feature, have a great UX, and eventually, be built on top of our shared memory layer.

## **Where This Is Going**

Whispering is the first app in the Epicenter ecosystem: local-first, open-source tools built on top of a shared memory of plain text and SQLite. We hope to replace siloed, data-driven tools with local-first alternatives that share a single, user-owned memory layer.

We also hope to support many more offline models over time, giving you maximum flexibility in how and where your data is processed.

We’re not stopping at transcription. While most transcription apps tinker with static dictionaries or custom word lists, our eventual goal with Epicenter is to leverage that shared memory. We could connect transcription to everything you think, write, and build, all within a trustworthy, local-first environment.

Whispering would pick up your common phrases, technical terms, and more. Over time, you create custom transformation pipelines that adapt to your writing style, your voice, and your world.

## **Our Ask**

* 🌟 [**Upvote on Product Hunt**](https://www.producthunt.com/products/whispering?launch=whispering). Help others discover open-source alternatives
* 💻[ **Download the desktop app**](https://go.epicenter.so/install-whispering) from our [installation guide](https://go.epicenter.so/install/whispering), or directly from our latest [releases](https://github.com/epicenter-so/epicenter/releases)
* ⭐ [**Star on GitHub**](https://github.com/epicenter-so/epicenter/tree/main/apps/whispering). Back local-first software. Fork it, break it, improve it. Everything’s MIT licensed. Copy whatever you want.
* 💬 [**Join our Discord**](https://go.epicenter.so/discord). Shape what we build next

Try it, and let us know what’s up. I hope Whispering becomes a part of your workflow!

[Full Setup Guide](https://www.youtube.com/watch?v=1jYgBMrfVZs)

## Epicenter: A Database for Your Mind, Built on Plain Text

**TL;DR:** if you're a hacker, a generalist, a cracked Svelte/Typescript developer, or a local-first/open-source/privacy enthusiast, join our [Discord and DM me](https://go.epicenter.so/discord). I would love to build with you.

https://www.youtube.com/watch?v=nZNOH5yKxO0

Hey everyone! 👋 It’s[ Braden](https://www.linkedin.com/in/braden-wong/), and I’m building Epicenter.

Epicenter is an open-source suite of tools built around a single idea:

**Creativity thrives when you blur the lines between disciplines.**

Your tools should reflect that. Most tools divide you—one for writing, one for planning, one for research. We’re building tools that talk to each other—so you can stay in flow across every kind of work. 

Epicenter will be a growing software ecosystem—a text editor, a CRM, a personal assistant, and more—all built around a shared local memory.

**The problem**

Modern knowledge work is fragmented.

I journal into an app I don’t trust. I plan my week in a calendar app I’ll abandon next month. My notes drift aimlessly in systems I’ve outgrown. And every time I switch apps, the app forgets what I was working on.

Notes, code, and ideas live in isolated tools that don’t talk to each other, breaking flow and burying context.

**The solution**

A suite of open-source tools that share a single memory: a folder on your machine. Open-source, open-format, and fully yours.

The tools share so you can make connections across disciplines. Your ideas and data are never locked in.

[**epicenter.sh**](http://epicenter.sh)

I just launched [epicenter.sh](http://epicenter.sh): a local-first assistant you can chat with. It lives in a folder, and we want to make it the access point to everything you’ve ever written, thought, or built.

[epicenter.sh](http://epicenter.sh) is the first addition to Epicenter. This is your new shell: your second brain becomes your dialogue partner. You type; it thinks. You ask; it searches. Under the hood, it’s powered by a modified version of [Opencode](https://github.com/sst/opencode), an excellent open-source coding agent. We’ve made our own CLI and UI to simplify configuration and the user experience. It’s rough around the edges, but it’s our first step in laying the foundation for our future applications.

**Where We’re Headed**

In a world where every app wants to trap you and your data, we’re building the opposite.

Epicenter is open-source, local-first, and plain-text native—so you can trust it, tweak it, or take it with you. We’re building tools that support intentional, interdisciplinary thinking: software for people who read, write, build, and connect.

A renaissance workflow, built on plain text and real ownership.

**Our Ask**

We’re early. But if you think like a generalist, build like a hacker, and value tools that respect your mind—we’d love to hear from you.

**→ if you’re a cracked Svelte/Typescript developer, please[ DM me](https://go.epicenter.so/discord)**

**→ star / fork / dive into the code on GitHub: [https://github.com/epicenter-md/epicenter/](https://github.com/epicenter-md/epicenter/)**

**→ join the community on [Discord](https://go.epicenter.so/discord). share what you’re excited to build**

Sign up and tell us which tools you’d be most excited to use. Your input will shape what we build next.

**About me:**

At 18, I taught myself to code while studying ethics, politics, and economics at Yale. Since then, I’ve averaged \~10k commits/year and worked at three YC startups. I wrote my 65-page senior thesis on open-source governance and digital platforms. I care deeply about data ownership, open-source, and interdisciplinary thinking.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92752&key=user_uploads/1027274/a3ef7b07-ca73-4d27-bf0a-53e194f9f587)
