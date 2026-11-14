# Token Usage and Cost - 2026-11-14

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-1-terra | 1,773,659 | $0.30 | 177,431 | 9,284 | 1,586,944 | 0 | 05:44:43 | 27 |
| gemini-4-hydrogen | 2,085,857 | $0.66 | 189,436 | 31,132 | 1,865,289 | 0 | 06:57:24 | 23 |
| gpt-6-astra | 2,202,067 | $4.03 | 132,597 | 13,022 | 2,056,448 | 0 | 05:31:23 | 23 |
| gpt-6-1-sol | 2,614,406 | $0.66 | 142,529 | 12,997 | 2,458,880 | 0 | 05:38:21 | 25 |
| kimi-k3-1-pro | 3,640,017 | $1.18 | 137,820 | 20,917 | 3,481,280 | 0 | 06:05:07 | 32 |
| gemini-4-argon | 3,781,546 | $1.40 | 267,015 | 51,543 | 3,462,988 | 0 | 06:42:58 | 32 |
| deepseek-v4-pro | 4,435,907 | $0.38 | 318,224 | 41,139 | 4,076,544 | 0 | 05:52:11 | 59 |
| grok-4-7 | 4,545,973 | $3.07 | 203,184 | 68,229 | 4,274,560 | 0 | 06:15:46 | 37 |
| sonnet-5-5 | 4,615,412 | $1.37 | 76 | 27,927 | 4,424,235 | 163,174 | 06:47:05 | 38 |
| glm-5-3 | 4,667,188 | $1.44 | 119,046 | 22,062 | 4,526,080 | 0 | 07:03:56 | 58 |
| fable-5-2 | 4,881,756 | $5.91 | 62 | 33,739 | 4,620,526 | 227,429 | 05:40:36 | 31 |
| haiku-5-5 | 4,922,167 | $0.41 | 78 | 51,739 | 4,679,081 | 191,269 | 06:52:49 | 39 |
| fable-5-1 | 5,572,425 | $9.10 | 866 | 41,055 | 5,244,312 | 286,192 | 05:31:23 | 28 |
| opus-5-5 | 6,482,945 | $3.60 | 88 | 32,067 | 6,236,356 | 214,434 | 05:46:22 | 44 |
| qwen-3-8-max-0902 | 6,621,760 | $2.36 | 200,544 | 61,152 | 6,360,064 | 0 | 06:05:14 | 56 |
| gpt-6-luna | 7,044,702 | $0.11 | 179,574 | 41,448 | 6,823,680 | 0 | 05:49:24 | 58 |
| gemini-4-carbon | 8,074,947 | $2.32 | 438,759 | 68,264 | 7,567,924 | 0 | 07:11:53 | 39 |
| minimax-m3-1-flash | 10,198,396 | $0.23 | 188,034 | 91,130 | 9,919,232 | 0 | 06:08:40 | 71 |
| deepseek-v4-1-flash-1017 | 10,455,328 | $0.10 | 177,003 | 71,605 | 10,206,720 | 0 | 06:33:25 | 95 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-carbon | Not recorded | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.36 | 56/56 |
| minimax-m3-1-flash | $0.23 | 71/71 |
| deepseek-v4-1-flash-1017 | $0.07 | 95/95 |
| glm-5-3 | $0.72 | 58/58 |
| gpt-6-luna | No per-token charge | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.18 | 32/32 |
| gpt-6-astra | No per-token charge | Not applicable |
| deepseek-v4-pro | $0.55 | 59/59 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 2,872,366 |
| Output | 790,451 |
| Cache Read | 93,871,143 |
| Cache Write | 1,082,498 |
| Calls with available telemetry | 815 |
| API estimate subtotal (available telemetry) | $38.63 |
| Recorded OpenRouter charges | $5.11 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| None - every cohort run succeeded on its first dispatch; no interrupted or retried attempts exist for this date | — | — | — | — | — | — | — | — |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 19 final editions of the 2026-11-14 batch.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost and totals, as requested (its deployment tier is not determinable from usage this date: Singapore / International / Global). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
*pricing uses the collector-selected snapshot (pricing/2026-11-13T113820742994Z, as of 2026-11-13, no newer snapshot existed so no fallback substitution was needed; the daily source check on 2026-11-14 08:04 UTC reported all 19 models unchanged); all nineteen model identities resolved, including google/gemini-4-hydrogen (Standard $1.50 input / $7.50 output including thinking / $0.075 implicit cache read per million tokens; explicit caching unsupported). Verify official validity dates before later runs.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the nineteen final HTML editions, bound by terminal-record session ID, not latest-by-name. No earlier attempts exist for this date: the collector found one not-yet-run diagnostic cron job (GPT-6.1 Terra MEDIUM experiment 15819, status not run), which is not part of this batch and carries no usage. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The nineteen collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Hydrogen Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-14T07:46:28-05:00. Pricing source: pricing/2026-11-13T113820742994Z/api-pricing.json, as of 2026-11-13; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 14, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (18 models with single-tier estimates): $38.63; adding Qwen at its upper regional estimate ($2.36) gives an upper-bound batch total of $40.99. Recorded OpenRouter charges for the final editions: $5.11. Pricing snapshot age at report date: 1 day(s). Last successful daily source verification for this snapshot: 2026-11-14T08:04:09.706874+00:00. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-13T113820742994Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-14/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-14.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

