# AI Brief model comparison 2026-10-29: usage, API-equivalent estimates, recorded charges

Generated 2026-10-29T07:16:17-04:00 by `scripts/brief_usage_collector.py` (read-only; usage/metadata only).
Pricing: `pricing/2026-10-29/api-pricing.json` (as of 2026-10-29). Hash check against verification.json: passed (10 files).
Runs are matched to pricing entries by exact `model_ref` == run.json `expected_model` (cron job payload model for extra runs).

## 1. Token usage

| Run (ET start) | Role | Route | Billing | Status | Calls | Uncached input | Output | Cache read | Cache write | Usage check |
|---|---|---|---|---|---:|---:|---:|---:|---:|---|
| GLM-5.3 05:56 | comparison | openrouter | billed | ok | 49 | 154,139 | 28,950 | 4,005,562 | 0 | exact |
| GPT-6 Astra 06:30 | comparison | codex | subscription | ok | 25 | 150,214 | 17,164 | 2,455,680 | 0 | exact |
| GPT-6 Luna 06:19 | extra | codex | subscription | ok | 7 | 35,348 | 1,100 | 175,232 | 0 | exact |
| GPT-6 Luna 06:25 | comparison | codex | subscription | ok | 70 | 209,238 | 60,420 | 9,373,696 | 0 | exact |
| GPT-6.1 Sol 06:43 | comparison | codex | subscription | ok | 24 | 146,163 | 15,355 | 2,392,064 | 0 | exact |
| GPT-6.1 Terra 05:56 | comparison | openrouter | billed | ok | 36 | 108 | 12,434 | 432,425 | 3,224,932 | exact |
| Grok-4.7 06:53 | comparison | xai | billed | ok | 45 | - | - | - | - | - |
| Kimi K3.1 Pro 06:17 | comparison | openrouter | billed | ok | 26 | 161,043 | 17,759 | 2,618,624 | 0 | exact |
| MiniMax M3.1 Flash 06:09 | comparison | openrouter | billed | ok | 45 | 201,419 | 33,505 | 5,547,008 | 0 | exact |
| Opus 5.5 subscription 06:09 | comparison | claude-code | subscription | ok | 45 | 90 | 31,737 | 5,534,823 | 201,355 | Claude log |

## 2. API-equivalent estimates (NOT bills)

tokens x published direct-provider list rates, per call; an estimate, not a bill. Includes subscription runs. Basis: Direct provider public standard API list pricing. No subscription allocation, taxes, tools, infrastructure or negotiated discounts.

| Run (ET start) | Role | model_ref | Tiers used (calls) | API-equivalent USD | Rate source |
|---|---|---|---|---:|---|
| GLM-5.3 05:56 | comparison | `openrouter_eich/z-ai/glm-5.3` | Z.AI direct (49) | $1.3846 | https://docs.z.ai/guides/overview/pricing |
| GPT-6 Astra 06:30 | comparison | `openai/gpt-6-astra` | Standard short (25) | $4.8160 | https://developers.openai.com/api/docs/pricing |
| GPT-6 Luna 06:19 | extra | `openai/gpt-6-luna` | Standard short (7) | $0.0058 | https://developers.openai.com/api/docs/pricing |
| GPT-6 Luna 06:25 | comparison | `openai/gpt-6-luna` | Standard short (70) | $0.1449 | https://developers.openai.com/api/docs/pricing |
| GPT-6.1 Sol 06:43 | comparison | `openai/gpt-6.1-sol` | Standard short (24) | $0.6851 | https://developers.openai.com/api/docs/pricing |
| GPT-6.1 Terra 05:56 | comparison | `openrouter_terra/openai/gpt-6.1-terra` | Standard short (36) | $4.1151 | https://developers.openai.com/api/docs/pricing |
| Grok-4.7 06:53 | comparison | `xai/grok-4.7` | - | GAP | - |
| Kimi K3.1 Pro 06:17 | comparison | `openrouter_kimi/moonshotai/kimi-k3.1-pro` | Standard flat (26) | $1.0234 | https://www.kimi.ai/resources/kimi-k3-1-pro-pricing |
| MiniMax M3.1 Flash 06:09 | comparison | `openrouter_mini/minimax/minimax-m3.1-flash` | Direct flat (45) | $0.1335 | https://www.minimax.io/blog/minimax-m31f |
| Opus 5.5 subscription 06:09 | comparison | `anthropic/claude-opus-5-5` | Standard (45) | $3.3529 | https://platform.claude.com/docs/en/models/opus-5-5/overview |

**Estimate total, comparison runs: $15.6555.** All priced runs incl. extras: $15.6613. Unpriced: Grok-4.7 2026-10-29T06:53:21-04:00.

## 3. Recorded charges

OpenRouter per-generation total_cost (provider-billed) as recorded per call. Subscription runs (Codex, Claude Code) have no per-token charge.

| Run (ET start) | Role | Route | Billing | Recorded charge USD | Calls with charge |
|---|---|---|---|---:|---|
| GLM-5.3 05:56 | comparison | openrouter | billed | $0.6964 | 49/49 |
| GPT-6 Astra 06:30 | comparison | codex | subscription | none (subscription) | - |
| GPT-6 Luna 06:19 | extra | codex | subscription | none (subscription) | - |
| GPT-6 Luna 06:25 | comparison | codex | subscription | none (subscription) | - |
| GPT-6.1 Sol 06:43 | comparison | codex | subscription | none (subscription) | - |
| GPT-6.1 Terra 05:56 | comparison | openrouter | billed | $4.1151 | 36/36 |
| Grok-4.7 06:53 | comparison | xai | billed | not recorded | - |
| Kimi K3.1 Pro 06:17 | comparison | openrouter | billed | $1.0234 | 26/26 |
| MiniMax M3.1 Flash 06:09 | comparison | openrouter | billed | $0.1335 | 45/45 |
| Opus 5.5 subscription 06:09 | comparison | claude-code | subscription | none (subscription) | - |

**Recorded OpenRouter charges, comparison runs: $5.9684** (all runs: $5.9684). Incomplete per-call charge data: none. Billed routes with no recorded charge: Grok-4.7 (xai).
Estimates and charges are different quantities and are never added together.

## Pending / not finished

- AI Brief local - DeepSeek v4 Pro (`openrouter_deek/deepseek/deepseek-v4-pro`): not run yet
- AI Brief local - DeepSeek v4.1 Flash (`openrouter_flash/deepseek/deepseek-v4.1-flash-1017`): not run yet
- AI Brief local - Qwen 3.8 Max 0902 (`openrouter_qwenmax/qwen/qwen3.8-max-0902`): running

## 4. Unresolved (disclosed, not settled by these numbers)

### Pricing tiers

- MiniMax M3.1 Flash: 1 tier(s) on card (Direct flat: {}). Calls per tier: {"Direct flat": 45}. Card lists a single tier; no long-context threshold verified.
- MiniMax M3.1 Flash note (pricing file): Separate cache-write pricing is not specified in the cited announcement; an empty map does not mean free.
- Claude Opus 5.5: 1 tier(s) on card (Standard: {}). Calls per tier: {"Standard": 45}. Card lists a single tier; no long-context threshold verified.
- Claude Opus 5.5 note (pricing file): Audit aggregates cache writes without TTL split; do not assume all writes use 5m for an exact estimate.
- GLM-5.3: 1 tier(s) on card (Z.AI direct: {}). Calls per tier: {"Z.AI direct": 49}. Card lists a single tier; no long-context threshold verified.
- GLM-5.3 note (pricing file): Cache storage is limited-time free; a distinct cache-write token price is not specified on the cited rate card.
- GLM-5.3 note (pricing file): Direct Z.AI list pricing is not the DeepInfra/Fireworks OpenRouter bill.
- GPT-6 Astra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 25}.
- GPT-6 Astra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Astra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Astra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6 Luna: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 77}.
- GPT-6 Luna note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6 Luna note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6 Luna note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Sol: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 24}.
- GPT-6.1 Sol note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Sol note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Sol note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- GPT-6.1 Terra: 2 tier(s) on card (Standard short: {"prompt_tokens_lte": 272000}; Standard long: {"prompt_tokens_gt": 272000}). Calls per tier: {"Standard short": 36}.
- GPT-6.1 Terra note (pricing file): Tier is selected per request, not from total run tokens.
- GPT-6.1 Terra note (pricing file): Batch/Flex 0.5x; Fast 2x; regional/FedRAMP uplift 1.1x. Reference baseline is Standard, no regional uplift.
- GPT-6.1 Terra note (pricing file): Codex reported cache_write=0 does not prove an equivalent API execution would incur no cache-write charge.
- Kimi K3.1 Pro: 1 tier(s) on card (Standard flat: {}). Calls per tier: {"Standard flat": 26}. Card lists a single tier; no long-context threshold verified.
- Kimi K3.1 Pro note (pricing file): USD international rate card; no currency conversion from domestic CNY rates.
- Kimi K3.1 Pro note (pricing file): Flat rates across supported context.

### Cache-write TTL and premiums

- MiniMax M3.1 Flash: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- Claude Opus 5.5: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 201,355; TTL basis: reported per-call TTL.
- GLM-5.3: no cache-write price verified on the cited card (empty map is NOT zero). Cache writes in today's runs: 0.
- GPT-6 Astra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6 Luna: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Sol: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 0; TTL basis: none needed.
- GPT-6.1 Terra: card has cache-write rates for TTL 12h/30m. Cache writes in today's runs: 3,224,932; TTL basis: 30m TTL rate (route rule; matches OpenRouter billed cost).
- Kimi K3.1 Pro: card has cache-write rates for TTL 1h/5m. Cache writes in today's runs: 0; TTL basis: none needed.

### Cache semantics by route

- **claude-code:** OpenClaw/cron store only the last API call of each claude-cli turn; totals come from the Claude Code session log under ~/.claude/projects (deduped by message id). Cache writes are priced by their reported TTL (5m/1h).
- **codex:** Codex native input_tokens INCLUDES cached input; uncached = input - cached_input. Codex reports cache_write 0, which does not prove an API run would have no cache-write charge, so the estimate may be low by the cache-write premium.
- **openrouter:** Per-call usage from the OpenClaw transcript; input = uncached only (cron usage.input_tokens is the same, uncached only). For OpenAI models via OpenRouter, the uncached prompt part is billed as cache write ($1.25/M for Terra, the 30m-TTL rate; inferred from matching the provider-billed cost, not a documented TTL). Other OpenRouter providers reported cache_write 0 today.
- **xai:** xAI route recorded zero usage for every call (transcript, cron, trajectory); no tokens, no estimate, no recorded charge.

## Gaps

- Grok-4.7 (2026-10-29T06:53:21-04:00): route recorded zero usage for every call (xai); tokens unavailable

## Notes

- Input = uncached input only (excludes cache read and cache write).
- Failed or retried runs are separate rows; non-run sessions are not included.
