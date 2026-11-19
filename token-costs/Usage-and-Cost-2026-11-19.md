# Token Usage and Cost - 2026-11-19

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 737,462 | $1.58 | 143,157 | 4,993 | 589,312 | 0 | 07:23:43 | 17 |
| gpt-6-astra | 1,457,319 | $2.58 | 87,798 | 6,705 | 1,362,816 | 0 | 05:31:41 | 22 |
| gemini-4-hydrogen | 1,723,969 | $0.62 | 177,908 | 31,302 | 1,514,759 | 0 | 07:22:36 | 22 |
| gemini-4-neon | 1,938,683 | $1.45 | 188,625 | 41,751 | 1,708,307 | 0 | 07:36:40 | 20 |
| sonnet-5-5 | 2,748,475 | $1.08 | 52 | 21,570 | 2,575,955 | 150,898 | 07:14:26 | 26 |
| gpt-6-1-terra | 2,878,385 | $0.30 | 113,002 | 9,799 | 2,755,584 | 0 | 05:44:18 | 34 |
| gpt-6-1-sol | 3,036,401 | $0.75 | 159,000 | 14,937 | 2,862,464 | 0 | 05:36:25 | 26 |
| gpt-6-luna | 3,298,381 | $0.05 | 140,331 | 16,290 | 3,141,760 | 0 | 07:43:31 | 37 |
| glm-5-3 | 3,416,940 | $1.11 | 107,778 | 23,275 | 3,285,887 | 0 | 06:09:03 | 47 |
| kimi-k3-1-pro | 3,890,112 | $1.24 | 122,565 | 24,891 | 3,742,656 | 0 | 06:19:48 | 36 |
| gpt-6-2-sol | 4,443,260 | $1.36 | 393,717 | 17,415 | 4,032,128 | 0 | 07:27:20 | 46 |
| gemini-4-argon | 4,482,867 | $1.55 | 262,081 | 61,180 | 4,159,606 | 0 | 05:51:43 | 39 |
| haiku-5-5 | 4,856,572 | $0.41 | 82 | 52,435 | 4,626,673 | 177,382 | 07:17:54 | 41 |
| opus-5-5 | 4,865,833 | $2.77 | 78 | 33,476 | 4,686,889 | 145,390 | 05:55:33 | 39 |
| qwen-3-8-max-0902 | 5,324,274 | $1.93 | 183,484 | 47,542 | 5,093,248 | 0 | 07:29:00 | 48 |
| fable-5-2 | 5,815,373 | $7.24 | 64 | 39,681 | 5,491,152 | 284,476 | 05:48:10 | 32 |
| grok-4-7 | 5,859,591 | $4.30 | 413,532 | 77,099 | 5,368,960 | 0 | 06:37:15 | 45 |
| deepseek-v4-pro | 6,116,369 | $0.39 | 188,969 | 67,048 | 5,860,352 | 0 | 06:02:03 | 53 |
| gemini-4-carbon | 6,292,319 | $2.06 | 384,661 | 70,610 | 5,837,048 | 0 | 06:15:24 | 32 |
| fable-5-1 | 6,942,444 | $10.30 | 1,058 | 60,313 | 6,600,043 | 281,030 | 05:31:41 | 34 |
| minimax-m3-1-flash | 8,890,450 | $0.22 | 458,331 | 42,359 | 8,389,760 | 0 | 06:26:36 | 75 |
| deepseek-v4-1-flash-1017 | 11,506,004 | $0.12 | 161,601 | 100,755 | 11,243,648 | 0 | 06:57:36 | 111 |
| qwen-4-max | 29,594,742 | $3.48 | 538,669 | 152,905 | 28,903,168 | 0 | 06:33:03 | 108 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-neon | Not recorded | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| qwen-4-max | $3.48 | 108/108 |
| fable-5-2 | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.24 | 36/36 |
| grok-4-7 | Not recorded | Not applicable |
| minimax-m3-1-flash | $0.22 | 75/75 |
| gemini-4-carbon | Not recorded | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.08 | 111/111 |
| gemini-4-argon | Not recorded | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| deepseek-v4-pro | $1.05 | 53/53 |
| qwen-3-8-max-0902 | $1.93 | 48/48 |
| gpt-6-1-terra | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| glm-5-3 | $0.78 | 47/47 |
| gpt-6-luna | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 4,226,543 |
| Output | 1,018,331 |
| Cache Read | 123,832,175 |
| Cache Write | 1,039,176 |
| Calls with available telemetry | 990 |
| API estimate subtotal (available telemetry) | $46.87 |
| Recorded OpenRouter charges | $8.77 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-luna (earlier failed attempt, excluded) | 338,315 | $0.01 | 40,467 | 3,192 | 294,656 | 0 | 05:49:30 | 10 |

| Session | Job label | Status | Calls | Reason |
|---|---|---|---|---|

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-19 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
One earlier coordinator-recorded attempt is reported separately: gpt-6-luna attempt 1 failed after 103 s scheduler time with no HTML produced (session 4bf2a2c3, recorded as kind "other"); its usage is not added to final-edition totals. No other unbound sessions were collected this date.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-18T223149877955Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-18T223149877955Z/api-pricing.json, as of 2026-11-18); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-three final HTML editions, bound by terminal-record session ID, not latest-by-name. The earlier failed attempt above is bound to the coordinator-recorded attempts array of its job; no unbound sessions were collected this date. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-three collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-19T07:56:47-05:00. Pricing source: pricing/2026-11-18T223149877955Z/api-pricing.json, as of 2026-11-18; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $46.87; upper-bound additions from tier-indeterminate models (Qwen regional upper estimates) bring the batch upper bound to $52.28. Recorded OpenRouter charges for the final editions: $8.77. Pricing snapshot age at report date: 1 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-18T223149877955Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-19/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-19.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

