# Launches

## Elodin - CI/CD for Aerospace ✈️ 🛰 🚀

### **TL;DR**

[Elodin](https://www.elodin.systems) helps aerospace engineers rapidly design, test, and simulate control systems. For example, an engineer could use our Python physics toolkit, which automatically optimizes physics computations for GPU computing, to test a new satellite control system in minutes instead of hours.

---

Hello everyone! We’re [Dan](https://linkedin.com/in/x46085), [Sascha](https://linkedin.com/in/sascha-wise), [Andrei](https://linkedin.com/in/andrei-khvalko), [Tom](https://linkedin.com/in/tomgurka), and [Akhil](https://www.linkedin.com/in/akhil-velagapudi/) from [Elodin](https://bookface.ycombinator.com/company/29381). 

Drawing experience from roles at AstroForge, Google, Salesforce, Spatial, and several startups. We discovered that the rapid iteration in cloud software was missing in the field of aerospace, so we were compelled to make the development experience better.

---

### **Problem**

If you want to build an autonomous drone today, you've only got a few options when it comes to testing.

* You can write your control system, flash it to your flight computer, launch the drone, and watch it crash over and over again. 
* You can agonize over setting up a complex simulation using MATLAB, Gazebo, or something homegrown.

Those choices are time-consuming, complex, and costly.

Now, imagine you are building a satellite or an eVTOL aircraft; you have no choice but to set up a complicated simulation.

---

### **Solution**

How does Elodin prevent this complexity?\
**We don’t; we just do it for you.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77547&key=user_uploads/1618322/9f285018-486c-4602-adb3-43297bf75961)

Congrats! You can now simulate your drone's control system easily, but that's not enough. What if a massive windstorm comes around? What if the neighborhood dog decides to take a bite out of one of the propellers? You need to test your control system for any situation you can imagine.

**Enter** - [Monte Carlo Testing](https://aws.amazon.com/what-is/monte-carlo-simulation/#:\~:text=The%20Monte%20Carlo%20simulation%20is,on%20a%20choice%20of%20action.)

Monte Carlo testing is when you run a simulation multiple times with randomized initial conditions. For example, you could run your simulation with randomized wind speeds.

Elodin makes running Monte Carlo simulations seamless, through our cloud platform. We let you run 100,000s of simultaneous simulations right from the comfort of your laptop. 

Our dream is that you run a full Monte Carlo test of your control system every time you push code to GitHub. Historically, this would be very costly and difficult to achieve.

---

### **What Elodin is**

🐍 **Python physics library** - A toolkit for building custom physics engines using the GPU, imagine Tensorflow, but for Physics

🎲 **Monte Carlo Cloud Runner** - A cloud runner that enables you to run your simulation in a scalable Monte Carlo fashion

🌎 **3D Viewer** -  A live-reloading 3d viewer to share, inspect, and analyze your simulations

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77547&key=user_uploads/1618322/d2e5c348-a7f8-47c4-8522-1025a8d966dc)

**Try out our Alpha!** We have an early alpha sandbox prototype that showcases the real-time editing experience of Elodin but does not include our customizable physics engine or Monte Carlo support.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77547&key=user_uploads/1618322/effd2707-d83b-4dc4-9c1f-deea7f65fb74)

---

### **Our Asks**

**Reach Out:** If you work with drones, satellites, or anything else with a control system, [schedule a call with our CEO, Dan](https://calendly.com/dan-elodin/30min), to discover how Elodin can streamline your design and testing processes

**Share Your Insights:** We value your perspective! If you have any feedback or suggestions, we'd love to hear from you. Your insights are crucial to shaping the future of Elodin.

**Connect Us:** Even if Elodin is not the perfect fit for your needs, you may know someone who could benefit from our platform. If you have connections in aerospace or related industries, we'd greatly appreciate sharing our website/demo with them or even better a direct introduction to [founders@elodin.systems](mailto:founders@elodin.systems)
