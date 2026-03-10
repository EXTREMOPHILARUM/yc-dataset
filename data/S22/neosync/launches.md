# Launches

## Neosync - PII Detection and Anonymization in Free-form Text

We’re an open source data anonymization and synthetic data platform that companies like Intel, Siemens, C2FO, Alasco and others use to anonymize their sensitive production data and sync it to lower-level environments.

Today, we’re launching a new product designed to detect and anonymize PII data in free-form text.

These are two main use cases:

1. **Detecting and redacting PII data before sending it to an LLM for inference**. If you’re building agentic systems or working with LLMs and sensitive data, you shouldn’t be sending your sensitive data to those LLMs. You can now use our API to first detect and anonymize that data and then send it to your LLM provider.
2. **Detecting and redacting PII data before training.** You generally want to avoid training a model on PII (especially if others will be using it). You can use our API to detect and redact free-form text in training data so that you’re not training it on PII.

For example:

The text:

```
{ text: "Dear Mr. John Chang, your physical therapy for your rotator cuff injury is approved for 12 sessions. Your first appointment with therapist Jake is on 8/1/2024 at 11 AM. Please bring a photo ID. We have your SSN on file as 246-80-1357. Is this correct?"}
```

Would be transformed to:

```
Anonymization result: '{"text":"Dear Mr. \u003cREDACTED\u003e, your physical therapy for your rotator cuff injury is approved for 12 sessions. Your first appointment with therapist \u003cREDACTED\u003e is on \u003cREDACTED\u003e at \u003cREDACTED\u003e. Please bring a photo ID. We have your SSN on file as \u003cREDACTED\u003e. Is this correct?"}' 
```

You can also customize this with custom allow/deny lists and even custom recognizers.

We’re already working with companies in Healthtech and Fintech on this and would love to open it up to more companies. If you’re interested in trying it out, shoot me a note at [**evis@neosync.dev**](mailto:evis@neosync.dev), and I can get you a sandbox and free credits to trial it.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85312&key=user_uploads/89898/ea3d02aa-68e7-4a21-8bd0-c35f9786490e)

## Nucleus - The Modern Backend Platform for Microservices

**Nucleus is a platform that helps developers build, deploy and manage a production-grade microservices architecture in minutes.**

### **Problem**

Building a microservices architecture is complex and can easily take 6+ months. From our experience at our own companies and from talking with many engineering teams, we see that most engineering teams try to build this platform from scratch by piecing together AWS or GCP building blocks. The problem is that this is difficult, incredibly time consuming and if not done right, can be a massive security risk. You shouldn’t have to be an infrastructure and security expert to have a secure, scalable architecture. That’s where Nucleus comes in. 

**Who uses Nucleus?**

Companies that want to use microservices but don’t want to spend months building out their infrastructure. These can be early stage companies that are just starting out, to mid-market companies that are architecting for growth.

**How it works**

Nucleus is delivered through an interactive CLI that helps you declaratively define your service. Here is an example of the declarative file:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64124&key=user_uploads/980900/fb0612aa-3ab3-4e0f-8a48-aa76dd40fb8b)

Here is how to deploy a microservice:

1. Install the CLI through homebrew and sign up for an account.
2. Write your service’s code or use one of our example repos to quickly get started.
3. Declaratively define your service using the interactive Nucleus CLI. All services are automatically authenticated and secured. Manage things like environment variables, secrets, and logging, all from the CLI.
4. Deploy your service, and it will be available in less than 2 minutes.

**Can I try it?**

Yes! We just kicked off our private beta and would love to have you test the system to the limits. To get started, just shoot us your email so we can add you to the allowlist. Easy as that!

**The Ask**

1. Try us out and give us feedback. We obsess over with the developer experience, and want to make it as intuitive and magical as possible.
2. Talk to us about your backend :) We’re focused on microservices and want to learn more about what you like, don’t like or don’t know about them. Collectively, we have 25 years of experience in engineering & product. We can be a sounding board or help you design your architecture.

Have questions? Shoot me an email at [evis@usenucleus.cloud](mailto:evis@usenucleus.cloud) or feel free to book some time directly here: <https://calendly.com/evis1/30min>
