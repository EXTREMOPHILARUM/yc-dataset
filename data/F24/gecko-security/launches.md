# Launches

## Gecko Security: AI SAST for finding Vulnerabilities in Code

**TL;DR:** Static analysis tools flood teams with false positives and miss the vulnerabilities that matter. We use LLMs to find the complex business logic flaws that traditional scanners can't detect.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92703&key=user_uploads/1969797/42239d23-2918-4c49-bc6d-38a1955fc1c7)

# **The Problem**

Companies scan their code for security vulnerabilities and are often met with a big pile of findings. 80% of these findings are false positives and not exploitable vulnerabilities. Even among the true positives, these scanners still miss issues like privilege escalation and authentication bypasses. These are the most important issues that only surface later during manual code review or penetration testing.

Security teams have to deal with this by spending hours tuning scanners and rules or hiring headcount to triage through the false positives. This translates into delayed releases, overtime costs, and compliance risks when critical flaws slip through undetected.

# **The Solution**

Traditional SAST (Static Application Security Testing) tools have two fundamental limitations. First, they parse code into simplistic models like ASTs or call graphs, which lose context and can't resolve complex call chains. Second, they rely on pattern matching against predefined rules, which works for basic vulnerabilities like XSS and SQLi but fails completely for custom business logic flaws.

Gecko solves both problems. We built a custom, compiler-accurate indexer that preserves semantic information and allows us to precisely navigate code like an IDE. This gives us the ground truth of how your code actually works.

With that foundation, we use LLMs to perform threat modeling. The LLM analyzes your code's business logic, data flows, and trust boundaries to generate targeted attack scenarios. We then systematically validate each potential attack path, using the indexer to reconstruct full call chains from source to sink and determine real-world exploitability before flagging it as a vulnerability.

This approach finds the complex, multi-step business logic vulnerabilities that have been invisible to traditional tools.

# **Ask**

We've got a handful of Fortune 500 companies and startups alike excited about this, because it addresses key pain points they couldn’t address with traditional scanners. Customers are seeing 50% fewer false positives on the same codebases, and are finding issues using the scanner that would only appear in pentests and manual code reviews.

We’ve used it to find 30+ CVEs in projects like Ollama, Gradio, and Ragflow (<https://www.gecko.security/research>). You can [try it on any OSS repo](https://app.gecko.security) at or [get a demo](https://cal.com/geckosec/30min).

# **Team**

JJ and Artemiy met four years ago while studying in London. Since then, they have traveled the world competing in CTFs and hackathons, earning over $100,000 in prizes.

JJ, CEO and Co-founder, previously worked for the UK Intelligence Service, as a teenager building automated tooling to defend critical infrastructure. He also worked at Binance in China leading security tool development for the Red Team. 

Artemiy, CTO and Co-founder, served in the Austrian Cyberforces and built threat intelligence platforms used by Interpol and national governments. A scholar of Imperial College London, he’s spent his career developing systems that detect and respond to complex cyber threats

## Gecko Security: Your AI Security Engineer

**TL;DR:** We built [Gecko](https://gecko.security/) for teams that want to build secure code quickly without wasting time on tools that don’t deliver results, or relying on one-time human pentests that quickly become outdated.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=84816&key=user_uploads/1969797/81233561-38af-49a4-b7ed-03f61aa03ae0)

### **The Problem**

Most developers tell us they think of security as an afterthought, added out of fear rather than part of the development process at the start. This is because current security tools **can’t find critical business logic vulnerabilities**, which are the ones attackers actually exploit, and instead flag low-priority issues with many **false positives**. This makes fixing these issues slow and costly, **pulling engineers away from building** features that grow revenue.

### **The Solution**

Gecko uses AI to understand how your application should work, simulates relevant attacks to find critical vulnerabilities, and then verifies these vulnerabilities by exploiting them. It also helps you understand the risk of these vulnerabilities and applies a working fix to **continuously** **keep your code secure**. [Watch our demo here!](https://www.youtube.com/watch?v=ObuItEP3rZk)

### **Technical Details**

At a high level, Gecko mimics the approach of skilled security experts by using LLM agents combined with program analysis tools like static analyzers, fuzzers, and symbolic executors, which were previously **only used in intelligence agencies**. For fixing vulnerabilities, Gecko uses multiple agents to iteratively refine the patches - ensuring the vulnerability is remediated, and your code isn’t broken. All testing is done in parallel with certified human pentesters, as we continue to benchmark Gecko’s performance to ensure no vulnerabilities are overlooked.

### **Ask**

**Do you have code that needs to be secured?** Email us at [**gecko@gecko.security**](mailto:gecko@gecko.security) or book a demo at [**https://cal.com/geckosec/15min**](https://cal.com/geckosec/15min).

### **Team**

[JJ](https://www.linkedin.com/in/jeevan-jutla/) and [Artemiy](https://www.linkedin.com/in/artemiy-malyshau/) met four years ago while studying in London. Since then, they have traveled the world competing in CTFs and hackathons, earning over $100,000 in prizes. 

JJ previously worked for the UK Intelligence Service (GCHQ), as a teenager building automated tooling to defend critical infrastructure. He also worked at Binance in China leading security tool development for the Red Team.

Artemiy holds an MSc from Imperial College London, where he was a scholar. He has contributed to research in multi-agent systems and reinforcement learning. As the first employee and only non-PhD member at his previous company, he developed threat intelligence software for Interpol and national governments. 

Both are deeply committed to cybersecurity and AI, and are focused on solving one of the industry's most challenging problems.
