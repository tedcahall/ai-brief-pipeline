# Astra route/cache comparison — Saturday, October 31, 2026

## Fresh attempt result

**The fresh funded Astra OpenRouter attempt failed with HTTP 402 after 24 billed responses, costing $31.52.** The specific diagnostic is “This request would exceed your available credits given your current in-flight requests.” This does not establish a zero account balance. No paid retry was performed.

The run produced local canonical JSON-Markdown, HTML and Markdown; all six saved validator checks passed, and all ten source-parity checks passed. It did not produce a successful final assistant response or finalize run.json, which remains `in_progress`; terminal cron status is authoritative (`failed`). The audit separately repaired the local preview check. The original failed attempt’s **$11.47** is historical and excluded from every fresh-run total below.

## Three-route comparison

Ordinary input excludes reads and writes. Total prompt = ordinary input + cache write + cache read. Cache hit = reads / total prompt. New-input share = (ordinary input + writes) / total prompt. Totals count tokens across requests, not unique evidence tokens.

| Model | Calls | Runtime seconds | Ordinary input | Cache write | Cache read | Total prompt | Output |
|---|---:|---:|---:|---:|---:|---:|---:|
| Astra Codex | 29 | 513 | 145,725 | Unavailable¹ | 3,111,680 | 3,257,405 | 18,087 |
| Astra OpenRouter | 24 | 299.277 | 72 | 2,445,181 | 300,936 | 2,746,189 | 13,001 |
| Terra OpenRouter | 32 | 252 | 96 | 2,464,419 | 388,771 | 2,853,286 | 10,994 |

¹ Codex native cache-write counter is absent, normalized to zero only for computation; this is not evidence of no physical writes. Its ordinary-input figure is native prompt minus reported reads. Runtime is cron start-to-terminal, including startup. Calls count token-bearing responses; the fresh terminal rejected request is retained separately, with charge unavailable, not zero.

| Model | Cache hit | New-input share | API-equivalent estimate | Recorded charges | Accounting coverage |
|---|---:|---:|---:|---:|---|
| Astra Codex | 95.53% | 4.47% | $5.47 | N/A (subscription) | 29 responses; bills N/A |
| Astra OpenRouter | 10.96% | 89.04% | $31.52 | $31.52 | 24 responses; bills 24/24 |
| Terra OpenRouter | 13.63% | 86.37% | $3.16 | $3.16 | 32 responses; bills 32/32 |

**Codex’s $5.47 is an API-equivalent estimate, NOT an actual bill.** No subscription allocation is made. Estimates and recorded charges are never added. OpenRouter recorded charges cover every token-bearing response, including Terra’s successful final response. Fresh Astra ends with HTTP 402 after a tool-use response, so there is no successful final response to include. Missing rejected-request charges remain unavailable.

## Cache pattern

| Model | First prompt | First read | First write | Subsequent reads | Last prompt |
|---|---:|---:|---:|---|---:|
| Astra Codex | 21,123 | 0 | Unavailable | 20,992 → 158,976; increasing | 159,200 |
| Astra OpenRouter | 13,700 | 12,539 | 1,158 | 12,539 on every later call | 182,812 |
| Terra OpenRouter | 13,656 | 0 | 13,653 | 12,541 on every later call | 131,767 |

Fresh Astra already reports 12,539 cached tokens on its first call and retains exactly that amount on all 24 calls. This is a fresh session, not demonstrated cold provider cache. Codex reuse grows across its request sequence; Terra starts at zero, then stays at 12,541. Stable-prefix reuse is an interpretation consistent with the OpenRouter counters, not proof of cache implementation or cause. All per-call counts, timestamps, generation IDs and raw normalized usage are in the companion JSON.

## Pricing and provider reconciliation

Source: https://developers.openai.com/api/docs/pricing — same archived rate basis as the original baselines; pricing archive hashes reverified. No newer card or configured component price is substituted. Unit rates below retain their original precision (USD per million tokens).

| Model | Ordinary input | Cache read | Output | Write 30m | Write 12h |
|---|---:|---:|---:|---:|---:|
| Astra (both routes) | 10 | 1 | 50 | 12.5 | 25 |
| Terra | 1 | 0.05 | 5 | 1.25 | 2.5 |

All 85 token-bearing requests fit Standard short (prompt ≤272,000), determined per call rather than from summed tokens. Full cards, including unused long-context tiers, are retained in JSON. No batch, regional or service-tier multiplier is assumed. Decimal calculations retain precision until displayed dollar amounts round to cents.

Every one of the 24 fresh Astra and 32 Terra provider-billed response totals matches the independently recomputed 30m write-rate estimate exactly. The 25% write premium is therefore supported by recorded bills, not inferred solely from config. Physical cache TTL is not reported; price reconciliation does not prove retention duration.

The installed OpenAI-completions adapter obtains writes from explicit provider fields: `prompt_tokens_details.cache_write_tokens`, `prompt_tokens_details.cache_creation_input_tokens`, or `cache_creation_input_tokens`. It does not derive writes from all uncached input. It subtracts writes and reads from native prompt once to calculate ordinary input. Native response bodies are not retained, so the exact alternative provider field cannot be identified; normalized counters and contextUsage.promptTokens are preserved. Codex native input already contains cache reads; subtracting once avoids double counting.

The adapter applies provider `rawUsage.cost` independently of locally calculated component costs. Recorded totals here are retained `usage.cost.total` with `totalOrigin=provider-billed`, not a newly fetched generation-endpoint `total_cost`. Separate endpoint billing records are unavailable. No Astra credential was accessed or used during analysis.

Reasoning tokens are included in output, never charged a second time: Codex Astra 3,568; fresh OpenRouter Astra 1,029; OpenRouter Terra 16. Native Codex and normalized OpenRouter reasoning counters are retained.

## Identity, frozen inputs and artifacts

- Fresh job: `456a8ee5-f557-4538-8741-519c76a78390`. Session: `0be82e16-a14d-4c6c-b50c-bb2be0206c10`. Every successful call executed `openrouter_astra/openai/gpt-6-astra`; no fallback execution observed.
- Baselines are the ORIGINAL same-day `gpt-6-astra` and `gpt-6-1-terra` sessions, not predecessor Astra OpenRouter outputs. Fresh extraction independently queries its own session.
- All 30 frozen files and manifest hashes rechecked. Every compared run references manifest `b9e6ff8918f021ae784b2ffdce414d96a985227c2a2daba22f0226baac24d0be`. Frozen instruction/template hash: `84ec7b7f1be5217a85ff1a7c86404f39081ea43c3b0ddf58f5512aecd3b80922`. This verifies the shared frozen inputs, not identity of complete prompts or separately mutable renderer assets.
- Original 12-model audit and publication report remain hash-verified unchanged. Fresh totals match terminal cron counters; baseline totals match the original saved audit. Native per-call prompt totals and aggregate Decimal costs independently match the generated totals.
- Local artifacts remain under `briefs/model-tests/2026-10-31/gpt-6-astra-openrouter-fresh/`; source run.json is preserved without falsely changing failed inference to success. Preview recovery and verification are separate audit artifacts.

## Interpretation and completion

The observed fresh run has much less cache reuse and a higher API-equivalent cost than Codex Astra, but this is not causal proof that Codex itself caused the differences. Routing, prompt/tool scaffolding, request sequence, model decisions, live verification and terminal outcome differ. One failed run is not a completed-work price benchmark.

Test and post-run audit are complete; Ken can retire the test key. No key deletion, further inference, retry, publication or messages to other agents were performed.

Companion audit: `Astra-Route-Cache-Comparison-Fresh-2026-10-31.audit.json`. Independent extraction, finishing and verification scripts/results are retained alongside the report.
