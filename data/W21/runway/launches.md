# Launches

## 📲 ⏪ Mobile Rollbacks by Runway

## Mobile Rollbacks ensure your team is always just one click away from addressing critical bugs in production. 

No one is immune from shipping critical bugs to production. No matter how extensive your test coverage, no matter how thorough your QA, no matter how much you put behind feature flags — your mobile team _will_ ship irreversibly-bad updates that break things and upset your users. 

This is especially problematic for mobile because you can’t roll back immediately like your web or backend friends can. Rather, you have to triage the issue and assign it to the right team members, implement fixes (or carefully revert the offending changes), compile one or more RCs, upload to the stores, submit for review, then cross your fingers and pray to the store review gods for a speedy review. And the negative impacts of even just a few hours with a critically broken app can be eye-watering: tens or hundreds of thousands of dollars in lost revenue, a flood of negative user reviews, and overwhelmed CX or ops folks.   

But what if it didn’t have to be that way? What if you could instantly resolve a critical issue in prod, with a single click? Now, you can. 

### Recover from production issues in zero time — literally

Critical issue? Roll back instantly. In the background of every normal release cycle, Runway automatically re-signs your last live production build and preps it for a possible rollback release — including preemptive submission for review (iOS only) — to remove all possible sources of delay. Should something go wrong in prod, there’s always a corresponding rollback build ready and waiting for single-click release in Runway. 

![](https://assets-global.website-files.com/5ef1f28e08458502ba614d85/6555b0344379d5700b526a01_deploy-rollback-button.png)

Here’s how the rollback flow works in a bit more detail:

1. Your team is busy getting your next regularly-scheduled release out the door. Let’s call it version 1.2.0.
2. In the background, Runway takes your latest live build in production — say, 1.1.0 — and re-signs it, bumping the version to 1.2.1 and incrementing the build number as necessary.
3. Your team releases 1.2.0 as scheduled. Nice!
4. The 1.2.1 rollback release is surfaced in Runway, just in case. For iOS, we also preemptively create a new version for the possible rollback in App Store Connect and submit the rollback build for review.
5. Your team is monitoring the rollout of 1.2.0 and identifies a critical issue 🚨You halt the rollout.
6. Right next to the button you used to halt the rollout, there’s another button to release the rollback build that’s ready and waiting. Click that, and you’re all set.

With rollback builds primed and ready to go, your team can address critical bugs in prod with a single click — cutting out all the lead time needed to investigate and implement a fix, get builds compiled and uploaded, and make it through the store review process.

### Take the pressure out of hotfixes; triage more fully and fix more confidently

Even if you ship a rollback to address an issue in prod, it doesn’t mean you’ll necessarily wait until your next regularly-scheduled release to issue a fix. In fact, it’s likely you’ll use rollbacks in conjunction with roll-forward hotfixes — and those hotfixes will be better as a result. Because rollbacks allow you to instantly stabilize a critical situation, you can take your time in triaging, investigating, implementing fixes, and then working through your hotfix release process.

![](https://assets-global.website-files.com/5ef1f28e08458502ba614d85/6555b0ce132292bf3747a1af_rolllout-rollbacks-final.gif)

### More predictable resolution timelines & fewer unanswerable questions from stakeholders

Every team knows the feeling of dread that hits when you’ve shipped a breaking change and leadership shows up in your #mobile Slack channel. _Is the fix in yet? Is the build approved by Apple? How about now?_ With rollbacks in Runway, you can actually respond to these kinds of asks, and give stakeholders confidence that the situation is under control.

![](https://assets-global.website-files.com/5ef1f28e08458502ba614d85/6555b15743d1af6cfd9dcf50_slack-popup.png)

### When you need a rollback, it’s there for you (batteries included). When you don’t, we’ll handle all the cleanup.

Runway’s rollbacks functionality encompasses quite a few dependencies and steps which, if approximated manually each and every release, would require a lot of work — not just to prepare each rollback, but also to clean up unused rollbacks along the way. Now, you no longer have to choose between investing huge amounts of time and effort into setting up rollbacks manually or else forfeiting the safety net rollbacks provide.

![](https://assets-global.website-files.com/5ef1f28e08458502ba614d85/6555b18d930993fe03666aaa_rollback-settings.png)

With rollbacks, Runway gives your mobile team _the quickest_ possible way to respond to critical issues in production. Instead of scrambling to identify, implement, and ship a fix, you can immediately “stem the bleeding” and resolve things with a single click. Stakeholders won’t hover wondering when a resolution will land, and your team can triage and implement fixes more confidently, without all the pressure that typically accompanies hotfix situations. Plus, rollbacks mitigate the serious negative impact to revenue and app store reviews that comes with a buggy app being in users’ hands for even just a couple of hours.

### How to give Rollbacks a try

You can sign up for free on the [Runway site](http://runway.team), no credit card required, and we’re always available to give you a guided walkthrough — just get in touch!

## 📲 🚀 Build Distro by Runway

## Build Distro makes it dead simple to get the right app builds into the right teammates’ hands

Mobile build distribution is hard. There’s the provisioning and signing gauntlet, of course, but the challenges don’t end there. Getting the right builds in front of the right teammates takes constant effort and shepherding, and creating an install flow that’s pain-free is difficult. Existing tooling options tend to jumble all different kinds of builds together and offer half-baked installation flows; the “human factors” aspect of build distribution is secondary, or ignored altogether.

We set about building a better, more foolproof and human-centric way.

### What is Build Distro?

Build Distro allows you to clearly define and group the different types of mobile builds your team distributes – from one-offs and work-in-progress dev builds, to staging builds, to release candidates. You can avoid the usual jumbled pile of builds that folks have to carefully sift through, and give technical and non-technical team members alike an easier way to grab builds, with streamlined installation via QR or Slack link. With hassle-free distribution, your team can check out builds earlier and more often, improving collaboration and app quality.

Here are some highlights:

📲 **Get the right builds into the right people’s hands**

Build Distro introduces the idea of build buckets to allow you to clearly define and group different flavors of builds. Instead of having all distributed builds landing in that jumbled pile, you can now separate different kinds of builds using definitions based on branch, CI workflow, or some combination of both — or using more freeform, ad hoc buckets. Not only are build flavors logically separated into buckets, but you can set up targeted notifications and scope access per bucket to ensure the right people are aware of and able to seamlessly install new builds relevant to them.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71808&key=user_uploads/562880/830900f0-fe8a-4c8e-b050-5b86956de7d5)

**✨ Share one-offs & early test builds more easily**

With branch-based and ad hoc, personal build buckets, Runway makes it much easier to share work-in-progress builds. You can create dedicated buckets for test builds and nightlies on your main development branch or any feature branches, and everyone on your team can also have their own personal buckets to drop updates into as they work. Product managers, QA, designers, and other engineers and stakeholders can now easily grab any WIP builds, earlier and more often during the development cycle, helping your mobile org improve quality and shift left.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71808&key=user_uploads/562880/e0e69e93-f6bd-4497-a3ed-7d50a23c68df)

🔒 **Make it impossible to ship the wrong build to prod**

One of the worst failure modes around build distribution has to do with test or staging builds getting accidentally shipped to production. It may be rare, but when it happens, it can be devastating. Confusion around distributed build flavors is often to blame, and Runway’s build buckets remove this risk. Clearly delineate prod and pre-prod builds, and scope access accordingly.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71808&key=user_uploads/562880/5c3d452c-2760-44b9-98c6-eb3b97edef2d)

**📥 Install app builds with less hassle, and more context**

Even once someone has tracked down a build they want to check out, actually getting it onto their device comes with its own hassles. Runway makes installation foolproof and seamless: with each build, you can install directly by scanning a QR code or sending yourself a link in Slack. Plus, alongside each build you can see full context on the build flavor and exactly what work it contains — no more guesswork, pinging build numbers back and forth and hoping you’re grabbing the right version of the app.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71808&key=user_uploads/562880/a26f0045-ebdb-4b8b-9048-82f90457d415)

⚙️ **Integrate with your existing tools for zero extra overhead**

Getting up and running is simple: connect your existing CI and… that’s it. Once you’re connected, Runway will get you started with a few default shared buckets for development and RC builds, and anyone on your team can easily create scoped personal buckets. To define a new shared bucket, simply select a workflow (from among any defined in your CI, automatically pulled in by Runway), a branch, or some combination of both.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71808&key=user_uploads/562880/1bef9a17-07df-4d74-8d39-b1607e832e8e)

🤝 **Standalone or tightly integrated with the rest of Runway**

Exactly how you leverage Build Distro is up to your team. You can spin up Build Distro by itself and use it as a standalone tool. Or, for a tightly integrated experience across the entire dev and release cycle, Build Distro plugs seamlessly into Runway’s end-to-end release management platform as a beta integration, allowing you to manage everything to do with pre-prod builds and testers alongside the rest of the release context. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71808&key=user_uploads/562880/21fcb35f-06ec-4ee9-8b97-529a179561bc)

### Who is Build Distro for?

Build Distro is for mobile teams of all sizes who care about getting builds into the hands of team members and testers early and often. 

There are a few team members that might be especially excited about Build Distro:

* Mobile engineers who want to get more eyes on their in-progress work, well before it makes its way to the team’s main branch
* PMs who care about checking out product work as it’s being developed, without having to hunt around for specific builds
* QA folks who want to stay on top of testing without the volley of unintelligible build numbers over Slack
* Anyone on the team, technical or non-technical, who cares about the product and wants to check out and help test builds pre-production

 

### How to give Build Distro a try

You can sign up for free on the [Runway site](https://app.runway.team/signup?intent=buildDistro), no credit card required, and we’re always available to give folks a guided walkthrough as well – just get in touch!

## 📲 📈 Rollouts by Runway

# A single source of truth for mobile release health, instantly understandable – and actionable

As former mobile engineers ourselves, the Runway team and I have experienced the challenge of rollouts firsthand  — and now, we’ve built something that can help. We’re excited to announce [_Rollouts_](https://www.runway.team/blog/introducing-rollouts-by-runway), a new part of the Runway platform that helps your team navigate rollouts with less collective stress, and more confidence. _Rollouts_ allows you to easily keep tabs on release health in just one place instead of many, alerts you whenever configured metrics become unhealthy, and safeguards release health by automatically halting rollouts based on thresholds you define.

# What is _Rollouts_?

Here are some highlights:

### 🗺 The only complete picture of release health

Rollouts integrates with the mix of different tools you use to measure app health – crash reporting, observability & product analytics, the app stores (for per-version user ratings) – to create a single source of truth and unified dashboard that gives your team a holistic and instantly understandable view of release health at a glance. No more context-switching, no more mental overhead.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=67143&key=user_uploads/562880/098822f9-93e6-4ac4-a612-c13ce50f187e)

### 🌡 You define exactly what “healthy” means for your team

Across all tools and every metric, you can configure granular thresholds that together define what “healthy” looks like for your team. Runway will surface a crystal clear view of how each release is tracking relative to that definition. With expectations around health codified this way, there’s no room for ambiguity or hand-waving when it comes to your team’s standards for quality of the product you’re shipping.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=67143&key=user_uploads/562880/479df881-d88e-4e1e-9cc2-d4ac27941bc4)

### 🚨 Avoid blind spots and delays with instant alerting

The moment any of your configured metrics become unhealthy during a rollout, Runway will alert your team, in specific channels of your choosing and with full context on which metrics are problematic. You can be confident that no bad trends will go unnoticed – and that they can be acted on more quickly.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=67143&key=user_uploads/562880/115d18e8-0167-47e6-8ce4-630bed0f564a)

### 🛑 Automatically halt unhealthy rollouts

Building on the custom thresholds you define, Runway can automatically halt unhealthy releases. With this automation enabled, if certain metrics of your choosing fall afoul of your acceptable thresholds during a rollout, Runway will automatically stop the rollout and alert your team. This prevents delays and human error, saving you from the negative consequences of a bad release making it out to even more users.

_(Available on the Runway Pro plan and above.)_

![uploaded image](https://www.ycombinator.com/media/?type=post&id=67143&key=user_uploads/562880/7f6156eb-df96-4332-b4d7-c432c4aac58f)

### 💨 Automatically accelerate healthy rollouts

If all of your metrics are looking good and your rollout has reached a minimum number of users you define, Runway can accelerate things and release to all users immediately. Getting a good release out to all users more quickly can be just as impactful as halting a bad release!

_(Available on the Runway Pro plan and above.)_

![uploaded image](https://www.ycombinator.com/media/?type=post&id=67143&key=user_uploads/562880/9088b19a-3ce0-467f-a390-2368f4c92464)

# Who is _Rollouts_ for?

_Rollouts_ is for mobile teams of all sizes who care about the quality and health of the apps they ship. If you want to ensure you’re not shipping bad product and your users are having the best possible experience, without painstaking babysitting, _Rollouts_ is for you.

There are a few folks _Rollouts_ might resonate with especially:

* Release captains/drivers/pilots who want to de-stress and de-risk the experience of being in the driving seat during a rollout
* Mobile engineers who are tired of poking PMs to check on key events in some analytics dashboard they don’t have access to or don’t understand
* PMs who are tired of said mobile engineers poking them all the time
* Mobile leads or EMs who want to be sure their entire team has the full picture of release health, to foster a healthy sense of ownership and accountability
* Engineering leadership who care about keeping tabs on their mobile org, easily and noise-free
* Anyone and everyone who cares about app health and preventing bad releases from making it out to even more users

 

# How to give _Rollouts_ a try

You can sign up for a free trial via the [Runway site](https://www.runway.team), no credit card required, and we’re available to give folks a guided walkthrough as well – just get in touch!

For indies, small teams, and YC fam, we’re happy to talk discounting too.
