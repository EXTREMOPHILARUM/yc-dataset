# Launches

## Mem0 - Open Source Memory Layer for AI Apps

**TL;DR**

[Mem0](https://mem0.ai) is an open-source memory layer for AI applications. It solves the problem of stateless LLMs by efficiently storing and retrieving user interactions, enabling personalized AI experiences that improve over time. Our hybrid datastore architecture combines graph, vector, and key-value stores to make AI apps personalized and cost-efficient. Watch our explainer video [here](https://youtu.be/Rg3_Mpr3Kcs).

—

Hey everyone! We're Taranjeet and Deshraj, and we built [Mem0](https://github.com/mem0ai/mem0) to solve a big problem we faced with LLMs while building Embedchain (an open-source RAG framework with 2M+ downloads). LLMs don’t have memory, so they forget everything after each session. This leads to inefficient and repetitive interactions, making it hard to create personalized AI experiences. Think about having to repeat your preferences over and over again, and how frustrating that gets! Mem0 changes that.

❌ **The Problem**

LLMs are stateless—they don’t remember anything between sessions. Every time you interact with them, you have to provide the same context, which gets repetitive and wastes computational resources. This makes AI apps less useful and personalized over time.

✨ **Our Solution**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83896&key=user_uploads/661173/ed531d50-421e-4d2f-a361-088587c27198)

Mem0 adds a **memory layer** to AI applications, making them stateful which allows them to store and recall user interactions, preferences, and relevant context. This way, AI apps evolve with every interaction, delivering more personalized and relevant responses without needing large context blocks in each prompt.

To make this possible, we needed to create a system that could efficiently manage and retrieve all the relevant information AI apps collect over time. That’s where Mem0’s **hybrid datastore architecture** comes in, making AI smarter and more efficient as it learns.

⚙️ **How it works**

[Mem0](https://mem0.ai) employs a hybrid datastore architecture that combines graph, vector, and key-value stores to store and manage memories effectively. Here’s the breakdown:

* **Adding memories:** When you use Mem0 with your AI App, it automatically detects and stores the important parts of your messages or interactions.
* **Organizing information:** Mem0 categorizes memories in three ways:
  * **Key-value stores** for quick access to structured data (facts, preferences).
  * **Graph stores** for understanding relationships (like people, places, objects).
  * **Vector stores** for capturing the overall meaning and context of conversations, allowing AI apps to find similar memories later.
* **Retrieving memories:** When an input query is received, Mem0 searches for and retrieves relevant memories using a combination of graph traversal techniques, vector similarity, and key-value lookups. It prioritizes the most important, relevant, and recent information, ensuring that the AI has the right context, no matter how much memory is stored.

Watch this video for a demo of our playground in action [here](https://youtu.be/VtRuBCTZL1o)

🙏 **Our Asks**

* Try out [Mem0](https://mem0.ai)! We guarantee that your users will have personalized interactions after adding Mem0 in your AI apps. Moreover, you will save on your LLM costs.
* If you are looking for a memory provider for your AI app and want to schedule a demo, please feel free to block some time on [my calendar](https://cal.com/taranjeetio/mem0) or email me at [taranjeet@mem0.ai](mailto:taranjeet@mem0.ai)
* Checkout our platform and open-source offering and give feedback:
  * Platform: <https://app.mem0.ai/playground>
  * GitHub: <https://github.com/mem0ai/mem0>
