# Launches

## Tusk 🐘 - AI Agent for Generating Unit/Integration Tests

Hey everyone, we’re Sohil and Marcel, the founders of [Tusk](https://usetusk.ai) (YC W24).

Tusk is an AI agent that **generates unit and integration tests** for your PRs.

We’re the team that built the first publicly available AI coding agent in the market. Now we’re focused on taking on the tedious software engineering work that developers dread the most — writing automated tests.

<https://youtu.be/OK_uhIGEQ0Y?feature=shared>

## Problem

It goes without saying that writing tests is important for maintaining high code quality in any engineering organization.

However, any software engineer who has had to hastily meet product deadlines knows that writing unit and integration tests is the first thing to go. Their main priority in this case is to ship the feature as fast as possible.

The problem is that the lack of tests then results in **customers complaining about bugs** in the feature. And all too often the blame is assigned to engineering leadership for not caring enough about quality.

We know how painful this experience is from our previous jobs. We’ve experienced instances of forgone tests leading to embarrassing bugs, including one that ruined a live demo for a high-value pilot customer (who you can guess didn’t convert).

## Solution

We built [Tusk](https://usetusk.ai/) to provide EMs and senior engineers in charge of quality efforts a way to **ship fast while improving code quality**. Our AI agent generates unit and integration tests using your codebase context and business logic.

Tusk functions as a non-blocking PR check that suggests **happy path and edge case tests** that have not been covered by the existing test suite. Our agent shows you which tests have passed or failed and allows you to incorporate the test cases into the PR with one click.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=87010&key=user_uploads/317259/da66276a-94e5-4cf0-8cf7-b9e0e5635fe6)

Engineering teams at companies like DeepLearning.AI, Wyndly, and Afterword use Tusk to prevent bugs while increasing test coverage.

> Tusk is the first AI tool that noticeably accelerated our dev cycle. By scaling our testing infra, it's given us confidence to ship faster and been instrumental in helping our lean team scale across 3 stacks. Of all the AI tools being built right now, I'm most excited about Tusk.

– Zack Moy, Co-Founder & CTO at [Afterword](https://afterword.com/)

> Edge cases that are not covered can cause the most critical issues. By using Tusk, our team gains an additional guardian to protect our product from the threats of edge cases.

– Amo Chen, Senior Backend Engineer at [DeepLearning.AI](http://DeepLearning.AI)

> Our priority as a fast-shipping product team is making sure we get high quality code out the door quickly. Tusk has been instrumental in helping our engineering team increase test coverage with minimal effort.

– Aakash Shah, Founder & CEO at [Wyndly](https://www.wyndly.com/) (YC W21)

## Why Use Tusk

Tusk surpasses other test generation and code review tools in these ways:

**We run the tests we generate**. Tusk runs the tests it generates in an ephemeral sandbox and iterates on its output so you can be confident that its tests are checking for relevant happy path and edge cases. Code review tools do not do this, which results in vague comments that are hard to trust.

**Optimized for test generation quality**. 69% of Tusk-generated test suites are incorporated into customers’ PRs. We use more compute to reason through test scenarios. AI copilots in your IDE are optimized for latency as opposed to quality when generating tests.

**Developer-centric, fully customizable**. Tusk puts engineers in control by allowing them to accept/decline the generated tests and customize configs to meet your team's testing guidelines (how to mock, using factories, avoiding specific directories, etc.).

Read [our documentation](https://docs.usetusk.ai/automated-tests/overview) to learn more.

## Interested?

Tusk is now available for growth-stage and enterprise companies looking to auto-generate tests for their PRs and/or backfill tests for their monolith.

[Apply for access](https://tally.so/r/nP29pQ) to see how Tusk can help your team ship faster but safer.

## 🐘 Tusk - AI coding agent that completes your chores

**tl;dr**: [Tusk](https://usetusk.ai) is an AI coding agent that completes annoying tickets, letting software engineers focus on more important work. Simply assign a ticket to Tusk. Our AI will traverse your codebase for context and then create a pull request (PR).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78780&key=user_uploads/317259/6868cbd5-72a5-495b-b4df-022d6b53d313)

Hey everyone! We’re Sohil and Marcel.

We’re on a mission to boost developer productivity and satisfaction by automating the day-to-day tasks that bog down software engineers.

# Problem

Software engineers are often assigned menial “product quality” tickets and bugs that require them to context-switch from more important, interesting work.

**15-20% of all tickets** in the typical 2-week sprint are chores like fixing bugs and polishing up UI. Additionally, there are similar tickets in every company’s graveyard backlog that rarely ever get cleared.

The result? A simple engineering task that should’ve taken 15 minutes to complete sometimes ends up taking 3 weeks to get done, or not at all.

While it makes sense for engineers to deprioritize these tasks, this work is important for ensuring that customers have a delightful, bug-free user experience. Janky UX on an ongoing basis causes “**death by a thousand cuts**” for customers, leading to churn.

# Solution

[Tusk (YC W24) Demo](https://youtu.be/W0O3p5EIO1I?feature=shared)

[Tusk](https://usetusk.ai/) is an AI coding agent that completes product quality tickets and bug fixes, letting your software engineers focus on more important work.

We integrate with Linear, Jira, Notion, and GitHub so that engineers can **go from ticket to PR** with one click of a button. We’re fully embedded into your engineering workflow so you don’t have to change how you work.

With Tusk, engineers no longer need to context-switch to do something simple like adding a confirmation modal or fixing a page index bug for table pagination.

### How Tusk works

* **Simply assign a ticket to Tusk**. Our AI agent will traverse your codebase for context and create a PR for the ticket.
* **Tusk will** **regenerate code to address PR reviews** left by engineers and errors in automated checks.
* **Tusk investigates complex tasks** and provides a branch and advice to save engineers time even if it can’t create a PR.
* **Beta**: If your team deploys a preview environment for every PR, Tusk will do an end-to-end test of the change and record a testing video.

# Our story

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78780&key=user_uploads/317259/51f7aee6-bf8d-400d-a07f-b09da476bce6)

[Sohil](https://www.linkedin.com/in/sohil-kshirsagar/) was previously a Senior Software Engineer at Aspire. Because of his product-mindedness, he was usually the first engineer to complete product quality tickets. Sohil was also the first person to tell you that **these chores distracted him** from working on more important tasks.

[Marcel](https://www.linkedin.com/in/marcel-tan/) was formerly a Product Manager for 6sense’s AI email product. He often made product decisions that were outside of the initial PRD due to customer feedback. However, he risked distracting his engineers by pulling these ad hoc tickets into the current sprint.

We both deeply wished there was a way to **protect engineers’ uninterrupted coding blocks**, while also raising the quality bar of our products. Today we’re using Tusk to help build our own product.

# Get early access

We’re already helping companies like Wefunder (YC W13), Toolbox (YC S20), and HitPay (YC S21) automate up to 20 engineering tickets monthly.

**Apply to get early access** **to Tusk** **on** [**this form**](https://tally.so/r/w4xOpA). We’ll give the first 50 companies who sign up free customization of your AI agent and a white-glove onboarding.
