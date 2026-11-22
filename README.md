# AI Brief Pipeline

### One editorial task. Multiple models. Inspectable results.

This pipeline tests and compares AI models for [Max’s AI Brief](https://maxsaibrief.com/), the production daily AI newsletter. This repository shares the testing results: how different models turn a shared pool of news evidence into a briefing, which stories and posts they select, how their short-form writing is judged, how long their workflows take, and what their recorded token usage would cost at published API rates. [Compare each model's results.](https://tedcahall.github.io/ai-brief-pipeline/daily-results/)

The aim is to demonstrate the trade-offs of each of the non-deterministic steps in the workflow.

<!-- MODEL-LEADERBOARD:START -->
## Model Performance Leaders

**Seven-calendar-day statistics | 2026-11-16 through 2026-11-22 | Minimum 4 observed days per metric**

Judging update pending. Judging rows retain 2026-11-21. Other rows are current.

### 🏆 Leaders

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | Gemini 4 Neon | **88.0/100** | 68.2/100 | 45.6/100 | 88.0/100 | 4 |
| Selection SD | Gemini 4 Neon | **5.9** | 12.2 | 5.9 | 20.2 | 4 |
| Editorial Score | DeepSeek V4.1 Flash | **3.66/5** | 3.01/5 | 2.39/5 | 3.66/5 | 7 |
| Ed Score SD | Fable 5.1 | **0.1** | 0.3 | 0.1 | 0.5 | 7 |
| Lowest Cost | GPT-6 Luna | **$0.09** | $1.98 | $0.09 | $10.27 | 7 |
| Run Time | GPT-6.2 Astra | **2m 47s** | 9m 57s | 2m 47s | 27m 13s | 5 |
| Token Usage | GPT-6.2 Astra | **788,487** | 5,183,277 | 788,487 | 14,468,209 | 5 |
| Pulse Words | DeepSeek V4 Pro | **160** | 116 | 68 | 160 | 7 |
| Pulse SD | GPT-6.1 Terra | **9.2** | 21.3 | 9.2 | 71.0 | 7 |
| Story Words | Fable 5.1 | **351** | 309 | 259 | 351 | 7 |
| Story SD | GPT-6.2 Sol | **4.7** | 20.7 | 4.7 | 43.7 | 5 |

### ⚠️ Laggards

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | GPT-6 Luna | **45.6/100** | 68.2/100 | 45.6/100 | 88.0/100 | 7 |
| Selection SD | GPT-6.2 Astra | **20.2** | 12.2 | 5.9 | 20.2 | 5 |
| Editorial Score | GPT-6.1 Terra | **2.39/5** | 3.01/5 | 2.39/5 | 3.66/5 | 7 |
| Ed Score SD | DeepSeek V4 Pro | **0.5** | 0.3 | 0.1 | 0.5 | 7 |
| Highest Cost | Fable 5.1 | **$10.27** | $1.98 | $0.09 | $10.27 | 7 |
| Run Time | Qwen4 Max | **27m 13s** | 9m 57s | 2m 47s | 27m 13s | 7 |
| Token Usage | Qwen4 Max | **14,468,209** | 5,183,277 | 788,487 | 14,468,209 | 7 |
| Pulse Words | GPT-6.1 Terra | **68** | 116 | 68 | 160 | 7 |
| Pulse SD | DeepSeek V4 Pro | **71.0** | 21.3 | 9.2 | 71.0 | 7 |
| Story Words | GPT-6.1 Terra | **259** | 309 | 259 | 351 | 7 |
| Story SD | GPT-6 Luna | **43.7** | 20.7 | 4.7 | 43.7 | 7 |

Mv Avg is the window mean for ordinary rows and sample SD for SD rows. All columns use only eligible models. Word counts rank length, not quality.
<!-- MODEL-LEADERBOARD:END -->

## Explore the results

- **[Model comparisons](model-comparison/)** - Where models agree, where they diverge, and which stories and posts each selects. Daily consensus scores measure selection agreement, not factual accuracy.
- **[Pulse judging](pulse-judging/)** - Blind, multi-judge evaluation of each model’s **AI Industry Pulse** summary. Model identities are removed and labels are shuffled separately for each judge. Explore daily scores, judge notes, self-preference checks, the [cumulative leaderboard](pulse-judging/LEADERBOARD.md), and the [judging prompt](pulse-judging/PROMPT.md).
- **[Token costs](token-costs/)** - Recorded input, output, and cache usage, with API-equivalent estimates kept separate from provider-billed charges.
- **[Summaries](summary/)** - The cross-day view: consensus, estimated cost, elapsed time, total tokens, and effective cost per token.
- **[API prices](api-prices/)** - The saved pricing reference for the models in the comparison, including context tiers, cache rates, source links, and observed update dates.
- **[Daily results](daily-results/)** - The generated HTML editions themselves, organized by day and model. Read the outputs behind the scores.

## Two different lenses on the output

**Consensus asks: “Did the models choose the same news?”** Pulse judging asks: **“How did the summaries perform against an editorial rubric?”** These are separate measures. Agreement does not prove accuracy, and a judge’s score is an evaluation - not an objective truth.

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
