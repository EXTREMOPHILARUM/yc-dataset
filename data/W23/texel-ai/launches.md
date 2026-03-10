# Launches

## Texel: Optimizing AI and video pipelines

**tl;dr: Texel makes your AI infrastructure 10x more efficient. We do this by providing tools and APIs that allow you to quickly encode or decode media and optimize models for inference.**\
\
💸 **The problem:**\
Many companies run inference on media, to do things like generate images or detect events in scenes. **Running inference is expensive both in compute and cost, and video decoding and encoding is too.**

Most developers use the best tools available to optimize inference and media processing in isolation, but shuffling the data between these pipelines is slow. As an example, four different inference pipelines means first decoding a video frame and then sending it to each of four GPUs running different models and finally compositing all the frames before re-encoding.

**😎 The solution:**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69917&key=user_uploads/1188792/4bdc96f4-6c64-44a8-bc65-c07bd88e8437)

Vanilla PyTorch running Stable Diffusion (left), Texel-accelerated version (right)\
\
We optimize the entire pipeline for you, from input to inference to output, by providing APIs that allow you to control the features you want to activate and taking care of the data flow and scaling behind the scenes. You can bring your own custom models that we optimize, cutting down on inference time and reducing GPU memory size. If you want to just optimize inference, training on media, or encode a video, that’s totally fine and we can do that for you! 

In the example mentioned above, the video decode, all four models, and the video encode would be streamlined to run on as few GPUs as possible. **With these optimizations, editing images and videos with AI can become real-time.** **You’ll also save money by using less GPUs.**

**📖 The story:**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=69917&key=user_uploads/1188792/97257823-69f1-4c89-a8b4-af5bae7b0b92)

Rahul (left) and Eli (right) spent years working together building one of the world’s largest GPU-based services at scale while at Snapchat and discovered many optimization techniques. **We built out and ran a fleet of thousands of GPUs serving hundreds of millions of daily active users generating over one billion images per day in real-time.** **Our optimizations saved the company over $20 million a year in operational costs.** AI is taking the world by storm and mainly runs on GPUs, so we saw an opportunity to use our expertise and build the best product in the space.

**🔧 How it works:**

We deploy your models and provide an API for you to control them and run your inference faster. You can also add rendering, video encoding, or any other GPU-based workflow and it will be accelerated. The deployment can be hosted or on-premise, depending on your needs.

**🙏 Our asks:**

* Please reach out to us at [founders@texel.ai](mailto:founders@texel.ai) if:
  * You are running inference and/or processing video/image data and are interested in optimization
  * You want to try our API out and want to request an API key
  * Would like to introduce us to others that want to optimize their MLOps and/or VideoOps
