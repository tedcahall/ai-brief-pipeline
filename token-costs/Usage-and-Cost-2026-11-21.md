# Token Usage and Cost - 2026-11-21

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gpt-6-2-astra | 795,929 | $1.68 | 150,860 | 5,325 | 639,744 | 0 | 06:59:20 | 18 |
| gpt-6-astra | 936,254 | $1.93 | 78,613 | 5,929 | 851,712 | 0 | 05:31:37 | 16 |
| gemini-4-neon | 2,141,249 | $1.40 | 187,483 | 36,584 | 1,917,182 | 0 | 07:10:59 | 23 |
| gemini-4-hydrogen | 2,174,042 | $0.66 | 184,303 | 31,216 | 1,958,523 | 0 | 07:15:25 | 25 |
| gpt-6-1-terra | 2,284,763 | $0.25 | 99,916 | 9,231 | 2,175,616 | 0 | 05:43:14 | 30 |
| gpt-6-1-sol | 3,541,330 | $0.81 | 151,536 | 17,378 | 3,372,416 | 0 | 05:35:17 | 30 |
| gpt-6-2-sol | 3,546,883 | $1.22 | 371,214 | 16,501 | 3,159,168 | 0 | 07:02:55 | 38 |
| grok-4-7 | 4,339,108 | $2.84 | 211,231 | 64,517 | 4,063,360 | 0 | 06:34:15 | 37 |
| gemini-4-argon | 4,394,363 | $1.48 (upper estimate) | 261,844 | 54,728 | 4,077,791 | 0 | 05:59:50 | 35 |
| glm-5-3 | 4,518,272 | $1.45 | 166,624 | 21,344 | 4,330,304 | 0 | 06:17:40 | 65 |
| opus-5-5 | 4,531,372 | $2.74 | 70 | 31,779 | 4,345,084 | 154,439 | 05:52:15 | 35 |
| kimi-k3-1-pro | 4,795,725 | $1.58 | 189,659 | 28,018 | 4,578,048 | 0 | 06:12:38 | 38 |
| qwen-3-8-max-0902 | 4,898,276 | $1.76 | 157,002 | 45,594 | 4,695,680 | 0 | 07:20:05 | 55 |
| deepseek-v4-pro | 4,918,672 | $0.34 | 229,773 | 41,219 | 4,647,680 | 0 | 05:59:06 | 65 |
| fable-5-2 | 5,295,620 | $6.43 | 64 | 38,671 | 5,014,525 | 242,360 | 05:45:25 | 32 |
| gpt-6-luna | 5,672,016 | $0.09 | 182,693 | 33,067 | 5,456,256 | 0 | 05:47:48 | 45 |
| sonnet-5-5 | 6,218,715 | $1.72 | 86 | 30,719 | 5,983,807 | 204,103 | 07:03:47 | 43 |
| haiku-5-5 | 6,281,485 | $0.55 | 82 | 58,354 | 5,998,296 | 224,753 | 07:10:08 | 41 |
| fable-5-1 | 7,800,639 | $11.18 | 1,090 | 65,972 | 7,433,162 | 300,415 | 05:31:37 | 35 |
| qwen-4-max | 8,337,454 | $1.21 | 280,676 | 56,010 | 8,000,768 | 0 | 06:39:40 | 55 |
| minimax-m3-1-flash | 8,695,946 | $0.18 | 170,919 | 50,275 | 8,474,752 | 0 | 06:27:00 | 63 |
| gemini-4-carbon | 9,096,359 | $2.33 | 368,669 | 72,503 | 8,655,187 | 0 | 07:18:57 | 39 |
| deepseek-v4-1-flash-1017 | 13,757,815 | $0.13 | 177,415 | 111,088 | 13,469,312 | 0 | 06:47:12 | 117 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| gemini-4-argon | Not recorded | Not applicable |
| qwen-3-8-max-0902 | $1.76 | 55/55 |
| qwen-4-max | $1.21 | 55/55 |
| fable-5-2 | No per-token charge | Not applicable |
| gemini-4-neon | Not recorded | Not applicable |
| fable-5-1 | No per-token charge | Not applicable |
| gemini-4-hydrogen | Not recorded | Not applicable |
| glm-5-3 | $0.66 | 65/65 |
| gemini-4-carbon | Not recorded | Not applicable |
| kimi-k3-1-pro | $1.58 | 38/38 |
| opus-5-5 | No per-token charge | Not applicable |
| deepseek-v4-1-flash-1017 | $0.13 | 117/117 |
| grok-4-7 | Not recorded | Not applicable |
| sonnet-5-5 | No per-token charge | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| gpt-6-2-sol | No per-token charge | Not applicable |
| minimax-m3-1-flash | $0.18 | 63/63 |
| deepseek-v4-pro | $0.46 | 65/65 |
| gpt-6-luna | No per-token charge | Not applicable |
| gpt-6-2-astra | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 3,621,822 |
| Output | 926,022 |
| Cache Read | 113,298,373 |
| Cache Write | 1,126,070 |
| Calls with available telemetry | 980 |
| API estimate subtotal (available telemetry) | $42.49 |
| Recorded OpenRouter charges | $5.98 |
| Models with unavailable estimates | gemini-4-argon |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| gemini-4-carbon (earlier failed attempt, excluded) | 8,521,795 | $2.23 | 421,163 | 58,328 | 8,042,304 | 0 | 06:25:54 | 37 |

| Session | Job label | Status | Calls | Reason |
|---|---|---|---|---|

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 23 final editions of the 2026-11-21 cohort.
Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
One earlier failed attempt of gemini-4-carbon (job cb24593a, Google PROHIBITED_CONTENT stop) was collected and is bound to the coordinator-recorded attempts array; it is excluded from totals and shown separately. Every other collected run binds one-to-one to a coordinator-selected final edition.
Qwen 3.8 Max 0902 uses the higher regional estimate for its displayed cost (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
qwen-4-max is priced from the day-appropriate snapshot pricing/2026-11-21T080621351982Z/api-pricing.json (canonical key qwen4-max): $1.425 input / $4.275 output / $0.07125 cache read / $1.78125 cache write (TTL unspecified) per million tokens (OpenRouter rates lowered 5% from the 2026-11-16 debut snapshot per the daily pricing check). Cache-write TTL is unspecified by the source and is not claimed as a verified 5m/1h schedule. Qwen 3.8 regional upper-estimate rules are not applied to Qwen4-Max.
GPT-6.2 Astra and GPT-6.2 Sol are priced from the same verified snapshot (canonical keys gpt-6.2-astra and gpt-6.2-sol): Astra Standard short $8 input / $40 output / $0.40 cache read / $10 (30m) cache write per million tokens, Sol Standard short $2 / $10 / $0.10 / $2.50 (30m), with Standard long tiers above 272,000 prompt tokens per request; 30m/12h cache-write distinctions are preserved and neither predecessor pricing is substituted.
Gemini 4 Neon is priced from the same verified snapshot (canonical key gemini-4-neon): Standard $3 input / $15 output including thinking / $0.15 implicit cache read per million tokens. Explicit caching is unsupported; the empty cache-write map is not a zero price. No Batch/Flex/Priority rates are substituted for Standard usage.
*Pricing uses the collector-selected day-appropriate snapshot (pricing/2026-11-21T080621351982Z/api-pricing.json, as of 2026-11-21); pricing verification passed. Verify official validity dates before later runs; never reprice historical days.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the twenty-three final HTML editions, bound by terminal-record session ID, not latest-by-name. No earlier or unbound sessions were collected this date. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
The twenty-three collected final runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Carbon introductory Standard rates apply through November 30, 2026 (scheduled December increases are not current rates); Hydrogen and Neon Standard rates include thinking; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-21T07:46:22-05:00. Pricing source: pricing/2026-11-21T080621351982Z/api-pricing.json, as of 2026-11-21; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 17, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent subtotal (models with single-tier estimates): $42.49; upper-bound additions from tier-indeterminate models (Qwen regional upper estimates) bring the batch upper bound to $46.94. Recorded OpenRouter charges for the final editions: $5.98. Pricing snapshot age at report date: 0 day(s). Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics

- Gemini 4 Argon (2026-11-21T05:59:50-05:00): tier not determinable from usage (Introductory Standard)

## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-21T080621351982Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- qwen-4-max: [qwen4-max](https://openrouter.ai/api/v1/models/qwen/qwen4-max/endpoints)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-neon: [gemini-4-neon](https://aistudio.google.com/docs/pricing)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- gemini-4-hydrogen: [gemini-4-hydrogen](https://aistudio.google.com/docs/pricing)
- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- gemini-4-carbon: [gemini-4-carbon](https://aistudio.google.com/docs/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-2-sol: [gpt-6.2-sol](https://developers.openai.com/api/docs/pricing)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)
- gpt-6-2-astra: [gpt-6.2-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-21/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-21.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

