# Launches

## Radars for end-to-end autonomy

**TL;DR:** Everyone wants an autonomous car, but today they are cost prohibitive because they rely on multiple lidars. The answer is radar, it's tens of dollars, already in most cars, and works in all weather. The problem: no one has built a radar compatible with end-to-end training, which is how all modern autonomous vehicles learn to drive. We built the radar hardware and radar simulator to change that.

<https://youtu.be/gxdcpLKO_xA>

Today, a robotaxi costs hundreds of thousands of dollars, largely because it relies on lidar, an expensive sensor that works but doesn't scale. **Radar costs tens of dollars per unit, is already in 90% of US cars**, and works in rain, snow, fog, and dust where lidar and cameras degrade. The problem is that no one has built a radar that is compatible with how autonomous vehicles are actually trained.

**The state of the art in autonomy is end-to-end training:** a single neural network learns driving actions directly from raw sensor data. Inclusion in end-to-end training requires two things from each sensor: access to raw data and a high-fidelity simulator. Cameras have both. Lidars have both. Radars have neither. Every automotive radar on the market throws away over 99% of the raw data before the model sees it, and no existing world model is able to simulate radar data.

**Self-driving requires multi-sensor redundancy** and depth sensing that cameras alone cannot provide, but camera-radar fusion can. An OEM that adopts Congruent's radar can train a single end-to-end system on several cameras and radars together, reaching full self-driving, at a sensor cost low enough to ship in every vehicle they make.

We are Clement Barthes and Evan Carnahan, two PhDs who met as research engineers building radar perception pipelines for autonomous vehicles. Clement earned his doctorate in Structural Mechanics from UC Berkeley and developed advanced sensor systems for automotive and structural health monitoring applications. Evan earned his doctorate from UT-Austin, where he built physics-learned models for multi-sensor satellite data. We launched Congruent because we kept running into the same wall: **radar has the physics to enable mass-market autonomy, but no one was building the hardware and simulation tools to make it usable in modern training architectures… until now**.

**If you are at an OEM, tier-one supplier, or AV company working on sensor architecture or end-to-end training, let’s get in touch !  [info@congruent.io](mailto:info@congruent.io)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98073&key=user_uploads/1953552/87d983de-4b46-4ea3-ad8a-44bedfb39325)
