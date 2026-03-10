# Launches

## Vogent Voice Agent Wizard: build voice agents with just a description

**TL;DR:** **Vogent's Voice Agent Wizard uses AI trained on thousands of real agent designs to generate complete, ready-to-deploy voice agents from a simple description and any relevant files**

https://youtu.be/IKisqK4cO5U

Building a performant voice AI agent today means weeks of trial and error—clicking through dashboards, configuring countless parameters, testing edge cases, and waiting on support tickets. By the time you've iterated your way to something that works, your competitors have shipped and your launch momentum is gone.

**Introducing Vogent's Voice Agent Wizard.** Trained on thousands of real agent design processes, our wizard understands what makes voice agents work in production. Just describe what you want your agent to do, attach a few transcripts or conversation examples, and it builds a complete, production-ready voice agent in minutes—not weeks.

The wizard handles everything: reasoning through the right agent architecture for your use case, configuring optimal parameters, generating appropriate system prompts, and even anticipating edge cases based on patterns it's learned from real deployments. What used to take experienced engineers days of iteration now happens automatically.

The result? You can go from idea to deployed voice agent immediately. Test new use cases instantly. Iterate in real-time based on user feedback. Focus on building your product, not wrestling with infrastructure.

**Try the Agent Wizard today at [app.vogent.ai](http://app.vogent.ai)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95431&key=user_uploads/539546/0cb9a065-4760-44be-bdce-c3e00b4f1636)

## Vogent Turn: State-of-the-art Turn Detection for Voice AI

**TL;DR: Vogent-Turn-80M is a state-of-the-art turn-detection model that detects when users are done speaking with extraordinary accuracy, so your voice AI can stop interrupting.**\
\
https://youtu.be/XQeSUc2ID6g

What makes conversation feel natural isn't just what we say; it's knowing when to speak and when to listen. Current voice AI systems struggle with this fundamental challenge, either interrupting users mid-thought or waiting awkwardly long after they've finished. The problem? Existing turn detection relies on either audio-only signals (missing semantic context) or text-only analysis (losing critical vocal cues). When a user says "I'm flying from San Francisco..." are they pausing to think, or done answering? Audio and text alone can't tell; but humans know instantly.

**Introducing Vogent-Turn-80M**. Vogent-Turn-80M solves this by doing what humans do naturally: processing both how you're speaking and what you're saying simultaneously. Built on a streamlined 80M parameter architecture, our model fuses acoustic features from audio with conversational context from text, enabling it to understand that "123 456" with rising intonation means more is coming, while "I'm departing from San Francisco" is incomplete when asked about two airports. This multimodal approach achieves 94.1% accuracy while running in just \~7ms on a T4 GPU—fast enough to feel completely natural in real-time conversations.

The result? Voice agents that finally feel like talking to a human. No more frustrating interruptions. No more awkward pauses. Just natural, flowing conversation that responds at the right moment, every time.

Hugging Face: https://huggingface.co/vogent/Vogent-Turn-80M

GitHub: https://github.com/vogent/vogent-turn

Blog Post: https://blog.vogent.ai/posts/voturn-80m-state-of-the-art-turn-detection-for-voice-agents

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94839&key=user_uploads/539546/d4b5cab9-e1c3-47cf-bcc5-cc4d519a1d88)

## Vogent Voicelab: API to run top open-source voice models, like CSM-1B

We’re excited to launch **Vogent Voicelab (vogent.ai/voicelab): an optimized API to run top open-source voice models.**

New open-source text-to-speech models come out every week, with many ranking as state-of-the-art on popular benchmarks.

However, most of these models are not readily usable for high-volume, low-latency inference. Additionally, some research preview models can struggle with hallucinations and inconsistent outputs. Finally, as with any model, hosting yourself and managing compute can be a headache.

Voicelab solves these problems:

1. Voicelab maintains a proprietary inference stack that is optimized to serve text-to-speech transformers efficiently and scalably.
2. Voicelab post-trains select models to improve consistency and offer high-quality professional voice clones.
3. Voicelab manages all compute, so you can pay for these models per-character instead of managing GPUs.

All of this is exposed through a standard text-to-speech API (with streaming/websocket support) and an online playground.

Docs: [docs.vogent.ai/voicelab](http://docs.vogent.ai/voicelab)

TTS Playground: [app.vogent.ai](http://app.vogent.ai)

https://youtu.be/KMIVXYhb7lY

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91917&key=user_uploads/539546/a6d5dd4f-0ed4-4ed9-9d69-8b12308b3e1d)

## Vogent: *Insanely* Realistic Voice Agents powered by Sesame

TL;DR: Make your voice agents _way_ more realistic and stop getting hangups. Check it out in action at or talk to it yourself by calling our AI Trump voice agent at (510) 315-0014 or [**vogent.ai/sesame**](http://vogent.ai/sesame)

Vogent powers millions of voice AI phone calls for healthcare, customer support, travel, and more.

Today, we’re launching the **most realistic realtime voice engine** ever. It inserts natural pauses and disfluencies (“um”, “uh”) without being explicitly prompted, and is _uncannily_ good at cloning voices. Check it out in the videos below:

<https://youtu.be/CbqTfVQGcd0>

<https://youtu.be/QLiYmsw2-zk>

How did we do it?

If you’ve been online recently, you’ve probably come across Sesame’s super humanlike voice AI, and their open-source launch of CSM-1B, a 1B-parameter text-to-speech model.

We’ve spent the past couple of weeks rearchitecting CSM-1B from the ground-up to support realtime, low-latency inference, and we’ve finally cracked it. The results are pretty insane; it’s a step-function increase in realism (customer hangup rates have decreased by 60%+), and we made it available out-of-the-box.

If you want to create your own Sesame agents, sign up at [**app.vogent.ai**](http://app.vogent.ai), and select one of our Sesame voices. You can also use Sesame to clone new voices, as long as you have a 10-15 second reference clip.

We’re also releasing a realtime Sesame TTS soon; email [j@vogent.ai](mailto:j@vogent.ai) for beta access.

## Vogent: Self-Learning Voice AI

Announcing Vogent Self-Learning: 𝐀𝐈 𝐚𝐠𝐞𝐧𝐭𝐬 𝐭𝐡𝐚𝐭 𝐝𝐞𝐬𝐢𝐠𝐧 𝐚𝐧𝐝 𝐢𝐦𝐩𝐫𝐨𝐯𝐞 𝐭𝐡𝐞𝐦𝐬𝐞𝐥𝐯𝐞𝐬, learning from real failure cases and requiring no prompt engineering. No more need for hundreds of prompt iterations, or burning GPU (and human) hours on fine-tunes that don’t work.

Using reinforcement learning methods, like the kinds used by Deepseek and other research labs, our voice agents design themselves given call recordings, and improve themselves by evaluating every single dial and correcting bad behaviors.

Sign up by going to [app.vogent.ai](http://app.vogent.ai) and clicking “Self Learning”

<https://www.youtube.com/watch?v=Bg6K3wXxozQ>

## Vogent: Build Voice AI Agents, Fast

**TL;DR**: [**Vogent**](https://vogent.ai/) is an all-in-one platform for building voice agents by using intelligent building blocks, including drag-and-drop conversational flow builders, IVR detection models, spelling-optimized voices, custom phone-ready LLMs, and more. Vogent is made for developers and no-code users alike.

<https://youtu.be/mu1rHsGjiMU>

# The Problem

We’ve spent the past year building high-volume voice AI agents for a number of big-ticket customers, including the second largest prescription network in the US, the biggest flight and hotel booking sites in Europe, top-10 health insurance companies, car dealership chains, and more.

While the core voice agent cycle (STT-LLM-TTS-VAD) is a mostly solved problem at this point, the last-mile problem for making these agents performant was frustrating. We ended up building a lot of band-aids, and we decided to consolidate all of the tools that we used to build these agents into a self-serve platform for developers and non-developers alike.

# How Vogent Works

Voice AI isn’t new, and neither are platforms to build agents. Our approach is to also offer higher-level building blocks that make it easier to build performant agents that can handle complex tasks. These include:

* Our drag-and-drop flow builder, which lets teams build agents that are both conversationally flexible and aligned to a task.
* Our counterfactuals feature, which lets you test new agents on past calls
* Our IVR detection model, which can tell the difference between a human or prerecorded message and navigate the latter
* Custom, in-house voices that are optimized for realistic numbers and spelling
* LLMs fine-tuned on millions of phone conversations that can be easily prompted to follow phone-call tasks

As well as other powerful abstractions.

Our other focus is providing as much to developers as possible. We expose most of our platform through GraphQL and REST APIs, and we have a JS SDK that makes voice as easy to add to your product as any other AI modality. (Mobile SDKs in beta – email [j@vogent.ai](mailto:j@vogent.ai) for access!)

# Get Started 

* Sign up now at [**https://vogent.ai**](https://vogent.ai) 
* Join our Discord - [**https://discord.gg/JmThYcyG**](https://discord.gg/JmThYcyG)
* Follow us on X - [**x.com/vogentai**](http://x.com/vogentai) 
* Follow us on LinkedIn - [**linkedin.com/company/vogent**](http://linkedin.com/company/vogent) 
* Email us directly: [**j@vogent.ai**](mailto:j@vogent.ai) 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87288&key=user_uploads/539546/65341827-c3b0-40fe-9fa1-e9fede328808)

## Elto AI: The AI that makes phone calls

**tl;dr:** Elto AI is a highly authentic, low-latency conversational AI that can make phone calls. Elto has automated phone calls to/for health systems, insurance providers, pharmacies, staffing agencies, municipalities, and more. Get a call from the AI at <https://elto.ai>!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80688&key=user_uploads/539546/d298a29f-a5c3-4cde-a2c4-d2455baa28be)

Elto is an end-to-end platform for training, deploying, and monitoring AI voice agents that make phone calls.

### The Problem

Phone calls are the most reliable way to execute tasks and receive information, whether it’s checking the status of an insurance claim or canvassing potential voters. Unfortunately, making phone calls is expensive, time-consuming, and resource-intensive; an offshore human caller can only make 100-300 dials a day, and increasing the number of humans dialing adds management burden. Making calls time-sensitive only adds to the operational complexity.

Others’ attempts to solve this problem with AI fall short; chaining together out-of-the-box API’s makes conversational agents that are difficult to train and **very** slow to respond.

### Our Solution: Custom, Low-Latency Voice Agents

It took a while for us to get here -- we tried to get a version of this working a year ago by naïvely chaining together transcription, language, and text-to-speech services, but we ran into the problem that most AI voice agent solutions have: the latency was too high, instructing unspecialized models to execute tasks on the phone was difficult, and the realism was just not there.\
\
Fast-forward a few months; our parallel dialer ([eltodialer.com](http://eltodialer.com)) was growing quickly, and we realized that it gave us what we needed to fix our earlier issues: from a small subset of consenting customers, we were able to gather troves of conversational data to train condensed, specialized models that were low-latency and worked well on the phone with prompting and few-shot fine-tuning. The dialer also gave us robust infrastructure for serving and monitoring hundreds of thousands of dials a day.\
\
We've used that data and infrastructure to build an end-to-end in-house pipeline for training easy-to-teach, low-latency, realistic voice agents, and have worked with a handful of pilot customers to get the agents to execute tasks consistently. Elto's AI now runs tens of thousands of dials daily with no human oversight, automating work for verticals from logistics providers and healthcare payers to staffing solutions and municipalities, and more, with failure rates lower than those of human callers.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80688&key=user_uploads/539546/05909c0f-0456-453f-b49a-94de17a161ca)

\
\
We're now making the platform generally available on an invite basis. Sign up for an invite on the site!\
\
Note: we _do not_ support sales use-cases for Elto AI, due to TCPA regulations. Check out our parallel dialer ([eltodialer.com](http://eltodialer.com)) instead!

## Elto: Human-in-the-loop AI call center (50% cheaper than typical call center/BPO)

**TLDR:** [**Elto**](https://elto.ai) is a human-in-the-loop AI-powered call center. We automate phone call tasks in ops/support/etc. with AI, while employing a team to oversee the phone calls and interject when necessary. This enables us to offer call center services for a fraction of the price of normal BPO solutions (typically 50% off), while handling more complex tasks, maintaining higher quality conversations, and ramping up more quickly on a task than an AI alone could.

Hey everyone,

We’re excited to launch the evolution of [Elto](https://elto.ai), an AI that makes phone calls, with a great slate of pilot customers calling insurance, tax agencies, and more. Though our initial offering was primarily an AI agent to automate phone calls for ops/support tasks, we’re now expanding to a fully managed human-in-the-loop call center, to enable more complex call tasks and a quicker implementation cycle for the AI.

If you currently employ a BPO firm, call center, or dedicated team members for handling (non-sales) phone calls, our team will manage the task for 50% less. If you’re interested, please reach out to [**j@elto.ai**](mailto:j@elto.ai) and we can get started with a POC easily.

Note: We do not support outbound sales tasks, due to TCPA regulations.

## Elto - AI-powered parallel dialer

TLDR: Elto dials up to 6 prospects at once, detects when a human picks up, and immediately drops the user into the call. Spend less time waiting on dial tones and voicemail, and more time on the phone with engaged prospects. 

Hey everyone, 

We’re Jagath and Vignesh, and we’re building Elto. Elto is an AI-powered parallel dialer that makes cold-calling _way_ less painful and more productive. 

**The Problem** 

Cold-calling _sucks_. Sitting through dozens of dial-tones and voicemail inboxes can be exhausting and demoralizing, and while getting on the phone with an engaged prospect can be magical, it’s easy to go through multiple _days_ without a productive conversation. With a 3% pickup rate, for example, it can take **2 hours** of dialing to get a prospect on the phone (let alone a prospect who converts!).

**The solution**: Elto **dials 6+ contacts in parallel, detects when someone answers, and connects the pickup to the user.** The rest of the calls disconnect immediately, so they can be re-dialed later.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72727&key=user_uploads/539546/969b79ec-53c4-4439-9a66-aa85c97fa272)

Using Elto increases the number of engaged leads on the phone in a single calling session by an **order of magnitude**. It also integrates seamlessly with your CRM (HubSpot, Salesforce, etc.) and/or SEP ([Apollo.io](http://Apollo.io), Salesloft, Outreach, etc.), so you can import contact lists/sequences/due call tasks and write call recordings, transcriptions, and dispositions back to your platform of choice.

**Want to get started?** [Schedule a time to get set up.](http://calendly.com/elto/elto_get_started)
