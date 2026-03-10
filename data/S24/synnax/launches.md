# Launches

## Synnax - The software infrastructure for operating & observing complex hardware

### **Summary**

Teams operating hardware from rockets to manufacturing lines use outdated, unintuitive control software that disregards the importance of rapid, quality data processing. This leads to unexpected downtime, disastrous anomalies, and delayed development.\
\
[Synnax](https://synnaxlabs.com) delivers a modern mission control stack with integrated data storage & processing. Wrap [LabVIEW](https://www.ni.com/en/shop/labview.html?cid=PSEA-7013q000001fLK5AAM-CONS-GOGSE_161597904920&utm_keyword=labview&gad_source=1&gclid=CjwKCAjwhvi0BhA4EiwAX25ujz2zA6xF3VRQaQaUKSnIWT-PQLXdmQGvejLgYkhZ7wgR4DdhgZxLyRoClgkQAvD_BwE#521715&s_kwcid=AL!6304!3!691563588228!b!!g!!labview), [Snowflake](https://www.snowflake.com/en/), and [Grafana](https://grafana.com/) into a single package, tune it for hardware, and you get Synnax.

### **The Problem**

We’re a group of Aerospace Engineers hailing from NASA JPL, SpaceX, and Firefly Aerospace. (From left to right: [Patrick Dotson,](https://www.linkedin.com/in/patrick-dotson/) [Elham Islam](https://www.linkedin.com/in/elham-islam-/), and [Emiliano Bonilla](https://www.linkedin.com/in/emiliano-bonilla-8a0a95187/))

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82381&key=user_uploads/529055/2aa036ec-8e14-4f42-b5e3-7715e93d17a1)

We’ve seen the best engineers blow up multi-million dollar systems because their mission control software didn’t give them a comprehensive picture of how their hardware was behaving. A director of test & launch operations once told our team:

> It’s amazing what people guess at just because loading data is so hard

To put their quote in context, here’s what the leading aerospace control software, LabVIEW, shows as a UI screenshot on their landing page:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82381&key=user_uploads/529055/fe8ee6b7-a6bb-43c6-8cda-ee5c596d40b8)

Remember [Scratch](https://scratch.mit.edu/about) or [Lego Mindstorms](https://www.nxtprograms.com/help/learn.html) from elementary school? LabVIEW is kind of like that, except people use it to fly humans to space. LabVIEW and its cross industry counterparts (such as [AVEVA Scada](https://www.aveva.com/en/solutions/operations/scada/) and [Rockwell FactoryTalk](https://www.rockwellautomation.com/en-us/products/software/factorytalk.html)) were first developed in the 20th century and have evolved little since. These tools come with:

* Outdated, unintuitive user interfaces
* High price tags
* Closed ecosystems with no integrations
* Poor documentation
* Expensive certifications

**Most importantly, they disregard the importance of tightly integrated and automated data processing that drives the innovation of today’s software giants.** Most solutions spit out massive CSV files or mindlessly write data to an SQL table. They’re disorganized, difficult to locate, inaccessible to most engineers, and are challenging to integrate with analysis tools.

### **Our Solution - The Product**

At Synnax, we’re building a modern alternative to tools like LabVIEW by developing tightly integrated hardware control, sensor data storage, and automated post-processing software. Here’s our UI:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82381&key=user_uploads/529055/012764f7-8440-406b-b51e-fc82ee687b6c)

We deliver:

* Intuitive interfaces for humans to manually operate everything from automotive test stands to manufacturing lines.
* Tools for categorizing and reviewing historical data.
* Automated post-processing and report generation pipelines.
* Direct integration with existing sensor systems so teams don’t need to buy new hardware.
* A simple API for writing automated control sequences in Python, C++, and TypeScript.

It’s this easy to open a valve based on temperature in Synnax:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82381&key=user_uploads/529055/197cb0a0-dc36-41fb-a273-816dd06d67f8)

Here’s a comparable sequence in LabVIEW:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82381&key=user_uploads/529055/64d695d8-a786-49a1-975d-cecb7facf9f7)

### **Our Solution - The Tech**

We’ve built one of the fastest time-series database engines available. Synnax can stream millions of samples per second in real time, making it possible to control systems with extremely tight timing requirements, such as starting a rocket engine.

### **Our Solution - The Impact**

By bringing together hardware control and sensor data processing, organizations operating large, complex systems tighten the feedback loop between recording sensor data and using it to make actionable decisions.

With Synnax, teams:

* Reduce risk by detecting and reacting to anomalies in real time.
* Spend less time developing in-house data processing solutions.
* Reduce the manual labor involved in extracting insights from sensor data.

### **Our Asks**

Do you work on hardware and need updated control software? Do you know someone who does? Let us know at [founders@synnaxlabs.com](mailto:founders@synnaxlabs.com).
