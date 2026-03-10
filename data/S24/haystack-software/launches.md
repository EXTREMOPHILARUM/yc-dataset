# Launches

## Haystack Editor: An AI-powered code editor built on top of a digital canvas

**TL;DR:** Navigating and refactoring in codebases sucks! No engineer likes going through mountains of files to find the right spots where they want to make changes and then do the complicated plumbing to make those changes work.

[Haystack](https://haystackeditor.com/) is a standalone code editor that makes this much faster so engineers can focus on actually writing code. In Haystack, users can explore and edit their code on a 2D canvas with a navigational copilot assisting them every step of the way.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83226&key=user_uploads/1538506/57802433-cc2e-4a5a-992e-ad67c23a570c)

**Our Ask**: Engineers have really enjoyed the smooth experience of editing their codebase in Haystack. Join them at [https://haystackeditor.com](https://haystackeditor.com/)! It takes just a single click to import your VS Code extensions and settings, so you can get to coding straight away.

Hi everyone! We’re [Akshay Subramaniam](https://www.linkedin.com/in/akshay-s-152126139/) and [Jake Yatvitskiy](https://www.linkedin.com/in/jake-yatvitskiy/), and we’re building Haystack.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=83226&key=user_uploads/1538506/1c4592f6-265d-44af-b2d6-80b8f1664504)

**The Problem:**\
Haystack was born out of our frustrations with working in large and mature codebases, specifically with navigating and editing functional flows. A great example of a functional flow is the code flow for adding an item to the Amazon shopping cart — from the database layer all the way to the frontend UI.

Oftentimes dealing with such flows would involve navigating a maze of files and functions, and making any edits would involve a lengthy process of doing corresponding downstream/upstream plumbing.\
\
**The Solution:**

Haystack attempts to address this in the following ways:

1. It allows you to explore your codebase as a directed graph of functions, classes, etc, on the canvas. We feel like this better fits how your mind understands your codebase and helps you find and alter functional flows more intuitively.
2. It has a navigational copilot that makes edits across files or functions much easier. After you make some changes, Haystack will try to predict your next action and create functions/methods or refactor upstream/downstream code for you. Haystack will surface these speculative edits on the canvas in a way that you can easily dismiss or incorporate them, allowing you to make large-scale changes with a few clicks or keystrokes.

[See Haystack in action!](https://www.youtube.com/watch?v=c2uZnR5D_cc)\
\
\
**Our Ask, Again:**\
Download and use Haystack at <https://haystackeditor.com/>!
