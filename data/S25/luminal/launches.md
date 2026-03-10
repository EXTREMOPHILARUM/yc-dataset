# Launches

## Luminal - PyTorch for Production

Hey we’re Joe, Jake, and Matthew, cofounders of Luminal. 

Luminal is an [open-source](https://github.com/jafioti/luminal) ML compiler that generates blazingly fast CUDA kernels and makes deploying AI to production one line of code. We’re already powering research at Yale, production workloads at VC-backed startups and several research labs.

https://youtu.be/Rgo15NY9K-8

**TLDR:**

* Our drop-in upgrade to PyTorch automatically generates complex GPU kernel code, like Flash Attention, with zero hand-engineering
* We provide truly serverless deployments; no idle costs or cold starts.
* By not relying on pretrained LLMs or hand-written optimizations, we can reliably speed up any model

**Ask:**

* [Book a meeting](https://calendly.com/accounts-luminalai/30min) if you write PyTorch and want your models to run fast
* [Star us on github](https://github.com/jafioti/luminal) and try Luminal right now on your own laptop!
* Email us if you know someone who runs custom models: [contact@luminalai.com](https://mailto:contact@luminalai.com)

—

### **The problem:**

Most people running their own AI models are lighting money on fire and don’t even know it. AI teams are frustrated when moving their model from dev to production. They either fall into dependency hell or kill their model’s speed. Today, **companies waste millions of dollars on GPU engineering** teams to optimize new models before they can be served to users.\
—

### **How Luminal solves it:**

**Luminal replaces a process that companies pay GPU engineers $300k+ a year to do.**

Our key insight is that by treating optimization as a search problem, we’re able to automatically discover extremely complex optimizations in minutes that would take a GPU expert weeks. We use a series of ‘rewrite rules’ to create millions of graphs to describe your model, generate kernel code for each and then search for the fastest one based on runtime.

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfNzLo_zAkiYY_fsEQMseEQZXpdFjn0chhSJ8Wn-0WOkSHGblAi1XseXLIbZsiim6z8_AiWxx6wuzTuCQYfNe2ELulijuOBR5b_1x4-kzEoxEoxutW0qv127MHbl1Lu6YLIJBfP_A?key=gRJ545K4hfVVtN0eX-o_ZQ)

_Example of a complicated kernel on the left that Luminal automatically sped up, on the right._

Luminal is:

1. **Closing the research → engineering gap.** Because we auto-generate optimized GPU code directly from your PyTorch, a brand-new model can go from research notebook to production in hours instead of weeks
2. **Writing blazing fast models.** Luminal generates kernels that would take a seasoned GPU engineer weeks of painstaking profiling and tuning to write.
3. **Future-proofing AI for new chips**. We can rerun our compiler on fresh hardware to get new optimal kernels so you're never out of date.

—

### **You should reach out if:**

* You’re an AI researcher or ML engineer
* You’d like to lower your compute bill by **tens of thousands of dollars a month**
* You work at a company that runs their own **custom models**

If you want your team spending more time making the world’s best models and less time optimizing hardware and cloud infrastructure, we’re for you!

—

### **The Team:**

[Joe](https://www.linkedin.com/in/joe-fioti-24a986189/) - ex Intel, every Intel chip sold has the AI accelerator Joe worked on. He has extensive experience optimizing performance at the silicon level.

[Matt](https://www.linkedin.com/in/matthewjgunton/) - ex Amazon where his software handled finding and automatically fixing issues within the global inventory network 24/7

[Jake](https://www.linkedin.com/in/jake-stevens-/) - ex Apple Jake worked on imaging at Apple for your iPhone. He’s been a founder (with an exit) and head of growth at another startup that he grew to \~$5M ARR.

Send us an email: [contact@luminalai.com](https://mailto:contact@luminalai.com)

[Book a call with us](https://calendly.com/accounts-luminalai/30min)

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd1hRLOasxYQ38r0AmMN9fTC9-BatUjGjE9-BXM21-w8PRvhBJVeYAc3pWlLPVlmTtnP3jG9Pa5HmUIGTYaZ93ClC-M-CRx0nkNw-DgS3Wh28xWXaUzXVwL_XPCNUL8JyTd_9FmBA?key=gRJ545K4hfVVtN0eX-o_ZQ)
