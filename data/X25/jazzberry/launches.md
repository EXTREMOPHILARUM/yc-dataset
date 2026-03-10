# Launches

## Jazzberry - AI bug finding with real code execution

Hello everyone, 

We’re Mateo and Marco, and we're excited to introduce Jazzberry, an AI agent for finding bugs. Jazzberry is powered by running your code in a secure sandbox and integrates directly into your pull request workflow on GitHub.

**Try it here →** <https://jazzberry.ai>

<https://www.youtube.com/watch?v=L6ZTu86qK8U>

**Why we built Jazzberry**

AI code generation has dramatically increased the amount of code that is written without the tools for bug finding keeping up, leading to a world with more buggy code that is hindering developers. To improve bug finding, we’ve created an AI agent with the ability to run snippets of your code. We're not just flagging potential issues based on code patterns; we're observing the real behavior of your software. Here’s how it works.

1. When you create a pull request, Jazzberry gets to work.
2. Your repository is cloned into a microVM.
3. Our agent examines the contents of the pull request to guide its search. It can write and execute code in the microVM as it looks for bugs.
4. Jazzberry returns a clear markdown table directly as a comment.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90047&key=user_uploads/2557020/31d75b00-abc3-4a60-8ef5-b3a685edfcd5)

**Real Bugs, Real Impact**

We've already seen Jazzberry make a tangible difference for our early users. So far, Jazzberry has…

* successfully identified a SQL injection vulnerability
* discovered a critical logical error in API key validation
* [found an incorrect page navigation](https://blog.openint.dev/how-we-scale-prs/) (see below, we are formerly known as Prophet)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90047&key=user_uploads/2557020/864328cf-c4b9-4b9a-b267-e9059a158f32)

**Who we are**

We have been friends for over a decade, and are coming together to create Jazzberry. Marco completed his MS at the University of Stellenbosch specializing in LLMs for automated test suite generation. Mateo completed his PhD at the University of Colorado Boulder with a research focus on reinforcement learning and formal methods.

**Our Ask**

* **Try it out** – Jazzberry is available now with a free trial at <https://jazzberry.ai>.
* **Contact us** – We’d love to hear your feedback and what bugs Jazzberry helps you catch. Reach us at [founders@jazzberry.ai](mailto:founders@jazzberry.ai).
