# Token Usage and Cost - 2026-11-24

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 988,824 | $1.89 | 167,649 | 5,559 | 815,616 | 0 | 06:50:46 | 20 |
| gemini-4-hydrogen | 1,443,688 | $0.50 | 142,394 | 24,878 | 1,276,416 | 0 | 07:03:15 | 18 |
| gpt-6-astra | 1,519,776 | $2.88 | 108,787 | 7,853 | 1,403,136 | 0 | 05:31:51 | 19 |
| gpt-6-1-terra | 2,006,934 | $0.24 | 98,515 | 8,899 | 1,899,520 | 0 | 05:44:44 | 28 |
| gemini-4-neon | 2,258,358 | $1.45 | 192,595 | 37,793 | 2,027,970 | 0 | 07:04:32 | 25 |
| sonnet-5-5 | 2,627,552 | $1.05 | 50 | 20,912 | 2,457,845 | 148,745 | 06:55:08 | 25 |
| glm-5-3 | 2,940,393 | $0.98 | 111,968 | 20,105 | 2,808,320 | 0 | 06:15:29 | 46 |
| gpt-6-luna | 3,356,374 | $0.06 | 146,293 | 26,593 | 3,183,488 | 0 | 05:49:19 | 35 |
| kimi-k3-1-pro | 3,617,996 | $1.26 | 169,461 | 23,575 | 3,424,960 | 0 | 06:14:07 | 34 |
| gemini-4-argon | 3,721,169 | $1.34 (upper estimate) | 265,718 | 46,699 | 3,408,752 | 0 | 05:58:57 | 34 |
| gpt-6-1-sol | 3,743,436 | $0.80 | 135,096 | 17,044 | 3,591,296 | 0 | 05:36:44 | 34 |
| grok-4-7 | 3,824,154 | $2.53 | 173,951 | 65,435 | 3,584,768 | 0 | 06:27:43 | 38 |
| haiku-5-5 | 4,149,323 | $0.35 | 70 | 52,762 | 3,931,854 | 164,637 | 06:58:36 | 35 |
| fable-5-1 | 4,471,114 | $9.00 | 738 | 52,998 | 4,152,097 | 265,281 | 05:31:51 | 24 |
| minimax-m3-1-flash | 4,684,685 | $0.10 | 119,752 | 27,333 | 4,537,600 | 0 | 06:24:14 | 47 |
| gemini-4-carbon | 4,765,237 | $1.58 | 284,040 | 56,788 | 4,424,409 | 0 | 06:21:10 | 28 |
| opus-5-5 | 5,385,263 | $2.90 | 82 | 32,216 | 5,200,584 | 152,381 | 05:51:57 | 41 |
| fable-5-2 | 5,432,348 | $6.08 | 72 | 38,475 | 5,174,411 | 219,390 | 05:45:40 | 36 |
| deepseek-v4-pro | 5,454,194 | $0.36 | 180,567 | 61,211 | 5,212,416 | 0 | 05:57:35 | 55 |
| gpt-6-2-sol | 5,574,374 | $1.60 | 442,526 | 20,168 | 5,111,680 | 0 | 06:54:17 | 56 |
| qwen-3-8-max-0902 | 6,041,845 | $2.10 | 180,609 | 47,348 | 5,813,888 | 0 | 07:06:49 | 57 |
| deepseek-v4-1-flash-1017 | 7,327,357 | $0.09 | 140,391 | 74,006 | 7,112,960 | 0 | 06:41:00 | 72 |
| qwen-4-max | 8,087,452 | $1.05 | 190,040 | 51,780 | 7,845,632 | 0 | 06:37:44 | 71 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| deepseek-v4-1-flash-1017 | $0.06 | 72/72 |
| sonnet-5-5 | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| kimi-k3-1-pro | $1.26 | 34/34 |
| deepseek-v4-pro | $0.95 | 55/55 |
| grok-4-7 | Not recorded | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| glm-5-3 | $0.96 | 46/46 |
| qwen-3-8-max-0902 | $2.10 | 57/57 |
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| qwen-4-max | $1.05 | 71/71 |
| fable-5-2 | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.10 | 47/47 |
| gpt-6-astra | No per-token charge | Not applicable |
| gemini-4-neon | Not recorded | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,251,364 |
| Output | 820,430 |
| Cache Read | 88,399,618 |
| Cache Write | 950,434 |
| Calls with available telemetry | 878 |
| API estimate subtotal (available telemetry) | $38.85 |
| Recorded OpenRouter charges | $6.48 |
| Models with unavailable estimates | gemini-4-argon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-24 cohort.
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
Collector generated: 2026-11-24T07:37:38-05:00. Pricing source: pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $38.85; upper-bound additions from tier-indeterminate models (Gemini 4 Argon and Qwen regional estimates) bring the batch upper bound to $43.33. Recorded OpenRouter charges for the final editions: $6.48. Pricing snapshot age at report date: 1 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-24T05:58:57-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-23T020315256499Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-24/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-24.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

