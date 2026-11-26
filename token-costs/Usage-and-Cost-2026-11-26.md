# Token Usage and Cost - 2026-11-26

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 926,707 | $1.83 | 165,899 | 5,096 | 755,712 | 0 | 07:24:18 | 21 |
| gpt-6-astra | 1,545,215 | $2.81 | 103,300 | 6,907 | 1,435,008 | 0 | 05:31:29 | 20 |
| gemini-4-neon | 2,056,882 | $2.03 | 403,006 | 38,713 | 1,615,163 | 0 | 07:35:27 | 22 |
| gemini-4-hydrogen | 2,148,058 | $0.65 | 164,467 | 34,313 | 1,949,278 | 0 | 06:53:51 | 22 |
| gpt-6-1-sol | 2,398,757 | $0.62 | 127,724 | 13,881 | 2,257,152 | 0 | 05:36:18 | 24 |
| gpt-6-2-sol | 2,530,071 | $0.93 | 280,249 | 15,070 | 2,234,752 | 0 | 07:28:22 | 29 |
| gpt-6-1-terra | 2,578,761 | $0.27 | 100,043 | 10,110 | 2,468,608 | 0 | 05:42:35 | 34 |
| glm-5-3 | 3,495,404 | $1.16 | 116,170 | 28,026 | 3,351,208 | 0 | 06:24:15 | 46 |
| deepseek-v4-pro | 4,002,904 | $0.30 | 147,360 | 60,344 | 3,795,200 | 0 | 05:55:32 | 48 |
| sonnet-5-5 | 4,042,810 | $1.29 | 70 | 26,252 | 3,855,614 | 160,874 | 06:42:51 | 35 |
| haiku-5-5 | 4,162,195 | $0.35 | 70 | 49,094 | 3,943,544 | 169,487 | 06:48:36 | 35 |
| kimi-k3-1-pro | 4,234,641 | $1.55 | 258,444 | 24,703 | 3,951,494 | 0 | 06:11:30 | 36 |
| fable-5-2 | 4,391,254 | $5.59 | 60 | 36,023 | 4,147,851 | 207,320 | 05:43:41 | 30 |
| fable-5-1 | 4,887,662 | $8.51 | 898 | 43,684 | 4,584,650 | 258,430 | 05:31:29 | 29 |
| opus-5-5 | 5,194,344 | $2.92 | 78 | 29,562 | 4,998,494 | 166,210 | 05:50:16 | 39 |
| grok-4-7 | 5,859,079 | $3.65 | 215,218 | 72,277 | 5,571,584 | 0 | 06:26:22 | 47 |
| minimax-m3-1-flash | 5,957,520 | $0.14 | 153,720 | 50,840 | 5,752,960 | 0 | 06:19:26 | 51 |
| gemini-4-carbon | 6,256,493 | $2.26 | 547,299 | 60,022 | 5,649,172 | 0 | 06:30:41 | 31 |
| qwen-3-8-max-0902 | 6,328,306 | $2.19 | 193,049 | 46,809 | 6,088,448 | 0 | 06:58:25 | 55 |
| gpt-6-luna | 6,385,213 | $0.10 | 212,131 | 39,194 | 6,133,888 | 0 | 05:47:53 | 48 |
| gemini-4-argon | 6,875,654 | $2.27 (upper estimate) | 473,526 | 69,212 | 6,332,916 | 0 | 06:02:23 | 48 |
| qwen-4-max | 10,661,282 | $1.31 | 253,254 | 50,012 | 10,358,016 | 0 | 07:11:14 | 64 |

## Failed-attempt usage (no edition produced)

| Model | Coordinator run ID | Total tokens | API Cost* | Status |
|---|---|---|---|---|
| deepseek-v4-1-flash-1017 (failed attempt, no edition) | cron-request.d1566f27-d0a9-4d8c-8c4e-1836d03c3be8 | 43,945 | $0.00 | error |
| deepseek-v4-1-flash-1017 (failed attempt, no edition) | cron-request.fe61671d-22e0-4e0d-ab4d-898d1e9b3655 | 74,595 | $0.01 | error |

These two rows are the coordinator-recorded failed attempts of deepseek-v4-1-flash-1017 (DeepSeek provider invalid_request_error). Their available telemetry is reported separately and is not included in final-edition totals or the consensus.

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-neon | Not recorded | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.19 | 55/55 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.64 | 36/36 |
| qwen-4-max | $1.31 | 64/64 |
| fable-5-2 | No per-token charge | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.14 | 51/51 |
| sonnet-5-5 | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| deepseek-v4-pro | $0.75 | 48/48 |
| grok-4-7 | Not recorded | Not applicable |
| glm-5-3 | $1.16 | 46/46 |
| gpt-6-luna | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,916,035 |
| Output | 810,144 |
| Cache Read | 91,230,712 |
| Cache Write | 962,321 |
| Calls with available telemetry | 814 |
| API estimate subtotal (available telemetry) | $40.48 |
| Recorded OpenRouter charges | $7.19 |
| Models with unavailable estimates | gemini-4-argon |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover the 22 final editions of the 2026-11-26 cohort; deepseek-v4-1-flash-1017 produced no edition (two failed attempts reported separately above), so this is a partial batch and totals are not comparable to full 23-model days.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Every collected final run binds one-to-one to a coordinator-selected final edition session this date; the only additional rows are the two coordinator-recorded failed attempts, bound by attempt session key and listed separately.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the collector-selected snapshot pricing/2026-11-23T020315256499Z/api-pricing.json (canonical key qwen4-max) per million tokens. Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol), with Standard short tiers at or below 272,000 prompt tokens per request and Standard long above; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected snapshot (pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23); pricing verification passed (17 files checked) and the collector records pricing_fallback_used=True (latest fully verified card rather than a fresh same-day capture). Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the 22 final HTML editions, bound by terminal-record session ID, not latest-by-name. The 23rd cohort model (deepseek-v4-1-flash-1017) failed twice before synthesis; its two attempts are bound by coordinator attempt records and shown in the failed-attempt table only. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The 22 collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-26T07:52:39-05:00. Pricing source: pricing/2026-11-23T020315256499Z/api-pricing.json, as of 2026-11-23; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $40.48; upper-bound additions from tier-indeterminate models (Gemini 4 Argon and Qwen regional estimates) bring the batch upper bound to $46.26. Recorded OpenRouter charges for the final editions: $7.19. Pricing snapshot age at report date: 3 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-26T06:02:23-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-23T020315256499Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-26/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-26.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

