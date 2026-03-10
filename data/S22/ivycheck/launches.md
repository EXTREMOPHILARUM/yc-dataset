# Launches

## IvyCheck – Guard against AI risks with real-time checks

**TL;DR:** [IvyCheck](https://www.ivycheck.com/) offers an API designed for classifying user- and AI-generated texts, along with extracting sensitive data. Our specialized machine-learning models ensure the safety and quality of your AI app in real-time.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79742&key=user_uploads/825709/1100f870-2ce1-44f4-a45f-2c1f640a2867)

### What are AI risks?

AI-powered interfaces such as chatbots emerge and pose **new AI risks:**

* **Prompt Injection Attacks:** Attackers try to manipulate language models to execute unauthorized actions or access sensitive data. These attacks exploit the way AI interprets inputs as natural language text. Prompt injection attacks create a risk that spans from data exfiltration to influencing decision-making processes.
* **PII Data Leakage:** Customers may include sensitive data in requests that are then sent to LLM providers. Companies must ensure that sensitive data is detected and redacted from requests.
* **Hallucinations:** Chatbots in RAG applications use context retrieved from document stores, posing the risk of hallucinated, inaccurate, off-topic, or made-up information to users. IvyCheck evaluates whether chatbot answers are faithful to the provided context.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79742&key=user_uploads/825709/84a94c2d-9885-461e-a9f0-0724ccf1748a)

### How does IvyCheck help?

IvyCheck provides a library of checks for managing AI risks in your application. IvyCheck is:

* **Flexible**: You can add checks to your LLM app with **just 2 lines of code** and protect your users and your data from prompt injection attacks, PII data leakage, and hallucinations. Works regardless of which LLM provider you use in your app.
* **Secure**: We use customized, fine-tuned models for the checks. We self-host all our models and your data is not sent to third-party model providers.
* **Fast**: Since the models are small and specialized, you can expect a latency under 100-200 ms. If you require even faster endpoints, please get in touch!

### The founding team

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79742&key=user_uploads/825709/6e2a1539-300a-4ab5-ac5a-46318b4e89d2)

We’re [Tammo](https://de.linkedin.com/in/tammo-rukat-34529471) (left) and [Dustin](https://www.linkedin.com/in/dustin--lange/) (right). We met at Amazon, where we were part of the Core Machine Learning team in Berlin. We worked on systems for large-scale data quality checks, missing value imputation, and search filter optimization. We’re both obsessed with delighting our customers and solving their toughest challenges! Let’s create a safer world with AI.

### How do I get started?

Visit [https://ivycheck.com](https://ivycheck.com/) or [book a call](https://ivycheck.com/request-demo) directly with us. We’d love to get in touch and help you make your AI app safe today!

## Deekard - Instant answers from your database with AI

**TLDR:**

Deekard is your one-stop shop for fast and easy data analysis. Just enter your database details, ask your burning questions, and let Deekard do the rest. Forget waiting on your data team - it’s time to get your answers fast.

**Problem:**

You are collecting data about your business and want to become more data-driven in your decision-making. But you’re hitting some speed bumps:

* **Waiting game:** You’re stuck in a queue, waiting for your data team to free up and handle your request. They can’t update the dashboards fast enough or don’t have time to work on your ad-hoc data requests.
* **No time to write SQL**: You’ve got a business to run, not a course in SQL to take. It should be simple to run your database queries, not a guessing game.
* **Documentation? What documentation?** You look at your team’s data warehouse and you don’t understand what’s in there. There’s no documentation and you have no idea if that column really contains the data you hope for.

**Solution**

Deekard gives you a powerful, integrated analytics experience - powered by AI. Connect your database and you’re ready to go.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74336&key=user_uploads/825709/f9b112f8-94be-4f61-a329-3ce789b49b53)

* **Requests in plain English**: Get started with your request in natural language and Deekard takes care of translating it into a database query. Refine your request with a graphical query builder - or just edit the plain English request. You can also switch to SQL mode - _and back -_ whenever you like.
* **Explore your database**: See what’s _inside_ your database. Deekard automatically profiles your data and creates that missing documentation for you. This helps with writing queries that actually work.
* **Team effort**: Share the AI-powered query editor and unblock your whole team. They can instantly reuse your database connection and ask their own questions.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=74336&key=user_uploads/825709/3623b336-0a6f-44ec-a3f8-9c8d5babf861)

**Ask:**

Try Deekard! Start at [deekard.com](https://www.deekard.com). Tell us what you think at [founders@deekard.com](mailto:founders@deekard.com).

If you have a few min for a chat about Deekard, please book time with us [here](https://calendly.com/d/dxz-ddm-67k/deekard-call).

Thank you!\
Dustin and Tammo

## 🤖 Deekard - Your autonomous assistant for data science and analytics

Hey everyone! We’re Tammo and Dustin from [Deekard](https://www.deekard.com/).

**_TL;DR:_** _Deekard is an all-in-one data science and analytics assistant. Connect your data source and get any question answered and any task executed, using only natural language. Powered by GPT-4, our AI model understands your intent, plans workflows, and executes them step-by-step._

**The Problem**

Data science involves a wide range of skills, tools, and formats, which can be challenging to learn and manage. Tasks like extracting data with SQL, training machine learning pipelines with Python, and visualizing data using frameworks such as Vega are time-consuming, iterative, and error-prone.

**Our Solution**

Deekard simplifies data science by offering a chat interface where you simply state what you want to do and watch the AI select the right tools in the right order. Like in a data science notebook, you can refer to previously created datasets and refine or combine them later in the conversation. Data science has never been easier or more approachable.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=71231&key=user_uploads/825709/1d06fb3a-336e-4c6f-b93a-ce38f4a0a6f1)

**Features**

📚 Database: Write queries in natural language and let Deekard translate them into SQL for you! Simply state your query, and you'll receive the result table.

🐍 Python: Transform data or apply machine learning models with ease. Just write your request, and Deekard translates it into Python code and executes it. You'll get the results in no time.

📊 Visualization: Generate charts with natural language. Deekard translates your request into Vega-Lite specifications and creates beautiful visualizations. Apply changes to charts just by writing them down.

🧠 Wikipedia: Enrich your datasets by retrieving tables from Wikipedia. Just write your request, and Deekard will access the world's greatest knowledge base for you.

🎯 Task Organization: Write complex requests, and Deekard will split them into multiple tasks that are executed in the right order.

**Start Today**

You can start using Deekard today at [deekard.com](http://deekard.com). 

Thank you for your support, and we look forward to hearing your thoughts on Deekard! 🎉
