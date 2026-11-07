# Usage and Cost - 2026-11-03

Generated 2026-11-03T12:24:23-05:00 by `scripts/brief_usage_collector.py` (read-only; usage/metadata only).
Pricing: `pricing/2026-10-29/api-pricing.json` (as of 2026-10-29, FALLBACK to earlier date). Hash check against verification.json: passed (10 files).
Runs are matched to pricing entries by exact `model_ref` == run.json `expected_model` (cron job payload model for extra runs).

## Scope and totals

All 12 final HTML runs are matched by exact session ID to this edition's saved run records. No extra attempt rows were returned for this edition. Production publishing and report generation are outside scope.

**API-equivalent estimate: $27.34. Recorded OpenRouter charges: $9.76. Do not add these figures.** Subscription-backed runs have no per-token bill; subscription fees are not allocated. Actual xAI charges are not recorded. Qwen's higher estimate is used; raw bounds remain in the audit JSON. Pricing uses the verified older snapshot identified above, not freshly checked current rates.

## 1. Token usage

| Model | Calls | Uncached input | Output | Cache read | Cache write | API Cost* |
|---|---:|---:|---:|---:|---:|---:|
| DeepSeek v4 Pro | 59 | 441,823 | 79,090 | 4,718,848 | 0 | $0.55 |
| DeepSeek v4.1 Flash | 60 | 163,746 | 71,445 | 6,029,696 | 0 | $0.09 |
| GLM-5.3 | 64 | 130,802 | 43,872 | 5,348,352 | 0 | $1.77 |
| GPT-6 Astra | 38 | 177,573 | 15,089 | 4,560,768 | 0 | $7.09 |
| GPT-6 Luna | 41 | 140,605 | 23,292 | 4,008,960 | 0 | $0.07 |
| GPT-6.1 Sol | 39 | 197,167 | 21,762 | 4,694,400 | 0 | $1.08 |
| GPT-6.1 Terra | 37 | 111 | 11,947 | 451,476 | 3,316,607 | $4.23 |
| Grok-4.7 | 49 | 276,465 | 75,787 | 6,295,936 | 0 | $5.95 |
| Kimi K3.1 Pro | 33 | 156,052 | 23,423 | 3,343,360 | 0 | $1.22 |
| MiniMax M3.1 Flash | 101 | 346,541 | 133,706 | 18,874,880 | 0 | $0.42 |
| Opus 5.5 | 23 | 46 | 39,440 | 3,276,237 | 231,336 | $3.29 |
| Qwen 3.8 Max 0902 | 44 | 166,311 | 47,410 | 3,907,968 | 0 | $1.59 |

*API Cost = API-equivalent estimated cost in USD, calculated from token usage at published API list rates, including subscription-backed runs. It is not an actual bill. For Qwen, the higher available estimate is used in the tables and estimate totals; the deployment tier remains unverified. Other ranges reflect unresolved pricing tiers.


## 2. API-equivalent estimates (NOT bills)

tokens x published direct-provider list rates, per call; an estimate, not a bill. Includes subscription runs. Basis: Direct provider public standard API list pricing. No subscription allocation, taxes, tools, infrastructure or negotiated discounts.

| Run (ET start) | model_ref | Tiers used (calls) | API Cost* |
|---|---|---|---:|
| DeepSeek v4 Pro 07:46 | `openrouter_deek/deepseek/deepseek-v4-pro` | [Off-peak (59)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.55 |
| DeepSeek v4.1 Flash 07:46 | `openrouter_flash/deepseek/deepseek-v4.1-flash-1017` | [Off-peak (60)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.09 |
| GLM-5.3 07:34 | `openrouter_eich/z-ai/glm-5.3` | [Z.AI direct (64)](https://docs.z.ai/guides/overview/pricing) | $1.77 |
| GPT-6 Astra 07:22 | `openai/gpt-6-astra` | [Standard short (38)](https://developers.openai.com/api/docs/pricing) | $7.09 |
| GPT-6 Luna 07:14 | `openai/gpt-6-luna` | [Standard short (41)](https://developers.openai.com/api/docs/pricing) | $0.07 |
| GPT-6.1 Sol 07:22 | `openai/gpt-6.1-sol` | [Standard short (39)](https://developers.openai.com/api/docs/pricing) | $1.08 |
| GPT-6.1 Terra 07:14 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (37)](https://developers.openai.com/api/docs/pricing) | $4.23 |
| Grok-4.7 08:43 | `xai/grok-4.7` | [Standard long (15), Standard short (34)](https://docs.x.ai/developers/pricing) | $5.95 |
| Kimi K3.1 Pro 08:43 | `openrouter_kimi/moonshotai/kimi-k3.1-pro` | [Standard flat (33)](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing) | $1.22 |
| MiniMax M3.1 Flash 08:10 | `openrouter_mini/minimax/minimax-m3.1-flash` | [Direct flat (101)](https://www.minimax.io/blog/minimax-m31f) | $0.42 |
| Opus 5.5 07:34 | `anthropic/claude-opus-5-5` | [Standard (23)](https://platform.claude.com/docs/en/models/opus-5-5/overview) | $3.29 |
| Qwen 3.8 Max 0902 08:10 | `openrouter_qwenmax/qwen/qwen3.8-max-0902` | [Global (44), Singapore / International (44)](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | $1.59 |

**Estimate total, comparison runs: $27.34.** All priced runs incl. extras: $27.34. Unpriced: none.

## 3. Recorded charges

OpenRouter per-generation total_cost (provider-billed) as recorded per call. Subscription runs (Codex, Claude Code) have no per-token charge.

| Run (ET start) | Recorded charge USD | Calls with charge |
|---|---:|---|
| DeepSeek v4 Pro 07:46 | $1.46 | 59/59 |
| DeepSeek v4.1 Flash 07:46 | $0.05 | 60/60 |
| GLM-5.3 07:34 | $0.80 | 64/64 |
| GPT-6 Astra 07:22 | none (subscription) | - |
| GPT-6 Luna 07:14 | none (subscription) | - |
| GPT-6.1 Sol 07:22 | none (subscription) | - |
| GPT-6.1 Terra 07:14 | $4.23 | 37/37 |
| Grok-4.7 08:43 | not recorded | - |
| Kimi K3.1 Pro 08:43 | $1.22 | 33/33 |
| MiniMax M3.1 Flash 08:10 | $0.42 | 101/101 |
| Opus 5.5 07:34 | none (subscription) | - |
| Qwen 3.8 Max 0902 08:10 | $1.59 | 44/44 |

**Recorded OpenRouter charges, comparison runs: $9.76** (all runs: $9.76). Incomplete per-call charge data: none. Billed routes with no recorded charge: Grok-4.7 (xai).
Estimates and charges are different quantities and are never added together.

## 4. Unresolved (disclosed, not settled by these numbers)

### Pricing tiers

- MiniMax M3.1 Flash: 1 tier(s) on card (Direct flat: {}). Calls per tier: {"Direct flat": 101}. Card lists a single tier; no long-context threshold verified.
- MiniMax M3.1 Flash note (pricing file): Separate cache-write pricing is not specified in the cited announcement; an empty map does not mean free.
- Claude Opus 5.5: 1 tier(s) on card (Standard: {}). Calls per tier: {"Standard": 23}. Card lists a single tier; no long-context threshold verified.
- Claude Opus 5.5 note (pricing file): Audit aggregates cache writes without TTL split; do not assume all writes use 5m for an exact estimate.
- DeepSeek V4.1 Flash 1017: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 60}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4.1 Flash 1017 note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4.1 Flash 1017 note (pricing file): No separate cache-write price on cited card.
- DeepSeek V4 Pro: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 59}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4 Pro note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4 Pro note (pricing file): No separate cache-write price on cited card.
- GLM-5.3: 1 tier(s) on card (Z.AI direct: {}). Calls per tier: {"Z.AI direct": 64}. Card lists a single tier; no long-context threshold verified.
- GLM-5.3 note (pricing file): Cache storage is limited-time free; a distinct cache-write token price is not specified on the cited rate card.
- GLM-5.3 note (pricing file): Direct Z.AI list pricing is not the DeepInfra/Fireworks OpenRouter bill.
- GPT-6 Astra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 38}.
- GPT-6 Astra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Astra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Astra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6 Luna: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 41}.
- GPT-6 Luna note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Luna note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Luna note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Sol: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 39}.
- GPT-6.1 Sol note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Sol note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Sol note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Terra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 37}.
- GPT-6.1 Terra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Terra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Terra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- Grok-4.7: 2 tier(s) on card (Standard short: {"prompt_tokens_lt": 200000}; Standard long: {"prompt_tokens_gte": 200000}). Calls per tier: {"Standard short": 34, "Standard long": 15}.
- Grok-4.7 note (pricing file): Global endpoint baseline; US regional endpoint 1.1x; Priority 2x; Batch 0.8x.
- Grok-4.7 note (pricing file): No separate cache-write price on cited card.
- Kimi K3.1 Pro: 1 tier(s) on card (Standard flat: {}). Calls per tier: {"Standard flat": 33}. Card lists a single tier; no long-context threshold verified.
- Kimi K3.1 Pro note (pricing file): USD international rate card; no currency conversion from domestic CNY rates.
- Kimi K3.1 Pro note (pricing file): Flat rates across supported context.
- Qwen 3.8 Max 0902: 2 tier(s) on card (Singapore / International: {"deployment_scope": "International", "region": "Singapore", "cache_read_mode": "implicit"}; Global: {"deployment_scope": "Global", "cache_read_mode": "implicit"}). Calls per tier: {"Singapore / International": 44, "Global": 44}. Tier depends on deployment region/cache mode not visible in usage; reported as a low-high range.
- Qwen 3.8 Max 0902 note (pricing file): Snapshot-specific pricing used. Explicit cache reads are $0.17 International and $0.137 Global per MTok; do not mix implicit and explicit read rates.
- Qwen 3.8 Max 0902 note (pricing file): OpenRouter route region/cache mode is not established by this reference.

### Cache-write TTL and premiums

- MiniMax M3.1 Flash: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Claude Opus 5.5: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 231,336; TTL basis: reported per-call TTL.
- DeepSeek V4.1 Flash 1017: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- DeepSeek V4 Pro: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GLM-5.3: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GPT-6 Astra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6 Luna: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Sol: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Terra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 3,316,607; TTL basis: 30m TTL rate (route rule; matches OpenRouter billed cost).
- Grok-4.7: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Kimi K3.1 Pro: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 0; TTL basis: none needed.
- Qwen 3.8 Max 0902: card has cache-write rates for TTL explicit. Cache writes in today's runs: 0; TTL basis: none needed.

### Cache semantics by route

- **claude-code:** OpenClaw/cron store only the last API call of each claude-cli turn; totals come from the Claude Code session log under ~/.claude/projects (deduped by message id). Cache writes are priced by their reported TTL (5m/1h).
- **codex:** Codex native input_tokens INCLUDES cached input; uncached = input - cached_input. Codex reports cache_write 0, which does not prove an API run would have no cache-write charge, so the estimate may be low by the cache-write premium.
- **openrouter:** Per-call usage from the OpenClaw transcript; input = uncached only (cron usage.input_tokens is the same, uncached only). For OpenAI models via OpenRouter, the uncached prompt part is billed as cache write ($1.25/M for Terra, the 30m-TTL rate; inferred from matching the provider-billed cost, not a documented TTL). Other OpenRouter providers reported cache_write 0 today.
- **xai:** Per-call token counts are available and support the API-equivalent estimate. Actual xAI charges are not recorded; they are not zero.

## Gaps

- Qwen 3.8 Max 0902 (2026-11-03T08:10:19-05:00): tier not determinable from usage (Singapore / International / Global)

## Notes

- Input = uncached input only (excludes cache read and cache write).
- Failed or retried runs are separate rows; non-run sessions are not included.
