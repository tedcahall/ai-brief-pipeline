# Usage and Cost - 2026-11-02

Generated 2026-11-03T04:49:26-05:00 by `scripts/brief_usage_collector.py` (read-only; usage/metadata only).
Pricing: `pricing/2026-10-29/api-pricing.json` (as of 2026-10-29, FALLBACK to earlier date). Hash check against verification.json: passed (10 files).
Runs are matched to pricing entries by exact `model_ref` == run.json `expected_model` (cron job payload model for extra runs).

## Scope and headline totals

**Edition-based accounting:** 12 final HTML runs, three earlier unsuccessful inference attempts (Luna, Terra and Qwen), plus a Sol scheduler failure before a session started. Three runs executed that morning belong to the prior edition and are excluded; their session IDs match the prior-edition audit. Production publishing and this reporting task are outside scope.

| Scope | API-equivalent USD range | Recorded OpenRouter USD |
|---|---:|---:|
| 12 final HTML runs | $23.8958–$24.1604 | $8.6620 |
| 3 earlier unsuccessful attempts | $2.6242–$2.7245 | $2.7102 |
| 15 measured attempts for this edition | $26.5200–$26.8849 | $11.3722 |
| 3 prior-edition runs — excluded | $2.7959–$2.7959 | $4.1636 |

The Sol pre-start failure has no session or usage record: no inference was recorded, but no fabricated zero-cost estimate is assigned. The measured-attempt subtotal excludes this unpriced launch. The three earlier unsuccessful attempts are additional to the 12 final HTML runs, not double-counted within them.

**Do not add API-equivalent estimates and recorded charges.** The first is list-price modeling (including subscription-backed runs); the second is recorded OpenRouter billing only. Codex Astra/Sol/Luna and Claude Code Opus have no per-token charge under these subscriptions; subscription fees are not allocated here. Grok/xAI charges are not recorded.

**Qwen ranges:** final run $1.2425–$1.5071; earlier timeout $0.4713–$0.5716. Tables below use the upper bound. Regional/deployment-tier selection is unverified. The earlier Qwen attempt has recorded charges for only **20 of 24 calls**, so the all-attempt recorded-charge total is incomplete, not a full invoice. All final-run OpenRouter calls have charge records.

Costs use the hash-verified older pricing snapshot stated below, not freshly verified current prices. Totals sum the collector’s four-decimal per-run estimates; displayed per-run tables round to cents.

**Comparison:** among the final runs, Flash has the lowest API-equivalent estimate ($0.0792); Astra has the highest ($6.1677). These are workflow costs with different output lengths, research and validation paths, not controlled per-task efficiency scores. DeepSeek Pro’s $0.3853 list-rate estimate differs from its $1.1625 recorded OpenRouter charge; neither is substituted for the other.

Usage comes from per-call accounting, not rounded session-status snapshots. Non-Claude measured runs reconcile exactly to scheduler usage; Claude uses its deduplicated native log over the run window. Worker elapsed times in the selection report are a different measure from token consumption.

## 1. Token usage

| Model | Calls | Uncached input | Output | Cache read | Cache write | API Cost* |
|---|---:|---:|---:|---:|---:|---:|
| DeepSeek v4 Pro [final HTML] | 53 | 189,245 | 82,456 | 4,413,568 | 0 | $0.39 |
| DeepSeek v4.1 Flash [final HTML] | 81 | 190,285 | 49,557 | 6,981,248 | 0 | $0.08 |
| GLM-5.3 [final HTML] | 47 | 92,089 | 28,266 | 2,804,480 | 0 | $0.98 |
| GPT-6 Astra [final HTML] | 37 | 145,154 | 15,481 | 3,942,144 | 0 | $6.17 |
| GPT-6 Luna [final HTML] | 57 | 221,127 | 47,433 | 8,108,800 | 0 | $0.13 |
| GPT-6.1 Sol [final HTML] | 40 | 172,678 | 18,555 | 4,273,024 | 0 | $0.96 |
| GPT-6.1 Terra [final HTML] | 40 | 120 | 10,970 | 489,099 | 3,177,759 | $4.05 |
| Grok-4.7 [final HTML] | 42 | 277,050 | 69,345 | 5,275,392 | 0 | $5.28 |
| Kimi K3.1 Pro [final HTML] | 32 | 149,254 | 17,095 | 3,278,336 | 0 | $1.13 |
| MiniMax M3.1 Flash [final HTML] | 65 | 519,447 | 86,414 | 9,258,496 | 0 | $0.27 |
| Opus 5.5 [final HTML] | 26 | 52 | 43,867 | 3,305,814 | 210,831 | $3.23 |
| Qwen 3.8 Max 0902 [final HTML] | 40 | 165,209 | 41,647 | 3,707,136 | 0 | $1.51 |
| GPT-6 Luna [earlier unsuccessful] | 13 | 71,625 | 4,620 | 484,224 | 0 | $0.01 |
| GPT-6.1 Terra [earlier unsuccessful] | 24 | 72 | 9,669 | 288,443 | 1,660,623 | $2.14 |
| Qwen 3.8 Max 0902 [earlier unsuccessful] | 24 | 116,373 | 19,799 | 880,128 | 0 | $0.57 |
| GPT-6.1 Sol [pre-start failure] | - | - | - | - | - | GAP |

*API Cost = API-equivalent estimated cost in USD, calculated from token usage at published API list rates, including subscription-backed runs. It is not an actual bill. For Qwen, the higher available estimate is used in the tables and estimate totals; the deployment tier remains unverified. Other ranges reflect unresolved pricing tiers.


## 2. API-equivalent estimates (NOT bills)

tokens x published direct-provider list rates, per call; an estimate, not a bill. Includes subscription runs. Basis: Direct provider public standard API list pricing. No subscription allocation, taxes, tools, infrastructure or negotiated discounts.

| Run (ET start) | model_ref | Tiers used (calls) | API Cost* |
|---|---|---|---:|
| DeepSeek v4 Pro [final HTML] 16:56 | `openrouter_deek/deepseek/deepseek-v4-pro` | [Off-peak (53)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.39 |
| DeepSeek v4.1 Flash [final HTML] 16:56 | `openrouter_flash/deepseek/deepseek-v4.1-flash-1017` | [Off-peak (81)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.08 |
| GLM-5.3 [final HTML] 11:04 | `openrouter_eich/z-ai/glm-5.3` | [Z.AI direct (47)](https://docs.z.ai/guides/overview/pricing) | $0.98 |
| GPT-6 Astra [final HTML] 16:44 | `openai/gpt-6-astra` | [Standard short (37)](https://developers.openai.com/api/docs/pricing) | $6.17 |
| GPT-6 Luna [final HTML] 11:10 | `openai/gpt-6-luna` | [Standard short (57)](https://developers.openai.com/api/docs/pricing) | $0.13 |
| GPT-6.1 Sol [final HTML] 18:43 | `openai/gpt-6.1-sol` | [Standard short (40)](https://developers.openai.com/api/docs/pricing) | $0.96 |
| GPT-6.1 Terra [final HTML] 15:03 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (40)](https://developers.openai.com/api/docs/pricing) | $4.05 |
| Grok-4.7 [final HTML] 18:43 | `xai/grok-4.7` | [Standard long (14), Standard short (28)](https://docs.x.ai/developers/pricing) | $5.28 |
| Kimi K3.1 Pro [final HTML] 18:43 | `openrouter_kimi/moonshotai/kimi-k3.1-pro` | [Standard flat (32)](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing) | $1.13 |
| MiniMax M3.1 Flash [final HTML] 17:27 | `openrouter_mini/minimax/minimax-m3.1-flash` | [Direct flat (65)](https://www.minimax.io/blog/minimax-m31f) | $0.27 |
| Opus 5.5 [final HTML] 16:45 | `anthropic/claude-opus-5-5` | [Standard (26)](https://platform.claude.com/docs/en/models/opus-5-5/overview) | $3.23 |
| Qwen 3.8 Max 0902 [final HTML] 19:55 | `openrouter_qwenmax/qwen/qwen3.8-max-0902` | [Global (40), Singapore / International (40)](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | $1.51 |
| GPT-6 Luna [earlier unsuccessful] 11:04 | `openai/gpt-6-luna` | [Standard short (13)](https://developers.openai.com/api/docs/pricing) | $0.01 |
| GPT-6.1 Terra [earlier unsuccessful] 11:04 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (24)](https://developers.openai.com/api/docs/pricing) | $2.14 |
| Qwen 3.8 Max 0902 [earlier unsuccessful] 17:27 | `openrouter_qwenmax/qwen/qwen3.8-max-0902` | [Global (24), Singapore / International (24)](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | $0.57 |
| GPT-6.1 Sol [pre-start failure] 11:05 | `openai/gpt-6.1-sol` | - | GAP |

**API-equivalent estimate, 12 final HTML runs: $24.16.** All 15 measured edition attempts: $26.88. Unpriced: GPT-6.1 Sol [pre-start failure].

## 3. Recorded charges

OpenRouter per-generation total_cost (provider-billed) as recorded per call. Subscription runs (Codex, Claude Code) have no per-token charge.

| Run (ET start) | Recorded charge USD | Calls with charge |
|---|---:|---|
| DeepSeek v4 Pro [final HTML] 16:56 | $1.16 | 53/53 |
| DeepSeek v4.1 Flash [final HTML] 16:56 | $0.06 | 81/81 |
| GLM-5.3 [final HTML] 11:04 | $0.49 | 47/47 |
| GPT-6 Astra [final HTML] 16:44 | none (subscription) | - |
| GPT-6 Luna [final HTML] 11:10 | none (subscription) | - |
| GPT-6.1 Sol [final HTML] 18:43 | none (subscription) | - |
| GPT-6.1 Terra [final HTML] 15:03 | $4.05 | 40/40 |
| Grok-4.7 [final HTML] 18:43 | not recorded | - |
| Kimi K3.1 Pro [final HTML] 18:43 | $1.13 | 32/32 |
| MiniMax M3.1 Flash [final HTML] 17:27 | $0.27 | 65/65 |
| Opus 5.5 [final HTML] 16:45 | none (subscription) | - |
| Qwen 3.8 Max 0902 [final HTML] 19:55 | $1.51 | 40/40 |
| GPT-6 Luna [earlier unsuccessful] 11:04 | none (subscription) | - |
| GPT-6.1 Terra [earlier unsuccessful] 11:04 | $2.14 | 24/24 |
| Qwen 3.8 Max 0902 [earlier unsuccessful] 17:27 | $0.57 | 20/24 |
| GPT-6.1 Sol [pre-start failure] 11:05 | not recorded | - |

**Recorded OpenRouter charges, 12 final HTML runs: $8.66** (15 measured edition attempts: $11.37). Incomplete per-call charge data: Qwen 3.8 Max 0902 2026-11-02T17:27:28-05:00. Billed routes with no recorded charge: Grok-4.7 (xai).
Estimates and charges are different quantities and are never added together.

## 4. Unresolved (disclosed, not settled by these numbers)

### Pricing tiers

- MiniMax M3.1 Flash: 1 tier(s) on card (Direct flat: {}). Calls per tier: {"Direct flat": 65}. Card lists a single tier; no long-context threshold verified.
- MiniMax M3.1 Flash note (pricing file): Separate cache-write pricing is not specified in the cited announcement; an empty map does not mean free.
- Claude Opus 5.5: 1 tier(s) on card (Standard: {}). Calls per tier: {"Standard": 26}. Card lists a single tier; no long-context threshold verified.
- Claude Opus 5.5 note (pricing file): Audit aggregates cache writes without TTL split; do not assume all writes use 5m for an exact estimate.
- DeepSeek V4.1 Flash 1017: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 81}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4.1 Flash 1017 note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4.1 Flash 1017 note (pricing file): No separate cache-write price on cited card.
- DeepSeek V4 Pro: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 53}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4 Pro note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4 Pro note (pricing file): No separate cache-write price on cited card.
- GLM-5.3: 1 tier(s) on card (Z.AI direct: {}). Calls per tier: {"Z.AI direct": 47}. Card lists a single tier; no long-context threshold verified.
- GLM-5.3 note (pricing file): Cache storage is limited-time free; a distinct cache-write token price is not specified on the cited rate card.
- GLM-5.3 note (pricing file): Direct Z.AI list pricing is not the DeepInfra/Fireworks OpenRouter bill.
- GPT-6 Astra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 37}.
- GPT-6 Astra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Astra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Astra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6 Luna: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 70}.
- GPT-6 Luna note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Luna note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Luna note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Sol: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 40}.
- GPT-6.1 Sol note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Sol note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Sol note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Terra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 64}.
- GPT-6.1 Terra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Terra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Terra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- Grok-4.7: 2 tier(s) on card (Standard short: {"prompt_tokens_lt": 200000}; Standard long: {"prompt_tokens_gte": 200000}). Calls per tier: {"Standard short": 28, "Standard long": 14}.
- Grok-4.7 note (pricing file): Global endpoint baseline; US regional endpoint 1.1x; Priority 2x; Batch 0.8x.
- Grok-4.7 note (pricing file): No separate cache-write price on cited card.
- Kimi K3.1 Pro: 1 tier(s) on card (Standard flat: {}). Calls per tier: {"Standard flat": 32}. Card lists a single tier; no long-context threshold verified.
- Kimi K3.1 Pro note (pricing file): USD international rate card; no currency conversion from domestic CNY rates.
- Kimi K3.1 Pro note (pricing file): Flat rates across supported context.
- Qwen 3.8 Max 0902: 2 tier(s) on card (Singapore / International: {"deployment_scope": "International", "region": "Singapore", "cache_read_mode": "implicit"}; Global: {"deployment_scope": "Global", "cache_read_mode": "implicit"}). Calls per tier: {"Singapore / International": 64, "Global": 64}. Tier depends on deployment region/cache mode not visible in usage; reported as a low-high range.
- Qwen 3.8 Max 0902 note (pricing file): Snapshot-specific pricing used. Explicit cache reads are $0.17 International and $0.137 Global per MTok; do not mix implicit and explicit read rates.
- Qwen 3.8 Max 0902 note (pricing file): OpenRouter route region/cache mode is not established by this reference.

### Cache-write TTL and premiums

- MiniMax M3.1 Flash: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Claude Opus 5.5: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 210,831; TTL basis: reported per-call TTL.
- DeepSeek V4.1 Flash 1017: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- DeepSeek V4 Pro: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GLM-5.3: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GPT-6 Astra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6 Luna: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Sol: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Terra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 4,838,382; TTL basis: 30m TTL rate (route rule; matches OpenRouter billed cost).
- Grok-4.7: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Kimi K3.1 Pro: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 0; TTL basis: none needed.
- Qwen 3.8 Max 0902: card has cache-write rates for TTL explicit. Cache writes in today's runs: 0; TTL basis: none needed.

### Cache semantics by route

- **claude-code:** OpenClaw/cron store only the last API call of each claude-cli turn; totals come from the Claude Code session log under ~/.claude/projects (deduped by message id). Cache writes are priced by their reported TTL (5m/1h).
- **codex:** Codex native input_tokens INCLUDES cached input; uncached = input - cached_input. Codex reports cache_write 0, which does not prove an API run would have no cache-write charge, so the estimate may be low by the cache-write premium.
- **openrouter:** Per-call usage from the OpenClaw transcript; input = uncached only (cron usage.input_tokens is the same, uncached only). For OpenAI models via OpenRouter, the uncached prompt part is billed as cache write ($1.25/M for Terra, the 30m-TTL rate; inferred from matching the provider-billed cost, not a documented TTL). Other OpenRouter providers reported cache_write 0 today.
- **unknown:** not characterized
- **xai:** Per-call tokens are available and support an API-equivalent estimate. Actual xAI charges are not recorded; they are not zero.

## Gaps

- Qwen 3.8 Max 0902 [final HTML] (2026-11-02T19:55:31-05:00): tier not determinable from usage (Singapore / International / Global)
- Qwen 3.8 Max 0902 [earlier unsuccessful] (2026-11-02T17:27:28-05:00): tier not determinable from usage (Singapore / International / Global)
- GPT-6.1 Sol [pre-start failure] (2026-11-02T11:05:03-05:00): run has no session (failed before start)

## Notes

- Input = uncached input only (excludes cache read and cache write).
- Earlier unsuccessful attempts are separate rows. The Sol pre-start failure is disclosed without invented usage or cost.
