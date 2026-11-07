# AI Brief model comparison 2026-10-31: usage, API-equivalent estimates, recorded charges

Generated 2026-10-31T11:45:16-04:00 by `scripts/brief_usage_collector.py` (read-only; usage/metadata only).
Pricing: `pricing/2026-10-29/api-pricing.json` (as of 2026-10-29, FALLBACK to earlier date). Hash check against verification.json: passed (10 files).
Runs are matched to pricing entries by exact `model_ref` == run.json `expected_model` (cron job payload model for extra runs).

## 1. Token usage

| Model | Calls | Uncached input | Output | Cache read | Cache write | API Cost* |
|---|---:|---:|---:|---:|---:|---:|
| DeepSeek v4 Pro | 54 | 246,520 | 136,119 | 5,234,432 | 0 | $0.55 |
| DeepSeek v4.1 Flash | 85 | 216,742 | 123,374 | 10,593,408 | 0 | $0.14 |
| GLM-5.3 | 42 | 125,472 | 23,708 | 3,402,752 | 0 | $1.16 |
| GPT-6 Astra | 29 | 145,725 | 18,087 | 3,111,680 | 0 | $5.47 |
| GPT-6 Luna | 42 | 154,748 | 34,479 | 4,600,704 | 0 | $0.08 |
| GPT-6.1 Sol | 25 | 150,976 | 13,583 | 2,562,176 | 0 | $0.69 |
| GPT-6.1 Terra | 32 | 96 | 10,994 | 388,771 | 2,464,419 | $3.16 |
| Grok-4.7 | 42 | 301,132 | 65,199 | 5,736,448 | 0 | $6.11 |
| Kimi K3.1 Pro | 28 | 144,731 | 16,200 | 2,566,144 | 0 | $0.96 |
| MiniMax M3.1 Flash | 59 | 273,064 | 46,576 | 10,433,408 | 0 | $0.23 |
| Opus 5.5 | 51 | 102 | 42,935 | 6,324,500 | 215,242 | $3.85 |
| Qwen 3.8 Max 0902 | 48 | 204,953 | 61,252 | 5,491,072 | 0 | $2.15 |

*API Cost = API-equivalent estimated cost in USD, calculated from token usage at published API list rates, including subscription-backed runs. It is not an actual bill. For Qwen, the higher available estimate is used in the tables and estimate totals; the deployment tier remains unverified. Other ranges reflect unresolved pricing tiers.


## 2. API-equivalent estimates (NOT bills)

tokens x published direct-provider list rates, per call; an estimate, not a bill. Includes subscription runs. Basis: Direct provider public standard API list pricing. No subscription allocation, taxes, tools, infrastructure or negotiated discounts.

| Run (ET start) | model_ref | Tiers used (calls) | API Cost* |
|---|---|---|---:|
| DeepSeek v4 Pro 10:52 | `openrouter_deek/deepseek/deepseek-v4-pro` | [Off-peak (54)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.55 |
| DeepSeek v4.1 Flash 10:52 | `openrouter_flash/deepseek/deepseek-v4.1-flash-1017` | [Off-peak (85)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.14 |
| GLM-5.3 10:06 | `openrouter_eich/z-ai/glm-5.3` | [Z.AI direct (42)](https://docs.z.ai/guides/overview/pricing) | $1.16 |
| GPT-6 Astra 10:30 | `openai/gpt-6-astra` | [Standard short (29)](https://developers.openai.com/api/docs/pricing) | $5.47 |
| GPT-6 Luna 10:06 | `openai/gpt-6-luna` | [Standard short (42)](https://developers.openai.com/api/docs/pricing) | $0.08 |
| GPT-6.1 Sol 10:30 | `openai/gpt-6.1-sol` | [Standard short (25)](https://developers.openai.com/api/docs/pricing) | $0.69 |
| GPT-6.1 Terra 10:06 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (32)](https://developers.openai.com/api/docs/pricing) | $3.16 |
| Grok-4.7 10:52 | `xai/grok-4.7` | [Standard long (18), Standard short (24)](https://docs.x.ai/developers/pricing) | $6.11 |
| Kimi K3.1 Pro 10:30 | `openrouter_kimi/moonshotai/kimi-k3.1-pro` | [Standard flat (28)](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing) | $0.96 |
| MiniMax M3.1 Flash 10:06 | `openrouter_mini/minimax/minimax-m3.1-flash` | [Direct flat (59)](https://www.minimax.io/blog/minimax-m31f) | $0.23 |
| Opus 5.5 10:30 | `anthropic/claude-opus-5-5` | [Standard (51)](https://platform.claude.com/docs/en/models/opus-5-5/overview) | $3.85 |
| Qwen 3.8 Max 0902 10:52 | `openrouter_qwenmax/qwen/qwen3.8-max-0902` | [Global (48), Singapore / International (48)](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | $2.15 |

**Estimate total, comparison runs: $24.54.** All priced runs incl. extras: $24.54. Unpriced: none.

## 3. Recorded charges

OpenRouter per-generation total_cost (provider-billed) as recorded per call. Subscription runs (Codex, Claude Code) have no per-token charge.

| Run (ET start) | Recorded charge USD | Calls with charge |
|---|---:|---|
| DeepSeek v4 Pro 10:52 | $1.53 | 54/54 |
| DeepSeek v4.1 Flash 10:52 | $0.09 | 85/85 |
| GLM-5.3 10:06 | $0.58 | 42/42 |
| GPT-6 Astra 10:30 | none (subscription) | - |
| GPT-6 Luna 10:06 | none (subscription) | - |
| GPT-6.1 Sol 10:30 | none (subscription) | - |
| GPT-6.1 Terra 10:06 | $3.16 | 32/32 |
| Grok-4.7 10:52 | not recorded | - |
| Kimi K3.1 Pro 10:30 | $0.96 | 28/28 |
| MiniMax M3.1 Flash 10:06 | $0.23 | 59/59 |
| Opus 5.5 10:30 | none (subscription) | - |
| Qwen 3.8 Max 0902 10:52 | $2.15 | 48/48 |

**Recorded OpenRouter charges, comparison runs: $8.69** (all runs: $8.69). Incomplete per-call charge data: none. Billed routes with no recorded charge: Grok-4.7 (xai).
Estimates and charges are different quantities and are never added together.

## 4. Unresolved (disclosed, not settled by these numbers)

### Pricing tiers

- MiniMax M3.1 Flash: 1 tier(s) on card (Direct flat: {}). Calls per tier: {"Direct flat": 59}. Card lists a single tier; no long-context threshold verified.
- MiniMax M3.1 Flash note (pricing file): Separate cache-write pricing is not specified in the cited announcement; an empty map does not mean free.
- Claude Opus 5.5: 1 tier(s) on card (Standard: {}). Calls per tier: {"Standard": 51}. Card lists a single tier; no long-context threshold verified.
- Claude Opus 5.5 note (pricing file): Audit aggregates cache writes without TTL split; do not assume all writes use 5m for an exact estimate.
- DeepSeek V4.1 Flash 1017: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 85}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4.1 Flash 1017 note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4.1 Flash 1017 note (pricing file): No separate cache-write price on cited card.
- DeepSeek V4 Pro: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 54}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4 Pro note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4 Pro note (pricing file): No separate cache-write price on cited card.
- GLM-5.3: 1 tier(s) on card (Z.AI direct: {}). Calls per tier: {"Z.AI direct": 42}. Card lists a single tier; no long-context threshold verified.
- GLM-5.3 note (pricing file): Cache storage is limited-time free; a distinct cache-write token price is not specified on the cited rate card.
- GLM-5.3 note (pricing file): Direct Z.AI list pricing is not the DeepInfra/Fireworks OpenRouter bill.
- GPT-6 Astra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 29}.
- GPT-6 Astra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Astra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Astra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6 Luna: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 42}.
- GPT-6 Luna note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Luna note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Luna note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Sol: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 25}.
- GPT-6.1 Sol note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Sol note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Sol note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Terra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 32}.
- GPT-6.1 Terra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Terra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Terra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- Grok-4.7: 2 tier(s) on card (Standard short: {"prompt_tokens_lt": 200000}; Standard long: {"prompt_tokens_gte": 200000}). Calls per tier: {"Standard short": 24, "Standard long": 18}.
- Grok-4.7 note (pricing file): Global endpoint baseline; US regional endpoint 1.1x; Priority 2x; Batch 0.8x.
- Grok-4.7 note (pricing file): No separate cache-write price on cited card.
- Kimi K3.1 Pro: 1 tier(s) on card (Standard flat: {}). Calls per tier: {"Standard flat": 28}. Card lists a single tier; no long-context threshold verified.
- Kimi K3.1 Pro note (pricing file): USD international rate card; no currency conversion from domestic CNY rates.
- Kimi K3.1 Pro note (pricing file): Flat rates across supported context.
- Qwen 3.8 Max 0902: 2 tier(s) on card (Singapore / International: {"deployment_scope": "International", "region": "Singapore", "cache_read_mode": "implicit"}; Global: {"deployment_scope": "Global", "cache_read_mode": "implicit"}). Calls per tier: {"Singapore / International": 48, "Global": 48}. Tier depends on deployment region/cache mode not visible in usage; low-high bounds are retained in the audit JSON, while tables use the higher estimate.
- Qwen 3.8 Max 0902 note (pricing file): Snapshot-specific pricing used. Explicit cache reads are $0.17 International and $0.137 Global per MTok; do not mix implicit and explicit read rates.
- Qwen 3.8 Max 0902 note (pricing file): OpenRouter route region/cache mode is not established by this reference.

### Cache-write TTL and premiums

- MiniMax M3.1 Flash: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Claude Opus 5.5: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 215,242; TTL basis: reported per-call TTL.
- DeepSeek V4.1 Flash 1017: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- DeepSeek V4 Pro: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GLM-5.3: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GPT-6 Astra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6 Luna: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Sol: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Terra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 2,464,419; TTL basis: 30m TTL rate (route rule; matches OpenRouter billed cost).
- Grok-4.7: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Kimi K3.1 Pro: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 0; TTL basis: none needed.
- Qwen 3.8 Max 0902: card has cache-write rates for TTL explicit. Cache writes in today's runs: 0; TTL basis: none needed.

### Cache semantics by route

- **claude-code:** OpenClaw/cron store only the last API call of each claude-cli turn; totals come from the Claude Code session log under ~/.claude/projects (deduped by message id). Cache writes are priced by their reported TTL (5m/1h).
- **codex:** Codex native input_tokens INCLUDES cached input; uncached = input - cached_input. Codex reports cache_write 0, which does not prove an API run would have no cache-write charge, so the estimate may be low by the cache-write premium.
- **openrouter:** Per-call usage from the OpenClaw transcript; input = uncached only (cron usage.input_tokens is the same, uncached only). For OpenAI models via OpenRouter, the uncached prompt part is billed as cache write ($1.25/M for Terra, the 30m-TTL rate; inferred from matching the provider-billed cost, not a documented TTL). Other OpenRouter providers reported cache_write 0 today.
- **xai:** Per-call xAI token usage is available for this run and supports an API-equivalent estimate. The gateway does not record an actual xAI billed charge; do not treat that missing charge as zero.

## Gaps

- Qwen 3.8 Max 0902 (2026-10-31T10:52:13-04:00): tier not determinable from usage (Singapore / International / Global)

## Notes

- Input = uncached input only (excludes cache read and cache write).
- Failed or retried runs are separate rows; non-run sessions are not included.
