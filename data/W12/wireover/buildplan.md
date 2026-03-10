# Build Plan: WireOver 2026

## Overview

By 2026, WireOver is a browser-native file transfer platform for regulated industries—healthcare, legal, and biotech teams that need to move large files securely without installing software or managing infrastructure. The product lives in the browser, works instantly via a shareable link, and encrypts everything client-side before it leaves your machine. For compliance teams, every transfer generates an audit log; for end users, it's frictionless—no accounts, no apps, just send and receive.

The shift that makes this work now is WebRTC. In 2014, peer-to-peer transfer in the browser was a fantasy. Today it's native across Chrome, Firefox, Safari, and Edge. That means you can build a zero-install, zero-trust file transfer that actually competes with Aspera and enterprise MFT platforms—but without the $50K implementation cost or the IT overhead. The compliance layer (audit logs, SSO, BAA) is what enterprise buyers actually want; the P2P speed is what makes it possible.

Go-to-market is bottom-up through the recipient viral loop—every file transfer creates a new user who can immediately send—paired with direct outbound to IT and compliance buyers in healthcare and legal. You win by being the only product that's simultaneously frictionless for end users and auditable for regulators. Pricing starts free (5 GB transfers, no logs

## Why Now?

The single most important change since WireOver's failure is that **WebRTC, now natively supported in all major browsers since approximately 2017 and fully standardized by the W3C in January 2021, eliminates the two-sided desktop installation requirement that was WireOver's primary adoption killer.** In 2014, both sender and recipient had to install a Python desktop client before a single byte could transfer. Today, a sender opens a browser tab and shares a link; the recipient clicks it and receives the file — no installation on either side. Products like Wormhole.app have already validated this browser-native P2P model commercially.

This architectural shift unlocks everything else. The cold-start problem that made WireOver's network effect impossible to seed dissolves when the recipient experience requires zero friction.

Additional structural tailwinds compound the opportunity:

- **Enterprise encryption demand is now a procurement checkbox, not a niche concern.** HIPAA, GDPR, and SOC 2 Type II explicitly require encrypted data transfer. A 2023 IBM Cost of a Data Breach Report found the average breach cost $4.45M — giving enterprise buyers a concrete ROI frame for encrypted transfer tools that did not exist when WireOver was pitching its $10/month Pro tier to privacy enthusiasts.

- **Remote work has permanently expanded the large-file transfer market.** Post-2020, video production teams, genomics researchers, and AI training data pipelines regularly move 100 GB–10 TB files outside corporate VPNs, a workflow WireOver identified but could not monetize.

- **Infrastructure costs have collapsed.** Cloudflare R2 (launched 2022) charges zero egress fees, making relay-server fallback economically sustainable at free-tier scale. In 2012, WireOver's relay architecture had unpredictable server costs; today those costs are predictable and cheap.

- **Cryptographic primitives are now commodities.** libsodium and the `age` encryption library (stable release 2021) are well-audited, trivially embeddable, and require no bespoke cryptographic engineering — eliminating the 18-month prototype cycle WireOver burned before launch.

The Frame.io acquisition by Adobe for $1.275B in 2021 confirms that large-file transfer in media and entertainment is a real, premium-monetizable problem. The market has matured; the infrastructure has caught up.

---

## Current Market Analysis

**Market size:** The global managed file transfer (MFT) market was valued at approximately $2.4B in 2023 and is projected to reach $4.1B by 2028 (MarketsandMarkets, 2023). The adjacent large-file transfer segment — spanning media production, genomics, AI/ML data pipelines, and legal/healthcare document exchange — is not cleanly separated in public data, but Frame.io's $1.275B acquisition price and Aspera's continued growth under IBM suggest the media vertical alone supports nine-figure revenue at scale. When WireOver operated (2012–2015), the MFT market was estimated at under $1B globally; the problem has grown substantially.

## Competition map and gaps:

- **Aspera (IBM):** The incumbent for media and entertainment large-file transfer. Strengths: FASP protocol delivers near-line-speed transfers regardless of latency; deep enterprise integrations. Weaknesses: pricing starts in the tens of thousands of dollars annually; requires dedicated server infrastructure; procurement cycle measured in months. Inaccessible to teams under ~50 people.

- **Frame.io (Adobe):** Dominates video review-and-approval workflows with integrated transfer. Weakness: tightly coupled to Adobe Creative Cloud; not useful for non-video file types or non-Adobe shops; no zero-knowledge encryption.

- **WeTransfer Pro (2026):** Browser-based, no installation required, strong brand. Weaknesses: 200 GB transfer limit on Pro ($15/month); no end-to-end encryption; files stored on WeTransfer servers, creating compliance exposure for regulated industries.

- **Wormhole.app:** Browser-native P2P with E2E encryption; closest to the rebuilt WireOver concept. Weaknesses: 10 GB limit on free tier, 5 TB on paid ($15/month); no enterprise features (audit logs, SSO, admin controls, compliance reporting); consumer-focused positioning with no documented SOC 2 certification.

- **Secure MFT vendors (GoAnywhere, MOVEit, Globalscape):** Enterprise-grade compliance and audit trails. Weaknesses: legacy UX, on-premise deployment bias, no browser-native P2P, expensive.

**The gap:** No current product combines browser-native zero-install P2P transfer, genuine zero-knowledge E2E encryption, enterprise compliance features (audit logs, SSO, SOC 2), and pricing accessible to mid-market teams (10–500 employees). Wormhole owns the consumer P2P space; Aspera owns enterprise media. The mid-market regulated-industry buyer — healthcare, legal, financial services, architecture/engineering — is underserved by both.

**Demand signals:** Slack's file size limits (1 GB on paid plans as of 2024) regularly force teams to use workarounds. Google Drive's 5 TB individual file limit and lack of zero-knowledge encryption create documented compliance gaps for HIPAA-covered entities. These friction points generate consistent complaint threads on Reddit's r/sysadmin and r/msp communities — unprompted demand signals for exactly the product WireOver tried to build.

---

## Recommended MVP

## Core Features:

### Browser-native zero-install P2P transfer with automatic relay fallback.

Using WebRTC DataChannels, the sender initiates a transfer from a browser tab and shares a link; the recipient clicks the link and receives the file with no installation required on either side. When P2P is blocked by firewalls or NAT (a common enterprise network condition), the file routes through a Cloudflare R2-backed relay that holds data in transit only — never at rest. This directly eliminates WireOver's fatal two-sided installation barrier while preserving its architectural advantage of not storing files on servers.

## Zero-knowledge end-to-end encryption using the `age` encryption library.

Every transfer is encrypted client-side before any data leaves the sender's browser, using `age` (stable release 2021, audited by Cure53). The recipient's browser decrypts locally; the relay server — if used — sees only ciphertext. Encryption is on by default for all tiers, not gated behind a paid upgrade. Unlike WireOver, which made encryption a $10/month upsell that most users skipped, encryption here is the baseline — the paid tier unlocks compliance features built on top of it.

## Compliance and audit layer for enterprise buyers.

Every transfer generates a tamper-evident audit log: sender identity, recipient identity, file hash, transfer timestamp, encryption key fingerprint, and delivery confirmation. Logs are exportable in formats compatible with HIPAA, SOC 2, and GDPR documentation requirements. This is the feature WireOver never built — the enterprise-specific capability that justifies a premium price point above the free tier and maps directly to a procurement checkbox rather than a discretionary security preference.

## Recipient-side web delivery with no account requirement.

Recipients receive a time-limited, single-use download link that works in any browser. No account creation, no app installation, no friction. This is the asymmetric onboarding model WeTransfer proved works — the sender has an account; the recipient does not need one. WireOver required both parties to install software; this version requires neither.

## Admin dashboard with SSO and team management.

For enterprise accounts: centralized user provisioning, SAML/OIDC SSO integration, per-user transfer limits, and revocable access. This is the feature layer that converts a team tool into an IT-approved procurement decision.

## What we will NOT build (MVP scope):

- A desktop application of any kind
- Video review or annotation features (Frame.io's territory)
- Storage or cloud sync (Dropbox's territory)
- Mobile apps (Phase 2)
- Custom FASP-style transfer protocol (WebRTC is sufficient for MVP; Aspera-level protocol engineering is a Series B problem)

## Success metrics with concrete thresholds:

- **Week 8:** 500 completed transfers from non-founder users, with ≥30% involving files >1 GB
- **Month 3:** 10 paying teams (≥3 seats each) at the mid-market tier; MRR ≥ $2,000
- **Month 6:** ≥1 customer in a regulated industry (healthcare, legal, or financial services) using the audit log feature; NPS ≥ 40 from paying users
- **Month 9:** ≤15% monthly churn on paid accounts; ≥25% of new paid accounts sourced from recipient-side viral loop (recipients who became senders)

---

## Go-to-Market Strategy

### Target customer segment:

Mid-market teams in regulated industries — specifically healthcare (radiology practices, genomics labs, clinical research organizations), legal (litigation support, e-discovery firms, boutique M&A practices), and architecture/engineering firms — with 10–200 employees who regularly transfer files exceeding 5 GB and have documented HIPAA, SOC 2, or GDPR obligations. This segment is narrow enough to have a specific, verifiable compliance pain point (unlike WireOver's diffuse "anyone who sends big files" positioning) and large enough to support enterprise pricing. They are currently underserved: Aspera is too expensive, WeTransfer lacks encryption compliance, and Wormhole has no enterprise features.

## Primary distribution channel:

Bottom-up PLG through the recipient viral loop, accelerated by direct outbound to IT/compliance buyers. Every file a sender transfers creates a recipient touchpoint — the download page is branded, includes a "Send files this way" CTA, and converts recipients into senders. This is the viral mechanic WireOver never had because its recipient experience required installation. Supplement with targeted LinkedIn outreach to IT directors and compliance officers at healthcare and legal firms in the 50–500 employee range, using the IBM breach cost data ($4.45M average) as the cold outreach hook.

Secondary channel: **Zapier and Make (formerly Integromat) integration marketplace.** Publishing a WireOver integration on Zapier's marketplace (5M+ users as of 2024, per Zapier's published figures) enables discovery by operations and IT teams already automating workflows — a distribution channel unavailable to WireOver in 2014.

## Pricing strategy:

- **Free tier:** Up to 5 GB per transfer, 3 transfers per day, E2E encryption included, no audit logs, 7-day link expiry. Gating on transfer size and frequency — not on encryption — creates a natural conversion path as users hit limits, correcting WireOver's fatal pricing error of giving away unlimited transfers for free.
- **Pro tier ($18/month per user):** Unlimited transfer size, unlimited transfers, 30-day link expiry, basic audit logs. Priced above WeTransfer Pro ($15/month) on the strength of zero-knowledge encryption and no file size cap.
- **Team tier ($49/month per user, minimum 5 seats):** Full audit logs, SSO, admin dashboard, HIPAA Business Associate Agreement (BAA) available, priority relay routing. This is the tier WireOver's $40/month enterprise tier gestured at but never delivered — with the compliance documentation that regulated-industry buyers actually require.

## Differentiation vs. 2026 competitors:

Against Wormhole: enterprise compliance layer (audit logs, SSO, BAA) and explicit regulated-industry positioning. Against WeTransfer: zero-knowledge encryption on by default, no file stored on servers, compliance documentation. Against Aspera/IBM: browser-native zero-install experience, 10x lower price point, no server infrastructure required from the buyer. Against legacy MFT vendors (GoAnywhere, MOVEit): modern UX, no on-premise deployment, recipient-side zero-friction delivery. The positioning statement is precise: **"The only zero-install, zero-knowledge file transfer tool with enterprise compliance built in — for teams that can't afford a breach and can't afford Aspera."**
