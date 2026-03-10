# Launches

## Salus - Runtime guardrails that validate AI agent actions before they execute

### **TL;DR:**

**Salus is an API that wraps around your agent and checks its actions at runtime, blocking incorrect ones and providing immediate feedback to guide retries.**

We’re Kevin and Vedant, former roommates at Stanford who studied CS, now building Salus full-time.

### 😔**The problem:** 

Your agent processed a refund without looking up the order, costing you thousands. It emailed your top lead using hallucinated data, ruining the deal. You only found out three hours later from a support ticket or an angry email.

Evals, output scoring, and observability are all necessary—but all reactive. They can reduce the likelihood of these problems occurring, but there's no solution that inspects an action as it’s about to execute. Salus does that.

**Ask:** If you are deploying agents and want to improve their correctness we’d love to help. Book a demo [here](https://calendly.com/d/cycy-fbc-fyj/salus-demo), and we can onboard you immediately with just a pip install and a few lines of code.

### 💻 **Our Solution:** 

<https://youtu.be/uyl5NJTY5Cg>

**How Salus validates an action:**

1. Actions must be **grounded in evidence**: Salus maintains an evidence cache for each run that every proposed action is validated against. Evidence includes all outputs from prior tool calls and the entire conversation history.
2. It must **adhere to policy**: Write constraints in YAML, markdown, or plain English. Salus compiles them into runtime checks that are version-controlled, diffable, and shadow-testable
3. And **more**: PII detection, budget/loop protection, idempotency, human-in-the-loop escalation, content moderation

**Self-repairing:** When Salus blocks an action, the agent receives structured feedback to guide a retry. In our benchmarks, **58%** of blocked actions recover and complete the task correctly.

### 📊 **Benchmarks:** 

We tested Salus on τ²-bench and ODCV-Bench. On τ²-bench, agents with Salus follow policies more reliably, at up to **60% lower cost**. On ODCV-Bench, Salus **reduced misalignment by 52%** on average across 12 frontier models (see below).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97574&key=user_uploads/1940292/e48b27f6-2e13-4d40-a9a4-13135ff981bc)

### ➕ **Other Features:** 

While we believe the missing piece is runtime validation, we know **evals and observability** are crucial. That’s why we incorporate all three in **one centralized product**. Using templates and LLMs, we generate thousands of both adversarial and realistic evals that have full context of your agent’s domain.

Contact us: [founders@usesalus.ai](https://founders@usesalus.ai)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97574&key=user_uploads/1940292/cc3d0be7-941f-46ef-be8f-1294b9148073)
