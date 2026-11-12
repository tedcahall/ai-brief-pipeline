# Token Usage and Cost - 2026-11-12

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-1-sol | 1,813,370 | $0.54 | 119,663 | 12,811 | 1,680,896 | 0 | 05:40:03 | 21 |
| gpt-6-1-terra | 2,138,949 | $0.24 | 88,079 | 9,270 | 2,041,600 | 0 | 05:46:25 | 32 |
| glm-5-3 | 2,878,597 | $0.97 | 104,955 | 25,226 | 2,748,416 | 0 | 07:30:25 | 47 |
| sonnet-5-5 | 3,086,354 | $1.19 | 56 | 25,958 | 2,899,162 | 161,178 | 06:53:44 | 28 |
| gpt-6-astra | 3,261,596 | $5.46 | 154,612 | 16,424 | 3,090,560 | 0 | 05:31:17 | 29 |
| kimi-k3-1-pro | 4,624,918 | $1.52 | 150,758 | 33,392 | 4,440,768 | 0 | 06:25:29 | 36 |
| deepseek-v4-pro | 4,640,427 | $0.64 | 585,036 | 85,087 | 3,970,304 | 0 | 05:53:47 | 46 |
| fable-5-1 | 5,049,101 | $8.20 | 1,026 | 42,919 | 4,762,337 | 242,819 | 05:31:17 | 33 |
| gpt-6-luna | 5,100,371 | $0.08 | 178,408 | 27,627 | 4,894,336 | 0 | 05:51:02 | 45 |
| fable-5-2 | 5,183,537 | $6.31 | 62 | 37,026 | 4,906,165 | 240,284 | 05:41:09 | 31 |
| opus-5-5 | 5,221,399 | $3.24 | 76 | 32,775 | 4,990,143 | 198,405 | 05:48:04 | 38 |
| gemini-4-argon | 5,490,428 | $1.53 | 315,040 | 38,871 | 5,136,517 | 0 | 07:13:19 | 41 |
| gemini-4-carbon | 5,959,323 | $2.40 | 591,631 | 68,702 | 5,298,990 | 0 | 07:37:51 | 36 |
| haiku-5-5 | 6,008,975 | $0.54 | 80 | 61,776 | 5,725,948 | 221,171 | 06:57:46 | 40 |
| grok-4-7 | 6,012,138 | $3.81 | 292,276 | 66,358 | 5,653,504 | 0 | 06:37:54 | 50 |
| qwen-3-8-max-0902 | 7,519,156 | $2.61 | 200,398 | 65,126 | 7,253,632 | 0 | 07:03:31 | 57 |
| minimax-m3-1-flash | 8,359,741 | $0.17 | 210,825 | 34,484 | 8,114,432 | 0 | 06:30:49 | 66 |
| deepseek-v4-1-flash-1017 | 8,644,964 | $0.12 | 241,721 | 93,611 | 8,309,632 | 0 | 06:43:58 | 89 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| deepseek-v4-pro | $1.05 | 46/46 |
| kimi-k3-1-pro | $1.52 | 36/36 |
| gemini-4-argon | Not recorded | Not applicable |
| glm-5-3 | $0.49 | 47/47 |
| grok-4-7 | Not recorded | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.08 | 89/89 |
| fable-5-2 | No per-token charge | Not applicable |
| gemini-4-carbon | Not recorded | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| qwen-3-8-max-0902 | $2.61 | 57/57 |
| gpt-6-astra | No per-token charge | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.17 | 66/66 |
| gpt-6-luna | No per-token charge | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,234,702 |
| Output | 777,443 |
| Cache Read | 85,917,342 |
| Cache Write | 1,063,857 |
| Calls with available telemetry | 765 |
| API estimate subtotal (available telemetry) | $39.58 |
| Recorded OpenRouter charges | $5.91 |
| Models with unavailable telemetry/estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| Qwen 3.8 Max 0902 | 6,902,273 | $2.44 | 209,118 | 61,091 | 6,632,064 | 0 | 06:01:38 | 60 |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 18 final editions of the 2026-11-12 batch.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
*pricing uses the collector-selected snapshot (pricing/2026-11-11T120252913396Z, as of 2026-11-11) with the collector recording earlier-date fallback; the 2026-11-12 daily source verification reported all 18 models / 11 sources unchanged at 2026-11-12T08:06:48Z, so no fresher snapshot exists; all eighteen model identities resolved, including anthropic/claude-fable-5-2 and google/gemini-4-carbon.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the eighteen final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
No earlier or diagnostic attempts exist for this date: all eighteen collected runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon and Carbon use introductory rates; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-12T08:05:18-05:00. Pricing source: pricing/2026-11-11T120252913396Z/api-pricing.json, as of 2026-11-11; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 13, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent total (18/18 models): $39.58. Recorded OpenRouter charges for the final editions: $5.91. Pricing snapshot age at report date: 1 days. Last successful daily source verification for this snapshot: 2026-11-12T08:06:48.459090+00:00. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-11T120252913396Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-12/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-12.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

