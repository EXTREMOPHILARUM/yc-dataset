# Launches

## Cactus 🌵: Deploy AI models locally on smartphones

# TL;DR

Deploy AI models locally, privately, and offline in any app using Cactus. Cactus is a blazing-fast inference engine optimized for smartphones and comes with React Native, Flutter, and Kotlin bindings.

https://youtu.be/xwKrmYkJZD8

# Our framework:

Cactus is a cross-platform & open-source framework for doing inference on smartphones, wearables, and other low power devices. It supports any LLM or VLM available on HuggingFace directly.

The recently released Google AI Edge and Apple Foundation Frameworks are platform-specific and primarily support specific models from the companies.

To this end, Cactus:

* Is available in Flutter and React-Native for cross-platform developers, since most apps are built with these today.
* Supports any GGUF model you can find on Huggingface; Qwen, Gemma, Llama, DeepSeek, Phi, Mistral, SmolLM, SmolVLM, InternVLM, Jan Nano etc.
* Accommodates from FP32 to as low as 2-bit quantized models, for better

  efficiency and less device strain.
* Have MCP tool-calls to make models performant, truly helpful (set reminder, gallery search, reply messages) and more.
* Fallback to big cloud models for complex, constrained or large-context tasks, ensuring robustness and high availability.

So far, our customers have built:

* Personalised and private RAG and prompt-enhancement pipelines for their app users.
* Offline fallback for the big remote AI models.
* Phone tool use agents like gallery & calendar management.
* AI for medical and other privacy-pertinent industries.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92059&key=user_uploads/1131467/bd9fc810-5239-41b7-90ac-bf6d1686bb3c)

# Some demos:

**LLMs and embedding models**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92059&key=user_uploads/1131467/0f36edcb-6e65-408f-b30b-a920b37a0aa0)

**Real-time vision inference**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92059&key=user_uploads/1131467/24403145-da55-4c01-ad60-8472f49b439d)

Tell us how we can make it great!

Repo: https://github.com/cactus-compute/cactus \
Discord: https://discord.gg/nPGWGxXSwr
