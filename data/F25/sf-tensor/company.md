---
name: SF Tensor
slug: sf-tensor
batch: F25
status: Active
one_liner: Infrastructure for AI labs to focus on research.
website: "https://sf-tensor.com"
team_size: 4
year_founded: 2025
twitter_url: "https://x.com/sftensor"
linkedin_url: "https://www.linkedin.com/company/sftensor"
industries:
  - B2B
  - Infrastructure
regions:
  - Unspecified
is_hiring: true
yc_partner: Harj Taggar
---

# SF Tensor

> Infrastructure for AI labs to focus on research.

AI researchers should be pushing the boundaries of what's possible with new architectures and training methods. Instead, they waste weeks configuring cloud infrastructure, debugging distributed systems, and optimizing their GPU code. We know because we lived it: While training our own models across thousands of GPUs earlier this year, we spent more time fighting our infrastructure than doing actual research.

That's why we're building two things. First, Elastic Cloud: a managed platform that automatically finds the cheapest GPUs across all providers, handles spot instance preemption, and cuts compute costs by up to 80%. Second, automatic kernel optimization that makes training code run faster by modeling hardware topology, often beating hand-tuned implementations.

The problem is that getting high performance across different hardware is genuinely hard. NVIDIA's CUDA moat exists because writing fast kernels requires deep expertise. Most teams either accept vendor lock-in or hire expensive kernel engineers. Our goal is to break the CUDA moat.

The compute bottleneck is the biggest constraint on AI progress. NVIDIA can't manufacture enough GPUs, and their monopoly keeps prices astronomical. Meanwhile, AMD, Google, and Amazon are shipping capable alternative hardware that nobody uses because the software is too hard. We're breaking that moat. If we succeed, anyone will be able to train state-of-the-art models without thinking past their PyTorch code.
