# Token Usage and Cost - 2026-11-23

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 709,141 | $1.52 | 138,761 | 4,620 | 565,760 | 0 | 07:10:19 | 16 |
| gpt-6-astra | 1,349,630 | $2.67 | 109,195 | 6,899 | 1,233,536 | 0 | 05:31:38 | 18 |
| gemini-4-hydrogen | 2,208,390 | $0.63 | 170,987 | 30,265 | 2,007,138 | 0 | 07:18:56 | 25 |
| gpt-6-1-terra | 2,283,819 | $0.25 | 95,959 | 9,300 | 2,178,560 | 0 | 05:42:09 | 31 |
| gemini-4-neon | 2,437,604 | $1.65 | 211,982 | 45,610 | 2,180,012 | 0 | 07:21:29 | 24 |
| gpt-6-1-sol | 2,694,069 | $0.69 | 151,106 | 13,299 | 2,529,664 | 0 | 05:35:51 | 25 |
| gpt-6-2-sol | 3,249,723 | $1.11 | 334,059 | 14,800 | 2,900,864 | 0 | 07:13:54 | 37 |
| glm-5-3 | 3,487,227 | $1.14 | 130,252 | 20,271 | 3,336,704 | 0 | 06:23:25 | 45 |
| fable-5-1 | 3,829,409 | $7.97 | 706 | 42,633 | 3,538,963 | 247,107 | 05:31:38 | 23 |
| kimi-k3-1-pro | 3,881,924 | $1.24 | 134,619 | 22,633 | 3,724,672 | 0 | 06:21:02 | 38 |
| sonnet-5-5 | 4,019,166 | $1.39 | 64 | 27,550 | 3,807,968 | 183,584 | 07:09:28 | 32 |
| fable-5-2 | 4,359,674 | $5.42 | 62 | 33,142 | 4,121,913 | 204,557 | 05:41:29 | 31 |
| gemini-4-argon | 4,912,099 | $1.50 (upper estimate) | 276,275 | 48,867 | 4,586,957 | 0 | 06:09:20 | 40 |
| haiku-5-5 | 5,128,822 | $0.43 | 80 | 54,566 | 4,878,629 | 195,547 | 07:13:43 | 40 |
| grok-4-7 | 5,448,243 | $3.51 | 255,982 | 73,413 | 5,118,848 | 0 | 06:32:55 | 46 |
| qwen-3-8-max-0902 | 6,232,783 | $2.23 | 193,973 | 57,498 | 5,981,312 | 0 | 07:23:42 | 58 |
| qwen-4-max | 6,456,202 | $0.98 | 221,308 | 53,518 | 6,181,376 | 0 | 06:59:24 | 46 |
| opus-5-5 | 6,513,219 | $3.50 | 84 | 34,912 | 6,285,035 | 193,188 | 05:47:15 | 42 |
| gpt-6-luna | 7,092,303 | $0.12 | 219,515 | 63,700 | 6,809,088 | 0 | 05:46:47 | 54 |
| deepseek-v4-pro | 8,480,740 | $0.51 | 210,602 | 96,314 | 8,173,824 | 0 | 05:53:37 | 74 |
| minimax-m3-1-flash | 8,530,277 | $0.18 | 150,617 | 49,548 | 8,330,112 | 0 | 06:25:40 | 71 |
| gemini-4-carbon | 11,619,235 | $2.87 | 492,798 | 77,850 | 11,048,587 | 0 | 06:31:13 | 48 |
| deepseek-v4-1-flash-1017 | 13,397,339 | $0.14 | 203,451 | 123,552 | 13,070,336 | 0 | 06:48:44 | 112 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| grok-4-7 | Not recorded | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| qwen-4-max | $0.98 | 46/46 |
| gemini-4-neon | Not recorded | Not applicable |
| kimi-k3-1-pro | $1.24 | 38/38 |
| opus-5-5 | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| deepseek-v4-pro | $1.40 | 74/74 |
| fable-5-1 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.18 | 71/71 |
| deepseek-v4-1-flash-1017 | $0.09 | 112/112 |
| gemini-4-carbon | Not recorded | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.23 | 58/58 |
| gemini-4-hydrogen | Not recorded | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| glm-5-3 | $1.13 | 45/45 |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,702,437 |
| Output | 1,004,760 |
| Cache Read | 112,589,858 |
| Cache Write | 1,023,983 |
| Calls with available telemetry | 976 |
| API estimate subtotal (available telemetry) | $40.15 |
| Recorded OpenRouter charges | $7.25 |
| Models with unavailable estimates | gemini-4-argon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-23 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Every collected run binds one-to-one to a coordinator-selected final edition session this date; there are no earlier, retried or unbound attempts in the collection.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the collector-selected snapshot pricing/2026-11-21T080621351982Z/api-pricing.json (2026-11-21 fallback after the failed 2026-11-23 check; the 2026-11-22 check verified rates unchanged) (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write (TTL unspecified) per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected snapshot (pricing/2026-11-21T080621351982Z/api-pricing.json, as of 2026-11-21); the 2026-11-23 daily pricing check failed source verification (unverified kimi_usd source), so the collector fell back to the 2026-11-21 snapshot, the most recent fully verified card (the 2026-11-22 check verified rates unchanged); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-three final HTML editions, bound by terminal-record session ID, not latest-by-name. No earlier or unbound sessions were collected this date. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-three collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-23T08:01:18-05:00. Pricing source: pricing/2026-11-21T080621351982Z/api-pricing.json, as of 2026-11-21; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $40.15; upper-bound additions from tier-indeterminate models (Gemini 4 Argon and Qwen regional estimates) bring the batch upper bound to $44.87. Recorded OpenRouter charges for the final editions: $7.25. Pricing snapshot age at report date: 2 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-23T06:09:20-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-21T080621351982Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-23/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-23.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

