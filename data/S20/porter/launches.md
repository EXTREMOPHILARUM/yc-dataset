# Launches

## Porter - Turn your AWS account into Heroku

**TLDR -** [Porter](https://porter.run) is a Platform as a Service (PaaS) that runs in your own cloud. It brings the magical experience of deploying your applications with a few clicks into your own cloud account. After a year since we closed down our self-serve flow, we are opening Porter back up for self-serve today.

* [Sign up here](https://dashboard.getporter.dev) and start deploying applications on your own infrastructure that scales with you.
* [Claim $10,000 in credits](https://gcpjnf9adme.typeform.com/to/lHMQdJYb) if your company is enrolled in YC Startup School. Along with the AWS credits you can claim from Startup School, this deal effectively lets you deploy on a PaaS for free - it’s like using Heroku with your AWS credits!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71916&key=user_uploads/323071/cc2f3fac-340f-4f39-9e4d-533f7ab40053)

## **What is Porter?**

Hi everyone,

We are Trevor and Justin from [Porter](https://porter.run/). We first launched Porter almost 2 years ago - a lot has happened since then, and today we’re excited to re-launch our product and share our story so far.

**For those of you who aren’t familiar:**

_Porter is a Platform as a Service (PaaS) that runs in your own cloud. You just link up your Git Repository, and Porter will deploy it into your own AWS/GCP/Azure account. Under the hood, it runs your apps on a Kubernetes cluster that’s been battle-tested against real life incidents so you can scale on the same kind of infrastructure that growth-stage companies run without any DevOps work._

## **The PaaS Graduation Problem**

Many startups first get started on a PaaS like Heroku to move quickly without worrying about infrastructure. However, most of these companies end up migrating to their own cloud infrastructure at some point, because their applications need more flexibility as they scale (they “graduate” from their PaaS provider). Moving off production applications off a PaaS is time-consuming and difficult, and hosting all of your infrastructure on in-house solutions of a single PaaS vendor comes with the risk of getting locked in.

Porter hits the sweet spot between simplicity and flexibility by allowing startups to deploy into their own cloud infrastructure with the convenience of a PaaS. Get started on Porter just as easily as you would on a traditional PaaS, then customize your infrastructure freely as you grow. Under the hood, Porter runs a Kubernetes cluster with the same kind of architecture that growth-stage companies build out with an army of infra engineers, so you don’t have to worry about outgrowing the infrastructure.

## **Opening back up for self-serve**

**Porter was originally open for self-serve when we first launched.** We onboarded a lot of companies through the self-serve flow in the beginning, but after a few months quickly realized that we didn’t have the resources to properly manage the Kubernetes clusters that are distributed across different cloud accounts at scale.

This led us to the difficult decision of shutting down our self-serve function and focusing on larger growth-stage companies that warrant the scalability of Kubernetes. This strategy worked well - we incrementally moved upmarket, quickly grew our revenue, and even onboarded a few public companies.

After a year since the initial launch, however, something fascinating started happening; some of the seed-stage companies we’ve onboarded in the beginning started to reach true scale on Porter. [Writesonic](https://www.ycombinator.com/companies/writesonic) (YC S21), who first started on Porter during their YC batch, now runs a Kubernetes cluster with 1.5 _Terabytes_ of RAM without a single full-time infra engineer. [Memberstack](https://www.ycombinator.com/companies/memberstack) (S20) routinely handles more than a million requests a day processing >$5M in payments every month, and [OneShop](https://www.ycombinator.com/companies/oneshop) (S21) runs 60 different integration services on Porter. The list goes on.

Because we had been building a product for larger companies, our platform evolved on many axes to accommodate projects that are running at true scale - and we have lived long enough to witness companies who initially had tiny workloads on Porter organically grow into a scale that we’ve never even imagined.

We took the learnings from this experience and are opening Porter back up for self-serve with two key improvements:

1. With a new onboarding and deployment flow, getting started on Porter is truly just as easy as using a traditional PaaS like Heroku or Render. **The only difference** is that you need to connect your cloud account and wait 30 minutes for infrastructure to be provisioned.

   ![](https://www.ycombinator.com/media/?type=post&id=71916&key=user_uploads/323071/890e143d-5d10-4138-9c8e-aeb05a89d420)

2. We’ve built out an internal system that oversees and manages the Kubernetes clusters that are distributed across different cloud accounts, so we are now ready to support a self-serve motion at scale.

You can [get started here](https://dashboard.getporter.dev). If you’re enrolled in YC Startup School, [claim $10k in credits here](https://gcpjnf9adme.typeform.com/to/lHMQdJYb).
