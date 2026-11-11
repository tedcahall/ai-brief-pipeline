# Token Usage and Cost - 2026-11-11

## Final-edition token usage

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|
| kimi-k3-1-pro | 2,234,594 | $0.80 | 119,338 | 13,880 | 2,101,376 | 0 | 06:14:03 | 26 |
| gpt-6-astra | 2,322,735 | $4.15 | 139,368 | 11,719 | 2,171,648 | 0 | 05:31:09 | 23 |
| gpt-6-1-terra | 2,372,865 | $0.26 | 97,382 | 9,371 | 2,266,112 | 0 | 05:44:38 | 33 |
| sonnet-5-5 | 2,995,627 | $1.18 | 52 | 21,168 | 2,802,449 | 171,958 | 06:53:54 | 26 |
| gpt-6-1-sol | 3,001,335 | $0.73 | 152,429 | 14,474 | 2,834,432 | 0 | 05:37:39 | 26 |
| gemini-4-argon | 4,009,067 | $1.52 | 349,450 | 45,819 | 3,613,798 | 0 | 06:43:22 | 37 |
| opus-5-5 | 4,468,787 | $2.83 | 74 | 30,587 | 4,267,340 | 170,786 | 05:47:28 | 37 |
| deepseek-v4-pro | 4,474,132 | $0.36 | 155,477 | 82,111 | 4,236,544 | 0 | 05:53:18 | 49 |
| gpt-6-luna | 4,683,266 | $0.08 | 177,739 | 35,255 | 4,470,272 | 0 | 05:49:22 | 40 |
| glm-5-3 | 4,714,013 | $1.57 | 227,283 | 19,914 | 4,466,816 | 0 | 07:00:48 | 48 |
| fable-5-1 | 5,267,532 | $9.08 | 834 | 43,505 | 4,940,194 | 282,999 | 05:31:09 | 27 |
| grok-4-7 | 5,537,090 | $3.51 | 219,467 | 74,871 | 5,242,752 | 0 | 06:37:45 | 46 |
| fable-5-2 | 5,564,594 | $6.45 | 66 | 35,885 | 5,281,332 | 247,311 | 05:41:00 | 33 |
| qwen-3-8-max-0902 | 5,711,461 | $2.15 | 185,882 | 68,555 | 5,457,024 | 0 | 06:01:41 | 53 |
| haiku-5-5 | 6,064,546 | $0.50 | 90 | 56,021 | 5,813,676 | 194,759 | 06:57:58 | 45 |
| deepseek-v4-1-flash-1017 | 6,298,242 | $0.08 | 142,682 | 62,248 | 6,093,312 | 0 | 06:33:26 | 67 |
| minimax-m3-1-flash | 25,376,839 | $0.51 | 220,021 | 164,818 | 24,992,000 | 0 | 06:18:14 | 110 |

## Final-edition recorded charges

| Model | Recorded charge | Calls with recorded charge |
|---|---|---|
| glm-5-3 | $1.50 | 48/48 |
| fable-5-2 | No per-token charge | Not applicable |
| opus-5-5 | No per-token charge | Not applicable |
| deepseek-v4-pro | $1.08 | 49/49 |
| fable-5-1 | No per-token charge | Not applicable |
| grok-4-7 | Not recorded | Not applicable |
| gemini-4-argon | Not recorded | Not applicable |
| qwen-3-8-max-0902 | $2.15 | 53/53 |
| deepseek-v4-1-flash-1017 | $0.05 | 67/67 |
| minimax-m3-1-flash | $0.51 | 110/110 |
| sonnet-5-5 | No per-token charge | Not applicable |
| gpt-6-astra | No per-token charge | Not applicable |
| gpt-6-1-sol | No per-token charge | Not applicable |
| gpt-6-1-terra | No per-token charge | Not applicable |
| haiku-5-5 | No per-token charge | Not applicable |
| kimi-k3-1-pro | $0.80 | 26/26 |
| gpt-6-luna | No per-token charge | Not applicable |

## Totals

| Measure | Value |
|---|---|
| Input Uncached | 2,187,634 |
| Output | 790,201 |
| Cache Read | 91,051,077 |
| Cache Write | 1,067,813 |
| Calls with available telemetry | 726 |
| API estimate subtotal (available telemetry) | $35.74 |
| Recorded OpenRouter charges | $6.09 |
| Models with unavailable telemetry/estimates | None |

## Earlier / diagnostic attempts

| Model | Total tokens | API Cost* | Uncached input | Output | Cache read | Cache write | Start ET | Calls |
|---|---|---|---|---|---|---|---|---|

## Definitions and limits

*API Cost is an estimate calculated from token usage at published API list rates, not a bill. Estimates include subscription-backed models. Recorded OpenRouter charges are separate actual provider-billed amounts. Do not add estimates to recorded charges. Subscription runs have no per-token charge.
Claude-code models (Opus, Fable, Sonnet, Haiku) are collected from Claude Code native session logs, deduplicated by message ID. Totals cover all 17 final editions of the 2026-11-11 batch.

Total tokens = uncached input + output + cache read + cache write, summed across calls (including repeated cached context). Input means uncached input only. Cache-read/write tokens are separate. Output is the collector output counter, not a fabricated visible-text word count. Zero is retained only where the collector records it; unavailable counters are not replaced with estimates.
Qwen uses the higher regional estimate for its displayed cost and totals, as requested (its deployment tier is not determinable from usage this date). This is a conservative estimate, not a claim about deployment region. xAI per-call billed charges are not recorded. Cache-write pricing/TTL gaps and unverifiable tier selections remain in the collector audit.
*pricing uses the fresh collector snapshot for this date (pricing/2026-11-11T120252913396Z), verified against saved source snapshots with no earlier-date fallback; all seventeen model identities resolved, including anthropic/claude-fable-5-2.*

## Selection and collection

Primary tables contain the exact coordinator-attempted run for each of the seventeen final HTML editions, bound by terminal-record session ID, not latest-by-name. Earlier attempts appear separately and are excluded from primary totals. The final-edition token usage table is sorted by total tokens, fewest to most, with alphabetical ties and unavailable totals last.
No earlier or diagnostic attempts exist for this date: all seventeen collected runs bind one-to-one to the coordinator-selected final editions. Pricing matches the unique model identity independently of routing prefixes and authentication profiles. Execution transport determines billing separately. Argon uses introductory rates; Haiku tiers are resolved per request including cache tokens.
Collector generated: 2026-11-11T07:11:47-05:00. Pricing source: pricing/2026-11-11T120252913396Z/api-pricing.json, as of 2026-11-11; earlier-date fallback: False. Pricing verification: {'status': 'passed', 'files_checked': 13, 'mismatched': [], 'verification_checks': 'passed'}. These are historical saved rates, not independently refreshed current rates.
Available-telemetry API-equivalent total (17/17 models): $35.74. Recorded OpenRouter charges for the final editions: $6.09. Pricing snapshot age at report date: 0 days. Last successful daily source verification for this snapshot: not yet recorded. Hash verification checks saved-file integrity; the separate daily check verifies source rates.

## Collector diagnostics


## Pricing sources

Pricing JSON: `/home/openclaw/.openclaw/workspace/briefs/model-tests/pricing/2026-11-11T120252913396Z/api-pricing.json`. Each model references a source ID with URL, retrieval timestamp and saved source snapshot.

- glm-5-3: [glm-5.3](https://docs.z.ai/guides/overview/pricing)
- fable-5-2: [claude-fable-5-2](https://platform.claude.com/docs/en/about-claude/pricing)
- opus-5-5: [claude-opus-5-5](https://platform.claude.com/docs/en/models/opus-5-5/overview)
- deepseek-v4-pro: [deepseek-v4-pro](https://api-docs.deepseek.com/quick_start/pricing/)
- fable-5-1: [claude-fable-5-1](https://platform.claude.com/docs/en/about-claude/pricing)
- grok-4-7: [grok-4.7](https://docs.x.ai/developers/pricing)
- gemini-4-argon: [gemini-4-argon](https://aistudio.google.com/docs/pricing)
- qwen-3-8-max-0902: [qwen3.8-max-0902](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-max)
- deepseek-v4-1-flash-1017: [deepseek-v4-1-flash-1017](https://api-docs.deepseek.com/quick_start/pricing/)
- minimax-m3-1-flash: [MiniMax-M3.1-Flash](https://www.minimax.io/blog/minimax-m31f)
- sonnet-5-5: [claude-sonnet-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- gpt-6-astra: [gpt-6-astra](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-sol: [gpt-6.1-sol](https://developers.openai.com/api/docs/pricing)
- gpt-6-1-terra: [gpt-6.1-terra](https://developers.openai.com/api/docs/pricing)
- haiku-5-5: [claude-haiku-5-5](https://platform.claude.com/docs/en/about-claude/pricing)
- kimi-k3-1-pro: [kimi-k3.1-pro](https://www.kimi.ai/resources/kimi-k3-1-pro-pricing)
- gpt-6-luna: [gpt-6-luna](https://developers.openai.com/api/docs/pricing)

## Audit files

- Raw collection: `/home/openclaw/.openclaw/workspace/briefs/model-tests/2026-11-11/usage-audit-ken/usage-and-cost.json`.
- Companion selection/totals audit: `Usage-and-Cost-2026-11-11.audit.json`.
- Collection reads usage/metadata only. No runs, retries, newsletter sends or production changes.

