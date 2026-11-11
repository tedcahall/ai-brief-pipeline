# API Prices — Models in the AI Brief Comparison

**Rate-card date: Wednesday, November 11, 2026 · 17 models · All prices in US dollars per 1 million tokens.**

A readable reference to the saved API pricing used for our model comparisons. Prices describe token categories—not the cost of a finished briefing. For measured run costs, see [token-costs](../token-costs/).

## Pricing table

Models are listed alphabetically by their full versioned report IDs. Each distinct saved pricing tier has its own row. Cache-write durations are shown in parentheses.

| Model | Tier | Input (uncached) | Output | Cache read | Cache write | Updated |
|---|---|---:|---:|---:|---|---|
| [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/) | Peak | $0.3 | $1.2 | $0.006 | — | 2026-10-29 |
| [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/) | Off-peak | $0.15 | $0.6 | $0.003 | — | 2026-10-29 |
| [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/) | Peak | $1.32 | $3.96 | $0.044 | — | 2026-10-29 |
| [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/) | Off-peak | $0.66 | $1.98 | $0.022 | — | 2026-10-29 |
| [fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing) | Standard | $10 | $50 | $0.25 | $12.5 (5m); $20 (1h) | 2026-11-08 |
| [fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing) | Standard | $8 | $40 | $0.2 | $10 (5m); $16 (1h) | 2026-11-10 |
| [gemini-4-argon](https://aistudio.google.com/docs/pricing) | Introductory | $2 | $10 | $0.1 | — | 2026-11-08 |
| [glm-5-3](https://docs.z.ai/guides/overview/pricing) | Z.AI direct | $1.4 | $4.4 | $0.26 | — | 2026-10-29 |
| [gpt-6-1-sol](https://developers.openai.com/api/docs/pricing) | Standard short | $2 | $10 | $0.1 | $2.5 (30m); $5 (12h) | 2026-10-29 |
| [gpt-6-1-sol](https://developers.openai.com/api/docs/pricing) | Standard long | $4 | $15 | $0.2 | $5 (30m); $10 (12h) | 2026-10-29 |
| [gpt-6-1-terra](https://developers.openai.com/api/docs/pricing) | Standard short | $1 | $5 | $0.05 | $1.25 (30m); $2.5 (12h) | 2026-10-29 |
| [gpt-6-1-terra](https://developers.openai.com/api/docs/pricing) | Standard long | $2 | $7.5 | $0.1 | $2.5 (30m); $5 (12h) | 2026-10-29 |
| [gpt-6-astra](https://developers.openai.com/api/docs/pricing) | Standard short | $10 | $50 | $1 | $12.5 (30m); $25 (12h) | 2026-10-29 |
| [gpt-6-astra](https://developers.openai.com/api/docs/pricing) | Standard long | $20 | $75 | $2 | $25 (30m); $50 (12h) | 2026-10-29 |
| [gpt-6-luna](https://developers.openai.com/api/docs/pricing) | Standard short | $0.1 | $0.5 | $0.01 | $0.125 (30m); $0.25 (12h) | 2026-10-29 |
| [gpt-6-luna](https://developers.openai.com/api/docs/pricing) | Standard long | $0.2 | $0.75 | $0.02 | $0.25 (30m); $0.5 (12h) | 2026-10-29 |
| [grok-4-7](https://docs.x.ai/developers/pricing) | Standard short | $2 | $6 | $0.5 | — | 2026-10-29 |
| [grok-4-7](https://docs.x.ai/developers/pricing) | Standard long | $4 | $12 | $1 | — | 2026-10-29 |
| [haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing) | Standard short | $0.1 | $0.5 | $0.01 | $0.125 (5m); $0.2 (1h) | 2026-11-08 |
| [haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing) | Standard long | $0.5 | $2.5 | $0.05 | $0.625 (5m); $1 (1h) | 2026-11-08 |
| [kimi-k3-1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing) | Standard flat | $2 | $10 | $0.2 | $2 (5m); $4 (1h) | 2026-10-29 |
| [minimax-m3-1-flash](https://www.minimax.io/blog/minimax-m31f) | Direct flat | $0.15 | $0.6 | $0.015 | — | 2026-10-29 |
| [opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview) | Standard | $4 | $20 | $0.2 | $5 (5m); $8 (1h) | 2026-10-29 |
| [qwen-3-8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | Singapore / International | $2 | $6 | $0.25 implicit; $0.17 explicit | $2.5 (explicit) | 2026-10-29 |
| [qwen-3-8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | Global | $1.65 | $4.951 | $0.206 implicit; $0.137 explicit | $2.063 (explicit) | 2026-10-29 |
| [sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing) | Standard | $2 | $10 | $0.1 | $2.5 (5m); $4 (1h) | 2026-11-08 |

**Updated:** Date we first recorded these rates or last observed a price change. Unchanged daily checks do not advance this date. These are observation dates, not necessarily provider effective dates.

## Selecting the right rate

- **OpenAI:** Standard short applies to requests with up to 272,000 prompt tokens; Standard long applies above that threshold. The saved card lists Batch/Flex at 0.5×, Fast at 2×, and regional/FedRAMP uplift at 1.1×; these modifiers are not applied in the table.
- **Haiku:** Short applies to requests with up to 100,000 prompt tokens, including cached prompt tokens; long applies above that threshold.
- **Grok:** Short applies below 200,000 prompt tokens; long applies at or above 200,000. The table uses the global Standard baseline; the saved card lists US regional at 1.1×, Priority at 2×, and Batch at 0.8×.
- **DeepSeek:** Peak applies Monday–Friday, 01:00–04:00 and 06:00–10:00 UTC, excluding Chinese public holidays; all other times are off-peak. The card flags a model-version discrepancy between provider materials, so execution identity must be checked before attributing a direct-endpoint run.
- **Qwen:** Both saved regional schedules and both cache-read modes are shown. Run-cost reports use the higher regional estimate conservatively; this does not establish the actual execution region. Do not mix implicit and explicit cache rates.
- **Gemini Argon:** The saved rates are introductory Standard prices. Cache read refers to implicit caching; the source card states that explicit caching is not supported.
- **Cache writes:** “—” means a separate rate was not verified in the saved card, not that writing or storage is free. Durations describe the cache lifetime. Select the applicable lifetime before calculating a cost.

Request tiers are selected per call, not from the cumulative token count of a multi-call run. These rates exclude taxes, tool fees, infrastructure, subscription allocation, and negotiated discounts. Direct-provider list prices can differ from routed provider bills.

## Price history

The available saved rate cards show no numeric changes for existing entries across this snapshot series. Updated therefore reflects the initial recorded date for these rows. In particular, Terra’s current rates already appear in the earliest saved card; this history does not establish when the provider changed them. Fable 5.2 is a newly recorded model, not a price change to Fable 5.1.

## Freshness and provenance

This document reflects the saved pricing JSON. The daily verification record for November 11, 2026 checked all 17 models across 10 freshly captured sources and reported no rate or condition changes. Older source-capture timestamps remain in the JSON history and should not be mistaken for fresh captures of every source.

- **Daily check:** `2026-11-11T08:11:45.450983+00:00`; status: `unchanged`.
- **Snapshot:** `2026-11-10T132547960000Z/api-pricing.json`.
- **SHA-256:** `ae378fb5abafbd842140157d7b3c6f176495b9c85f31012160c619d189c37dda`.

Model-name links in the table point to the pricing sources recorded in the JSON. Historical run-cost reports retain their original pricing basis; this reference does not retroactively reprice them.

## Daily maintenance

On each successful daily pricing refresh, regenerate this table from the approved rate card and current model cohort. Preserve all applicable tiers, cache durations, source links, and verification metadata. If verification fails, retain the last verified table and disclose the stale status rather than advancing its date.
