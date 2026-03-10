# Build Plan: Reduced Energy Microsystems 2026

## Overview

Reduced Energy Microsystems (REM) was a San Francisco-based fabless semiconductor startup that operated from 2014 to 2020, building ultra-low-power asynchronous chips for edge AI inference in body cameras, drones, and security systems — and failed not because the technology was wrong, but because $2M cannot fund a chip company through a 5-year development cycle in a market that was simultaneously being captured by better-capitalized competitors.

The rebuild thesis is not to retry REM's original approach with more money. It is to do something REM pivoted toward only in its final months but never had the runway to execute: license a production-ready asynchronous RISC-V processor IP core into a RISC-V ecosystem that has since grown to 4,000+ member organizations and billions of shipped devices annually. The new REM is an IP licensing company first, a chiplet vendor second, and a full-chip company never — a low-power asynchronous RISC-V core business built for the infrastructure moment the original company was too early and too underfunded to reach.

---

## Why Now?

### The single most important change since REM's failure is that the RISC-V ecosystem has become a production-grade distribution channel for processor IP.

When REM joined the RISC-V Foundation in November 2017, RISC-V was an academic project with institutional momentum but almost no commercial deployment. By 2026, RISC-V International reports 4,000+ member organizations, and commercial RISC-V SoCs ship in billions of devices annually — including Western Digital hard drives, Alibaba server chips, and a growing share of IoT microcontrollers. This is not a projection; it is a documented market transition. The ecosystem bootstrapping cost that would have consumed a significant fraction of REM's $2M seed round simply does not exist in 2026.

The second critical change is the collapse of early-stage chip design costs. Open-source EDA tools — OpenROAD, OpenLane, and the SkyWater Sky130 PDK — have matured to the point where a small team can complete early design iterations at a fraction of the cost of commercial EDA licenses. Cadence Virtuoso and Synopsys Design Compiler licenses that cost $200K–$500K annually in 2017 are no longer the only path to a working design. This directly addresses the capital constraint that starved REM's development cycles.

Third, the chiplet architecture transition — enabled by UCIe interconnect standards ratified in 2022 — means a startup can now build a specialized asynchronous processing tile that integrates with standard synchronous chiplets rather than taping out a complete SoC. A full-chip tape-out on an advanced node costs $500K–$5M; a chiplet tile targeting a mature node like GLOBALFOUNDRIES 22FDX (now production-proven with a broad IP ecosystem, unlike its status when REM announced its partnership in December 2017) costs substantially less and reaches customers faster.

Fourth, TinyML frameworks — TensorFlow Lite Micro, ONNX Runtime for microcontrollers — have standardized the software stack for edge inference. REM would have needed to build custom neural network tooling in parallel with hardware; a 2026 rebuild inherits that stack.

Finally, the body camera and drone markets REM targeted now have explicit regulatory demand signals: body camera mandates exist in 40+ U.S. states, and FAA drone weight and power rules create procurement criteria that favor ultra-low-power silicon. Market size data for the specific asynchronous IP licensing segment is not publicly available, but the broader edge AI chip market was valued at approximately $3.5B in 2023 (MarketsandMarkets; exact 2026 figure unknown).

---

## Current Market Analysis

**Market size:** The global edge AI chip market was valued at approximately $3.5B in 2023 (MarketsandMarkets) and is projected to grow at a CAGR above 20% through the late 2020s, though specific 2026 figures are not confirmed in the research report. For context, REM operated when this market was pre-commercial — Movidius had just shipped its first Myriad 2 units to DJI and Google in 2016. The market has since been validated at scale. The RISC-V processor IP licensing segment specifically is smaller and less publicly quantified; exact TAM figures are not available.

## Competition map:

- **SiFive** (founded 2015, raised $175M+ through 2021): The dominant commercial RISC-V IP licensor. Weakness: SiFive's cores are synchronous. They compete on ecosystem breadth and toolchain maturity, not power efficiency. A 3–4x power efficiency advantage on always-on workloads is not something SiFive can replicate without architectural change.
- **Andes Technology**: Taiwanese RISC-V IP vendor with strong Asia-Pacific distribution. Weakness: synchronous architecture, limited presence in U.S. defense and public safety procurement channels.
- **Syntiant**: Asynchronous neural decision processors for always-on audio and vision. Weakness: application-specific (keyword detection, gesture recognition) rather than general-purpose programmable inference. Not a RISC-V IP licensor. Raised $35M+ by 2020 — proof that the power-efficiency positioning attracts capital.
- **Eta Compute**: Sub-threshold CMOS for always-on vision; acquired by Nordic Semiconductor in 2021. Weakness: no longer an independent IP licensing business; absorbed into a larger product company.
- **Hailo**: High-performance edge inference accelerator. Weakness: targets higher-power, higher-performance applications (automotive, smart city) rather than ultra-low-power always-on sensing. Raised $136M — validates the market, not a direct competitor.

**The gap:** No current competitor offers a general-purpose, programmable, asynchronous RISC-V processor IP core that chip designers can license and integrate into their own SoCs. SiFive owns the RISC-V IP licensing market but is synchronous. Syntiant owns the asynchronous inference niche but is not licensable IP.

**Defensibility against platform incumbents:** This is the honest hard question. ARM Holdings — now public after its 2023 IPO — has every incentive to offer a low-power RISC-V-compatible core and the resources to do so. The structural defense is not that ARM cannot build an asynchronous core; it is that ARM's entire business model, toolchain investment, and customer relationship infrastructure is built around synchronous design. Koven's 2017 observation — "asynchronous is a dirty word at Intel" — applies equally to ARM in 2026. This is a real but not permanent moat. The rebuild must reach licensing revenue and design wins before ARM decides the market is large enough to justify the organizational disruption of an asynchronous product line. If ARM moves, the exit is acquisition, not competition.

---

## Recommended MVP

### Core Feature 1: Asynchronous RISC-V RV32IMC IP Core on GF 22FDX

A production-characterized, silicon-verified asynchronous implementation of the RISC-V RV32IMC instruction set, delivered as licensable RTL with full verification collateral. This is the product REM was building toward in December 2017 but never completed with sufficient commercial packaging. The difference from REM's approach: this is the *first* product, not a pivot from chip sales. It targets SoC designers at IoT chip companies who already use GF 22FDX and need a lower-power processor option than SiFive's synchronous cores. Delivery format matches existing SiFive licensing conventions so procurement teams face no new process.

## Core Feature 2: TinyML Inference Benchmark Suite and Power Characterization Package

A standardized benchmark package — running MLPerf Tiny workloads on the asynchronous core — that gives prospective licensees a credible, third-party-verifiable power efficiency comparison against SiFive E31 and ARM Cortex-M4. REM claimed 3–4x efficiency gains but never published silicon-validated data. This feature exists to close that credibility gap. It is not a product; it is a sales tool that converts technical interest into signed license agreements.

## Core Feature 3: OpenLane-Compatible Design Flow Integration

A documented, tested integration of the asynchronous core into the OpenLane open-source EDA flow, enabling licensees to perform early integration experiments without purchasing commercial EDA licenses. This directly addresses the toolchain friction that historically blocked asynchronous chip adoption. REM built proprietary internal tooling; the 2026 rebuild publishes the integration layer as open source to drive adoption, retaining the core RTL as the commercial asset.

**What we will NOT build:** A complete SoC. A body camera chip. A drone chip. A custom ASIC for any single customer. Any product that requires a full tape-out before generating licensing revenue. The original REM's mistake was building a chip before building a customer base; this rebuild inverts that sequence.

## Success metrics:

- 3 signed IP license agreements within 18 months of silicon characterization data availability
- Silicon-validated power efficiency of ≥2.5x vs. SiFive E31 on MLPerf Tiny keyword spotting benchmark (threshold below REM's claimed 3–4x to account for measurement conservatism)
- GF 22FDX tape-out of characterization vehicle completed within 14 months of founding

**Cold-start note:** This is a B2B IP licensing business, not a network-effects product. There is no cold-start problem in the consumer sense. The minimum viable customer base is one signed license agreement with a chip designer who integrates the core into a shipping SoC — at which point royalty revenue begins and the reference design validates the product for subsequent licensees.

---

## Go-to-Market Strategy

**Target customer segment:** IoT SoC design teams at Tier 2 and Tier 3 semiconductor companies (annual revenue $50M–$500M) building chips for always-on sensing applications — specifically companies already qualified on GF 22FDX who are designing for body camera, industrial sensor, or drone applications. This excludes ARM's direct licensees (too large, too locked in) and pure startups (insufficient procurement infrastructure). The specific procurement trigger is a design team that has evaluated SiFive's E-series cores and found the power budget insufficient for their application.

**Primary distribution channel:** Direct engagement with the GF 22FDX FDXcelerator Partner Program ecosystem — the same channel REM announced in December 2017 but never had the product to activate. GLOBALFOUNDRIES has a documented interest in populating its 22FDX IP ecosystem with differentiated processor cores; this is a warm channel, not a cold one. Secondary channel: RISC-V International member events and the RISC-V Summit, where the target customer's chip architects are concentrated.

**Pricing strategy:** Standard RISC-V IP licensing structure — a one-time license fee of $150K–$500K (depending on support tier) plus a per-unit royalty of $0.05–$0.15. This is consistent with SiFive's published pricing tiers. The stress test: SiFive offers free access to some core configurations through its developer program. The rebuild's answer is that the free SiFive cores are synchronous — a chip designer who needs ultra-low-power always-on inference cannot substitute a free synchronous core for a paid asynchronous one. The value proposition is not convenience; it is physics. A customer who doesn't need the power efficiency won't pay; a customer who does has no free alternative.

**Differentiation vs. 2026 competitors:** Against SiFive — asynchronous architecture delivering silicon-validated power efficiency on an identical process node and instruction set. Against Syntiant — general-purpose programmability and RISC-V software ecosystem compatibility rather than fixed-function inference. Against ARM — open licensing terms, no architecture royalty stack, and a power efficiency claim ARM's synchronous Cortex-M line cannot match on always-on workloads. The differentiation is narrow, technically specific, and deliberately so: broad positioning invites broad competition; narrow positioning on a measurable, silicon-validated metric is defensible.
