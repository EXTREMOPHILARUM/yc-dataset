# Launches

## Pillar - Your app's copilot

Hey everyone! We’re JJ and Mark, cofounders of [Pillar](https://trypillar.com) 👋

**TL;DR: Pillar is an embedded AI copilot that executes tasks inside your product for users and agents.**

Users or agents can type what they want. The copilot carries it out **client-side in the browser**, using the user’s existing session, permissions, and security checks. You install the SDK via npm and register your existing frontend code as tools.

Example: in a banking app, a user types _“send $200 to my cleaners.”_ Pillar finds the right recipient, navigates to the transfer flow, and pre-fills the form. The user still reviews and confirms. If your app requires 2FA for that acion, so does the copilot.

Demo: <https://www.youtube.com/watch?v=ruNJ5OFuKsI>

# The Problem

Teams ship faster than ever. But when your changelog is 10x longer than it used to be, users can’t keep up.

* **Discoverability breaks down:** the UI changes, features move, and people forget where things live.
* **Friction turns into “support”:** users open tickets that aren’t really support tickets. The user wanted to do something your product already supported but couldn’t get there.
* **Most products don’t have an “action layer”:** AI agents are starting to use web apps the same way users do: navigate, click, fill forms. Products need to prepare for this

**Bottom line:** products need a reliable, permissioned way to execute actions end-to-end - not just document them.

# How Pillar Works

Pillar turns a user request into action by combining planning with **in-browser execution**.

1. **Plan:** Pillar determines which steps/tools to run
2. **Execute:** your app runs those tools in the browser (navigation, API calls, state updates, form fills)
3. **Confirm:** the user stays in control for sensitive actions.

You register tools inside your existing React components:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97986&key=user_uploads/376672/a918639c-e2a9-405b-9e4d-2f54acac8af0)

What happens at runtime when a user types _“send $200 to my cleaners”_:

* Pillar calls **search_recipients** with “cleaners”
* Selects the right match
* Calls **prefill_transfer** with the recipient + amount
* User reviews and confirms in the existing flow

Because execution happens in the browser, tools run with the current user’s permissions and session. **Pillar can’t do anything the user can’t do.**

Pillar syncs with your help content (Zendesk, Intercom, Notion, Confluence, internal docs) so requests map to the right tools/flows. When it picks the wrong path, you flag it and the correction is captured so the same issue is less likely to repeat.

SDKs are available for React and vanilla JavaScript. Registered tools can also be reused by other copilots/agents via WebMCP (navigator.modelContext).

# Try It

Install: [trypillar.com](http://trypillar.com)

We also have live demos you can try right now - Pillar installed on open-source products:

* Grafana ([trypillar.com/demos/grafana](https://trypillar.com/demos/grafana)): you can have Pillar build you a monitoring dashboard and set up alerts
* Apache Superset ([trypillar.com/demos/superset](https://trypillar.com/demos/superset)): you can explore the names dataset and build a dashboard

👉 Want help getting live? Reach out at [founders@trypillar.com](https://mailto:founders@trypillar.com)

# Our Ask

* If you lead product/engineering and users open tickets for things your product already does, we’d love to talk: [founders@trypillar.com](mailto:founders@trypillar.com)
* If you know someone who fits that (founders, VP Product, Head of Support), intros are appreciated
* Share this post. Follow us on LinkedIn and X.

# Backstory

We built Pillar to solve our own problem. At our last company (Double Finance), we saw a pattern: users asked for outcomes we already supported, but still opened support tickets. We wanted a way to reuse the frontend code we’d already shipped, without rebuilding flows or adding new “automation” surfaces.

_Pillar is what we wish we had._

![uploaded image](https://www.ycombinator.com/media/?type=post&id=97986&key=user_uploads/376672/597895ee-5fab-49bb-b55e-cabb1f3f6ff2)

## Double - Design your own stock index

![uploaded image](https://www.ycombinator.com/media/?type=post&id=82801&key=user_uploads/1289064/c2a6166e-82a3-419a-9800-0648a58901ea)

**TL; DR** — Design and invest in your own stock index that’s advised, managed, and tax-optimized by [Double](https://double.finance/).

Historically, access to sophisticated finance tools like direct indexing and tax loss harvesting has come at a steep cost and only through exclusive financial advisors. We are on a mission to revolutionize investing by providing world-class portfolio tools to everyday investors without any AUM fees. 

# Key Features

* **Direct Index into 20+ ETFs:** Build an elite portfolio with the ability to tilt towards specific sectors, industries, themes, or even custom groupings like all YC publicly listed companies.
* **Daily Tax Optimization, Rebalancing & Potential Tax Loss Harvesting**: Our optimization engine keeps your portfolio on track by factoring in drift, taxes and transaction costs. If your account qualifies, our tax-loss harvesting service aims to help you minimize your tax liability and maximize your after-tax returns.
* **Dollar-cost averaging:** We allow users to move between positions at a set cadence, regardless of the market's performance, helping you reduce timing risks associated with active trading.

# Example Use Cases

Work for AAPL and want to diversify away from tech?

* Buy a direct-indexed [S&P 500 Portfolio](https://app.double.finance/public/explore/3), remove AAPL entirely, and cut the rest of your tech exposure in half.

Did you know AI was going to be a big deal before everyone else?

* Double makes it easy to tilt your portfolio towards your hunches. Pick a handful of stocks set to benefit from the Inflation Reduction Act, or some that target the booming AI and semiconductor industry, or shift your portfolio towards the explosive meme growth of Zyn.

Feeling confident in the overall market and ready to pile on the risk?

* Follow [Hedgefundie’s Adventure](https://app.double.finance/explore/110), which uses 3x leverage in a Stock and Bond ETF to try and increase returns. Or pick from our smart screens that target top growing companies or even a basket of the [YC Public Companies](https://app.double.finance/public/explore/140).

Think we’re headed for a recession and want to take some chips off the table? 

* You can invest in a version of [Ray Dalio’s All Weather Portfolio](https://app.double.finance/public/explore/108) comprising 5 ETFs or [John Bogles Majesty of Simplicity](https://app.double.finance/public/explore/105) and migrate between these Strategies and Bonds over time.

Build and backtest your own stock index!

* Use our Stock and ETF Screeners to build your very own personalized portfolio.

#### Fees

Double doesn’t charge AUM fees. Financial Advisors often charge around 1% a year for tools like Direct Indexing and Dollar Cost Averaging. In a sample $1M portfolio, these fees lead to a dollar cost of $1,800,000 or a 24.5% overall reduction in performance over 30 years, assuming 6% growth vs. 7% growth. We aim to eventually make money like the commission-free trading pioneers. Our custodian Apex Clearing charges some fees which we pass on to users which you can see [here](https://help.double.finance/en/articles/9450171-service-provider-fees). 

#### Additional Features

* Backtest a custom stock grouping to see its historic performance.
* Cash sweep available: Earn 4.5% interest on your uninvested cash (as of August 5th, 2024, not a guarantee of future rates)
* Fractional investing: Invest in over 3,000 US stocks and 1,400 ETFs for as little as $5 per share.
* Support for Personal, Joint, and Trust Accounts
* Daily portfolio optimization and trade execution
* Recurring or one-time deposits via ACH or Wire
* ACAT Transfer in an existing brokerage account

#### Get Started Today

We’re live at <https://double.finance>. Sign up for a Double account today and start building your own stock index. Please reach out to [founders@double.finance](mailto:founders@double.finance) with any feedback or questions!

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXctLsEGUWaE1ScP7EqAuz0sPPYQDg7Vt1Zlpn5Cx-sfubv0nJvIZertGsNS0zPWoWzzJSw-orkpmSTzIFepxiDziCKdJN6sMXMAS1GSYwcTfiyY3ZqlIA_db-gZX4rHTji2-dZPfMWgdz-qmvb7whdOackQ?key=nGDLEdHNSqYCi809_9DeNQ)
