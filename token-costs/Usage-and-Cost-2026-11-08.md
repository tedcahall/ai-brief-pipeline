# Token Usage and Cost - 2026-11-08

## Final-edition token usage

| Model | Start ET | Calls | Uncached input | Output | Cache read | Cache write | API estimate* |
|---|---|---|---|---|---|---|---|
| Opus | 07:40:34 | 48 | 96 | 36,634 | 6,588,963 | 203,153 | USD 3.68 |
| Sonnet | 16:14:54 | 34 | 68 | 29,826 | 3,800,883 | 168,564 | USD 1.35 |
| Kimi | 08:13:40 | 33 | 159,932 | 23,225 | 3,617,216 | 0 | USD 1.28 |
| MiniMax | 09:11:10 | 125 | 413,443 | 182,511 | 29,484,800 | 0 | USD 0.61 |
| Grok | 08:19:25 | 46 | 339,876 | 75,563 | 5,948,160 | 0 | USD 5.86 |
| Qwen | 08:23:09 | 65 | 214,857 | 54,679 | 7,335,680 | 0 | USD 2.59 |
| Argon | 16:48:14 | 45 | 307,278 | 47,066 | 5,930,994 | 0 | USD 1.68 |
| Flash | 08:51:40 | 72 | 187,156 | 76,771 | 8,489,216 | 0 | USD 0.10 |
| Sol | 07:48:14 | 26 | 147,152 | 13,343 | 2,642,048 | 0 | USD 0.69 |
| Fable | 16:00:11 | 32 | 994 | 65,540 | 6,241,424 | 277,357 | USD 10.39 |
| Terra | 07:55:14 | 29 | 105,928 | 9,794 | 2,159,488 | 0 | USD 0.26 |
| GLM | 07:47:43 | 54 | 246,851 | 24,338 | 3,407,782 | 0 | USD 1.34 |
| Astra | 07:40:34 | 24 | 191,251 | 13,902 | 2,307,584 | 0 | USD 4.92 |
| DeepSeek Pro | 07:52:28 | 68 | 1,147,290 | 50,472 | 5,758,464 | 0 | USD 0.98 |
| Haiku | 16:19:30 | 37 | 74 | 55,973 | 4,170,461 | 172,142 | USD 0.37 |
| Luna | 07:59:50 | 59 | 205,256 | 68,021 | 7,252,992 | 0 | USD 0.13 |

## Final-edition recorded charges

| Model | Recorded charge USD | Calls with recorded charge |
|---|---|---|
| Opus | No per-token charge | Not applicable |
| Sonnet | No per-token charge | Not applicable |
| Kimi | USD 1.28 | 33/33 |
| MiniMax | USD 0.61 | 124/125 |
| Grok | Not recorded | Not applicable |
| Qwen | USD 2.59 | 65/65 |
| Argon | Not recorded | Not applicable |
| Flash | USD 0.07 | 72/72 |
| Sol | No per-token charge | Not applicable |
| Fable | No per-token charge | Not applicable |
| Terra | No per-token charge | Not applicable |
| GLM | USD 1.67 | 54/54 |
| Astra | No per-token charge | Not applicable |
| DeepSeek Pro | USD 1.12 | 68/68 |
| Haiku | No per-token charge | Not applicable |
| Luna | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,667,502 |
| Output | 827,658 |
| Cache Read | 105,136,155 |
| Cache Write | 821,216 |
| Calls with available telemetry | 797 |
| API estimate subtotal (available telemetry) | USD 36.23 |
| Recorded OpenRouter charges | USD 7.33 |
| Models with unavailable telemetry/estimates | None |

## Earlier / diagnostic attempts

| Model | Start ET | Calls | Uncached input | Output | Cache read | Cache write | API estimate* |
|---|---|---|---|---|---|---|---|
| Fable 5.1 subscription | 15:57:19 | 1 | 2 | 4 | 0 | 36,700 | USD 0.73 |
| Gemini 4 Argon | 15:57:29 | 1 | 14,945 | 5 | 0 | 0 | USD 0.03 |
| Gemini 4 Argon | 16:00:15 | 31 | 218,580 | 16,594 | 2,108,618 | 0 | USD 0.81 |
| Gemini 4 Argon | 16:18:00 | 39 | 239,269 | 33,805 | 3,127,351 | 0 | USD 1.13 |
| Haiku 5.5 subscription | 15:57:10 | 1 | 2 | 4 | 0 | 35,634 | USD 0.01 |
| MiniMax M3.1 Flash | 08:19:20 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |
| MiniMax M3.1 Flash | 08:53:36 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |
| Sonnet 5.5 subscription | 15:57:02 | 1 | 2 | 4 | 0 | 34,811 | USD 0.14 |

## Definitions and limits

*API estimate means tokens priced at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Fable, Sonnet and Haiku usage was recovered from Claude Code native logs using unique exact-model matches within each coordinator-selected run window after the stored CLI bindings were absent. Calls are deduplicated by message ID, using the same native-log accounting as Opus. Totals cover all 16 final editions.

Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested. This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the sixteen final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. Rows follow the model-comparison rank order.
Two earlier MiniMax dispatch attempts for the same job (08:19 and 08:53 ET) failed before producing usage; the 09:11 ET run (session ca8ce19a-954b-4cbb-b3ac-ba7559d3dbdb) is the coordinator-selected attempt and matches the edition run.json. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. The four added models use the additive verified pricing snapshot; prior model rates are unchanged. Argon uses introductory rates; Haiku tiers are resolved per request including cache tokens. The two failed Argon attempts remain in the diagnostic table.
Collector generated: 2026-11-08T17:20:41-05:00. Pricing source: pricing/2026-11-08T210140765623Z/api-pricing.json, as of 2026-11-08; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 11, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent total (16/16 models): USD 36.23. Recorded OpenRouter charges for the final editions: USD 7.33. Pricing snapshot age at report date: 0 days. Last successful daily source verification for this snapshot: not yet recorded. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- MiniMax M3.1 Flash (2026-11-08T08:19:20-05:00): route recorded zero usage for every call (openrouter); tokens unavailable
- MiniMax M3.1 Flash (2026-11-08T08:53:36-05:00): route recorded zero usage for every call (openrouter); tokens unavailable

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-08T210140765623Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- Opus: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- Sonnet: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- Kimi: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- MiniMax: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- Grok: [grok-4.7](https://docs.x.ai/developers/pricing)
- Qwen: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- Argon: [gemini-4-argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/)
- Flash: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- Sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- Fable: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- Terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- GLM: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- Astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- DeepSeek Pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- Haiku: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- Luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-08/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-08.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

