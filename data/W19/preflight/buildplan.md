# Build Plan: Preflight 2026

## Overview

Preflight was a Chicago-area no-code web testing startup (2018–2023) that let non-engineers record automated browser tests via a Chrome extension — a direct response to the Selenium maintenance crisis — before being acqui-hired by Applitools in June 2023 for a reported $10–15M after reaching only "tens of customers" with approximately 20 employees, a cost structure its revenue could never support.

The rebuild thesis is simple: the two things that killed Preflight — brittle DOM-selector-based recordings and the absence of a defensible distribution channel — are both solvable in 2026. LLMs can now generate and self-heal tests from plain-English descriptions, eliminating the recorder's fragility, while the no-code app development ecosystem (Bubble, Webflow, Framer) has matured into a large, structurally underserved market that enterprise testing incumbents will never prioritize. The new Preflight is the dedicated QA layer for no-code builders: an AI-native testing platform that ships inside the tools they already use, not alongside them.

---

## Why Now?

### The single most important change: LLMs can now write and repair tests that no-code recorders could not sustain.

Preflight's core technical failure was that its Chrome extension recorded tests by capturing DOM selectors — CSS classes, element IDs, XPath expressions — that broke every time a developer renamed a button or restructured a component. Self-healing logic existed in the product (Applitools' CTO cited it as the differentiator), but it was heuristic-based and fragile on dynamic, JavaScript-heavy applications. GPT-4 (March 2023) and Claude 3 Opus (March 2024) changed this structurally: a model that understands the semantic intent of a user action ("click the primary checkout button") can locate the correct element even after a full UI redesign, without relying on brittle selectors. Momentic, Octomind, and Reflect have demonstrated this capability in production since 2023 — the technical risk is no longer speculative.

**Infrastructure costs have collapsed.** Browserless, Playwright Cloud, and BrowserStack Automate now offer headless browser execution at commodity pricing. Running 10,000 cross-browser test executions per month costs roughly $50–200 depending on provider (exact 2026 pricing unknown), compared to the significant infrastructure overhead that constrained a $1.5M-funded startup in 2021.

**The no-code app market is substantially larger.** Bubble reported over 4 million registered developers as of 2023 (source: Bubble.io press materials); Webflow claimed 3.5 million users as of 2023 (source: Webflow). The combined no-code/low-code development platform market was estimated at $26.9B in 2023, growing at approximately 28% CAGR through 2030 (source: Grand View Research, 2023). This is not the same market Preflight was addressing in 2019 — it is materially larger and more production-oriented.

**PLG distribution is now a proven motion for developer tools.** The Chrome Web Store, Bubble Plugin Marketplace, and Webflow App Marketplace provide zero-CAC distribution channels with built-in intent signals. This was less trusted by buyers in 2019; it is now the default expectation for tools in this category.

---

## Current Market Analysis

**Market size today vs. 2019:** The global test automation market was approximately $12.6B in 2019 (source: Allied Market Research); it reached an estimated $28.8B in 2023 (source: MarketsandMarkets). The no-code testing subsegment has no reliable standalone sizing data — any figure here would be invented. What is documentable: the no-code app development platforms that represent the rebuild's primary distribution channel have grown from niche tools to production infrastructure used by millions of builders, creating a testing gap that did not exist at meaningful scale when Preflight launched.

## Competition map:

- **Applitools** (now owns Preflight's IP): Focused on visual regression testing for enterprise engineering teams. Pricing starts at approximately $1,500/month for team plans. Not positioned for no-code builders; requires technical setup. The Preflight technology was absorbed into an enterprise product that non-engineers cannot realistically use.
- **Momentic** (founded 2023): AI-native testing using vision models; targets engineers, not no-code builders. No native integrations with Bubble or Webflow as of available research. Strong technical product, weak no-code distribution.
- **Reflect** (founded 2020): No-code recorder, similar to original Preflight. Has not publicly disclosed integrations with no-code app platforms. Competes on the same horizontal positioning that failed Preflight.
- **Octomind** (founded 2023): AI-powered test generation from user stories; developer-oriented, requires GitHub integration. Not accessible to non-engineers.
- **Testsigma / Autify**: Better-funded horizontal no-code testing tools. Both target QA teams at mid-market software companies, not no-code builders. Autify raised $10M Series A (2021); Testsigma raised $18M Series B (2022).

**The gap:** No current competitor has built deep, native integration with Bubble, Webflow, or Framer as a primary distribution and product strategy. This is the structural white space.

**Defensibility against platform incumbents:** Bubble, Webflow, and Framer are unlikely to build native testing infrastructure themselves — testing is not their core product motion, and their developer ecosystems are explicitly designed to be extended by third-party plugins. Apple, Google, and Meta have no meaningful adjacent products in this specific niche. The more honest risk is that a well-funded horizontal player (Momentic, Reflect) pivots to target no-code platforms after this opportunity is validated. The defensible answer is speed of integration depth and community trust within each platform's ecosystem — not a permanent structural moat. This should be treated as a 24–36 month window, not a permanent advantage.

---

## Recommended MVP

### Core Feature 1: AI-Native Test Generation from Plain English

A user describes a workflow in natural language ("log in, add the Pro plan to cart, complete checkout") and the system generates a runnable, cross-browser test without recording or code. Powered by GPT-4o or Claude 3.5 Sonnet (both available as of mid-2024), the model interprets semantic intent rather than capturing DOM selectors, making tests resilient to UI changes by design. This directly replaces Preflight's Chrome extension recorder — the feature that generated the most maintenance overhead — with an approach that degrades gracefully when the UI changes.

## Core Feature 2: Bubble-Native Test Runner

A Bubble plugin that installs in one click from the Bubble Plugin Marketplace, authenticates against the user's Bubble app, and runs tests against both the development and live versions without any external configuration. Tests are aware of Bubble's component model (not raw DOM), making them structurally more stable than generic browser automation. This is the Bubble partnership Preflight was building at acquisition — shipped as a first-class product, not a roadmap item.

## Core Feature 3: Self-Healing Test Maintenance

When a test fails due to a UI change (not a real bug), the system uses a vision model to identify the new location of the target element and proposes an automatic fix with a one-click approval flow. The user sees a diff: "Button 'Checkout' moved from position A to position B — approve update?" This addresses the exact failure mode that made Selenium unsustainable at ShipBob and that Preflight's heuristic self-healing only partially solved.

## Core Feature 4: Slack-First Alerting with Failure Triage

Test failures are reported in Slack with a screenshot, the failing step highlighted, and an LLM-generated plain-English explanation of what broke and why. Non-engineers can understand and act on failures without reading logs. This mirrors Preflight's alerting feature but adds the LLM triage layer that was not available in 2021.

**What we will NOT build in MVP:** CI/CD pipeline integration, API test generation, multi-platform support beyond Bubble, enterprise SSO, or a generic Chrome extension recorder. These were Preflight's surface-area expansions that diluted focus without driving customer concentration.

## Success metrics:

- 500 active Bubble apps running at least one test per week within 6 months of launch
- 30-day retention above 40% (users who ran tests in week 1 still running tests in week 5)
- Median time-to-first-test under 10 minutes from plugin install

**Cold-start problem:** This product delivers value to a single user on day one — a solo Bubble builder can install the plugin, generate a test, and catch a bug without any other users present. There is no network effect dependency and no local density requirement. The cold-start problem does not apply.

---

## Go-to-Market Strategy

**Target customer:** Solo founders and two-to-five-person teams building production web applications on Bubble. Specifically: teams that have launched a paying product, are shipping updates weekly, and have experienced at least one regression bug that reached a customer. This is a buyer who already understands the cost of broken software and is not being sold on the concept of testing — only on the accessibility of the solution.

**Primary distribution channel:** Bubble Plugin Marketplace, with a free tier that allows up to 25 test runs per month. The Bubble ecosystem has over 4 million registered users (source: Bubble.io, 2023); even 0.1% conversion to paid represents 4,000 customers. Secondary channel: Bubble's official forum and community (active, high-intent, developer-adjacent). No outbound sales in year one.

**Pricing:** $49/month for 500 test runs, $149/month for 2,500 runs, with a free tier of 25 runs. Stress-test against free alternatives: Bubble builders currently test manually (clicking through their app before each release) or use generic tools like Playwright, which require writing JavaScript that most Bubble builders cannot do. The free alternative is not a competing product — it is manual regression testing, which is slower and less reliable. The $49/month price point is justified if it saves two hours of manual testing per month at a $25/hour opportunity cost, which is a conservative threshold for a founder shipping weekly updates. The risk is churn from users who test infrequently; the free tier is designed to keep low-volume users engaged until their usage grows.

**Differentiation vs. 2026 competitors:** Every current AI-native testing competitor (Momentic, Octomind, Reflect) is built for engineers and distributed through GitHub, VS Code, or direct sales. None has a native Bubble integration. The rebuild's differentiation is not better AI — it is better distribution into a specific ecosystem that competitors have structurally ignored. When Momentic eventually builds a Bubble plugin, the rebuild should already own the community trust and the integration depth that makes switching costly.

**Constraint acknowledgment:** All market size figures for the no-code testing subsegment are unavailable in the research report; the Bubble user count and Webflow user count cited above come from platform press materials and should be treated as directional, not audited. Pricing benchmarks for comparable tools are based on publicly listed prices as of available research and may have changed by 2026.
