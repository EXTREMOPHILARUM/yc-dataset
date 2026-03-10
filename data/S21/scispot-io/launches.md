# Launches

## GLUE Robo: Lab automation layer for robots & instruments

Hey everyone! This is [Satya](https://www.linkedin.com/in/satyaravisingh/) & [Guru](https://www.linkedin.com/in/iamguru/) from Scispot. We just launched [Scispot GLUE Robo](https://www.scispot.com/blog/glue-robo-automation-transforming-lab-efficiency) - lab automation layer that seamlessly connects high throughput plate movements with Scispot LIMS.

TL;DR: GLUE Robo connects lab instruments, robots, and data systems so results flow into [Scispot labsheets](https://www.scispot.com/labsheets) and databases in real time. No manual copy‑paste. No brittle scripts. Researchers get cleaner data. Heads of Data get lineage and control. Teams get time back.

🚨**The problem:**

Modern labs live between hardware, software, and complex protocols. Manual steps slow them down. Data gets siloed. Errors creep in.

Take an example of a high throughput lab tracking plate movements.

High throughput plate movements refers to the challenge of verifying and tracking the large volume of rapid, automated operations occurring in laboratory environments. When plates are moved frequently and at scale, it becomes difficult to maintain a consistently accurate record of each transaction, ensure none are missed or duplicated, and verify that every action is valid for downstream lab and data processes.

💡**The solution:**

https://www.youtube.com/watch?v=osUdOo5COJQ

Scispot webhooks (offered by GLUE Robo) are essential in this context because they capture real-time, reliable updates for every eligible system call from the robot to Scispot. This enables seamless integration, error-catching, and audibility across platforms, ensuring data integrity and full traceability as throughput increases. Here are the key highlights of Glue Robo:

* **Event‑Driven Automation.** GLUE Robo listens for lab events—plate movement, data capture, file drops, status changes—and reacts instantly.
* **Instrument‑Agnostic.** Works with leading robots and instruments (e.g., Automata, Hamilton, and more). Connect once. Scale as you add hardware.
* **No‑Code Workflows.** Build rules that match protocols, QC gates, or regulatory steps. Reconfigure as methods evolve.
* **Auditable by Default.** Every action is logged. You get traceability, reproducibility, and peace of mind.
* **Built for Throughput.** Designed to keep pace with overnight screens and multi‑run genomics pipelines.

⚡**Impact:**\
Scispot provides high throughput labs with real-time data synchronization, automation, and auditability for operations, ensuring accurate tracking and seamless integration across lab systems.

**🤝 Our Ask:**

We’re looking to connect with high throughput labs who currently leverage one or all of the following at scale:

* Automata LINQ
* Hamilton STAR
* qPCR systems
* Plate readers

Scispot provides webhooks to seamlessly capture events from such systems so you can connect your computational workflows with wet lab.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95334&key=user_uploads/697526/5a103264-9e5d-46d5-992e-697f2b67b700)

## Plato - Scispot's multi-well plate agent

Scispot is launching the world’s first agent for multi-well plates called Plato.

**Plato has the wisdom of plate automation not philosophy.**

A multi-well plate is basically a lab tool with multiple tiny "wells" or slots in one single tray. Each well can hold a separate sample, letting you run lots of tests at once—ideal for experiments like drug screening or diagnostics. It’s like having a mini grid of test tubes all in one place, so you can work faster and more efficiently.

**Plato is the agent that helps wet lab scientists design, load, integrate and run their multi-well plates using natural language.** It understands the input and output from various plate readers such as **BMG Clariostar** for your assays. It also seamlessly integrates with **Tecan** and **Hamilton** for dilution.

While designing your experiments, scientists can use Plato to create controls— standards for their assays— using AI.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85309&key=user_uploads/697526/7c482e2c-a2a5-4cb1-b775-4f670c58c10c)

### **Problem**

A wet lab scientist typically follows the journey of

* Designing a plate in excel
* Enter sample details such as IDs, concentration, standards and controls
* Prepare samples in plate according to layout and execute experiment
* Get the readings
* Add the raw data back to their ELN or LIMS system
* Cross-check data for errors and manually correct if needed

This process is not only time consuming, but labor intensive and leaves room for a lot of errors. It also doesn’t create a complete chain of custody for your plate data. You end up compromising your data integrity.

**In a high throughput lab you cannot follow this process for 100s of plates!**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85309&key=user_uploads/697526/e90e3342-c5e5-4eb7-b5bb-ad4ce911a5ab)

### **Solution**

With Scispot’s AI-powered Plato, the process finally shifts to where it should be: automated. Plate configurations happen at the click of a button, data flows directly into Scispot (ELN/LIMS), and error-checking is automatic. The time saved here isn’t just convenient; it maintains the complete chain of custody. You can also create plates in bulk using Plato while automating the logistics of moving, and transferring data.

Once you have this data in one place called Scispot Labsheets (Scispot data lake), you can then easily run regression or analytics.

As a result, you save a LOT of time while being compliant with 21 CFR Part 11 compliance controls.

<https://youtu.be/4Y009dnwg8Q>

### **Our Ask**

* If you run a Biotech lab, join us for the official launch of Plato this Thursday, 7th November 2024. More details here: <https://lu.ma/uj7djz2b?tk=i4NxSp>
* If you are a YC bio company, you get Plato for free along with 50% off on your first year with Scispot YC deal - <https://www.scispot.com/yc-offer>

## 🧪+🤖 Scibot - AI lab assistant to accelerate your biotech R&D

**tl;dr:** Introducing Scibot, your AI Lab Assistant that supercharges biotech R&D. Simplify experiment design, get real-time insights, and streamline data management—all with natural language commands.

---

### Problems Scientists Face:

* Managing and integrating vast amounts of structured and unstructured lab data.
* Spending too much time on repetitive data entry and analysis tasks.
* Needing quick, reliable assistance while conducting experiments at the bench.
* Difficulty in visualizing complex data relationships and generating actionable insights.

Disconnected lab data is stored across disparate systems, and it is super hard to make it AI-ready.

### Solution: Scibot

**Scibot - Your AI Lab Assistant to Accelerate Biotech R&D**

Four years ago, we launched Scispot, the first ELN + LIMS alternative—a modern data lake that integrates both structured data (experiment metadata, instrument results) and unstructured data (lab notes, protocol deviations). Our goal: create the ultimate Lab Operating System (LOS) for biotech companies.

Now, we’re taking it a step further with Scibot. Leveraging generative AI trained on scientific data and workflows, Scibot enhances your lab operations by:

**1\. Create Your Unified R&D Data Model Using Labsheets:** Standardize your data model based on workflows and data types. Labsheets link entities through relationships, making it easy to manage and visualize data. For instance:

* Create a Labsheet to store and visualize LCMS data.
* Manage cell line stocks with an inventory Labsheet.
* Convert your notebook entries into structured data

**2\. Talk to Your Data:** Interact with your data using natural language. Ask Scibot to summarize key findings or perform complex analyses with simple commands. For example:

* "Summarize the key findings from samples submitted by customer ABC Biotech”
* "Display the heat map for ADME data to identify the best hit molecules based on solubility and permeability."
* "Summarize the key ADME properties of the top-performing compounds from my recent experiments."

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81624&key=user_uploads/697526/025c395c-f3ab-43bc-9570-f452b571307c)

**3\. Get At-the-Bench Assistance:** Scibot offers one-click support for capturing protocol deviations, checking inventory status, tracking samples, and performing calculations—all while your hands and eyes are busy with experiments.

**4\. Generate Real-Time Insights:** Get actionable insights to optimize experiments. Ask Scibot for recommendations based on historical data or to identify trends and patterns. For example:

* "What are the recommended parameters for improving the yield in my protein expression experiments?"
* "Show trends in gene expression levels from my RNA-seq data over the past six months."

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81624&key=user_uploads/697526/4704f337-e098-41af-9770-eb831e984f45)

The real-time insights can be saved as “widgets” so you can create your own dashboard.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81624&key=user_uploads/697526/c50fd70a-dcc7-40ac-8d2f-380f39193255)

**5\. Convert Your Google Sheets, Excel, PDFs, and Docs to Notebook Entries and Registries:** Scibot integrates various data formats into your ELN and LIMS, converting data from Google Sheets, Excel files, PDFs, and Word documents into Labsheets. This centralizes and streamlines data management.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=81624&key=user_uploads/697526/9f113306-0449-4812-b577-4d937ac7105f)

**6\. Maintain your security and privacy while using Scispot AI (Scibot)**

* Customer data never leaves your Scispot instance.
* We do not train any models on customer data.
* Scispot AI upholds all enterprise-grade security and compliance requirements while fulfilling SOC 2 and HIPAA controls.
* Customers can choose to switch off Scispot AI functionalities in their account if they prefer not to use them.

### Ask:

* Join our launch event today - <https://lu.ma/1r5afh0e>
* We’d love to chat if you use any ELN or LIMS system or want to explore new ELN or LIMS for your lab! Reach out at [team@scispot.io](mailto:team@scispot.io) or book a demo directly [here](https://www.scispot.com/demo).
* We’d also appreciate sharing our launch and following us on [LinkedIn](https://www.linkedin.com/company/scispot-com).

## 🚀 Scispot's Lab-as-Code solution: Turn your biotech into an AI powerhouse

Hello YC Community,

We're thrilled to introduce [**Scispot’s Lab-as-Code solution**](https://www.scispot.com/), the best data infrastructure for biotech. Think of it as the Zapier + Snowflake of biotech.

🔗 **Three Pillars of Scispot** 🔗

1️⃣ **Self-Serve Integrations**

* **Problem**: Labs struggle with integrating data from platforms and lab instruments, causing inefficiencies.
* **Solution**: Integrate with Benchling, Snowflake, LabVantage, Veeva, and lab instruments.
* **Real Example**: A client integrated Snowflake, Benchling, and mass spectrometer data, cutting data prep time by 50%.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74769&key=user_uploads/453596/078d26ca-a01d-4978-ac6d-0b6af72167d9)

2️⃣ **Data Readiness for AI**

* **Problem**: Raw data is messy, hindering effective AI applications.
* **Solution**: Staging lakehouse with embedded Jupyter Notebook and R Studio for data cleaning and transformation.
* **Real Example**: A client standardized genomic data, boosting predictive model accuracy by 20%.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74769&key=user_uploads/453596/2f23ec82-b0aa-48d7-8af7-b9429f9200e0)

3️⃣ **API-First ELN & LIMS**

* **Problem**: Traditional ELN and LIMS don't meet modern computational demands.
* **Solution**: Our [API-First](https://docs.scispot.com/) ELN & LIMS add-on is designed for computational teams.
* **Real Example**: A genomics lab automated 80% of workflows using our add-on.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74769&key=user_uploads/453596/151f63ab-ea24-4fcc-86e0-a47f07719880)

Join us in revolutionizing biotech with AI. Let's make science faster, smarter, and more efficient. \
\
You can **book a free consultation call **[**here**](https://www.scispot.com/demo)**.**

## Scispot GLUE - Stitch your biotech R&D data

**Tl;dr:** Scispot GLUE helps Biotech R&D labs extract data from Benchling, Notion, and Airtable, and easily transform it for auditing, visualization, and machine learning.  Scispot started as the world’s most configurable Electronic Lab Notebook (ELN) and Lab Information Management System (LIMS) two years ago for modern biotechs. As we acquired more customers, we learnt that many of them wanted to stitch their data with existing legacy ELN + LIMS, so we decided to launch an extension called Scispot GLUE to sit on top of your existing lab informatics systems and augment them. **Check out more** [**here.**](https://www.scispot.com/scispot-glue)

**Hi everyone, we are Scispotters, the team behind** [**Scispot GLUE!**](https://www.scispot.com/scispot-glue)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70891&key=user_uploads/697526/610d10ec-be64-440c-8046-56f005fe485a)

We’re a team of molecular biologists, computational biologists, data engineers, bench scientists, and biomedical engineers working to solve the data swamp challenge.

**In Biotech R&D, 80% of the generated metadata and data never get fully analyzed or used.** 

* Biotech R&D labs generate vast amounts of metadata and data from various sources, including instruments
* With the current ELN + LIMS landscape, it becomes increasingly difficult to manage, access, and derive insights from data
* As a result, there is a disconnect between wet lab and computational workflows

Scispot GLUE is built to solve this.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70891&key=user_uploads/697526/366fb516-a78b-4b51-951f-1ba54060e2fc)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70891&key=user_uploads/697526/32f45378-ce40-470b-b2dc-8618457afa66)

If this resonates with you, [Schedule a demo](https://calendly.com/scispot/30min?back=1&%3Bmonth=2021-11&month=2023-04) of Scispot GLUE

**Our ask 🙏**

1. Share this post! Many bio companies are facing the data swamp challenge where they struggle to connect their wet lab and computational workflows
2. Connect us with any mid-size biotech companies who have their own ELN and LIMS but want to get the most out of their data
