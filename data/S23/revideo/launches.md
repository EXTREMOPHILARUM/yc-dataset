# Launches

## Revideo - Create videos with code

### TLDR:

We are building [Revideo](https://re.video/), a web-based open-source framework that lets you create videos using the animation library Motion Canvas. It exposes basic video & audio editing functionality through a typescript API and lets you render videos with dynamic inputs. You can find our code on [**Github**](https://github.com/redotvideo/revideo)!

### **The Problem:**

We believe that AI will drastically change how people produce video and that huge amounts of video will soon be created in an automated manner. Initially, we wanted to build applications in this space ourselves and started to work on a few ideas. For example, we worked on an AI-based app to automatically create highlight videos for Twitch streamers, as well as a platform that lets companies A/B test video ads.

While building these products, we noticed that we weren’t really happy with the tooling we used. Most video editing frameworks lacked essential features, and the tools we liked were not open source. Therefore, we decided to build Revideo.

### **The Solution:**

We built Revideo by extending the animation library Motion Canvas and adding features that are essential for automatically creating videos. These features include support for audio, substantially faster video rendering, and an API for programmatically rendering videos with dynamic inputs.

Here is a code example of a basic video created with Revideo:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80105&key=user_uploads/1023703/4f0ca7c8-30c6-402a-a087-2b2829275c40)

The code above produces the following result:

<https://youtu.be/FGeujyec7_g>

### **Our Asks:**

* Check out [Revideo](https://github.com/redotvideo/revideo) on Github and give us a ⭐ if you like it!
* We’d love to chat with anyone building video products! If you are building one or know people who do, please reach out ❤️

## Haven: Fine-tune and run open source LLMs super fast ⚡

# TLDR:

We are excited to launch [Haven](https://haven.run/)’s fine-tuning platform for open source LLMs!

* Haven lets you fine-tune open source LLMs such as Llama or Mistral without writing code or setting up infrastructure. We charge $0.004/1k training tokens, and you get $5 in free credits after signing up
* You can host models for testing with <1s cold start times. We achieve this by running hundreds of model adapters on a single GPU and hot-swapping them based on user requests (will write more about this in a blog post)

You can get started [**here**](https://app.haven.run/) - alternatively, reach out to [**hello@haven.run**](https://app.haven.run/) or watch our [demo](https://www.youtube.com/watch?v=XpyVKUyt7k8) if you want to learn more!

### **The Problem**

Over the last months, we’ve identified two big pain points that make it hard to work with open source models:

1. Open source models work best when they are trained for specific use cases, but the fine-tuning process with existing tools is super annoying. We have found that most of our time is spent setting up infrastructure to go from finishing a training run to actually testing our models, rather than actually writing code and improving our models
2. Hosting custom models is expensive. Running a single Llama-7B model in float16 requires at minimum an A10 GPU, which costs $700+ per month. To run ten or a hundred specialized models for common tasks, this would mean that we have a monthly AWS bill of $7,000 or $70,000, respectively.

### **The Solution**

Haven’s platform offers a super simple way to fine-tune models without managing infrastructure or writing code, and to test and run them with low costs and without any additional work.

We are able to provide a super short feedback loop of going from training to running a fine-tuned model by hosting multiple lora adapters in parallel. This makes it possible for us to host hundreds of fine-tuned models on-demand on a single GPU. For our users, this reduced model cold start times to <1s and internally, we are able to host a single fine-tuned model for a couple of dollars per month. We also enable our users to export their model weights to Huggingface, so that they can run models entirely on their terms.

### **Our Ask**

Feel free to check out our [**platform**](https://app.haven.run/) and give us feedback! After signing up, you’ll receive $5 in credits to train a couple of models :) We are also happy to answer questions at [**hello@haven.run**](https://app.haven.run/)

## 🔮 Haven - Run LLMs on Your Own Cloud

**TL;DR:** Haven makes it easy to deploy LLMs in your GCP / AWS environment. We provide the user experience of serverless solutions like Replicate or Huggingface Inference Endpoints - but instead of running your models on Haven’s servers, we just manage your infrastructure for you. This gives you full control over your data and you get to use your precious cloud credits!

### **🤕 The Problem**

Many companies want to use large language models but do not want to rely on third-party providers as it makes them dependent on external services and comes with significant privacy risks.

However, deploying models in-house is just not easy: engineers have to figure out CUDA environments, write and containerize efficient serving code, and expose it as an API server. And let’s not even talk about scalability…

Haven solves this problem. We offer the simplicity, reliability, and scalability of third-party providers while allowing our users to securely run models on their own infrastructure.

### **🤯 How It Works**

Haven is built on top of Kubernetes, which makes it easy to scale and reliable in production settings. Deploying a model with Haven consists of just three steps:

**1\. Upload a Service Account Key**

Uploading a service account key gives Haven permission to manage your cloud resources for you. Under the hood, Haven will now set up a Kubernetes cluster running in your cloud environment.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73716&key=user_uploads/1023703/6b35bcd0-f0f5-4f4b-b3ab-dbb6a46261ff)

**2\. Configure Your Deployment**

You can now choose your model, select the GPUs you want it to run on, and configure the scaling behavior of your deployment. Haven will accordingly set up the model in your Kubernetes cluster.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73716&key=user_uploads/1023703/59c94edb-14a5-4e4e-b173-a4b19223ebdb)

**3\. Enjoy Your Model**

Your LLM is up and running in minutes! Our deployments offer super-fast inference and advanced features like input batching for efficient serving. This way, you can immediately integrate them into your application.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73716&key=user_uploads/1023703/773c461a-05ba-48b2-ba96-6b4c88d23cbf)

### **💪 The Team**

We’re Konstantin and Justus. The two of us met as freshmen in college, and have since built multiple projects together.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=73716&key=user_uploads/1023703/95a23ea8-c105-4d8d-af62-f2a527bb50f7)

[Justus](https://www.linkedin.com/in/justus-mattern-a04230184/) is an AI researcher and has been working on LLMs since 2020. As a member of AI labs at UC Berkeley and ETH Zürich, he has published multiple papers at leading research conferences.

[Konstantin](https://www.linkedin.com/in/konsti-h/) has already been a full-time software engineer before starting his university studies. At Germany’s biggest social networking company, he built infrastructure handling requests from millions of daily users.

### **💜 Our Ask**

**Sign up **[**here**](https://vkg6c80ex61.typeform.com/to/IMCFY5Cf)** to work with us!**

We are working closely with our users to fully understand the needs of companies aiming to integrate LLMs into their products. Beyond giving access to our deployment tool, we partner with early customers to evaluate their use cases and fine-tune models for their needs. If this sounds interesting, sign up for early access or contact us at [hello@haven.run](mailto:hello@haven.run)!

**Refer us to companies looking to use LLMs!**

If you have connections at companies looking to use LLMs, we’d highly appreciate introductions! You can reach us at [hello@haven.run](mailto:hello@haven.run).
