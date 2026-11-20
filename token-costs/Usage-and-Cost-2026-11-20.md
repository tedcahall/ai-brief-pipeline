# Token Usage and Cost - 2026-11-20

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 783,243 | $1.62 | 146,195 | 4,856 | 632,192 | 0 | 07:12:34 | 17 |
| gpt-6-1-terra | 1,745,263 | $0.21 | 88,700 | 8,051 | 1,648,512 | 0 | 05:43:19 | 26 |
| gpt-6-astra | 1,932,434 | $3.60 | 141,416 | 8,106 | 1,782,912 | 0 | 05:31:29 | 20 |
| gemini-4-hydrogen | 2,022,050 | $0.63 | 178,125 | 29,962 | 1,813,963 | 0 | 06:56:29 | 23 |
| gemini-4-neon | 2,689,919 | $1.61 | 217,360 | 39,240 | 2,433,319 | 0 | 07:24:31 | 25 |
| gpt-6-1-sol | 2,930,755 | $0.71 | 142,028 | 14,839 | 2,773,888 | 0 | 05:36:19 | 27 |
| sonnet-5-5 | 3,454,477 | $1.18 | 64 | 26,444 | 3,281,042 | 146,927 | 06:45:38 | 32 |
| kimi-k3-1-pro | 3,537,717 | $1.17 | 117,173 | 25,600 | 3,394,944 | 0 | 06:11:34 | 34 |
| gpt-6-2-sol | 3,714,935 | $1.22 | 360,460 | 16,875 | 3,337,600 | 0 | 07:16:02 | 43 |
| fable-5-2 | 4,292,022 | $5.59 | 56 | 31,478 | 4,040,609 | 219,879 | 05:42:36 | 28 |
| grok-4-7 | 4,422,097 | $2.81 | 195,474 | 56,127 | 4,170,496 | 0 | 06:20:26 | 34 |
| glm-5-3 | 4,430,290 | $1.41 | 131,213 | 25,206 | 4,273,871 | 0 | 06:14:58 | 49 |
| gemini-4-argon | 5,331,561 | $1.54 | 289,654 | 45,904 | 4,996,003 | 0 | 06:04:10 | 41 |
| haiku-5-5 | 5,587,820 | $0.48 | 84 | 64,139 | 5,326,937 | 196,660 | 06:49:40 | 42 |
| fable-5-1 | 5,811,644 | $9.00 | 994 | 48,978 | 5,503,162 | 258,510 | 05:31:30 | 32 |
| deepseek-v4-pro | 5,840,328 | $0.81 | 950,366 | 39,786 | 4,850,176 | 0 | 05:54:15 | 69 |
| minimax-m3-1-flash | 6,018,323 | $0.13 | 155,543 | 32,636 | 5,830,144 | 0 | 06:16:10 | 52 |
| gemini-4-carbon | 6,143,117 | $1.97 | 340,522 | 71,218 | 5,731,377 | 0 | 06:22:06 | 34 |
| qwen-3-8-max-0902 | 6,515,494 | $2.31 | 225,443 | 49,539 | 6,240,512 | 0 | 07:00:30 | 52 |
| opus-5-5 | 6,672,775 | $3.34 | 96 | 33,016 | 6,466,886 | 172,777 | 05:48:20 | 48 |
| gpt-6-luna | 6,730,197 | $0.10 | 192,645 | 41,424 | 6,496,128 | 0 | 05:47:57 | 53 |
| deepseek-v4-1-flash-1017 | 6,874,024 | $0.09 | 160,439 | 75,377 | 6,638,208 | 0 | 06:34:20 | 68 |
| qwen-4-max | 18,075,418 | $2.20 | 409,484 | 84,622 | 17,581,312 | 0 | 06:39:50 | 89 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| fable-5-1 | No per-token charge | Not applicable |
| gemini-4-neon | Not recorded | Not applicable |
| qwen-4-max | $2.20 | 89/89 |
| fable-5-2 | No per-token charge | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| qwen-3-8-max-0902 | $2.31 | 52/52 |
| sonnet-5-5 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.13 | 52/52 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.17 | 34/34 |
| deepseek-v4-1-flash-1017 | $0.06 | 68/68 |
| glm-5-3 | $0.70 | 49/49 |
| haiku-5-5 | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| deepseek-v4-pro | $2.09 | 69/69 |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 4,443,534 |
| Output | 873,423 |
| Cache Read | 109,244,193 |
| Cache Write | 994,753 |
| Calls with available telemetry | 938 |
| API estimate subtotal (available telemetry) | $43.72 |
| Recorded OpenRouter charges | $8.66 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|

| Session | Job label | Status | Calls | Reason |
|---|---|---|---|---|

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-20 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
No earlier or unbound sessions were collected this date; every collected run binds one-to-one to a coordinator-selected final edition.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-18T223149877955Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write (TTL unspecified) per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-18T223149877955Z/api-pricing.json, as of 2026-11-18); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-three final HTML editions, bound by terminal-record session ID, not latest-by-name. No earlier or unbound sessions were collected this date. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-three collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-20T07:37:17-05:00. Pricing source: pricing/2026-11-18T223149877955Z/api-pricing.json, as of 2026-11-18; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $43.72; upper-bound additions from tier-indeterminate models (Qwen regional upper estimates) bring the batch upper bound to $48.23. Recorded OpenRouter charges for the final editions: $8.66. Pricing snapshot age at report date: 2 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-18T223149877955Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-20/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-20.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

