# Launches

## MICSI-PET: Anatomical Positron Emission Tomography

TLDR; MICSI-PET makes PET imaging fast, anatomical, and scalable for Alzheimer’s care.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96226&key=user_uploads/1352304/a5488138-be4b-4093-86c1-1b2663488117)

**Problem:** **PET is the bottleneck capping the entire Alzheimer’s market.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96226&key=user_uploads/1352304/40ba7516-1b46-454a-9a26-98fb91fe3169)

Disease modifying Alzheimer’s drugs like Leqembi and Kisunla are here, and they are projected to generate $5-8B/year by 2030. However, to get these drugs, patients need a positive amyloid PET scan.

This is an ambitious figure that is limited by the fact that there are only 2500 PET/CT scanners in the US, where the average age is 14 years old. PET scanners have a predictable 4-5% drop in sensitivity (or detected count rate) per year \[Watanuki et al. Ann Nucl Med. 2010\], suggesting a loss of half of the sensitivity since its initial install. Operationally, this sensitivity loss forces centers to lengthen acquisitions or increase dose just to preserve image quality, reducing throughput or margins right as amyloid PET demand is exploding. It’s also unrealistic to assume that the existing PET fleet is built for imaging Alzheimer’s at scale. PET systems are also heavily utilized for oncology, cardiology, infection, and presurgical planning, where 74% of all PET scans use FDG, a general purpose tracer for cellular metabolism. 

**Solution: Transform aging PET fleets into Anatomical PET with MICSI-PET.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96226&key=user_uploads/1352304/be3b873c-3dd7-4326-8447-316161d179db)

MICSI-PET is a turnkey upgrade that dramatically enhances PET image quality by using the MRI as an anatomical guide. This process does not require any additional imaging as all patients should have received an MRI prior to amyloid PET imaging. Operationally, this upgrade removes the primary barrier for scaling Alzheimer’s therapies by (1) enabling high-end PET imaging on low-end or aging PET scanners; (2) enabling shorter PET examinations leading to greater throughput; (3) minimizing ambiguity of positive/negative amyloid PET imaging by showing clearer boundaries between gray and white matter:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96226&key=user_uploads/1352304/90dd7722-405d-4a4f-967b-4ec6df183ff6)

**Figure:** Coregistered conventional PET and MICSI-PET amyloid images across a range of amyloid burdens, highlighting differences in apparent cortical sparing: **left, amyloid-negative** with strong gray/white contrast; **right, amyloid-positive** with reduced gray/white contrast.

**Addressing the Radiologist Workforce Crisis:** Scaling Alzheimer's care isn't just a hardware problem; it's a workforce problem. AD imaging is about to become a high-volume modality layered onto a nuclear medicine workforce where 54% of radiologists already report burnout.

Beyond anatomical PET, MICSI-PET is designed to streamline diagnosis through automatic SUVR/Centiloid reporting with built-in QC.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=96226&key=user_uploads/1352304/b48c9a16-d7b6-4fe9-bf74-509653e159dd)

Fast and anatomical PET is just the start. The same MR-guided upgrade would generalize across tracers, and eventually across doses, elevating the global standard of PET toward a new default: molecular imaging that’s both specific and anatomically precise. 

Our first product, MICSI-RMT, is already FDA-cleared and in the market. MICSI-PET is currently in clinical validation and we are preparing our FDA submission.

**Ask:** We are expanding pre-FDA clearance pilot collaborations to validate MICSI-PET across sites and workflows, and we are closing a seed extension to support multi-center validation and early installs. If you lead a PET imaging program or invest in medical imaging and Alzheimer’s care, we would love to connect.  

**Email Us:** 

[**Gregory.Lemberskiy@micsi.com**](mailto:Gregory.Lemberskiy@micsi.com)

[**Benjamin.Adesaron@micsi.com**](mailto:Benjamin.Adesaron@micsi.com)

## MICSI (Microstructure Imaging)

TLDR; MICSI is introducing an innovative image processing algorithm to decrease MRI scan time, increase image resolution, and unlock new diagnostic capabilities using Microstructure Imaging.

![](https://lh4.googleusercontent.com/166C-4hbfRCmiC20D9EbOVhdubPqEE3tuTb-ZvNh8bnOXts8Rf9ZfhssNQ8ptJsGYAFqtkSt6w9Cu-aRvnBDBoKesDzc1ou7ddUVUZqTZ0knq8MmlZsbLWYY4rpGoFqUmrbmjEeSjfMx7KMKRdEngWA)

**Problem: MRI Centers are overbooked.**

If you've ever had an MRI, you've probably waited weeks for an available slot and then spent a long time in the scanner. These long scan times inconvenience patients, create hospital backlogs, and delay appointments. Delays like these can critically impact conditions that require prompt diagnosis and intervention, inflate healthcare costs, increase patient anxiety, and potentially compromise treatment strategies. Why the wait? An MRI of the whole brain can be acquired in [**seconds**](https://mriquestions.com/echo-planar-imaging.html)!

**Compromise: Why is your MRI an hour long?**

Most of the scan time is spent on preserving signal-to-noise ratio (SNR) to produce images of the highest quality. These standard SNR preserving methods include:

* Line-by-line acquisitions: These are fax-machine-like acquisitions that read the image one line at a time, where the time spent on each line is equivalent to the time that could have been spent acquiring the whole image.
* Averaging: To boost SNR, images may be reacquired and averaged together. However, SNR improves slowly as a square root of scan time (ie 4 images are required to double the SNR).

An additional compromise is related to the spatial resolution, since MRI is acquired in 3D with “voxels”, doubling the resolution in each dimension from (2x2x2 mm3 to 1x1x1 mm3) would require the SNR to increase by **8x**, which even after 50 years of innovation, seems near impossible.

![](https://lh4.googleusercontent.com/y1p1DzihqAvnmKvtoSJAbVSBrInECVUP2GvzVc5TFmLNqwTQ1hevnLgcPX7iplxNhKchrjAAQq8L8WlPbLNVWX31jAN-VIg6dSJ7Nzv-lKMUTvy8xsUIlzfFOZLlgSoGL0ZAC1lk8xqtYL2V4Q1caJk)

**The MRI exam is full of compromise.**

* Long scan times means fewer patients can be scanned by a given radiology center.
* Lower resolution means a compromise in anatomical accuracy, where pathologies that could have otherwise been detected at an earlier stage would need to progress further to be MR visible.

We believe that the ultimate compromise is that MRI is not being used to its fullest potential for microstructure imaging, where MRI could be used to [**image cellular properties non-invasively**](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/nbm.3998).

**Solution: Boosting SNR over the MRI exam using MICSI-RMT.**

Our patented approach (pending FDA510k clearance in Q4-2023) uses a self-supervised AI method to learn the noise properties of the MRI exam and remove noise uniformly across all images of the dataset. Our algorithm, MICSI-RMT, can be described as a smart averaging approach, whereby many images of the MRI exam are combined while preserving their unique image properties and discarding the noise. This boost in SNR would be approximately, sqrt(M/P), where M is the number of images included in the dataset, whereas P describes how different the images are (physical properties: proton density, T1, T2, diffusion, etc + artifacts: motion, errors, etc).

MICSI-RMT is the commercial implementation of the MP-PCA algorithm that was developed by our research group led by Drs. Dmitry S. Novikov and Els Fieremans of NYU Radiology’s Center for Biomedical Imaging.

MP-PCA is the most popular denoising approach in the MRI community:

* The [**original paper**](https://pubmed.ncbi.nlm.nih.gov/27523449/) introducing the approach has achieved over 1300 citations since November 2016.
* Denoising of [**task-based FMRI**](https://pubs.rsna.org/doi/full/10.1148/radiol.2020200822) for presurgical planning of Neurosurgery
* Enabling low field [**0\.55T prostate diffusion**](https://pubmed.ncbi.nlm.nih.gov/37222526/) MRI

With MICSI-RMT, MRI centers will not only be able to provide higher quality imaging but also drastically reduce the scan time (up to [50%](https://pubs.rsna.org/doi/full/10.1148/radiol.2020200822)). This improved efficiency allows centers to scan more patients per day, enhancing their operational capacity and throughput. Financially, this increase in capacity translates into a significant boost in revenue for every MRI center. By doubling the number of patients scanned daily, we estimate an additional $2 million in annual revenue per MRI scanner. Furthermore, the improved image quality and resolution could lead to more accurate diagnoses, early disease detection, and reducing overall healthcare costs in the long run.

**Who we are - Greg and Ben**

![](https://lh6.googleusercontent.com/F5FGyVn85R_Oxvkgw_uEOhvkKUEg_2VemnSso8p1nBfc7vgYVd1q1Vnt2BgIJrm2CRenojq9RkwoxbuP0lebYfKIcs6anX6wQEPQj0T-yaTJGLBOvqqzsw4JL4ftzrHLozX-QX592SesWUotkt92ZCw)

We are scientists and engineers who have spent the last decade developing machine learning software to both improve the quality diagnostic utility of MRI. [**Gregory Lemberskiy, PhD**](https://www.linkedin.com/in/gregory-lemberskiy/) is an [**experimental physicist**](https://scholar.google.com/citations?user=_TvugCIAAAAJ&hl=en). He discovered how to use MRI to measure the diameter of the [**prostate glandular lumen**](https://www.frontiersin.org/articles/10.3389/fphy.2018.00091/full), which may obviate the need for tissue biopsy to detect prostate cancer progression. [**Benjamin Ades-Aron, PhD**](https://www.linkedin.com/in/benjamin-aron-b0313349/) is an [**electrical engineer**](https://scholar.google.com/citations?user=xNhHFuAAAAAJ&hl=en) who developed and deployed the [**DESIGNER**](https://pubmed.ncbi.nlm.nih.gov/30077743/) open-source image processing pipeline, which is the global gold standard of diffusion MRI image processing. He has also developed a number of novel neural network architectures to aid in the denoising of compressed sensing MRI data, to facilitate brain mapping for functional neurosurgery of Epilepsy and brain tumor.

Together, the MICSI team owns over a dozen approved patents and has a clear vision for the future of MRI. The goal of MICSI is to use our patented denoising and parameter estimation technologies to make MRI quantitative and reproducible for the first time, creating a new category in diagnostic healthcare and improving patient satisfaction and outcomes.

**Our Ask**

* Do you know anyone in private practice, hospitals, or in large academic centers who may be interested in our approach? We want to talk to them.
* Questions, comments, feedback? We want to hear from you!

**Email us:**

[**Gregory.Lemberskiy@micsi.com**](mailto:Gregory.Lemberskiy@micsi.co)

[**Benjamin.adesaron@micsi.com**](mailto:Benjamin.adesaron@micsi.co)
