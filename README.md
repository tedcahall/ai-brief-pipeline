# AI Brief Pipeline

### One editorial task. Multiple models. Inspectable results.

This pipeline tests and compares AI models for [Max’s AI Brief](https://maxsaibrief.com/), the production daily AI newsletter. This repository shares the testing results: how different models turn a shared pool of news evidence into a briefing, which stories and posts they select, how their short-form writing is judged, how long their workflows take, and what their recorded token usage would cost at published API rates. [Compare each model's results.](https://tedcahall.github.io/ai-brief-pipeline/daily-results/)

The aim is to demonstrate the trade-offs of each of the non-deterministic steps in the workflow.

<!-- MODEL-LEADERBOARD:START -->
## Model Performance Leaders

**Seven-calendar-day statistics | 2026-11-17 through 2026-11-23 | Minimum 4 observed days per metric**

Judging as of 2026-11-23; status: complete.

### 🏆 Leaders

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | Gemini 4 Neon | **86.4/100** | 67.8/100 | 45.4/100 | 86.4/100 | 5 |
| Selection SD | Sonnet 5.5 | **4.7** | 11.7 | 4.7 | 21.4 | 7 |
| Editorial Score | DeepSeek V4.1 Flash | **3.67/5** | 3.02/5 | 2.41/5 | 3.67/5 | 7 |
| Ed Score SD | Fable 5.1 | **0.1** | 0.3 | 0.1 | 0.5 | 7 |
| Lowest Cost | GPT-6 Luna | **$0.09** | $1.95 | $0.09 | $9.93 | 7 |
| Run Time | GPT-6.2 Astra | **2m 47s** | 10m 03s | 2m 47s | 26m 25s | 6 |
| Token Usage | GPT-6.2 Astra | **775,262** | 5,172,087 | 775,262 | 14,778,430 | 6 |
| Pulse Words | DeepSeek V4 Pro | **171** | 116 | 67 | 171 | 7 |
| Pulse SD | GPT-6.1 Terra | **8.2** | 21.1 | 8.2 | 65.0 | 7 |
| Story Words | Fable 5.1 | **351** | 308 | 257 | 351 | 7 |
| Story SD | GPT-6.2 Sol | **4.6** | 20.9 | 4.6 | 42.8 | 6 |

### ⚠️ Laggards

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | GPT-6 Luna | **45.4/100** | 67.8/100 | 45.4/100 | 86.4/100 | 7 |
| Selection SD | GPT-6.2 Astra | **21.4** | 11.7 | 4.7 | 21.4 | 6 |
| Editorial Score | GPT-6.1 Terra | **2.41/5** | 3.02/5 | 2.41/5 | 3.67/5 | 7 |
| Ed Score SD | Gemini 4 Neon | **0.5** | 0.3 | 0.1 | 0.5 | 5 |
| Highest Cost | Fable 5.1 | **$9.93** | $1.95 | $0.09 | $9.93 | 7 |
| Run Time | Qwen4 Max | **26m 25s** | 10m 03s | 2m 47s | 26m 25s | 7 |
| Token Usage | Qwen4 Max | **14,778,430** | 5,172,087 | 775,262 | 14,778,430 | 7 |
| Pulse Words | GPT-6.1 Terra | **67** | 116 | 67 | 171 | 7 |
| Pulse SD | DeepSeek V4 Pro | **65.0** | 21.1 | 8.2 | 65.0 | 7 |
| Story Words | GPT-6.1 Terra | **257** | 308 | 257 | 351 | 7 |
| Story SD | GPT-6 Luna | **42.8** | 20.9 | 4.6 | 42.8 | 7 |

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
