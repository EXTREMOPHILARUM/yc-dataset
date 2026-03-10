# Launches

## Anto Biosciences: A Foundation Model for Microbial Communities

We’re [Arvid](https://www.linkedin.com/in/arvid-gollwitzer/) and [David](https://www.linkedin.com/in/daviddegruijl/), and we’re building [Anto Biosciences](https://www.linkedin.com/company/anto-biosciences).

### tl;dr

Anto is building a multimodal foundation model for microbial communities, making the gut microbiome computable for the first time. We predict drug toxicity and efficacy across diverse populations and optimize molecules for universal efficacy — addressing the microbiome-driven causes of drug response and failures.

**Launch Video**: https://youtu.be/BDPp2wXiDbw

### The Key Problem

**We caught a cancer drug that worked in China but failed in U.S. trials. Same molecule, different microbiomes. $1B lost.**

This isn't an isolated story; more than a billion people are currently on medications where the microbiome dictates success or failure. The gut microbiome drives drug toxicity and efficacy, but pharma lacks the tools to understand and act on it \[10,11,13\]. Current methods to simulate the gut take months, cost millions, and rely on animal models that are too different from humans to be useful.

### About Anto

**We predict drug toxicity and efficacy across diverse populations and optimize molecules for broader efficacy—addressing the hidden, microbiome-driven causes of drug response and failures.**

Input any drug molecule. We tell you how people will respond. We show where it works and where it fails—by geography, age, or diet.

We predict:

* Population-specific efficacy (geographic, age-based, vegans vs. meat eaters, etc.)
* Failure mechanisms (specific microbial metabolic pathways) \[9,11\]
* Treatment response profiles across diverse populations \[10,14\]

And we don't just flag risk; we identify failure mechanisms down to microbial metabolic pathways and generate treatment response profiles across populations. Then we optimize the molecule for broader efficacy. Turning 20% efficacy into 80% becomes an optimization problem we can actually solve.

**Why we can do this:** We've pioneered quality-aware, goal-directed sparsification algorithms \[5,9,15\]. Microbiome data is 99% noise. We remove most of the noise and low-quality data through sparsification, leaving only the 1% that actually carries predictive power. That's how we make the microbiome computationally tractable. \[6,7,8,14\].

### About Us

[Arvid](https://www.linkedin.com/in/arvid-gollwitzer/) — Broad Institute of MIT and Harvard, ETH Zurich. Nature-published researcher who pioneered microbiome sparsification. Built the methods that make noisy microbial data tractable.

[David](https://www.linkedin.com/in/daviddegruijl/) — ex-ETH Zurich, J&J, BWH, Harvard Med, Gastroenterology. Struggled with current drug digestion models firsthand. Knows where current workflows break and how to fix them.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95292&key=user_uploads/89898/3b2d64c2-dbc0-4bad-aad7-40b7995faeca)

We’re second-time founders who have lived this problem and published at leading AI conferences and Journals.

### Traction

We're working with pharma R&D to simulate drug–microbiome interactions and de-risk cross-border deals with population-specific efficacy predictions and response profiles. Our open-source tools and research \[1-9,14,15\] are widely adopted and taught in engineering and computational biology programs \[16\].

### What This Means for Digital / Computational Biology

**The microbiome is the missing layer in drug development.** Most orally administered drugs are modified by gut bacteria before reaching their targets. We're making this layer computable for the first time \[11-14\].

If you're building in digital biology, precision medicine, or drug development, let's talk. The microbiome affects everything.

### Our Asks

If you’re in drug development, cross-border deals, or translational medicine, we’d love to learn what microbiome requirements matter most to you. If you know teams in pharma and believe this product is cool, sharing / intros would mean a lot.

If you are in academia or microbiome research, try out our open-source tools \[5-15\]!

**Get in touch**: [founders@anto.bio](mailto:founders@anto.bio) | [anto.bio](https://www.anto.bio/)

### Our Research

Our foundational work spans high-performance genomic analysis \[1-4\], metagenomic classification algorithms \[5,9,14,15\], in-storage computing for microbiome data \[6-8\], and the first large-scale datasets for causal modeling of microbial ecosystems \[11,12\]. We've pioneered techniques that make microbial communities computationally tractable, including quality-aware sparsification that reduces noise by 99% while preserving predictive power \[5,9,15\]. Our recent work on therapeutic resistance \[10\] and AI-controlled metagenomics for clinical applications \[14\] directly informs our drug optimization capabilities.

**References:**

\[1\] N. M. Ghiasi et al., "GenStore: A high-performance in-storage processing system for genome sequence analysis," in _Proc. 27th ACM Int. Conf. Architectural Support for Programming Languages and Operating Systems_, 2022, pp. 635-654.

\[2\] N. M. Ghiasi et al., "GenStore: In-storage filtering of genomic data for high-performance and energy-efficient genome analysis," in _2022 IEEE Computer Society Annual Symposium on VLSI (ISVLSI)_, 2022, pp. 283-287.

\[3\] N. M. Ghiasi et al., "GenStore: A high-performance and energy-efficient in-storage computing system for genome sequence analysis," _arXiv preprint arXiv:2202.10400_, 2022.

\[4\] M.-D. Rumpf, M. Alser, A. E. Gollwitzer et al., "SequenceLab: A comprehensive benchmark of computational methods for comparing genomic sequences," _arXiv preprint arXiv:2310.16908_, 2023.

\[5\] A. E. Gollwitzer et al., "MetaTrinity: Enabling fast metagenomic classification via seed counting and edit distance approximation," _arXiv preprint arXiv:2311.02029_, 2023.

\[6\] N. M. Ghiasi et al., "MetaStore: High-performance metagenomic analysis via in-storage computing," _arXiv preprint arXiv:2311.12527_, 2023.

\[7\] N. M. Ghiasi et al., "MetaStore: High-performance metagenomic analysis via in-storage computing," _arXiv e-prints_, pp. arXiv-2311, 2023.

\[8\] N. M. Ghiasi et al., "MegIS: High-performance, energy-efficient, and low-cost metagenomic analysis with in-storage processing," in _2024 ACM/IEEE 51st Annual Int. Symp. Computer Architecture (ISCA)_, 2024, pp. 660-677.

\[9\] A. Gollwitzer et al., "MetaFast: Enabling fast metagenomic classification via seed counting and edit distance approximation," _arXiv preprint arXiv:2311.02029_, 2023.

\[10\] A. E. Gollwitzer, D. A. Subramanian, I. Tucker, and G. Traverso, "Steering the evolutionary game: Hierarchical control of therapeutic resistance in cancer treatment," in _NeurIPS 2025 AI for Science Workshop_, 2025.

\[11\] A. E. Gollwitzer, D. A. Subramanian, I. Tucker, and G. Traverso, "MetaOmics-10T: The foundational dataset to unlock causal modeling of microbial ecosystems," in _NeurIPS 2025 AI for Science Workshop_, 2025.

\[12\] N. M. Ghiasi et al., "MegIS: High-performance, energy-efficient, and low-cost metagenomic analysis with in-storage processing," _arXiv preprint arXiv:2406.19113_, 2024.

\[13\] H. J. Haiser and D. de Gruijl, "Emerging tools and technologies for microbiome-aware drug development," _Clinical Pharmacology & Therapeutics_, 2025, doi:10.1002/cpt.70026.

\[14\] A. Gollwitzer et al., "AI-controlled metagenomics: High-throughput taxonomic profiling for clinical pathogen detection and early-stage cancer screening and type classification," _arXiv preprint arXiv:2311.02029_, 2025.

\[15\] A. Gollwitzer et al., "The Thinking Microscope: A reinforcement learning framework for the co-optimization of computational and generative data sparsification in metagenomics," _arXiv preprint arXiv:2311.02029_, 2025.

\[16\] A. E. Gollwitzer, "Decoding the human microbiome through AI-controlled metagenomics: Promises and ethical implications," presented at ETH Zurich ETHix Series, Dec. 2024. \[Online\]. Available [here](https://bioethics.ethz.ch/news-and-events/news-bioethics/2024/12/decoding-the-human-microbiome-through-ai-controlled-metagenomics-promises-and-ethical-implications.html).
