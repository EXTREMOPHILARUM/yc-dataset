# Launches

## Million Lint – Grammarly for performance

Hey YC! I’m [Aiden](https://twitter.com/aidenybai), founder of [Million](https://million.dev/) — we’re building a tool that helps fix slow React code. Here is a quick demo: [ ](https://www.youtube.com/watch?v=k-5jWgpRqlQ&ab_channel=AidenBai)

Fixing web performance issues is hard. Every developer knows this experience: we insert console.log everywhere and catch some promising leads, but nothing happens before "time runs out." Eventually, the slow/buggy code never gets fixed, problems pile up on a backlog, and our end users are hurt.

We started Million to fix this. A VSCode extension that identifies slow code and suggests fixes (like Grammarly, for performance!) The website is here: <https://million.dev/blog/lint> 

I realized this was a problem when I tried to write an optimizing compiler for React in high school (src: <https://github.com/aidenybai/million>). It garnered a lot of interest (14K+ stars) and usage, but it didn't solve all user problems.

Traditionally, devtools either hinge on full static analysis OR runtime profiling. We found success in a mixture of the two with dynamic analysis. During compilation, we inject instrumentation where it's necessary.

From there, the runtime collects this info and feeds it back into VSCode. This is a great experience! Instead of switching around windows and trying to interpret flamegraphs, you can just see it inline with your code.

We are still in the very early days of experimentation! Million Lints focuses on solving unnecessary re-renders right now and will move on to handling slow-downs arising from the React ecosystem: state managers, animations, bundle sizes, waterfalls, etc. Our eventual goal is to create a toolchain that keeps your whole web infrastructure fast, automatically - frontend to backend.

In the next few weeks, we're planning to open source (MIT) the Million Lint compiler and the VSCode extension. 

To earn a living, we will charge a subscription model for customized linting. We believe this aligns our incentives with yours: we only make money when we make your app faster.

We'd love to know your thoughts – happy to answer :)
