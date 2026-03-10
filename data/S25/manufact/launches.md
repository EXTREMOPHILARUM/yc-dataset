# Launches

## Manufact (mcp-use) - Open source infrastructure and dev tools for MCP agents

**TL;DR**

mcp-use is building open-source dev tools and infrastructure for MCP to help dev teams quickly build and deploy custom AI agents with MCP servers.

Our SDK just crossed 100,000 downloads and 4,800 Github stars.

Teams at large enterprises like NVIDIA, NASA and SAP are using us to build internal AI tools.

### **The ask**

Building an agent with or without MCP?

If you're building an AI agent, we'd love to show you how mcp-use can help you develop and deploy your custom agents.

<https://cal.com/mcp-use/30min> or shoot a message to us: +1 (628) 899-2498 or [founders@mcp-use.com](mailto:founders@mcp-use.com)

<https://www.youtube.com/watch?v=rU5eQiZFdlI>

### **Our story**

When MCP and the first use cases came out, we could not believe that such a powerful tech could only be used on IDEs or Claude Desktop.

You can now rebuild any existing AI agent product using just a simple script.

We felt the need to write agents ourselves, in code, in a structured and composable way, and allow other developers to do the same. That’s why we first released the mcp-use[ library](https://github.com/mcp-use/mcp-use).

Now we want to make the development of MCP agents dev-friendly and production-ready for companies.

### **Problem**

An MCP agent is a set of MCP servers + LLM + system prompt.

With mcp-use library you define the MCP servers config, and initialize the MCP client.

Choose the LLM and system prompt and the agent is ready to go.

```
async def main():

    load_dotenv()

    client = MCPClient.from_config_file("browser_mcp.json")

    llm = ChatOpenAI(model="gpt-4o")

    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    async for chunk in agent.astream("Look for job at nvidia for machine learning engineer."):

        print(chunk["messages"], end="", flush=True)
```

This is all great, but when you have to roll out those agents, you don’t want to share local configurations via email or stitch together pieces of code in your existing codebases.

* You want agent logic to be decoupled and testable.
* A single place to manage configs, auth and access control.

What we've built at mcp-use solves both.

### **Demo**

<https://www.youtube.com/watch?v=BbgmUpaQC_s>

### **Concrete Use Cases**

* NASA is using mcp-use to build their internal agent called “MADI”.
* A famous YC company developed an internal incident management agent with multiple MCP servers (Incidents io, Grafana, Slack). However, the rollout is blocked because they need a central place to manage authentication and access control for tools and resources.
* Our customers integrate production-ready AI agents directly into their products, replacing manual processes. We get our hands dirty with them to provide the infra and avoid common pitfalls (e.g., incorrectly wrapping OpenAPI specs).

### **ASK**

Do you know anyone already using MCP servers internally or building products powered by AI agents?

For the first few companies we will personally create/integrate MCP servers you need, have everything running through our platform, either on cloud or your own infrastructure. We even help you integrate our SDK into your code.

What do you think? Can we help you?

Book a call: <https://cal.com/mcp-use/30min>

Shoot a message to us: +1 (628) 899-2498 or [founders@mcp-use.com](mailto:founders@mcp-use.com)
