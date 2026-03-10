# Launches

## phospho: give a brain to your robot

**TL;DR**: phospho enables software engineers to train and build with the latest robotics AI models, even on low-cost hardware. Companies like NVIDIA, Hitachi, [rerun.io](http://rerun.io) and [comma.ai](http://comma.ai) use phospho to control robots intuitively, train advanced models and push the frontier of AI robotics.

https://youtu.be/72EOUeDMUYc?feature=shared

Imagine asking ChatGPT “What should my robot do next?” with a picture of what your robot sees attached. Add some bells and whistles, and you have VLAs (Vision Language Action models), the latest AI robotics architecture.

VLAs reach never-seen-before levels of generalization, which could finally bring robots out of factories and into our homes. “The ChatGPT moment for general robotics is just around the corner” (Jensen Huang, CEO of Nvidia).

So why aren’t VLAs more popular in robotics?

# The problem

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90566&key=user_uploads/1345093/14eb12de-bee4-4dd6-8cc8-c84257b14b5c)

First, let’s find some data to train your model. Guess what: even if you find public datasets, they likely won’t work for your specific robot and setup. So you’ll need to use some software for humans to control the robots and collect this specific data. Of course, such software usually doesn’t exist or doesn’t work. Today, controllers are built from scratch for every project, by engineers, for engineers.

Second, you train the model. This is where you shine.

Third, now that you have trained a model, you can’t “just run” your tinkered AI model in a lab on a $20,000 robot arm. You need a lot of software glue to make robots move. For example, powering on a robot can take up to 10 minutes, and keeping it idle requires dozens of specific instructions to avoid breakdowns.

Overall, we found that the traditional robotics software stack is too specific to the available hardware, too closed source, and too prohibitively expensive to reproduce robotics research papers. This is because every robotics team, from garage hobbyists to giants like Figure, Tesla, and Physical Intelligence, build their stacks from scratch and won’t share them.

Nobody works together. Robots still suck. How can we reach physical superintelligence with this absurd stack?

# Our solution

https://www.youtube.com/shorts/q7f3XKadKxQ

We believe robotics is too important to let roboticists do it alone. Robotics is the next step in our civilization, and every human brain should be able to help us reach this goal. Building an intelligent robot should feel as fun as vibe-coding a web app.

That’s why we are releasing phosphobot, an open-source app to control robots intuitively and train the most powerful AI models for the cheapest robots possible.

We handle the piping and nitty-gritty, so you can focus on what matters: making your robots do cool things.

phosphobot is written in Python and TypeScript, with software engineers in mind. It’s just another API, with a nice frontend, that you can “pip install” and connect to your stack.

In the coming weeks, the plan is to support even more affordable and capable robots, let you train even more advanced AI models, and keep the app simple enough so it’s still fun.

# Key features

* 🕹️ Control your robot with a keyboard, a leader arm, a Meta Quest headset or via API
* 📹 Teleoperate robots to record datasets in LeRobot dataset format
* 🤖 Train SOTA action models like ACT, gr00t n1 or Pi0
* 🔥 Use action models to control robots
* 🌐 Connect remotely to your robots
* 💻 Run on any OS (macOS, Linux and Windows)
* 🦾 Compatible with the SO-100, SO-101, WX-250 and AgileX Piper
* 🔧 Extend it with your own robots and cameras

## Train your first robotic action model today

Go to our Github repo ([phospho-app/phosphobot](https://github.com/phospho-app/phosphobot)) and get started in minutes.

Don’t have a robot? Order one here: [robots.phospho.ai](http://robots.phospho.ai)

Want to integrate custom robots, train more complex models or have a specific request? Contact us at [contact@phospho.ai](mailto:contact@phospho.ai).
