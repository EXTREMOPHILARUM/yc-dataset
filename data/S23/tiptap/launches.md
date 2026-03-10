# Launches

## Bidirectional Markdown Support for Tiptap

Hi everyone, we’re the team behind Tiptap, the open source text editor framework used by thousands of developers to build rich text and AI-powered writing tools.

We just launched **bidirectional Markdown support!** You can now import Markdown into Tiptap and export your editor content back to Markdown, without losing structure or formatting.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94631&key=user_uploads/1335640/a7c2a608-e669-4e56-bf8c-05fdece38c47)

### **The problem**

Markdown is becoming the common language for AI and LLM-based workflows.\
When you feed prompts, train models, or structure outputs, they often rely on Markdown. But most editors don’t handle it well. Converting between Markdown and rich text is lossy, inconsistent, and full of edge cases.

Developers who build AI tools, documentation platforms, or note-taking apps need a way to work _natively_ with Markdown without giving up modern editing experiences.

### **How we’re solving it**

With this release, Tiptap makes Markdown a native format. You can:

* **Parse** Markdown content into Tiptap's ProseMirror-based JSON for editing,
* **Serialize** your Tiptap content back to multiple variants of Markdown,
* **Use it client-side or server-side** via the MarkdownManager,
* **Define custom Markdown** syntax for your custom nodes and marks,

### **How to try it**

1. Install the Markdown package via _@tiptap/markdown_
2. Either setup the _MarkdownManager_ and directly parse and serialize it or import the _Markdown_ extension and extend your editor instance with Markdown features
3. Use the serialized and parsed content in your apps (for example parsing file contents or AI streams)

### **Why this matters**

As AI tools grow, Markdown is quickly becoming the glue between humans and LLMs. Writers, developers, and apps need a format both people and models can read and write.

By making Markdown fully bidirectional, Tiptap bridges that gap, giving developers a foundation to build the next generation of editors, copilots, and AI-native content tools.

### **Call to action**

If you’re building AI products or content tools that use Markdown, try it out and tell us how it fits into your stack.

Docs: https://tiptap.dev/docs/editor/markdown/ 

You can reach us at [humans@tiptap.dev](https://mailto:humans@tiptap.dev) or discuss on [GitHub](https://github.com/ueberdosis/tiptap/discussions)

## Tiptap Pages: Word-style layouts in your editor

Hey everyone! Philip here, Co-founder at [Tiptap](https://tiptap.dev), the open-source text editor framework used by thousands of dev teams to build collaborative and smart editors.\
\
We’ve launched **Tiptap Pages** into live beta, a new extension that adds pagination, page layouts, headers, footers, and structure to your Tiptap editor.

If you’re building anything that looks like a document editor but ends up hacked together in an infinite scroll, this is for you.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94225&key=user_uploads/1335640/3d14271b-bf90-4e24-8d48-800403fdcc21)

### **The Problem**

Most rich text editors treat documents as one long, continuous scroll.

That works for notes. But not for:

* Contracts with signature blocks that must land on the right page
* RFPs and government proposals with strict page counts
* Exams, policies, or legal docs where structure really matters
* PDFs that actually need to look like the document you typed

Adding “real” document behavior (pages, breaks, headers, print formatting) is hard to maintain.

### **What We Built**

Tiptap Pages brings page awareness to your editor.

**Visual page layouts**\
Choose A4, Letter, Legal, or define your own. Layouts reflect actual document dimensions.

**Smart pagination**\
Content flows across pages with clean, logical breaks

**Dynamic headers and footers**\
Insert page numbers, section names, document metadata, and custom elements.

**Custom node support**\
Build and export structured content the way your product needs it, including callouts, exhibits, and embeds.

**Built for developers**\
Extend behavior, apply custom styling, and integrate deeply with your stack.

Pages is now available on **Team** and **Growth** plans.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94225&key=user_uploads/1335640/1a13e116-ecec-40f4-bb07-6c08e0b9005b)

### **See It in Action**

* **Product Overview:** https://tiptap.dev/docs/pages/getting-started/overview
* **Live Demo:** https://feature-pages-extension--tiptap-pro.netlify.app/src/extensions/pages/react/
* **Join our Discord:** https://tiptap.dev/discord

### **Why We Built It**

Docs still matter, especially in verticals like legal, fintech, govtech, insurtech, and education. But those documents don’t live in Word forever. They’re part of the tools you’re building.

Teams using Tiptap were already trying to force structure into an unstructured model. We built Pages to give them something better, not just for writing, but for layout, formatting, and final delivery.

If you’ve ever faked a page break with extra line breaks… you get it.

### **Our Ask**

We’d love feedback from developers building products with structured documents.

* Try the demo and tell us what breaks.
* Share what your team would need next (collaboration? AI? export formats?).
* If you’re in one of the verticals above, let’s chat.

## Tiptap – Better DOCX Import & Export

Hey everyone! Philip here, Co-founder at Tiptap (https://tiptap.dev), the open-source text editor framework used by thousands of dev teams to build collaborative and smart editors.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91336&key=user_uploads/1335640/25fe0263-453c-44eb-a825-c0cdad1aa51a)

Today we’re launching a major upgrade to our DOCX import and export capabilities, including new extensions, new endpoints, smarter formatting handling, and custom node support.

If your product deals with Microsoft Word files in any way, this is for you.

### The Problem

Handling DOCX files in modern web apps is a pain.

* Importing DOCX often breaks formatting or loses structure.
* Exporting to DOCX from custom content structures (like callouts, embeds, or warnings) is clunky or impossible.
* Styling ends up looking like Word, not your app.
* Most solutions are heavy, hard to control, or require running backend services yourself.

This matters if you’re building anything with rich text and need interoperability with Word, from internal tools and documentation platforms to knowledge bases, legal tech, and publishing tools.

### What We Built

We rebuilt our DOCX pipeline, including both import and export, from the ground up with developers in mind.

**DOCX Import Endpoint**:\
Easily parse Word docs and convert them to Tiptap-compatible JSON.

**DOCX Export Extension**:\
Create DOCX files directly from your editor content.

**Better formatting**: \
More accurate handling of nested lists, tables, and mixed styles.

**Custom node support**: \
Map your own content blocks (like warnings or embeds) to standard DOCX elements.

**Style control**: \
Match exported DOCX files to your product’s fonts, colors, and spacing.

**Flexible execution**: \
Run it in the frontend for full control or in the backend for performance.

We also now support image uploading from DOCX into your own storage.

### Why We Built It

We kept seeing developers often had to work around Word support using custom scripts or third-party tools that weren't compatible with custom content models.

Tiptap already powers many text editors, so DOCX support needed to be customizable and ready for production.

→ Product Website: [https://tiptap.dev/product/conversion](https://tiptap.dev/product/conversion)

→ Developer Docs: [https://tiptap.dev/docs/conversion/getting-started/overview](https://tiptap.dev/docs/conversion/getting-started/overview)

→ Questions: [humans@tiptap.dev](mailto:humans@tiptap.dev)

## Tiptap – AI infrastructure for text editors

Hey everyone! Philip here, Co-founder at Tiptap (https://tiptap.dev), the open-source text editor framework used by thousands of dev teams to build collaborative and smart editors.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=91010&key=user_uploads/1335640/7f4a081f-e73b-446c-bd13-8bf62848a9a9)

Today, we’re launching the **Tiptap AI Agent,** a developer-first way to add an AI agent that edits documents on your user's behalf, right inside your product. With this tool, you can add a Cursor-like assistant inside your text editor with a few lines of code.

## The problem

Adding AI to a text editor seems easy! Just call an API, right?

But in reality, you end up rebuilding everything: prompt handling, context extraction, streaming, undo/redo, multiplayer state sync, UX for AI changes… It’s a lot of work just to get to something usable.

And it only gets harder when you want to use your custom LLM, tools, and backend..

## **What we built**

The Tiptap AI Agent gives you all of this out of the box:

* An AI assistant that can read and edit rich text based on user-defined tasks
* Optional AI review flow (accept/reject changes)
* Works with Tiptap Cloud or your customLLM, tools and RAG pipelines
* Fully compatible with Tiptap’s multiplayer, comments, and change tracking

Go from “idea” to “AI in production” in minutes, not weeks.

## **Why we built it**

We started building this after seeing the same request from users over and over:

> How do I add AI beyond simple text commands to my Tiptap editor?

So we turned our existing AI features into a full-fledged AI Agent toolkit that anyone can use, no matter what model or backend they prefer.

**Live demo:** https://ai-agent.tiptap.dev/\
**Demo video:** https://youtu.be/w3ocdyi5qps\
**Docs:** https://tiptap.dev/docs/content-ai/capabilities/agent/overview

## Our ask

Try the demo and plug it into your editor. If you’re building something cool, we’d love to hear from you.

We’re also happy to answer technical questions and receive feedback. Join our [Discord community](https://tiptap.dev/discord), or email us at [humans@tiptap.dev](mailto:humans@tiptap.dev).

Thanks for building with us!\
The Tiptap Team

## Tiptap 3.0 Beta: The Next-Gen Open Source Editor

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90091&key=user_uploads/1335640/ecc226df-3a58-45cc-aa81-2af38457fc1a)

**Hey everyone! Philip here, Co-founder at Tiptap (**[**https://tiptap.dev**](https://tiptap.dev)**).**

We're launching **Tiptap 3.0 Beta**, the next major version of our open-source text editor framework for web developers.

**The Problem:** Building custom, reliable, and performant text editors from scratch is painful. Developers spend countless hours struggling with edge cases, extensibility, and maintaining compatibility! Time better spent building core features.

**Our Solution:** Tiptap version 2 already provides a flexible, unopinionated, extension-based editor framework. But with Tiptap 3.0, we've focused heavily on removing even more friction:

* **Full TypeScript integration:** Strongly typed APIs for fewer bugs.
* **Server-side compatible:** Manipulate content server-side without the need for a DOM.
* **JSX support:** Write custom nodes using a familiar React/Vue-style syntax.
* **Simplified dependencies:** Consolidated popular extensions (like TableKit) to streamline your workflow.
* **Interactive marks:** React and Vue markviews to easily add rich, interactive elements.
* **Static renderer:** Render your editor content to HTML, Markdown, or even React components, anywhere.

**Why Tiptap?** We initially built Tiptap to solve our own frustrations with text editors. Four years, 30k GitHub stars, and a large open-source community later, we’ve learned a lot and incorporated that directly into Tiptap 3.0.

**Give Tiptap 3.0 Beta a try:**

* What's new in 3.0: <https://next.tiptap.dev/docs/resources/whats-new>
* Documentation: <https://next.tiptap.dev/docs/editor/getting-started/overview>
* GitHub: <https://github.com/ueberdosis/tiptap/tree/next>

**Our ask:** We'd love your feedback! If you're building something cool with Tiptap, or have feature requests and ideas, please reach out directly at [founders@tiptap.dev](mailto:founders@tiptap.dev) or reply here.

Thanks for building with us!\
The Tiptap Team

## Tiptap – Editor UI Components and Templates

**Hey everyone 👋 We’re the team behind Tiptap**

We just launched **Tiptap UI Components** — a free library of React components and templates to help developers build rich text editor UIs faster, without starting from scratch.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89529&key=user_uploads/1335640/b6e5aed3-1527-46c8-b4d7-9be817a44f16)

Tiptap itself is a headless editor framework used by thousands of developers to power text editing across their apps. The headless approach gives full flexibility, but it also means you're on your own when it comes to building the UI.

That’s the problem we’re solving here: many teams don’t have time to design and build all the editor UI pieces (toolbars, menus, upload buttons, etc.) every time they want to add a new editor to their product.

**So we built a solution that gives you a head start:**

* A growing set of handcrafted, MIT-licensed React components
* A CLI to scaffold your setup in seconds
* A live editor template you can use out of the box or customize as needed

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89529&key=user_uploads/1335640/76cac74a-0b69-4fa2-81af-e18f3cdbd803)

Everything is fully optional and customizable. You can add just one component to your existing editor, or build your entire UI with the kit. And Tiptap remains headless at the core — these components sit on top and stay out of your way.

**Backstory:** We originally built Tiptap as a tool for ourselves, and it has grown far beyond that. We’ve seen it used in everything from CRMs and email builders to collaborative docs and CMS platforms. But we also saw devs rebuilding the same UI patterns over and over. So we asked: what if we made that part easier, too?

**Demo template:** <https://template.tiptap.dev/simple>\
**GitHub repo:** <https://github.com/ueberdosis/tiptap-ui-components>\
**Docs + Components Overview:** <https://tiptap.dev/docs/ui-components/getting-started/overview>\
**CLI:** npx @tiptap/cli init

We’re already working on more components, including some integrated with Tiptap Cloud (e.g. comments, version history).

**Ask:**

* Try out the components and tell us what you'd like to see next
* Upvote our Product Hunt launch if you like what we’re building
* Feedback, issues, and PRs are always welcome

Feel free to DM us here or reach out at [founders@tiptap.dev](mailto:founders@tiptap.dev)

Thanks for building with us!\
The Tiptap Team

## ⚫️ Tiptap – The developer toolkit for building collaborative apps

[Tiptap](https://tiptap.dev) is a suite of open source content editing and real-time collaboration tools for developers building apps like Notion or Google Docs. It’s used by thousands of businesses worldwide, including GitLab, Axios, and Substack.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72947&key=user_uploads/1335640/87be68c6-2dfb-47a7-a6c3-90e012aa554b)

🤔 **The Problem**

Extensive content editing interfaces and real-time collaboration are a key feature of most apps to deliver value to their users, such as Notion, Miro, Figma, and Google Docs.

While the users of these apps expect a best-in-class editing and collaboration experience, it's super painful and complex to develop. As developers, we can testify to this: Entire IT departments despair of these tasks.

💡 **The Solution**

With Tiptap Editor, you can build apps like Notion in no time. The headless approach gives you complete freedom to build your editor experience the way you want. Tiptap Editor comes with a ton of powerful extensions to help you elevate your app beyond the ordinary. Better yet, Tiptap Editor is free and open-source.

Thanks to Tiptap's cloud services, you can easily add more sophisticated features like collaborative editing, real-time sync, or soon AI editor capabilities to your app in less than a minute. Tiptap's cloud services are available for fast-growing startups and as an on-premises solution for enterprises.

🚀 **Who is it for?**

Tiptap is for developers and product teams who need to integrate rich text editors into their apps, especially those who value customization, ease of use, and real-time collaboration. Tiptap toolkits and cloud services significantly reduce development time, enabling faster time-to-market and increased profitability for product teams.

Tiptap is already used by **thousands of businesses worldwide,** including:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72947&key=user_uploads/1335640/619e8a25-0b5c-4174-89f0-4a4084091375)

With over 1.8 million npm downloads per month, Tiptap is one of the top 5 most popular editor frameworks in the world and is strongly supported by a huge developer community:

* **26k+ community members**
* **20k+ GitHub stars**
* **1\.8k forks**
* **5k+ commits**
* **200+ contributors**

🎉 **Meet the Tiptap team**

We're six co-founders with over a decade of digital consultancy experience, transforming our struggle with building custom editor interfaces into a solution. Since launching Tiptap in 2019, we've been dedicated to scaling up and fully committed since 2022. As passionate designers and developers, we're proud to craft Tiptap's core ourselves.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72947&key=user_uploads/1335640/c49d9774-dae5-4aea-8721-650108864024)

❤️ **Our ask**

We invite you to explore Tiptap's capabilities in your app, contribute to its open source development, and join our welcoming community.

* Star our GitHub repository: [**https://github.com/ueberdosis/tiptap**](https://github.com/ueberdosis/tiptap)
* Follow us on Twitter: [**https://twitter.com/tiptap_editor**](https://twitter.com/tiptap_editor)
* and on LinkedIn: [**https://www.linkedin.com/company/tiptapdev/**](https://www.linkedin.com/company/tiptapdev/)

If you have any questions, or would like to use Tiptap in your app, write us at [**humans@tiptap.dev**](mailto:humans@tiptap.dev)

Yours\
 Nick, Patrick, Philip, Sebastian, Sven and Timo
