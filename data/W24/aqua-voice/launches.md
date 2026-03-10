# Launches

## Aqua Voice Desktop: Write clear, well-formatted text using only your voice.

[Aqua Voice Desktop](https://withaqua.com/) lets you create and edit clear, well-formatted text with your voice.

<https://www.youtube.com/watch?v=yFtMQdLwLGA>

Hey, this is Finn from Aqua Voice. I’m excited to show you what we’re building.

> This feels like upgrading voice dictation on my Mac _making it work how it should work_.

The desktop experience is the best way to use Aqua yet. It lets you talk easily into any app and comes with:

\- **Fine-tuning:** can have up to 800 custom words/phrases at a time, no pronunciation tuning required.

\- **Context Awareness:** automatically identifies relevant words and phrases in the active application. This uses system accessibility APIs (not screenshots, like some others) and is heavily processed on device before inference to preserve privacy.

\- **Command recognition:** the system now shows you what it's going to do before it does it. "Deleting…" or "Adding to list…" or "Fixing Spelling…"

![uploaded image](https://www.ycombinator.com/media/?type=post&id=86308&key=user_uploads/1652937/f10f3395-e52f-487a-a34f-10b598444c68)

We've also spent a ton of time getting **better out-of-the-box accuracy.** Our core transcription engine is the most accurate real-time system that we know of. **We scored 3.2% WER on Librispeech clean, significantly better than the next best real-time system we tested (Google) at 5.5%.** We also released a benchmark that tests accuracy & human-friendly formatting which showed that out of the box, Wispr Flow makes 10x as many mistakes as Aqua Voice for emails and technical writing. The full write-up including audio and code is available [here](https://withaqua.com/blog/benchmark-nov-2024).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=86308&key=user_uploads/1652937/9762e173-97c9-46b5-9e2e-e7e8ea073105)

Everyone uses dictation for different reasons - I started in sixth grade (dyslexic) with Dragon Professional and always wanted it to be more than a clunky substitute for the keyboard. Hopefully Aqua Desktop can be that for some of you.

\-Finn

## 🎙️ Aqua Voice - Voice-only text editor

Edit: Check us out on [Hacker News](https://news.ycombinator.com/item?id=39828686) (currently #1)!

**TLDR:** [**Aqua**](https://withaqua.com/) is a voice-native text editor. Imagine dictating to a professional writer who can clean up your phrasing, fill in words, and understand your intent.

🟩 Watch our demo video [here](https://www.youtube.com/watch?v=qwSAKg1YafM):

**🔴 Problem**

Dictation still **sucks**:

* It's not very accurate.
* You have to learn specialized commands.
* Edits require the keyboard.

[**Finnian Brown**](https://linkedin.com/in/finn-brown-3b0b56113) has never been a very good speller (he’s dyslexic) and has been using dictation software since the sixth grade, when his dad got him set up on Dragon Dictation to write papers for school. It's always been easier for him to dictate—despite the janky software.

Dictation has remained surprisingly rigid in the era of LLMs. They make a lot of mistakes (see Siri lmao). All existing dictation services rely on learning a set of specialized commands.

They struggle to distinguish between filler phrases/commentary and stuff you actually want to write down.

**🌎 Aqua**

Aqua innovates on this paradigm by fusing real-time audio and an LLM to understand your intent. It does as much of the writing and formatting as you ask it to.

**Accuracy is King 👑** - Better than Whisper! - we use an MoE transcription architecture to have a lower WER than Whisper-largev3 in real-time.

**Think Don’t Type 🧠** - Aqua can execute arbitrary commands. You don’t need the keyboard. Most people talk **twice as fast** as they can type.

**Make Writing Chill 🏝️** - Aqua reacts naturally to feedback and can recover from mistakes if you tell it to!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79717&key=user_uploads/1653094/f99f4176-5433-45ca-89be-738edeb4746c)

🙏 **Asks**

Try Aqua Voice! No account is needed; just head over to <https://withaqua.com>. If you like it, sign up for $10/month after a 1000-token free trial.
