# Astra OpenRouter — Last Two Runs

Saturday, October 31, 2026

## Bottom line

**Combined recorded charges: $42.99 across 38 billed responses. Cache writes account for $41.66 (96.92%) of the total.**

Both runs ended with HTTP 402 in-flight-credit rejection. These are recorded provider-billed response costs, not merely local cost estimates. The rejected requests have no recorded charges; missing charges are not asserted to be zero. No new model run was made to prepare this report.

## Token usage and billed cost

| Run | Calls | Ordinary input | Cache writes | Cache reads | Total prompt | Output | Cache hit | Billed |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 — initial | 14 | 42 | 887,791 | 163,007 | 1,050,840 | 4,218 | 15.51% | $11.47 |
| 2 — fresh funded | 24 | 72 | 2,445,181 | 300,936 | 2,746,189 | 13,001 | 10.96% | $31.52 |

Ordinary input excludes both cache categories. Total prompt = ordinary input + cache writes + cache reads. Cache hit = cache reads / total prompt. These are summed request tokens, not unique evidence tokens. Reasoning is included in output, not charged twice.

## Where the money went

| Category | Rate per million tokens | Run 1 tokens | Run 1 cost | Run 2 tokens | Run 2 cost |
|---|---:|---:|---:|---:|---:|
| Ordinary input | $10 | 42 | $0.00 | 72 | $0.00 |
| Cache writes | $12.5 | 887,791 | $11.10 | 2,445,181 | $30.56 |
| Cache reads | $1 | 163,007 | $0.16 | 300,936 | $0.30 |
| Output | $50 | 4,218 | $0.21 | 13,001 | $0.65 |
| **Total** | | | **$11.47** | | **$31.52** |

Formula: (ordinary input × 10 + cache writes × 12.5 + cache reads × 1 + output × 50) / 1,000,000. Each of the 38 per-call results matches its recorded provider-billed total exactly before rounding. Totals use full precision; displayed money is rounded to cents. $0.00 means less than half a cent here, not necessarily no charge.

Rate basis: saved vendor pricing snapshot used in the two audits; Standard short. The $12.5 cache-write rate reconciles to recorded charges, but does not establish actual cache retention duration. [Vendor pricing](https://developers.openai.com/api/docs/pricing).

## What the cache counters show

- Run 1: first call had zero cache reads; each of the next 13 calls read exactly 12,539 cached tokens.
- Run 2: all 24 calls read exactly 12,539 cached tokens, including its first call. A fresh session did not imply a cold provider cache.
- As the conversation grew, the cache-read amount stayed fixed while reported cache writes grew. Repeated cache writes—not generated output—dominated cost.
- For context, the original Codex Astra run reported 95.53% cache hits and a $5.47 API-equivalent estimate (not a bill). Terra OpenRouter reported 13.63% hits and $3.16 billed. Terra therefore also showed low reuse; its relevant input/write/output unit rates are one-tenth Astra’s.
- This is evidence of poor cache reuse on these runs. It does not yet establish which configuration, request-prefix change, adapter behavior, or provider behavior caused it. Native provider response bodies were not retained; normalized per-call usage was.

## Why the runs stopped

> This request would exceed your available credits given your current in-flight requests. Retry after in-flight requests settle, or add credits.

Both errors specified Retry-After: 120 seconds. OpenRouter documents a separate temporary account-level in-flight budget, including recently completed requests awaiting settlement. This is distinct from the key spending cap or a zero account balance. Its exact allowance and held amounts were not obtained. [OpenRouter limits](https://openrouter.ai/docs/api/reference/limits#in-flight-spending-budget).

Run 1 did not finish a brief. Run 2 produced local brief artifacts and passed saved validators, but its inference session still ended in error without a successful final response. Do not label either a successfully completed cron run.

## Run 1: every billed response

Session: `628bde35-fa28-46a2-b129-aeb125b3b126`. Source: `Astra-Route-Cache-Comparison-2026-10-31.audit.json`.

| Call | Total prompt | Ordinary input | Cache writes | Cache reads | Output | Billed | Cumulative |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13,649 | 3 | 13,646 | 0 | 88 | $0.18 | $0.18 |
| 2 | 20,465 | 3 | 7,923 | 12,539 | 175 | $0.12 | $0.30 |
| 3 | 33,632 | 3 | 21,090 | 12,539 | 44 | $0.28 | $0.57 |
| 4 | 34,284 | 3 | 21,742 | 12,539 | 32 | $0.29 | $0.86 |
| 5 | 35,280 | 3 | 22,738 | 12,539 | 386 | $0.32 | $1.18 |
| 6 | 42,128 | 3 | 29,586 | 12,539 | 1,025 | $0.43 | $1.61 |
| 7 | 50,680 | 3 | 38,138 | 12,539 | 416 | $0.51 | $2.12 |
| 8 | 71,269 | 3 | 58,727 | 12,539 | 379 | $0.77 | $2.89 |
| 9 | 87,968 | 3 | 75,426 | 12,539 | 231 | $0.97 | $3.85 |
| 10 | 107,115 | 3 | 94,573 | 12,539 | 213 | $1.21 | $5.06 |
| 11 | 122,443 | 3 | 109,901 | 12,539 | 489 | $1.41 | $6.47 |
| 12 | 139,604 | 3 | 127,062 | 12,539 | 23 | $1.60 | $8.07 |
| 13 | 140,012 | 3 | 127,470 | 12,539 | 362 | $1.62 | $9.69 |
| 14 | 152,311 | 3 | 139,769 | 12,539 | 355 | $1.78 | $11.47 |

## Run 2: every billed response

Session: `0be82e16-a14d-4c6c-b50c-bb2be0206c10`. Source: `Astra-Route-Cache-Comparison-Fresh-2026-10-31.audit.json`.

| Call | Total prompt | Ordinary input | Cache writes | Cache reads | Output | Billed | Cumulative |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | 13,700 | 3 | 1,158 | 12,539 | 123 | $0.03 | $0.03 |
| 2 | 27,834 | 3 | 15,292 | 12,539 | 119 | $0.21 | $0.24 |
| 3 | 33,005 | 3 | 20,463 | 12,539 | 54 | $0.27 | $0.51 |
| 4 | 34,074 | 3 | 21,532 | 12,539 | 32 | $0.28 | $0.80 |
| 5 | 35,082 | 3 | 22,540 | 12,539 | 1,261 | $0.36 | $1.15 |
| 6 | 41,285 | 3 | 28,743 | 12,539 | 451 | $0.39 | $1.55 |
| 7 | 61,322 | 3 | 48,780 | 12,539 | 400 | $0.64 | $2.19 |
| 8 | 81,151 | 3 | 68,609 | 12,539 | 341 | $0.89 | $3.08 |
| 9 | 97,180 | 3 | 84,638 | 12,539 | 329 | $1.09 | $4.17 |
| 10 | 102,793 | 3 | 90,251 | 12,539 | 253 | $1.15 | $5.32 |
| 11 | 108,849 | 3 | 96,307 | 12,539 | 270 | $1.23 | $6.55 |
| 12 | 128,160 | 3 | 115,618 | 12,539 | 534 | $1.48 | $8.03 |
| 13 | 135,255 | 3 | 122,713 | 12,539 | 115 | $1.55 | $9.59 |
| 14 | 135,508 | 3 | 122,966 | 12,539 | 469 | $1.57 | $11.16 |
| 15 | 150,047 | 3 | 137,505 | 12,539 | 209 | $1.74 | $12.90 |
| 16 | 154,493 | 3 | 141,951 | 12,539 | 201 | $1.80 | $14.70 |
| 17 | 155,517 | 3 | 142,975 | 12,539 | 546 | $1.83 | $16.52 |
| 18 | 173,281 | 3 | 160,739 | 12,539 | 247 | $2.03 | $18.56 |
| 19 | 174,195 | 3 | 161,653 | 12,539 | 4,568 | $2.26 | $20.82 |
| 20 | 178,832 | 3 | 166,290 | 12,539 | 643 | $2.12 | $22.94 |
| 21 | 179,510 | 3 | 166,968 | 12,539 | 32 | $2.10 | $25.04 |
| 22 | 180,538 | 3 | 167,996 | 12,539 | 1,087 | $2.17 | $27.21 |
| 23 | 181,766 | 3 | 169,224 | 12,539 | 97 | $2.13 | $29.34 |
| 24 | 182,812 | 3 | 170,270 | 12,539 | 620 | $2.17 | $31.52 |

## Verification

- Recomputed token totals, cache-hit denominators, all 38 per-call bills, run totals and combined total from the saved per-call audit data. No credential or model API call was needed. Original reports and audit JSON remain unchanged.
- Cost breakdown is recomputed from reconciled unit rates; recorded bills are retained provider response totals, not a newly downloaded invoice.
- Earlier preflight/cooldown failures are outside these two token-bearing runs.

- `Astra-Route-Cache-Comparison-2026-10-31.audit.json` SHA-256: `b7ed7dd7ef21739ea0b773e8a987173ba69f8edd86ee511ae1a90e72f7dc480f`
- `Astra-Route-Cache-Comparison-Fresh-2026-10-31.audit.json` SHA-256: `cb0abe13608c661a14de1c9230f73784f3c3d8f8087fc42fba48675371186a2f`
