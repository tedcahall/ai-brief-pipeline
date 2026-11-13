# Token Usage and Cost - 2026-11-13

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gemini-4-hydrogen | 1,892,913 | $0.62 | 184,771 | 28,419 | 1,679,723 | 0 | 07:53:03 | 20 |
| gpt-6-astra | 2,286,028 | $4.07 | 126,353 | 13,115 | 2,146,560 | 0 | 05:31:28 | 25 |
| gpt-6-1-terra | 2,437,060 | $0.29 | 134,004 | 9,168 | 2,293,888 | 0 | 05:45:05 | 33 |
| gpt-6-1-sol | 2,501,705 | $0.65 | 144,540 | 12,845 | 2,344,320 | 0 | 05:38:47 | 24 |
| glm-5-3 | 3,056,908 | $0.99 | 95,586 | 20,138 | 2,941,184 | 0 | 07:26:17 | 50 |
| sonnet-5-5 | 3,568,488 | $1.19 | 58 | 27,389 | 3,398,019 | 143,022 | 07:40:11 | 29 |
| gpt-6-luna | 3,652,258 | $0.06 | 137,731 | 20,639 | 3,493,888 | 0 | 05:51:21 | 41 |
| fable-5-2 | 4,061,748 | $5.49 | 58 | 34,246 | 3,817,514 | 209,930 | 05:45:29 | 29 |
| opus-5-5 | 4,547,957 | $3.10 | 66 | 31,963 | 4,316,411 | 199,517 | 05:52:08 | 33 |
| kimi-k3-1-pro | 4,898,712 | $1.52 | 143,358 | 28,378 | 4,726,976 | 0 | 06:23:55 | 39 |
| gemini-4-argon | 4,960,182 | $1.53 | 286,107 | 49,377 | 4,624,698 | 0 | 07:02:59 | 40 |
| haiku-5-5 | 5,087,096 | $0.45 | 76 | 56,000 | 4,823,295 | 207,725 | 07:02:58 | 38 |
| minimax-m3-1-flash | 5,400,226 | $0.12 | 199,586 | 28,416 | 5,172,224 | 0 | 06:29:04 | 44 |
| deepseek-v4-pro | 5,724,572 | $0.43 | 173,465 | 98,819 | 5,452,288 | 0 | 05:57:56 | 61 |
| qwen-3-8-max-0902 | 6,266,327 | $2.24 | 202,790 | 55,089 | 6,008,448 | 0 | 05:59:30 | 58 |
| fable-5-1 | 6,546,164 | $11.47 | 866 | 67,315 | 6,149,896 | 328,087 | 05:31:27 | 28 |
| grok-4-7 | 6,573,167 | $5.62 | 224,030 | 89,553 | 6,259,584 | 0 | 06:34:01 | 51 |
| gemini-4-carbon | 10,001,340 | $2.53 | 430,597 | 71,965 | 9,498,778 | 0 | 07:32:48 | 44 |
| deepseek-v4-1-flash-1017 | 11,766,080 | $0.15 | 293,265 | 122,543 | 11,350,272 | 0 | 07:08:21 | 92 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| fable-5-2 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.24 | 58/58 |
| gemini-4-argon | Not recorded | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| glm-5-3 | $0.49 | 50/50 |
| gemini-4-hydrogen | Not recorded | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| deepseek-v4-1-flash-1017 | $0.13 | 92/92 |
| deepseek-v4-pro | $1.33 | 61/61 |
| gemini-4-carbon | Not recorded | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.12 | 44/44 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| kimi-k3-1-pro | $1.52 | 39/39 |
| gpt-6-1-terra | No per-token charge | Not applicable |
| gpt-6-luna | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 2,777,307 |
| Output | 865,377 |
| Cache Read | 90,497,966 |
| Cache Write | 1,088,281 |
| Calls with available telemetry | 779 |
| API estimate subtotal (available telemetry) | $42.52 |
| Recorded OpenRouter charges | $5.83 |
| Models with unavailable telemetry/estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| DeepSeek v4.1 Flash | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | 06:34:27 | Unavailable |
| Sonnet 5.5 subscription | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | 06:55:24 | Unavailable |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 19 final editions of the 2026-11-13 batch.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
*pricing uses the collector-selected snapshot (pricing/2026-11-13T113820742994Z, as of 2026-11-13, no fallback used); all nineteen model identities resolved, including google/gemini-4-hydrogen (Standard $1.50 input / $7.50 output including thinking / $0.075 implicit cache read per million tokens; explicit caching unsupported). Verify official validity dates before later runs.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the nineteen final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
Two earlier attempts exist for this date, both interrupted by the 12:02 UTC gateway restart before any session started (DeepSeek v4.1 Flash 11:34 ET, Sonnet 5.5 11:55 ET); they carry no session, no usage and no charge, and appear only in the earlier-attempts table. The nineteen collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Hydrogen Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-13T08:01:39-05:00. Pricing source: pricing/2026-11-13T113820742994Z/api-pricing.json, as of 2026-11-13; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 14, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent total (19/19 models): $42.52. Recorded OpenRouter charges for the final editions: $5.83. Pricing snapshot age at report date: 0 days. Last successful daily source verification for this snapshot: not yet recorded. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- DeepSeek v4.1 Flash (2026-11-13T06:34:27-05:00): run has no session (failed before start)
- Sonnet 5.5 subscription (2026-11-13T06:55:24-05:00): run has no session (failed before start)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-13T113820742994Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-13/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-13.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

