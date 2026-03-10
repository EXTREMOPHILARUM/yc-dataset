# Launches

## OpenNext — Deploy Next.js apps to AWS

**TL;DR:** _OpenNext is an open-source serverless adapter for Next.js. You can use it to deploy Next.js 13 apps to your AWS account._

Hi all! Today we are launching OpenNext — [https://open-next.js.org](https://open-next.js.org/). An open-source serverless adapter for Next.js. It allows you to deploy Next.js apps _serverlessly_ outside of Vercel.

(We created a silly video to celebrate the launch 🤪)

<https://youtu.be/k_8lBdPC3gk>

### Problem

Even though Next.js is designed to run in a serverless environment and does on Vercel; they make it really hard to self-host Next.js with serverless. It requires you to reverse engineer how Vercel does things internally. There have been many attempts to fix this. But most of these projects have either failed or have ended up as closed source paid services that are often buggy. [Learn more about the problem](https://open-next.js.org/).

### How it works

So we decided to bring the community together and build an open-source serverless adapter for Next.js.

OpenNext works by running `next build` and transforming the output to a format that can be deployed to AWS. [Learn more about how it works](https://github.com/serverless-stack/open-next#how-does-opennext-work).

### Get started

OpenNext generates an output that is framework agnostic but the easiest way to use it is with [SST](https://sst.dev/).

* `npx create-next-app`
* `npx create-sst`
* `npx sst deploy`

Check out our tutorial to get started — [**https://docs.sst.dev/start/nextjs**](https://docs.sst.dev/start/nextjs) and join us on Discord if you have any questions — <https://discord.gg/sst>

---
