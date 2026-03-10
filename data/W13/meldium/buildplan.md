# Build Plan: Meldium 2026

## Overview

Meldium 2026 targets IT-aware founders and ops leads at B2B SaaS companies (15–150 employees) drowning in SaaS sprawl and manual access control. The product is a lightweight identity layer: MDM-deployed browser extension for credential sharing, one-click offboarding that revokes access across all apps simultaneously, and a SaaS discovery dashboard that surfaces shadow IT. It's not trying to be Okta—it's solving the specific pain of teams too small for dedicated IT but too large to manage passwords in a spreadsheet.

The market shift is technical, not behavioral: browser extensions are now enterprise-deployable through Intune and Jamf, eliminating the 2013 barrier that made this category hard to distribute. Combined with the explosion of SaaS tools (average company now uses 100+ apps vs. 20 in 2014), the offboarding problem has become acute. One employee departure shouldn't require IT to manually revoke 50+ logins.

Go-to-market is founder-to-founder: direct outreach to B2B SaaS founders via LinkedIn and Slack communities, emphasizing speed of deployment (extension installs via MDM in hours, not weeks) and the visceral win of one-click offboarding. Land at $150–200/month per team, expand to larger cohorts as the34:T85b,

## Why Now?

The single most important change since Meldium's retirement is the collapse of the browser extension deployment barrier. In 2013–2014, enterprise IT departments routinely blocked or restricted third-party browser extensions, making Meldium's Chrome/Firefox-only architecture a hard ceiling on upmarket expansion. Today, Microsoft Intune and Jamf Pro—the two dominant MDM platforms covering an estimated 60%+ of managed enterprise endpoints (exact 2026 market share data unavailable)—allow administrators to silently push, configure, and enforce browser extensions across entire device fleets from a central policy console. The IT resistance that constrained Meldium's distribution is structurally gone.

The second critical enabler is the maturation of zero-knowledge cryptographic tooling. Meldium's split-credential architecture—where employees could authenticate but not extract passwords—required significant custom engineering in 2013 and extensive customer education. Today, open-source libraries implementing zero-knowledge encryption (as standardized by 1Password's Secret Key model, released 2018, and Bitwarden's open-source implementation, available since 2016) reduce that engineering investment dramatically and give buyers a familiar vocabulary for evaluating the security model.

Third, the SaaS management platform (SMP) category has been independently validated by capital markets. Torii raised $50M Series B (2022), Zluri raised $20M Series B (2022), and BetterCloud has raised over $185M cumulatively—collectively proving that IT and finance buyers will pay for centralized SaaS visibility and access governance. Meldium's original "open federation layer" thesis, which Founders' Co-op described in 2013 as the company's true ambition, is now a funded, named category with established buyer budgets.

Distribution channels unavailable to Meldium now include the Okta Integration Network (7,000+ app listings with direct access to Okta's SMB and mid-market customer base) and the Microsoft Azure Marketplace, which surfaces identity-adjacent tools directly to IT administrators managing Entra ID tenants.

---

## Current Market Analysis

The identity and access management market has grown from an underdeveloped SMB niche in 2013 into a multi-billion-dollar category with validated enterprise buyer budgets. Okta's market capitalization has exceeded $10 billion, and 1Password for Business raised at a $6.8 billion valuation—both confirming that the demand Meldium identified in 2013 was real and large. The global IAM market was valued at approximately $16 billion in 2023 and is projected to exceed $34 billion by 2028 (MarketsandMarkets, 2023), though SMB-specific segment sizing within that figure is not publicly broken out.

## Competition map and gaps:

- **1Password for Business** — Market leader in SMB password management. Weakness: primarily a credential vault, not a provisioning or governance layer; SCIM support is limited to a narrow set of identity providers; no native SaaS spend visibility.
- **Okta** — Dominant enterprise identity provider. Weakness: pricing starts at $2/user/month for Workforce Identity but implementation complexity and minimum contract sizes effectively exclude companies under 100 employees; no shared-credential model for apps lacking SAML/OIDC support.
- **Rippling** — Emerging unified HR/IT platform with app provisioning. Weakness: identity is a feature within a broader HR suite, not a standalone product; requires full Rippling adoption to access provisioning capabilities; overkill for companies not ready to consolidate HR.
- **Zluri, Torii, BetterCloud** — SaaS management platforms with access governance features. Weakness: positioned as IT operations tools, not security products; pricing and complexity target 500+ employee organizations; weak on shared-credential management for apps without SSO support.

**The gap:** No current product serves the 10–200 employee company that needs (a) shared credential management for apps that don't support SAML, (b) lightweight provisioning and deprovisioning without an HR system dependency, and (c) SaaS spend visibility—in a single, self-serve product priced below $500/month. This is precisely the gap Meldium occupied in 2013, and it remains structurally unaddressed in 2026.

**Demand signals:** Rippling's rapid growth in the SMB IT segment and 1Password's $6.8B valuation both confirm sustained buyer appetite. Reddit communities (r/sysadmin, r/msp) consistently surface complaints about offboarding gaps for non-SSO apps—a direct echo of the problem Meldium solved.

---

## Recommended MVP

## Core Features:

## Shared Credential Vault with Zero-Knowledge Architecture

A centralized vault where administrators store credentials for SaaS apps that lack SAML/OIDC support, using a zero-knowledge encryption model (built on Bitwarden's open-source SDK or equivalent) that allows employees to authenticate without ever seeing or extracting the underlying password. This is Meldium's original core feature, rebuilt on modern open-source cryptographic foundations that reduce engineering cost by an estimated 60–70% versus a custom implementation. Unlike 1Password for Business, the vault is explicitly designed for shared team credentials with role-based access, not individual password storage.

## MDM-Deployed Browser Extension

A Chrome and Edge extension (covering 85%+ of enterprise browser market share as of 2024, per StatCounter) packaged with Intune and Jamf deployment manifests so IT administrators can push it silently across managed devices without end-user action. This directly eliminates Meldium's primary 2013 distribution friction. Unlike Meldium's original extension, this ships with pre-built MDM configuration profiles, reducing IT deployment time from hours to minutes.

## Automated Offboarding Workflow

A one-click offboarding flow that revokes an employee's access to all provisioned apps simultaneously and rotates shared credentials for apps where the departing employee had visibility. This addresses the highest-urgency use case in the target segment—the security risk of a departing employee retaining access to shared accounts. Unlike Rippling's offboarding, this requires no HR system integration and works for companies without a formal HRIS.

## SaaS Discovery and Spend Dashboard

A lightweight dashboard that surfaces shadow IT by scanning SSO login events and browser extension activity, showing administrators which apps are in use, by whom, and at what estimated cost. This positions the product within the validated SaaS management category (Torii, Zluri) without requiring the full implementation complexity those platforms demand. Exact cost data accuracy will depend on integration depth and is a known limitation to communicate transparently to buyers.

**What we will NOT build in MVP:** SAML/OIDC identity provider functionality (Okta's core), HR workflow automation, mobile app support, or a consumer-facing tier. These expand scope without serving the core buyer.

## Success metrics:

- 100 paying teams within 6 months of launch
- Average contract value ≥ $150/month (vs. Meldium's $79–$199 range)
- Offboarding workflow used within 30 days of signup by ≥ 60% of accounts (activation signal)
- Net Revenue Retention ≥ 110% at 12 months (expansion via seat growth)

---

## Go-to-Market Strategy

**Target customer segment:** IT-aware founders and operations leads at B2B SaaS companies with 15–150 employees, no dedicated IT department, and 20+ SaaS tools in active use. This is the segment Meldium originally served—companies too large to manage access informally but too small for Okta's implementation overhead. The specific trigger event is a bad offboarding experience: a departed employee retaining access, or a shared password not rotated after a departure. This segment is reachable without enterprise sales and has demonstrated willingness to pay for self-serve security tools (evidenced by 1Password for Business adoption in this cohort).

**Primary distribution channel:** Product-led growth via the Okta Integration Network and direct outreach to r/sysadmin and r/msp communities, supplemented by content targeting "employee offboarding checklist" and "shared password management" search queries—terms with documented high commercial intent (exact search volume data unavailable but category is well-established). The Okta Integration Network listing surfaces the product to IT administrators already managing identity, providing warm distribution unavailable to Meldium in 2013.

**Pricing strategy:** Per-seat SaaS pricing at $8/seat/month (billed annually), with a minimum of 10 seats ($80/month floor) and no artificial ceiling. This corrects Meldium's structural error—the $199/month cap for 250 users that made enterprise expansion uneconomical. A 50-person company pays $400/month ($4,800 ACV); a 150-person company pays $1,200/month ($14,400 ACV). This pricing is justified by the offboarding risk reduction value proposition, which is quantifiable in security incident cost terms, and positions the product above 1Password for Business ($4/seat) on value while remaining below Okta's full identity platform cost.

**Differentiation vs. 2026 competitors:** Unlike 1Password, the product is built for shared credentials and team provisioning, not individual vaults. Unlike Okta, it requires no implementation project and works for apps without SAML support. Unlike Rippling, it requires no HR system and can be deployed in a single afternoon. The MDM-native extension deployment is a specific, demonstrable differentiator that no current SMB-focused competitor has made a primary feature.
