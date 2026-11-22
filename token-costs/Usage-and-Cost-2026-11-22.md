# Token Usage and Cost - 2026-11-22

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 827,453 | $1.67 | 150,813 | 4,896 | 671,744 | 0 | 07:10:20 | 17 |
| gemini-4-neon | 1,735,968 | $1.33 | 186,079 | 36,251 | 1,513,638 | 0 | 07:21:31 | 20 |
| gpt-6-astra | 1,742,801 | $3.00 | 98,440 | 7,497 | 1,636,864 | 0 | 05:31:38 | 23 |
| gemini-4-hydrogen | 2,152,078 | $0.67 | 157,146 | 37,710 | 1,957,222 | 0 | 07:04:35 | 27 |
| gpt-6-1-sol | 2,374,363 | $0.61 | 127,551 | 13,340 | 2,233,472 | 0 | 05:36:27 | 24 |
| glm-5-3 | 2,454,786 | $0.85 | 98,513 | 23,345 | 2,332,928 | 0 | 06:18:05 | 35 |
| gpt-6-1-terra | 2,632,065 | $0.28 | 99,225 | 10,216 | 2,522,624 | 0 | 05:43:13 | 36 |
| gpt-6-2-sol | 3,601,393 | $1.17 | 340,577 | 16,656 | 3,244,160 | 0 | 07:13:23 | 36 |
| gemini-4-argon | 4,083,217 | $1.51 (upper estimate) | 376,922 | 39,394 | 3,666,901 | 0 | 06:06:06 | 38 |
| kimi-k3-1-pro | 4,308,328 | $1.34 | 183,894 | 14,610 | 4,109,824 | 0 | 06:15:20 | 29 |
| fable-5-2 | 4,335,754 | $5.71 | 54 | 32,096 | 4,078,184 | 225,420 | 05:45:57 | 27 |
| deepseek-v4-pro | 4,360,395 | $0.27 | 137,799 | 43,140 | 4,179,456 | 0 | 06:01:26 | 58 |
| sonnet-5-5 | 4,397,486 | $1.52 | 68 | 31,774 | 4,169,244 | 196,400 | 06:52:45 | 34 |
| grok-4-7 | 4,742,031 | $3.06 | 199,225 | 71,126 | 4,471,680 | 0 | 06:25:48 | 40 |
| gpt-6-luna | 6,209,716 | $0.10 | 213,933 | 47,879 | 5,947,904 | 0 | 05:48:56 | 45 |
| fable-5-1 | 6,526,847 | $11.29 | 898 | 63,530 | 6,133,722 | 328,697 | 05:31:39 | 29 |
| gemini-4-carbon | 7,681,841 | $2.05 | 357,751 | 61,040 | 7,263,050 | 0 | 06:24:26 | 34 |
| qwen-3-8-max-0902 | 7,725,421 | $2.76 | 238,320 | 71,037 | 7,416,064 | 0 | 07:10:24 | 60 |
| haiku-5-5 | 8,756,462 | $0.72 | 106 | 74,728 | 8,434,405 | 247,223 | 06:57:34 | 53 |
| opus-5-5 | 9,250,531 | $4.23 | 114 | 40,484 | 9,007,424 | 202,509 | 05:51:42 | 57 |
| minimax-m3-1-flash | 9,785,179 | $0.20 | 192,013 | 48,334 | 9,544,832 | 0 | 06:19:24 | 65 |
| deepseek-v4-1-flash-1017 | 10,499,470 | $0.10 | 196,402 | 65,116 | 10,237,952 | 0 | 06:40:48 | 81 |
| qwen-4-max | 14,597,617 | $1.68 | 270,255 | 66,370 | 14,260,992 | 0 | 06:43:27 | 85 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-neon | Not recorded | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.20 | 65/65 |
| gemini-4-argon | Not recorded | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| qwen-4-max | $1.68 | 85/85 |
| grok-4-7 | Not recorded | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.34 | 29/29 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.76 | 60/60 |
| deepseek-v4-1-flash-1017 | $0.07 | 81/81 |
| haiku-5-5 | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| deepseek-v4-pro | $0.38 | 58/58 |
| glm-5-3 | $0.42 | 35/35 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,626,098 |
| Output | 920,569 |
| Cache Read | 119,034,286 |
| Cache Write | 1,200,249 |
| Calls with available telemetry | 953 |
| API estimate subtotal (available telemetry) | $44.61 |
| Recorded OpenRouter charges | $6.84 |
| Models with unavailable estimates | gemini-4-argon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-22 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Every collected run binds one-to-one to a coordinator-selected final edition session this date; there are no earlier, retried or unbound attempts in the collection.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-21T080621351982Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write (TTL unspecified) per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-21T080621351982Z/api-pricing.json, as of 2026-11-21); the 2026-11-22 daily pricing check verified rates unchanged, so the 2026-11-21 snapshot is the effective day-appropriate card; pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-three final HTML editions, bound by terminal-record session ID, not latest-by-name. No earlier or unbound sessions were collected this date. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-three collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-22T07:49:48-05:00. Pricing source: pricing/2026-11-21T080621351982Z/api-pricing.json, as of 2026-11-21; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $44.61; upper-bound additions from tier-indeterminate models (Gemini 4 Argon and Qwen regional estimates) bring the batch upper bound to $50.56. Recorded OpenRouter charges for the final editions: $6.84. Pricing snapshot age at report date: 1 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-22T06:06:06-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-21T080621351982Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-22/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-22.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

