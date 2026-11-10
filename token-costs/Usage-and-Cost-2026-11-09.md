# Token Usage and Cost - 2026-11-09

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| Astra | 2,247,132 | $4.05 | 138,601 | 11,379 | 2,097,152 | 0 | 05:31:22 | 24 |
| Terra | 2,254,288 | $0.25 | 96,652 | 8,516 | 2,149,120 | 0 | 05:45:00 | 32 |
| Sol | 2,467,448 | $0.61 | 125,325 | 12,907 | 2,329,216 | 0 | 05:38:26 | 26 |
| Sonnet | 2,928,719 | $1.08 | 56 | 20,920 | 2,759,330 | 148,413 | 06:33:24 | 28 |
| Kimi | 3,732,497 | $1.43 | 269,413 | 20,204 | 3,442,880 | 0 | 06:07:07 | 35 |
| Argon | 4,842,496 | $1.68 | 317,409 | 60,224 | 4,464,863 | 0 | 06:42:24 | 34 |
| Opus | 5,102,116 | $3.04 | 84 | 30,785 | 4,890,094 | 181,153 | 05:38:59 | 42 |
| Haiku | 5,468,926 | $0.46 | 84 | 59,810 | 5,212,721 | 196,311 | 06:38:09 | 42 |
| Grok | 5,764,827 | $3.65 | 275,925 | 65,030 | 5,423,872 | 0 | 06:18:02 | 48 |
| Fable | 6,009,720 | $8.95 | 68 | 43,146 | 5,697,893 | 268,613 | 05:31:21 | 34 |
| DeepSeek Pro | 6,284,628 | $0.41 | 188,185 | 76,091 | 6,020,352 | 0 | 05:44:49 | 59 |
| Qwen | 6,605,970 | $2.38 | 214,550 | 61,052 | 6,330,368 | 0 | 05:52:21 | 53 |
| GLM | 6,892,169 | $2.27 | 310,390 | 29,139 | 6,552,640 | 0 | 07:00:37 | 61 |
| MiniMax | 7,618,838 | $0.18 | 325,254 | 40,208 | 7,253,376 | 0 | 06:10:40 | 64 |
| Luna | 9,466,214 | $0.14 | 210,394 | 59,276 | 9,196,544 | 0 | 06:44:40 | 65 |
| Flash | 17,787,312 | $0.17 | 229,010 | 134,686 | 17,423,616 | 0 | 06:21:39 | 125 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| MiniMax | $0.18 | 64/64 |
| Qwen | $2.38 | 53/53 |
| Grok | Not recorded | Not applicable |
| Terra | No per-token charge | Not applicable |
| DeepSeek Pro | $1.36 | 59/59 |
| Kimi | $1.43 | 35/35 |
| Sonnet | No per-token charge | Not applicable |
| Argon | Not recorded | Not applicable |
| Opus | No per-token charge | Not applicable |
| Sol | No per-token charge | Not applicable |
| Flash | $0.11 | 125/125 |
| Astra | No per-token charge | Not applicable |
| Haiku | No per-token charge | Not applicable |
| Fable | No per-token charge | Not applicable |
| Luna | No per-token charge | Not applicable |
| GLM | $1.02 | 60/61 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 2,701,400 |
| Output | 733,373 |
| Cache Read | 91,244,037 |
| Cache Write | 794,490 |
| Calls with available telemetry | 772 |
| API estimate subtotal (available telemetry) | $30.76 |
| Recorded OpenRouter charges | $6.48 |
| Models with unavailable telemetry/estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| GPT-6 Luna | 468,068 | $0.01 | 60,647 | 4,221 | 403,200 | 0 | 05:49:16 | 12 |

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 16 final editions.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested. This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the sixteen final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
One earlier Luna run for the same job (05:49 ET, session 854cc0c8) precedes the coordinator-selected 06:44 ET attempt (session 6261bb49-bd11-400c-9f13-d1dbc81f0517); only the selected attempt is counted in primary totals. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. The four added models use the additive verified pricing snapshot; prior model rates are unchanged. Argon uses introductory rates; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-09T07:17:11-05:00. Pricing source: pricing/2026-11-09T093833725338Z/api-pricing.json, as of 2026-11-09; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 12, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent total (16/16 models): $30.76. Recorded OpenRouter charges for the final editions: $6.48. Pricing snapshot age at report date: 0 days. Last successful daily source verification for this snapshot: not yet recorded. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-09T093833725338Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- MiniMax: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- Qwen: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- Grok: [grok-4.7](https://docs.x.ai/developers/pricing)
- Terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- DeepSeek Pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- Kimi: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- Sonnet: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- Argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- Opus: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- Sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- Flash: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- Astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- Haiku: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- Fable: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- Luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- GLM: [glm-5.3](https://docs.z.ai/guides/overview/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-09/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `json/Usage-and-Cost-2026-11-09.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

