# Launches

## ➿ Preloop - Deploy your ML models in hours instead of weeks

**Tl;dr:** [Preloop](https://www.preloop.com/) automatically translates your ML training scripts into production services, handling the creation of the training pipeline and REST endpoints. This means that science teams can focus on developing new models while cutting deployment times from weeks to just a few hours (or less). We’re building Vercel for model deployments.

—

Hey everyone, we’re [Tejas](https://linkedin.com/in/tejashosangadi) and [Nikith](https://linkedin.com/in/nikithhosangadi) and we’re building Preloop. Tejas previously worked as a data scientist and software engineer at several companies, including Amazon and most recently EvolutionIQ, often leading 0-1 projects on newly established teams. Nikith has experience as a software engineer building multi-tenant distributed systems, most recently working at AWS on the networking team.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78894&key=user_uploads/1310033/6f2948a3-73ad-43eb-829c-0b23006cd26b)

Our goal is to unshackle scientists from the repetitive tasks that accompany their model deployments and empower science teams to move faster. 

## **😫 The problem**

Data scientists hate the work associated with deploying their models. Science teams spend anywhere from a couple of weeks to over two months deploying their models. Assuming that a team deploys 10 models a year and each model takes 2 weeks on average to deploy, this is 20 weeks of science time spent just on deployments. 

The biggest bottlenecks to quick deployment are a lack of easy-to-use tools and delays caused by handing off deployments to a separate team.

## **🪄 Our solution**

Preloop automates the tedious and repetitive tasks associated with deploying and using your ML models, including creating the training pipeline and inference endpoints, autoscaling based on demand and retraining. We provide an easy-to-use CLI in addition to a dashboard to monitor and track your models. It works with major ML packages like xgboost, torch, and scikit-learn, with broader support on the roadmap.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78894&key=user_uploads/1310033/3a401fe4-e051-45c2-a3b9-98bd8b492abd)

## **🔍 How it works**

We scan through your existing script, identifying key information about the data, transformations, and the model being trained. This is used to construct both the training and data pipelines, as well as the inference endpoints that serve your model. 

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78894&key=user_uploads/1310033/976dd0ad-2492-43a4-a674-eb3618536144)

We also handle auto-scaling, observability, and versioning, so that you can train and deploy, but just as easily roll back unintended model changes. We have support for on-prem deployments for teams that have stronger security requirements.

## **🤔 Why are we building this?**

As a data scientist, Tejas noticed that scientists (including himself) loved experimenting and building models but hated deploying them. More importantly, he witnessed that it often took multiple weeks before they were in production. There was a lack of a more automated solution to handle the deployment process, and even tools like Sagemaker require tons of boilerplate to work.

We want to make it easier to deploy models, so that teams can move quicker, and scientists can focus more on science. 

## **🙏 Our ask**

* Intros to data science and ML managers at mid to large-size startups as well as large enterprises. 
* If your science team struggles with lengthy deployment times, please reach out to us by emailing [founders@preloop.com](mailto:founders@preloop.com), or by booking a meeting [here](https://outlook.office.com/bookwithme/user/27ea63c6cc9c4d398ba6525a9c0e6b25@preloop.com/meetingtype/ZKpbyV0QyU2cya_WNaNuJw2?anonymous&ep=mlink).
