# AI Brief Pipeline

### One editorial task. Multiple models. Inspectable results.

This pipeline tests and compares AI models for [Max’s AI Brief](https://maxsaibrief.com/), the production daily AI newsletter. This repository shares the testing results: how different models turn a shared pool of news evidence into a briefing, which stories and posts they select, how their short-form writing is judged, how long their workflows take, and what their recorded token usage would cost at published API rates. [Compare each model's results.](https://tedcahall.github.io/ai-brief-pipeline/daily-results/)

The aim is to demonstrate the trade-offs of each of the non-deterministic steps in the workflow.

<!-- MODEL-LEADERBOARD:START -->
## Model Performance Leaders

**Five-batch moving averages | November 11-15, 2026 | Minimum 3 observed runs**

### 🏆 Leaders

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | Fable 5.2 | **80.0/100** | 68.3/100 | 44.0/100 | 80.0/100 | 5 |
| Editorial Score | DeepSeek V4.1 Flash 1017 | **3.40/5** | 2.96/5 | 2.40/5 | 3.40/5 | 5 |
| Lowest Cost | GPT-6 Luna | **$0.0802** | $2.1514 | $0.0802 | $9.6506 | 5 |
| Run Time | gemini-4-hydrogen | **3m 35s** | 10m 57s | 3m 35s | 32m 09s | 3 |
| Ed Consistency | GPT-6.1 Sol | **SD 0.114** | SD 0.291 | SD 0.114 | SD 0.510 | 5 |
| Token Usage | gemini-4-hydrogen | **2,109,253** | 5,234,173 | 2,109,253 | 11,604,880 | 3 |

### ⚠️ Laggards

| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |
|---|---|---:|---:|---:|---:|---:|
| Ed Selection | GPT-6 Luna | **44.0/100** | 68.3/100 | 44.0/100 | 80.0/100 | 5 |
| Editorial Score | GPT-6.1 Terra | **2.40/5** | 2.96/5 | 2.40/5 | 3.40/5 | 5 |
| Highest Cost | Fable 5.1 | **$9.6506** | $2.1514 | $0.0802 | $9.6506 | 5 |
| Run Time | Qwen 3.8 Max 0902 | **32m 09s** | 10m 57s | 3m 35s | 32m 09s | 5 |
| Ed Consistency | Qwen 3.8 Max 0902 | **SD 0.510** | SD 0.291 | SD 0.114 | SD 0.510 | 5 |
| Token Usage | MiniMax M3.1 Flash | **11,604,880** | 5,234,173 | 2,109,253 | 11,604,880 | 5 |
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
