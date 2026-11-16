# Token Usage and Cost - 2026-11-16

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-astra | 2,054,103 | $4.13 | 169,338 | 11,357 | 1,873,408 | 0 | 05:55:33 | 22 |
| gemini-4-hydrogen | 2,058,387 | $0.60 | 174,464 | 25,943 | 1,857,980 | 0 | 07:34:45 | 26 |
| gpt-6-1-sol | 2,605,843 | $0.67 | 142,199 | 13,724 | 2,449,920 | 0 | 06:02:39 | 25 |
| gpt-6-1-terra | 2,687,912 | $0.28 | 98,205 | 10,123 | 2,579,584 | 0 | 06:09:36 | 36 |
| qwen-4-max | 4,284,652 | $0.82 | 219,039 | 42,061 | 4,023,552 | 0 | 07:25:23 | 36 |
| glm-5-3 | 4,420,657 | $1.69 | 401,708 | 20,613 | 3,998,336 | 0 | 06:58:52 | 50 |
| kimi-k3-1-pro | 4,909,235 | $1.45 | 131,742 | 23,957 | 4,753,536 | 0 | 06:42:06 | 43 |
| fable-5-2 | 5,234,321 | $6.32 | 62 | 36,203 | 4,955,612 | 242,444 | 06:07:40 | 31 |
| grok-4-7 | 5,329,704 | $4.64 | 273,951 | 73,737 | 4,982,016 | 0 | 06:51:03 | 37 |
| qwen-3-8-max-0902 | 5,876,719 | $2.10 | 202,826 | 47,141 | 5,626,752 | 0 | 06:18:08 | 50 |
| sonnet-5-5 | 6,282,798 | $1.79 | 84 | 32,708 | 6,034,858 | 215,148 | 07:24:21 | 42 |
| haiku-5-5 | 6,287,190 | $0.48 | 102 | 59,436 | 6,034,760 | 192,892 | 07:28:56 | 51 |
| deepseek-v4-pro | 6,637,482 | $0.43 | 184,768 | 83,690 | 6,369,024 | 0 | 06:20:20 | 64 |
| fable-5-1 | 6,837,750 | $10.35 | 994 | 49,246 | 6,474,676 | 312,834 | 05:55:23 | 32 |
| gpt-6-luna | 7,049,941 | $0.12 | 305,534 | 54,359 | 6,690,048 | 0 | 07:38:49 | 69 |
| gemini-4-argon | 7,120,431 | $1.80 | 346,400 | 43,518 | 6,730,513 | 0 | 06:39:52 | 49 |
| gemini-4-carbon | 7,355,332 | $2.05 | 333,950 | 68,619 | 6,952,763 | 0 | 07:06:16 | 37 |
| opus-5-5 | 7,643,337 | $3.59 | 100 | 34,416 | 7,432,087 | 176,734 | 06:13:58 | 50 |
| minimax-m3-1-flash | 8,069,658 | $0.19 | 387,810 | 27,576 | 7,654,272 | 0 | 06:47:20 | 55 |
| deepseek-v4-1-flash-1017 | 10,853,809 | $0.11 | 165,602 | 89,679 | 10,598,528 | 0 | 07:06:58 | 106 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-hydrogen | Not recorded | Not applicable |
| glm-5-3 | $0.78 | 50/50 |
| sonnet-5-5 | No per-token charge | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.10 | 105/106 |
| deepseek-v4-pro | $1.42 | 64/64 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.10 | 50/50 |
| gpt-6-1-terra | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.45 | 43/43 |
| minimax-m3-1-flash | $0.19 | 55/55 |
| qwen-4-max | $0.82 | 36/36 |
| gemini-4-carbon | Not recorded | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,538,878 |
| Output | 848,106 |
| Cache Read | 108,072,225 |
| Cache Write | 1,140,052 |
| Calls with available telemetry | 911 |
| API estimate subtotal (available telemetry) | $43.60 |
| Recorded OpenRouter charges | $6.86 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-luna (earlier failed attempt, excluded) | 730,405 | $0.02 | 78,856 | 7,837 | 643,712 | 0 | 06:14:17 | 15 |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 20 final editions of the 2026-11-16 cohort, including first cohort appearance of qwen-4-max.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
One earlier coordinator-recorded attempt is reported separately: gpt-6-luna failed pre-dispatch (no HTML produced, 178 s scheduler time, session 902f4ebd); its usage is not added to final-edition totals. One additional qwen-4-max collector row (session 798584e1, 04:47 ET) predates the coordinator batch launch (10:49 UTC) and is not bound to any coordinator-recorded attempt, so it is excluded from all tables rather than guessed by time; it is disclosed here only as an unbound diagnostic attempt.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-16T105548994629Z (key qwen4-max, SHA-256 fff059c7c51033444372b8f8b87100ab0c10d32e2fe6d7ad58c35965f1d9b846): $1.50 input / $4.50 output / $0.075 cache read / $1.875 cache write per million tokens; cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-16T105548994629Z/api-pricing.json, as of 2026-11-16); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty final HTML editions, bound by terminal-record session ID, not latest-by-name. The earlier failed attempt above is bound to the coordinator-recorded attempts array of its job. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Hydrogen Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-16T08:02:10-05:00. Pricing source: pricing/2026-11-16T105548994629Z/api-pricing.json, as of 2026-11-16; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 15, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $43.60; upper-bound additions from tier-indeterminate models (Qwen regional upper estimate) bring the batch upper bound to $46.52. Recorded OpenRouter charges for the final editions: $6.86. Pricing snapshot age at report date: 0 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- GPT-6 Luna (2026-11-16T07:38:49-05:00): per-call sum differs from cron run usage
- Qwen4 Max (2026-11-16T04:47:44-05:00): tier not determinable from usage (OpenRouter / Alibaba)
- Qwen4 Max (2026-11-16T07:25:23-05:00): tier not determinable from usage (OpenRouter / Alibaba)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-16T105548994629Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-16/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-16.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

