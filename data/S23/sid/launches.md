# Launches

## SID.ai – AI research lab for retrieval

**Intelligence needs Context**

AI is giving humanity a new computer: one that can learn, reason, and act. But intelligence and skills are inconsequential without context. _Context imposes the upper bound._ At SID, we're training models to provide this context. _To connect intelligence to the world._

**Context needs Retrieval**

To provide the right context, you need to find it first: Humanity has known how to do search on the internet for a while. But great search over everything else has been elusive so far. We think _we have an angle to solve it once and for all_. [SID-1](https://www.sid.ai/research/sid-1), our first agentic retrieval model, doubles embedding-only accuracy and outperforms frontier models on the most complex retrieval tasks.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72952&key=user_uploads/1134710/cd8dc357-3db7-4db0-9476-265e176bb6bb)

**SID-1**

_SID-1 is our first model for agentic retrieval: 1.8x more likely to surface the right results than embedding-only search across general knowledge, finance, science, legal, and email. It is more accurate than agentic retrieval based on Gemini 3 Pro, Sonnet 4.5, and GPT-5.1 at its highest compute setting, while being 24x faster (144 vs 5.7 seconds)._

Traditional retrieval pipelines pre-program each step: query rewriting, searching, reranking. SID-1 retrieves like a human would: it searches, reads results, and refines its queries, taking as many steps as needed. We trained SID-1 on questions that take human researchers over an hour to solve.

SID-1 is drop-in compatible with existing retrieval systems. It is designed to work as a subagent with larger LLMs like GPT-5 or Sonnet. Teams running embedding-only retrieval or RAG can typically integrate it in an afternoon.

Step-change improvements in retrieval create new winners. Claude Code was better at finding the right file, unlocking larger code bases and driving massive adoption for Anthropic. Open Evidence made retrieving over medical research easier and took doctors by storm. Looking back further, relational was better than hierarchical for databases, creating Oracle. Better web search created Google. [_We're working closely with a small group of companies who want that edge now for their domains._](https://tally.so/r/gDDVMd)

Given we're compute-limited, we're rolling SID-1 out slowly. We're offering SID-1 through our API, AWS Bedrock, and as a self-hosted model. _If you're interested in SID-1, please sign up to our [waitlist](https://tally.so/r/gDDVMd), follow us on [X](https://x.com/SID_AI), or read the [technical report](https://www.sid.ai/research/sid-1-technical-report) for more details._
