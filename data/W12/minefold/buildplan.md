# Build Plan: Minefold 2026

## Overview

The single most important change since Minefold's failure is the demographic shift in Minecraft's player base. In 2012, Minecraft skewed heavily toward teenagers and pre-teens culturally conditioned to expect free online services. By 2023, Minecraft surpassed 140 million monthly active users (Microsoft earnings disclosures), and a meaningful cohort of those players are now adults in their mid-20s to early 30s — people who were 12 when Minefold launched and are now paying for Spotify, AWS, and Netflix without friction. The willingness-to-pay problem was never about the product; it was about the audience. That audience has aged into paying customers.

The second structural unlock is Minecraft Realms itself. Mojang's first-party hosting — the existential threat that ended Minefold — has inadvertently validated the paid managed-server market at scale while simultaneously defining its own ceiling. Realms is deliberately limited: no plugin support, no modpack compatibility, capped at 10 concurrent players, and priced at $7.99/month regardless of usage. It proved people pay; it left the entire modded Minecraft ecosystem unserved.

That ecosystem is now enormous. CurseForge reports over 100,000 Minecraft mods and modpacks as of 2024 (CurseForge platform data), and Modrinth has grown to host millions of monthly active mod downloads. Modpack players — Feed The Beast, ATM9, Vault Hunters communities — are technically sophisticated adults who already pay for CurseForge Premium and Patreon tiers supporting modpack developers. This is precisely the segment Minefold was beginning to address with its February 2013 FTB expansion before shutting down.

Cloud compute economics have also shifted materially. Hetzner's AX41 dedicated server runs approximately €39/month as of early 2025, delivering compute that would have cost multiples of that on AWS in 2012. Spot and preemptible instances on AWS and GCP have further compressed per-hour costs. The unit economics that made Minefold's $5/month price point structurally fragile are now workable at a competitive price.

Distribution channels unavailable in 2012 now exist at scale: the CurseForge App has millions of active modpack launcher users, Modrinth's launcher is growing rapidly, and Discord servers for specific modpacks (e.g., All the Mods, Vault Hunters) aggregate exactly the high-intent communities a rebuilt Minefold needs to reach. These are not generic "app marketplaces" — they are pre-assembled audiences of paying modpack players.

---

## Why Now?

### Current Market Analysis

**Market size:** The managed Minecraft server hosting market did not exist as a tracked category in 2012. Today, Apex Hosting, Nodecraft, and BisectHosting collectively serve hundreds of thousands of paying subscribers (exact figures are not publicly disclosed by any of these private companies). The broader game server hosting market was valued at approximately $1.7 billion in 2023 and is projected to grow at roughly 8% CAGR through 2030 (Grand View Research, 2023 — treat this figure as directional, not precise). Minecraft's 140 million MAU base represents a large addressable pool, with the modded segment conservatively estimated in the low millions of active players.

## Competition map and gaps:

- **Apex Hosting** is the current market leader in Minecraft hosting by brand recognition. Its weakness is a generic, plan-based pricing model (fixed RAM tiers starting at $2.99/month) that does not accommodate the variable resource demands of modpacks, which routinely require 6–12GB RAM and spike unpredictably. Customer reviews on Trustpilot consistently cite lag and RAM allocation issues on modded servers.

- **Nodecraft** offers a cleaner UX than Apex but uses a proprietary "NodeCraft Credits" currency that obscures actual costs and has drawn sustained criticism in Reddit communities (r/admincraft, r/feedthebeast) for billing confusion — precisely the trust problem Stripe's transparent metering now solves.

- **BisectHosting** competes primarily on price and has a large affiliate network through Twitch streamers and modpack developers. Its weakness is support quality; response times and resolution rates are frequently criticized in modpack-specific Discord servers.

- **Minecraft Realms** serves the casual, vanilla player segment effectively and is not a direct competitor for the modpack audience. It cannot run Forge, Fabric, or NeoForge modpacks at all.

**Demand signals from adjacent products:** Patreon pages for popular modpack developers (e.g., Vault Hunters, All the Mods) generate thousands of dollars monthly from players who want enhanced server access or early modpack builds — direct evidence that this audience pays for premium Minecraft experiences. The existence of the Modrinth launcher, which reached 1 million downloads within months of launch (Modrinth blog, 2023 — verify before citing), signals a technically engaged player base actively seeking better tooling.

---

## Recommended MVP

**Feature 1: Modpack-native server deployment.** A player selects any modpack from a live-synced CurseForge or Modrinth catalog and has a running server within 60 seconds, with correct Java version, memory allocation, and mod dependencies pre-configured automatically. This matters because every current competitor requires manual modpack installation or offers a limited curated list; the configuration burden is the primary reason modpack communities self-host on rented VPS instances. Unlike Minefold's 2013 FTB expansion — which supported a single modpack collection — this feature covers the full catalog dynamically.

**Feature 2: Usage-based billing with transparent metering.** Servers are billed per hour of active runtime, with a real-time dashboard showing current spend, projected monthly cost, and per-player cost if the group splits the bill. Stripe Billing (available since 2018 with usage-record APIs) makes this trivially implementable. This directly addresses the churn mechanism that killed Minefold: players who felt $5/month was too much for occasional play can now pay $0.08/hour and see exactly what they owe. The cost-sharing model Minefold pioneered is preserved and made legible.

**Feature 3: Persistent world with group billing.** Any member of a server's player group can become the billing owner, preventing the "server host as single point of failure" problem Minefold originally solved. If the original creator stops paying, the system prompts other members to take over before the server suspends — not deletes. World data is retained for 90 days post-suspension. This is the best feature Minefold built; it should be rebuilt first.

**Feature 4: Modpack-specific performance profiles.** Pre-tuned JVM flags, garbage collection settings, and RAM ceilings for the 50 most-played modpacks, updated monthly. This is a low-engineering, high-value differentiator against Apex and BisectHosting, whose generic configurations cause the lag complaints documented in community forums.

**What we will NOT build:** World rendering/map features (Minefold's original community layer — nice to have, not a retention driver), support for non-Minecraft games (the original founders' stated ambition was premature then and remains a distraction now), a proprietary launcher or client application, or a free tier of any kind.

**Success metrics:** 500 paying servers within 90 days of launch; average revenue per server above $12/month; monthly churn below 8%; modpack deployment success rate (server online within 90 seconds, correct version) above 95%.

---

## Go-to-Market Strategy

**Target customer segment:** Adults aged 22–35 who play modded Minecraft in friend groups of 4–10 players, specifically those active in Discord communities for top-50 CurseForge and Modrinth modpacks. This segment is narrow by design: they have disposable income, they already pay for mod-adjacent products (Patreon, CurseForge Premium), and they experience the configuration pain of modpack server setup directly. They are not the casual Realms customer and not the technical self-hoster — they are the person in the friend group who gets asked to "just set up the server" and resents the complexity.

**Primary distribution channel:** Direct integration with modpack Discord servers. The top 100 modpacks by CurseForge download count each have official or community Discord servers ranging from tens of thousands to hundreds of thousands of members. A rebuilt Minefold should sponsor or partner with 10–15 of these communities at launch, offering modpack developers a referral revenue share (20% of first-year revenue from referred servers) in exchange for a pinned post and bot command (e.g., `/host` returning a pre-configured server link for that specific modpack). This is not generic influencer marketing — it is distribution embedded at the exact moment of player intent.

**Pricing strategy:** Base rate of $0.06–$0.09 per server-hour (depending on RAM tier), with a monthly cap option at $15/month for servers running more than 200 hours. This undercuts Apex's effective per-hour rate on modpack-appropriate RAM tiers while remaining above the margin floor enabled by Hetzner-class compute. The monthly cap reduces billing anxiety for heavy users without subsidizing light users — a structural improvement over Minefold's flat $5/month that charged occasional players the same as daily players.

**Differentiation vs. 2026 competitors:** Apex and BisectHosting compete on price and affiliate volume; Nodecraft competes on UX but obscures costs. A rebuilt Minefold competes on modpack-specific reliability and transparent billing — two dimensions the current market leaders have explicitly failed on in community feedback. The positioning is "the hosting provider that modpack players built for modpack players," backed by public performance benchmarks per modpack that no current competitor publishes.
