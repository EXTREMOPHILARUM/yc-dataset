# Launches

## Strand AI - The Data Layer for Biology.

We're Yue and Oded, the founders of Strand AI ([strandai.com](http://strandai.com)).

## TL;DR

Strand AI develops foundation models that generate missing bio-data about patients. With this imputed data, pharmaceutical companies can select better patients for their drug trials and shave months from their drug launch timelines. We’ve already trained a multimodal foundation model that integrates spatial biology modalities, beating SOTA, at a fraction of the cost.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98178&key=user_uploads/1489450/cc2b35d7-9723-496f-a8c8-694e3da64100)

## The Problem

Every year, $60-100B is invested into clinical trials that do not result in approved therapies. 9 out of 10 drug trials fail. These drugs work by targeting specific biological pathways, but not every patient has the same pathways active. When a trial can't tell who has what, responders get diluted by non-responders, the effect washes out, and the trial fails. The key to selecting the right patients is multimodal data: genomics, RNA, proteins, imaging, clinical outcomes. But for any given patient, most of this data is missing. You might have their RNA expression but no pathology slides. Their genomics but not their clinical outcomes. The full picture is never there.

Yue saw this firsthand. Before starting Strand AI, he was building foundation models on the largest patient dataset in existence, working directly with the founders of Tempus AI. Whether predicting patient drug response, modeling disease progression, or finding new mechanisms of action, every task hit the same wall. Even with the largest dataset in existence, there simply wasn't enough to make good predictions.

The easy answer is "collect more data." But multimodal patient data is expensive, invasive, and often impossible to get. Patients drop out of trials, skip evaluations, or are part of rare populations where the data simply doesn't exist.

## Our Insight

The good news is that there's enough paired data across modalities that the missing biology can be intelligently and accurately predicted from what's already there. Strand AI builds cross-modal prediction models that take what you already have and predict what you don't.

We can efficiently evaluate which modalities we're able to predict accurately for a given dataset, so teams know exactly where we can fill gaps and when new measurements are needed. This lets pharma and biotech teams take their incomplete clinical cohorts and unlock precision that would otherwise be locked behind missing data.

<https://youtu.be/VUkR15k8X1E>

## What We've Built

We recently trained from the ground up a foundation model that predicts spatial proteomics from routine H&E staining. It beats state-of-the-art and we did it in under 6 weeks, at a fraction of the cost of comparable efforts. We were able to achieve this due to our deep, hands-on experience with both the data and the infrastructure. We’ll be deploying this model at scale for pharmaceutical and biotech companies to enrich their patient data.

## About Us

Before Strand AI, we worked shoulder-to-shoulder at Enable Medicine, where we built the platform for petabyte-scale multimodal spatial biology data — single-cell resolution imaging, spatial transcriptomics, spatial proteomics, and clinical metadata — all linked at the patient level. We indexed, analyzed, and served the largest spatial biology datasets in existence. That work gave us an unusually deep understanding of what multimodal biological data actually looks like at scale — what's missing, what's noisy, and what it takes to make it useful.

Oded has been programming since he was 8. At Enable Medicine, he led product to build the spatial biology platform end-to-end.

Yue previously worked at Yoshua Bengio's Element AI, Microsoft Research, and Pathos, a Tempus AI initiative, where he built foundation models on the largest multimodal patient dataset in existence. He's built and managed ML infrastructure at scale, including clusters of thousands of GPUs.

We know how to train large models efficiently, and it shows in our costs and timelines.

## Our Ask

We're looking for introductions to decision makers at pharma and biotech companies running clinical trials. If you know someone who wants to find better biomarkers, stratify patients more precisely, or catch signals they're currently missing, we can help. When a trial fails, it's not just years and capital lost, it's patients who were counting on that treatment. Better data means better patient selection, and drugs that reach the people who need them.

reach us at [founders@strandai.com](mailto:founders@strandai.com)
