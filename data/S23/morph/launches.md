# Launches

## WarpGrep v2: Code Search Subagent -> #1 on SWE-Bench Pro

### WarpGrep v2 is a fast code search subagent that works via parallel tool calls. Runs up to 36 grep/read tool calls in under 5s.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98329&key=user_uploads/405977/ba17c624-92ca-4502-8c56-00c22e31ad4e)

### SWE-Bench Pro: WarpGrep v2

#### Scores

* Opus 4.6 → 55.4
* GPT-5.3 Codex → 56.0
* MiniMax 2.5 → 55.4
* Opus 4.6 + WarpGrep → **57.5** (**+2.1**)
* Codex 5.3 + WarpGrep → **59.1 (+3.1)**
* MiniMax 2.5 + WarpGrep → **57.6** (**+3.7**)

#### Efficiency

Tokens:

* Input tokens: **\~17% less** (Opus, Codex, MiniMax, etc..)
* Output tokens: **13% less** (fewer turns)

Turns (MiniMax):

* Avg turns per task: **157 → 135**

Runtime (Opus):

* Opus 4.6: **518s**
* Opus 4.6 + WarpGrep: **545s**
* **178s saved** (**12% faster**)

Cost (Opus):

* Opus 4.6: **$3.06**
* Opus 4.6 + WarpGrep: **$2.51**
* **$0.55 saved** (**15.6% cheaper**)

#### TLDR

WarpGrep v2 raises SWE-Bench Pro scores (**+2.1 Opus**, **+3.7 MiniMax**) while using **\~17% fewer input tokens**, **13% fewer turns**, running **12% faster**, and costing **15.6% less**. The median WarpGrep codebase search takes 5s end to end compared to 75s for the Claude Code Explore subagent

On normal usage on production repos these numbers improve across the board \~40% faster

\
install it in your favorite coding agent here <https://www.morphllm.com/mcp>

or integrate it into your product here <https://docs.morphllm.com/sdk/components/warp-grep/tool>

## WarpGrep: A 20x faster subagent to grep for code

**Problem**\
Coding agents don’t feel fast because they aren’t.

In our benchmarks, agents spend **60%+ of their time searching for the right code**, not generating any. They why they do more than you want, and break developer flow.

The bottleneck isn’t “agent intelligence.”\
It’s **speed, context retrieval** and the **irrelevant code** that gets shoved into the prompt.

Most agent stacks today are basically **sequential grep pipelines**:

1. Ask the model where to look
2. Call a tool
3. Read output
4. Repeat 10–20x

It’s slow, noisy, and compounds latency every step.

WarpGrep is built to do that dirty job correctly and fast.

**Our Insight**

\*\*We value human attention.\*\*\
You can’t build responsive coding agents until retrieval is treated as its own learning and inference optimization problem.\
We optimized for a simple goal: keep both the developer and the agent inside the sub-10-second “flow window.” Anything slower and usage collapses.

**What we built**\
WarpGrep is an RL-trained retrieval model designed specifically to be used as a tool by a coding agent. It operates under a strict budget:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95846&key=user_uploads/405977/cbc2f17d-1ff9-4d7c-bfa1-38d3d36b3ac7)

* Up to eight parallel tool calls per turn (grep, glob, file read, semantic search)
* A reward function that only cares about two things: did it fetch the correct files and did it hit the correct line ranges.

WarpGrep is an expert at deciding what to grep, and what context is relevant for the task. That’s it. This combination reduces context rot by more than fifty percent in production and eliminates the “forty irrelevant files in your prompt” failure mode.

**Performance**\
SWE-Grep runs at around 650 tokens per second on Cerebras.\
WarpGrep hits around 900 tokens per second on B200.\
\
We worked closely with NVIDIA to optimize WarpGrep. CUDA gives us the stability and customization ability to push non-standard inference workloads for parallel search.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95846&key=user_uploads/405977/8e04cd3d-9646-4f25-a0f6-96d2a440471b)

**RL Training**\
RL for MOEs is notoriously inefficient, so we built infrastructure to eliminate dead time:

* Dedicated inference and training GPU pools, continuous rollout streaming to the trainer
* Controlled policy staleness without collapsing effective sample size
* Partial rollout interruption so slow sequences don’t stall sync
* In-flight weight updates so vLLM workers ingest new weights mid-generation with only millisecond pauses

Those optimizations delivered a 1.6 to 2.35 times training throughput boost with essentially no sample efficiency loss.

**Why this matters**\
Every company building coding agents is running into the same wall.\
Once your agent touches a large codebase, retrieval dominates latency and derails reasoning.\
You solve it by giving the agent a retrieval system that behaves like a specialist, not a bottleneck.

If you want an agent that actually performs on large codebases, doesn’t have crippling context rot, and stays within real-time latency, reach out!

https://docs.morphllm.com/api-reference/endpoint/mcp

https://docs.morphllm.com/sdk/components/warp-grep

## Morph: The "other models" you need to build coding agents like Cursor

**TLDR: Morph: the “other models” you need to build the best coding agents like Cursor and Windsurf.**

**Retrieve and rerank code, stuff context, and apply edits to files FAST. Relevant context, fast applies, every time.**

**Morph Apply:** The fastest way to apply updates from Claude, GPT-4o, and others into any file - codebases, docs, etc - 5000+ tok/sec

[Try API for Free →](https://morphllm.com/dashboard)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90352&key=user_uploads/405977/887a632b-bd61-4ace-9af5-d6abc166c319)

> Benchmarked on a 9,000 token file, \~2 seconds

# **The Problem**

There’s no good way to apply edits that models want to make into files. Outputting the full file again is slow and expensive. Diff/Patch edits are brittle and a poor product experience.

In a production setting, AI agents need to update thousands of files. What about when you have a 50k token docx to update? Or when you need to be world-class at retrieving relevant info from a 500+ file repo?

# **Solution:**

Morph is the foundational infrastructure for AI Coding Agents that **_work and feel amazing_** _-_ not a quick demo.

**~~Tired~~**~~: Chunked RAG and having Claude re-output full files~~

**Wired**: Syntax-aware embeddings, reranking, and Fast Apply models = the perfect product experience

**Cursor and Windsurf _roughly_ do this:**

1. For a query, search for top-k relevant embeddings.
2. Re-rank the corresponding content with a re-ranking model → stuff prompt using Claude/Gemini tool calls
3. Use Claude/Gemini to generate small, focused changes
4. Use a Fast Apply model to apply those changes back to the original file

**We provide:**

**Morph Apply**: _Fast Apply_ model: Merge updates from GPT-4o, Claude, and others into your files in under 2s (5000+ toks/second) \
**Morph Embeddings:** Syntax-aware embeddings, built for code

**Morph Reranking:** Rerank functions/classes or file snippets to stuff your context with only the relevant context - every time.

[Try it Now →](https://morphllm.com/dashboard)

**Morph SDK:** Intelligently watch for file changes + smarter embeddings.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90352&key=user_uploads/405977/20ff3242-a426-4ec3-8c62-4e8633a5cc74)

> Morph Fast Apply dropped errors by 8x vs. patch-based edits in our internal IDE and worked on our largest files - **Staff Eng @ Fortune-50**

If you’re building the Cursor for \__\_, or building agents that modify code:

Email us: [info@morphllm.com](mailto:info@morphllm.com)

[Grab a Time Here](https://calendar.app.google/PW4nayCdGanN9iEKA)\
Get Started for Free: https://morphllm.com

[Self Host Morph](https://morphllm.com/blog/self-hosting)
