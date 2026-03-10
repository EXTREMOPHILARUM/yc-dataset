# Launches

## Golf:  Open-source platform for shipping production MCP servers

Hi YC,

We’re Wojciech and Antoni -  high school friends who’ve been building together since we were 14. We're incredibly bullish on a future where AI agents have their own internet through which they access our services - so much so that we dropped out of university to build Golf.

**Golf lets you ship a production-ready MCP server without worrying about the plumbing.** You just write the tools, prompts, and resources you want agents to call. Golf handles everything else - routing, auth, telemetry, error reporting, and deployment. Then you can observe and manage it through our gateway.

https://youtu.be/u9ar4w2uE7E

# **The problem**

Over the past few weeks, we spoke with over 40 teams building MCP servers. Everyone hit the same walls: wiring up authentication, figuring out how to trace agent calls, setting up working transports, and debugging behavior in production. The MCP spec doesn’t cover these parts. Teams told us it takes **2-4 weeks** to get that to production.

# **What we built**

**GolfMCP** is an open-source framework that gives you a clear, file-based structure to define what your agent can call. No decorators, no spec knowledge, no boilerplate - just write your logic.

**Golf Gateway** is the hosted layer that runs and observes your server. golf deploy gives you a live server in under 60 seconds, with real-time traces, tool usage, and error monitoring built in.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90569&key=user_uploads/1366358/b035bdc4-02c2-42d5-a230-ad38be34dfa9)

# **Early traction**

We’re already running Golf in production with companies, and we’ve got more landing this week. 

**CTAs**\
If you are looking to ship server for your company, schedule a demo of our platform here: https://golf.dev\
Also we’d love to get your feedback, and we’re happy to help teams get to production faster. Reach us at [founders@golf.dev](mailto:founders@golf.dev)
