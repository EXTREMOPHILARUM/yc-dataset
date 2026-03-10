# Launches

## GoldenBasis - Modern back-office software for brokerages

### **TLDR;**

[GoldenBasis](https://www.goldenbasis.com) makes it easy for brokerages (think Schwab or Fidelity) to run their back office with modern software, and we’re starting with investment account transfers. For example, when you want to transfer your stocks from Schwab to Fidelity, GoldenBasis would let Fidelity gather your transfer information, track the status of your transfer, and automatically update their internal records.

### **Ask**

If you or someone you know is leading a brokerage operations team and wants to improve their account transfer process, please reach out at [founders@goldenbasis.com](mailto:founders@goldenbasis.com)!

### **A quick primer on account transfers**

* Account transfers exist so you can move to a new brokerage without selling your positions, which could incur taxes.
* Incoming account transfers are a primary source of growth for brokerages.
* Over $90 billion of assets are transferred every month in the US. Surprisingly, 18% of these transfers are delayed, often for several weeks \[1\].

**How the process works**

Let’s say you want to transfer your assets from Schwab to Fidelity. The following needs to happen:

* You fill out an account transfer form at Fidelity.
* Fidelity sends this information to Schwab.
* Schwab tells Fidelity what assets are in your account.
* Fidelity makes sure they can hold these assets.
* Your assets move to Fidelity a few days later.

This back-and-forth process is part of a standard protocol called ACATS, and it lets brokerages transfer assets to each other electronically \[2\]. The process above sounds straightforward, but there are hundreds of edge cases detailed in manuals that total over 1000 pages.

### **Problem**

Transfers are supposed to take 3-4 days but often take weeks. During the transfer:

* You can’t trade your assets.
* To find out the status of your transfer, you need to contact customer support.
* The brokerage receiving your assets is missing out on revenue.
* The brokerage delivering your assets gets in trouble with the regulators if they don’t go quickly enough.

Why are delays so common? It’s because there are multiple rounds of manual data entry and any small mistake (e.g. missing comma) can delay the transfer. Furthermore, the operations team has to resolve issues on outdated platforms that are hard to use.

Here’s a taste of the experience today:

* You begin the transfer by filling out a daunting form.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=78734&key=user_uploads/714908/c77b27cb-a621-4364-a3dc-4f2f371897b0)

* The brokerage operations team re-enters your form and handles issues in a back-office system.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=78734&key=user_uploads/714908/9a53a162-695a-40b4-a41a-a7cc1cb1834d)


### **Solution**

GoldenBasis provides a modern software stack that solves these issues:

* With GoldenBasis, you don’t need to fill out any forms. Just upload your account statement from the brokerage you want to leave, and our AI extracts and validates the fields, which vastly reduces errors.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=78734&key=user_uploads/714908/1966b057-cc89-42ab-b4ce-acc20f50d53a)

* GoldenBasis lets you easily track the status of your transfer so you know what’s going on without having to contact support.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=78734&key=user_uploads/714908/984e522f-5537-4876-b8d3-748ca0971ed5)

* GoldenBasis provides modern GUIs for the operations team to handle issues.

  ![uploaded image](https://www.ycombinator.com/media/?type=post&id=78734&key=user_uploads/714908/234c33e9-a876-4aba-9080-30c7d741a042)


### **Team**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=78734&key=user_uploads/714908/9c49f965-4e87-4d7e-86ec-eb85ead3e823)

[Grant](https://linkedin.com/in/grant-a-391184a5) (CEO) met [Andrew](https://linkedin.com/in/andrew-wang-0b5526109) (CTO) in college at Princeton, where they became best friends. In fact, Andrew was the best man at Grant’s wedding. They teamed up to take on their biggest adventure yet: building a startup and reading a couple thousand pages of manuals along the way.

Before GoldenBasis, Grant worked at Altruist, where he discovered the outdated technology that was causing so much pain for brokerage back offices. He also led Altruist’s integration of SSG post-acquisition, which made Altruist the third-largest custodian for financial advisors, behind Charles Schwab and Fidelity. Before that, Grant helped grow Princeton’s endowment from $26.1 billion to $37.7 billion as a member of the 20-person investment staff.

Before GoldenBasis, Andrew did quant research and software engineering at Citadel, where he built trading systems that process billions of dollars per day. Before that, he worked at Bridgewater, where he wrote software to model global economies and trade fixed-income securities. Andrew loved the prospect of bringing legacy systems to the modern age, especially the back office since it’s so often neglected.

\[1\] <https://www.sifma.org/wp-content/uploads/2022/10/SIFMA-Transfer-of-Customer-Assets-Guidance-2022.pdf>

\[2\] <https://www.investopedia.com/terms/a/acat.asp>
