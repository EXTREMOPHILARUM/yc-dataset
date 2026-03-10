# Launches

## Mux Player: The <video> tag with Mux superpowers

Hello YC compatriots,

⏱ **The quick and dirty**

Mux is video infrastructure for developers. We just launched the public beta for a web player, [Mux Player](https://mux.com/player), that allows you to instantly take full advantage of it, including things like adaptive streaming and preview thumbnails on the timeline, all while being fully responsive for mobile.

🤕 **The problem**

Online video has come a _long_ way in the last 10+ years. You used to need to create 3 different versions of a file (mp4, webm, ogg) to support all the major browsers, and then you’d _still_ need a Flash fallback just in case that browser didn’t support HTML5 video.

Fast forward to 2022 and basically every browser supports one major codec, but now there are all sorts of ways to deliver streaming video. Instead of just 3 different codecs, now you need to create a bunch of different versions of a video to support people on different devices and connection speeds. It’s a **much** better experience for viewers everywhere, but it’s…a lot. On top of all of that, if you care about that experience, you need to quantify it, which means now you’ve got a bunch of data infrastructure and player instrumentation to build.

The good news is, Mux has been solving those infrastructure bits of the equation for years. We’ve got Mux Video that takes video in and then does all the magic stuff to have you streaming like Netflix. We’ve got Mux Data so you can both know how your video engagement is going, and how good the experience is while people are watching it.

But…what player do you use in your product? Do you pick a random open source player? Do you pick a random commercial player? One of the benefits of Mux is that you don’t need to be an expert to stream like one, but now you’ve got to know at least a bit about how we stream to make an informed decision.

📼 **The solution**

We built `<mux-player>`. It’s a web component that understands Mux. Point it at a Mux video and you’ve immediately got a clean, responsive player with things like preview thumbnails on the timeline (you know, the cool hover scrubber thing), streaming that adapts to a viewer’s internet connection and device, instantly configurable poster images, and data built right in with no extra work required.

You can treat it like a futuristic `<video>` element. It works in all the major JavaScript frameworks, and we even built a special React version to make things nice and idiomatic.

**💅 We’re particularly good at this**

We’re extremely proud to be experts and leaders in the online video industry in general, but we specifically have built the hell out of online players. The founding team created and helped maintain Video.js, the most popular HTML5 video player for over a decade, and hired a team that’s worked on some of the best commercial and open source players on the web.

If you’re interested, go [check out the docs](https://docs.mux.com/guides/video/mux-player). If there’s anything we can help with, reach out.

Cheers,\
Matt, Adam, Heff, and Jon
