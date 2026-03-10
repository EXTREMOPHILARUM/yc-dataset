# Launches

## BuildJet - Change 1 line, get 2x faster & cheaper GitHub Action builds

### **⚡️ TL;DR**

Hey, this is Adam & Lian from [@BuildJet](https://www.ycombinator.com/companies/buildjet)

BuildJet makes GitHub Actions faster, by running the workflows on our Gaming CPU cloud. You still keep everything GitHub Actions, we just replace the underlying GitHub Actions runner with our Gaming CPUs.

\
**Change 1 line, and get 2x faster and cheaper builds.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69746&key=user_uploads/730963/214d6b00-fec2-4f4a-8a6b-132c63f8c6cb)

### **GitHub Actions is slow**

* **Developers are wasting their time –** Waiting for GitHub Actions to get a green checkbox on a PR, is wasteful and extremely tedious.
* **GitHub Actions runner hardware is old and slow –** GitHub Actions use old and slow machines from Azure. Some of your workflows run on servers from 2015.
* **GitHub Actions use the wrong type of hardware** – CI workflows are usually computing intense, and specifically require high single-core performance. GitHub Actions uses server CPUs, which generally have low single-core performance.

### **Our Solution**

GitHub Actions rely on server CPUs from Azure. **Server CPUs mostly have low single-core performance.** This is where BuildJet differentiates itself, with its fundamentally different approach to computing, using dedicated **high-performance gaming CPUs** that all have a very high-single core performance.

This provides an inherent speed advantage for BuildJet, even without software optimizations. High single-core performance is the key to a fast CI process, and BuildJet's gaming CPU cloud is optimized to deliver just that.

Take a look at our at the chart below, **MacBook Pro 2015 hardware beating GitHub Actions runner in 2022.** It’s yet another instance where you can see the limitation of using server CPUs in tasks that need high single-core performance.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69746&key=user_uploads/730963/40b07ca7-7828-4ae1-9c6b-20b8d1ea0026)

### **Founding Team**

Lian and I, first met at a data privacy startup in Berlin in 2014, where we developed a strong working relationship and launched many products together. After leaving that company, we joined a German startup that runs the biggest market research panel in Germany, Civey, with Adam as CPO and Lian as CTO. When scaling the company, we quickly learned **the great impact gaming CPU's have on CI speed.**

### **Next Steps**

Head over to <https://buildjet.com/for-github-actions>, sign up in 1 minute and start accelerating your GitHub Actions workflows.

If you have any questions about your CI pipeline, don’t hesitate to reach out to [adam@buildjet.com](mailto:adam@buildjet.com), and I’ll make sure to help you out!
