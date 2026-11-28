# Token Usage and Cost - 2026-11-28

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 828,765 | $1.89 | 178,656 | 4,989 | 645,120 | 0 | 06:49:12 | 18 |
| gpt-6-astra | 1,404,981 | $2.69 | 101,654 | 7,583 | 1,295,744 | 0 | 05:31:34 | 19 |
| gemini-4-neon | 1,650,500 | $1.37 | 179,496 | 41,160 | 1,429,844 | 0 | 07:00:10 | 20 |
| gemini-4-hydrogen | 2,601,986 | $0.71 | 175,796 | 35,177 | 2,391,013 | 0 | 07:37:43 | 27 |
| gpt-6-1-sol | 2,620,989 | $0.65 | 130,309 | 14,520 | 2,476,160 | 0 | 05:36:26 | 26 |
| gpt-6-1-terra | 3,090,657 | $0.32 | 113,247 | 10,754 | 2,966,656 | 0 | 05:42:42 | 36 |
| gpt-6-2-sol | 3,597,921 | $1.17 | 348,405 | 15,340 | 3,234,176 | 0 | 06:52:40 | 40 |
| kimi-k3-1-pro | 3,719,546 | $1.27 | 141,284 | 27,347 | 3,550,915 | 0 | 06:17:33 | 37 |
| glm-5-3 | 4,469,055 | $1.39 | 123,984 | 20,719 | 4,324,352 | 0 | 06:13:31 | 58 |
| sonnet-5-5 | 4,542,781 | $1.40 | 76 | 29,281 | 4,345,399 | 168,025 | 07:26:06 | 38 |
| gpt-6-luna | 4,629,316 | $0.09 | 398,685 | 25,959 | 4,204,672 | 0 | 05:48:31 | 44 |
| deepseek-v4-pro | 4,672,479 | $0.30 | 145,593 | 54,566 | 4,472,320 | 0 | 06:02:48 | 55 |
| fable-5-2 | 5,508,730 | $6.41 | 66 | 36,672 | 5,228,471 | 243,521 | 05:46:30 | 33 |
| minimax-m3-1-flash | 5,642,744 | $0.13 | 195,471 | 38,377 | 5,408,896 | 0 | 06:24:35 | 48 |
| gemini-4-argon | 5,777,331 | $1.80 (upper estimate) | 321,481 | 61,853 | 5,393,997 | 0 | 05:58:41 | 41 |
| deepseek-v4-1-flash-1017 | 5,843,045 | $0.06 | 196,791 | 29,614 | 5,616,640 | 0 | 06:45:19 | 71 |
| haiku-5-5 | 5,918,486 | $0.47 | 94 | 60,897 | 5,667,686 | 189,809 | 07:31:27 | 47 |
| grok-4-7 | 5,974,198 | $3.69 | 195,680 | 75,222 | 5,703,296 | 0 | 06:29:13 | 52 |
| fable-5-1 | 6,107,485 | $10.02 | 898 | 58,625 | 5,766,007 | 281,955 | 05:31:33 | 29 |
| qwen-3-8-max-0902 | 6,684,225 | $2.34 | 197,445 | 56,188 | 6,430,592 | 0 | 07:41:43 | 60 |
| qwen-4-max | 7,030,902 | $1.01 | 206,215 | 55,791 | 6,768,896 | 0 | 06:37:28 | 52 |
| gemini-4-carbon | 7,868,253 | $2.33 (upper estimate) | 435,872 | 71,861 | 7,360,520 | 0 | 06:19:16 | 31 |
| opus-5-5 | 9,850,516 | $4.54 | 114 | 41,272 | 9,584,276 | 224,854 | 05:53:20 | 57 |

No failed or retried attempts exist this date; every one of the 23 coordinator runs produced a terminal HTML edition and each collected run binds one-to-one to its terminal-record session.

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| glm-5-3 | $0.63 | 58/58 |
| kimi-k3-1-pro | $1.58 | 37/37 |
| fable-5-1 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.13 | 48/48 |
| deepseek-v4-1-flash-1017 | $0.07 | 71/71 |
| gemini-4-argon | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| qwen-3-8-max-0902 | $2.34 | 60/60 |
| qwen-4-max | $1.01 | 52/52 |
| sonnet-5-5 | No per-token charge | Not applicable |
| deepseek-v4-pro | $0.14 | 55/55 |
| gemini-4-hydrogen | Not recorded | Not applicable |
| gemini-4-neon | Not recorded | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,787,312 |
| Output | 873,767 |
| Cache Read | 104,265,648 |
| Cache Write | 1,108,164 |
| Calls with available telemetry | 939 |
| API estimate subtotal (available telemetry) | $41.94 |
| Recorded OpenRouter charges | $5.91 |
| Models with unavailable estimates | gemini-4-argon, gemini-4-carbon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (fable-5-1, fable-5-2, opus-5-5, sonnet-5-5, haiku-5-5) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-28 cohort; every cohort model produced a terminal edition this date (full batch).
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the collector-selected snapshot pricing/2026-11-28T080209145863Z/api-pricing.json (canonical key qwen4-max) per million tokens. Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol), with Standard short tiers at or below 272,000 prompt tokens per request and Standard long above; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected snapshot (pricing/2026-11-28T080209145863Z/api-pricing.json, as of 2026-11-28); pricing verification passed (17 files checked) and the collector records pricing_fallback_used=False (latest fully verified card rather than a fresh same-day capture). Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the 23 final HTML editions, bound by terminal-record session ID, not latest-by-name. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The 23 collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-28T08:14:22-05:00. Pricing source: pricing/2026-11-28T080209145863Z/api-pricing.json, as of 2026-11-28; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $41.94; upper-bound additions from tier-indeterminate models (Gemini 4 Argon, Gemini 4 Carbon and Qwen regional estimates) bring the batch upper bound to $49.42. Recorded OpenRouter charges for the final editions: $5.91. Pricing snapshot age at report date: 0 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-28T05:58:41-05:00): tier not determinable from usage (Introductory Standard)
- Gemini 4 Carbon (2026-11-28T06:19:16-05:00): tier not determinable from usage (Introductory Standard)
- Qwen 3.8 Max 0902 (2026-11-28T07:41:43-05:00): tier not determinable from usage (Singapore / International / Global)
- Qwen4 Max (2026-11-28T06:37:28-05:00): tier not determinable from usage (OpenRouter / Alibaba)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-28T080209145863Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-28/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-28.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

