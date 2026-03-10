# Build Plan: Memo 2026

## Overview

Memo was a UK-based messaging application (2019–2020) that attempted to replace email and Slack with a calmer, annotation-rich form of asynchronous communication — it raised $150,000 from Y Combinator's S20 batch, failed to attract follow-on funding, and quietly shut down, with its domain now resolving to a parking page.

The rebuild thesis is not to try again against Slack — it is to stop competing with Slack entirely. Between 2020 and 2026, a documented, reachable segment of async-first companies (GitLab, Doist, 37signals and their imitators) has emerged that has already rejected synchronous communication as an organizational principle; LLMs can now do the structured work — surfacing questions, summarizing threads, flagging action items — that previously required users to change their behavior; and the creator-to-team communication layer remains genuinely unbuilt. The new Memo is a vertical async communication layer for async-first teams of 5–50, with AI-native thread intelligence baked in from day one.

---32:Ta9a,

## Why Now?

The single most important change since Memo's failure is the emergence of async-first companies as an identifiable, self-selecting, and reachable B2B customer segment — one that did not meaningfully exist in 2020.

In 2020, remote work was a crisis response, not an organizational philosophy. Teams were scrambling onto Slack and Teams under IT mandate, not making deliberate communication choices. By 2026, that has stratified. GitLab's public handbook, Doist's published async manifesto, 37signals' *It Doesn't Have to Be Crazy at Work*, and the broader "calm company" movement have produced a documented cohort of companies that have explicitly written async communication into their operating principles. These companies are not locked into Slack by organizational inertia — many have actively migrated away from it. Twist (by Doist) reports that its user base grew substantially through 2022–2024 on the back of this segment, though exact figures are not publicly disclosed.

The second critical change is LLM capability. GPT-4 (March 2023) and its successors made it technically feasible to automatically surface highlighted questions, summarize thread context, and extract action items from unstructured message text — features Memo offered as manual UX affordances that required users to change their behavior. The behavior change requirement was almost certainly a friction source that suppressed adoption. In 2026, the AI layer removes it: the structure emerges from the message, not from the user.

Third, infrastructure costs have collapsed. Supabase Realtime (production-ready by 2022), Ably, and Pusher now provide managed real-time messaging backends that a two-person team can operate at scale. The 2020 version of Memo required building this infrastructure from scratch on $150,000; the 2026 version does not.

On market signals: the global team collaboration software market was valued at approximately $17.6 billion in 2023 (Grand View Research) and is projected to grow through 2030, though the specific async-first sub-segment size is not independently documented. The Substack and newsletter economy — which crossed 35 million paid subscriptions in 2023 (Substack, per company disclosure) — has demonstrated that users will pay for slower, richer written communication, validating Memo's original attention-economy thesis with actual willingness-to-pay data.

Distribution channels unavailable in 2020 now exist: the Notion template marketplace, the Linear integration ecosystem, and async-first community hubs like the Remote Work community on Reddit (2.8M members) and the Async Work Slack (yes, ironically) provide targeted reach to the exact segment this rebuild targets.

---

## Current Market Analysis

**Market size:** The broader business communication software market was valued at approximately $17.6 billion in 2023 (Grand View Research), up from an estimated $11–12 billion in 2020. The async-first sub-segment is not independently sized in any source reviewed for this report — that figure does not exist publicly, and inventing one would be misleading. What is documentable is the proxy signal: Twist has operated profitably in this niche since approximately 2017, and Basecamp (37signals) has publicly stated it generates tens of millions in annual revenue serving a similar philosophy-aligned customer. The segment is real and monetizable, even if its total size is unquantified.

## Competition map:

- **Twist (Doist):** The most direct competitor. Organized around threads rather than channels, explicitly async-first. Its weakness is that it has not meaningfully invested in AI-native features as of early 2025; the product feels philosophically correct but technically stagnant. No paragraph-level annotation. No LLM thread intelligence.
- **Basecamp:** Targets small businesses broadly, not async-first teams specifically. Message boards are async but lack structured annotation or AI summarization. Pricing ($299/month flat) creates a floor that makes it uncompetitive for teams under ~10 people.
- **Notion AI + comments:** Notion's inline comment system validates the annotation interaction model, but Notion is a document tool, not a communication tool. Switching contexts between Notion and a chat app is the problem the rebuild solves, not a solution to it.
- **Linear:** Validates threaded, structured async communication in the engineering workflow. Not a general communication tool; no rich media, no cross-functional messaging.
- **Slack AI (launched 2024):** Adds AI summarization to Slack threads. This is the most serious competitive threat — but Slack AI is a retrofit onto a synchronous-first architecture. The notification model, the channel structure, and the presence indicators all remain. Async-first teams reject these at the organizational level, not the feature level.

**Defensibility against platform incumbents:** This is the honest version of the answer. Microsoft Teams and Slack could build everything described in this plan. The structural argument for why they won't is not technical — it is organizational. Slack's business model depends on engagement metrics that async-first design actively suppresses. Fewer notifications, slower response norms, and thread-first navigation reduce the daily active usage numbers that Slack reports to Salesforce. Building a genuinely async-first product would cannibalize Slack's core engagement story. This is a real but not ironclad moat — it is a strategic misalignment, not a technical barrier. If the rebuild reaches meaningful scale, incumbents will respond. The defensibility window is approximately 18–36 months before a well-resourced competitor builds a credible async mode. The go-to-market strategy must account for this.

**Demand signals:** Twist's continued operation, Basecamp's revenue, and the growth of async-first job boards (e.g., Remote OK, We Work Remotely) all confirm that the customer segment exists and is willing to pay for philosophy-aligned tools.

---

## Recommended MVP

## Core Feature 1: Thread-first messaging with paragraph-level annotation

Every message in the rebuild is a structured document, not a chat bubble. Users can highlight any sentence or paragraph and attach a threaded reply directly to it — the interaction Memo pioneered and that Notion has since validated in document workflows. This differs from the original in one critical way: the annotation layer is the primary interface, not an optional affordance. There is no "send a plain message" mode that bypasses structure.

## Core Feature 2: LLM-native thread intelligence

On every thread, an AI layer (built on GPT-4o or Claude 3.5 Sonnet, both available via API as of 2024) automatically surfaces: open questions that have not received a response, action items with implicit owners, and a one-paragraph thread summary for anyone joining mid-conversation. This eliminates the behavior change requirement that likely killed Memo's adoption — users do not need to manually tag questions or format action items. The original Memo offered "highlighted questions" as a manual UX feature; the rebuild makes it automatic and invisible.

## Core Feature 3: Async status and response-time norms

Each user sets a response window (e.g., "I respond within 4 hours, Mon–Fri"). This is displayed on their profile and surfaced in thread context when they are mentioned. This is not a presence indicator — it is a commitment signal. It directly addresses the anxiety that drives teams back to synchronous tools ("I don't know if they saw it") without reintroducing real-time pressure.

**What we will NOT build:** Real-time chat, voice or video calling, a mobile app (web-first for MVP), integrations beyond a single Slack import tool, and any enterprise SSO or compliance features. These are scope traps that killed the original by forcing competition on every axis simultaneously.

**Success metrics:** 10 teams of 5+ members each completing 30+ threads in their first 30 days (indicating genuine workflow adoption, not trial); week-4 retention above 60%; at least 3 teams upgrading from free to paid within 90 days of signup.

**Cold-start approach:** The product delivers value to a single team of 2+ people from day one — it is not dependent on cross-team network density. The minimum viable network is one team. To reach the first 10 teams, the go-to-market strategy targets async-first community spaces (see Section 4) where teams are already self-identified and actively seeking tools. No general launch; invite-only seeding into 3 async-first communities before public availability.

---

## Go-to-Market Strategy

**Target customer segment:** Remote-first software teams of 5–30 people that have explicitly adopted async communication as an organizational policy — not teams that are "open to async" but teams that have written it into their norms, use Twist or Basecamp today, and cite communication overhead as a top operational complaint. This segment is narrow by design. It is reachable through self-identification (they write about async work publicly) and has demonstrated willingness to pay for philosophy-aligned tools.

**Primary distribution channel:** Direct community seeding in async-first spaces. Specifically: the Doist community forums (Twist users who are already async converts), the 37signals/Basecamp community, the Async Work and Remote-first channels within communities like Indie Hackers and the Remote Work subreddit (2.8M members). The tactic is founder-led participation — not advertising, but answering questions about async communication, sharing the product as a solution to specific problems raised in threads, and offering free onboarding calls to the first 20 teams. Secondary channel: a Notion template ("Async Team Communication Playbook") distributed through the Notion template gallery that embeds the product as the recommended tool for teams implementing the playbook.

**Pricing:** $12 per user per month, with a free tier capped at 3 users and 90 days of message history. The stress-test against free alternatives is honest: Slack's free tier, group email threads, and Notion comments all serve overlapping use cases at no cost. The justification for $12/user/month is not feature superiority — it is organizational alignment. Async-first teams that have already decided to pay for Twist ($7/user/month) or Basecamp ($299/month flat) have demonstrated that they will pay a premium for a tool built around their communication philosophy rather than retrofitted to it. The price is positioned above Twist to signal quality and below Basecamp to remain accessible to sub-10-person teams. If users are unwilling to pay over Twist's price point, the free tier provides a 90-day window to demonstrate value before the conversion ask.

**Differentiation vs. 2026 competitors:** Against Twist — AI-native thread intelligence that Twist has not built. Against Slack AI — async-first architecture rather than async features bolted onto a synchronous product. Against Notion comments — a communication tool, not a document tool; no context-switching required. The differentiation is not a feature list; it is the claim that this is the only tool designed from the ground up for teams that have already decided synchronous communication is the problem.
