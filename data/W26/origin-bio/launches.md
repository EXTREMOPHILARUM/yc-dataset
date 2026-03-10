# Launches

## Origin - Safer Cell & Gene Therapies with AI

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97480&key=user_uploads/552024/dd558bc0-b110-466f-b603-d3acb473ba54)

Hey everyone!

We’re Yash and Malhar from Origin.

**TL;DR**

* Using AI to make cell & gene therapies **safer** by designing **DNA switches and dials**.
* Our model’s synthetic regulatory sequences program precise gene expression patterns in disease cells.
* We’re building the **largest** **proprietary dataset** consisting millions of experimentally validated regulatory DNA sequences across many different cell and tissue types.
* Our model **outperforms Google DeepMind’s AlphaGenome** at predicting regulatory element activity.

<https://youtu.be/jCN43gOy7x8?si=pkZU6sGREgiI-EHA>

**The Promise**

Cell and gene therapies have successfully been used to treat diseases like stage IV leukemia, retinal disease, and spinal muscular atrophy. However, their application is limited due to concerns around safety and efficacy. But this drug class holds the promise of being a **durable cure** for diseases like cancer, autoimmune, neurodegenerative, aging, and more.

**The Problem**

Toxicity events largely arise due to our inability to control **where**, **when,** and to **what** extent genes are turned on. Regulatory DNA sequences - enhancers and promoters - function to modulate the expression of genes. Current approaches to design these sequences involve naive methods like repeats of known motifs (patterns) and random ligation. These methods either **reliably yield poor candidates** or require **brute force to search** for even one promising hit.

<https://youtu.be/SDJFAJULTP0?si=IYXFHLAqU88CcaXK>

**Our Solution**

Axis – our state-of-the-art model – is trained to design and screen regulatory DNA to activate therapeutic genes in target disease cell-states.

Axis is able to rapidly sample **millions** of functional candidates when prompted by the cell-state. We’re currently testing these sequences in the lab to produce the **largest proprietary dataset** of synthetic regulatory elements, measuring their interaction with transcription factors and the phenotypic outcomes of gene expression.

**Axis’ sequences have the highest predicted expression in targeted cell types**

Using Malinois, an independent and in-vitro validated prediction model by the Broad Institute, we observed that Axis’ generated sequences had the highest transcriptional activity in the cell type they were prompted by.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97480&key=user_uploads/552024/deb58343-aec7-4554-a176-d4ff1927da9f)

**Axis’ sequences contain known biological features**

Regulatory DNA sequences are activated when proteins called transcription factors bind to them at specific patterns of ATGCs known as motifs.

HNF4A is a known master regulator of hepatocyte and liver gene expression. We observed that in the generated sequences, its known motif most frequently occurred in HepG2 (liver cell line) targeted sequences.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97480&key=user_uploads/552024/d4e9dc1a-47c7-4599-99f3-f0b4d8980c6a)

**Axis’ sequences have high diversity and explore a large design space**

Over 72% of our generated sequences have no BLAT alignment match up amongst themselves (using a 20bp threshold).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97480&key=user_uploads/552024/45c66f66-c144-46ac-aea9-2739e6aae6d9)

**Axis outperforms Google DeepMind’s AlphaGenome**

Axis demonstrates strong performance in predictive benchmarks measuring molecular properties of real regulatory sequences. These include measures like chromatin accessibility and transcription factor protein binding.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97480&key=user_uploads/552024/f1b68778-ea47-44b1-a2fc-ee4ac39c25bf)

**The ask:**

If you know or are someone working on partnerships at pharmaceutical / biotech companies working in cell & gene therapies, reach out to explore:

* Partnering on regulatory sequence designs for target disease cells.
* Getting access to our proprietary dataset of sequence properties, sequence-protein interactions, and cell-state perturbations.

\
Feel free to reach out via email at [yash@origin.bio](mailto:yash@origin.bio)
