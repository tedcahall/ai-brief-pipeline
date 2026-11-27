# Token Usage and Cost - 2026-11-27

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 573,133 | $1.34 | 122,331 | 4,594 | 446,208 | 0 | 06:54:56 | 14 |
| gpt-6-astra | 1,693,856 | $3.30 | 139,675 | 7,045 | 1,547,136 | 0 | 07:14:19 | 22 |
| gemini-4-neon | 1,916,086 | $1.56 | 248,510 | 38,094 | 1,629,482 | 0 | 07:06:58 | 24 |
| gpt-6-1-terra | 2,194,023 | $0.24 | 89,669 | 10,018 | 2,094,336 | 0 | 05:40:55 | 33 |
| gpt-6-1-sol | 2,625,515 | $0.62 | 114,831 | 14,428 | 2,496,256 | 0 | 05:34:05 | 29 |
| gemini-4-hydrogen | 2,881,702 | $0.74 | 194,738 | 33,308 | 2,653,656 | 0 | 07:39:08 | 26 |
| gpt-6-2-sol | 3,090,686 | $1.20 | 368,182 | 19,016 | 2,703,488 | 0 | 06:57:50 | 36 |
| sonnet-5-5 | 4,016,932 | $1.25 | 70 | 24,823 | 3,838,153 | 153,886 | 07:28:09 | 35 |
| gemini-4-argon | 4,078,175 | $1.37 (upper estimate) | 230,615 | 52,564 | 3,794,996 | 0 | 05:57:44 | 36 |
| glm-5-3 | 4,172,164 | $1.33 | 108,188 | 28,923 | 4,035,053 | 0 | 06:09:55 | 54 |
| deepseek-v4-pro | 4,386,073 | $0.39 | 261,204 | 66,501 | 4,058,368 | 0 | 05:56:30 | 54 |
| gpt-6-luna | 4,458,535 | $0.08 | 170,248 | 32,415 | 4,255,872 | 0 | 05:46:05 | 38 |
| haiku-5-5 | 4,508,957 | $0.36 | 78 | 51,601 | 4,287,893 | 169,385 | 07:33:26 | 39 |
| opus-5-5 | 4,778,408 | $2.82 | 74 | 30,741 | 4,586,906 | 160,687 | 05:51:05 | 37 |
| fable-5-1 | 5,217,045 | $8.74 | 962 | 46,719 | 4,910,982 | 258,382 | 05:31:32 | 31 |
| fable-5-2 | 5,217,595 | $6.29 | 64 | 36,199 | 4,940,204 | 241,128 | 05:44:47 | 32 |
| kimi-k3-1-pro | 5,774,847 | $1.80 | 173,847 | 33,551 | 5,567,449 | 0 | 06:18:12 | 51 |
| grok-4-7 | 5,883,863 | $3.90 | 206,541 | 74,634 | 5,602,688 | 0 | 06:48:23 | 48 |
| gemini-4-carbon | 7,254,369 | $2.02 | 344,703 | 64,789 | 6,844,877 | 0 | 06:17:19 | 35 |
| qwen-3-8-max-0902 | 7,598,650 | $2.64 | 225,279 | 59,835 | 7,313,536 | 0 | 07:44:15 | 57 |
| qwen-4-max | 10,290,286 | $1.51 | 290,687 | 91,375 | 9,908,224 | 0 | 06:35:44 | 63 |
| minimax-m3-1-flash | 11,496,314 | $0.27 | 459,108 | 58,774 | 10,978,432 | 0 | 06:26:07 | 89 |
| deepseek-v4-1-flash-1017 | 18,864,244 | $0.16 | 205,238 | 128,958 | 18,530,048 | 0 | 07:04:53 | 136 |

## Failed-attempt usage (no edition produced)

| Model | Coordinator run ID | Total tokens | API Cost* | Status |
|---|---|---|---|---|
| gpt-6-astra (failed attempt, no edition) | cron-request.c87b242c-35ea-41b5-b229-938003c54546 | 479,030 | $1.31 | ok |

This row is the coordinator-recorded failed first attempt of gpt-6-astra (no HTML produced). Its available telemetry is reported separately and is not included in final-edition totals or the consensus.

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-neon | Not recorded | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.64 | 57/57 |
| sonnet-5-5 | No per-token charge | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| kimi-k3-1-pro | $2.24 | 51/51 |
| fable-5-2 | No per-token charge | Not applicable |
| deepseek-v4-pro | $1.17 | 54/54 |
| qwen-4-max | $1.51 | 62/63 |
| gpt-6-luna | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.17 | 136/136 |
| glm-5-3 | $1.33 | 54/54 |
| gemini-4-hydrogen | Not recorded | Not applicable |
| minimax-m3-1-flash | $0.27 | 89/89 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,954,842 |
| Output | 1,008,905 |
| Cache Read | 117,024,243 |
| Cache Write | 983,468 |
| Calls with available telemetry | 1019 |
| API estimate subtotal (available telemetry) | $42.56 |
| Recorded OpenRouter charges | $9.32 |
| Models with unavailable estimates | gemini-4-argon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-27 cohort; every cohort model produced a terminal edition this date (full batch).
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Every collected final run binds one-to-one to a coordinator-selected final edition session this date; the only additional row is the coordinator-recorded failed gpt-6-astra attempt, bound by attempt session key and listed separately.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the collector-selected snapshot pricing/2026-11-23T020315256499Z/api-pricing.json (canonical key qwen4-max) per million tokens. Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol), with Standard short tiers at or below 272,000 prompt tokens per request and Standard long above; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected snapshot (pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23); pricing verification passed (17 files checked) and the collector records pricing_fallback_used=True (latest fully verified card rather than a fresh same-day capture). Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the 23 final HTML editions, bound by terminal-record session ID, not latest-by-name. The single additional row is the coordinator-recorded failed first gpt-6-astra attempt, bound by attempt record and shown in the failed-attempt table only. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The 23 collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-27T08:17:20-05:00. Pricing source: pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $42.56; upper-bound additions from tier-indeterminate models (Gemini 4 Argon and Qwen regional estimates) bring the batch upper bound to $48.08. Recorded OpenRouter charges for the final editions: $9.32. Pricing snapshot age at report date: 4 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-27T05:57:44-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-23T020315256499Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-27/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-27.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

