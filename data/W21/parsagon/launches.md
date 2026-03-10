# Launches

## Parsagon: Universal API for Regulatory Data

**TL;DR If you're scraping legislation, regulations, or other government publications, we provide a simpler option: a daily-updated dataset across 70+ countries, available via API. Check it out here: [https://parsagon.io/solutions/api](https://parsagon.io/solutions/api)**

Hi YC! We've built a global database of legislation, regulations, and other government publications. It updates daily and currently covers 70+ countries.

We originally built this for a handful of enterprise policy monitoring workflows, but we keep meeting founders who need reliable regulatory data for very different products/verticals (e.g., automating compliance workflows). Rather than trying to build every vertical ourselves, we're opening the dataset via API so you can build on top of it.

**What It Looks Like**

The API is pretty simple: give a data category, and get a list of documents back:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98455&key=user_uploads/145104/f67f65dd-772a-4bfd-b1ee-a982b71afea4)

You can search for documents with date ranges and search queries as well:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=98455&key=user_uploads/145104/c4c17ef5-5dfc-4d52-a468-33c3763099b3)

To see more examples, check out our docs: <https://docs.parsagon.io/api-reference/introduction>

**What's Different About Parsagon**

We've seen a few solutions attempt to provide global regulatory/policy data, but they often are far from comprehensive. They often only include data for specific verticals/workflows, lack data for “smaller” jurisdictions, or just don't work as advertised (one of our customers said one provider only had half their data available via API - the other half was sent to them as excel spreadsheets of new regulations manually put together by humans each week).

Parsagon is built on AI research that generates and maintains data pipelines for government sources, which lets us scale coverage faster and keep it current.

If you need a source/jurisdiction we don’t have yet, just request it! We can usually add new coverage quickly. As one example, when a Global 500 tech company asked for \~20 additional countries, we added them within two weeks.

**Who Uses Our Data**

Parsagon helps Global 500 teams track new legislation, regulations, and policy developments. Examples:

* A streaming platform tracks media/broadcasting rules in \~60 countries
* Multiple pharma companies track healthcare policy across 20+ countries
* A major airline tracks policy developments across the EU

If you’re building anything that needs regulatory context (or you want to expand your existing product into more jurisdictions), we’d love to chat! You can email us at [**founders@parsagon.io**](mailto:founders@parsagon.io) or sign up at [**https://parsagon.io/solutions/api**](https://parsagon.io/solutions/api)

## Parsagon: AI to Track and Analyze Public Policy

Hi YC! I'm Sandy, and I'm trying to improve government transparency with Parsagon.

**TL;DR**

Parsagon is an AI that can collect and analyze publications from any government body in any jurisdiction. It currently parses and analyzes legislation, press releases, speeches, meeting minutes, executive orders, and much more in 64 countries and counting.

**Fortune/Global 500 companies, policy firms, non-profits, and other organizations are using Parsagon to uncover policy insights in hundreds of jurisdictions that they would otherwise miss.**

Ask #1: If you want to try out Parsagon, email us at [founders@parsagon.io](mailto:founders@parsagon.io) or sign up for our beta at [parsagon.io](http://parsagon.io)

Ask #2: We just launched on Product Hunt! We'd greatly appreciate if you could support [our launch](https://www.producthunt.com/products/parsagon)!

## **😠The Problem:**

Government data is much less accessible than it could be. Government affairs professionals spend countless hours sifting through legislation, press releases, speeches, etc. Tracking policy in one jurisdiction is hard enough, and any given organization may have to monitor dozens if not hundreds of different jurisdictions.

Current platforms to track public policy are outdated. They track a limited set of sources, and they make you sift through those sources using clunky, keyword-based searches like the one below.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=92447&key=user_uploads/145104/d2c61d43-51e6-465a-84df-124d0132a808)

## **😃The Solution:**

Parsagon is an AI that can collect and analyze publications from any government body in any jurisdiction. You query Parsagon’s data in natural language, and Parsagon analyzes the policy developments relevant to you to create custom monitoring alerts, policy memos, and reports.

https://www.youtube.com/watch?v=MnTf_Vz79AE

# **🙏 Our Ask**

* If you want to try out Parsagon, email us at [founders@parsagon.io](mailto:founders@parsagon.io) or sign up for our beta at [parsagon.io](http://parsagon.io)
* We just launched on Product Hunt! We'd greatly appreciate if you could support [our launch](https://www.producthunt.com/products/parsagon)!

## Parsagon: Track business and policy developments

**Hi YC! We’re excited to announce that **[**Parsagon**](https://parsagon.io/)** can now monitor business and policy developments for you!**

## **😠The Problem:**

Current news monitoring tools are too noisy and too limited. They rely on simple keyword searches that fail to encompass complex topics, and they only monitor very standard news and social media sources. They lack the customization necessary to track many of the developments we care about in our industries and areas of expertise.

## **😃The Solution:**

Parsagon’s AI monitors and analyzes events from sources across the web. You can specify custom sources to monitor, such as company websites, organizations’ meeting minutes, or government legislation. And you can filter for the events you care about using custom prompts.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80386&key=user_uploads/89898/1a881b41-a2c0-4c64-91b8-b673305ff667)

For example, you can use Parsagon to:

* Collect data on mergers and acquisitions in the news
* Get email alerts about announcements from state/local governments
* Monitor bills related to a certain topic
* And much more!

Just tell Parsagon what types of events you want to monitor, and our AI will find what's relevant to you.

## **How you can help:**

If you want to try out Parsagon, email us at [founders@parsagon.io](mailto:founders@parsagon.io) or sign up for our beta at [parsagon.io](https://parsagon.io/)

## Parsagon - Real-time fundraising data for cheaper

**Hi YC! We’re excited to announce that **[**Parsagon**](https://parsagon.io/)** is offering real-time fundraising data similar to Crunchbase or Pitchbook, but for cheaper!**

## **😠The Problem:**

Collecting data on private companies is difficult and expensive, and as a result, if you want an API for fundraising data from Crunchbase or Pitchbook, you typically need to pay thousands of dollars per month.

## **😃The Solution:**

Parsagon’s AI is now capable of auto-generating the scrapers and parsers needed to collect fundraising data, which allows us to offer the same data for much cheaper! To start, **we’re offering a real-time data feed starting at $50 per month!** You can use our API to monitor fundraising deals related to a given company, investor, industry, etc., and receive real-time data that looks something like this:

```
[
  {
    "id": 156,
    "date": "2024-02-27",
    "round": "Series B",
    "amount_raised": 43000000,
    "valuation": 500000000,
    "valuation_type": "Post-money",
    "currency": "USD",
    "org": {
      "id": 687,
      "name": "Photoroom",
      "website": "https://www.photoroom.com"
    },
    "investors": [
      {
        "org": {
          "id": 443,
          "name": "Balderton",
          "website": "https://www.balderton.com"
        },
        "is_lead": true
      },
      {
        "org": {
          "id": 688,
          "name": "Aglae",
          "website": "https://aglaeventures.com"
        },
        "is_lead": true
      },
      {
        "org": {
          "id": 689,
          "name": "YCombinator",
          "website": "https://www.ycombinator.com"
        },
        "is_lead": false
      }
    ],
    ...
  },
  ...
]
```

We’re also collecting historical fundraising data as well! Extensive coverage on that front will take some time, but **we’re currently collecting historical data on demand**. For example, one financial firm gave us a list of 1,000 companies on which they wanted historical data, and we were able to add that data to our API within a few days for a fraction of what it would cost from Pitchbook.

## **How you can help:**

* If you want to try out the API, email us at [founders@parsagon.io](mailto:founders@parsagon.io)
* Do you know a VC or other financial firm that would be interested? Feel free to reach out to us at [founders@parsagon.io](mailto:founders@parsagon.io)
* Not what the data you were trying to track? Reach out anyway! Our AI generated everything needed to get the data above in about two weeks, and it might be able to handle your use case just as easily!

## Parsagon - Scrape sites with just their URLs

**Hi YC! We’re excited to announce that Parsagon now offers a new AI scraping service: you give a list of URLs, and you get back a set of scrapers!**

**The Problem:**

Parsagon's AI allows you to generate web scrapers from natural language prompts. For example, you can get city population data from Wikipedia by telling our AI:

> **_Go to _**[**_https://en.wikipedia.org/wiki/List_of_largest_cities_**](https://en.wikipedia.org/wiki/List_of_largest_cities)**_. Scrape data in the format \[{"city": "str", "link": "link", "population": "num"}\]_**

This works fine if you want to scrape a single site, but what if you want to scrape dozens, hundreds, or thousands of sites? What if each site works differently and needs a slightly different prompt? While it's faster than writing thousands of scrapers, writing thousands of prompts is still a lot of work.

**The Solution:**

Now you can give Parsagon a list of sites and the data you want from each site, and we'll pass that list to Upworkers trained to use Parsagon. The Upworkers write a prompt for each site, and you get scrapers for a fraction of the time/cost it would take to write code or hire developers! 🎉 For example, companies are using Parsagon to:

* generate scrapers that monitor hundreds of state/local government websites for events and announcements related to economic policy
* generate scrapers for thousands of company websites to get details on private companies’ financials and investors
* scrape laws from government websites across the EU to create an AI legal assistant

**The Ask:**

If you want to try out the service, email us at [**founders@parsagon.io**](mailto:founders@parsagon.io)!

## Parsagon - GPT for browser automations ⚡️

**Hi YC! We’re excited to announce that you can now use Parsagon to create browser automations with natural language!**

**The Problem:**

If you want to do something like the following:

* Go to a website, enter a query into a search bar, and get all the search results as JSON
* Check a website for changes/updates every day
* Test a form on your website with many different inputs, and run the tests on command

You usually have to write code. And then you might have to write code to monitor whether the website’s format has changed. And if the website changes, you need to write even more code. This is tedious and time-consuming for developers, and as an AI researcher, I wanted to use my research to build a better way to create automations…

**The Solution:**

We’ve trained GPT to use Parsagon’s AI, which is built specifically to write Python code for web page interactions and web scraping. Now you can type something like:

> _‘Go to _[_https://assessment.cot.tn.gov/TPAD/_](https://assessment.cot.tn.gov/TPAD/)_. Select "Carter" from the County dropdown. Type "WEST DOE AVE" into the Search Term box and hit enter. Scrape data in the format \[{"owner": "str", "address": "str"}\], clicking the Next button up to 3 times.’_

and Parsagon will create a Python program to do what you described using Selenium. 🎉

![uploaded image](https://www.ycombinator.com/media/?type=post&id=72447&key=user_uploads/145104/52d57427-2220-4040-bc2e-5ac6c22a5a46)

As shown above, you can make complex browser automations in just 3 steps:

* Type what you want the automation to do.
* Parsagon will explore the website(s) you mentioned to create a Python program. Parsagon will show you an abridged version of what the program does, and if it looks correct, you can save the program to be run whenever you want. The program doesn’t use GPT, making it cheaper, faster, and more consistent.
* You can use Parsagon to schedule your automations, alert you when a website’s format has changed and/or automatically try to adapt to format changes, and change the parameters of your automations (e.g., Parsagon will generate a program that allows you to change “Carter” and “WEST DOE AVE” to other values on each run in the example above).

**Asks:**

* If you want to try out the product, email us at [founders@parsagon.io](mailto:founders@parsagon.io) and we will move you up the waitlist to use the product.
* If you know anyone who might be interested in using our tool, we’d appreciate an intro! Feel free to reach out to us at [founders@parsagon.io](mailto:founders@parsagon.io)

## Parsagon: Universal API for product data

### **✨ TL;DR**

Hi YC! We’re excited to announce that [Parsagon](https://parsagon.io/) is offering an API with which you can **collect product data from any e-commerce site with 1 API call**.

### **🤯 The Problem**

If you’re trying to get data on products from e-commerce sites like Amazon, Etsy, etc., you essentially have 2 options:

1. 1\. Develop or purchase web scrapers for every site, which are time-consuming and expensive to build and maintain.
2. 2\. Use a product data API, where you provide a URL to a product page, and the API tries to extract product data from the page via ML models. This is cheaper, but these APIs often return inaccurate data for 20+% of product pages. We’ve seen these APIs say the price of a $350 TV was $16 because the warranty was $16, we’ve seen them say a price was $3400 when it was really $34.00, we’ve seen them say products were in stock when they were out of stock—the list goes on and on.

As developers, we at Parsagon have spent countless hours building and maintaining such web scrapers and wishing that we could use a product data API without sacrificing the accuracy and reliability of custom scrapers.

### **💡 The Solution**

**Parsagon provides a product data API with near 100% reliability.** We avoid the inaccuracies of previous product data APIs by using a novel AI to generate custom scrapers for every e-commerce website, ensuring that we consistently return accurate data for each site. Just give our API a URL for a product or list of products, and Parsagon will build a scraper for the site (if it hasn’t already) and return data for your product(s) with a standardized format.

For example, giving the API the URL for this page

![uploaded image](https://bookface.ycombinator.com/media/?type=post&id=70282&key=user_uploads/145104/ac033de5-2e1e-4e30-b6bf-0b8dbb1faf28)

yields:

```
{
```

```
"name": "Amazon eero 6 mesh Wi-Fi system | Supports speeds up to 500 mbps | Connect to Alexa | Coverage up to 4,500 sq. ft. | 3-pack, one router + two extenders, 2020 release",
"price": 179.99,
"regular_price": 199.99,
"currency": "$",
"sku": "B085WSCTS4",
"out_of_stock": false,
. . .
```

```
}
```

And giving the API the URL for this page

![uploaded image](https://www.ycombinator.com/media/?type=post&id=70282&key=user_uploads/145104/061755a7-0e01-4b75-8fa1-080259038282)

yields

> ```
> [
> 
> ```
>
> ```
> {
>     "name": "WICKER KURA BED- Pretty Stickers- Peel and Stick- Gifts- Adhesive Kura Bed Designs- Room Decor- Wicker Designs- Customizable Kura Beds", 
>     "link": "https://www.etsy.com/listing/1141689620/wicker-kura-bed-pretty-stickers-peel-and?click_key=aa9bb9d8d3aaf77acefa1143c7d023c6631c1c59%3A1141689620&click_sum=5ea4b26e&ga_order=most_relevant&ga_search_type=all&ga_view_type=gallery&ga_search_query=beds&ref=search_grid-367299-1-1&pro=1&frs=1",  
>     "price": 58.99,  
>     "regular_price": 78.66,  
>     "currency": "$",  
>     "sku": "1141689620",  
>     "out_of_stock": false,   
>     . . . 
> },
> {
>     "name": "Upholstered SOFT WALL PANELS for King or Queen size beds.",
>     . . . 
> },
> . . . 
> ]
> 
> ```

### **❓ Our Asks**

If you want an easier way to collect product data, email us at [founders@parsagon.io](mailto:founders@parsagon.io)

## Parsagon - Geographic data for half the price

**tl;dr: Parsagon is now offering a data service on all U.S. land parcels for 50% cheaper**

Parsagon is an AI that can auto-generate web scrapers and data pipelines. We had some customers ask for geographic data, so we decided to have Parsagon collect data on all land parcels in the U.S., as provided by municipal/county governments. We have collected data for several hundred counties within a few days, and we should have data covering the entire U.S. within a few weeks. We clean and standardize the data, which includes properties’ boundaries, coordinates, tax info, address info, data on structures, and [much more](https://parsagon.io/docs/parcels/parcel-data-fields).

How are we different from other data providers? Since we’re able to get the data much more easily, **we’ll charge you 50% less than what similar data providers are charging.** e.g., if competitors are charging $200/month for API access, we’ll charge $100.

**Our ask:**

If you want access to the service, please contact us at [founders@parsagon.io](mailto:founders@parsagon.io)!

## Parsagon: Real-time price indexes

**tl;dr: Parsagon now offers real-time price indexes by scraping daily prices of retailers.** 

Parsagon is an AI that can auto-generate web scrapers and data pipelines. With inflation affecting so many consumers and businesses, we had our AI generate dozens of scrapers to collect prices and track inflation for over 50,000 food products across 38 cities in North America. You can access daily inflation estimates per food category (e.g., bread, seafood) and per region (e.g., Northeast U.S., Western U.S.) via our API. For example, here’s the change in price for various foods in the U.S. over the past week:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=66389&key=user_uploads/145104/6b268c1b-9eb6-4ca6-acd0-d7d19f356145)

And earlier this month, when a jump in food inflation sent markets tumbling, our index reported that jump in inflation two weeks before the Bureau of Labor Statistics released the inflation numbers.

**Our ask:**

If you want access to the API, please contact us at [founders@parsagon.io](mailto:founders@parsagon.io) for a free trial!

Want prices for a different sector or industry? Let us know! We generated our scrapers for food in about a week, so we can likely get data for whatever industry you’re interested in.
