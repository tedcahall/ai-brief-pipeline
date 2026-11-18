# Token Usage and Cost - 2026-11-18

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 798,346 | $1.67 | 148,775 | 5,603 | 643,968 | 0 | 07:16:33 | 17 |
| gpt-6-astra | 1,286,840 | $2.46 | 97,365 | 6,115 | 1,183,360 | 0 | 05:31:36 | 19 |
| gpt-6-1-sol | 2,211,817 | $0.61 | 132,592 | 13,817 | 2,065,408 | 0 | 05:35:19 | 22 |
| gemini-4-hydrogen | 2,339,918 | $0.70 | 186,299 | 35,296 | 2,118,323 | 0 | 07:03:17 | 25 |
| gpt-6-1-terra | 2,499,838 | $0.27 | 103,021 | 9,361 | 2,387,456 | 0 | 05:42:08 | 32 |
| gpt-6-2-sol | 2,955,674 | $1.03 | 309,645 | 14,989 | 2,631,040 | 0 | 07:20:32 | 35 |
| sonnet-5-5 | 3,157,932 | $1.10 | 62 | 22,056 | 2,991,749 | 144,065 | 06:53:31 | 31 |
| glm-5-3 | 3,307,142 | $1.09 | 115,158 | 25,068 | 3,166,916 | 0 | 06:18:20 | 48 |
| deepseek-v4-pro | 4,068,421 | $0.34 | 151,155 | 76,498 | 3,840,768 | 0 | 05:56:28 | 48 |
| kimi-k3-1-pro | 4,548,901 | $1.41 | 174,499 | 19,394 | 4,355,008 | 0 | 06:14:54 | 43 |
| gemini-4-argon | 4,641,279 | $1.51 | 298,135 | 48,122 | 4,295,022 | 0 | 05:57:46 | 34 |
| gpt-6-luna | 4,731,745 | $0.07 | 149,462 | 28,555 | 4,553,728 | 0 | 05:46:42 | 47 |
| minimax-m3-1-flash | 5,309,325 | $0.12 | 168,847 | 23,294 | 5,117,184 | 0 | 06:20:12 | 43 |
| fable-5-1 | 5,558,014 | $9.69 | 866 | 55,890 | 5,222,399 | 278,859 | 05:31:36 | 28 |
| qwen-3-8-max-0902 | 5,708,376 | $2.07 | 201,399 | 50,209 | 5,456,768 | 0 | 07:08:23 | 52 |
| fable-5-2 | 5,817,970 | $6.63 | 66 | 35,408 | 5,525,985 | 256,511 | 05:43:40 | 33 |
| opus-5-5 | 6,048,495 | $3.07 | 90 | 34,230 | 5,862,524 | 151,651 | 05:49:59 | 45 |
| grok-4-7 | 6,317,882 | $4.12 | 204,967 | 77,075 | 6,035,840 | 0 | 06:23:10 | 53 |
| deepseek-v4-1-flash-1017 | 6,334,270 | $0.09 | 165,600 | 74,078 | 6,094,592 | 0 | 07:29:00 | 60 |
| haiku-5-5 | 6,769,788 | $0.59 | 92 | 68,588 | 6,462,825 | 238,283 | 06:57:05 | 46 |
| gemini-4-carbon | 9,734,478 | $2.46 | 419,072 | 69,674 | 9,245,732 | 0 | 06:23:40 | 42 |
| qwen-4-max | 15,268,703 | $1.94 | 356,444 | 87,811 | 14,824,448 | 0 | 06:44:18 | 74 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| deepseek-v4-1-flash-1017 | $0.06 | 60/60 |
| fable-5-1 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| glm-5-3 | $0.76 | 48/48 |
| gpt-6-2-sol | No per-token charge | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.07 | 52/52 |
| qwen-4-max | $1.94 | 74/74 |
| deepseek-v4-pro | $1.01 | 48/48 |
| sonnet-5-5 | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.41 | 43/43 |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.12 | 43/43 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,383,611 |
| Output | 881,131 |
| Cache Read | 104,081,043 |
| Cache Write | 1,069,369 |
| Calls with available telemetry | 877 |
| API estimate subtotal (available telemetry) | $43.03 |
| Recorded OpenRouter charges | $7.36 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| deepseek-v4-1-flash-1017 (earlier failed attempt, excluded) | 6,362,304 | $0.08 | 136,839 | 75,705 | 6,149,760 | 0 | 06:40:25 | 69 |

| Session | Job label | Status | Calls | Reason |
|---|---|---|---|---|
| 3f6b4070 | GPT-6.2 Astra | error | 0 | Not a coordinator-recorded attempt; not bound to any final edition session; excluded from totals |
| 3aaafa0b | GPT-6.2 Astra | ok | 2 | Not a coordinator-recorded attempt; not bound to any final edition session; excluded from totals |
| c052f3e1 | GPT-6.2 Sol | error | 0 | Not a coordinator-recorded attempt; not bound to any final edition session; excluded from totals |
| b2a8687e | GPT-6.2 Sol | ok | 3 | Not a coordinator-recorded attempt; not bound to any final edition session; excluded from totals |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 22 final editions of the 2026-11-18 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
One earlier coordinator-recorded attempt is reported separately: deepseek-v4-1-flash-1017 attempt 1 failed after an OpenRouter provider error ("terminated", request 44; 730 s scheduler time, session 132cd072, no HTML produced); its usage is not added to final-edition totals. Four additional collected sessions (job-labeled GPT-6.2 Astra/Sol at 04:43 and 05:02 ET, sessions 3f6b4070, 3aaafa0b, c052f3e1, b2a8687e) do not match any coordinator-recorded attempt or final-edition session; they are excluded unbound attempts, not model runs.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-17T233002747281Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-17T233002747281Z/api-pricing.json, as of 2026-11-17); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-two final HTML editions, bound by terminal-record session ID, not latest-by-name. The earlier failed attempt above is bound to the coordinator-recorded attempts array of its job; the four unbound sessions are listed with reasons. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-two collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-18T07:44:39-05:00. Pricing source: pricing/2026-11-17T233002747281Z/api-pricing.json, as of 2026-11-17; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 16, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $43.03; upper-bound additions from tier-indeterminate models (Qwen regional upper estimates) bring the batch upper bound to $47.04. Recorded OpenRouter charges for the final editions: $7.36. Pricing snapshot age at report date: 1 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- GPT-6.2 Astra (2026-11-18T04:43:33-05:00): no per-call telemetry or native session binding available
- GPT-6.2 Sol (2026-11-18T04:43:36-05:00): no per-call telemetry or native session binding available

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-17T233002747281Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-18/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-18.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

