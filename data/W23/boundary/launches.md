# Launches

## Gloo: Empower LLM’s with domain-specific knowledge

**tl;dr** LLMs are awesome, but they have no knowledge about your data, and when you give it to them, they’re prone to make stuff up. We help developers build a searchable knowledgebase that LLMs can understand, and validate their responses are legit.

Hey everyone! We’re Aaron and Vaibhav from Gloo and we’re on a mission to help LLMs understand your data and get them to stop hallucinating all over the place.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70071&key=user_uploads/855521/fefa49cf-6a22-4913-ac9e-da9550da9e69)

### **The problem**

Building a knowledge graph isn’t as easy as calling OpenAI embeddings API, storing them in a VectorDB and calling it a day. Developers have to choose from a myriad of parameters like chunking algorithm, embedding type (even based on the content), vectorDB, whether to fine-tune or not, how to securely store the data — and the list goes on and on.

Once you feed everything into the LLM, you’re only halfway there, as getting rid of hallucinations is tricky, and confidently incorrect answers to customer questions will give you headaches in the long-term.

On top of that, you still have your actual customer problems to still fix: getting the customer data, building flows on top of the LLM, writing the right prompts, getting more customers.

### **The solution**

Gloo is the managed solution to building your knowledge graph — built for LLM context-windows from the ground-up. **We stand up a search API for your data that supports both keyword and semantic search**, and we smartly index and compute embeddings for you based on the content type. Once that’s setup, you can call our **_Check-_GPT API to check LLM answers** against your knowledgebase to ensure trustworthiness.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70071&key=user_uploads/855521/4c3b7bd2-6924-427b-a1f6-6aa194ae500f)

We built our search with a security-first approach. Your data is always server-side encrypted, and never actually stored in 3rd party Vector DBs. We are also supporting new transformations search engines couldn’t do before, like generating document summaries (powered by LLMs!), so you don’t have to spend precious time computing this at query time.

All of your data is viewable in your own personal dashboard where you can track embedding jobs, play around with different search parameters, and search query performance and analytics.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70071&key=user_uploads/855521/3e191b7a-73b1-4b36-983c-8852002a646e)

### **Asks**

Reach out to us at **founders@gloo.chat**

* If your AI keeps making shit up ☠️
* If you want your LLM to stop saying “Sorry I dont know 😵‍💫”
* If you’re worried about data security and VectorDBs / LLMs 🔒
