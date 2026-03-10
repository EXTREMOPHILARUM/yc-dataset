# Launches

## ZeroStep - AI-assisted actions and assertions for Playwright tests

[**ZeroStep**](https://zerostep.com/) is a JavaScript library that adds the power of AI to Playwright tests. ZeroStep’s **ai()** function lets developers test a web application using simple plain-text instructions, embedded directly in their Playwright tests.

Here’s a complete Playwright test using ZeroStep that verifies the core “book a meeting” workflow in Calendly:

```javascript
import { test, expect } from '@playwright/test'
import { ai } from '@zerostep/playwright'

test.describe('Calendly', () => {
  test('book the next available timeslot', async ({ page }) => {
    await page.goto('https://calendly.com/zerostep-test/test-calendly')

    await ai('Verify that a calendar is displayed', { page, test })
    await ai('Dismiss the privacy modal', { page, test })
    await ai('Click on the first available day of the month', { page, test })
    await ai('Click on the first available time in the sidebar', { page, test })
    await ai('Click the Next button', { page, test })
    await ai('Fill out the form with realistic values', { page, test })
    await ai('Submit the form', { page, test })

    const element = await page.getByText('You are scheduled')
    expect(element).toBeDefined()
  })
})
```

Six months ago, we launched an AI “prompt” feature in [**Reflect**](https://reflect.run/), our low-code testing platform, that lets users execute actions and assertions from plain-text prompts. Since then, two-thirds of our customers have incorporated AI prompts into their Reflect tests. We’re convinced that AI will lead to a step change in how products are end-to-end tested, and want as many devs as possible to be able to take advantage of this new technology.

With ZeroStep, you can get the benefits of easy-to-write test steps and less flaky tests, with minimal changes to your existing Playwright testing workflow.

**The biggest benefits of ZeroStep are:**

* **Tests are easier to write**. Writing an ai() step is equivalent to describing the action (“Fill out the form with realistic values”), assertion (“Verify there are no errors displayed on the page”), or extraction (“What is the shopping cart total?”) in plain English. The AI does the rest. There’s no need to write selectors, or add data-test-id attributes all over your app so that your tests have stable locators. Our website and GitHub repo show several examples of tricky testing scenarios that are made easy with ZeroStep.
* **Tests are less frustrating to maintain**. Unlike selectors, ZeroStep ai() steps are not tightly coupled to your app’s markup. The ZeroStep AI interprets your ai() steps at runtime which means even large scale changes in the app won’t break your tests, so long as your functional requirements remain unchanged. Selectors, in my opinion, are one of the worst leaky abstractions in software development. I can’t imagine how many dev hours have been lost due to them. We’re happy to not use any concept of selectors with this approach.
* **It’s easy to ramp up**. ai() steps have no predefined syntax (unlike Cucumber). You just need to be able to clearly describe what action, assertion, or extraction you want the AI to perform.

**Our Ask:**

If your front-end developers write and maintain Playwright tests, and would benefit from tests being faster to write and easier to maintain, we think they’ll love ZeroStep.

We offer a generous free tier and it’s easy to get started. More information is available at <https://zerostep.com/> and our GitHub repo: <https://github.com/zerostep-ai/zerostep>
