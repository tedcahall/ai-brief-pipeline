# Token Usage and Cost - 2026-11-08

## Final-edition token usage

| Model | Start ET | Calls | Uncached input | Output | Cache read | Cache write | API estimate* |
|---|---|---|---|---|---|---|---|
| Opus | 07:40:34 | 48 | 96 | 36,634 | 6,588,963 | 203,153 | USD 3.68 |
| Grok | 08:19:25 | 46 | 339,876 | 75,563 | 5,948,160 | 0 | USD 5.86 |
| Qwen | 08:23:09 | 65 | 214,857 | 54,679 | 7,335,680 | 0 | USD 2.59 |
| Kimi | 08:13:40 | 33 | 159,932 | 23,225 | 3,617,216 | 0 | USD 1.28 |
| GLM | 07:47:43 | 54 | 246,851 | 24,338 | 3,407,782 | 0 | USD 1.34 |
| MiniMax | 09:11:10 | 125 | 413,443 | 182,511 | 29,484,800 | 0 | USD 0.61 |
| Sol | 07:48:14 | 26 | 147,152 | 13,343 | 2,642,048 | 0 | USD 0.69 |
| Terra | 07:55:14 | 29 | 105,928 | 9,794 | 2,159,488 | 0 | USD 0.26 |
| Flash | 08:51:40 | 72 | 187,156 | 76,771 | 8,489,216 | 0 | USD 0.10 |
| Astra | 07:40:34 | 24 | 191,251 | 13,902 | 2,307,584 | 0 | USD 4.92 |
| Luna | 07:59:50 | 59 | 205,256 | 68,021 | 7,252,992 | 0 | USD 0.13 |
| DeepSeek Pro | 07:52:28 | 68 | 1,147,290 | 50,472 | 5,758,464 | 0 | USD 0.98 |

## Final-edition recorded charges

| Model | Recorded charge USD | Calls with recorded charge |
|---|---|---|
| Opus | No per-token charge | Not applicable |
| Grok | Not recorded | Not applicable |
| Qwen | USD 2.59 | 65/65 |
| Kimi | USD 1.28 | 33/33 |
| GLM | USD 1.67 | 54/54 |
| MiniMax | USD 0.61 | 124/125 |
| Sol | No per-token charge | Not applicable |
| Terra | No per-token charge | Not applicable |
| Flash | USD 0.07 | 72/72 |
| Astra | No per-token charge | Not applicable |
| Luna | No per-token charge | Not applicable |
| DeepSeek Pro | USD 1.12 | 68/68 |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,359,088 |
| Output | 629,253 |
| Cache Read | 84,992,393 |
| Cache Write | 203,153 |
| Calls | 649 |
| API estimate total | USD 22.43 |
| Recorded OpenRouter charges | USD 7.33 |
| Models with missing API estimates | None |

## Earlier / diagnostic attempts

| Model | Start ET | Calls | Uncached input | Output | Cache read | Cache write | API estimate* |
|---|---|---|---|---|---|---|---|
| MiniMax M3.1 Flash | 08:19:20 | 1 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |
| MiniMax M3.1 Flash | 08:53:36 | 1 | Unavailable | Unavailable | Unavailable | Unavailable | Unavailable |

## Definitions and limits

*API estimate means tokens priced at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested. This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twelve final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. Rows follow the model-comparison rank order.
Two earlier MiniMax dispatch attempts for the same job (08:19 and 08:53 ET) failed before producing usage; the 09:11 ET run (session ca8ce19a-954b-4cbb-b3ac-ba7559d3dbdb) is the coordinator-selected attempt and matches the edition run.json. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Pricing rates themselves are unchanged.
Collector generated: 2026-11-08T09:37:53-05:00. Pricing source: pricing/2026-10-29/api-pricing.json, as of 2026-10-29; earlier-date fallback: True. Pricing verification: {'status': 'passed', 'files_checked': 10, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Complete twelve-model API-equivalent total: USD 22.43. Recorded OpenRouter charges for the final editions: USD 7.33. Pricing snapshot age at report date: 10 days. Last successful daily source verification for this snapshot: 2026-11-08T08:02:38.345253+00:00. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- MiniMax M3.1 Flash (2026-11-08T08:19:20-05:00): route recorded zero usage for every call (openrouter); tokens unavailable
- MiniMax M3.1 Flash (2026-11-08T08:53:36-05:00): route recorded zero usage for every call (openrouter); tokens unavailable

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-10-29/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- Opus: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- Grok: [grok-4.7](https://docs.x.ai/developers/pricing)
- Qwen: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- Kimi: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- GLM: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- MiniMax: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- Sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- Terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- Flash: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- Astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- Luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- DeepSeek Pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-08/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-08.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

