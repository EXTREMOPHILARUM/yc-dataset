# Launches

## Slack Huddles API by Recall.ai

Hey everyone!

We just launched an API that lets developers programmatically access Slack Huddles data, making it possible to build apps that capture, analyze, and integrate Slack Huddles conversations.

**Why we built this**

Slack Huddles are great for quick discussions, but they don’t provide a way to retrieve transcripts, recordings, or speaker data. Once a huddle ends, the conversation is gone.

**What developers can build with the Slack Huddle API**

With a single API call, you can:

* Retrieve transcripts, recordings, and speaker timelines from Slack Huddles
* Automate workflows for incident management, support escalations, and team handoffs
* Integrate Slack Huddles data into CRMs, analytics platforms, and knowledge bases
* Build AI-powered tools for summarization, insights, or search on top of huddle data

**Get access**

Check out the [Slack Huddles API documentation](https://docs.recall.ai/docs/slack-huddle-bots-overview) and get started [here](https://www.recall.ai/get-started).

<https://youtu.be/EWjJqO0wL4g>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=88317&key=user_uploads/316225/0c06a860-4f67-4669-98c0-3786623228ce)

## Recall.ai Desktop Recording SDK: Access real-time meeting data without bots 🚫🤖

<https://youtu.be/stsH9jv715g>

Today, we’re excited to introduce the [Recall.ai](https://www.recall.ai) **Desktop Recording SDK**. Built to simplify meeting data integration, this SDK allows you to get the recording, transcript and metadata directly within your desktop app — without the need for bots. Integrates with Electron applications in under 5 minutes to provide live data from platforms like Zoom, Google Meet, and Microsoft Teams.

### **Why we built this**

Many industries have strict compliance requirements that limit the use of bots, and sometimes bots may make people uncomfortable. 

To address this, we developed an SDK that provides direct access to live meeting data, letting you build features that leverage this data, such as:

* Lightweight note-taking
* Speech coaching
* Telehealth appointment recorders
* Financial advisor calls
* Real-time sales coaching

### **Get started**

Check out the Desktop Recording SDK documentation [here](https://docs.recall.ai/docs/desktop-sdk-beta) for setup instructions and more details on how to get started.

Let us know your thoughts — we’re eager to hear how the Desktop Recording SDK fits into your app and your use cases.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85723&key=user_uploads/316225/d873ac6f-9125-4204-9293-7dbd0cfcfb7b)

## Recall.ai: Output Media API - AI agents that talk in meetings 🤖

TLDR - [Recall.ai](https://www.recall.ai)’s Output Media API lets you build AI agents that join video conferences on Zoom, Meet, Teams, and Webex. These agents can output audio and video, listen, and respond like real participants. 

<https://youtu.be/YzzzqPpL47o>

Today, we're excited to introduce the Output Media API. With this API, you can easily build live, interactive AI agents that can listen and react to meetings in real time. 

### 📈 The Problem and Solution

For developers, building AI agents have become much easier with APIs like the [OpenAI realtime API](https://openai.com/index/introducing-the-realtime-api/). The difficult part is actually getting your AI agent into a video conference. This is because there are no APIs to send and receive low-latency video streams from Zoom, MS Teams, Google Meet etc.

The solution is to use a service like [Recall.ai](https://www.recall.ai) which provides an API to create virtual participants that can join video conferences, receive the real-time data from the conference, and display the agent as a participant in the meeting. 

### 🤖 AI Agents as a Web App

The Output Media API works by rendering any web app into ultra-low-latency audio and video, and streaming that into your video conference through a bot.

This functionality makes it possible to develop AI agents that listen to the meeting audio and react in real-time, in just a few steps:

1. Develop a webpage that listens to and reacts to audio coming from the microphone (e.g. via [getUserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia))
   * [Recall.ai](http://Recall.ai) sends the mixed audio of the meeting to the webpage microphone so your agent can listen to what’s being said
2. Send a [Recall.ai](http://Recall.ai) bot to a meeting and configure it to show the webpage you developed

```
// POST /api/v1/bot/
{
  "meeting_url": "https://us02web.zoom.us/j/1234567890",
  "bot_name": "Recall.ai Notetaker",
  "output_media": {
    "camera": {
      "kind": "webpage",
      "config": {
        "url": "https://{YOUR_WEBPAGE_URL}"
      }
    }
  }
}
```

### 🚀 Getting Started:

* Check out our [Output Media Guide](https://docs.recall.ai/docs/stream-media).
* We’ve built 2 sample apps using Output Media, with walkthroughs of how they’re built.
  * 💻 [Voice Agent Demo](https://github.com/recallai/voice-agent-demo) lets the bot have a conversation with meeting participants, using OpenAI’s [realtime API](https://openai.com/index/introducing-the-realtime-api/).
  * 💻 [Real-time Translator](https://github.com/recallai/real-time-translator-demo) displays live meeting translations on screen for a spoken conversation.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85172&key=user_uploads/316225/39433a6c-c885-402b-922f-5d477117fde6)

## Recall.ai — The universal API for meeting bots

Hey all!

We’re building [Recall.ai](https://www.recall.ai), a single API for you to get meeting data from Zoom, Google Meet, Microsoft Teams, Slack, and more.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=75617&key=user_uploads/316225/e4c4cc37-13fb-493d-900f-fb8124655197)

The data you receive includes:

* Video recording
* Audio recording
* Transcription
* Participant names
* When people spoke in the meeting
* When people joined/left the meeting
* When people turned their cameras on/off in the meeting
* What device someone is joining from
* …and 10+ more pieces of meeting data.

🎥 [**Click to watch our 2 min demo**](https://www.loom.com/share/60a7500d2a8c40c3b05a88dca376107e)

## The Problem

* Building robust meeting bots takes 1000s of engineering hours.
* Running the infrastructure is a big operational burden, and complicates your architecture.
* Companies like Gong have a team of 5 engineers dedicated to running this infrastructure to be stable and scalable.
* People are building hacky workarounds like bots that screen-record Zoom in a web browser, but this breaks frequently.
* Some meeting platforms (eg. Google Meet, Slack) don’t even have APIs.

## The Solution

We provide 1 simple API that abstracts over differences between meeting platforms (even for platforms that don’t have an API). We run, monitor, and scale the complex real-time video infrastructure - so you can focus on building your core product.

This allows our customers to get into production in a week instead of a year.

## Use Cases

We work with 150+ companies today that ingest meeting data, like Grain, Apollo.io, BrightHire, Fellow, and more. Some examples of products our customers are building with Recall:

* Meeting productivity tools
* Sales conversation intelligence tools
* Interview intelligence tools
* User research tools
* Customer success tools
* Financial advisor tools
* Virtual deposition tools
* Meeting translation tools
* Video editing tools
* Edtech tools

## Can I try it?

Yes! We’d love to have you try [Recall.ai](https://www.recall.ai). Feel free to book a demo [here](https://recallai.typeform.com/to/z2CoFKjj).
