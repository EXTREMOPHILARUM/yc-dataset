# Launches

## EdgeBit - Secure your software supply chain

tl;dr: [EdgeBit](https://edgebit.io) automatically inventories software dependencies, ensures they are trusted, and monitors vulnerabilities – securing your software supply chain. For security teams, we help you meet new compliance requirements about the libraries and packages in your products. For engineers, we make vulnerability investigation/patching streamlined, so you can get back to writing code.

Hi everyone, we are Rob, Russell and Eugene, the team behind [EdgeBit](https://edgebit.io).

We’re on a mission to make software secure by default. EdgeBit deeply understands how your app is built, what makes it up and how it’s running. That knowledge builds up trust to make developers lives easier, and your entire server fleet more secure.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69144&key=user_uploads/230598/b3341e0d-c53a-49b4-a31a-c5d9a5fa6c8c)

Left - [Eugene](https://www.linkedin.com/in/eugene-yakubovich-4640604/) - Chief Architect and low level hacker. He worked on pathfinding algorithms at Lyft, container networking at CoreOS and performance optimization in his high frequency trading days.

Center - [Rob](https://www.linkedin.com/in/robszumski/) - CEO and product leader. He was a Director of Product at Red Hat working on the OpenShift/Kubernetes platform after their acquisition of CoreOS (YC S13).

Right - [Russell](https://www.linkedin.com/in/russellhaering/) - CTO and master of backend systems. He ran security engineering at Okta after their acquisition of ScaleFT, the zero trust access management startup he cofounded.

## The Problem: securing software still feels like throwing problems over a wall

Security teams have important work to do – meeting a maze of compliance rules against a constantly moving target of dependencies, frameworks and deployment platforms. Automation is key, but security teams aren’t experts in each app, so “open a ticket for any vulnerability found” is a typical workflow. This is a firehose for app teams, and tickets don’t contain the context needed for a speedy investigation.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69144&key=user_uploads/230598/201aef87-ad12-4842-9b9d-f423f8ccd315)

Looking beyond compliance, real attacks are happening via software dependencies. For a single library, it’s tricky to securely download, integrate, sign and verify it…and very hard for 100s of dependencies across multiple apps. An enterprise can use [40,000 open-source software packages](https://www.theregister.com/2023/02/05/supply_chain_security_efforts/) each bringing another 77 dependencies.

An end-to-end system across the build→scan→run→monitor is required to stop these attacks. Dependencies are fragmented across OS packages, standalone binaries and containers, but a single view across all is required to understand the full attack surface.

## EdgeBit: Map your supply chain from build to production in real time

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69144&key=user_uploads/230598/9872f16b-3980-4c64-bf6f-fe47a5f82262)

EdgeBit builds up context and trust by observing your software from build until deployment to your server fleet. How does it work? Install EdgeBit into your build pipeline and your server fleet/Kubernetes cluster via a tiny agent to immediately enable teams to bring vulnerabilities under control:

* Security: track workload signatures, provenance and prevent malicious modification
* Compliance: build a real time inventory tracked back to the software’s bill of materials (SBOM)
* Engineering: prioritize vulnerability investigation based on deep context
* Enterprises: track patching across teams. The next log4j will come, and it’s a huge endeavor without real time inventory across all tech stacks and packaging formats.

## Try out EdgeBit

Security teams can [install EdgeBit](https://edgebit.io) to track their supply chain and even help compliance managers do their job without getting engineering involved. Remove frustration from your vulnerability response program by connecting your teams together and take control back from noisy scanners.

Securing supply chains is just a step in our journey. Using trust profiles between systems is key to a zero trust security posture. We’d love to chat with you about acute compliance needs or long term security goals of your organization.
