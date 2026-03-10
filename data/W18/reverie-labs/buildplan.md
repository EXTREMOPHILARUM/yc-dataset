# Build Plan: Reverie Labs 2026

## Overview

By 2026, Reverie becomes a specialized AI chemistry platform for mid-size biotech — not a drug developer. The target: computational chemistry teams at Series B+ oncology companies who need to compress kinase inhibitor design cycles from 18 months to 90 days. The insight that makes this work now is structural: pharma's internal AI/ML teams have matured enough to become real buyers, and they're actively shopping for tools that integrate wet-lab feedback loops, not theoretical models.

The platform wins by closing the synthesis-assay-model cycle in days through automated chemistry integration (Emerald Cloud Lab, Chemspeed) and a proprietary training corpus built from DNA-encoded library screening. This generates millions of binding affinity data points per campaign — something no off-the-shelf generative chemistry tool can match. The go-to-market is direct sales to computational chemistry leads who already have budget authority and understand the ROI of faster iteration.

This is a $50–150M TAM business, not a $5B pharma software play. It's built for teams that exist now, not markets that need to be created.

## Why Now?

The single most important change since Reverie's failure is structural, not technological: large pharmaceutical companies have built internal AI/ML organizations with real software procurement budgets. Pfizer, AstraZeneca, and Novartis each publicly committed more than $1 billion to AI R&D between 2022 and 2024. These commitments created dedicated teams — with headcount, infrastructure budgets, and vendor evaluation processes — that did not exist when Reverie was selling software in 2017–2018. Gupta's post-mortem identified the TAM as "double digit millions" because pharma didn't buy software; that calculation is now empirically out of date. The buyer has changed.

The technological stack has also shifted in ways that make the underlying platform dramatically more capable. AlphaFold 2 (July 2021) and AlphaFold 3 (May 2024) made near-instantaneous protein structure prediction essentially free, eliminating months of target characterization work that previously preceded hit generation. Diffusion-based generative chemistry models — DiffSBDD, RFDiffusion (October 2022) — now produce synthetically accessible, property-optimized candidates at a scale that was computationally impossible during Reverie's active years. Together, these tools compress the pre-hit and lead generation phases from months to days.

The data generation bottleneck — which forced Reverie to depend on customers' proprietary datasets, creating both a sales friction and a model quality ceiling — has a credible solution in 2026. DNA-encoded library (DEL) screening can now produce millions of binding affinity data points for under $500,000, according to published benchmarks. A new company can intentionally generate its own training corpus rather than waiting for pharma to share theirs.

On the regulatory side, the FDA's 2023 FDORA legislation explicitly permits IND submissions supported by computational and organoid evidence without mandatory animal data, reducing the preclinical cost and timeline that made Reverie's drug-developer pivot so capital-intensive. This matters for the rebuild not because the new company will develop drugs, but because it lowers the cost of generating the clinical-stage validation data that makes the platform credible to pharma buyers.

Automated chemistry platforms — Chemspeed, Emerald Cloud Lab — now allow hundreds of parallel synthesis-and-assay cycles per week at CRO cost structures, addressing the experimental feedback loop bottleneck that Reverie's no-lab model struggled to close. The synthesis-to-assay-to-model iteration cycle that took Reverie months can now run in days.

---

## Current Market Analysis

**Market size:** The pharma AI software market is difficult to size precisely with public data, and any figure here should be treated with appropriate skepticism. Estimates from analysts (Grand View Research, MarketsandMarkets) place the AI in drug discovery market at $1.5–4 billion in 2024, growing at 30–45% CAGR — but these figures conflate software tools, platform companies, and integrated drug developers in ways that obscure the addressable market for pure infrastructure software. The more relevant signal is behavioral: Pfizer's $1B+ AI commitment, AstraZeneca's partnership with Recursion (announced 2023, $1.2B deal), and Novartis's internal AI center of excellence each represent procurement events that did not exist in 2018. The enterprise software TAM for pharma AI infrastructure is larger than Reverie's original estimate, though by how much is genuinely unknown.

**Competition map:** The current competitive landscape has three meaningful clusters.

*Integrated AI drug developers* — Recursion Pharmaceuticals (NASDAQ: RXRX), Exscientia (acquired by Recursion, 2024), Insilico Medicine — are building proprietary pipelines and licensing platforms simultaneously. Their weakness is that their platform businesses are subordinate to their pipeline narratives; pharma buyers evaluating them as software vendors are also evaluating them as pipeline competitors. This creates a structural conflict of interest that a pure infrastructure play avoids.

*Point-solution chemistry tools* — Schrödinger (NASDAQ: SDGR), OpenEye (acquired by Cadence), Chemical Computing Group — sell established computational chemistry software with deep pharma penetration. Their weakness is that their models are largely physics-based and do not improve from proprietary experimental data; they cannot offer the compounding data flywheel that a DEL-trained generative model provides.

*Foundation model entrants* — Isomorphic Labs (DeepMind spinout), Xaira Therapeutics (launched 2024 with $1B) — are building general-purpose biology foundation models. Their weakness is that they are targeting the same integrated drug developer model that failed Reverie, just with larger balance sheets. They are not selling infrastructure to pharma's internal teams; they are competing with those teams.

**Demand signals:** AstraZeneca's $1.2B Recursion partnership, Sanofi's $1B Insilico deal, and Pfizer's internal AI platform investments all signal that large pharma is willing to pay for external AI capability — but the deal structures favor platform access and co-development over pure software licensing. A company that sells infrastructure enabling pharma's internal AI teams to build better models — rather than competing with those teams — occupies a gap none of the above competitors address.

**Defensibility:** The honest answer is that this is not a platform-proof business. Schrödinger, Cadence, and large cloud providers (AWS HealthLake, Google Cloud Life Sciences) all have adjacent products. The structural defense is not technical moat but data moat: a company that generates proprietary DEL screening data and trains models on it accumulates an asset that cannot be replicated by a cloud provider adding a feature. The compounding nature of experimental data — each synthesis cycle improves the model, which improves the next cycle — creates a flywheel that is slow to start but durable once established. This is a real but not impenetrable defense, and founders should be clear-eyed that it requires three to five years of consistent data generation to become meaningful.

---

## Recommended MVP

### Core Feature 1: DEL-Powered Proprietary Training Corpus

The platform generates its own binding affinity training data through DNA-encoded library screening, producing millions of data points per campaign for under $500,000. This directly addresses Reverie's original dependency on customers' proprietary data — which created a chicken-and-egg problem where the platform needed data to be useful, but customers wouldn't share data until the platform was proven. The new company owns its training data from day one, enabling model quality that is demonstrable before the first enterprise sale. Unlike Reverie's customer-data-in-VPC approach, this corpus is a company asset that compounds with each campaign.

## Core Feature 2: Kinase-Selective Generative Chemistry Module

A diffusion-based molecular generation system (building on RFDiffusion-class architectures, available as of October 2022) fine-tuned specifically on kinase inhibitor chemistry, with explicit optimization for selectivity profiles and blood-brain barrier penetrance. Kinase inhibitors remain the most commercially validated target class in oncology — BTK, CDK4/6, and KRAS inhibitors all received FDA approval between 2020 and 2024 — confirming that Reverie's biological thesis was correct. The MVP does not attempt to generalize across all target classes; depth in kinases is the defensible starting position, and breadth can be added after the data flywheel is established.

## Core Feature 3: Automated Synthesis-Assay-Model Feedback Loop

Integration with Emerald Cloud Lab or Chemspeed automated chemistry platforms to close the synthesis-to-assay-to-model iteration cycle in days rather than months. This directly addresses the ADMET optimization bottleneck that Gupta identified as the primary timeline driver — "months to years per program." The loop runs continuously, with each experimental result updating model weights and reprioritizing the synthesis queue. Unlike Reverie's CRO-dependent model, the automation layer provides a controlled, high-throughput feedback mechanism that the company owns and can optimize.

**What we will NOT build:** A proprietary drug pipeline. The rebuild explicitly avoids the pivot that destroyed Reverie's venture economics. No IND filings, no clinical programs, no pipeline assets. The company sells infrastructure, not molecules.

**Success metrics:** 3 enterprise pharma customers with contracts exceeding $500K annually within 18 months of launch; model performance demonstrably superior to Schrödinger's physics-based baseline on at least two published kinase selectivity benchmarks; synthesis-to-model feedback cycle under 72 hours for standard assay panels.

**Network effects / cold-start:** This product does not depend on user network effects or local density. Value is delivered to each pharma customer independently through model quality and data generation throughput. The cold-start risk is model quality before sufficient DEL data is generated — the mitigation is to run two to three DEL campaigns internally before the first enterprise sale, establishing a baseline corpus that makes the platform demonstrably useful on day one of the customer relationship.

---

## Go-to-Market Strategy

**Target customer:** Computational chemistry and AI/ML leads at mid-size oncology-focused biotech companies (50–500 employees, Series B and beyond) with active kinase inhibitor programs but without the internal data generation infrastructure to train proprietary models. This is a more tractable initial segment than large pharma — procurement cycles are shorter, technical buyers have more direct budget authority, and the pain of depending on Schrödinger's physics-based tools without a generative alternative is acutely felt. Large pharma (Pfizer, AstraZeneca, Novartis) is the expansion segment, not the launch segment.

**Primary distribution channel:** Direct enterprise sales through scientific co-development partnerships, not traditional software licensing. The first three customers should be structured as co-development agreements — the company runs DEL campaigns on the customer's target, trains models on the resulting data, and delivers both the model and the generated candidates. This mirrors the "molecules as a service" framing that Reverie found more legible to pharma buyers than pure software, while keeping the company in an infrastructure role rather than a pipeline role. Conference presence at AACR, AAPS, and the Society for Medicinal Chemistry provides direct access to the computational chemistry buyer.

**Pricing:** Co-development agreements priced at $300K–$750K per program, structured as upfront fees with no milestone contingency. This is the critical structural departure from Reverie's model: no milestone-dependent revenue, no partnership optionality, no contingent payments. Upfront fees are smaller but predictable. The stress-test against free alternatives is real — Schrödinger offers a free academic tier, and AlphaFold is free. The justification for paying $300K+ is not access to a model but access to proprietary experimental data generated specifically for the customer's target, which no free tool provides. Customers are paying for a data generation service with a model attached, not a model alone.

**Differentiation vs. 2026 competitors:** Against Recursion and Insilico, the rebuild is not a pipeline competitor — pharma's internal teams can use the platform without worrying about IP conflicts. Against Schrödinger, the rebuild offers generative chemistry trained on experimental data rather than physics-based scoring. Against Isomorphic Labs and Xaira, the rebuild is accessible to mid-size biotechs that cannot afford a $1B partnership. The positioning is "the infrastructure layer for pharma's internal AI teams" — a category that the well-capitalized integrated players have explicitly chosen not to occupy.
