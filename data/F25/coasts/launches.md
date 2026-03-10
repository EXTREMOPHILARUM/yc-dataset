# Launches

## JSX Tool: In-Browser React IDE

**tl;dr**

JSX Tool is an in-browser IDE that creates a common language between developers and AI for building React UIs. Click any element in the browser to jump straight to the relevant line of code and edit it yourself, or provide precise context to an LLM to make updates.

https://www.youtube.com/watch?v=JIIXvN7vhrs

---

---

---

**The Problem**

LLMs have transformed how we write code, yet they consistently struggle with precise UI updates. The common belief is that AI simply doesn’t do well with visual tasks, but the real problem is that we're asking LLMs to understand UI without giving them proper context. They’re great at vibe styling but not great at producing precise UIs.

When you prompt an LLM about styling or component changes today, you're describing visual elements through text alone. It's like giving directions without a map. Meanwhile, developers juggle between browser DevTools, their code editor, screenshot tools, and component explorers just to gather enough context to make AI useful for these kinds of tasks.

**Our Solution**

JSX Tool addresses this by letting you click on any element and prompt your LLM with precise DOM context, the exact source component, its styles, and its position in the React hierarchy. Everything happens in one place: inspect, prompt, edit, and see changes instantly. 

And when AI suggestions aren't quite right, our full IDE is right there in the browser with that same context, so you can jump to the exact line of code you want to edit with a single click. You get the benefits of AI, while keeping the creative control and the nuanced decision-making that UI development demands.

Now developers and AI models share a common language for UI; both can reference the exact same visual elements with clarity, turning LLMs from guessing machines into powerful UI collaborators.

**@Tagging:** In your prompts, you can either type @ and click on a section of your webpage to reference another element relative to the one you’re focused on OR you can type @/ to mention files and directories you want the LLM to have as context in your prompt.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95312&key=user_uploads/3082625/2b76e7e0-6efc-4bb5-8b16-86f1cffd6f08)

**CSS Editor:** JSX Tool has a CSS editor that is nearly as feature-complete as the native CSS style editors found in browser element inspectors. Instead of applying your changes to a single element, you can see how your change to a line of JSX code would be applied globally.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95312&key=user_uploads/3082625/f911aeb0-3a85-4e30-9042-d49fd4a06d61)

**LSP Integrations:** JSX Tool ships with a lightweight IDE for manually editing code, but still an IDE that does some heavy lifting. The JSX Tool IDE integrates in language servers for common React development tasks, so you can have things like type-checking, auto-complete, and linting upon save. We currently ship with LSPs for Typescript, Tailwind, ESLint, and Prettier.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95312&key=user_uploads/3082625/57a590b7-b2c0-41e1-90c3-336c839b7219)

To learn more or start using the extension, go to [jsxtool.com](https://jsxtool.com)!

_Note: IDE features are currently in app review and will be available in our next release._

**Team**

Jamie and Dan grew up in New York City and have been working on projects together for nearly 20 years. Before JSX Tool, we most recently built a mobile app for bypassing news site paywalls.

Jamie is a second-time YC founder. Prior to starting JSX Tool, he worked as a Software Engineer at YCombinator on their investor software. He previously co-founded Cheqout, a restaurant technology company that was a part of the YC W21 batch. Prior to his first startup, Jamie worked on Airbnb's China Risk Team.

Jamie has had a deep interest in higher-order and visual programming for a while. He previously built a version control system to diff and merge structured, non-textual assets. Many of the technical problems encountered in that project were very similar to those encountered in JSX Tool.

Dan worked most recently as a Senior Software Engineer at Everblue, where he led engineering teams building workflow applications to power US government systems. Prior to that, he worked as a Senior Cloud Engineer at Sela US. He got his start in tech in the world of React and has since returned to his roots. In a former life, he was a Chef at a James Beard award-winning restaurant.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=95312&key=user_uploads/89898/dc4d88be-c544-45e6-9936-8dd8f08e80aa)
