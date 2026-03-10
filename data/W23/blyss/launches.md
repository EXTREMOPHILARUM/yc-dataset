# Launches

## Blyss - the SDK for privacy.

## **TLDR:** Homomorphic encryption offers much stronger privacy guarantees than anyone thought possible. Blyss is the future of privacy, available today as a [developer-focused API](https://blyss.dev/).

We are Samir and Neil, the founders of Blyss.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69550&key=user_uploads/75138/64e460e5-9627-4f23-b3ec-57be1d24ac9e)

## 😧 Problem: outside of FAANG, privacy is stuck in the ‘90s🕺

Privacy is a competitive advantage. There’s a billboard on the 101 explaining how WhatsApp can’t read your messages, millions of consumers use VPNs to secure their everyday browsing, and Apple doesn’t finish a keynote without touting new, frontier-pushing privacy practices. 

But unless you’re at big tech, the most powerful new privacy tools are almost completely inaccessible. Chrome and Edge use homomorphic encryption to scan unsafe URLs and check passwords, but a startup wanting to offer similar features would need a team of PhDs to build them in-house.

## 🛠️ Our solution: cutting-edge privacy, as a service

The [Blyss SDK](https://blyss.dev/) offers developers a key-value store with unusually strong privacy guarantees. Create S3-like buckets, fill them with data, and then make cryptographically secure retrievals. No entity, not even the Blyss service itself, can learn which items are retrieved from a Blyss bucket.

Private retrieval is a simple but powerful new primitive. Using it,

* Password managers can check if you’ve been exposed in a data breach, without learning anything about your passwords
* Browsers can resolve domain names privately, without revealing every website you visit to DNS servers
* Code scanners can safely check repos for vulnerabilities, without ever seeing customer codebases or the scan results

People are building lots of new web apps with Blyss - try some of the best ones at the [Blyss playground](https://playground.blyss.dev)!

# 🙇 The ask

## 🧑‍💻 Developers:

Try [our SDK](https://blyss.dev/) - it’s a self-serve, cloud storage service (feels just like S3), that transparently handles encryption and privacy for you. And if it isn’t quite clear how to fit privacy into your app, we’ll help you!

## 🕵️ Privacy-conscious users:

Tell us about apps/services that feel icky because they collect too much data. It may not be obvious how to fix them, but your gut feelings on privacy are super valuable to us.

## 🕴️ Bonus:

If you know companies that are trying to make privacy their competitive advantage (password managers, VPNs, etc), introduce us ([founders@blyss.dev](mailto:founders@blyss.dev))!

## 👯 About us

We met eight years ago on Day 1 of freshman year at Stanford; we’ve been best friends since. Neil was previously at Apple working on ML; Samir worked at Yubico on applied security, and before that did research on homomorphic encryption with Dan Boneh. We [published](https://eprint.iacr.org/2022/368) the fastest-ever scheme for private retrieval at a top cryptography conference (Oakland). Now, we’re working to make advanced privacy technology available to everyone.
