# Launches

## Conductor — Run a bunch of Claude Codes in parallel

Back in June, we started doing most of our dev work through Claude Code. It’s been so productive we [declared it a member of the team](https://x.com/charliebholtz/status/1935029747815432505).

We immediately wanted to get _more_ Claude, but the tooling was tedious. At one point we tried cloning our repo into three directories and running Claude in each of them, but it felt like driving a Subaru with a jet engine strapped on.

We needed a tool that would push Claude to its limits and that we’d enjoy working in all day.

So we built Conductor!

https://www.youtube.com/watch?v=VsWWy2kVpa8

Other people seem to like it too:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93356&key=user_uploads/331436/b581e29f-2ada-49d3-88f7-c91e6bfb7cf4)

### **How it works**

**In one click, start a new Claude in an isolated copy of your codebase.**

We integrate with Linear so you can easily start work on your issues.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93356&key=user_uploads/331436/315a80c3-3a33-4296-83cc-f0ac06a4b1f4)

**See at a glance what every Claude is working on.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93356&key=user_uploads/331436/3993651e-9bbf-4b62-9e70-32c4ff01ffe8)

**Review Claude’s changes, create PRs, and merge!**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93356&key=user_uploads/331436/3d654281-7394-483a-b53d-b7b09d8f5980)

### **Start Conducting**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=93356&key=user_uploads/331436/b151e732-3397-4d8e-a138-911dd03a3c64)

It's free—we use your existing Claude Code login. You can [download for Mac now](https://conductor.build).

Can’t wait to hear what you think!

## Melty: Open source AI code editor for 10x engineers

Hi everyone! We’re Charlie and Jackson. We’re longtime friends who met playing ultimate frisbee at Brown.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83684&key=user_uploads/229410/ab31f858-0576-4cfc-8796-4148b999faae)

[Charlie](http://charlieholtz.com/) comes from [Replicate](https://replicate.com/), where he started the Hacker in Residence team and [accidentally struck fear](https://www.businessinsider.com/david-attenborough-ai-video-hollywood-actors-afraid-sag-aftra-2023-11) into the heart of Hollywood. [Jackson](https://jdecampos.com/) comes from Netflix, where he [built machine learning infrastructure](https://netflixtechblog.com/scaling-media-machine-learning-at-netflix-f19b400243) that picks the artwork you see for your favorite shows.

We’ve used most of the AI coding tools out there, and often ended up copy-pasting code, juggling ten chats for the same task, or committing buggy code that comes back to bite us later. AI has already transformed how we code, but we know it can do a lot more.

So we’re building [Melty](https://melty.sh/), the first editor that’s aware of what you’re doing from the terminal to GitHub and collaborates with you to write production-ready code.

We’ve been working on Melty for 28 days, and it’s already writing about half of its own code. It can…

_(all demos real-time)_

**Refactor code across files**

<https://www.loom.com/share/f0e7ae2644e6492ab9e9352fbd14ae8d?sid=b5d497cd-65f4-47ca-955a-73332d8edc4d>

**Create web apps from scratch**

<https://www.loom.com/share/4f4f85c3de8b420e85b65537b775e3c8?sid=01b43f48-0fec-400a-8bee-71132f6d4610>

**Navigate large codebases**

<https://www.loom.com/share/fc4eb54385a5426586160fad5dbfc1be?sid=73a79e2e-1505-47a1-838b-a375cf7523e4>

**Write its own commits**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83684&key=user_uploads/229410/5b579ebb-e893-4a2e-b571-97d7136c681c)

We’re designing Melty to

* Help you understand your code better, not worse
* Watch every change you make, like a pair programmer
* Learn and adapt to your codebase
* Integrate with your compiler, terminal, and debugger, as well as tools like Linear and GitHub

Our asks:

1. Try Melty ([melty.sh](http://melty.sh)) and tell us what you think. It’s a fork of VS Code, so it’s compatible with all your settings and extensions.
2. Tell us: what AI coding tools do you use, what do you like about them, and what’s frustrating? [DM Charlie](https://x.com/charliebholtz) or send us an email at [founders@melty.sh](mailto:founders@melty.sh).
