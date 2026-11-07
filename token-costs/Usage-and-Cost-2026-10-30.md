# AI Brief model comparison 2026-10-30: usage, API-equivalent estimates, recorded charges

Generated 2026-10-30T12:40:26-04:00 by `scripts/brief_usage_collector.py` (read-only; usage/metadata only).
Pricing: `pricing/2026-10-29/api-pricing.json` (as of 2026-10-29, FALLBACK to earlier date). Hash check against verification.json: passed (10 files).
Runs are matched to pricing entries by exact `model_ref` == run.json `expected_model` (cron job payload model for extra runs).

## 1. Token usage

| Model | Calls | Uncached input | Output | Cache read | Cache write | API Cost* |
|---|---:|---:|---:|---:|---:|---:|
| DeepSeek v4 Pro | 42 | 288,444 | 67,399 | 3,040,256 | 0 | $0.3907 |
| DeepSeek v4.1 Flash | 76 | 157,261 | 69,109 | 6,621,440 | 0 | $0.0849 |
| GLM-5.3 | 41 | 97,522 | 23,226 | 2,470,387 | 0 | $0.8810 |
| GPT-6 Astra | 27 | 265,227 | 16,912 | 2,618,752 | 0 | $6.1166 |
| GPT-6 Luna | 47 | 146,492 | 25,278 | 4,554,112 | 0 | $0.0728 |
| GPT-6.1 Sol | 21 | 120,115 | 11,803 | 1,659,776 | 0 | $0.5242 |
| GPT-6.1 Terra | 34 | 102 | 12,183 | 407,715 | 3,229,391 | $4.1181 |
| Grok-4.7 | 37 | 386,559 | 63,855 | 4,211,456 | 0 | $3.3703 |
| Kimi K3.1 Pro | 28 | 113,204 | 15,609 | 2,090,752 | 0 | $0.8006 |
| MiniMax M3.1 Flash | 41 | 164,769 | 23,087 | 3,913,856 | 0 | $0.0973 |
| Opus 5.5 | 44 | 88 | 31,179 | 4,976,640 | 169,254 | $2.9733 |
| Qwen 3.8 Max 0902 | 48 | 190,542 | 51,108 | 5,060,736 | 0 | $1.9529 |

*API Cost = API-equivalent estimated cost in USD, calculated from token usage at published API list rates, including subscription-backed runs. It is not an actual bill. For Qwen, the higher available estimate is used in the tables and estimate totals; the deployment tier remains unverified. Other ranges reflect unresolved pricing tiers.


## 2. API-equivalent estimates (NOT bills)

tokens x published direct-provider list rates, per call; an estimate, not a bill. Includes subscription runs. Basis: Direct provider public standard API list pricing. No subscription allocation, taxes, tools, infrastructure or negotiated discounts.

| Run (ET start) | model_ref | Tiers used (calls) | API Cost* |
|---|---|---|---:|
| DeepSeek v4 Pro 09:45 | `openrouter_deek/deepseek/deepseek-v4-pro` | [Off-peak (42)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.3907 |
| DeepSeek v4.1 Flash 09:00 | `openrouter_flash/deepseek/deepseek-v4.1-flash-1017` | [Off-peak (76)](https://api-docs.deepseek.com/quick_start/pricing/) | $0.0849 |
| GLM-5.3 08:50 | `openrouter_eich/z-ai/glm-5.3` | [Z.AI direct (41)](https://docs.z.ai/guides/overview/pricing) | $0.8810 |
| GPT-6 Astra 08:50 | `openai/gpt-6-astra` | [Standard short (27)](https://developers.openai.com/api/docs/pricing) | $6.1166 |
| GPT-6 Luna 08:33 | `openai/gpt-6-luna` | [Standard short (47)](https://developers.openai.com/api/docs/pricing) | $0.0728 |
| GPT-6.1 Sol 08:50 | `openai/gpt-6.1-sol` | [Standard short (21)](https://developers.openai.com/api/docs/pricing) | $0.5242 |
| GPT-6.1 Terra 08:33 | `openrouter_terra/openai/gpt-6.1-terra` | [Standard short (34)](https://developers.openai.com/api/docs/pricing) | $4.1181 |
| Grok-4.7 09:45 | `xai/grok-4.7` | [Standard long (1), Standard short (36)](https://docs.x.ai/developers/pricing) | $3.3703 |
| Kimi K3.1 Pro 09:00 | `openrouter_kimi/moonshotai/kimi-k3.1-pro` | [Standard flat (28)](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing) | $0.8006 |
| MiniMax M3.1 Flash 08:33 | `openrouter_mini/minimax/minimax-m3.1-flash` | [Direct flat (41)](https://www.minimax.io/blog/minimax-m31f) | $0.0973 |
| Opus 5.5 08:33 | `anthropic/claude-opus-5-5` | [Standard (44)](https://platform.claude.com/docs/en/models/opus-5-5/overview) | $2.9733 |
| Qwen 3.8 Max 0902 09:00 | `openrouter_qwenmax/qwen/qwen3.8-max-0902` | [Global (48), Singapore / International (48)](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max) | $1.9529 |

**Estimate total, comparison runs: $21.3827.** All priced runs incl. extras: $21.3827. Unpriced: none.

## 3. Recorded charges

OpenRouter per-generation total_cost (provider-billed) as recorded per call. Subscription runs (Codex, Claude Code) have no per-token charge.

| Run (ET start) | Recorded charge USD | Calls with charge |
|---|---:|---|
| DeepSeek v4 Pro 09:45 | $1.0266 | 42/42 |
| DeepSeek v4.1 Flash 09:00 | $0.0552 | 76/76 |
| GLM-5.3 08:50 | $0.8810 | 41/41 |
| GPT-6 Astra 08:50 | none (subscription) | - |
| GPT-6 Luna 08:33 | none (subscription) | - |
| GPT-6.1 Sol 08:50 | none (subscription) | - |
| GPT-6.1 Terra 08:33 | $4.1181 | 34/34 |
| Grok-4.7 09:45 | not recorded | - |
| Kimi K3.1 Pro 09:00 | $0.8006 | 28/28 |
| MiniMax M3.1 Flash 08:33 | $0.0973 | 41/41 |
| Opus 5.5 08:33 | none (subscription) | - |
| Qwen 3.8 Max 0902 09:00 | $1.9529 | 48/48 |

**Recorded OpenRouter charges, comparison runs: $8.9317** (all runs: $8.9317). Incomplete per-call charge data: none. Billed routes with no recorded charge: Grok-4.7 (xai).
Estimates and charges are different quantities and are never added together.

## 4. Unresolved (disclosed, not settled by these numbers)

### Pricing tiers

- MiniMax M3.1 Flash: 1 tier(s) on card (Direct flat: {}). Calls per tier: {"Direct flat": 41}. Card lists a single tier; no long-context threshold verified.
- MiniMax M3.1 Flash note (pricing file): Separate cache-write pricing is not specified in the cited announcement; an empty map does not mean free.
- Claude Opus 5.5: 1 tier(s) on card (Standard: {}). Calls per tier: {"Standard": 44}. Card lists a single tier; no long-context threshold verified.
- Claude Opus 5.5 note (pricing file): Audit aggregates cache writes without TTL split; do not assume all writes use 5m for an exact estimate.
- DeepSeek V4.1 Flash 1017: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 76}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4.1 Flash 1017 note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4.1 Flash 1017 note (pricing file): No separate cache-write price on cited card.
- DeepSeek V4 Pro: 2 tier(s) on card (Peak: {"schedule": "Mon-Fri 01:00-04:00 and 06:00-10:00 UTC, excluding Chinese public holidays"}; Off-peak: {"schedule": "All other times"}). Calls per tier: {"Off-peak": 42}. Peak/off-peak chosen from call time in UTC; the Chinese-public-holiday exception is NOT evaluated.
- DeepSeek V4 Pro note (pricing file): Current pricing table explicitly distinguishes V4-Pro-0813 and V4.1-Flash-1017. Earlier phase-out announcement disagrees; verify returned execution model before attributing a direct-endpoint run.
- DeepSeek V4 Pro note (pricing file): No separate cache-write price on cited card.
- GLM-5.3: 1 tier(s) on card (Z.AI direct: {}). Calls per tier: {"Z.AI direct": 41}. Card lists a single tier; no long-context threshold verified.
- GLM-5.3 note (pricing file): Cache storage is limited-time free; a distinct cache-write token price is not specified on the cited rate card.
- GLM-5.3 note (pricing file): Direct Z.AI list pricing is not the DeepInfra/Fireworks OpenRouter bill.
- GPT-6 Astra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 27}.
- GPT-6 Astra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Astra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Astra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6 Luna: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 47}.
- GPT-6 Luna note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Luna note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Luna note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Sol: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 21}.
- GPT-6.1 Sol note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Sol note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Sol note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Terra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 34}.
- GPT-6.1 Terra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Terra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Terra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- Grok-4.7: 2 tier(s) on card (Standard short: {"prompt_tokens_lt": 200000}; Standard long: {"prompt_tokens_gte": 200000}). Calls per tier: {"Standard short": 36, "Standard long": 1}.
- Grok-4.7 note (pricing file): Global endpoint baseline; US regional endpoint 1.1x; Priority 2x; Batch 0.8x.
- Grok-4.7 note (pricing file): No separate cache-write price on cited card.
- Kimi K3.1 Pro: 1 tier(s) on card (Standard flat: {}). Calls per tier: {"Standard flat": 28}. Card lists a single tier; no long-context threshold verified.
- Kimi K3.1 Pro note (pricing file): USD international rate card; no currency conversion from domestic CNY rates.
- Kimi K3.1 Pro note (pricing file): Flat rates across supported context.
- Qwen 3.8 Max 0902: 2 tier(s) on card (Singapore / International: {"deployment_scope": "International", "region": "Singapore", "cache_read_mode": "implicit"}; Global: {"deployment_scope": "Global", "cache_read_mode": "implicit"}). Calls per tier: {"Singapore / International": 48, "Global": 48}. Tier depends on deployment region/cache mode not visible in usage; reported as a low-high range.
- Qwen 3.8 Max 0902 note (pricing file): Snapshot-specific pricing used. Explicit cache reads are $0.17 International and $0.137 Global per MTok; do not mix implicit and explicit read rates.
- Qwen 3.8 Max 0902 note (pricing file): OpenRouter route region/cache mode is not established by this reference.

### Cache-write TTL and premiums

- MiniMax M3.1 Flash: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Claude Opus 5.5: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 169,254; TTL basis: reported per-call TTL.
- DeepSeek V4.1 Flash 1017: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- DeepSeek V4 Pro: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GLM-5.3: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GPT-6 Astra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6 Luna: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Sol: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Terra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 3,229,391; TTL basis: 30m TTL rate (route rule; matches OpenRouter billed cost).
- Grok-4.7: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Kimi K3.1 Pro: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 0; TTL basis: none needed.
- Qwen 3.8 Max 0902: card has cache-write rates for TTL explicit. Cache writes in today's runs: 0; TTL basis: none needed.

### Cache semantics by route

- **claude-code:** OpenClaw/cron store only the last API call of each claude-cli turn; totals come from the Claude Code session log under ~/.claude/projects (deduped by message id). Cache writes are priced by their reported TTL (5m/1h).
- **codex:** Codex native input_tokens INCLUDES cached input; uncached = input - cached_input. Codex reports cache_write 0, which does not prove an API run would have no cache-write charge, so the estimate may be low by the cache-write premium.
- **openrouter:** Per-call usage from the OpenClaw transcript; input = uncached only (cron usage.input_tokens is the same, uncached only). For OpenAI models via OpenRouter, the uncached prompt part is billed as cache write ($1.25/M for Terra, the 30m-TTL rate; inferred from matching the provider-billed cost, not a documented TTL). Other OpenRouter providers reported cache_write 0 today.
- **xai:** xAI route recorded zero usage for every call (transcript, cron, trajectory); no tokens, no estimate, no recorded charge.

## Gaps

- Qwen 3.8 Max 0902 (2026-10-30T09:00:46-04:00): tier not determinable from usage (Singapore / International / Global)

## Notes

- Input = uncached input only (excludes cache read and cache write).
- Failed or retried runs are separate rows; non-run sessions are not included.
