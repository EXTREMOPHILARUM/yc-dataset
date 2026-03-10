# Launches

## 🧠 Codeball – AI Code Review

Hey fellow builders!

I'd like to show you something we recently built at Sturdy (W21).

[**Codeball**](https://codeball.ai/) **is a code review AI which approves safe Pull Requests that a human would have approved.** We _hate_ waiting for reviews.

This started off as scratching our own itch in answering "How predictable are programmers?" Very predictable, turned out to be the answer.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64214&key=user_uploads/586182/2a1fd4ab-7a26-4a54-a9cd-a7ccc394aaed)

## **🧠 How**

Codeball is trained on over 1M Pull Requests, so it has seen tons of failure (shitty code) and success (decent code) patterns, making it really good at telling the difference.

You can play with it at [codeball.ai](https://codeball.ai) where you can do "historical" tests on GitHub repos to see what Codeball would have done.

Using AI for mundane reviews saves a bunch of time, but the part that's really cool is that once you stop rubber stamping every single PR, you pay more attention to the tricky ones.

## **👉 Getting started**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64214&key=user_uploads/586182/956431aa-6b25-45dc-b343-fb9905cced54)

You can add Codeball to your repository as a [GitHub Action](https://github.com/sturdy-dev/codeball-action/) (takes like 2 minutes).

_Try for free!_

## **💻 What are developers saying?**

Codeball is currently used by over 100 open-source repositories, including HUGE communities like gogs, kratos, and emqx!

“This is incredible, don’t forget to charge us!” – CEO

“I love it, developers are now trying to ‘cheat’ the system by creating smaller PRs, just like I’ve been telling them to!” – Senior Software Engineer

Also a bunch more in the [Hacker News thread](https://news.ycombinator.com/item?id=31533180) that made front page recently.
