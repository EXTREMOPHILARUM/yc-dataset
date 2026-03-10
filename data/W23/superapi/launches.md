# Launches

## SuperAPI - Make all your fetch APIs cacheable

### **✨ TL;DR**

SuperAPI is a programmable API gateway that makes all your fetch APIs cacheable, and makes sure your cached API responses never goes stale.

Hey everyone - it’s Aditya and Adithya here introducing **SuperAPI**.\
\
—

### **🤯 Problem**

A lot of application APIs are considered non-cacheable either because:

1. the underlying data changes frequently
2. they use GraphQL making it difficult to cache
3. they’re REST APIs that fetch using POST because they have their search parameters within the body

Most applications in this situation do not cache their API responses, and end up serving APIs with a high latency, or setup multiple clusters close to their users to give them low latencies.

# **💡 Solution**

SuperAPI makes such APIs cacheable by monitoring your incoming **POST / PUT / PATCH** API calls, and your database updates to invalidate stale data and keep your API cache fresh.

Because we listen to your database changes, SuperAPI can also update your cache in-place. This means, any updates in your database will only modify the relevant portions of your cached API responses.

This reduces the amount of computations on your database & compute instances, helping reduce your cloud spend.

# **🚀 How does SuperAPI work?**

SuperAPI can either be deployed as a separate API gateway, or can run on top of other caching providers like **Cloudflare & Cloudfront.**

This API gateway listens to all incoming update API calls (POST / PUT / PATCH), and invalidates any API cache that could go stale as a result of this incoming update API call.

We also have a tiny docker container running within your network that listens to your database updates (using the replication stream or database triggers), which helps us catch any invalidations coming from internal cron jobs & batch processes.

Read more about how SuperAPI works [here](https://trysuperapi.com/blog/how-does-superapi-work-clet0rvf1446071ko73x4q6qtr).

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70198&key=user_uploads/11606/c7fdb60e-043e-49d6-b23b-e6123de076e6)

# **📜 How did we get here?**

Both of us founders worked together at a Tiger Global backed Indian tech company before starting on SuperAPI.

I was the first engineer there, and built out majority of the product & platform for the first couple of years. For the next 2 years, I was heading the engineering team, growing the team from 6 engineers to \~55 engineers, designers & PMs.

Aditya was heading the platform engineering team, where he built a majority of the infrastructure to scale the platform and bring down the API latencies to less than 50ms.

We’ve been obsessed with API latencies since our time working together, and are using a lot of learnings from back then to build out SuperAPI.

# ❓ **Asks**

If you are looking to **reduce your API latencies**, let’s talk. Drop us a note at: [founders@trysuperapi.com](mailto:founders@trysuperapi.com).
