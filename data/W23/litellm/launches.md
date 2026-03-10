# Launches

## 🚅 LiteLLM - Call all LLM APIs using the OpenAI format [Llama2, Anthropic, Huggingface, etc.]

Hello, I’m Ishaan - one of the maintainers of [LiteLLM.](https://github.com/BerriAI/litellm/)

**TLDR; LiteLLM let’s you call all LLM APIs (Azure, Anthropic, Replicate, etc.) using the OpenAI format. We translate the inputs, standardize exceptions, and guarantee consistent outputs for completion() and embedding() calls**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74316&key=user_uploads/1083928/3b30d01e-433a-48e1-9a58-10a34913d45d)

### **Problem ❌: Multiple LLM APIs - Hard to debug**

Calling LLM APIs involved **multiple \~100 line if/else statements** which made our **debugging problems explode.**

I remember when we added Azure and Cohere to our chatbot. Azure’s API calls would fail so we implemented model fallbacks - (e.g. if Azure fails, try Cohere then OpenAI etc.). However, provider-specific logic meant our code became increasingly complex and hard to debug.

# **Solution 💡**

# 1️⃣ Simplify calling existing LLM APIs

That’s when we decided to abstract our LLM calls behind a [single package - LiteLLM.](https://github.com/BerriAI/litellm) We needed I/O that just worked, so we could spend time improving other parts of our system (error-handling/model-fallback logic, etc.).

[LiteLLM](https://github.com/BerriAI/litellm) does 3 things really well:

* **Consistent I/O:** It removes the need for multiple if/else statements.
* **Reliable**: Extensively tested with 50+ cases and used in our production environment.
* **Observable**: Integrations with Sentry, Posthog, Helicone, etc.

### 2️⃣ Easily add new LLM APIS - [LiteLLM UI](https://docs.litellm.ai/docs/debugging/hosted_debugging)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74316&key=user_uploads/1083928/8624880b-20dc-4f39-8b40-1537c91a5380)

The next big challenge was adding new LLM APIs. Each addition involved 3 changes:

* Update list of available models users can call from
* Adding key to our secret manager / .env file
* Mapping the model name - e.g. `replicate/llama2-chat-...` to a user-facing alias `llama2`.

Since LiteLLM integrates with every LLM API - we provide all of this out of the box with zero configuration. With a single environment variable - `LITELLM_EMAIL` you can automatically add 100+ new LLM API integrations into your production server, **without modifying code / redeploying changes 👉** [LiteLLM UI](https://docs.litellm.ai/docs/debugging/hosted_debugging)

## Ask 👀:

* Adding new LLM providers? Contact us at [krrish@berri.ai](mailto:krrish@berri.ai) if you need help!
* ⭐️ us on [GitHub](https://github.com/BerriAI/litellm) to keep up with releases and news.
* Join [our Discord](https://discord.com/invite/wuPM9dRgDw)!
