# Launches

## Meticulous: The easiest way to write end-to-end tests

Hey there!

I'm Gabe and I'm super excited to share [Meticulous](https://meticulous.ai/) with you today, the easiest way to create end-to-end tests, without writing (or maintaining) any code.

What is Meticulous?

Meticulous is a CLI tool with ‘record’, ‘simulate’ and ‘test’ commands. The record command opens an instrumented browser which records your actions as you interact with your web application. Watch the record command below:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64757&key=user_uploads/155134/7b3e6754-07fe-424f-9896-1ba0b78f513a)

The simulate command re-executes the recorded sequence of actions on a URL of your choice, like localhost . A test consists of a recording ID (which identifies the recording to simulate on the new version of code) and a simulation ID. Tests are defined and maintained in a meticulous.json file. Meticulous takes a visual snapshot at the end of each simulation and a test fails if there is a discrepancy between the two snapshots.

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64757&key=user_uploads/155134/cda27a4d-831e-4a25-b884-20583a4832f2)

Watch the test command in action below:

![uploaded image](https://www.ycombinator.com/media/?type=post&id=64757&key=user_uploads/155134/484ba0aa-628b-4885-a341-f55e4a2daf2b)

### What about flows that mutate state?

Imagine a test that simulates a user signing up to your application. You can't sign up twice with the same email address. Traditionally you have two options: 1) Write a mock for the network call 2) Introduce a mechanism for resetting state after each test execution. Meticulous solves this problem by providing an option to automatically mock out all network calls, eliminating the need for either of these approaches. This option should be used if you wish to isolate the frontend.

### How can I try this?

Sign up [here](https://app.meticulous.ai/) and try out the product (no credit card required), or check out the [docs](https://docs.meticulous.ai) here.

On a related note, I started offering testing office hours to YC founders. I’d be happy to help you out, even if you’re not a YC founder and it's just to strategize around your testing strategy. Just email [gabe](mailto:gabe@meticulous.ai) with the title ‘Testing office hours request’.
