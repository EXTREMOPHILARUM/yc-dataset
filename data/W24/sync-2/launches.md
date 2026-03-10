# Launches

## [sync.] we built the most natural lipsync model in the world, again.

# tldr;

* lipsync-2 is the most advanced video-to-video lipsyncing model in the world
* It’s zero-shot, so you don’t need to wait for an “actor”, “clone”, or “avatar” to train before using it.
* Even so, it learns and generates a speaker’s unique style of speech
* It works across live-action, animated, and AI-generated humans
* Thousands of developers use it to build video translation, word-level editing of video, and character re-animation workflows today (including generating realistic AI UGC)
* We’re launching our YC deal, **4mo’s of our scale plan for free plus $1000** **in credits** 🚀

<https://www.youtube.com/watch?v=j5iJ2k05ltc>

# What did we build?

We built lipsync-2, the first in a new generation of zero-shot lipsyncing models. It seamlessly edits any person's lip movements in a video to match any audio without having to train or be fine-tuned on that person.

Zero-shot lipsync models are versatile because they edit any arbitrary person and voice without having to train or fine-tune on every speaker. But traditionally they can lose traits unique to the person, like their speaking style, skin textures, teeth, etc.

With lipsync-2, we introduce a new capability in zero-shot lipsync: _style preservation_. We learn a representation of how a person _speaks_ by _watching_ how they speak in the input video. We train a spatiotemporal transformer that encodes the different mouth shapes in the input video into a style representation. A generative transformer synthesizes new mouth movements by conditioning on the new target speech and the learned style representation.

# How can you use it?

We built a simple API that let’s you build workflows around our core lipsyncing models. You submit a video and an audio (or a script and voiceID to generate audio from), and get a response with the final output.

We see thousands of developers and businesses integrating our APIs to build generative video workflows into their products and services.

# \[1\] Video translation

Notice how even across different languages, we preserve the speaking style of Nicolas Cage. We are the first zero-shot lipsyncing model to achieve this.

<https://youtu.be/GaCoHy99zT4>

We can even handle long videos with multiple speakers — we built a state-of-the-art active speaker detection pipeline that associates a unique voice with a unique face, and only applies lipsync when we detect that person is actively speaking.

<https://www.youtube.com/watch?v=ZaXbiKdoBz8>

It also works across animated characters, from Pixar-level animations to AI generated characters.

<https://www.youtube.com/watch?v=F_6lGFl6bcA>

But translation is only the beginning, with the power to edit dialogue in any video in post-production we’re on the cusp of reimagining how we create, edit, and consume videos forever.

# \[2\] Record once and edit dialogue to use forever.

<https://youtu.be/HJR4BbhZ8Uo>

Imagine a world where you only ever have to hit record once. lipsync-2 is the only model that let’s you edit a dialogue while preserving the original speakers style, _without needing to train or fine-tune beforehand._

## \[3\] AI video

In an age where we can generate any video by typing a few lines of text, we don’t have to limit ourselves to what we can capture with a camera.

<https://youtube.com/shorts/KnzWtu3niKQ>

## Our YC deal

For any YC company we’re giving away our Scale Plan for free for 4 months, plus $1000 to spend on usage.

With the scale plan you get access to up to 15 concurrent jobs processing at once and handle up to 30 minute video at a time — leveraging this maximally you have the ability to generate around **\~90 minutes of video per hour every hour.**

Launch an AI admaker, video translation tool, or any other content generation workflow you want and serve viral load with speed, reliability, and best-in-class quality.

Email us at [yc@sync.so](mailto:yc@sync.so) and we’ll get you set up.

## So why does this matter?

At sync, AI lipsync is just the beginning.

We live in an extraordinary age.

A high schooler can craft a masterpiece with an iPhone. A studio can produce a movie at a _tenth of the cost 10x faster_. Every video can be distributed worldwide in any language, _instantly._ Video is becoming as malleable as text.

But we have two fundamental problems to tackle before this is a reality:

\[1\] Large video models are great at generating entirely new scenes and worlds, but struggle with precise control and fine grained edits. The ability to make subtle, intentional adjustments – the kind that separates good content from great content – doesn’t exist _yet_.

\[2\] If video generation is world modeling, each human is a world unto themselves. We each have idiosyncrasies that make us unique — building primitives to capture, express, and modify them with high precision is the key to breaking through the uncanny valley.

We’re excited about lipsync-2, and for what’s coming up next. Reach out to [founders@sync.so](mailto:founders@sync.so) if you have any questions or are curious about our roadmap.

## sync. – AI lip sync tool for video content creators

**TL;DR:** we’ve built a state-of-the-art lip-sync model – and we’re building towards real-time face-to-face conversations w/ AI indistinguishable from humans 🦾

try our playground here: <https://app.synclabs.so/playground>

**how does it work?**

[ ](https://www.loom.com/share/a82317f622ec4e389387849a6c4a2073?sid=3f0b2b1e-4212-4940-bcca-b10aefeeda3e)

theoretically, our models can support any language — they learn phoneme / viseme mappings (the most basic unit / “token” of how sounds we make map to the shapes our mouths make to create them). it’s simple, but a start towards learning a foundational understanding of humans from video.

**why is this useful?**

_\[1\] we can dissolve language as a barrier_

check out how we used it to dub the [entire 2-hour Tucker Carlson interview with Putin speaking fluent English.](https://vimeo.com/914605299)

imagine millions gaining access to knowledge, entertainment, and connection — regardless of their native tongue.

realtime at the edge takes us further — live multilingual broadcasts + video calls, even walking around Tokyo w/ a Vision Pro 2 speaking English while everyone else Japanese.

_\[2\] we can move the human-computer interface beyond text-based-chat_

keyboard / mice are lossy + low bandwidth. human communication is rich and goes beyond just the words we say. what if we could compute w/ a face-to-face interaction?

maybe embedding context around expressions + body language in inputs / outputs would help us interact w/ computers in a more human way. this thread of research is exciting.

_\[3\] and more_

powerful models small enough to run at the edge could unlock a lot:

eg.

extreme compression for face-to-face video streaming

enhanced, spatial-aware transcription w/ lip-reading

detecting deepfakes in the wild

on-device real-time video translation

etc.

**who are we?**

[ ](https://www.loom.com/share/42b332287f3d473196d1a0929099e3ea?sid=604edca5-f5ba-441a-9e23-d8e1f6ac5aa5)

[**Prady Modukuru**](https://www.linkedin.com/in/prady-modukuru) **\[CEO\] |** Led product for a research team at Microsoft that made Defender a $350M+ product, took MSR research into production moving it from bottom of market to #1 in industry evals.

[**Rudrabha Mukhopadhyay**](https://www.linkedin.com/in/rudrabha/) **\[CTO\] |** PhD CVIT @ IIIT-Hyderabad, co-authored wav2lip / 20+ major publications + 1200+ citations in the last 5 years.

[**Prajwal K R**](https://www.linkedin.com/in/prajwalrenukanand/) **\[CRO\] |** PhD, VGG @ University of Oxford, w/ [**Andrew Zisserman**](https://scholar.google.com/citations?user=UZ5wscMAAAAJ&hl=en), prev. Research Scientist @ Meta, authored multiple breakthrough research papers (incl. Wav2Lip) on understanding and generating humans in video

[**Pavan Reddy**](https://www.linkedin.com/in/pavan-reddy-8bb85a67/) **\[COO/CFO\]** 2x venture-backed founder/operator, built the first smart air purifier in India, prev. monetizing sota research @ IIIT-Hyderabad, engineering @ IIT Madras

**how did we meet?**

Prajwal + Rudrabha worked together at IIIT-hyderabad — and became famous by [shipping the world’s first model](https://github.com/Rudrabha/Wav2Lip) that could sync the lips in a video to any audio in the wild in any language, no training required.

they formed a company w/ Pavan and then worked w/ the university to monetize state-of-the-art research coming out of the labs and bring it to market.

Prady met everyone online — first by hacking together a viral app around their open source models, then collaborating on product + research for fun, to cofounding sync. + going [**mega-viral.**](https://x.com/therealprady/status/1680645510103977987?s=20)

Since then we’ve hacked irl across 4 different countries, across the US coasts, and moved into a hacker house in SF together.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79187&key=user_uploads/587624/1beb86a1-5ea0-404a-aab7-ada7eff4f154)

**what’s our ask?**

try out our playground and API and let us know how we can make it easier to understand and simpler to use 😄

play around here: <https://app.synclabs.so/playground>
