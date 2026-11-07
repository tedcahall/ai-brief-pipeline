# Token Usage and Cost - 2026-11-07

## Final-edition token usage

| Model | Start ET | Calls | Uncached input | Output | Cache read | Cache write | API estimate* |
|---|---|---|---|---|---|---|---|
| Kimi | 08:15:35 | 49 | 190,499 | 34,104 | 7,227,456 | 0 | USD 2.17 |
| Grok | 08:40:29 | 49 | 374,522 | 84,918 | 6,451,840 | 0 | USD 5.84 |
| Qwen | 08:07:01 | 52 | 176,617 | 45,842 | 5,159,552 | 0 | USD 1.92 |
| Opus | 08:07:01 | 37 | 74 | 33,806 | 4,619,823 | 180,621 | USD 3.05 |
| GLM | 07:46:38 | 49 | 465,524 | 27,535 | 3,769,090 | 0 | USD 1.75 |
| Sol | 07:00:51 | 33 | 161,432 | 16,106 | 3,964,288 | 0 | USD 0.88 |
| DeepSeek Pro | 08:27:56 | 61 | 341,303 | 42,322 | 4,298,496 | 0 | USD 0.40 |
| Flash | 08:29:25 | 93 | 170,434 | 81,087 | 9,683,712 | 0 | USD 0.10 |
| Astra | 07:46:38 | 26 | 158,615 | 13,029 | 2,707,968 | 0 | USD 4.95 |
| Terra | 07:21:03 | 37 | 136,786 | 12,191 | 3,084,032 | 0 | USD 0.35 |
| MiniMax | 07:43:46 | 40 | 117,666 | 23,748 | 3,789,952 | 0 | USD 0.09 |
| Luna | 07:07:36 | 61 | 182,688 | 34,388 | 7,549,696 | 0 | USD 0.11 |

## Final-edition recorded charges

| Model | Recorded charge USD | Calls with recorded charge |
|---|---|---|
| Kimi | USD 2.17 | 49/49 |
| Grok | Not recorded | Not applicable |
| Qwen | USD 1.92 | 52/52 |
| Opus | No per-token charge | Not applicable |
| GLM | USD 0.96 | 49/49 |
| Sol | No per-token charge | Not applicable |
| DeepSeek Pro | USD 0.55 | 61/61 |
| Flash | USD 0.07 | 93/93 |
| Astra | No per-token charge | Not applicable |
| Terra | No per-token charge | Not applicable |
| MiniMax | USD 0.09 | 40/40 |
| Luna | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 2,476,160 |
| Output | 449,076 |
| Cache Read | 62,305,905 |
| Cache Write | 180,621 |
| Calls | 587 |
| API estimate total | USD 21.61 |
| Recorded OpenRouter charges | USD 5.76 |
| Models with missing API estimates | None |

## Earlier / diagnostic attempts

| Model | Start ET | Calls | Uncached input | Output | Cache read | Cache write | API estimate* |
|---|---|---|---|---|---|---|---|
| GLM-5.3 | 07:43:46 | 0 | 0 | 0 | 0 | 0 | USD 0.00 |
| GPT-6 Astra | 07:43:45 | 0 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |
| GPT-6 Luna | 07:00:50 | 7 | 35,954 | 926 | 182,016 | 0 | USD 0.01 |
| GPT-6 Luna | 07:04:00 | 12 | 46,592 | 3,642 | 370,048 | 0 | USD 0.01 |
| GPT-6.1 Terra | 06:01:36 | 5 | 29,803 | 307 | 108,928 | 0 | USD 0.04 |
| GPT-6.1 Terra | 06:26:07 | 8 | 32,237 | 999 | 204,288 | 0 | USD 0.05 |
| GPT-6.1 Terra | 06:27:05 | 8 | 13,742 | 1,300 | 226,304 | 0 | USD 0.03 |
| GPT-6.1 Terra | 06:34:20 | 6 | 31,821 | 1,130 | 145,408 | 0 | USD 0.04 |
| GPT-6.1 Terra | 06:36:05 | 18 | 39,200 | 3,291 | 692,992 | 0 | USD 0.09 |
| GPT-6.1 Terra | 07:07:37 | 12 | 68,352 | 2,610 | 325,376 | 0 | USD 0.10 |
| GPT-6.1 Terra MEDIUM experiment 15819 | 07:35:39 | 8 | 12,270 | 743 | 229,248 | 0 | USD 0.03 |

## Definitions and limits

*API estimate means tokens priced at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested. This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.

## Selection and collection

Primary tables contain the latest completed run for each of the twelve final HTML editions. Earlier attempts and the Terra medium diagnostic appear separately and are excluded from primary totals. Rows follow the model-comparison rank order.
The collector classified DeepSeek Pro as an extra because its run.json did not expose the expected session key pattern; this report selects its unique completed run by exact job name and start time. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Pricing rates themselves are unchanged.
Collector generated: 2026-11-07T10:11:59-05:00. Pricing source: pricing/2026-10-29/api-pricing.json, as of 2026-10-29; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 10, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Complete twelve-model API-equivalent total: USD 21.61. Recorded OpenRouter charges for the final editions: USD 5.76. Pricing snapshot age at report date: 9 days. This collector does not refresh prices; hash verification checks saved-file integrity, not current rates.

## Collector diagnostics

- GPT-6 Astra (2026-11-07T07:43:45-05:00): no per-call telemetry or native session binding available

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-10-29/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- Kimi: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- Grok: [grok-4.7](https://docs.x.ai/developers/pricing)
- Qwen: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- Opus: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- GLM: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- Sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- DeepSeek Pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- Flash: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- Astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- Terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- MiniMax: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- Luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-07/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-07.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

