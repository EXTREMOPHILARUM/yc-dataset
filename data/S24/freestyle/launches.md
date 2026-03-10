# Launches

## Freestyle: A new way to build fullstack TypeScript apps

Today, most new apps are written with Fullstack TypeScript, but the tooling around them is still built as though the frontend and backend are separate codebases. We built an open source framework, runtime, and cloud that acknowledges this and removes these unnecessary layers from the development process.

**What?**

Any JavaScript class can be marked as [@cloudstate](https://github.com/freestyle-sh/cloudstate), and:

1. The data in it is now persisted. You query the data with regular JavaScript.
2. The methods on it can now be called from the front end. No Express/API Routes/tRPC needed!

**Coolest Side Effect:** By building our tooling around Fullstack TypeScript, we enable **full-stack feature packages,** a way for JavaScript developers to package any feature they build and share it in a way that it can be embedded in other projects. Think **npm install mui**, except it’s **npm install chat**, or **npm install auth**. Imagine a world where every third-party SaaS provider today can be an open source package that runs in your application.

**Our Ask:**

**Build with us!** Contribute to our [Open Source Repository,](https://github.com/freestyle-sh/cloudstate) or try [deploying an app with us](https://docs.freestyle.dev)!

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83627&key=user_uploads/89898/0a2412f8-6b6e-4906-9d8f-256badd8b332)

## Freestyle: TypeScript for EVERYTHING

# **TLDR; You can use TypeScript for EVERYTHING**

[**Freestyle**](https://www.freestyle.sh) is a fundamental shift in how we approach web development. With Freestyle, you write your entire application—frontend and backend—in TypeScript. No context switching. No mental gymnastics. Just pure, consistent TypeScript throughout.\
\
Right now, building an application has a ton of disjointed layers. Imagine you’re writing a book in English for English readers. Now, imagine being told that all the connecting words—the “ands,” “buts,” and “ors”—must be written in Latin. Sounds absurd, right? Yet, this is often what web development feels like: you write your frontend in one language, only to switch to another for the backend, another for your database, and yet another to let your app connect to others.

![alt](https://blog.freestyle.dev/images/blogs/multiplayer-infinite-craft/meme-backend-frontend.png)

During our work for Apple, we lost hundreds of hours trying to integrate different layers and teams together to make our application run. That time should’ve been spent on features, but instead was spent on stitching features together. We created [Freestyle](https://www.freestyle.sh) not as a new stitching tool but as a way for whole organizations to not need those tools and instead function as a single unit.

When you use Freestyle, you write your frontend and backend in JavaScript. Then, when you wanna call functions from your backend on your frontend, you just use them — no more dealing with REST APIs. When you want to store data, you just mark your JavaScript as [@cloudstate](https://docs.freestyle.dev/guides/cloudstate/) and when you’re ready to deploy, you run **_npx freestyle deploy_** — and in one command you’re up and running.

No more SQL, no MongoDB, no Firebase, no GraphQL or REST, or anything else taking time away from building features. With Freestyle, all you need is TypeScript.

### Ready to try it? [**Sign up for a demo here**](https://www.freestyle.sh/join), or [**CHECK OUT THE DOCS HERE**](https://docs.freestyle.dev/getting-started/astro)
