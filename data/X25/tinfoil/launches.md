# Launches

## Tinfoil: Verifiable Privacy for Cloud AI

Sending your most sensitive or proprietary data to OpenAI et al?

Sick of deals getting stalled during enterprise or government security reviews?

Hate deploying on various configurations of on-prem infrastructure environments?

Say less ✋

We’re [Tanya](https://www.linkedin.com/in/tanya-verma-130a23124/), [Jules](https://www.linkedin.com/in/jdrean/), [Sacha](https://www.linkedin.com/in/sacha-servan-schreiber-308341305/) and [Nate](https://www.linkedin.com/in/nate-sales/) from[ Tinfoil](https://tinfoil.sh/). What we’re building at Tinfoil sidesteps these concerns because we can host models while guaranteeing zero data access and retention.

We let you run powerful models like Llama, Deepseek R1 on cloud GPUs without you having to trust us – or the cloud provider – with your private data.

Since AI performs better the more context you give it, we think solving AI privacy will unlock more valuable AI applications, just how TLS on the Internet enabled e-commerce to flourish knowing that your credit card info wouldn't be stolen by someone sniffing internet packets.

https://youtu.be/wnwI22qT-QQ

**Who we are**

We come from backgrounds in cryptography, security, and infrastructure. Jules did his PhD in trusted hardware and confidential computing at MIT, and worked with NVIDIA and Microsoft Research on the same, Sacha did his PhD in privacy-preserving cryptography at MIT, Nate worked on privacy tech like Tor, and I (Tanya) was on Cloudflare's cryptography team.

 We were unsatisfied with band-aid techniques like PII redaction (which is actually undesirable in some cases like AI personal assistants) or “pinky promise” security through legal contracts like DPAs. We wanted a real solution that replaced trust with provable security, and addressed our personal frustration with the false choice between exploring cutting-edge AI capabilities and personal privacy.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcicUJrVGkJrvHFqW2CaNEpGzvSfbjySaAR3k-Q8fbf56JtXg8xAJa5MJrYn-RIdJjFirmZ4khWay_UpV6WhnZKZEE9ApI5HX97jRKGw4mJOTblXrujRY_9xcCvGPL139p2QaKd1g?key=xi6EV3GMAYXvlmorGP948w)

**The magic sauce**

Running models locally or on-prem is an option, but can be expensive and inconvenient. Fully Homomorphic Encryption (FHE) is not practical for LLM inference for the foreseeable future. The next best option is using secure enclaves: a secure environment on the chip that no other software running on the host machine can access. This lets us perform LLM inference in the cloud while being able to prove that no one, not even Tinfoil or the cloud provider, can access the data. And because these security mechanisms are implemented in hardware, there is minimal performance overhead.

Up until recently, secure enclaves were only available on CPUs. But NVIDIA confidential computing recently added these hardware-based capabilities to their latest GPUs, making it possible to run GPU-based workloads in a secure enclave.

Believe it when you see it, but Tinfoil has negligible performance overhead despite the strong security & privacy guarantees.

**Getting Started**

**The best part is you can start using confidential AI chat and inference with Tinfoil today!**

**Try our private chat: [tinfoil.sh/chat](http://tinfoil.sh/chat).**

[**https://www.youtube.com/watch?v=FuFszT0_vXk**](https://www.youtube.com/watch?v=FuFszT0_vXk)

**Build with our API:** Drop-in replacement for the OpenAI chat-completions API with Tinfoil

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfBq_bx4bvZAzdB9BTzMg9KSE8UB2bKQO5uqfF5eoZkEWZFUtlbFnZpeD-m_PwaCVgUWftTt3QDLTW-r84u2dvUEGQ0ddbbQuq082ClI48l2cY4jWX-kWG1G6ZfwjNh8GN-EdAVJg?key=xi6EV3GMAYXvlmorGP948w)

We support several popular open source models like Deepseek R1 70B, Llama3.3 70B, Mistral 3.1 24B. Missing your favorite model? Just ask us to add it!

Try out our free version running Llama3.3 70B in [Colab](https://colab.research.google.com/drive/1DhpUSmSWjxERnEo3U0qyAyApfcdIhvMv?usp=sharing).

See how Nate psychoanalyzes himself by sending all his iMessage chats to Tinfoil!

https://www.loom.com/share/2381c02ba51043528c6d3bdf61270bc0?sid=9ea0e955-ae68-4ce4-9c86-d06cab18d25c

**Deploy your AI Application**: Make your AI application enterprise-ready in a matter of minutes. Here's a demo of how you can use Tinfoil to run a deepfake detection service that could run securely on people's private videos:

https://www.youtube.com/watch?v=_8hLmqoutyk

We encourage you to be skeptical of our privacy claims. Verifiability is our answer. It’s not just us _saying_ it’s private; the hardware and cryptography let _you_ check. Here’s a guide that walks you through the verification process:[ ](https://docs.tinfoil.sh/verify)https://docs.tinfoil.sh/verification/attestation-architecture.

**The Ask**

If you think this sounds interesting, or too good to be true, contact us at [**founders@tinfoil.sh**](mailto:founders@tinfoil.sh)**!**

We’d love to hear from you, whether you’re a:

* startup looking to sell into regulated industries
* government agency that does everything on-prem but doesn’t trust your AI team to handle sensitive data
* neocloud trying to secure enterprise customers in regulated industries that don’t migrate from the big clouds to you
* company providing your employees dead-simple confidential LLM chat app

You can also learn more on our [**blog**](https://tinfoil.sh/blog), and subscribe to our [**LinkedIn**](https://www.linkedin.com/company/tinfoil/) and [**Twitter**](https://x.com/TinfoilAI) to follow updates!
