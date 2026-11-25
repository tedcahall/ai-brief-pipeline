# AI Brief Pipeline

### One editorial task. Multiple models. Inspectable results.

This pipeline tests and compares AI models for [Max’s AI Brief](https://maxsaibrief.com/), the production daily AI newsletter. This repository shares the testing results: how different models turn a shared pool of news evidence into a briefing, which stories and posts they select, how their short-form writing is judged, how long their workflows take, and what their recorded token usage would cost at published API rates. [Compare each model's results.](https://tedcahall.github.io/ai-brief-pipeline/daily-results/)

The aim is to demonstrate the trade-offs of each of the non-deterministic steps in the workflow.

<!-- MODEL-LEADERBOARD:START -->
## Model Performance Leaders

**Seven-calendar-day statistics | 2026-11-19 through 2026-11-25 | Minimum 4 observed days per metric**

Judging as of 2026-11-25; status: complete.

### 🏆 Leaders

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | Gemini 4 Argon | **82.3/100** | 69.0/100 | 53.0/100 | 82.3/100 | 7 |
| Selection SD | Gemini 4 Hydrogen | **7.1** | 12.4 | 7.1 | 22.3 | 7 |
| Editorial Score | GPT-6.2 Astra | **3.56/5** | 2.99/5 | 2.40/5 | 3.56/5 | 7 |
| Ed Score SD | GPT-6 Luna | **0.1** | 0.3 | 0.1 | 0.5 | 7 |
| Lowest Cost | GPT-6 Luna | **$0.09** | $1.92 | $0.09 | $9.81 | 7 |
| Run Time | GPT-6.2 Astra | **2m 48s** | 9m 58s | 2m 48s | 26m 00s | 7 |
| Token Usage | GPT-6.2 Astra | **822,507** | 5,102,644 | 822,507 | 13,954,016 | 7 |
| Pulse Words | DeepSeek V4 Pro | **172** | 118 | 64 | 172 | 7 |
| Pulse SD | GPT-6 Astra | **1.8** | 20.4 | 1.8 | 63.8 | 7 |
| Story Words | Fable 5.1 | **353** | 308 | 254 | 353 | 7 |
| Story SD | GPT-6.2 Sol | **4.9** | 19.4 | 4.9 | 44.0 | 7 |

### ⚠️ Laggards

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | GPT-6 Luna | **53.0/100** | 69.0/100 | 53.0/100 | 82.3/100 | 7 |
| Selection SD | GPT-6.2 Astra | **22.3** | 12.4 | 7.1 | 22.3 | 7 |
| Editorial Score | GPT-6.1 Terra | **2.40/5** | 2.99/5 | 2.40/5 | 3.56/5 | 7 |
| Ed Score SD | DeepSeek V4.1 Flash | **0.5** | 0.3 | 0.1 | 0.5 | 7 |
| Highest Cost | Fable 5.1 | **$9.81** | $1.92 | $0.09 | $9.81 | 7 |
| Run Time | Qwen 3.8 Max 0902 | **26m 00s** | 9m 58s | 2m 48s | 26m 00s | 7 |
| Token Usage | Qwen4 Max | **13,954,016** | 5,102,644 | 822,507 | 13,954,016 | 7 |
| Pulse Words | GPT-6.1 Terra | **64** | 118 | 64 | 172 | 7 |
| Pulse SD | DeepSeek V4 Pro | **63.8** | 20.4 | 1.8 | 63.8 | 7 |
| Story Words | GPT-6.1 Terra | **254** | 308 | 254 | 353 | 7 |
| Story SD | MiniMax M3.1 Flash | **44.0** | 19.4 | 4.9 | 44.0 | 7 |

Mv Avg is the window mean for ordinary rows and sample SD for SD rows. All columns use only eligible models. Word counts rank length, not quality.
<!-- MODEL-LEADERBOARD:END -->

## Explore the results

- **[Summaries](summary/)** - The cross-day view: consensus, estimated cost, elapsed time, total tokens, and effective cost per token. With daily, weekly, monthly, rolling 7 and 30 day views of the data.
- **[Pulse judging](pulse-judging/)** - Blind, multi-judge evaluation of each model’s **AI Industry Pulse** summary. Model identities are removed and labels are shuffled separately for each judge. Explore daily scores, judge notes, self-preference checks, the [cumulative leaderboard](pulse-judging/LEADERBOARD.md), and the [judging prompt](pulse-judging/PROMPT.md).
- **[Story Selection comparisons](model-comparison/)** - Where models agree, where they diverge, and which stories and posts each selects. Daily Selection scores measure selection agreement, not factual accuracy.
- **[Token costs](token-costs/)** - Recorded input, output, and cache usage, with API-equivalent estimates kept separate from provider-billed charges.
- **[API prices](api-prices/)** - The saved pricing reference for the models in the comparison, including context tiers, cache rates, source links, and observed update dates.
- **[Daily results](daily-results/)** - The generated HTML editions themselves, organized by day and model. Read the outputs behind the scores.

## Two different lenses on the output

**Selection asks: “Did the models choose the the most popular news?”** Pulse judging asks: **“How did the summaries perform against an editorial rubric?”** These are separate measures. Agreement does not prove accuracy, and a judge’s score is an evaluation - not an objective truth.

Read both alongside the actual editions, execution times, and costs. Shared starting evidence improves comparability, but does not make every session, runtime instruction, or follow-up research step identical. Daily reports document their scope and limitations.

## Follow the evidence

- [Who Max Follows](https://tedcahall.github.io/ai-brief-pipeline/docs/who-max-follows/): the X.com (Twitter) source directory.  Searchable and sort-able by original, @name, and company.

Readable reports sit at the top of each reporting directory. Supporting JSON audits live in each reporting directory’s `json/` subdirectory, including `pulse-judging/json/`. Pulse Judging’s readable daily reports live in `pulse-judging/daily/`.

- [Archive notes](docs/archive-notes.md) explain selection rules and exceptions.
- [Import manifest](docs/import-manifest.json) records the original imported source paths and SHA-256 hashes.

This repository is a reporting and results archive, not a complete runnable distribution of the production newsletter pipeline.

## License

The reports, data, and documentation in this repository are licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). You may share and adapt them for any purpose, including commercial use, provided you give appropriate credit, link to the license, and indicate whether changes were made. Suggested credit: “AI Brief Pipeline by Agentilis.ai, from Max’s AI Brief.” See [LICENSE](LICENSE) for the full legal text.

The newsletter editions in `daily-results/` link to and briefly quote third-party news articles and social posts. That third-party material remains the property of its owners and is not covered by this license.
