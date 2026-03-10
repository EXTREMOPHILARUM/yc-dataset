# Launches

## Efference - Helping robots see like humans do

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95175&key=user_uploads/1945409/8214e17c-76b2-4c77-9b83-f11af13ff298)

Hey YC, I’m Gianluca. I’m building robotic cameras (stereo cameras) that treat vision as a software problem, not a hardware problem – just like humans do.\
\
We are actively taking pre-orders with delivery in March: https://efference.ai/preorder

[**https://youtu.be/0v0p2t3y4fI**](https://youtu.be/0v0p2t3y4fI)

Many robotics founders that I talk to are frustrated with current stereo cameras. They are expensive, require calibration, and still produce unreliable depth measurements despite their costs. Vision shouldn’t be an additional bottleneck when training robotic policies is already hard enough.

Our insight is that humans don’t have precise sensors: our eyes are noisy and imprecise but we run extremely sophisticated algorithms on top of them. Robotics already embraced this philosophy for arms (_cheap hardware + great algorithms_ → \[Zhao et al., 2023\]). We’re applying it to cameras by developing better algorithms.

What we built:

* A 3D perception model that combines stereo triangulation + learned priors about objects and environments.
* It runs in real time (unlike current neural depth approaches).
* We are distilling the model into our own hardware and shipping model wrappers for Realsense/ZED cameras so you can run these cameras better.

Check out the designs (going into production soon):

[**https://www.youtube.com/watch?v=oOmf4k2ZwaY**](https://www.youtube.com/watch?v=oOmf4k2ZwaY)

**Does it work?**

Self-Driving: [**https://www.youtube.com/watch?v=0f058JAk64A**](https://www.youtube.com/watch?v=0f058JAk64A)

Robotic Manipulation (via Functional Manipulation Benchmark): [**https://www.youtube.com/watch?v=GyV12gqGOMY**](https://www.youtube.com/watch?v=GyV12gqGOMY)

And many more demos coming to the YouTube channel: [https://www.youtube.com/@Efference](https://www.youtube.com/@Efference%5C)

**Why do we need this?**

Converting a vehicle to full autonomy can cost upwards of **$100,000**. The economics are terrible: the sensor stack dominates lifetime cost, keeping cost-per-mile high and slowing deployment. A stereo-vision stack like ours cuts that cost by **10–100×**. Lower integration cost → cheaper replacements → larger fleets → autonomy that scales. We know we can drive a car using a stereo camera because that is what humans use. It’s just a matter of getting the camera to work as well as the one humans have.

The same dynamic applies to humanoids, perhaps at an even greater scale. Companies like Unitree ship tens of thousands of robots every year, all with stereo cameras, and consumers often complain about quality. We’re building a camera that is both **affordable and usable**, so teams can actually build with it. As humanoid production scales to millions of units per year, we hope to be the camera that scales with it.

In urban drone environments, GPS fails. Reliable RGB-D depth enables SLAM, safe navigation, and collision avoidance; critical for companies like Skydio operating in urban valleys. Again, drones are another vertical that requires thousands of cameras per year that are cheap and effective.\
\
**Additional Background**

Any two-dimensional image is consistent with an infinite number of possible 3D worlds. “Seeing” is not just recording sensory input but resolving ambiguity; selecting the _most probable_ world given the available evidence **\[Born & Bencomo, 2021\]**.

Humans and nearly every other mammal have evolved the same solution to this problem over the past 500 million years of evolution: stereo triangulation + data-driven inference. We integrate every available depth cue – shadows, perspective, occlusions, and much more – along with what we know about objects and the environment to accurately represent 3D scenes and act accordingly.

Robots do not do this, but they need to.\
\
**Team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95175&key=user_uploads/1945409/2474fb24-fae7-4604-a549-2a875fad6452)

I spent the past four years at Princeton (on-leave from PhD) studying foundational topics in machine learning and neuroscience. I funded my research by writing two successful NSF grants to build biologically-inspired vision models based on the **fruit fly connectome** where the general research direction for myself and certainly my collaborators was the question of **“how do we make this fruit fly live inside a computer simulation?”**

Prior to Princeton, I spent two years at Harvard Medical School studying visual decision-making in primate models and publishing influential theoretical work on **dopamine’s role in schizophrenia and its effects on visual perception**. I did my undergraduate degree in Biochemistry and got to do some cool non-vision work at the NASA Jet Propulsion Laboratory, figuring out a **new way of converting CO2 into O2 on Mars** that recycled water and did not require heat (e.g. MOXIE).

Generally, I like to work on really hard problems.

**The Ask**

If you’re a roboticist, I’d love to learn what vision requirements matter most to you. If you know teams in autonomous vehicles, drones, or humanoid robotics, and believe this product is cool, sharing / intros would mean a lot.

We are actively taking pre-orders with delivery in March: https://efference.ai/preorder

Thank you — Gianluca.

**\[Born & Bencomo, 2021\] [https://karger.com/bbe/article-abstract/95/5/272/47302/Illusions-Delusions-and-Your-Backwards-Bayesian](https://karger.com/bbe/article-abstract/95/5/272/47302/Illusions-Delusions-and-Your-Backwards-Bayesian)**

**\[Zhao et. al., 2023\] [https://arxiv.org/abs/2304.13705](https://arxiv.org/abs/2304.13705)**
