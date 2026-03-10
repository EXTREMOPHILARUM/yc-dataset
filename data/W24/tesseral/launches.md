# Launches

## Tesseral: the open source auth infrastructure for B2B SaaS

Tesseral is open source auth infrastructure for business software. You can use it to authenticate your users, and manage their access to resources.

It’s similar to products like Auth0, but it’s open source and built specifically for B2B apps.

It comes with enterprise features like single sign-on, directory provisioning, user impersonation, and multi-factor authentication, as well as beautiful login pages and self-service settings for customers.

You can experiment with Tesseral using our hosted service for free at [console.tesseral.com](http://console.tesseral.com) or learn more by reading the docs at tesseral.com/docs!

https://www.youtube.com/watch?v=hawD-4PWy4Y

![uploaded image](https://www.ycombinator.com/media/?type=post&id=90141&key=user_uploads/1519710/328d4d9e-4a18-4dbe-ae6e-231ae3002b1c)

## SSOReady: Open source developer tools for enterprise single sign-on

**TLDR: set up SAML and SCIM in less than a day:** <https://www.youtube.com/watch?v=_HVtFkW8xCI>.

# Context: customers want SAML

There are lots of different ways to authenticate (i.e. log in) users in software.

Companies often require their employees to use single sign-on (SSO) to access business software, both for convenience and security.

For the most part, especially in large companies, SSO relies on an old, complicated protocol called SAML. (If you’ve used a service like Okta before, you’ve likely used SAML without realizing it!)

If you make business software, you probably will need to support SAML at some point.

# Problem: SAML is hard

But SAML is really hard, even for experienced developers. It just doesn’t work like most modern software, making implementations slow and risky. Companies as sophisticated as GitLab can make [very costly mistakes](https://ssoready.com/blog/engineering/ruby-saml-pwned-by-xml-signature-wrapping-attacks/).

# What we do: we make SAML easy

SSOReady makes SAML safe and easy enough that developers can often finish an implementation in [less than a day](https://blog.runreveal.com/we-shipped-sso-support-in-a-day-how/).

SSOReady is an open-source (MIT) service that helps developers implement SAML single sign-on without ever touching SAML directly. Devs just need to implement two API endpoints: one to initiate SAML logins and another to receive incoming SAML messages. And then they’re pretty much done.

SSOReady also offers a similar tool for SCIM, a protocol often used alongside SAML to provision and de-provision users. Developers can use SCIM to establish a live sync between their database of users and their customers’ central IT systems.

# Get in touch

* Our website: <https://ssoready.com>
* Our github: <https://github.com/ssoready>

![uploaded image](https://www.ycombinator.com/media/?type=post&id=84774&key=user_uploads/89898/5ad4c15a-246b-4e47-86ba-96e87cabf198)
