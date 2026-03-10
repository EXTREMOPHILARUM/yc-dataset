# Launches

## Kalpa Labs: Scaling Generalist Speech Models

# TL;DR

We’re building a **generalist speech model** - one system that does speech-to-text, text-to-speech, speech-in/speech-out reasoning, and cross-modal tasks with **LLM-level steerability and context** **engineering**. See the demo of [emergent capabilities](https://www.notion.so/2a83ca000c7780a7be71ed49447a882d?source=YC).

![Video](https://youtu.be/b0gAEsp3YdM)

# Problem

Today’s speech stack is fragmented. You need different models, and vendors for STT, TTS, voice design, conversational agents, dubbing, even music. That **“Curse of Specialization”** creates brittle workflows, poor context carryover, and zero “system-prompt” steerability. Meanwhile, LLMs proved that one generalist model + in-context learning [unlocks entirely new use cases](https://arxiv.org/abs/2005.14165).

**What’s missing in current speech models**

1. **Contextual awareness:** They ignore emotional/prosodic cues and can’t adapt delivery to spoken context history. Their response is the same whether the user says the sentence while crying, laughing, or in a banal tone.
2. **Instruction following:** There’s no real analogue to LLM system prompts like _“Speak slower for older callers” “Pronounce ‘WORA’ like ‘wah-rah’” “Use a neutral US accent unless user is in India”_.
3. **Generalism:** Separate models for STT/TTS/music/voice cloning make cross-specialization tasks impossible. Example: _“sing a song in my voice with the following lyrics and the tone from this audio clip”_.

We’re disciples of [Sutton’s Bitter Lesson](https://www.cs.utexas.edu/~eunsol/courses/data/bitter_lesson.pdf): performance eventually comes from scaling compute, data, and simple, general methods. We believe speech is where text was in 2019 - constrained by small models, fixed task boundaries, and narrow post-training. The upside is to do for speech what GPT-3/ChatGPT did for text: **one model, in-context learning, and steerability**.

Audio tokenization (RVQ) and decoding stacks are ripe for redesign - big efficiency wins are still on the table.

# What’s hard & what we changed

Audio is token-hungry. With typical RVQ, 1s of audio ≈ 100–400 tokens. Flattened token streams like [Orpheus](https://huggingface.co/canopylabs/orpheus-3b-0.1-ft) cap useful context that consumes 8K tokens to generate 90s of audio. Approaches like [CSM-1B](https://huggingface.co/sesame/csm-1b) help with context but still decode 32+ audio tokens per step, throttling inference.

We’ve removed the long-audio bottleneck, making audio roughly as cheap to train on as text while preserving long-range context. Practically, that means, you’ll be able to generate hours of audio in one-shot and use speech models with very long interleaved text and audio system prompts.

# Our Progress

We’ve pretrained speech models from 800M to 4.8B params on 2M hours of mixed-domain audio. \
\
**Cost Efficiency**: As a result of our efficient architecture, our 800M parameter model took less than $1000 to train. For a comparison, Kokoro-82M while being 10x smaller took $1000 to train on 1000x lesser data.

# Emergent Behavior

Our larger base models already show visible signs of emergent behaviour. We describe here, some of these behaviours - but the extent of such emergent capabilities is still under investigation.

Please checkout the audios and comparision with ElevenLabs V3 [on notion.](https://www.notion.so/2a83ca000c7780a7be71ed49447a882d?source=YC)

**Disfluency & repetition handling**\
Text: _“This is a a sentence we want our speech model to, to speak.”_

**Contextual identity/accents**\
“I am a software engineer living in _Bangalore_.” → natural Indian English\
“I just moved to _Shanghai_ for a new role.” → adapts toward Chinese-English prosody

\
**Note:** that there is no hardcoded voice switch; this emerges from context.

**Prosodic context awareness without explicit tags**\
“I said we could _try only once_.”\
“I said we could _ONLY_ try once.”\
“_I_ said we could _ONLY_ try _ONCE_?”

\
Stress and intonation match intent without explicit tags like _&lt;laugh&gt;, &lt;gasp&gt;, &lt;surprised&gt;_

**Voice diversity**

These base models can mimic a wide range of speakers/accents beyond a fixed dropdown of voices.

**What we’re building**

A single speech generalist you can steer like an LLM:

* Speech-in / speech-out with system prompts and audio examples “adopt this tone; pronounce these domain terms like this”
* Generalist Model: STT, TTS, conversational agents, dubbing, and cross-specialization (e.g., “sing this verse in my voice,” “explain this chart out loud in a calm tone”).

We’re solving this by

1. **Scale**: keep pushing model size, data diversity, and post-training task complexity.
2. **Align**: instruction-following for speech - system prompts + audio-in-context.
3. **Distill**: real-time deployment targets with graceful latency/quality trade-offs.

# Our Asks

* Have a speech use case that current models fail at? Tell us, we’ll try our best to solve your edge cases.
* Running speech in production? and have strong opinions on what current speech models do right or wrong. We would love your opinions. Coffee’s on us.
* Compute partners: If you can offer clusters ≥128×B200, we’re eager to collaborate.
* Early pilots: If you want to try out this models in early access and help us navigate the future of speech models - we’d love to chat.

You can reach out to us on \
Email: [founders@kalpalabs.ai](mailto:founders@kalpalabs.ai)\
X : [Prashant](https://x.com/pshishodiaa) | [Gautam](https://x.com/JhaGauti) | [KalpaLabs](https://x.com/KalpaLabsAI)\
Linkedin: [Prashant](https://www.linkedin.com/in/pshishodia/) | [Gautam](https://www.linkedin.com/in/gautam-jha37/) | [KalpaLabs](https://www.linkedin.com/company/kalpalabs/)

---

# About us

* **Prashant** led full-stack ML for Google Assistant; trained/evaluated models and scaled smaller Gemini variants to billions of queries/month.
* **Gautam** built nanosecond-latency infrastructure for high-frequency trading.
