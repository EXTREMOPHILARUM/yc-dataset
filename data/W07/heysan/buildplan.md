# Build Plan: Heysan 2026

## Overview

## Why Now?

## Current Market Analysis

**Market size today:** The global business messaging market was valued at approximately $62 billion in 2023 (Grand View Research, 2024), growing at a reported CAGR of roughly 12%. The consumer cross-platform messaging segment does not have a clean standalone valuation in available sources, but the scale of the underlying platforms is instructive: WhatsApp has 2 billion+ monthly active users (Meta, 2024), Telegram has 900 million (Telegram, 2024), Signal has approximately 40 million (Signal Foundation, 2023 estimate — exact figures not publicly disclosed), and iMessage is active on roughly 1.3 billion Apple devices (Apple, 2023). The re-fragmentation of messaging across these platforms has recreated the exact interoperability problem Heysan tried to solve in 2007, at a scale orders of magnitude larger.

## Competition map:

- **Beeper** (acquired by Automattic, 2024): The most direct current analog. Beeper aggregated iMessage, WhatsApp, Signal, and others via reverse-engineered bridges. Apple actively blocked its iMessage bridge in late 2023, demonstrating that the platform-dependency risk Heysan faced is still real for products that rely on unofficial access. Beeper's weakness: it depended on the same permissive-access model Heysan did, and Apple exercised exactly the same veto. A DMA-compliant rebuild avoids this by operating within the regulatory framework rather than around it.
- **Franz / Rambox**: Desktop-only messaging aggregators with no meaningful mobile presence and no AI routing layer. Weak monetization; free tiers dominate their user bases.
- **Texts.blog** (acquired by Automattic alongside Beeper): Similar aggregation approach, similar platform-dependency vulnerability. No B2B monetization layer.
- **WhatsApp Business API resellers**: Numerous, but none offer cross-platform routing or consumer-facing aggregation.

**Demand signals from adjacent products:** Discord grew from 45 million to 500 million registered users between 2019 and 2023 (Discord, 2023) by solving a different fragmentation problem — community communication across games and topics — which demonstrates sustained consumer appetite for unified communication layers. Notion's growth in the productivity space shows that users will pay for aggregation when the UX improvement is sufficiently clear.

**Defensibility analysis:** The honest answer is that platform incumbents remain the primary risk, and the DMA does not eliminate it — it restructures it. Apple, Meta, and Google could theoretically build their own cross-platform clients, but doing so would require them to actively route users to competitors' platforms, which is structurally contrary to their business models. Meta's revenue depends on keeping users inside WhatsApp; Apple's iMessage lock-in is a hardware retention mechanism. Neither has commercial incentive to build a neutral aggregation layer. The DMA creates a floor of mandated access; it does not create an incentive for incumbents to compete in the aggregation category. The rebuild's defensibility comes from the AI routing layer (proprietary model trained on contact behavior), the B2B API business (switching costs from integrated business workflows), and the Matrix-based proprietary network as a long-term destination. If Apple or Meta decides to build a neutral aggregator, there is no good structural answer — that risk should be disclosed to investors explicitly.

---

## Recommended MVP

## Feature 1: DMA-Compliant Unified Inbox (Mobile-First)

A single inbox aggregating WhatsApp, Telegram, Signal, and iMessage via DMA-mandated interoperability APIs and Matrix bridges, with read/write capability across all four. This is Heysan's original core feature, rebuilt on a legally defensible access model rather than permissive third-party tolerance. Unlike Beeper, the MVP does not use reverse-engineered bridges for any network; it operates only within officially published or DMA-mandated APIs, accepting that iMessage access outside the EU is not available at launch.

## Feature 2: AI Contact Routing

Using a fine-tuned LLM layer (built on GPT-4o or Claude 3.5 Sonnet, both available as of mid-2024), the product infers each contact's preferred platform based on response latency, read receipts, and historical patterns, and automatically routes outbound messages to the correct network. This is the feature that transforms aggregation from a manual protocol-switching chore into an invisible background process — the UX improvement Heysan could not deliver in 2007 because the underlying AI capability did not exist.

## Feature 3: Business Messaging API

A developer-facing API that allows SMBs to send and receive messages across WhatsApp, Telegram, and Signal from a single integration, priced per conversation on the WhatsApp Business API model. This is the monetization layer Heysan never had: revenue begins at user counts far below what ad-supported models require, and it creates B2B switching costs that consumer products do not.

**What we will NOT build:** A proprietary social network, community features, a virtual credits store, or any viral mechanism that touches users' contact lists without explicit opt-in. Heysan's auto-blast "Share with friends" feature is the specific anti-pattern this rebuild explicitly avoids.

## Success metrics:

- 10,000 MAU in the EU (primary DMA-compliant market) within 6 months of launch
- Business API: 100 paying SMB customers within 6 months, at ≥$50/month average revenue per customer
- Day-30 retention ≥ 40% (benchmark: messaging apps that achieve habitual use)

**Cold-start problem:** Unlike Heysan, this product delivers value to a single user on day one — the unified inbox works immediately for anyone with two or more messaging accounts, with no network density requirement. The AI routing layer improves with more contact data but is useful from the first week. There is no cold-start threshold for the core feature.

---

## Go-to-Market Strategy

**Target customer segment:** EU-based knowledge workers aged 25–45 who actively use three or more messaging platforms for a mix of personal and professional communication — specifically, freelancers, consultants, and small business owners who manage client relationships across WhatsApp and Telegram while maintaining personal contacts on iMessage or Signal. This segment is narrow enough to reach through targeted channels, large enough to validate the model, and located in the jurisdiction where DMA-mandated access is enforceable.

**Primary distribution channel:** Product Hunt and the Hacker News "Show HN" community for initial launch, followed by direct outreach to freelancer communities on Reddit (r/freelance, r/digitalnomad — combined 2M+ members) and LinkedIn targeting the "consultant" and "independent contractor" job titles in Germany, France, and the Netherlands, the three EU markets with the highest WhatsApp + iMessage dual-use rates (exact penetration data by country is not available in sources reviewed; this is an inference from general EU smartphone market data).

**Pricing strategy:** €9.99/month consumer subscription; Business API priced at €0.01–€0.08 per conversation (competitive with WhatsApp Business API published rates). The consumer subscription must be stress-tested against free alternatives: users can accomplish cross-platform messaging today for free by switching between apps, using WhatsApp Web on desktop, or relying on group chats. The justification for €9.99/month is not feature parity with free switching — it is time savings and cognitive load reduction for users who manage 50+ contacts across 3+ platforms daily. This is a productivity tool price point, not a social app price point, and it should be marketed as such. Users who primarily use one platform and occasionally switch will not pay; the product should not be marketed to them.

**Differentiation vs. 2026 competitors:** Beeper and Texts.blog both failed or pivoted because they relied on unofficial API access that incumbents could revoke. The rebuild's differentiation is DMA compliance as a structural moat (not a feature), AI routing as a UX layer no current competitor offers, and a B2B API revenue model that does not require consumer scale to generate meaningful revenue. The consumer product is the distribution mechanism; the business API is the business.
