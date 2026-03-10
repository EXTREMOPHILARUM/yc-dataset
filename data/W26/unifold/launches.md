# Launches

## Unifold – Universal deposit infrastructure for on-chain apps

**TL;DR**

Unifold is a **developer-first API + SDK** that makes it easy for any app to accept on-chain deposits – across any chain and token – with **less than 10 lines of code**. We handle the full deposit flow so teams can ship faster and give users a smooth experience that actually works.

If you’re building a consumer-facing on-chain product and want best-in-class deposits (or want to support more chains fast), we’d love to work with you.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97814&key=user_uploads/2866477/a3a77b36-7d14-4161-a12e-f9afd25df662)

## **The Problem**

Every modern blockchain app – prediction markets, exchanges, DeFi protocols, consumer platforms – hits the **same bottleneck**: deposits are slow, fragile, and a terrible experience.

Users don’t care about chain IDs or token standards, they just want to fund their account and use your product. But today, many platforms still force users through a maze of:

* chain switching prompts
* manual bridging flows
* token approvals
* figuring out whether their **USDC is the “right” USDC** (Solana vs Base vs Arbitrum vs Ethereum)

That confusion kills deposits. Users drop off not because they _don’t want_ to engage – but because the onboarding itself feels like a blocker. This is especially true for _time-sensitive_ products like prediction markets where speed _is_ product. By the time funds show up, the opportunity has passed.

## **Why This Happens**

Multi-chain deposits are _hard_. Tokens like USDC exist on dozens of networks with different contracts, wrapped versions, and incompatible standards. A user might hold “USDC” on one chain, but the platform only supports it on another. That mismatch turns a simple deposit into a support ticket and a lost user.

Existing tooling tackles parts of this (bridges, chain selectors, etc.), but none give platforms a **single, unified deposit layer** with consistent UX and routing logic built in. Developers end up re-implementing the same plumbing over and over.

## **Our Story**

Before Unifold, we built **wallet-as-a-service infrastructure** and were acquired by a leading crypto payments company, where we helped onboard **30M+ users** and supported major on-chain apps like **Phantom** and **Polymarket**.

When we later left the acquiring company, we began prototyping a consumer prediction market with a better on-chain UX. We expected trading to be the tough part, but during testing, users kept talking about how unusually smooth the deposit experience felt compared to everything else they had used in crypto. Then another prediction market reached out, currently **top 3 in weekly transactions behind Kalshi and Polymarket (Feb 2026)**, asking if they could use our deposit flow. 

That was the “aha” moment: even great on-chain products lose users at the _funding step_ because existing deposits are still fragmented and painful.

## **Solution**

<https://youtu.be/D5y9xklqaFI>

So we built **Unifold**, a universal deposit infrastructure for any internet platform that wants to accept on-chain money.

Unifold gives developers a single integration that handles deposits end-to-end:

* **cross-chain routing**
* **gas abstraction**
* **compliance checks**
* **settlement**
* **crypto + fiat deposits**

You can integrate in **less than 10 lines of code**, run it fully **headless** or with a customizable UI, and ship deposits natively across:

* **Web (React/NextJS)**
* **React Native (Expo)**
* **iOS (Swift)**
* **Android (Kotlin)**

We’re already working with ecosystems that don’t have strong deposit/onboarding support from existing providers, including **Algorand, MegaETH, and Thru**, and we’re excited to support more as they launch.

Most existing crypto deposit solutions are still **sales-driven**, gated behind volume minimums and long onboarding cycles. We’re building Unifold to be the opposite: **best-in-class docs, a clean integration, and a self-serve dashboard** so even small teams can get started fast.

If Stripe made it easy to accept card payments, **Unifold makes it easy to accept on-chain deposits.**

## **What our users (developers) are saying**

[**Alpha Arcade**](https://www.alphaarcade.com/) (Prediction Market on Algorand)

After integrating Unifold (30 minutes after checking the docs)

_“I just integrated the modal into our app locally and successfully deposited to Algorand wallet from Solana wallet. VERY smooth!! good shit” -_ Head of Engineering of Alpha Arcade

[**Lofty.ai**](http://Lofty.ai) (On-chain Nasdaq for real estate, YC S19)

_“HOLY that is smooth” -_ Co-founder of [**Lofy.ai**](http://Lofy.ai)

## **Ask / Call to Action**

If you’re building a consumer-facing on-chain product and want to give your users the best deposit experience or want to support more chains without rebuilding your stack, we’d love to work with you.

For more information, check us out at <https://unifold.io>.

DM us at [**https://x.com/unifold_io**](https://x.com/unifold_io) or reach out at [**hello@unifold.io**](mailto:hello@unifold.io) – we’re actively onboarding design partners.

Want to test out our deposit flows and provide feedback?

1. <https://ycstack.unifold.io> (deposit, buy tokens, play to win - Polygon)
2. <https://megaeth.unifold.io> (deposit to the latest L1 blockchain - MegaETH)
3. <https://trade.veromarket.xyz> (our prediction market with the deposit flow - USDC Solana)

## **The Team**

We are Timothy Chung, Quang Huynh, and Hau Chu, co-founders of Unifold.

Timothy studied computer science at Cambridge and Columbia. Timothy was also involved in the early days of Polymarket and co-led the initiative for a CBDC for the US Marshal Islands out of MIT. Afterwards, Timothy cofounded Streambird with Quang, the wallet as a service that was later acquired by a leading crypto payment company. Together, they built infrastructure that onboarded 30M+ users onto on-chain apps like Phantom and Polymarket.

Quang has 6+ years of experience building consumer-facing crypto and fintech products, from co-founding a wallet infrastructure startup (later acquired) to crafting authentication flows, consumer mobile apps, and UI/UX experiences that onboarded 30M+ users onto different platforms.

Hau has been building blockchain infrastructure since 2023 while completing his master’s at Cornell Tech. He worked at Solana Labs and later worked with Tim and Quang to scale wallets and DeFi infrastructure across 10+ blockchains.
