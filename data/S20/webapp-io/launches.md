# Launches

## 𝙒𝙚𝙗𝙖𝙥𝙥.𝙞𝙤 - Instant per-branch VMs for E2E tests & ephemeral environments

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64193&key=user_uploads/364633/589b9712-0cb1-49cd-9bf5-e059435f1451)

Hey! We’re Colin & Lyn from [webapp.io](http://webapp.io).

We’re helping webapp developers make new copies of their stack in seconds using memory snapshots. You can think of a cloud-agnostic, full-stack version of the branch deployments you’d get from Vercel, Netlify, Heroku, or Render - even if you’re using a regular cloud provider instead of a PaaS.

[Webapp.io](http://Webapp.io) lets you create full-stack environments for every pull request in seconds. We’ve built a custom hypervisor that watches which files are used in which build steps, and skips repetitive actions like starting microservices, seeding databases, or building images.

It came out of our own frustrations from having to often skip end-to-end testing for commits just for the sake of developer velocity. A typo fix on a landing page shouldn’t take 15+ minutes to spin up a fresh environment for some Cypress tests!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64193&key=user_uploads/364633/abdf8553-ec80-4b7a-9582-62e95d43cbc7)

[Webapp.io](http://Webapp.io) works with any Linux-based stack, and the configuration works like a Dockerfile for VMs so that you can get started without having to talk to support.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64193&key=user_uploads/364633/4e3f5b2c-3215-41ef-851d-5e46a72727d7)

Once you’ve installed our app on your GitHub, GitLab, or BitBucket profile, you can push files called Layerfile in the syntax above, and we’ll automatically discover them and build your environments.

[Webapp.io](http://Webapp.io) builds new VMs by re-using memory snapshots of your earlier builds. That means you can get a fresh copy of your database, microservices, and backend in seconds for a frontend change 10x faster than a production cloud provider or traditional CI.

Our free tier is generous and we’re happy to set up a shared slack channel to help prospective users get set up. [Try out the product here!](https://webapp.io/sign-up?utm_src=launchyc) or [read the docs](https://webapp.io/docs/?utm_src=launchyc).
