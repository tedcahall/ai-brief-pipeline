# Token Usage and Cost - 2026-11-17

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gemini-4-hydrogen | 1,713,178 | $0.60 | 174,037 | 29,452 | 1,509,689 | 0 | 07:08:06 | 22 |
| gpt-6-astra | 2,220,257 | $3.97 | 133,617 | 11,248 | 2,075,392 | 0 | 05:31:25 | 23 |
| gpt-6-1-terra | 2,389,657 | $0.27 | 108,752 | 9,033 | 2,271,872 | 0 | 05:47:00 | 30 |
| gpt-6-luna | 3,292,178 | $0.06 | 135,747 | 20,943 | 3,135,488 | 0 | 05:51:37 | 36 |
| gpt-6-1-sol | 4,201,191 | $0.89 | 155,615 | 17,544 | 4,028,032 | 0 | 05:37:51 | 34 |
| sonnet-5-5 | 4,401,912 | $1.40 | 68 | 26,160 | 4,197,095 | 178,589 | 06:58:52 | 34 |
| gemini-4-argon | 4,531,147 | $1.58 | 328,462 | 50,328 | 4,152,357 | 0 | 06:22:13 | 38 |
| qwen-3-8-max-0902 | 4,586,062 | $1.73 | 160,351 | 52,335 | 4,373,376 | 0 | 05:59:35 | 48 |
| glm-5-3 | 4,739,749 | $1.65 | 269,124 | 25,697 | 4,444,928 | 0 | 06:42:10 | 58 |
| fable-5-2 | 4,767,067 | $5.73 | 62 | 33,809 | 4,516,340 | 216,856 | 05:42:19 | 31 |
| deepseek-v4-pro | 5,097,397 | $0.34 | 178,783 | 57,942 | 4,860,672 | 0 | 05:55:24 | 58 |
| fable-5-1 | 5,316,809 | $10.07 | 866 | 49,430 | 4,949,019 | 317,494 | 05:31:26 | 28 |
| grok-4-7 | 5,355,953 | $3.38 | 209,927 | 70,058 | 5,075,968 | 0 | 06:27:05 | 46 |
| gemini-4-carbon | 5,383,160 | $1.75 | 336,259 | 58,150 | 4,988,751 | 0 | 06:50:15 | 31 |
| haiku-5-5 | 5,532,546 | $0.42 | 94 | 55,124 | 5,296,325 | 181,003 | 07:02:58 | 47 |
| minimax-m3-1-flash | 5,706,839 | $0.12 | 122,600 | 26,735 | 5,557,504 | 0 | 06:23:03 | 57 |
| opus-5-5 | 5,946,312 | $3.25 | 80 | 33,149 | 5,732,438 | 180,645 | 05:49:08 | 40 |
| kimi-k3-1-pro | 9,515,227 | $3.07 | 408,663 | 44,222 | 9,062,342 | 0 | 06:11:08 | 57 |
| deepseek-v4-1-flash-1017 | 10,990,805 | $0.11 | 192,722 | 85,891 | 10,712,192 | 0 | 06:44:14 | 93 |
| qwen-4-max | 11,118,877 | $1.63 | 391,294 | 72,607 | 10,654,976 | 0 | 07:30:54 | 57 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-hydrogen | Not recorded | Not applicable |
| qwen-4-max | $1.63 | 57/57 |
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| kimi-k3-1-pro | $3.07 | 57/57 |
| fable-5-1 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| deepseek-v4-pro | $1.12 | 58/58 |
| fable-5-2 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.12 | 57/57 |
| qwen-3-8-max-0902 | $1.73 | 48/48 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| glm-5-3 | $0.80 | 58/58 |
| haiku-5-5 | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.08 | 93/93 |
| gpt-6-luna | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,307,123 |
| Output | 829,857 |
| Cache Read | 101,594,756 |
| Cache Write | 1,074,587 |
| Calls with available telemetry | 868 |
| API estimate subtotal (available telemetry) | $42.00 |
| Recorded OpenRouter charges | $8.54 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| qwen-4-max (earlier failed attempt, excluded) | 712,443 | $0.24 | 98,044 | 12,799 | 601,600 | 0 | 07:20:34 | 17 |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 20 final editions of the 2026-11-17 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
One earlier coordinator-recorded attempt is reported separately: qwen-4-max attempt 1 failed at dispatch (Alibaba provider rejected the request with data_inspection_failed; 290 s scheduler time, session 4975de30); its usage is not added to final-edition totals. A pending non-cohort experiment job (GPT-6.1 Terra MEDIUM experiment) was not run and is not part of this report.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-17T080402783388Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-17T080402783388Z/api-pricing.json, as of 2026-11-17); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty final HTML editions, bound by terminal-record session ID, not latest-by-name. The earlier failed attempt above is bound to the coordinator-recorded attempts array of its job. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-17T07:58:13-05:00. Pricing source: pricing/2026-11-17T080402783388Z/api-pricing.json, as of 2026-11-17; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 15, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $42.00; upper-bound additions from tier-indeterminate models (Qwen regional upper estimates) bring the batch upper bound to $45.35. Recorded OpenRouter charges for the final editions: $8.54. Pricing snapshot age at report date: 0 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-17T080402783388Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-17/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-17.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

