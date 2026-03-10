# Build Plan: Cryptoseal 2026

## Overview

CryptoSeal was a San Francisco-based YC S11 company that built a consumer privacy VPN and a compliance-oriented enterprise VPN on top of an ambitious Trusted Computing vision; the consumer product shut down preemptively in October 2013 after the Lavabit case established that US government pen register orders could compel SSL key surrender, and Cloudflare acqui-hired the team in June 2014, retiring all products within two weeks.

The rebuild thesis is not to re-enter the consumer VPN market — that ship has sailed to NordVPN — but to finally commercialize CryptoSeal's original, deeper vision: a developer-facing secrets management and confidential computing platform where cryptographic architecture makes compelled disclosure structurally impossible, not merely legally promised. What has changed is everything the original team needed but didn't have: commodity confidential computing hardware, a mature secrets management market that IBM paid $6.4B to own, and a zero-knowledge design playbook that makes privacy and enterprise compliance genuinely non-contradictory. The rebuild is HashiCorp Vault meets AWS Nitro Enclaves, built for the developer who needs to prove to their enterprise customer that even they can't read the secrets.

---34:T90a,

## Why Now?

The single most important change since CryptoSeal's failure is the commoditization of hardware-attested confidential computing. In 2011, Ryan Lackey had to build custom Trusted Computing infrastructure from scratch to guarantee server-side application integrity to remote users. In 2026, that infrastructure is a cloud API call. AWS Nitro Enclaves (launched November 2020), Azure Confidential Computing (GA December 2020), and Google Confidential VMs (GA September 2020) provide hardware-rooted execution environments where even the cloud provider cannot inspect running workloads. CryptoSeal's founding vision — cryptographically attested, tamper-evident secret management — is now buildable by a two-person team in a weekend, not a multi-year infrastructure project.

The market that CryptoSeal was too early for has since produced billion-dollar validation. HashiCorp Vault, which launched in 2015 (four years after CryptoSeal's founding), was acquired by IBM for $6.4 billion in 2024. AWS Secrets Manager, launched in 2018, is now used by hundreds of thousands of AWS accounts (exact figure not publicly disclosed by AWS). The secrets management market is estimated at approximately $1.4 billion in 2024, projected to reach $4.2 billion by 2030 (MarketsandMarkets, 2024 — note: third-party market sizing figures should be independently verified before use in investor materials). Tom Sparks himself noted in 2018 that EnvKey was succeeding at exactly what CryptoSeal had attempted in 2011.

The legal architecture has also shifted. The two-party relay model — used by Cloudflare WARP (launched April 2019) and Apple iCloud Private Relay (launched September 2021) — structurally defeats the Lavabit-style SSL key compulsion that killed CryptoSeal Privacy, because no single provider holds both user identity and traffic simultaneously. This design pattern is now well-documented and implementable.

Distribution channels that did not exist in 2013 are now primary: the AWS Marketplace has over 300,000 active customers (AWS, 2023); the GitHub Marketplace reaches 100 million+ developers directly; and SOC 2 compliance requirements have made secrets management a procurement checkbox for any enterprise SaaS vendor, creating a pull-based sales motion that CryptoSeal's 2013 market entirely lacked.

---

## Current Market Analysis

**Market size:** The global secrets management market was approximately $1.4 billion in 2024 (MarketsandMarkets — verify independently). The adjacent confidential computing market is estimated at $5.4 billion in 2024, growing at roughly 45% CAGR through 2029 (Grand View Research — verify independently). For context, neither category existed as a named market segment when CryptoSeal operated in 2011–2014.

## Competition map and gaps:

- **HashiCorp Vault (now IBM):** The category-defining product, but the IBM acquisition has introduced enterprise sales motion friction, slower release cycles, and pricing that starts at $0.03/hour for Vault Dedicated — accessible for large enterprises, punishing for growth-stage startups. The open-source version requires significant DevOps investment to self-host securely. Gap: no confidential computing attestation layer; IBM's enterprise focus leaves developer-first onboarding underserved.

- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager:** Native cloud offerings with deep platform integration, but each is cloud-locked. A secret in AWS Secrets Manager cannot be attested to an Azure workload. Gap: multi-cloud and hybrid environments — which represent the majority of enterprise deployments (Flexera 2024 State of the Cloud: 87% of enterprises use multiple clouds) — are poorly served by single-cloud native tools.

- **Doppler / Infisical / EnvKey:** Developer-friendly secrets managers with good UX, but none offer hardware-attested confidential computing integration. They store and distribute secrets; they cannot prove to a relying party that the secret was processed inside a tamper-evident enclave. Gap: the attestation layer that satisfies enterprise security reviewers and regulators is absent.

- **Cloudflare Zero Trust:** Excellent network-layer product, but not a secrets management platform. Gap: application-layer secret lifecycle management is out of scope.

**Demand signals:** The SOC 2 Type II audit requirement, now standard for any B2B SaaS vendor selling to enterprise, explicitly requires secrets management controls. This creates a compliance-driven pull that did not exist in 2013.

**Defensibility analysis:** AWS, Google, and Azure could add attestation-backed secrets management to their native offerings — and this is a genuine risk that must be stated honestly. The structural defense is multi-cloud neutrality: a developer who needs to attest secret handling across AWS and Azure simultaneously cannot use either provider's native tooling. The rebuild's moat is the cross-cloud attestation layer, not the secrets storage itself. If the product is built as a single-cloud wrapper, it will be commoditized. If it is built as the attestation coordination layer across clouds, it occupies a position that no single platform incumbent is structurally motivated to fill.

---

## Recommended MVP

## Feature 1: Multi-cloud attested secret delivery

A secrets manager that delivers secrets to workloads only after cryptographically verifying, via hardware attestation (AWS Nitro, Azure CVM, GCP Confidential VM), that the requesting environment is unmodified and running the expected code. Unlike HashiCorp Vault, which trusts the network perimeter, this product trusts the hardware attestation report. Unlike cloud-native tools, it works across AWS, Azure, and GCP simultaneously. This is the core feature CryptoSeal's Trusted Computing vision pointed toward but could not build in 2011.

## Feature 2: Attestation audit log with compliance export

Every secret access generates a cryptographically signed attestation receipt — a verifiable record that the secret was accessed inside a known-good enclave, not by a rogue process or a compromised operator. Exports map directly to SOC 2 CC6.1, HIPAA §164.312(a), and PCI DSS Requirement 8 controls. The original CryptoSeal had no compliance export layer; this feature makes the product a procurement accelerant, not a procurement obstacle.

## Feature 3: Developer CLI with zero-config local simulation

A local development mode that simulates attestation flows without requiring actual enclave hardware, so developers can build and test attestation-aware applications on a MacBook. This addresses the cold-start adoption problem: developers will not instrument their code for a workflow they cannot test locally. Doppler and Infisical have demonstrated that CLI-first onboarding is the correct developer acquisition motion.

**What you will NOT build:** A consumer VPN. A network-layer zero-trust product. A general-purpose PKI. A compliance consulting service. Any product that requires the company to hold user traffic in transit.

## Success metrics:

- 500 developer accounts with at least one attested secret delivery within 90 days of launch
- 10 paying enterprise customers (defined as >$1,000/month ARR) within 6 months
- Attestation verification latency under 200ms at p99 (table-stakes for production adoption)
- Zero security incidents involving operator access to plaintext secrets (the core promise; one failure ends the company)

**Cold-start note:** This product does not depend on network effects or local density. Value is delivered to the first user on day one. The adoption risk is integration complexity, not empty-network syndrome — which is why the local simulation CLI (Feature 3) is non-negotiable for MVP.

---

## Go-to-Market Strategy

**Target customer:** Security-conscious engineering teams at Series B–D B2B SaaS companies (50–500 engineers) that are actively pursuing SOC 2 Type II certification or have recently failed a security audit on secrets management controls. These companies are large enough to have a dedicated security engineer or engineering manager who owns the audit, small enough that a $500–$2,000/month tool does not require a VP signature, and motivated by a concrete compliance deadline rather than abstract security interest. Geographically, target US-first where SOC 2 is the dominant framework.

**Primary distribution channel:** Bottom-up developer adoption via GitHub Marketplace and direct CLI install, converting to enterprise contracts through the compliance audit trigger. Tactics: (1) publish open-source attestation verification libraries under a permissive license to seed developer awareness; (2) sponsor security-track sessions at KubeCon and AWS re:Invent, where the target buyer is present; (3) build a free SOC 2 secrets management checklist that ranks in search for "SOC 2 secrets management" — a high-intent query with commercial content gaps as of early 2025.

**Pricing:** Free tier for up to 3 users and 10,000 secret accesses/month (enough for a startup to complete a POC and pass an initial audit). Growth tier at $500/month for up to 25 users with full attestation audit logs. Enterprise tier at $2,000+/month for unlimited users, SSO, custom attestation policies, and SLA. 

Stress-test against free alternatives: AWS Secrets Manager costs approximately $0.40/secret/month plus $0.05 per 10,000 API calls — effectively free at small scale. A developer team can accomplish basic secrets management for under $20/month using native cloud tools. The rebuild's price is only defensible if the attestation layer and multi-cloud audit export deliver something the free alternative structurally cannot: a cryptographic proof of secret handling integrity that satisfies an enterprise security reviewer. If the product cannot articulate that proof in a 60-second demo, the $500/month price will not survive procurement. The free tier exists precisely to let developers generate that proof before the sales conversation begins.

**Differentiation vs. 2026 competitors:** HashiCorp Vault (IBM) is the incumbent but is becoming enterprise-only and single-cloud-comfortable. The rebuild wins on multi-cloud attestation, developer-first onboarding, and pricing that does not require an IBM enterprise agreement. Doppler and Infisical are the developer-friendly alternatives but have no attestation layer — the rebuild's SOC 2 compliance export is a direct wedge into accounts those products already occupy.
