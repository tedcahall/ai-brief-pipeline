# AI Brief model comparison 2026-11-01: usage, API-equivalent estimates, recorded charges

Generated 2026-11-02T10:18:19-05:00 by `scripts/brief_usage_collector.py` (read-only; usage/metadata only).
Pricing: `pricing/2026-10-29/api-pricing.json` (as of 2026-10-29, FALLBACK to earlier date). Hash check against verification.json: passed (10 files).
Runs are matched to pricing entries by exact `model_ref` == run.json `expected_model` (cron job payload model for extra runs).

## Scope and totals

Twelve latest completed editions are included, plus the three original unsuccessful attempts. The three retries used revised selection rules; no new inference was launched for this report. `[retry]` rows are the new successful attempts; `[original unsuccessful]` rows are sunk costs, not part of the latest twelve-edition cohort.

The collector was locally adapted to include sessions bound to this edition even when executed the following day. The shared collector and prior reports were not modified. All twelve original usage/cost records exactly match the previous audit.

| Cost scope | API-equivalent estimate | Recorded OpenRouter charges |
|---|---:|---:|
| Latest completed twelve editions | $23.35 | $7.82 |
| Three retries only (included above) | $2.80 | $4.16 |
| Three original unsuccessful attempts | $1.51 | $1.23 |
| All fifteen attempts | $24.86 | $9.05 |

Qwen estimate range: **$1.1807–$1.4321**; the upper value is used in the summary and tables, consistent with prior reporting. Deployment tier is unverified. Consequently, all-attempt API-equivalent cost ranges from **24.6092 to 24.8606 USD**.

API-equivalent estimates are not bills. Codex Astra/Sol/Luna and Claude Code Opus use subscriptions. Recorded charges cover OpenRouter only; xAI charges are not recorded. These two cost bases are never added. Pricing is the verified older snapshot identified below, not newly checked current pricing.

DeepSeek Pro retry: list-rate estimate and recorded OpenRouter charge differ; both are retained as observed, with no assumption that provider billing must equal direct-provider list pricing.

## 1. Token usage

| Model | Calls | Uncached input | Output | Cache read | Cache write | API Cost* |
|---|---:|---:|---:|---:|---:|---:|
| DeepSeek v4 Pro [original unsuccessful] | 25 | 441,317 | 31,822 | 1,166,592 | 0 | $0.38 |
| DeepSeek v4 Pro [retry] | 61 | 310,222 | 129,349 | 8,903,808 | 0 | $0.66 |
| DeepSeek v4.1 Flash | 70 | 288,938 | 89,879 | 7,278,464 | 0 | $0.12 |
| GLM-5.3 | 46 | 136,274 | 29,098 | 4,115,200 | 0 | $1.39 |
| GPT-6 Astra | 36 | 155,373 | 17,156 | 3,946,368 | 0 | $6.36 |
| GPT-6 Luna [original unsuccessful] | 24 | 118,449 | 16,987 | 1,493,760 | 0 | $0.04 |
| GPT-6 Luna [retry] | 45 | 135,588 | 27,895 | 3,827,200 | 0 | $0.07 |
| GPT-6.1 Sol | 29 | 144,901 | 14,300 | 2,999,680 | 0 | $0.73 |
| GPT-6.1 Terra [original unsuccessful] | 20 | 60 | 6,703 | 238,279 | 838,973 | $1.09 |
| GPT-6.1 Terra [retry] | 26 | 78 | 10,543 | 313,525 | 1,603,969 | $2.07 |
| Grok-4.7 | 48 | 240,080 | 75,432 | 6,543,232 | 0 | $5.81 |
| Kimi K3.1 Pro | 32 | 262,383 | 22,375 | 2,708,480 | 0 | $1.29 |
| MiniMax M3.1 Flash | 57 | 401,215 | 53,378 | 6,989,440 | 0 | $0.20 |
| Opus 5.5 | 45 | 90 | 37,285 | 5,272,920 | 178,443 | $3.23 |
| Qwen 3.8 Max 0902 | 39 | 164,536 | 51,224 | 3,182,592 | 0 | $1.43 |

*API Cost = API-equivalent estimated cost in USD, calculated from token usage at published API list rates, including subscription-backed runs. It is not an actual bill. For Qwen, the higher available estimate is used in the tables and estimate totals; the deployment tier remains unverified. Other ranges reflect unresolved pricing tiers.


## 2. API-equivalent estimates (NOT bills)

tokens x published direct-provider list rates, per call; an estimate, not a bill. Includes subscription runs. Basis: Direct provider public standard API list pricing. No subscription allocation, taxes, tools, infrastructure or negotiated discounts.

| Run (ET start) | model_ref | Tiers used (calls) | API Cost* |
|---|---|---|---:|
| DeepSeek v4 Pro [original unsuccessful] 06:06 | `openrouter_deek/deepseek/deepseek-v4-pro` | [Off-peak (25)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.38 |
| DeepSeek v4 Pro [retry] 07:50 | `openrouter_deek/deepseek/deepseek-v4-pro` | [Off-peak (61)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.66 |
| DeepSeek v4.1 Flash 06:06 | `openrouter_flash/deepseek/deepseek-v4.1-flash-1017` | [Off-peak (70)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.12 |
| GLM-5.3 06:06 | `openrouter_eich/z-ai/glm-5.3` | [Z.AI direct (46)](https://docs.z.ai/guides/overview/pricing) | $1.39 |
| GPT-6 Astra 05:35 | `openai/gpt-6-astra` | [Standard short (36)](https://developers.openai.com/api/docs/pricing) | $6.36 |
| GPT-6 Luna [original unsuccessful] 05:34 | `openai/gpt-6-luna` | [Standard short (24)](https://developers.openai.com/api/docs/pricing) | $0.04 |
| GPT-6 Luna [retry] 07:41 | `openai/gpt-6-luna` | [Standard short (45)](https://developers.openai.com/api/docs/pricing) | $0.07 |
| GPT-6.1 Sol 05:34 | `openai/gpt-6.1-sol` | [Standard short (29)](https://developers.openai.com/api/docs/pricing) | $0.73 |
| GPT-6.1 Terra [original unsuccessful] 05:34 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (20)](https://developers.openai.com/api/docs/pricing) | $1.09 |
| GPT-6.1 Terra [retry] 07:41 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (26)](https://developers.openai.com/api/docs/pricing) | $2.07 |
| Grok-4.7 06:06 | `xai/grok-4.7` | [Standard long (14), Standard short (34)](https://docs.x.ai/developers/pricing) | $5.81 |
| Kimi K3.1 Pro 06:17 | `openrouter_kimi/moonshotai/kimi-k3.1-pro` | [Standard flat (32)](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing) | $1.29 |
| MiniMax M3.1 Flash 05:34 | `openrouter_mini/minimax/minimax-m3.1-flash` | [Direct flat (57)](https://www.minimax.io/blog/minimax-m31f) | $0.20 |
| Opus 5.5 05:34 | `anthropic/claude-opus-5-5` | [Standard (45)](https://platform.claude.com/docs/en/models/opus-5-5/overview) | $3.23 |
| Qwen 3.8 Max 0902 06:06 | `openrouter_qwenmax/qwen/qwen3.8-max-0902` | [Global (39), Singapore / International (39)](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | $1.43 |

**API-equivalent estimate, all fifteen attempts: $24.86.** Qwen upper-bound convention applies.

## 3. Recorded charges

OpenRouter per-generation total_cost (provider-billed) as recorded per call. Subscription runs (Codex, Claude Code) have no per-token charge.

| Run (ET start) | Recorded charge USD | Calls with charge |
|---|---:|---|
| DeepSeek v4 Pro [original unsuccessful] 06:06 | $0.13 | 25/25 |
| DeepSeek v4 Pro [retry] 07:50 | $2.09 | 61/61 |
| DeepSeek v4.1 Flash 06:06 | $0.08 | 70/70 |
| GLM-5.3 06:06 | $0.66 | 46/46 |
| GPT-6 Astra 05:35 | none (subscription) | - |
| GPT-6 Luna [original unsuccessful] 05:34 | none (subscription) | - |
| GPT-6 Luna [retry] 07:41 | none (subscription) | - |
| GPT-6.1 Sol 05:34 | none (subscription) | - |
| GPT-6.1 Terra [original unsuccessful] 05:34 | $1.09 | 20/20 |
| GPT-6.1 Terra [retry] 07:41 | $2.07 | 26/26 |
| Grok-4.7 06:06 | not recorded | - |
| Kimi K3.1 Pro 06:17 | $1.29 | 32/32 |
| MiniMax M3.1 Flash 05:34 | $0.20 | 57/57 |
| Opus 5.5 05:34 | none (subscription) | - |
| Qwen 3.8 Max 0902 06:06 | $1.43 | 39/39 |

**Recorded OpenRouter charges, all fifteen attempts: $9.05.** Incomplete per-call charge data: none. Billed routes with no recorded charge: Grok-4.7 (xai).
Estimates and charges are different quantities and are never added together.

## 4. Unresolved (disclosed, not settled by these numbers)

### Pricing tiers

- MiniMax M3.1 Flash: 1 tier(s) on card (Direct flat: {}). Calls per tier: {"Direct flat": 57}. Card lists a single tier; no long-context threshold verified.
- MiniMax M3.1 Flash note (pricing file): Separate cache-write pricing is not specified in the cited announcement; an empty map does not mean free.
- Claude Opus 5.5: 1 tier(s) on card (Standard: {}). Calls per tier: {"Standard": 45}. Card lists a single tier; no long-context threshold verified.
- Claude Opus 5.5 note (pricing file): Audit aggregates cache writes without TTL split; do not assume all writes use 5m for an exact estimate.
- DeepSeek V4.1 Flash 1017: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 70}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4.1 Flash 1017 note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4.1 Flash 1017 note (pricing file): No separate cache-write price on cited card.
- DeepSeek V4 Pro: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 86}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4 Pro note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4 Pro note (pricing file): No separate cache-write price on cited card.
- GLM-5.3: 1 tier(s) on card (Z.AI direct: {}). Calls per tier: {"Z.AI direct": 46}. Card lists a single tier; no long-context threshold verified.
- GLM-5.3 note (pricing file): Cache storage is limited-time free; a distinct cache-write token price is not specified on the cited rate card.
- GLM-5.3 note (pricing file): Direct Z.AI list pricing is not the DeepInfra/Fireworks OpenRouter bill.
- GPT-6 Astra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 36}.
- GPT-6 Astra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Astra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Astra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6 Luna: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 69}.
- GPT-6 Luna note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Luna note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Luna note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Sol: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 29}.
- GPT-6.1 Sol note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Sol note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Sol note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Terra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 46}.
- GPT-6.1 Terra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Terra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Terra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- Grok-4.7: 2 tier(s) on card (Standard short: {"prompt_tokens_lt": 200000}; Standard long: {"prompt_tokens_gte": 200000}). Calls per tier: {"Standard short": 34, "Standard long": 14}.
- Grok-4.7 note (pricing file): Global endpoint baseline; US regional endpoint 1.1x; Priority 2x; Batch 0.8x.
- Grok-4.7 note (pricing file): No separate cache-write price on cited card.
- Kimi K3.1 Pro: 1 tier(s) on card (Standard flat: {}). Calls per tier: {"Standard flat": 32}. Card lists a single tier; no long-context threshold verified.
- Kimi K3.1 Pro note (pricing file): USD international rate card; no currency conversion from domestic CNY rates.
- Kimi K3.1 Pro note (pricing file): Flat rates across supported context.
- Qwen 3.8 Max 0902: 2 tier(s) on card (Singapore / International: {"deployment_scope": "International", "region": "Singapore", "cache_read_mode": "implicit"}; Global: {"deployment_scope": "Global", "cache_read_mode": "implicit"}). Calls per tier: {"Singapore / International": 39, "Global": 39}. Tier depends on deployment region/cache mode not visible in usage; low-high bounds disclosed below; tables use the upper estimate.
- Qwen 3.8 Max 0902 note (pricing file): Snapshot-specific pricing used. Explicit cache reads are $0.17 International and $0.137 Global per MTok; do not mix implicit and explicit read rates.
- Qwen 3.8 Max 0902 note (pricing file): OpenRouter route region/cache mode is not established by this reference.

### Cache-write TTL and premiums

- MiniMax M3.1 Flash: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Claude Opus 5.5: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 178,443; TTL basis: reported per-call TTL.
- DeepSeek V4.1 Flash 1017: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- DeepSeek V4 Pro: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GLM-5.3: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GPT-6 Astra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6 Luna: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Sol: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Terra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 2,442,942; TTL basis: 30m TTL rate (route rule; matches OpenRouter billed cost).
- Grok-4.7: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Kimi K3.1 Pro: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 0; TTL basis: none needed.
- Qwen 3.8 Max 0902: card has cache-write rates for TTL explicit. Cache writes in today's runs: 0; TTL basis: none needed.

### Cache semantics by route

- **claude-code:** OpenClaw/cron store only the last API call of each claude-cli turn; totals come from the Claude Code session log under ~/.claude/projects (deduped by message id). Cache writes are priced by their reported TTL (5m/1h).
- **codex:** Codex native input_tokens INCLUDES cached input; uncached = input - cached_input. Codex reports cache_write 0, which does not prove an API run would have no cache-write charge, so the estimate may be low by the cache-write premium.
- **openrouter:** Per-call usage from the OpenClaw transcript; input = uncached only (cron usage.input_tokens is the same, uncached only). For OpenAI models via OpenRouter, the uncached prompt part is billed as cache write ($1.25/M for Terra, the 30m-TTL rate; inferred from matching the provider-billed cost, not a documented TTL). Other OpenRouter providers reported cache_write 0 today.
- **xai:** Per-call xAI tokens support an API-equivalent estimate; actual xAI charges are not recorded, not zero.

## Gaps

- Qwen 3.8 Max 0902 (2026-11-01T06:06:22-05:00): tier not determinable from usage (Singapore / International / Global)

## Notes

- Input = uncached input only (excludes cache read and cache write).
- Failed or retried runs are separate rows; non-run sessions are not included.
