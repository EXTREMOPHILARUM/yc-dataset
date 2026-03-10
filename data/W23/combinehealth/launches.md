# Launches

## UpTrain AI: Enterprise-grade tooling to ship LLM applications confidently

**TLDR:** Hi, everyone. We are Shikha & Sourabh, and we help companies ship LLM applications confidently. We provide enterprise-grade tools to evaluate, experiment, monitor, and test LLM changes easily. We provide seamless collaboration, and [being OSS](https://github.com/uptrain-ai/uptrain), we provide tons of customization and self-hosting capabilities to satisfy your data governance needs.

### **PROBLEM 🤔:**

**“Building LLM prototypes is easy, but productionising them is damn hard.”** (You might have guessed it given we are building an LLMOps platform 😉). So, LLMs are unpredictable and dealing with them is complex and messy:

1. You spend countless hours manually reading through your chatbot responses or analyzing the actions of your automation agents.
2. Fixing the prompt to solve one failure case opens a can of worms and can make previous answers go bad.
3. Improvements are always reactive - users complain, and then you go back and fix them, eroding their trust and your credibility. 
4. Collaborating with your team is messy - countless Google Docs and Slack channels are created to debug failure cases.

### **SOLUTION 💡:**

UpTrain provides the most advanced LLMOps platform to streamline the complete process. It goes beyond just giving scores or monitoring logs but provides a single platform to identify, debug, and collaborate to improve the accuracy of your LLM applications. 

* We give reliable scores over various metrics (both LLM-based and classical NLP ones) as well as allow you to define custom ones to evaluate your full LLM pipeline comprehensively.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77918&key=user_uploads/588096/c9c6e03f-be80-4799-a783-05074f0d72ea)

* We run root cause analysis to identify if it is a retrieval issue, if your context requires reranking, if the LLM is unable to utilize the context, or if certain instructions are not being followed.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77918&key=user_uploads/588096/117c15f7-c03b-4821-b033-8ab4b0d6e3df)

* State-of-the-art techniques for automated prompt optimization, automatic eval generation, finding common topics among failure cases, etc., to act as your LLMOps co-pilot.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=77918&key=user_uploads/588096/e190b97e-49f9-45be-9dba-ec8233e3f2fe)

Best of all, UpTrain is open-source under Apache 2.0 with more than 1700 GitHub stars and adoption among developers across multiple Fortune 500 companies. Being OSS, UpTrain has tons of customization options and can be deployed in your secure cloud environment, fulfilling your data governance requirements.

### **OUR ASK 🙌:**

1. If you are building LLM applications, we would love to get feedback on [our platform](https://uptrain.ai/).
2. If you are doing evaluations with home-grown solutions, let us know what they are. We would be happy to add them to [our OSS](https://github.com/uptrain-ai/uptrain).
3. Join [our Slack community](https://join.slack.com/t/uptraincommunity/shared_invite/zt-1yih3aojn-CEoR_gAh6PDSknhFmuaJeg) to stay updated on our progress.

If you want a demo or want to chat more, please [book a call here.](https://calendly.com/uptrain-sourabh/30min)

## UpTrain - Open-source tool to observe your ML models ⚙️ 🔧

**TL;DR:** UpTrain is an open-source ML observability and refinement tool. It helps data scientists observe how their ML models are performing in production and continuously improve them over time by automatically retraining them on cases where the model accuracy was low.

**Hi everyone!** Sourabh, Vipul, and Shikha here, and we’re the team behind UpTrain. 

Sourabh (CEO), previously founder at fitness tech, where he spent most of his time improving their AI models rather than, well, working out 🏋️

Vipul (CTO), previously worked at Meta and Bytedance, where he was busy applying his doctorate knowledge (yes, the Ph.D. kind) to improve their ML models 🔭

Shikha (CMO), an ex-VC, where she witnessed the magnanimity of AI problems from the inside of her portfolio companies and this is where she got her eureka moment 🔔

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69166&key=user_uploads/588096/a21aa066-6198-48c0-8c27-354f6e4ba73a)

### **Problem (The Origin Story 📖)**

During the last 7+ years of building and deploying ML models, we have been constantly frustrated due to a lack of good tools that could answer one simple question - “Are our models working as expected in production?“

Sourabh first experienced this issue while working on self-driving cars at a Fortune 500 company. Then again he faced similar issues at his startup. The only way the model issues were highlighted was through reading loads of customer complaints, and it was excruciating to see their (hard-earned) revenue churn due to model degradation **😩.** 

Coincidentally, Vipul was solving the same problem at the big techs, where he built internal observability tools and optimized model retraining processes. The three founders spoke to 100+ ML practitioners to validate their hypothesis and got a unanimous yes! In fact, during one of the user interviews, we learned that an innocuous bug in the model deployment code led to 3+ weeks of wasted debugging efforts and losses of millions of revenue dollars 🤯

We are building UpTrain to prevent you from experiencing the same agony!

### **The Solution 💡**

UpTrain is built specifically for Machine Learning. We natively support all the things an ML practitioner requires to observe and improve their models.

✅ Complete visibility into your model’s online health via real-time dashboards 

✅ Automatically collects outliers and edge cases 

✅ Identifies data distribution shifts 

✅ Monitors quality of object embeddings

✅ Model explainability 

✅ Continuously retrains and improves your model 

Cherry on the cake, we are Open-source! Some of the biggest AI-first startups are adopting UpTrain to fulfill their ML observability needs.

### **How to use UpTrain 🤔**

Install UpTrain from pip, just tell it what all you want to observe, and UpTrain handles all the complexities in the background. Something as simple as below:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69166&key=user_uploads/588096/3f9f9f08-df84-480d-af42-62a6af0950c2)

We DO NOT require you to change any part of your production pipelines and readily integrate with all major ML libraries and tools. In fact, we are running a limited beta program where we provide a no-strings-attached pilot and do all the heavy lifting to ensure seamless integration of UpTrain in your systems. Ping us to know more!

### **Our Ask 🙌**

* Interested? Try us [out](https://uptrain.ai/) or book a demo [here](https://calendly.com/uptrain-ai/30min?month=2023-02) 🔥
* To follow our progress, do star our [project](https://github.com/uptrain-ai/uptrain) on Github (show us some love - it’s free ❤️) 
* Know someone who needs ML observability, connect us 🔗

Feel free to reach out to any of us with questions, bugs, requests, etc. at [sourabh@uptrain.ai](mailto:sourabh@uptrain.ai)
