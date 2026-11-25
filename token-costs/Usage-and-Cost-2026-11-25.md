# Token Usage and Cost - 2026-11-25

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 915,500 | $1.82 | 162,375 | 5,477 | 747,648 | 0 | 07:19:23 | 19 |
| gemini-4-hydrogen | 1,730,038 | $0.71 | 256,330 | 28,336 | 1,445,372 | 0 | 07:14:34 | 22 |
| gpt-6-astra | 1,790,503 | $3.28 | 122,162 | 8,053 | 1,660,288 | 0 | 05:31:28 | 21 |
| gpt-6-1-sol | 1,945,702 | $0.58 | 127,629 | 14,425 | 1,803,648 | 0 | 05:36:21 | 21 |
| gemini-4-neon | 2,324,261 | $1.46 | 183,270 | 39,493 | 2,101,498 | 0 | 07:32:06 | 22 |
| gpt-6-1-terra | 2,722,696 | $0.29 | 104,726 | 10,354 | 2,607,616 | 0 | 05:43:23 | 34 |
| glm-5-3 | 2,997,901 | $1.05 | 158,907 | 21,830 | 2,817,164 | 0 | 06:23:42 | 44 |
| sonnet-5-5 | 4,028,609 | $1.32 | 70 | 26,612 | 3,834,499 | 167,428 | 07:03:39 | 35 |
| gpt-6-2-sol | 4,369,116 | $1.35 | 387,610 | 17,986 | 3,963,520 | 0 | 07:23:23 | 42 |
| fable-5-2 | 4,868,454 | $6.10 | 64 | 36,983 | 4,600,407 | 231,000 | 05:43:16 | 32 |
| gemini-4-argon | 4,900,661 | $1.61 (upper estimate) | 254,658 | 64,674 | 4,581,329 | 0 | 06:04:43 | 38 |
| deepseek-v4-pro | 4,949,547 | $0.33 | 159,854 | 58,813 | 4,730,880 | 0 | 05:55:35 | 59 |
| grok-4-7 | 5,176,394 | $3.59 | 430,547 | 64,375 | 4,681,472 | 0 | 06:35:36 | 42 |
| opus-5-5 | 5,347,607 | $2.91 | 80 | 30,513 | 5,158,461 | 158,553 | 05:50:14 | 40 |
| gpt-6-luna | 5,893,023 | $0.10 | 180,685 | 45,650 | 5,666,688 | 0 | 05:48:32 | 49 |
| kimi-k3-1-pro | 5,909,250 | $1.88 | 232,661 | 28,695 | 5,647,894 | 0 | 06:11:10 | 46 |
| haiku-5-5 | 5,923,363 | $0.49 | 92 | 59,228 | 5,672,394 | 191,649 | 07:08:18 | 46 |
| deepseek-v4-1-flash-1017 | 7,089,993 | $0.08 | 147,002 | 62,223 | 6,880,768 | 0 | 06:50:53 | 71 |
| qwen-3-8-max-0902 | 7,387,789 | $2.61 | 242,698 | 58,883 | 7,086,208 | 0 | 07:19:08 | 52 |
| fable-5-1 | 7,595,795 | $9.91 | 1,282 | 54,599 | 7,272,627 | 267,287 | 05:31:28 | 41 |
| gemini-4-carbon | 9,433,199 | $3.07 | 753,419 | 70,183 | 8,609,597 | 0 | 06:30:30 | 38 |
| minimax-m3-1-flash | 10,528,629 | $0.29 | 336,553 | 140,364 | 10,051,712 | 0 | 06:23:09 | 71 |
| qwen-4-max | 12,529,227 | $1.53 | 267,617 | 65,002 | 12,196,608 | 0 | 07:01:23 | 73 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-argon | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.05 | 71/71 |
| glm-5-3 | $0.55 | 44/44 |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gemini-4-neon | Not recorded | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| qwen-3-8-max-0902 | $2.61 | 52/52 |
| gpt-6-astra | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| qwen-4-max | $1.53 | 73/73 |
| deepseek-v4-pro | $0.87 | 59/59 |
| fable-5-2 | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.88 | 46/46 |
| sonnet-5-5 | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.29 | 71/71 |
| gpt-6-2-sol | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 4,510,291 |
| Output | 1,012,751 |
| Cache Read | 113,818,298 |
| Cache Write | 1,015,917 |
| Calls with available telemetry | 958 |
| API estimate subtotal (available telemetry) | $44.72 |
| Recorded OpenRouter charges | $7.77 |
| Models with unavailable estimates | gemini-4-argon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-25 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Every collected run binds one-to-one to a coordinator-selected final edition session this date; there are no earlier, retried or unbound attempts in the collection.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the collector-selected snapshot pricing/2026-11-23T020315256499Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write (TTL unspecified) per million tokens Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected snapshot (pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23); pricing verification passed (17 files checked) and the collector records pricing_fallback_used=True (latest fully verified card rather than a fresh same-day capture). Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-three final HTML editions, bound by terminal-record session ID, not latest-by-name. No earlier or unbound sessions were collected this date. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-three collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-25T07:49:55-05:00. Pricing source: pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $44.72; upper-bound additions from tier-indeterminate models (Gemini 4 Argon and Qwen regional estimates) bring the batch upper bound to $50.47. Recorded OpenRouter charges for the final editions: $7.77. Pricing snapshot age at report date: 2 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-25T06:04:43-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-23T020315256499Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-25/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-25.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

