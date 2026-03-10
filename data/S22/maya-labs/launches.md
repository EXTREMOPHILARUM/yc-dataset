# Launches

## 🛠️ 🧠 Maya Labs : Build custom software in minutes, using natural language

Hi, we are Sibesh and Shubham, founders of Maya Labs. We are on a mission to teach machines how to code - starting off with a fast way to build internal tools in minutes using just natural language. Here’s an early look :

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65194&key=user_uploads/272578/a3e654bf-56a0-48e4-abeb-8922bc23b8b0)

A longer 5-min demo [here](https://www.youtube.com/watch?v=NPm0idKktzs) :

Today, you can build one particular type of custom app well using Maya that let's you :

1. **Fetch custom data** : Configure setup + query custom data from an external source (currently we do SQL, Gsheets, Notion, Airtable etc, but are expanding fast)
2. **Visualize it** : Plot and visualize it in a custom table, line chart or bar graph
3. **Perform actions** : Select and act on a particular data item (send a custom email, upload a file, trigger an API, update a DB item)

Maya incrementally generates programs & shows results in response to steps you type in English, so the whole experience doesn’t feel like debugging someone else’s code. It’s possible to modify, delete & debug the natural language parts and Maya responds instantly - which makes it possible to hold and move around the _natural language program_ in your head. Checkout an early version of the docs [here](https://mayalabs.io/docs). We intend to keep it just one page long.

There’s still a lot to figure out and we’re trying to nail the experience for this one narrow use case first. When this works, we’ll try to extend it to just about any task you can think of - web navigation, connecting APIs, platform robots, RPA, home automation. Here’s a [show reel](https://mayalabs.io/library) of what else you can build manually with Maya today.

**Who is this for?**

Most internal tool builders are used by developers to build software for others on the product/ops/growth/sales/data teams, but we think this is a way for the user of the tool to also be the creator.

**How does this work?**

We use a combination of conditional logic, neural search/classification, fine-tuned language models and template generation to make this work **predictably** and **reliably** in response to words you type/modify. We generate programs in a custom flow-based programming language that lets us express a wide range of behaviours with a smaller program length and visual DAGs. We also created our own benchmark to measure how well machines are at generating code (see our paper on this [here](https://blogs.mayalabs.io/benchmark)).

**About us** :

We met in college many years back while starting Hyperloop India, the first Indian team at the SpaceX Hyperloop Competition - and have worked on-and-off on various projects since, sharing a common interest for hard engineering problems. Program synthesis is the hardest of them all - if software is eating the world, and you could build software that could build other software, why work on anything else?

We’ve been tinkering on this for years. Many Python libraries, papers, toy environments and product iterations later, we think we finally have an angle of attack that has a chance of working.

**Ask** :

1. Help us test our system! If you’d like to play around with or think someone in your team might benefit - send me a mail at sibesh\[at\]mayalabs\[dot\]io.
2. Improve Maya with useful data - Let me know if you think a particular kind of program pattern we could teach Maya would be useful for you and a wide variety of other similar users.
3. Introduce us to product/ops/growth/sales/data teams in your org who would like to build custom internal tools themselves without engineering effort
4. Hit me up to learn more about our approach! Program synthesis, robot-run economies, programs that build other programs (including the YCombinator function haha)
