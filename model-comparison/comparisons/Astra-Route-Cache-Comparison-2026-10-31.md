# Astra route/cache comparison — Saturday, October 31, 2026

## Result

The selected Astra OpenRouter attempt FAILED after 14 billed responses, then a terminal HTTP 402: `openrouter_in_flight_budget` / `in_flight_budget_exhausted`. This is the provider’s specific reason, not proof that the account balance was zero. The rejected request has no recorded bill. No retry or additional paid inference was launched by this audit.

Astra OpenRouter incurred **$11.47** before producing a completed brief. Its cache-hit share was **15.51%**, versus **95.53%** for completed Astra Codex and **13.63%** for completed Terra OpenRouter. The failed partial run is not an equivalent completed-work comparison.

## Token accounting

Ordinary input excludes both cache categories. Total prompt = ordinary input + cache write + cache read. New-input share = (ordinary input + cache write) / total prompt; cache-hit share = cache read / total prompt. These are token-weighted across requests, not unique source tokens.

| Model | Calls | Runtime seconds | Ordinary input | Cache write | Cache read | Total prompt | Output |
|---|---:|---:|---:|---:|---:|---:|---:|
| Astra Codex | 29 | 513 | 145,725 | unavailable (normalized 0) | 3,111,680 | 3,257,405 | 18,087 |
| Astra OpenRouter | 14 | 118.831 | 42 | 887,791 | 163,007 | 1,050,840 | 4,218 |
| Terra OpenRouter | 32 | 252 | 96 | 2,464,419 | 388,771 | 2,853,286 | 10,994 |

Runtime uses cron start-to-terminal duration, including startup; not the shorter self-reported synthesis time. Calls exclude the terminal rejected request; its metadata and zero placeholders are retained separately.

| Model | Cache hit | New-input share | API-equivalent estimate | Recorded API charges | Accounting coverage |
|---|---:|---:|---:|---:|---|
| Astra Codex | 95.53% | 4.47% | $5.47 | not applicable (subscription) | 29 token-bearing responses; billed N/A |
| Astra OpenRouter | 15.51% | 84.49% | $11.47 | $11.47 | 14 token-bearing responses; billed 14/14 |
| Terra OpenRouter | 13.63% | 86.37% | $3.16 | $3.16 | 32 token-bearing responses; billed 32/32 |

**Codex’s $5.47 is an API-equivalent estimate, NOT an actual bill.** No per-run subscription allocation. Estimates and bills are never added. OpenRouter charge coverage is complete for successful responses; rejected-request charges remain unavailable.

## First-call and subsequent cache patterns

| Model | First prompt | First read | First write | Subsequent cache reads | Last prompt |
|---|---:|---:|---:|---|---:|
| Astra Codex | 21,123 | 0 | unavailable | 20,992 → 158,976, growing every response | 159,200 |
| Astra OpenRouter | 13,649 | 0 | 13,646 | 12,539 on every later response | 152,311 |
| Terra OpenRouter | 13,656 | 0 | 13,653 | 12,541 on every later response | 131,767 |

Observation: Codex reuse grows with the request sequence; both OpenRouter runs reuse a nearly fixed 12.5k-token amount while reported writes grow. This is consistent with stable-prefix reuse on these OpenRouter sessions, not proof of the cache implementation or why reuse did not grow. All per-call counts and generation IDs are in the companion JSON.

## Pricing, cache semantics, and billing reconciliation

Source: https://developers.openai.com/api/docs/pricing — archived verified rate cards from 2026-10-29; archive hashes rechecked. Both Astra routes use the same Astra card. No fresh rate-card retrieval was needed for this same-basis comparison. Unit rates below are dollars per million tokens, retaining vendor precision.

| Model | Ordinary input | Read | Output (includes reasoning) | Write 30m | Write 12h |
|---|---:|---:|---:|---:|---:|
| Astra | 10 | 1 | 50 | 12.5 | 25 |
| Terra | 1 | 0.05 | 5 | 1.25 | 2.5 |

All 75 successful calls fall in Standard short (prompt ≤272,000); tier selection uses each request, not run totals. Long tiers are retained in JSON but unused. No Batch/Flex/Fast or regional multiplier assumed. Computation uses Decimal without intermediate rounding; only displayed dollar totals round to cents.

The installed OpenAI-completions adapter reads cache write from explicit provider fields (`prompt_tokens_details.cache_write_tokens`, `prompt_tokens_details.cache_creation_input_tokens`, or `cache_creation_input_tokens`); it does NOT derive writes by labeling all uncached input as writes. It subtracts read and write from native prompt to obtain ordinary input. Native response bodies were not retained, so which alternative field was supplied cannot be resolved. Normalized raw usage is preserved in JSON. Codex native input already includes cached input; subtract cached input once. Its absent native write field becomes zero in the collector, not evidence of no physical writes.

Provider-reported totals are independent of locally configured cost components: the adapter applies `rawUsage.cost` to the total. Each of Astra’s 14 and Terra’s 32 recorded provider-billed totals exactly matches recomputation using the 30m write rate (a 25% premium over ordinary input). Thus the premium is supported by billed totals, not config alone. This establishes the matching price, not the actual cache TTL. Separate OpenRouter generation-endpoint `total_cost` records were not fetched; retained values are provider-billed response costs with generation IDs. No Astra credential was accessed or used.

Reasoning counters: Astra Codex 3,568; Astra OpenRouter 109; Terra 16. Reasoning is included within output, not charged twice. Codex native output/reasoning counters and OpenRouter normalized counters are preserved. Final responses are included for completed baseline runs; the failed Astra run ends with a rejected-request event, not a successful final response.

## Identity, artifacts, and coverage

- Selected job: `603f1755-4cbc-4b82-b83a-7183da61337f`; session: `628bde35-fa28-46a2-b129-aeb125b3b126`; executed `openrouter_astra/openai/gpt-6-astra` throughout successful calls. No executed fallback observed.
- The local `run.json` remains stale `in_progress`; cron is terminal `failed`. Local evidence copies and candidate subset exist, but no completed canonical edition/HTML was produced. Source artifacts were not edited.
- Three earlier attempts also appear in the job history: model-policy rejection, HTTP 402, and auth/billing cooldown. They contain no token-bearing successful responses or recorded provider bills; their metadata is preserved separately, with missing charges unavailable rather than zero. This audit did not initiate those attempts.
- Frozen manifest and all 30 source-file hashes pass; all three run manifests match. The frozen `morning-brief-single-model.md` instruction/template hash is `84ec7b7f1be5217a85ff1a7c86404f39081ea43c3b0ddf58f5512aecd3b80922`. Shared evidence does not mean byte-identical complete prompts or independently prove a separate mutable HTML rendering template stayed unchanged.
- Baseline totals match the preserved 12-model audit; new-run totals match terminal cron counters. Codex per-call sums match native cumulative totals. Original audit and publication files are hash-verified unchanged.

## Interpretation and completion

These observations do not causally establish that Codex itself caused the difference. Routing, prompt/tool scaffolding, request sequences, model decisions, live verification, and completion status differ. One failed OpenRouter run cannot estimate the cost of its completed brief or establish a repeatable route effect.

Audit complete; the test is terminal and the Astra test key can be retired by Ken. No key deletion, publishing, extra test, retry, or messages to other agents were performed.

Companion: `Astra-Route-Cache-Comparison-2026-10-31.audit.json`. Full extraction and rendering scripts are retained alongside it.
