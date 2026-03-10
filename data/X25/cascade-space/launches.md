# Launches

## Cascade Designer - Spacecraft communication system design software

https://youtu.be/cPNXStE7LcE

Cascade Space was founded to build the ground station company of the future. But lack of large dishes is not the only thing broken about space communications, so are the design tools. 

Industry standard spreadsheets are painful to build and maintain and error prone, but they can at least get you started. That said, they completely break down once you need to predict how your spacecraft will perform in real world dynamic environments, analyzing multiple variations of a system, or sharing and keeping the design updated across teams.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96236&key=user_uploads/222992/5bdf36f9-9f71-4796-9f12-ecbeba37d8c4)

Every space company eventually starts to build internal tooling to parse 3D antenna patterns and scripts to evaluate link performance over given flight trajectories. This is usually unplanned work done by RF engineers that takes months to get even a rudimentary implementation up and running. This software is very bespoke and often brittle, and makes the tight timelines of early stage companies even tighter.

Across the industry this work gets duplicated over, and over, and over. 

**Enter Cascade Designer**. The pipeline is already built. Start by designing your system in a graphical interface, get your link margin with a single button click. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96236&key=user_uploads/222992/7e4a5642-dc70-4093-a7d5-5a2b1802cda3)

Next, analyze entire trajectories with a single API call. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96236&key=user_uploads/222992/980c9907-784c-4861-8758-b6341afd2721)

Designs can be shared with anyone on your team through our interface

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96236&key=user_uploads/222992/bec0b967-999c-4089-849f-d0c547431498)

We built this out because the customers of the best ground network need the best design tools, but we didn’t just build this for our ground station customers. Anyone designing a spacecraft for any orbit using any ground station can use it. 

Visit our website to learn more and book your demo: https://cascade.space/designer/

## Cascade Space - Deep space communications as a service

# tl;dr

Cascade Space is building a turn-key communications system for lunar and deep space missions. Our ground station network and integrated software tools work together to maximize uptime and availability, while reducing spacecraft iteration cycles from weeks to hours. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90423&key=user_uploads/222992/7b3a56ce-8dc0-48db-a2e5-3badb2afd893)

**Why are we building this and why now?**

The Deep Space Network (DSN), NASA’s global network of ground terminals for communicating with deep space probes, is [oversubscribed by 40% and in desperate need of upgrades.](https://newspaceeconomy.ca/2024/09/02/nasas-deep-space-network-challenges-and-the-road-ahead/) The DSN is all but unavailable for most commercial operations. Companies with missions going to the Moon and beyond have to deal with a patchwork of individual dish operators for every mission, each with bespoke hardware, specs, and interfaces. Furthermore, many of these commercial providers are not able to handle the demand and [operational failures also can lead to loss of mission](https://www.astroforge.com/updates-collection/odint-mission-debrief).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90423&key=user_uploads/222992/c6aa8968-e567-42e5-8866-866414630f22)

**Comms system design is fraught with peril**

The spacecraft comms system design is tightly coupled to the available ground network. Engineers spend hundreds of hours poring over datasheets, on the phone with vendors and suppliers, and endless email threads, only to put all this data into a giant spreadsheet to make sense of it. Every iteration requires not only painful attention to detail, but also in-depth esoteric knowledge of how radio frequency systems and channel coding schemes work in order to accurately predict in-flight performance. Simple misunderstandings can lead to catastrophic errors in design and configuration.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90423&key=user_uploads/222992/1623d16f-4789-4793-892f-2c7adffc84a7)

**End-to-end comms system validation often doesn’t happen**

Fully integrated testing between the spacecraft and ground terminal is typically cost prohibitive. Instead, engineers compare spec sheets and email configurations to the ground operators, and hope it works in flight (spoiler alert: it often doesn’t). It is routine for spacecraft to fly having never done an end-to-end test of their system with ground terminal representative hardware. The whole process is subject to human error from end to end. 

**This approach to space communications does not scale**

Commercial space ventures beyond low earth orbit have already pushed existing infrastructure to its breaking point, and demand for deep space comms support is expected to grow exponentially over the next decade. We will not have a spacefaring future for humanity until communications for spacecraft become as easy as signing up for cable internet. 

**We are redefining the process, starting with spacecraft design**

Better comms starts at the beginning, in the early trade study and design phase. We are replacing industry-standard spreadsheets with a modern software tool that lets you see how your system will perform with our ground network in real time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90423&key=user_uploads/222992/4873c5a0-9288-48fe-8d2e-a3a32f3fcad0)

**Test as you fly, fly as you test**

You don’t rise to the level of your expectations, you fall to the level of your testing. We ship you a “ground station in a box,” identical to hardware we’ve installed at the ground stations you will be using, and provide you with a test plan that you can use to test your entire system end to end, with both the space vehicle and the ground terminal in the loop. 

**Launch with confidence**

Fly and operate your spacecraft. Use our API to schedule passes on our network, track your spacecraft, stream data, monitor the ground site, and access recordings.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90423&key=user_uploads/222992/2b01ca98-b6d7-4f8b-9af5-5b93b0613ef0)

**We are rolling out our preliminary network rapidly**

We start by partnering with owners of dishes that are currently unused for any other telemetry applications. This allows us to build out the product and acquire customers with a minimal amount of capital. As we build out the network, we will further expand our network by strategically building our own ground stations in key locations. Our first downlink only ground stations are expected to come online in 2025, with more to follow in 2026.

**We are passionate about your mission success**

[Jacob](https://bookface.ycombinator.com/company/30556) and [Arlen](https://bookface.ycombinator.com/user/2222230) have solved many of these exact problems at company level scales in previous roles. Jacob was RF system architect at SpaceX and Arlen has built complex hardware/software systems his entire career. Collectively they have spent hundreds of hours in mission control, many of those hours dealing with anomalies and outright failures. They are both passionate about building the culture of excellence at Cascade that is required for flawless mission execution.

**If you are struggling with comms for your upcoming mission, drop us a line. We can help.**

https://cascade.space/
