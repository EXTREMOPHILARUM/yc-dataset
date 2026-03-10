# Launches

## Cakework - Custom user code in any developer product

**tldr**

_We make it easy to run custom user code using APIs instead of infrastructure. Build extensibility directly into your developer product, or launch your own serverless cloud solution._

Hi friends, we're Jessie and Eric from [Cakework](https://www.cakework.com). We're ex-AWS engineers that got tired of managing infra and wanted our tools to do it for us. We started Cakework to bake serverless into every developer product and never have to host our own code again.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70142&key=user_uploads/461027/608b19e2-7cf0-4402-8173-aa280ba89b58)

[Jessie](https://www.linkedin.com/in/jyoung73/) - Senior Engineer that led development of AWS call center AI analytics and NLP services.

[Eric](https://www.linkedin.com/in/ericchen90/) - Engineering Manager that led a team of engineers, scientists, and clinicians in building AWS services for healthcare.

**Problem**

Modern developer experiences let users run custom code natively, so users can build extensions and applications without any devops. This can be anything from in-browser scripting to webhook handlers or web services that deploy from Github.

Building a platform to do this is hard because cloud services like AWS are designed by default to run your code, not your users'. You need to package your users code, handling dependencies and multiple languages. You need to provide logging, metrics, and metering. Serverless options like Lambda help with security and cost, but have restrictions on timeout and prevent you from using protocols like gRPC.

You’re basically building your own Heroku.

One of our early customers had given up on building their own serverless cloud solution. With us, they were able to launch in a week.

**How did we do it?**

Cakework is a set of simple APIs for building serverless directly into your developer product. You describe how you want to package and run your users' code, and use Cakework to build images from Github, CLI, or even a browser. You use our APIs to run that code securely, and show logs and metrics back to your users.

Here's a gif of Cakework in action with a developer SaaS tool that wanted their users to be able to run custom code on webhooks in their system.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70142&key=user_uploads/461027/72dd917a-6381-4859-8341-6d278385f1d0)

You can build your own in-browser scripting with multiple languages!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70142&key=user_uploads/461027/7a15ec40-7de5-4641-8a73-87b612c1ba7c)

**Asks**

We're onboarding customers in early access now. If you or someone you know is working on a developer product and want to run your user's code, reach out at [eric@cakework.com](mailto:eric@cakework.com)!
