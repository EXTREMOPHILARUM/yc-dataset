# Build Plan: BarSense 2026

## Overview

By 2026, BarSense is a B2B2C parental control platform purpose-built for families managing neurodivergent children—autism, ADHD, sensory processing differences. The product sits between the blunt instruments of Apple Screen Time and Google Family Link and the surveillance-heavy monitoring of Bark. It combines a distraction-free launcher, AI-powered contextual content filtering, and visual routine scheduling—all shareable with therapists and educators who are already part of the child's care team.

The viability shift: Apple and Google now expose documented APIs for third-party parental controls (Screen Time API, Family Link API). This eliminates the structural threat that killed Kytephone. Simultaneously, the neurodivergent parenting community has matured into a recognizable segment with documented willingness to pay for tools that reduce anxiety and support executive function—not just surveillance.

Distribution bypasses the app store entirely. Occupational therapists and special education coordinators become referral partners. A family sees their child's OT using BarSense in session, asks about it, and converts. This B2B2C motion solves the cold-start problem that generic parental controls face: you're not competing on features in a crowded app store. You're embedded in an existing trust relationship with a professional who understands the child's specific needs.

## Why Now?

The single most important change since Kytephone's 2014 failure is the arrival of sanctioned, documented OS-level APIs for third-party parental control apps. Apple's Screen Time API (introduced iOS 12, September 2018) and Google's Family Link API now give third-party developers the same deep device integration that Kytephone had to hack together using undocumented Android hooks — and critically, these APIs work on both platforms. The original Android-only strategy was a rational response to a real technical constraint; that constraint no longer exists. A rebuilt product can reach the full smartphone market from day one.

The business model question that Kytephone never publicly answered has been empirically resolved by successors. Bark, Qustodio, and Circle have each raised $10M+ and built subscription businesses at $10–15/month per family, proving that parents will pay recurring fees for parental controls. The global parental controls software market was valued at approximately $1.1B in 2022 and is projected to grow significantly through 2030 (per industry reports cited in the research; specific CAGR figures are not available in the source material). The demand signal Drashkov described in 2012 as "only a matter of time" has fully materialized.

The average age of first smartphone ownership dropped from approximately 12 years old in 2012 to approximately 10 years old by 2020, per Common Sense Media research. This expands the addressable market and extends the product's useful life per family — parents now need solutions for younger children, for longer.

The decisive new technical capability is LLM-based content analysis. GPT-4 (March 2023) and Claude 3 (March 2024) can classify whether a child's text message, photo, or browser query is age-appropriate with high accuracy and low latency. This creates a genuine technical moat that platform-native controls — which remain blunt, keyword-based instruments — cannot easily replicate.

Distribution channels unavailable to Kytephone now exist at scale. T-Mobile's FamilyMode and Verizon's Smart Family demonstrate that carriers actively upsell parental controls at point of sale. A rebuilt product can pursue white-label carrier partnerships rather than relying on app store discovery alone.

---

## Current Market Analysis

The parental controls market has transformed from a nascent, unproven category in 2012 into a validated, growing software vertical. The global market was valued at approximately $1.1B in 2022 (per industry reports cited in the research report); specific market size figures from 2012 are not available in the source material, making a precise then-vs-now comparison impossible. What is documentable is the structural validation: multiple companies have built sustainable subscription businesses in the space post-2015, and carrier-level products have normalized the category for mainstream consumers.

## Competition map and gaps:

- **Bark** (~$14/month): Focuses on AI-powered monitoring of social media and messaging for concerning content (bullying, self-harm, explicit material). Its core weakness is that it is a monitoring-and-alert product, not a control product — parents receive notifications after the fact but cannot proactively restrict access. It also requires children to connect their accounts voluntarily, creating a compliance gap with younger children.

- **Qustodio** (~$55–$100/year): Broad feature set across platforms, strong web filtering and screen time controls. Its weakness is UI complexity — the parent dashboard is dense and requires significant setup time. It targets a technically comfortable parent demographic and does not serve families with children who have developmental or cognitive differences.

- **Circle** (hardware + subscription, ~$10/month): Router-based approach provides network-level filtering. Its weakness is that it only works on home Wi-Fi; controls evaporate the moment a child leaves the house or uses cellular data. The hardware dependency also creates a friction-heavy onboarding experience.

- **Google Family Link / Apple Screen Time**: Native platform controls are free and improving, but remain blunt instruments — they offer app time limits and content category filters, not contextual, AI-powered content understanding. They also cannot monitor cross-platform behavior or provide the specialized interface customization that parents of children with developmental disabilities require.

**The gap:** No major competitor has specifically targeted families of children with autism, ADHD, or developmental disabilities — a segment with documented high willingness to pay, strong word-of-mouth networks through special education and occupational therapy communities, and specific needs (predictable interfaces, distraction-free environments, routine enforcement) that generic parental controls do not address.

---

## Recommended MVP

## Core Feature 1: Cross-Platform Managed Launcher (iOS + Android)

A simplified, distraction-free home screen built on Apple's Screen Time API and Google's Family Link API that parents configure remotely. Unlike Kytephone's Android-only implementation, this works on both platforms from launch, doubling the addressable market. Unlike platform-native controls, it provides a fully customized visual interface — large icons, minimal chrome, predictable layout — that parents can tailor to their child's cognitive and sensory needs. This is the foundational feature that makes everything else possible.

## Core Feature 2: AI-Powered Contextual Content Monitoring

Using GPT-4-class LLM inference (available via API as of March 2023) running on-device where possible and server-side where necessary, the product classifies incoming messages, browser queries, and image content for age-appropriateness in real time — not by keyword matching, but by semantic understanding. Parents receive a weekly digest and immediate alerts for high-severity flags. This is the primary technical moat: platform-native controls use keyword blocklists; this product understands context. Bark monitors after the fact; this product can intervene proactively.

## Core Feature 3: Routine Scheduling with Visual Timers

Parents define daily routines — school hours, homework time, bedtime — and the device interface changes automatically to reflect what's permitted in each window. Crucially, the child sees a visual countdown timer showing when the next permitted activity begins, rather than a blank lock screen. This feature directly addresses the needs of children with autism and ADHD, for whom predictability and visual structure reduce behavioral distress. No current competitor offers this with the specificity required for this population.

## Core Feature 4: Therapist and Educator Sharing Portal

A read-only dashboard view that parents can share with occupational therapists, special education teachers, or pediatricians — showing screen time patterns, routine adherence, and flagged content categories (not content itself). This creates institutional distribution through clinical and educational networks, solving the customer acquisition problem that Kytephone never addressed. It also creates switching costs: once a family's care team is integrated into the product, churn drops.

## What we will NOT build at MVP:

- Social media monitoring integrations (Bark's territory; requires account access and creates privacy complexity)
- Hardware (Circle's weakness; adds cost and friction)
- Teen-focused monitoring products (Kytephone's Kytetime pivot diluted focus; we stay under-12 until unit economics are proven)
- Carrier white-label partnerships (pursue post-Series A, not MVP)

## Success metrics:

- 500 paying families within 90 days of launch (validates willingness to pay before scaling)
- Monthly churn below 3% (industry benchmark for sticky SaaS; above this signals product-market fit failure)
- 40% of acquired families referred by a therapist, educator, or parent community (validates institutional distribution thesis)
- Net Promoter Score above 50 among families of children with developmental disabilities (the core niche)

---

## Go-to-Market Strategy

## Target customer segment:

Parents of children aged 6–12 with autism spectrum disorder, ADHD, or other developmental and cognitive differences who are receiving or have received occupational therapy or special education services. This is a narrow, specific segment — not "all parents" — chosen because it has the highest willingness to pay, the strongest word-of-mouth infrastructure (parent Facebook groups, IEP networks, OT practices), and the clearest unmet need that generic competitors have not addressed. The research report explicitly identifies this as the segment where Kytephone found organic traction without even trying; a rebuilt product makes it the primary target rather than a footnote.

## Primary distribution channel:

Occupational therapists and special education coordinators as referral partners, not app store discovery. The go-to-market motion is B2B2C: identify 50 OT practices and 20 special education departments in the first six months, offer free family accounts for their clients in exchange for a referral relationship, and build the therapist portal (Feature 4) specifically to make this relationship sticky. This mirrors how successful assistive technology products distribute — through clinical trust networks rather than paid acquisition. Secondary channel: targeted presence in established parent communities (Facebook groups for autism parents, CHADD for ADHD families) where peer recommendations carry high credibility.

## Pricing strategy:

## Differentiation vs. 2026 competitors:

Bark monitors but doesn't control; Qustodio controls but doesn't understand context; Circle works only at home; Google and Apple provide blunt instruments without clinical-grade customization. The rebuilt product is the only one built specifically for children whose needs require more than a generic content filter — and the only one with a distribution strategy rooted in clinical and educational trust networks rather than app store rankings. The AI content layer (GPT-4-class, March 2023+) is the technical moat; the therapist portal is the distribution moat; the specialized population focus is the brand moat.
