# Build Plan: Flutter 2026

## Overview

Flutter was a San Francisco-based computer vision startup that built a free Mac app using the laptop's built-in webcam to recognize hand gestures for media control; acquired by Google in October 2013 for ~$40M after its algorithms demonstrably outperformed Google's internal work, the company was absorbed before it ever validated its intended B2B licensing model or expanded beyond a three-gesture vocabulary.

The rebuild thesis rests on three structural shifts: on-device ML has eliminated the gesture-vocabulary ceiling that kept Flutter a novelty, spatial computing has solved the consumer education problem, and enterprise accessibility compliance has created a procurement-driven B2B demand signal that Flutter's consumer-first framing never captured. The new Flutter is a JavaScript gesture-recognition SDK sold to enterprise SaaS companies and accessibility-focused software vendors — the licensing business the original always intended to be, now technically and commercially viable.

---

## Why Now?

The single most important change since Flutter's acquisition is the collapse of the gesture-vocabulary ceiling. In 2012–2013, webcam-based computer vision could reliably distinguish exactly three hand states under real-world conditions. Today, Google's MediaPipe Hands (released May 2020) tracks 21 hand landmarks in real time at over 30 frames per second on consumer hardware with no cloud dependency. Apple's Vision framework, available since iOS 14 / macOS 11 (September 2020), provides equivalent landmark detection natively on Apple Silicon. This is not an incremental improvement — it is a categorical one. A three-gesture vocabulary produces a novelty app; a 21-landmark model produces a programmable input layer capable of dozens of distinct, learnable gestures. The core UX limitation that prevented Flutter from becoming a daily driver no longer exists.

The second structural shift is hardware. Apple Silicon's Neural Engine (M1, November 2020; M3, October 2023) and Qualcomm's Snapdragon X Elite NPU (2024) provide dedicated on-device inference acceleration that did not exist in any consumer laptop in 2012. Always-on gesture recognition that would have drained a 2013 MacBook Air's battery in hours now runs as a background process with negligible power draw. Navneet Dalal explicitly named power efficiency as a founding challenge; that challenge is solved.

The third shift is distribution architecture. WebAssembly and browser-native ML inference — TensorFlow.js (stable v1.0, March 2019) and ONNX Runtime Web (v1.0, 2021) — allow a gesture-recognition engine to run entirely inside a browser tab with no native install required. This removes the Mac App Store dependency that constrained Flutter's original reach and enables a JavaScript SDK that any SaaS company can embed with a script tag. The B2B licensing model Flutter planned but never executed is now a standard SaaS SDK distribution pattern.

On the demand side, the accessibility technology market has matured into a procurement category. Enterprise ADA and WCAG compliance requirements create budget-line demand for gesture-based input alternatives — a signal Flutter's consumer framing never captured. The global assistive technology market was valued at approximately $22.6 billion in 2023 (Grand View Research; exact figure should be independently verified before use in investor materials). Spatial computing platforms — Apple Vision Pro (February 2024) and Meta Quest 3 (October 2023) — have normalized gesture-as-primary-input as a paradigm, substantially reducing the consumer education problem Flutter faced when waving at a laptop felt alien.

---

## Current Market Analysis

**Market size:** The gesture recognition market was nascent and difficult to size in 2012. Current analyst estimates for the global gesture recognition and touchless sensing market range from $9–12 billion in 2024, projected to reach $25–35 billion by 2030 (MarketsandMarkets, Grand View Research; these figures vary significantly by scope definition and should be treated as directional). The more relevant addressable market for a rebuild is the enterprise accessibility software and SDK licensing segment, which is smaller but procurement-driven — exact figures are not available in the research report and should not be invented here.

## Competition map:

- **HandsFree.js / Handtrack.js** (open source): Browser-based hand tracking libraries exist but are research-grade, undocumented for enterprise use, and carry no SLA, support contract, or accessibility certification. Their weakness is the gap between "works in a demo" and "embeddable in a production SaaS product."
- **Ultraleap** (formerly Leap Motion): Pivoted entirely to dedicated hardware for automotive and industrial HMI after the consumer USB controller failed to achieve mass adoption. No software-only, webcam-based SDK offering. Weakness: requires hardware purchase, eliminating the zero-marginal-cost distribution advantage.
- **Microsoft Azure AI Vision / Hand Pose**: Cloud-dependent, adding latency and data privacy concerns that disqualify it for many enterprise accessibility use cases. Weakness: not an embeddable on-device SDK; requires API calls.
- **Apple Vision framework**: On-device and high-quality, but locked to Apple platforms. No cross-platform JavaScript SDK. Weakness: zero reach on Windows or browser-based SaaS products.

**Demand signals from adjacent products:** The growth of voice control software (Dragon NaturallySpeaking, now Nuance Dragon, with reported enterprise revenue in the hundreds of millions annually) demonstrates that enterprises will pay for alternative input modalities when accessibility compliance is the procurement driver. Eye-tracking software companies like Tobii have built durable B2B businesses on the same compliance dynamic.

**Defensibility analysis:** The platform incumbents are the central risk. Apple already ships Vision framework; Google already ships MediaPipe. The honest answer is that neither has productized a cross-platform, browser-embeddable gesture SDK with enterprise support, accessibility certification, and a documented integration path for third-party SaaS vendors. The defensible position is not algorithmic superiority — that moat evaporated when MediaPipe went open source — but rather the enterprise go-to-market layer: compliance documentation, WCAG mapping, SLA guarantees, and the integration engineering that converts a research library into a production dependency. If Apple or Google decides to build and distribute a free enterprise SDK with those properties, this business faces existential platform risk. That risk is real and should be disclosed to investors.

---

## Recommended MVP

### Feature 1: Browser-embedded gesture SDK (JavaScript/WebAssembly)

A single-script-tag JavaScript library that runs MediaPipe Hands inference entirely in-browser, exposes a clean event API (`onGesture`, `onLandmark`), and requires no backend calls or native install. This is the core distribution unlock Flutter never had — any SaaS product can add gesture input in an afternoon. Unlike Flutter's Mac-only native app, this works on any device with a webcam and a modern browser, including Windows, ChromeOS, and Linux.

## Feature 2: Accessibility-certified gesture vocabulary

A pre-built library of 15–20 gestures mapped to WCAG 2.1 / 2.2 success criteria for pointer cancellation and alternative input, with accompanying documentation that enterprise accessibility teams can submit to compliance auditors. This is the feature that converts a developer tool into a procurement line item. Flutter had no accessibility framing; this rebuild leads with it.

## Feature 3: Enterprise dashboard and usage analytics

A web dashboard showing gesture adoption rates, error rates by gesture type, and device/browser compatibility breakdowns across an enterprise customer's user base. This is the instrumentation layer that justifies a recurring SaaS fee and enables customer success conversations. Flutter had no revenue instrumentation; this rebuild is built around it from day one.

**What you will NOT build:** A consumer app, a native desktop application, a hardware accessory, full-body or facial gesture recognition, or a mobile SDK. These are scope traps. The MVP is a browser SDK for enterprise SaaS vendors, nothing else.

## Success metrics:

- 10 paying enterprise customers within 12 months of SDK launch
- SDK embedded in at least 3 production SaaS products with >1,000 MAU each
- Gesture recognition accuracy ≥95% under standard office lighting conditions (measured against a defined test set)
- Average SDK integration time ≤8 engineering hours (measured via customer onboarding surveys)

**Cold-start note:** This product does not depend on network effects or local density. Value is delivered to the first enterprise customer on day one of integration. There is no cold-start problem in the traditional sense — but there is a chicken-and-egg problem between SDK credibility and enterprise adoption. The solution is to launch with two or three design-partner integrations (unpaid or heavily discounted) that generate public case studies before the paid sales motion begins.

---

## Go-to-Market Strategy

**Target customer segment:** Mid-market and enterprise SaaS companies (200–5,000 employees) with existing accessibility compliance programs and a dedicated engineering team. Specifically: companies that have already received ADA demand letters or VPAT requests from enterprise procurement teams, because those companies have a defined budget and a compliance deadline — the two ingredients that convert a "nice to have" into a purchase order. Vertical priority: HR software, learning management systems, and healthcare SaaS, where accessibility compliance is both legally mandated and actively audited.

**Primary distribution channel:** Direct outbound to VP Engineering and Head of Accessibility at target companies, supplemented by presence in accessibility-focused developer communities (A11y Project, WebAIM, CSUN Assistive Technology Conference). A free developer tier on npm (the JavaScript package registry, with over 2 million packages and tens of millions of weekly downloads) drives bottom-up discovery among engineers who then advocate internally for the paid enterprise tier.

**Pricing strategy:** Free tier for developers (up to 500 gesture events per day, watermarked); $500/month per application for production use (unlimited events, SLA, compliance documentation); enterprise contracts at $2,000–$5,000/month for multi-application deployment and dedicated support. The stress test: a developer can implement basic gesture recognition for free using MediaPipe Hands directly. The reason to pay is not the gesture recognition itself — it is the compliance documentation, the SLA, the tested cross-browser compatibility matrix, and the support contract that an enterprise procurement team requires before approving a production dependency. Group chats and built-in OS features do not provide WCAG mapping documentation or a signed BAA. The subscription is justified by the compliance layer, not the ML layer.

**Differentiation vs. 2026 competitors:** The rebuild's differentiation is the enterprise wrapper around open-source ML primitives — the same model that Elastic built on Lucene, or Confluent built on Kafka. The underlying gesture recognition is commoditized; the production-ready, compliance-certified, SLA-backed SDK is not. No current competitor occupies this specific position in the market as of the research report's findings.
