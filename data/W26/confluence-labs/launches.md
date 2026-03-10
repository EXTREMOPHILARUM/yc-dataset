# Launches

## Confluence Labs: an AI research lab focused on learning efficiency

Confluence Labs is coming out of stealth with **SOTA on ARC-AGI-2** with a score of **97.9%** at $11.77 per task on the public eval. This is how we did it, why it matters, and what's next.

ARC-AGI-2 is a benchmark that tests an AI system's ability to solve novel reasoning tasks from just a few examples. It's considered one of the hardest AI benchmarks in the world. As recently as a year ago, even the best models scored in the single digits.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98111&key=user_uploads/1164255/2f4e4c89-6f96-48ca-93ea-a84eccc15092)

We've open sourced our SOTA solver. You can reproduce our results here: <https://github.com/confluence-labs/arc-agi-2>.

**Our Approach – Program Synthesis driven by LLMs**

LLMs are exceedingly good at writing code. We take the latest models and allow them to find the optimal solution by directing them to write code which describes the transformation represented by a particular ARC problem.

The principles of our approach can be boiled down to a few key ideas:

1\. Structure the problem such that it optimally resembles the underlying LLM's training data

2\. Enable long-horizon work on the problem so a model can continue to build on its past work

3\. Precisely structure the criteria of the solution and give the model a way to measure that

**ARC-AGI-2 is Saturated – What Does This Mean for the World?**

ARC is a data efficiency benchmark. It measures how well you can make a prediction based on a few examples. Typical approaches to ARC-AGI have struggled because modern ML excels in areas where you can collect a lot of training data, but struggles in areas where data is sparse or costly to attain.

We think LLMs can be used in combination with discrete modeling to assist humans in data-sparse domains. We're most excited about the application of this to meaningful and challenging frontiers such as hardware engineering, drug design, and physics research.

**What Does This Mean for Us?**

Our core belief is that learning efficiency is the key bottleneck to solving the world's hardest problems. We think AI can help in data-sparse domains, and we're approaching this from 2 angles:

1\. **Hypothesis generation** – A hypothesis is a testable prediction about the world. If you optimally generate hypotheses, the results of your experiments are maximally informative, and you can reduce the time it takes to develop a new technology or solve a hard problem.

2\. **Data-Efficient Modeling** – By pushing the capabilities of both LLMs and discrete program search, we can make predictions with far less data and accelerate frontier research.

**What's Next?**

We're going hard on developing our core technology, building out the team, and developing partnerships with researchers and engineers. We're looking for collaborators in hardware engineering, biology, materials science, and other fields where progress is gated by the cost of physical experiments. If that sounds like you or someone you know, reach out at [founders@confluence.sh](mailto:founders@confluence.sh).
