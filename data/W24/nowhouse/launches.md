# Launches

## 🏛️ NowHouse: Modernizing trade clearing and settlement

### 🔑 tl;dr

NowHouse builds software that helps stock brokerages settle trades instantly. We’re starting by helping trading ops teams in the brokerage back office intelligently reconcile trades and corporate actions.

### 📱 Setting the scene

Many of you acutely recall quarantining at home in January 2021, nearly a year after the pandemic started. If you’re anything like me, you passed a lot of time switching between the same three or four apps on your phone amid curfews and indoor dining bans.

If one of those apps was a brokerage, you might also recall this headline.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79456&key=user_uploads/505974/d066507b-93e6-4eb1-9220-f6fabb99be06)

Two weeks after the [WallStreetBets](https://www.reddit.com/r/wallstreetbets/)-driven surge in the price of GME started, Robinhood restricted trading, drawing the ire of its users. When a stock is as volatile as GME was, the [NSCC](https://www.dtcc.com/about/businesses-and-subsidiaries/nscc) increases its collateral requirement to ensure it can continue to bear counterparty risk and clear the trades sent its way. As a result, Robinhood restricted buying to avoid becoming insolvent.

### 🏦 So what?

One of the things Robinhood had to do was reconcile, or match, its trades against its executing brokers and ultimately against those cleared by the NSCC. In fact, every firm has to reconcile trades against the firm immediately upstream in the state machine below—it’s a well-conserved pattern.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=79456&key=user_uploads/505974/14a00714-2952-4fa6-85e3-78709043a4e0)

For example, at market open, an introducing broker reconciles the previous day’s close against its carrying broker, which in turn reconciles against its clearing broker. Similarly, the clearing broker reconciles against trades reported via [UTC](https://www.dtcc.com/clearing-services/equities-trade-capture/utc) by the [DTC](https://www.dtcc.com/about/businesses-and-subsidiaries/dtc), which holds $87 trillion of securities. (You can think of the DTC as the custodian’s custodian.)

The DTC itself receives settlement instructions from the NSCC via the [CNS](https://www.dtcc.com/clearing-services/equities-clearing-services/cns) system, which nets transactions to one security position per firm per day. Member firms are _also_ apprised of securities movements by the NSCC via CNS. A given brokerage may even reconcile its own orders against partial fills or its settled shares against shares that are pending, held, or tradable.

The point is that **the 20 billion equity and options trades in the US every year are each netted and reconciled several times over at different levels of abstraction in the financial system.** At a single firm, reconciliation is done thousands of times per day across hundreds of thousands of trades.

### 📈 Technically speaking

…reconciliation is the process of creating as “good” a mapping as possible between disjoint subsets of two ordered or unordered finite sets. It’s a generalization of the subset sum problem, which is itself NP-complete. The size of the search space for reconciliation is given by the Bell numbers, a logarithmically convex sequence that counts the partitions of a set. Reconciliation can be constrained by, for example, enforcing that set partitions are non-crossing. Even then, however, the search space is given by the Catalan numbers, another logarithmically convex sequence.

This means that **the fastest general solution is exhaustive search—unacceptable for 100 trades, let alone 100,000…**

### 🗂 …so how does reconciliation work today?

It’s done by people. Even at the most tech-forward brokerages and clearinghouses, reconciliation is manually driven. In some cases, it’s naively automated—think **cron jobs executing stored procedures**—which is far less robust than human judgement. These procedures are slow and brittle. And whether it's driven by a trading ops team alone or augmented by computers, there's little variance in how reconciliation is done from firm to firm. It’s the same problem across the 3,400 SEC-registered broker-dealers.

### 👨🏽‍💻 How does NowHouse fix this?

To make this problem tractable, it needs to have a clear objective function and be constrained with heuristics. **NowHouse preprocesses and normalizes trading datasets using AI, reconciles trades under context-appropriate objective functions, and writes reconciled transactions to a general ledger.** It also enforces configurable constraints, like adjacency of transactions in a match so that the reconciliations it generates make sense given different business contexts. A trading ops associate need not waste time manually combing through reams of transactions to resolve discrepant ones.

### 🕓 Why now?

You’ve probably noticed that when you place a trade, the shares (or cash) take two business days to arrive, at which point you can sell the shares (or withdraw the cash). That's known as T+2 settlement, and it’s about to change. Just over a year ago, the SEC adopted [amendments](https://www.sec.gov/investment/settlement-cycle-small-entity-compliance-guide-15c6-1-15c6-2-204-2) to the Securities Exchange Act of 1934, **shortening the trade settlement cycle from T+2 to T+1**. Maintaining current books and records is paramount to supporting T+1 settlement, and efficiently reconciling trades is paramount to maintaining current books and records.

### 📝 The vision

…is to become the **de facto system of record to firms and their regulators on the 3 trillion shares that change hands in U.S. markets every year**. This will then enable NowHouse to shoulder compliance and recordkeeping responsibilities like [CAT reporting](https://www.finra.org/rules-guidance/key-topics/consolidated-audit-trail-cat) for brokerages.

### 🌆 My request

If you work (or worked) for a brokerage, clearinghouse, or any other party involved in the trade lifecycle, please reach out—**especially if your firm wrestles with trade clearing and settlement.**
