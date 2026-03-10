# Launches

## Vansec - Spear phishing simulation & security awareness training, powered by AI

**TL;DR**

* Vansec’s spear phishing simulation is highly-personalized (using AI), multi-message (parse + generate emails using AI), and multi-modal (email, SMS, and more), to accurately reflect the current sophistication of phishing that bad actors employ (we have basic phishing simulations as well).
* Vansec’s chat-based security awareness training is designed to be interactive (users will _actually_ learn) and bite-sized (< 5 mins).

**Vansec’s multi-message spear phishing simulation (expanded thread **[**here**](https://www.vansec.com/media/temp/sim_full.png)**)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80676&key=user_uploads/386068/dce3d55f-bfd8-4637-91c8-3556e3826144)

**Vansec’s chat-based security awareness training (personalized to each employee’s simulation) (expanded conversation **[**here**](https://www.vansec.com/media/temp/debrief_full.png)**)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80676&key=user_uploads/386068/fc97e518-4c5c-4c25-8894-967641397af3)

**Security awareness training on a cybersecurity topic (expanded conversation **[**here**](https://www.vansec.com/media/temp/ransomware_full.png)**)**

![uploaded image](https://www.ycombinator.com/media/?type=post&id=80676&key=user_uploads/386068/ce7ea892-3fcc-4f74-bd3f-a23bf910b294)

### **What is spear phishing simulation and why is it important?**

Spear phishing is an advanced form of phishing, where the bad actor engages the victim in a very personalized & targeted manner, usually involving prior research on the victim (e.g. via LinkedIn) as well as various social engineering techniques to try to trick the victim.

It’s common knowledge that phishing is by far the most common way in which cyber attacks occur (over 90%, as of 2020), and 66% of phishing victims are victims of spear phishing attacks (as of 2023). With proliferation of generative AI and everyone being on LinkedIn, the phishing techniques that bad actors are using are growing both in sophistication and scale.

### **Existing phishing simulations are ineffective**

The world of phishing simulation is dominated by legacy players like KnowBe4, and while their product is the standard of the industry, the product itself is very one-dimensional.

**Problem 1**. Existing phishing simulations are too basic, where you send out one templated email and that’s it.

**Problem 2**. Simulations are not highly-personalized, nor can you train your employees against dangerous social engineering techniques.

The reality is that this does not prepare your employees against the most dangerous type of phishing attacks: spear phishing. **Vansec’s spear phishing simulations are multi-message, hyper-personalized, and scenario-based where you can choose from common scenarios or customize your own (p.s. we also provide basic phishing simulation too).**

### **Security awareness training is broken**

Employees playing training videos in the background/minimized while doing something else. This is what security awareness training looks like today.

**Problem 1**. Obviously, this does not improve company’s actual security readiness.

**Problem 2**. It’s a waste of time for the employee.

The optimal outcome here is for the training to be a) effective i.e. employees actually learn and become security-effective and b) time-efficient i.e. minimal disruption to their workflow.

Our opinion is that learning should always be interactive, not passive. We also believe that getting pulled away from actual work to complete training is _always_ going to be annoying for the employee, no matter how you do it. **That’s why we designed Vansec’s security awareness training to be interactive & bite-sized (p.s. it’s also super personalized).**

### **The ask**

* Check out our [**interactive demo**](https://www.vansec.com/?demo_is_active=true#demo) and/or [**find a time**](https://calendly.com/vansec/vansec-discovery) to get started.
* If you already have a phishing sim + training vendor but are interested in Vansec, please reach out and we can explore an option for you to use Vansec for free until your existing contract lapses.
* If you are a security vendor looking for partnerships, let’s chat!

## PlusPassword - Share passwords without revealing them

**tl;dr**: **PlusPassword** is:

* A **free** tool ([**web app**](https://www.pluspassword.com) || Slack app & browser extension [download page](https://www.pluspassword.com/download)).
* That allows you to **share passwords** with others **without revealing them in plaintext or copying to clipboard**\*.

…………………………………………………………………………………………………

## **🫵 Do you…**

* Share passwords with others (coworkers / 3rd party vendors) more than once a week?
* And you know you shouldn’t be sharing them in plaintext over email / text / Slack...
* But you do so anyways because there isn’t a better alternative?
* Well, now there is!

## **💡 How does PlusPassword work?**

* **Sharing password**.

  1\. Set security options such as:
  * Automatic logout after X hours.
  * Restrict password paste to specific web domain.
  * Email allowlist.

  2\. Generate access link.

  3\. Share link.
* **Accessing password**.

  1\. Install browser extension.

  2\. Decrypt & paste password into password input field via browser extension. (Never revealed in plaintext or copied to clipboard.)

![uploaded image](https://www.ycombinator.com/media/?type=post&id=68603&key=user_uploads/386068/eeb51320-3f02-40ad-8f60-94a13fffa87f)

## **🔐 Why should I trust PlusPassword?**

* We take a lot of pride in our robust security design, but the reality is that nothing in this world is 100% failproof.
* That's why we always encrypt your passwords (using industry standard cryptographic practices\*\*) and never store anything on our servers that can ever decrypt them (zero-knowledge).
* Learn more in our [security page](https://www.pluspassword.com/security).

## **🙏 The Ask**

* Try sharing a password through [**PlusPassword**](https://www.pluspassword.com) (\~30 seconds, free). We also have an awesome **Slack app** and **browser extension** ([download page](https://www.pluspassword.com/download), also free).

\
\
\* With enough malicious intent, one technically can see the plaintext of the password by inspecting the value attribute of the password input field or listening to the POST request when the form is submitted (although most websites only send the hash of the password over the wire). But the thing is, if someone has that much malicious intent to begin with (i.e. going out of their way to dig up the plaintext of the password), you probably shouldn't be sharing the password and giving this person access to your account anyways.\
\*\* We never store anything on our servers that can ever decrypt your encrypted passwords (zero-knowledge). We use PBKDF2 (with 101,004 iterations) for key derivation and AES-GCM for symmetric encryption, both utilizing the Web Crypto API. PlusPassword is developed adhering to the compliance requirements of SOC 2 (PlusIdentity is SOC 2 Type II compliant).
