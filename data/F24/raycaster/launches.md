# Launches

## Raycaster - Cursor for regulatory documents in drug development

Hey YC 👋 I’m Levi, founder of Raycaster.

### TL;DR

* Raycaster is **Devin/Cursor, but for life sciences documents instead of code.**
* It does **project-level drafting** across hundreds of PDFs, Word, Excel, and PowerPoints - not just “write a file from scratch.”
* We’re starting with **drug development docs** (clinical, CMC, regulatory, quality) where delays and mistakes are insanely expensive.

**Video (1 min):** [link](https://youtu.be/FhpC9dyBUF4)

---

### The problem (in plain English)

In drug development, everything important lives in documents:

* protocols, reports, validation plans
* batch records, specs, methods
* Module 3, labels, responses to regulators

They’re scattered across SharePoint, Veeva, email, vendor portals, etc. When something changes - dose, batch size, impurity limit - you’re supposed to update _dozens_ of dependent docs so nothing contradicts anything else.

Today that means:

* **Research:** hunting across PDFs, Word, Excel, PowerPoints and public guidances for the right paragraph or table
* **Draft:** copy-pasting into new docs and hand-editing boilerplate that “mostly” matches
* **Edit:** reviewers tracking changes by eye and leaving 200 comments per document
* **Version control:** folders called `FINAL_v7_REALLY_FINAL_clean(2).docx` and hoping nobody sends the wrong one to the agency

This happens across _every_ stage of drug development - nonclinical → clinical → CMC → labeling. When documents drift, you get delay letters, extra review cycles, or a straight-up rejection. It’s one of the big reasons timelines slip.

ChatGPT / Copilot can draft a single file. They don’t understand a **cross-document project** with real regulatory consequences.

---

### What we built

Raycaster is an **AI workspace for document projects**, starting with regulatory and CMC work.

Think of a repo, but for your dossiers:

* A **workspace** that holds your source docs (guidances, prior submissions, lab reports, CoAs, batch records…).
* A graph of how they depend on each other (this spec feeds this batch record feeds this Module 3 section, etc.).
* An AI agent that can **research, draft, edit, and reconcile** across all of them—with citations and review controls.

Concretely:

1. **Research, with real citations**\
   Ask: “What does EMA say about a 5× batch size increase?” or “Which CoAs support these new commercial lots?”\
   Raycaster reads mixed formats (PDF, DOCX, XLSX, PPTX), pulls out the relevant paragraphs/tables, and shows you the answer with pinned citations back to the exact page and cell.

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=95955&key=user_uploads/299659/18f9f9a3-3ea8-49c7-b50f-17df326e526e)

2. **Project-level drafting**\
   Instead of “write me a cover letter,” you say “update the batch formula + cover letter + justification for the 5× scale-up.”\
   Raycaster drafts the actual Word docs in your workspace, using the research + your templates, and wires in all the cross-references.

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=95955&key=user_uploads/299659/a80d77f1-fbde-429f-b80d-30153df19a1e)

3. **Structured editing**\
   Editing is usually harder than drafting: “bump the batch size everywhere, but don’t touch the control batch,” “update only the EMA version,” etc.\
   Raycaster does **diff-aware edits**: it proposes precise changes inline, shows red/green diffs, and explains _why_ each change was made.

   ![uploaded image](https://www.ycombinator.com/media/?type=post&id=95955&key=user_uploads/299659/4b1ab418-fbe1-4517-a157-f54b076a9ca5)

4. **Version control + remote agents**\
   Every change is tracked like a commit. You see: who asked for it, what files were touched, what the diff was, and what sources were used.\
   You can let Raycaster run “in the background” on a workflow (e.g. keep Module 3 in sync with new CoAs), then come in as a human reviewer to approve or tweak before anything is finalized.

All of this lives in a collaborative, access-controlled workspace, so legal/reg affairs/IT don’t freak out.

---

### Why this is technically interesting

For devs: this is all the fun of agents and tooling, but on **documents instead of code**:

* Retrieval over **huge, messy, mixed-format corpora** (PDF/DOCX/XLSX/PPTX, scanned tables)
* A maintained **dependency graph** of citations and document links, so the agent can do impact analysis instead of one-off Q&A
* A diff engine that understands “regulatory text” and tables (git diff , not just lines of code
* Multi-agent workflows with strict evaluation + human checkpoints, because “just let the model commit” is not an option when the FDA is on the other side

---

### Why we’re doing this

I started Raycaster after seeing the same pattern over and over: the science was fine; **the documents were the bottleneck.** Teams were shipping “AI pilots,” but the real work was still people copying text between PDFs and Word.

We think documents deserve the same treatment code got:\
**good tooling, real version control, and smart agents that understand context.**

---

### Ask

We’re opening prioritized access for:

* **Biopharma, med-tech, and device companies** with heavy document work (regulatory, CMC, clinical, quality, safety) on major submissions or post-approval changes.
* **Engineers / researchers** who care about serious agentic systems on messy document workflows and want to kick the tires or collaborate on evals/benchmarks.

If that’s you (or someone you know):

👉 Email [**founders@raycaster.ai**](mailto:levi@raycaster.ai) with the subject **“YC Pilot”** and 2-3 sentences about your team + doc stack, or just ping me at [**raycaster.ai**](http://raycaster.ai).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95955&key=user_uploads/299659/474ffc8a-305f-4986-ba5e-b236cf06dd90)
