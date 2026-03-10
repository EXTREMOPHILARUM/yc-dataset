# Launches

## Benchify: Instant self-healing codegen

### **TL;DR**

Benchify handles the middle mile of codegen ensuring that generated code just works and is instantly executable. It’s a one-line SDK call between LLM clients and sandboxes to deliver instant code repair, accelerated bundling, and observability.

### **Who**

Anyone depending on non-human-in-the-loop codegen: – app builders, dynamic websites, agents, etc.

### **Problem**

Generated code breaks — constantly.

On top of normal bugs like duplicate function calls, parse errors, or missing or extra parens, AI systems introduce new ones, such as stray tool calls, /\* rest of code goes here \*/, and malformed diff applications. Running that code inside sandboxes only compounds the pain: every piece has to be perfect for execution to succeed, and the sandbox boot time delays the inevitable. Since all the sandboxes are just firecracker VMs designed to run anything, they’re not optimized for the common workflows builders actually care about. The result is slow setup, fragile execution, and painful feedback loops.

* **Missed errors**: Users hit error screens as soon as code loads in the browser. 
* **Delayed generations**: LLM-based auto-healing stretches generation times, slowing iteration.\
  **Token burn**: Edge-case failures trigger endless retries that chew through tokens without progress.  Often bugs are inherently out-of-distribution and thus hard to fix with AI.
* **Setup lag**: Sandboxes take 30-120s to boot before code even runs, adding cold-boot lag to the rep-cycle when there’s an error.
* **Lost data:** Sandboxes don’t easily track errors and the errors or only show the first (breaking) bug, making it hard to detect all the errors in code at once to push improvements 
* **Templates:** The use of templates speeds up sandboxes but leads to even more brittleness as the template has to be in perfect lockstep with the codegen.

 

### **Solution**

Benchify combines **non-AI techniques** (static analysis + program synthesis) with **highly optimized infrastructure** to deliver _turn-key code_ — fixed and bundled — in O(1 second).

It drops in as a **one-line SDK call** between your LLM client and the sandbox. If you’re only doing front-end work, you can skip the sandbox entirely and render directly from Benchify’s bundled output.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94193&key=user_uploads/1661832/dcd85900-d61c-47e4-b71e-0ef6244e5fd0)

**Code Repair**: Sub second fixes for parsing, dependency, CSS/Tailwind, type, and interaction errors (e.g. empty-Select) with more on the way. If there’s an issue you’re running into, let us know and we can add a fix!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94193&key=user_uploads/1661832/5d3a354c-69ee-4f5c-8437-0d0360f28874)

**Bundling**: Build and dependency resolution in 1-3s.

* _Front-end_: Returns code that instantly renders on client via our SDK.
* _Full-stack_: Bundles code that executes in any sandbox (skipping slow dependency & build steps) — the only delay left is sandbox cold boot.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=94193&key=user_uploads/1661832/10606bbc-8df4-43f8-a574-aa9f0bd97d26)

**Observability**: Analytics on error patterns in generated code.

**Product Demo** 

https://youtu.be/my7yzpp8AqY

### **How it works**

Benchify’s analysis engine detects bugs and dispatches them to a growing library of static repair strategies in a fraction of a second. Strategies are optimized for different bug types, and layered using an incremental parsing approach, since sometimes fixing one bug unlocks others.  Each candidate fix is re-analyzed, with the best one selected automatically provided it yields a strict improvement in the code.  The architecture builds on prior research in _program synthesis_ and _program repair_, where the idea is to have a collection of strategies that may or may not work at fixing different bug types, combined with an analysis and execution engine that can efficiently determine whether or not a strategy succeeded.

### **Story**

We entered YC with a formal-methods-driven code review product. But unreliable LLM-generated test harnesses kept breaking it. Talking with builders made it clear: **the real bottleneck was brittle codegen itself.** We pivoted to focus entirely on making generated code self-healing.

### **Ask**

We’re focused on app builders today, but our core tech generalizes: agents, self-updating sites, programmatic ads, and more.

If generated code is slowing you down, let’s talk.

## Benchify: Automatic code reviews that work

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83014&key=user_uploads/1661832/cb65a61c-fa84-4ccf-a1d5-2f6bf33b88fa)

# TL;DR

[Benchify](https://www.benchify.com/) is a code review tool that uncovers real bugs by actually running your code on strategically generated inputs, using methods typically restricted to rocket science and chip design.  When errors are found, Benchify provides verified bugs, unit tests, and a patch (coming soon).

# The problem

Engineers (like you) spend almost half their time testing and debugging, which, let’s be honest, they’d rather spend doing literally anything else.

* **Lower velocity:** Projects are delayed by testing & debugging
* **Site outages:** Despite all the effort, critical errors slip through, leading to site outages and other failures
* **Low test coverage:** Developing exhaustive tests is nearly impossible and generally put off for later…
* **Shallow test depth:** Testing is limited to a few hard-coded cases

# The solution

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83014&key=user_uploads/1661832/ed5d818b-cba4-41cf-9ca7-f9b9ca419737)

We test your code using _magic_ (ok, formal methods) and deliver the results in an actionable comment on your PR.

* **Automatic logical blueprint:** Benchify automatically writes a blueprint that says how your code is intended to function
* **Run thousands of tests:** Benchify tests your code against the blueprint using thousands of strategically generated inputs
* **Provide counterexamples:** Concrete, minimal counterexamples are provided when code fails so you can easily debug
* **Generate unit tests:** We automatically translate counterexamples into unit tests for easy reproducibility and test-driven development
* **Propose solutions:** When Benchify detects an error, it attempts to propose a solution, which it subjects to the same battery of tests as the original code

## Does it work?

The testing techniques Benchify uses are typically leveraged for mission critical use cases, such as silicon chip design, rocket engineering, and high-speed trading. Our secret sauce is in making these techniques usable and actionable. 

# The Team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83014&key=user_uploads/1661832/09a8c140-f845-4f96-9113-6daac4963be2)

Max and Juan first met as bright-eyed freshmen at Dartmouth College almost a decade ago and have been fast friends and on-and-off roommates since.  They’re deeply passionate about software assurance (who isn’t?) and excited to test your code.

* [**Max**](https://www.linkedin.com/in/max-von-hippel-3b90742a8/) holds a PhD in Computer Science from Northeastern University, focused on security and interactive theorem proving. He has worked at NASA, the DoD 😉, and Galois. Most importantly, he holds a Blue Belt from 10th Planet Jiu Jitsu. 
* [**Juan**](https://www.linkedin.com/in/juan-castano97/) built and sold a business, helped companies like Instawork and Klaviyo grow, and advised on deals at McKinsey. Juan double-majored in Economics and survival skills at Dartmouth (okay, the second one isn’t official), and later picked up an MBA from MIT, where he unfortunately missed out on a chance to test his skills with the [pirate certificate](https://physicaleducationandwellness.mit.edu/about/pirate-certificate/).

# Asks

* Hop on a [call](https://calendly.com/d/cpyy-ffc-ynf/juan-max-30-min) with us to try out Benchify or talk about your frustrations with software testing
* [Try out](http://www.benchify.com) our beta code reviewer and give us feedback
* Shoot us an email at [hello@benchify.com](mailto:hello@benchify.com) with your biggest backend software testing pain points, and we’ll see if we can help out!
