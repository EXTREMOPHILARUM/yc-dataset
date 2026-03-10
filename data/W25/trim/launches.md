# Launches

## Trim: Foundation model for physics to solve quantum gravity

Trim is building an AI model that can simulate real-world physical systems evolving over time. For example, given the starting position of a double pendulum, the model generates how it moves forward in time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92217&key=user_uploads/2370858/f0b2331d-d1d6-4a55-bc50-56d943ae60e6)

**What’s wrong with a traditional physics simulation?**

Traditional physics simulations take exponentially longer to run as you simulate more dimensions and polynomially longer as you increase the size of the simulation.

Simulating a **64x64** grid requires **4096** operations while a still modest **128x128** grid requires **16,384** operations.

In 3D this problem is even worse as 64³=262,144 and 128³=2,097,152.

The Trim Transformer’s linear-attention scales linearly in computation time with respect to both dimensions and grid size.

An exponential reduction in compute unlocks a new world of modeling complex, high-dimensional systems such as

* Low latency autonomous vehicle pathing
* Detailed molecular bonding for medicine research
* Global climate and weather modeling
* Population-scale financial modeling
* Nuclear fusion plasma modeling
* Gravitational waves and quantum mechanical systems

**Example: Navier-Stokes**

The Navier-Stokes equations describe the motion of fluids.

The Trim Transformer reduces memory usage by over _97%_ compared to a standard PyTorch transformer using softmax attention and _6.5x_ faster time/epoch with very similar loss. As grid size and sequence length increase these gains become even more drastic.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92217&key=user_uploads/2370858/7f50dba8-6c7a-4538-a1c5-264d9ff986b0)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92217&key=user_uploads/2370858/47c3e1c3-9ee7-41cb-b0ff-6de0d0cb971d)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92217&key=user_uploads/2370858/14dcbab4-5271-4eed-a103-f81ec085cc92)

**How will Trim solve quantum gravity?**

Even the strongest gravitational waves are extremely weak. Two super-massive black holes colliding generate vibrations measured by LIGO that are about as powerful as a pickup truck turning on one mile away. The only feasible way to extract the data out of the noise is by looking in the sky at an event, simulating what the waves should look like, and picking the needle out of the haystack on a years-long timeline.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92217&key=user_uploads/2370858/182bfb43-7354-441d-8e2a-09a16e7ab686)

The problem plaguing astronomers for the last decade is that gravitational wave frequencies that are quick to simulate aren’t very helpful for finding flaws in general relativity. The frequencies of interest would take thousands of years to simulate and identify in all the noise. A new gravitational wave detector, LISA, will soon be launched into space, capable of detecting new frequencies that could expose hints of new physics. Trim’s model makes the task of finding that data within reach for the first time.

**Our Ask:**

Check out the Trim Transformer on [GitHub](https://github.com/eg-trim/trim-transformer) and our blog at [trimresearch.com](https://trimresearch.com).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92217&key=user_uploads/2370858/3155682c-4fa9-4eaf-b23e-ce01e03e23f4)
