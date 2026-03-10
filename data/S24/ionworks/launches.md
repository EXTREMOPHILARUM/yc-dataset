# Launches

## Ionworks - Build and run battery simulations at scale

We provide battery-simulation-as-a-service to help battery engineers accelerate their battery design cycles by replacing experiments with simulations. We’re building this on top of [**PyBaMM,**](https://github.com/pybamm-team/PyBaMM) the world’s leading open-source battery modeling software, which was created by our team and is now used by most battery engineering teams around the world.

**Our ask:** If you are a battery engineer or know one, reach out to [**info@ionworks.com**](mailto:info@ionworks.com) for a demo

**Meet the team**

We ([**Valentin**](https://www.linkedin.com/in/valentinsulzer/), [**Rob**](https://www.linkedin.com/in/robertwtimms/), [**Tom**](https://www.linkedin.com/in/tom-tranter-355a1033/)) have PhDs in Maths/Chemical Engineering from Oxford/East Anglia/Leeds & UCL, and a collective 20 years of experience working on physics-based battery simulations. As academics, we were frustrated by the scientific reproducibility crisis, so we created an open-source project to share our research and hold ourselves accountable. This turned out to be something people wanted, and PyBaMM has now grown to become the leading open-source battery simulation package used by engineers in battery companies and academic labs around the world. We’re now building Ionworks to scale up this success and bring the power of digital design to every single battery engineer.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82425&key=user_uploads/1162906/8c9248b2-33cb-4cd1-a577-f564bb1f0ce6)

**The Need**

Batteries are a crucial technology underpinning the electrification of every application ranging from EVs to grid storage. This makes the battery market worth _$150b today (1.5% of global GDP)_, with projected growth to $680b in 10 years (4% of projected global GDP). However, batteries still need to improve massively to meet a difficult set of demands: **higher energy and power density, faster charge times, lower cost, longer lifetimes, and better safety.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82425&key=user_uploads/1162906/ba1d3286-9e94-4cf5-a24a-8f886d18dbdd)

**Why designing better batteries is difficult**

Batteries come in all shapes and sizes, with complex and nonlinear effects of design inputs on performance outputs. As a result, battery engineering teams build and test thousands of physical prototypes to find the optimal design for their application. This is an expensive and time-consuming process (up to $1000 and 2 years for each individual test), which leads to **$100m/5 year battery development cycles**. This makes batteries the bottleneck in many product development cycles, such as new laptops and electric cars.

**The Solution**

We’re doing for batteries what CFD (computational fluid dynamics) did for aerodynamics and CAD (computer-aided design) did for structural and electrical engineering: **move the design problem into the digital world**. Generic engineering software already exists but requires specialist knowledge and decades of experience to build battery-specific models. We’re building software that makes this process available to any battery engineer. Our solution is built for the cloud, providing the interfaces and cost models to do this at scale.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82425&key=user_uploads/1162906/00b0d1e5-e12b-4f4d-9eb7-a3e7d9deb650)

**How it works**

We move battery design into the digital world using the following process:

1. Collect a small amount of experimental data
2. Parameterize (i.e. train) the physics-based model to find the parameter values that best match the experimental data
3. Use the generated parameters to virtually explore the entire space of designs and operating conditions
4. Pick the best candidates from the virtual experiments and test those in the physical world to validate the simulation results

The underlying physics-based models are old-school partial differential equations that describe the chemical reactions, lithium transport, and heat exchange happening inside a battery. These models generalize well from their training data, which allows us to build accurate models from small amounts of data. **Our secret sauce is that we’ve built software that makes steps 2 and 3 fast and robust.**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82425&key=user_uploads/1162906/8cd0cdec-18b1-4468-87fe-245207c3aad3)

**Ask**

* If you are a battery engineer or know one, reach out to [**info@ionworks.com**](mailto:info@ionworks.com) for a demo
* Submit a [**PyBaMM Testimonial**](https://forms.gle/mZnbRFWFQdj48RFT6) for a chance to win some [swag](https://numfocus.myspreadshop.com/pybamm+logo-A65835f9218539517e7310303?productType=812&sellable=xr4nBeRpbRhJJX4enQn7-812-7)
* Star [**PyBaMM on GitHub**](https://github.com/pybamm-team/PyBaMM)
