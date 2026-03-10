# Launches

## K-Scale Labs 🤖 Open-source humanoid robots for everyone

At [K-Scale Labs](https://kscale.dev/), we are building the world’s first open-source general-purpose humanoid robot.

### The Problem

In recent years, domains like NLP and computer vision have benefited enormously from the [bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) that general methods that are able to leverage computation are ultimately the most effective. The ability to scrape the internet for large, in-the-wild datasets has brought these fields from working well on academic benchmarks to becoming useful real-world products.

However, although [there is evidence](https://robotics-transformer-x.github.io/) that the same scaling laws likely apply to robotics as well, the field is stymied by lack of access to the same large, in-the-wild datasets that work well in other domains, resulting in foundation models with poor cross-embodiment and out-of-distribution generalization. While there has been a [surge of investment](https://agilityrobotics.com/news/2023/opening-robofab-worlds-first-factory-for-humanoid-robotsnbsp-xxna2-g9mhr-rnk52) in trying to grow these datasets, we view the [capital-intensive](https://www.therobotreport.com/figure-raises-70m-to-commercialize-humanoids/), [factory-first](https://www.prnewswire.com/news-releases/figure-announces-commercial-agreement-with-bmw-manufacturing-to-bring-general-purpose-robots-into-automotive-production-302036263.html) approach as unlikely to generate the scale and diversity of data required to make these robotics foundation models match the state-of-the-art seen in other fields.

### Our Solution

We designed and built a fully-featured humanoid robot that anyone with a 3D printer and some time can build on their own. We are releasing it for anyone to build themself, along with an operating system that will enable the robot to perform basic task and learn from experience.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79758&key=user_uploads/216598/4ba0e510-77a0-4703-8df4-4d04593c537a)

Our robot, Stompy, is a 4-foot humanoid robot featuring the claw gripper from the recent [Universal Manipulation Interface](https://umi-gripper.github.io/) paper, designed so that each part fits on a 256 × 256 3D printer bed, with a total bill of materials costing less than $10,000. We’re using carbon fiber PAHT, but in principle, any reasonably strong plastic could be used instead. Our actuators are quasi-direct drives with between 6:1 and 8:1 reduction ratios, meaning that all the joints on our robot are low-inertia and back-drivable, with nominal torque values from 3-12 Nm. Each robot features a hot-swappable 48V 15Ah battery pack, which can power it for over an hour.

We started designing Stompy from scratch shortly after the start of the YC batch. In the last three months, we built five different iterations of the hardware as we’ve ironed out issues with assembly, part reliability, motor torque, and gripper design. Having worked with a number of robots in my professional career, including the Stretch from Hello Robot, the Spot from Boston Dynamics, and the early prototypes of the Optimus from Tesla, I feel confident saying that we have the best general-purpose hardware design for our BOM cost - and we are going to give it away for free.

![Image](https://pbs.twimg.com/media/GILolqbaEAAzDUv?format=jpg&name=large)

Additionally, we have built the software tooling to train policies in simulation, using simulators like Isaac from Nvidia, and translate those policies to the robot. This enables anyone to get started developing models for simple tasks for free. We will also release the VLM we’ve trained in-house as a foundation model for the robot perception stack, enabling developers to learn task-specific policies in a data-efficient manner.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79758&key=user_uploads/216598/2379dd19-b364-4990-958c-007b258bc1d7)

### About Us

Our CEO ([Ben](https://bookface.ycombinator.com/user/216598/linkedin_redirect?key=f2e912c331dc16e3f6c704008aeced6a0055e4ec)) is a robotics researcher and engineer who has worked on robotics foundation models at Tesla and Meta AI. At Tesla, he wrote the CUDA kernel behind the voxel occupancy network, which served as the first perception foundation model to run in the Optimus. At Meta, his papers on speech and robotics representation learning have been cited over 2000 times.

### Our Ask

If you are interested in either building, buying, or developing a humanoid robot, please send an email to [ben@kscale.dev](mailto:ben@kscale.dev) with your request. We’re working towards a future where anyone with a few 3D printers and some scrappiness can start a robot factory, and anyone who wants a humanoid robot will be able to get one.
