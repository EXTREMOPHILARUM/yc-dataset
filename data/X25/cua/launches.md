# Launches

## c/ua - Docker Container for Computer-Use Agents

### **📚 TL;DR**

**c/ua** is an open-source framework that enables AI agents to control full operating systems within high-performance, lightweight virtual containers. It delivers up to **97% native CPU speed on Apple Silicon** and works with any language models: [**https://github.com/trycua/cua**](https://github.com/trycua/cua).

<https://youtu.be/Ee9qf-13gho>

### **⚒️ The Problem**

For **Computer-Use AI agents** to be genuinely useful, they must interact with your system's native applications. But giving full access to your host device is **risky** - and not ideal. What if the agent's process gets compromised, or the LLM hallucinates and leaks your data? And practically speaking, do you really want to **give up control** of your entire machine just so the agent can do its job?

**In short: How can AI agents interact with operating systems, desktop applications, and browsers without jeopardizing security or sacrificing performance?**

### **⭐ Solution: An end-to-end framework**

We combined **Apple's Virtualization.Framework** with an agent-friendly interface to create:

\- **Lightweight VMs**: Run at 97% of native CPU speed on Apple Silicon, giving you near-native performance in a secure, virtualized space.

\- **Sandboxed Execution**: AI agents operate in tightly controlled environments, allowing secure interaction with desktop applications - without risking your host system.

\- **LLM-Compatible Runtimes**: Works out-of-the-box with popular LLM providers like OpenAI, Anthropic, and open-source tools like Ollama, LM Studio, and OpenRouter.

And we now support **MCP**! You can use Claude Desktop or Cursor, as your personal assistant to navigate even notoriously challenging apps like Tableau. Watch the demo to see it in action!

[**https://youtu.be/NTUVU1aBs3c**](https://youtu.be/NTUVU1aBs3c)

### **⚙️ How It Works**

**c/ua** brings together three powerful components into one unified framework stack:

1\. **Lume** - Our high-performance Virtualization layer leverages Apple's Virtualization.Framework to spin up macOS or Linux environments.

2\. **Computer-Use Interface (CUI)** - This layer lets any process or AI agent - no matter which framework it's built on (like AutoGen, LangGraph, etc.) - see the screen and interact with Lume VMs just like a human would. It supports actions such as clicking, typing, scrolling, and extracting the visual accessibility tree.

3\. **Computer-Use Agent (CUA)** - Built on top of CUI, this general agent framework runs intelligent workflows within these VMs. It's compatible with popular LLM providers like OpenAI, Anthropic, as well as open-source tools like Ollama, LM Studio, and OpenRouter.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=89628&key=user_uploads/1644303/c3e0e845-3223-4b82-85d1-316e41d9875c)

An AI agent built with **c/ua** operates within a virtual environment to:

\- Navigate and interact with any application's interface

\- Read screen content and perform keyboard/mouse actions

\- Switch between applications and self-debug when needed

\- Operate in a secure sandbox with controlled file access

All of this occurs in a fully isolated environment, ensuring your host system, files, and sensitive data remain completely secure - while you continue using your device without interruption.

### **🖥️ What Can You Build with c/ua?**

**c/ua** lets AI agents use real desktop apps - just like a human. For example:

\- **CAD Copilot**: Modify 3D models in tools like Fusion 360 or FreeCAD.

\- **Photoshop Assistant**: Crop, layer, and export assets via prompt.

\- **Operator for Tableau**: Navigate dashboards and filters with natural language.

\- **Legacy App Automator**: Control apps and websites with no APIs through UI actions.

### **🤝 Our Asks:**

If you're done burning money on fragile browser automations or slow, over-engineered computer-use agents - it's time to try c/ua:

* Book a call: <https://cal.com/francesco-bonacci/cua-demo>
* Email us: [founders@trycua.com](mailto:founders@trycua.com)

Also don’t forget to:

1\. Leave us a star, watch and fork on GitHub: [**https://github.com/trycua/cua**](https://github.com/trycua/cua)

2\. Join our Discord [**https://discord.com/invite/mVnXXpdE85**](https://discord.com/invite/mVnXXpdE85) - we're building this together
