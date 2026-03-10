# Launches

## Cedana - Real-time save, move and resume for compute

Hey, we’re Neel and Niranjan from [Cedana](https://cedana.ai/?utm_source=cedana&utm_medium=yc&utm_campaign=launch).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73681&key=user_uploads/77597/b1097aa9-66f2-4253-8243-63e63d5c23e9)

### **The Problem**

Losing work because of infra problems is painful. Imagine you have a long-running compute job and the instance fails. Your 20-hour job finished but because your pipeline was misconfigured you have to restart it from scratch.  

Burning cash is stressful.  Poor utilization results in your inference jobs costing more.  If you’re managing a cluster of 1,000s of GPUs, poor utilization leaves money on the table even while demand is skyrocketing.    

Cold start times impact your customer satisfaction and their reliance on your solution.  

Limited GPU access makes it difficult for you to innovate, and finding GPUs can be a full-time job of constantly identifying, evaluating, and adapting different vendors.    

### **Our Solution**

Cedana is real-time migration for compute.  We automatically schedule and move workloads across instances and vendors without interrupting progress or breaking anything.

There are several critical benefits:

* Utilization is maximized to save costs and eliminate idle resources.  
* Job-level SLAs dynamically allocate compute between inference and training, prioritizing costs, latency, and performance based on preferences.  
* Avoid re-running jobs from scratch due to infra, pipeline, or memory failures. Jobs continue their progress in the event of infra failure or spot revocation.
* Access planet-scale compute through vendor aggregation
* Solve the cold start problem by enabling fast auto-suspend-resume 
* Spot management that migrates and provisions new instances automatically upon revocation or failure.

  

OpenAI, Meta, Microsoft, and Databricks employ some of these methods internally and we’re bringing them to everyone.

### **How it works**

[Cedana](https://cedana.ai/?utm_source=cedana&utm_medium=yc&utm_campaign=launch) is available as an [open-source package](https://github.com/cedana/cedana-cli) and as a [managed service](https://www.ycombinator.com/launches/JAP-cedana-real-time-save-move-and-resume-for-compute). 

* Cedana needs no code modification and works with Linux processes or containers
* Current use cases and customers range from AI Training and Inference, High-Performance Compute, DevTools, ML Ops platforms, and Computational Biology.
* It automatically provisions and manages infra with your existing credentials. Our managed service can leverage our vendor relationships if preferred.

Here’s a 1m30s [demo video](https://www.youtube.com/watch?v=KC4STzSQ_DU)

### **Our Team**

Our team has built real-world robotics and large-scale computer vision systems across a number of places including 6 River Systems/Shopify and MIT.  We’ve led the development, commercialization, and scale of NLP for clinical workflows used in the delivery of patient care.   Our team’s publications span computer vision, computer graphics, robotics optimization, and spacecraft/aerospace controls, with patents in AI use cases for grid energy management, optimal battery control, and healthcare. 

### **We kindly ask**

* Give Cedana a try! [Check out our Github Repo](https://github.com/cedana/cedana-cli)
* Please support us with a Github star
