# Launches

## SiLogy: Chip design and verification in the cloud

**TL;DR**: SiLogy is building a platform for chip developers to run tests, track test statistics, and collaborate on debugging.

—

Hey, we’re [Paul](https://linkedin.com/in/paul-kim-7b766262) and [Kay](https://linkedin.com/in/kay-li-84924128b), the cofounders of [SiLogy](https://silogy.io). We’re building chip design and verification tools to speed up the semiconductor development cycle.

## **The Problem**

Interest in designing new chips is growing, thanks to demand from AI and the predicted decline of Moore’s Law. Since the number of possible states grows exponentially with chip complexity, the need for testing in simulation is exploding, with chip developers already spending 70% of their time on testing. (See this video on the [verification gap](https://www.youtube.com/watch?v=rtaaOdGuMCc)).

Tooling hasn’t kept up. The state-of-the-art in collaborative debugging is to walk to a coworker’s desk and point to an error in a log file or waveform file. Each chip company rolls out its own tooling and infra to deal with this—this was Kay’s entire job at his last gig. But they want to work on chips, not devtools! The solutions they come up with are often inadequate and frustrating. That’s why we started SiLogy.

## **The solution**

SiLogy is a web app to manage the entire digital verification workflow. (“Digital verification” means testing the logic of the design and includes everything before the physical design of the chip. It’s the most time-consuming stage in verification.)

We combine three capabilities:

**Test running, results, and statistics**: Our CI tool runs tests in the cloud, allowing engineering teams unlimited flexibility in scaling their test volume. We also track each project’s progress in test coverage and test pass rate.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79226&key=user_uploads/151331/d9a4d2a6-9662-4ee6-8eef-e735b10885b6)

**Killer application-specific features**: We’re building features tailored for verification use cases. We incorporate a test orchestration framework, waveform viewer, coverage report, and other features specifically for verification teams, providing customers an advantage over competitors using a generic CI solution such as Jenkins.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79226&key=user_uploads/151331/d2beb46c-884b-4fec-b731-698c1c0a2312)

**Collaboration**: soon you’ll be able to send a link to and leave a comment on a specific location within a log or waveform file, just like in Google Docs.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79226&key=user_uploads/151331/db8f1954-dafb-4a9e-b739-1b883c4963ac)

## **Asks**

If you have experience with Verilog, even just from college, give our product a try at <https://dash.silogy.io/signup>. Tell your loved ones who work on chip or FPGA design and verification to give us a try as well.

If you have thoughts on the state of verification, get in touch at [paul@silogy.io](mailto:paul@silogy.io). If you or someone you know wants a demo, schedule a meeting with us [here](https://calendly.com/d/5gd-rf6-66h/silogy-product-demo).

Thanks for your support!
