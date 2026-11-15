# Token Usage and Cost - 2026-11-15

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-1-terra | 2,270,340 | $0.26 | 104,751 | 9,685 | 2,155,904 | 0 | 05:47:52 | 30 |
| gemini-4-hydrogen | 2,348,989 | $0.69 | 189,852 | 33,142 | 2,125,995 | 0 | 07:15:32 | 26 |
| gpt-6-astra | 2,788,816 | $4.69 | 138,743 | 13,273 | 2,636,800 | 0 | 05:31:43 | 27 |
| fable-5-2 | 3,092,277 | $5.28 | 44 | 35,798 | 2,851,439 | 204,996 | 05:44:21 | 22 |
| sonnet-5-5 | 3,265,601 | $1.25 | 56 | 26,117 | 3,067,917 | 171,511 | 07:06:15 | 28 |
| deepseek-v4-pro | 3,384,996 | $0.42 | 429,565 | 34,983 | 2,920,448 | 0 | 05:59:18 | 42 |
| gpt-6-1-sol | 3,565,158 | $0.80 | 153,626 | 15,692 | 3,395,840 | 0 | 05:39:20 | 30 |
| kimi-k3-1-pro | 3,743,393 | $1.29 | 157,491 | 26,094 | 3,559,808 | 0 | 06:10:59 | 35 |
| glm-5-3 | 4,013,606 | $1.39 | 222,847 | 23,213 | 3,767,546 | 0 | 07:03:47 | 48 |
| gpt-6-luna | 4,661,306 | $0.07 | 163,037 | 27,229 | 4,471,040 | 0 | 05:52:35 | 42 |
| fable-5-1 | 5,336,358 | $10.40 | 706 | 46,726 | 4,947,876 | 341,050 | 05:31:43 | 23 |
| haiku-5-5 | 5,676,878 | $0.47 | 90 | 55,898 | 5,431,691 | 189,199 | 07:10:25 | 45 |
| gemini-4-argon | 5,770,415 | $1.83 | 319,118 | 65,443 | 5,385,854 | 0 | 06:44:34 | 42 |
| gemini-4-carbon | 6,118,582 | $2.27 | 544,577 | 62,866 | 5,511,139 | 0 | 07:09:44 | 31 |
| opus-5-5 | 6,414,899 | $3.66 | 90 | 38,035 | 6,168,008 | 208,766 | 05:51:16 | 45 |
| qwen-3-8-max-0902 | 7,393,212 | $2.57 | 222,100 | 57,640 | 7,113,472 | 0 | 07:19:35 | 54 |
| grok-4-7 | 7,495,617 | $6.13 | 286,293 | 87,148 | 7,122,176 | 0 | 06:25:14 | 54 |
| minimax-m3-1-flash | 8,689,198 | $0.19 | 218,356 | 50,362 | 8,420,480 | 0 | 06:16:45 | 65 |
| deepseek-v4-1-flash-1017 | 18,346,277 | $0.17 | 217,137 | 146,548 | 17,982,592 | 0 | 06:44:02 | 136 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.57 | 54/54 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.29 | 35/35 |
| fable-5-1 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| glm-5-3 | $1.39 | 48/48 |
| grok-4-7 | Not recorded | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.19 | 65/65 |
| deepseek-v4-1-flash-1017 | $0.17 | 136/136 |
| gemini-4-hydrogen | Not recorded | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| deepseek-v4-pro | $0.15 | 42/42 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,368,479 |
| Output | 855,892 |
| Cache Read | 99,036,025 |
| Cache Write | 1,115,522 |
| Calls with available telemetry | 825 |
| API estimate subtotal (available telemetry) | $43.86 |
| Recorded OpenRouter charges | $5.76 |
| Models with unavailable estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| qwen-3-8-max-0902 (earlier timed-out attempt, excluded) | 6,308,351 | $2.29 | 244,080 | 48,911 | 6,015,360 | 0 | 06:03:50 | 46 |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 19 final editions of the 2026-11-15 batch.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
The single earlier attempt (qwen-3-8-max-0902, session 86178ffd) timed out after 2402 s of scheduler time and is reported separately from the final successful run (session 337fdeef, 1732 s scheduler / 27m 13s worker); its usage is not added to final-edition totals. Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost and totals, as requested (its deployment tier is not determinable from usage this date: Singapore / International / Global). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
*pricing uses the collector-selected snapshot (pricing/2026-11-13T113820742994Z, as of 2026-11-13; the daily source check on 2026-11-15 08:03 UTC reported all 19 models unchanged, so the fallback snapshot was reused without substitution); all nineteen model identities resolved, including google/gemini-4-hydrogen (Standard $1.50 input / $7.50 output including thinking / $0.075 implicit cache read per million tokens; explicit caching unsupported). Verify official validity dates before later runs.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the nineteen final HTML editions, bound by terminal-record session ID, not latest-by-name. The one earlier attempt above is bound to the coordinator-recorded attempts array of its job, not selected by recency. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The nineteen collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Hydrogen Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-15T07:51:07-05:00. Pricing source: pricing/2026-11-13T113820742994Z/api-pricing.json, as of 2026-11-13; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 14, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (18 models with single-tier estimates): $43.86; adding Qwen at its upper regional estimate ($2.57) gives an upper-bound batch total of $46.43. Recorded OpenRouter charges for the final editions: $5.76. Pricing snapshot age at report date: 2 day(s). Last successful daily source verification for this snapshot: 2026-11-15T08:03:16.285169+00:00. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-13T113820742994Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-15/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-15.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

