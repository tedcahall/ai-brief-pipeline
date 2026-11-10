# What Does an AI Brief Actually Cost?

A model’s price per million tokens is only the beginning. Producing a finished briefing can involve repeated context, follow-up research, tool interactions, and substantial cache usage. The economics emerge from the whole run—not just the final page of prose.

This directory tracks the token usage and cost estimates behind the model-test editions of Max’s AI Brief. Its purpose is to make those economics inspectable: how much each run consumed, how caching affected the calculation, and which figures are estimates versus recorded charges.

## What you’ll find

- **Daily usage-and-cost reports** — token breakdowns and API-equivalent costs for selected final editions.
- **Billing information** — recorded provider charges where available, kept separate from estimated costs.
- **Focused investigations** — comparisons of token accounting, caching, and execution routes.
- **JSON audits** — detailed supporting records in `json/`.

Start with the most recent `Usage-and-Cost-*.md`. The main token table lists models from fewest to most total tokens; it is not a cheapest-to-most-expensive ranking.

## Three different cost concepts

| Cost concept | What it tells you |
|---|---|
| **API-equivalent cost** | What recorded tokens would cost at the selected published API rates, including estimates for subscription-backed runs. Not an invoice. |
| **Recorded provider charges** | Amounts captured from provider billing telemetry, where available. Coverage is explicitly identified. |
| **Subscription-backed execution** | No separate per-token charge for the reported run. Its API-equivalent estimate is not an additional subscription bill. |

These are different views of cost. **They must not be added together.**

## Understanding the token totals

Total tokens combine uncached input, output, cache reads, and cache writes across the recorded calls. Reused context can therefore be counted repeatedly. A large token total does not mean the model wrote an equally large response—or consumed that many unique words of evidence.

The reports retain these components because they can carry different prices. Missing telemetry remains unavailable, not zero. Pricing sources, model-identity matches, and relevant tier or cache-pricing limitations accompany the estimates. Qwen’s displayed estimate uses the higher regional figure as a conservative convention, not as proof of deployment region.

## Read cost alongside the result

Primary totals cover selected final editions; earlier or diagnostic attempts, when reported, are separate. These figures are not a complete accounting of every operational expense or failed experiment.

The useful question is not simply “Which model is cheapest?” It is **“What did this run produce, how long did it take, and what did its measured workload cost?”**

Read [model comparison](../model-comparison/) for selection results, [summary](../summary/) for the cross-day view, and [API prices](../api-prices/) for the current saved rate reference.
