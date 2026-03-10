# Launches

## 🚀 Reviewify.io - AI powered code reviews

TL;DR -  We are building [reviewify.io](http://reviewify.io) - automatic code review for every pull request, powered by GPT-4. Installation takes just 10 seconds, and you can start automatically receiving comments & suggestions.

# **Problem**

You want to make sure the code written by yourself and team is awesome. But having a code review can slow things down, especially if you only have a few Sr Engineers to review for everyone, and you don’t want their time wasted for obvious issues like not having null checks, or ordering imports.

# **Solution**

We use GPT, combined with custom review samples, to automatically run code reviews and post the comments in minutes on the PR.

[![Reviewify Demo](https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/b48f4158-e90b-42bc-8052-326c02dcc157.gif?ClientID=vimeo-core-prod&Date=1680109610&Signature=3d65ab548135d7de88de0442d6b11d451c863e4c)](https://vimeo.com/812887518)

# **Ask**

* Try it out and leave reactions to the comments it generates so we can improve the system
* If there are other features that would add value to you, please let us know (ex: Static analysis, code dependency report, integration into IDEs so comments can be seen at code time, etc).

Thanks,

Chris & Etienne

## Dev Tools AI 🤖 CoPilot for UI Testing

# **TL;DR**

[Dev Tools](https://www.dev-tools.ai/) is a library that makes it easy to write web tests in your existing framework by drawing a box over a screenshot instead of building a locator.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65540&key=user_uploads/1076464/6cf84e73-20ac-4ca5-994d-329f77e7b325)


# **🤕Problem**

Writing end to end tests is difficult and time consuming. It takes forever to dig into the page code to build the right XPath or locator. And even when these are found, they are likely to change over time as the product continues development.

# **⚡️Our solution**

We use computer vision to look at the screen, like an end user, and find the element you want to interact with. Then, in real-time, we find the element and return it so all your existing automation can keep working with it. We make this easy to use by extending Selenium with a `findByAI()` method where you just put a human readable name and let the AI do the hard work.

We even let you see the elements from within your IDE!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65540&key=user_uploads/1076464/bb8100b8-b570-4aeb-8bae-fd49cd8d470d)

# **🎉 Bonus Features**

### Work on Games

Traditional automation has trouble working with games as most games render within a canvas element. Because we only use the screenshot, and not page source, we can play games like LooneyToons!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=65540&key=user_uploads/1076464/3feb64e1-36cd-47c0-93f5-a8c3e98d10d1)

### Crawl for Errors

Monkey Testing for errors comes standard with Android, but there isn’t a default one for Web. We added that functionality to our SDK so that you simply call `scan_domain()` and it will crawl your page and look for errors like broken links, 404s, console errors, etc. Learn more in our [blog](https://www.dev-tools.ai/blog/site-sacnner) about the feature.

# **Our Ask - Try it out and give us feedback**

If you write or have written Selenium or UI tests, we would love your feedback on the tool.

Join us on [Discord](https://discord.gg/2J9WEYdq5C), or follow us on [Linkedin](https://www.linkedin.com/company/dev-tools-ai)!

If you have any questions or automation challenges, reach out to us anytime! [chris@dev-tools.ai](mailto:chris@dev-tools.ai) & [etienne@dev-tools.ai](mailto:etienne@dev-tools.ai)
