# Astra: Codex CLI vs OpenRouter API

**Scope:** Morning Codex Astra versus the latest fresh OpenRouter Astra attempt. One run per route; the earlier failed API run is excluded. No per-call breakdown.

| Metric | Astra — Codex CLI | Astra — OpenRouter API |
|---|---:|---:|
| Model calls | 29 | 24 |
| Total input / prompt tokens | 3,257,405 | 2,746,189 |
| Input served from cache | 3,111,680 | 300,936 |
| Input NOT served from cache | 145,725 | 2,445,253 |
| ↳ Ordinary input (reported category) | 145,725 | 72 |
| ↳ Cache writes (reported category) | Not separately reported | 2,445,181 |
| Output tokens (includes reasoning) | 18,087 | 13,001 |
| ↳ Reasoning subset | 3,568 | 1,029 |
| Input + output tokens | 3,275,492 | 2,759,190 |
| Cache-hit rate | 95.53% | 10.96% |
| API-equivalent cost | $5.47 estimate | $31.52 |
| Recorded API charge | N/A — subscription | $31.52 |
| Outcome | Completed | HTTP 402; no successful final response |

## What this means

**The API run did not use more total input tokens: it used 15.69% fewer. It processed 16.78× as many input tokens without a cache hit.**

- Codex: 145,725 uncached + 3,111,680 cached = 3,257,405 total input.
- API: 72 ordinary + 2,445,181 cache writes + 300,936 cache reads = 2,746,189 total input.
- The expensive difference is how the input is classified and reused, not a larger aggregate token count. API cache writes alone cost $30.56 of its $31.52 total at the reconciled $12.5-per-million write rate.
- Codex cache reuse grew across calls; the API reported exactly 12,539 cached tokens on every call while its prompt grew.

## Read the categories correctly

- Total input already includes cache reads and writes: do not add either again. The two indented input rows explain the non-cache-hit input row, not additional tokens.
- Codex does not separately report cache writes in the saved native usage. Its 145,725 uncached tokens are the comparable non-cache-hit category; do not interpret its normalized write zero as proof of no physical writes.
- Output includes reasoning. The reasoning row is a subset, not an additional charge.
- Tokens are summed across model requests, not unique text. Repeated conversation context is counted each time it is submitted.
- The API attempt has 24 calls versus Codex’s 29 and ended in error. These are observed totals, not equal-work or projected completion costs. Both use the same frozen source evidence, but full prompts, tools and follow-up research differ.
- Codex cost is a list-price API-equivalent estimate, not a subscription bill. The API amount is the retained provider-billed response total. Poor reuse is demonstrated; its configuration/provider root cause is not established.

## Sources and checks

- Codex session: `e200847e-1344-4d08-846e-5b972e3cc8ff`.
- API session: `0be82e16-a14d-4c6c-b50c-bb2be0206c10`.
- Source audit: `Astra-Route-Cache-Comparison-Fresh-2026-10-31.audit.json`.
- Source SHA-256: `cb0abe13608c661a14de1c9230f73784f3c3d8f8087fc42fba48675371186a2f`.
- Recomputed all token categories from saved per-call records and checked against audit totals. No model runs, credentials, or configuration changes were needed.
