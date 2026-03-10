# Launches

## 🏄 SensorSurf - Data infra for robotics

> **tl;dr:** Robots produce a lot of data, and it’s a challenge to collect and manage all of it. Our infrastructure enables companies to easily collect, offload, and make use of sensor data.
>
> ![uploaded image](https://www.ycombinator.com/media/?type=post&id=67785&key=user_uploads/1161431/6669487c-0baf-4116-b0b7-1dd6b0ba7ec6)


---

Howdy, YC! I’m [Alec Bell](https://www.linkedin.com/in/alec-bell/) from SensorSurf. I love robots, and I’m writing software to make it easier to build them.

### **❌** Problem

Robots generate absurd quantities of data. **A single self-driving car produces up to 1.5 petabytes/year** ([source](https://www.tuxera.com/blog/autonomous-cars-300-tb-of-data-per-year/)). Developers need access to this data to diagnose issues, train models, and run simulations; but it’s hard to get a hold of since its clunky and sits on an edge device. Robotics companies currently build data infra in-house, which is extremely costly.

### ✅ Solution

**SensorSurf offers the infrastructure to collect, offload, and make use of sensor data.** Users can specify where, when, and what data to collect. From there, they can selectively offload it, run queries on it, visualize it, and put it to work for purposes like debugging, annotation, and analytics.

### 👨‍💻 How it works

Robotics companies install **a tiny agent on their robots,** which allows us to establish a connection to our services and **observe their system.** We can then collect data across a fleet of robots and help users manage/search it in the cloud, accounting for network constraints that our customers may experience.

### 👍 Noteworthy features

* [Event-based data collection](https://docs.woeden.com/collection/auto_record)
* [Rolling buffers/windows of data](https://docs.woeden.com/collection/rolling_buffer)
* [Data streaming for visualization](https://docs.woeden.com/management/visualize)

### 🙏 Asks

* **Robotics developers:** [**try out our tool**](https://docs.woeden.com/getting_started)**!**
* Share this post to robotics communities.
* Connect us with robotics companies and researchers ([founders@woeden.com](mailto:founders@woeden.com)).
