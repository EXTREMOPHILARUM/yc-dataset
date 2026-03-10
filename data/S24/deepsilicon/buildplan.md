# Build Plan: deepsilicon 2026

## Overview

## Why Now?

## Current Market Analysis

**Market size.** The global edge AI chip market was estimated at approximately $3.5B in 2023 and is projected to exceed $15B by 2030, per MarketsandMarkets (2023 report). The narrower robotics inference subsegment does not have a clean public estimate; this is a gap in the available data. What is documentable: the humanoid robotics market alone attracted over $1B in disclosed venture investment in 2023–2024 (Crunchbase aggregates), and each deployed unit represents a recurring inference compute cost that OEMs are actively trying to reduce.

## Competition map.

- *llama.cpp / ExLlamaV2 / bitsandbytes*: Free, GPU/CPU-bound, no ternary-native hardware path, no enterprise SLA, no robotics-specific model support. Weakness: zero commercial support, no hardware co-design, accuracy at sub-4-bit degrades on vision-language-action models used in robotics.
- *Groq*: Cloud-only LPU, not deployable on-device. Weakness: requires network connectivity, incompatible with real-time robotics control loops.
- *Hailo*: Edge AI chips with automotive and industrial design wins, raised $200M+. Weakness: optimized for CNN-based vision, not transformer/VLA architectures; no ternary-native datapath.
- *Etched*: Transformer-specific ASIC, raised $120M. Weakness: cloud/datacenter focus, not edge-deployable, no robotics go-to-market.
- *Qualcomm AI Hub*: Broad edge deployment platform with NPU support. Weakness: general-purpose, not ternary-optimized, no co-design engagement model for robotics OEMs.

**Demand signals.** The llama.cpp GitHub repository's growth trajectory, combined with the rapid adoption of BitNet.cpp (Microsoft's reference ternary runtime, released late 2024), signals that developers are actively seeking ternary inference paths. Robotics OEMs posting job listings for "on-device inference optimization" and "edge ML runtime" engineers (observable on LinkedIn, though not systematically quantified here) are a secondary demand signal.

**Defensibility.** The honest answer is that platform incumbents — Qualcomm, NVIDIA with Jetson, Apple — could add ternary-optimized datapaths to their existing edge silicon. The structural defense is not technical exclusivity; it is co-design depth and switching cost. A rebuild that embeds its runtime into a robotics OEM's model training pipeline, inference stack, and hardware BOM creates a 12–18 month switching cost that a general-purpose platform vendor cannot replicate with a firmware update. The original Deepsilicon had no such embedded relationships. The rebuild must earn them early.

---

## Recommended MVP

## Core Feature 1: Ternary Inference Runtime for ROS 2

A pip-installable Python package and C++ shared library that runs BitNet b1.58-compatible ternary models natively within ROS 2 (Robot Operating System 2), the de facto middleware for humanoid and mobile robotics. It exposes a standard ROS 2 node interface so robotics engineers can drop it into an existing perception or action pipeline without rewriting their stack. Unlike the original Deepsilicon's generic pip-install, this is vertically scoped: it ships with pre-quantized versions of the three or four vision-language-action model architectures most commonly used in robotics (OpenVLA, RT-2 variants), removing the quantization step from the customer's workflow entirely.

## Core Feature 2: Power-Latency Profiler

An instrumented benchmarking harness that measures inference latency, memory footprint, and power draw on the customer's specific onboard compute (NVIDIA Jetson Orin, Qualcomm RB5, x86 NUC). It outputs a report comparing ternary runtime performance against the customer's current FP16 or INT8 baseline on their own models and hardware. This directly addresses the credibility gap that killed the original Deepsilicon: unvalidated 20x throughput claims. The profiler produces reproducible, customer-specific benchmarks that the customer can verify independently, converting a marketing claim into a procurement artifact.

## Core Feature 3: Managed Quantization Pipeline

A hosted service (API + CLI) that accepts a customer's FP16 model checkpoint and returns a ternary-quantized model with an accuracy report on a customer-supplied validation dataset. Priced per conversion job. This is the revenue entry point before any hardware exists.

**What we will NOT build:** a general-purpose cloud inference API, a consumer-facing product, a custom ASIC in the first 18 months, or support for non-transformer architectures.

**Success metrics:** 3 paid robotics OEM pilots at ≥$15K/pilot within 6 months of launch; ≥2 of those pilots converting to annual runtime licenses ≥$80K/year within 12 months; ≥15% latency improvement over Jetson Orin baseline demonstrated in at least 2 independent customer benchmarks.

**Cold-start note:** This product does not depend on network effects or local density. Value is delivered to a single customer on their own hardware. No minimum user threshold is required before the core feature delivers value.

---

## Go-to-Market Strategy

**Target customer segment:** Hardware engineering and ML infrastructure teams at Series A–C humanoid and mobile robotics companies (Figure, 1X, Unitree, Agility, Boston Dynamics AI Institute, and 10–15 comparable companies globally) that are actively deploying vision-language-action models on onboard compute and have a documented power or latency constraint. These teams have procurement authority, 6–12 week evaluation cycles, and budgets in the $50K–$200K/year range for runtime infrastructure.

**Primary distribution channel:** Direct outbound to robotics ML infrastructure leads, supplemented by presence at ROSCon (the annual ROS developer conference, ~1,000 attendees, highly concentrated target audience) and the Robotics Summit & Expo. GitHub presence with a public benchmark repository — showing reproducible latency and power numbers on Jetson Orin — serves as inbound credibility infrastructure for engineers who discover the tool through llama.cpp or BitNet.cpp adjacent searches.

**Pricing strategy:** Three tiers. (1) Open-source runtime: free, MIT-licensed, covers the ROS 2 node and basic ternary inference. This is the distribution mechanism, not the revenue mechanism. (2) Managed quantization pipeline: $2,500 per model conversion job, with a $500/month subscription for unlimited conversions. (3) Enterprise runtime license: $80K–$150K/year, includes SLA, private model support, profiler access, and engineering support hours.

The free alternative stress-test: a robotics engineer can use llama.cpp or BitNet.cpp for free. The rebuild's paid tier must justify its price against this baseline. The justification is (a) ROS 2 native integration that eliminates 2–4 weeks of engineering work, (b) pre-quantized VLA model checkpoints the customer cannot easily produce themselves, and (c) the profiler's reproducible benchmark report, which is a procurement artifact that free tools do not produce. Engineers at funded robotics OEMs are expensive; if the runtime saves one engineer-month of integration work, the $80K annual license pays for itself at a $150K fully-loaded engineer cost.

**Differentiation vs. 2026 competitors:** Hailo and Qualcomm sell general-purpose silicon with broad software support but no ternary-native datapath and no robotics-specific model library. Groq and Etched are cloud-only. The rebuild's differentiation is vertical depth — ROS 2 integration, VLA model support, and co-design engagement — not horizontal breadth.
