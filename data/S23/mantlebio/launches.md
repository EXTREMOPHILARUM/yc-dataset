# Launches

## MantleBio - Helping scientists transform data into discoveries

TL;DR: [Mantle](https://mantlebio.com/) makes data engineering easy (and sometimes fun) for scientists.

**Today, we are excited to announce the launch of Mantle’s free plan, now available to the scientific community. Get started **[**here**](https://mantlebio.com/get-started/)**!**

# 💻  Why does biology need better data engineering?

Biotech generates very big, very complex data. A single DNA sequencing experiment can create 7 TB of data, and generating high-throughput multi-modal data is becoming the norm. Recent breakthroughs in computer science and ML have incredible potential to accelerate life science research. 

Electronic lab notebooks (ELNs), like Benchling, help organize research in the wet lab. However, biotech lacks tools to organize and analyze data from instruments, CROs, and public databases.

**Does this sound familiar?**

* Storing experimental metadata in file paths
  * Writing regex scripts to parse metadata out of those file paths
  * Regex scripts break when the file path format changes
* Running bioinformatics scripts locally on a laptop
  * Not being able to process data when the computational scientist is on vacation
  * Losing analyses when the computational scientist loses their laptop on vacation
* Analyzing datasets one by one in a desktop application
  * Not being able to compare data between teams because each person made the graph slightly differently
  * Spending a weekend regenerating all of the graphs consistently, and finding several copy-and-paste errors made on the data that was submitted to the grant application last week

At Mantle, we think science deserves better.

# 🔬 What can you do with Mantle?

**Instant Insights**

Make decisions quickly and confidently. See everything in one place, in real time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82415&key=user_uploads/876391/0e8966ed-9477-45c2-ba61-408feb3884e8)

**Modern Data Management**

Don’t let unscalable spreadsheets and inflexible databases slow down your research. Scientific research requires rapid iteration and experimentation, and Mantle’s data lake can keep up.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82415&key=user_uploads/876391/7aeaa967-f989-4112-9a74-e6b343c4f57a)

**Bring Your Code**

Effectively leveraging computation, data science, and ML separates the next generation of biotech companies from the last. Mantle hosts the infrastructure to help connect no-code users and great-code writers.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82415&key=user_uploads/876391/6f1860f2-4570-4fa1-8a14-b4fea6961f0c)

# 🌎 How does it work?

Mantle is a data infrastructure layer (the “mantle” 🙂 🌎) for biological data analysis.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82415&key=user_uploads/876391/45cbb641-63e7-4475-8f46-35af154abca9)

* **Import** data from ELNs (e.g. Benchling), instruments (e.g. Illumina), CROs, and more
* **Process** data reproducibly with bioinformatics pipelines and Jupyter Notebooks
* In a private **data lake**, find, organize, and analyze data of any type and scale
* **Insights** are accessible to no-code users through real-time visualizations
* **Data Science & ML** results can be easily shared and traced back to raw data

**Why doesn’t biology use “normal” data engineering tools?**

* **The data is different.** General-purpose tools are designed for consistently structured tabular data. Biology generates data with frequently changing metadata in biology-specific formats. _Mantle’s data lake stores data of any scale, format, or type in a single place._
* **The ecosystem is different.** Tools that are not designed for biology don’t prioritize integrations with other tools in the science ecosystem. _Mantle has off-the-shelf integrations with standard life science tools._
* **The processing is different.** Tabular data can typically be processed with simple transformations. Preprocessing genomics data can take dozens of hours and careful parameter tuning. _Custom and off-the-shelf bioinformatics pipelines can be run reproducibly through Mantle, with or without code._

# 👋 Help us close the gap between data and discovery

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82415&key=user_uploads/876391/e731a73f-ecf6-4bc2-b601-ed42ee8fb6a9)

We love data engineering, and we love helping scientists. If you’d like to, here are some ways you can help us:

* **Give Mantle a try!**
  * Get started [here](https://mantlebio.com/get-started/) for free.
* **Let us know what you think!**
  * If you want to chat or see a demo, please reach out to me here: [emily@mantlebio.com](mailto:emily@mantlebio.com)
  * If you would like help debugging a weird AWS error, please reach out to my co-founder here: [madeline@mantlebio.com](mailto:madeline@mantlebio.com) 
  * We are celebrating this launch with a Computation & Biology happy hour at our SF office on August 13. Space is limited; please RSVP [here](https://lu.ma/jraavbdm).
* **Learn with us!**
  * Check out our blogs on [bioinformatics engineering](https://blog.mantlebio.com/p/intro-to-bioinformatics-engineering), [ELNs](https://blog.mantlebio.com/p/eln-breakdown-scale-scope-and-science), and [more](https://blog.mantlebio.com/).
  * Check out our upcoming [workshops and events](https://lu.ma/mantlebio).
* **Share this post!**
  * If you enjoyed reading this, your friends might too 😀

Thank you!

## 🔬 MantleBio: Scaling data driven discovery for biotech

Hi everyone, we’re [Emily](https://www.linkedin.com/in/emily-damato-36932523/) and [Madeline](https://www.linkedin.com/in/madeline-schade/) from [MantleBio](http://mantlebio.com)!

MantleBio is a modern data engineering platform for life science research and computational biology. While software like Benchling helps organize research in the wet lab, MantleBio powers research in the dry lab. Our platform helps biotech companies leverage advances in computational science and machine learning with tools built for biotech.

If you’re a computational biologist or work with biological data we would love to chat. Contact us at [mantlebio.com](http://mantlebio.com) or [info@mantlebio.com](mailto:info@mantlebio.com).

### The Problem

Biotech generates a tremendous amount of data. High-throughput sequencing and screening have become the norm, R&D groups can generate terabytes of data per day, and biotech is estimated to have the largest volume of data of any industry by [2025](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002195).

Recent breakthroughs in computer science and machine learning have the opportunity to profoundly impact scientific research. However, the majority of biotech companies lack the tools or software team necessary to fully utilize these advances and the data they have.

Without implementing the best data practices, biotech companies are often unable to find past results, reproduce analyses, or integrate multiomic datasets. This can be a bottleneck for future experiments and jeopardize regulatory filings. Meanwhile, generic data management software fails to address the complexities specific to life science. MantleBio bridges this gap, accelerating data driven discovery with tools built for biotech.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72941&key=user_uploads/1435929/28c97902-c13b-461a-917e-17858a41d971)

### Our Solution

* Simplify multiomics with centralized data management.
  * Other systems require scientists to design their own schemas. We collaborate with experts to create domain-aware data models available off the shelf.
  * Our API, CLI, and UI make datasets easily accessible to no-code users and computational scientists.
* Automate the analysis of routine workflows. Start a DNA sequencing run, grab coffee, and receive the results in your inbox.
  * We connect to Benchling, Notion, BaseSpace and other systems to read experimental data from the source. Our API and data transformation pipelines allow custom integrations with even the most difficult laboratory instruments.
* Create bioinformatics pipelines in minutes, not days.
  * Computational biologists can create production pipelines directly in MantleBio without managing cloud infrastructure or writing Docker files.
* Prepare for the next IND filing or FDA audit with reproducible datasets and analyses.
  * MantleBio automatically records a version history for all datasets. The platform captures inputs, processing, and outputs of all analyses, creating a connected and auditable graph of everything in the computational lab.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72941&key=user_uploads/1435929/c5949154-a9ed-49a9-9fa5-37c572dc06ad)

## About Us

Madeline is a software engineer with experience as a full-stack engineer at multiple biotech companies and at Google working on large data pipelines. At GRAIL she developed an EDC that supported one of the largest clinical trials ever performed (over 200k patients), and at Google worked on a system supporting 10 billion queries per day. She studied computer science and computer engineering at UC Santa Cruz, where she did research in large distributed systems.

Emily is a “full-stack computational biologist”. Her software experience includes back-end, full-stack, and machine learning. She has done biology research at MIT in both the wet lab and dry lab, and in industry has worked in drug discovery, cell therapy, diagnostics, molecular dynamics simulations, and patient health records.

Emily and Madeline met while working as software engineers at GRAIL, a cancer diagnostic company. From there they both went to Arsenal Bio, a cell therapy company. They realized these biotech companies had common data management needs, but there was no common tool available. They started MantleBio to make the best data engineering practices accessible to all life science research.

### Want to learn more?

Contact us at [mantlebio.com](http://mantlebio.com) or [info@mantlebio.com](mailto:info@mantlebio.com).

We love helping scientists. If you have questions about your current data practices (e.g.“will this scale?”) we also do free data infrastructure reviews.
