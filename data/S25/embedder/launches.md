# Launches

## Embedder – Cursor for Embedded

https://www.youtube.com/watch?v=aqCMsZwhXME

**TL;DR**: Embedder is building the AI-IDE for embedded software engineers. Today, we launched a web platform that allows you to manage your components, chat with agents and generate production-level driver code in seconds. Near term, we will be launching an agent mode via CLI that can flash, test and debug your hardware in real time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92136&key=user_uploads/2361352/b88ffbfb-9362-4984-aaa6-fe0734212ead)

https://embedder.dev/

**THE PROBLEM**

Embedded engineering is bottlenecked by repetitive, manual work. Engineers waste countless hours parsing 100+ page datasheets, writing boilerplate I2C/SPI drivers from scratch, and wrestling with scattered documentation just to get a new component working.

The industry’s tooling is stuck in the past. We’re forced to wrangle fragmented toolchains and navigate archaic, bloated IDEs. The major silicon vendors (ST, TI, Renesas, NXP) provide IDEs for their own ecosystems, but these tools are notoriously undocumented, unintuitive, and sometimes straight up broken. Because their business is selling silicon, they have little incentive to build the world-class development environment that engineers deserve.

**OUR SOLUTION**

Today, you can use our web platform to automate component bring-up:

* **Driver Generation**: upload one data sheet, get production-ready C/C++ drivers for STM32, ESP32, Arduino, or Raspberry Pi Pico in seconds. Our AI understands register maps, timing diagrams, and communication protocols.
* **Datasheet-Aware Agent**: chat with an agent that has deep context on your specific components and microcontrollers. It grounds all its responses in manufacturer-provided facts, ensuring accuracy for your hardware configuration.
* **Interactive Component Viewer**: ditch the PDF reader. Our custom UI gives you an interactive, searchable view of your component’s key information.
* **Community Repository**: stop reinventing the wheel. Share your component models and discover drivers built by the community.

**TEAM**

Bob and Ethan have known each other for over three years. They met through startup clubs at the University of Michigan and served on the board of an engineering fraternity together. 

Ethan has worked at three startups since starting college (2× YC backed) and Bob has worked on multiple firmware teams building humanoid robots and autonomous vehicles. We’re both passionate builders who have lived the frustrations we’re solving.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92136&key=user_uploads/2361352/db4d8132-9d6e-4171-ad8d-d4227c202131)

**CTA**

If you're an embedded software engineer (or know one) frustrated with existing tools and manual workflows, it’s free to sign up at [https://embedder.dev/](https://embedder.dev/%5C)

If you're building embedded systems (IoT, robotics, automotive, etc.) and want to 10× your engineering team, send us an email ([founders@embedder.dev](mailto:founders@embedder.dev)); we're working out our first design partnerships!
