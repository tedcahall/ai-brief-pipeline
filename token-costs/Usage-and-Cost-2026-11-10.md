# Token Usage and Cost - 2026-11-10

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-1-terra | 1,547,482 | $0.18 | 66,675 | 8,807 | 1,472,000 | 0 | 05:47:26 | 29 |
| gpt-6-astra | 2,627,321 | $4.48 | 133,454 | 13,355 | 2,480,512 | 0 | 05:31:06 | 26 |
| kimi-k3-1-pro | 3,020,238 | $1.00 | 112,406 | 19,576 | 2,888,256 | 0 | 06:06:22 | 33 |
| sonnet-5-5 | 3,079,107 | $1.17 | 54 | 23,381 | 2,893,382 | 162,290 | 06:30:22 | 27 |
| glm-5-3 | 3,544,536 | $1.16 | 122,458 | 22,654 | 3,399,424 | 0 | 07:09:46 | 50 |
| gpt-6-1-sol | 3,794,637 | $0.84 | 155,874 | 16,747 | 3,622,016 | 0 | 05:38:49 | 31 |
| haiku-5-5 | 4,283,638 | $0.31 | 84 | 46,307 | 4,087,830 | 149,417 | 06:34:12 | 42 |
| grok-4-7 | 4,365,052 | $2.98 | 307,367 | 61,781 | 3,995,904 | 0 | 06:15:34 | 37 |
| opus-5-5 | 4,377,214 | $2.85 | 70 | 28,440 | 4,167,847 | 180,857 | 05:42:44 | 35 |
| qwen-3-8-max-0902 | 5,109,276 | $1.86 | 169,685 | 49,863 | 4,889,728 | 0 | 06:14:49 | 54 |
| fable-5-1 | 5,510,588 | $8.73 | 962 | 50,440 | 5,214,619 | 244,567 | 05:31:06 | 31 |
| gemini-4-argon | 5,531,056 | $1.70 | 311,962 | 55,687 | 5,163,407 | 0 | 06:53:26 | 41 |
| fable-5-2 | 6,168,928 | $6.70 | 68 | 36,979 | 5,878,967 | 252,914 | 08:14:27 | 34 |
| deepseek-v4-pro | 7,256,919 | $0.44 | 316,929 | 41,814 | 6,898,176 | 0 | 05:47:56 | 78 |
| deepseek-v4-1-flash-1017 | 7,505,147 | $0.09 | 148,000 | 70,747 | 7,286,400 | 0 | 06:39:18 | 79 |
| minimax-m3-1-flash | 10,184,403 | $0.20 | 164,913 | 43,170 | 9,976,320 | 0 | 06:09:51 | 75 |
| gpt-6-luna | 12,494,269 | $0.18 | 262,238 | 54,623 | 12,177,408 | 0 | 05:52:05 | 79 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| qwen-3-8-max-0902 | $1.86 | 54/54 |
| gpt-6-1-sol | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.20 | 75/75 |
| fable-5-1 | No per-token charge | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| deepseek-v4-1-flash-1017 | $0.06 | 79/79 |
| kimi-k3-1-pro | $1.00 | 33/33 |
| sonnet-5-5 | No per-token charge | Not applicable |
| fable-5-2 | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| glm-5-3 | $0.59 | 50/50 |
| gpt-6-luna | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| deepseek-v4-pro | $1.37 | 78/78 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 2,273,199 |
| Output | 644,371 |
| Cache Read | 86,492,196 |
| Cache Write | 990,045 |
| Calls with available telemetry | 781 |
| API estimate subtotal (available telemetry) | $34.87 |
| Recorded OpenRouter charges | $5.07 |
| Models with unavailable telemetry/estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 17 final editions, including the fable-5-2 edition added in the 2026-11-10 expanded-cohort revision.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested. This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
*claude-fable-5-2 rates ($8 input / $40 output / $0.20 cache read / $10 5m write / $16 1h write per MTok) were re-verified live against the Anthropic pricing page during this finalizer run and added as an additive pricing snapshot (pricing/2026-11-10T132547960000Z); all prior rates unchanged.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the seventeen final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
No earlier or diagnostic attempts exist for this date: all seventeen collected runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. The four added models use the additive verified pricing snapshot; prior model rates are unchanged. Argon uses introductory rates; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-10T08:27:10-05:00. Pricing source: pricing/2026-11-10T132547960000Z/api-pricing.json, as of 2026-11-10; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 12, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent total (17/17 models): $34.87. Recorded OpenRouter charges for the final editions: $5.07. Pricing snapshot age at report date: 0 days. Last successful daily source verification for this snapshot: not yet recorded. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- GPT-6 Luna (2026-11-10T05:52:05-05:00): per-call sum differs from cron run usage

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-10T132547960000Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-10/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-10.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

