# Launches

## Cerulion 🤖 Fast, reliable, cross-platform robot middleware

Robots are expensive and hard to develop/debug. [Cerulion](https://www.cerulion.com/) solves the robot tooling problem to cut down development times by up to 10x.

# The Problem

The incredibly high capital costs required for robotics, combined with the inherently non-deterministic nature of embodied intelligence, result in an unpredictable system where even attempts, let alone failures, are cost-prohibitive.

**Robots are expensive and hard.**

And yet, despite time on hardware being such a precious resource, roboticists today are absolutely wasting 90% of it fighting against unoptimized tooling. Some common complaints are:

* Needlessly complex to install, maintain, and document
* Incredibly steep learning curve for non-transferable skills
* Poor observability into a robot's belief
* Artificial non-determinism induced by slow or unreliable message-passing
* Unreliable network protocols and IPCs
* System breakdown due to poor inter-robot communication
* Unreliable logging and cumbersome/nondeterministic log replay
* Wasting precious field time parsing 1000s of lines of runtime errors whooshing past the screen

And the list goes on and on.

**Robot tooling today is broken. Unacceptably so.**

# Our Solution: Performance never looked this good!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83665&key=user_uploads/1938980/f6733a7c-7d31-4bf8-9198-d19e786c5650)

* **Packaged as an app, rather than a CLI tool:** Instead of shipping as a bunch of CLI tools to be installed, patched, and reinstalled, Cerulion is an app you can download on Windows, Mac, or Linux. It will smartly detect and handle any dependencies as needed.
* **Intuitive, cross-platform visualizer:** The sleek, easy-to-use GUI is the main way of communicating with your robot in the field, which means you can run it with minimal resources on your favorite long-lasting laptop with any OS, instead of **_that_** RGB laptop with a gaming GPU running Linux.
* **Minimal boilerplate and setup:** The way you program robots in Cerulion is designed to get out of your way, so you can focus on the planner and perception algorithms instead of worrying about the inter-process comms, IP addresses, or network routes.
* **Fast and reliable communication:** We leverage cutting-edge Rust-based networking and IPC stacks like [Zenoh](https://github.com/eclipse-zenoh/zenoh) and [IceOryx2](https://github.com/eclipse-iceoryx/iceoryx2), along with tried and tested C++ alternatives like [LCM](https://github.com/lcm-proj/lcm) and [IceOryx](https://github.com/eclipse-iceoryx/iceoryx). By ensuring communications don't fail silently and messages are delivered when expected, Cerulion eliminates nasty surprises in safety-critical scenarios.

# Meet The Team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83665&key=user_uploads/1938980/62663160-4581-4de2-abb8-0bbb86179aa1)

As robotics PhD students at MIT, [Lakshay](https://www.linkedin.com/in/lakshay2010sharma/) and [Se Hwan](https://www.linkedin.com/in/sehwan-jeon/) have gathered years of experience (and frustration) working on robots, and want to see a world where you can take robot reliability for granted.

# Our Ask

Have experience with ROS or any other robot middleware? Did we miss something above that you really need? Send us a message at [founders@cerulion.com](mailto:founders@cerulion.com)!

We always love (and are happy to provide) warm intros to people working on robots and automation.

And of course, if you need help with your robot system, or are curious about any of this, we're happy to chat!

P.S. — Please star our [GitHub repo](https://github.com/cerulion-inc/cerulion)!
