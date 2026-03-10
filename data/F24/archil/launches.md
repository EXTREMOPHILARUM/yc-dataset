# Launches

## Archil: Transform S3 into an infinite, local file system

_TL;DR:  Archil transforms S3 buckets into infinite, local file systems. It’s 30x faster than accessing S3 directly, and 90% cheaper than manually managing EBS disks. Archil provides instant access to data in S3, and it powers AI applications that can’t wait for massive data sets to download. Archil doesn’t require code changes because it’s just a file system. You can try it today at [archil.com](https://archil.com)._

I’m Hunter, the founder of Archil. I’ve spent the past 9 years building cloud storage products on the frontier of what’s possible – leading both Amazon’s Elastic File System product and Netflix’s cloud storage team. During this time, I worked with thousands of application developers, cloud teams, and software providers to deeply understand how they use storage.

Here's the problem: I found that AI and analytics teams love storing their data in S3 because it’s low-cost and scalable, but their applications can only use this data once it’s in a local file system. As a result, these teams are constantly moving data back and forth from their local instance file systems to S3. For larger data sets, applications can wait for hours to download and decompress data before starting. Unlike S3, local file systems have a limited amount of capacity that you can’t easily change after creation, they don’t support sharing data, and they’re 10x more expensive.

Archil transforms your existing S3 buckets into a new kind of infinite, local file system. With Archil, your applications can instantly use petabyte-scale data sets in S3 without waiting for manual data download. Archil automatically scales with your data, and you only pay for the data you’re actively using – 90% cheaper than using EBS. With Archil’s shared, high-speed cache, all your instances and containers can take advantage of 30x faster, consistent reads and writes. When you’re done editing data, it automatically flows back to S3 within a few minutes, so you can easily share results with teammates. Archil has full POSIX compatibility (including renames, appends, and locking), so it’s already compatible with your applications – no code changes needed. Teams move faster when they use Archil because they don’t have to build custom data movement infrastructure.

[Check out how easy Archil is to set up and use.](https://www.tella.tv/video/cm2num964000e03jng6jl5d9c/view)

We are really excited about how Archil will help teams simplify their data management. We are currently working with: AI teams who want to start model inference without waiting for downloads to complete, researchers who want to experiment on models and create new versions without running out of disk capacity, analytics teams who want to speed up their batch pipelines, and cloud teams who want lower-cost local storage without worrying about utilization. We’d love to work with you, too. If you have any questions, feel free to email me at [hleath@archil.com](https://mailto:hleath@archil.com). You can try Archil today by signing up at [archil.com](https://archil.com).

Let’s build the future of the cloud together.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=85093&key=user_uploads/2542/df85a282-87df-4986-b3c7-9cb58acc84ab)
