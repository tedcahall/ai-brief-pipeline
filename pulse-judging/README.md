# Pulse Judging

## Leaderboard

Moving average of the last 7 judged run(s) (window: up to 7), 11-8 to 11-14. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-8 | 11-9 | 11-10 | 11-11 | 11-12 | 11-13 | 11-14 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | deepseek-v4-1-flash-1017 | **3.53** | 0.42 | 3.20 | 3.70 | 3.90 | 4.20 | 3.20 | 3.10 | 3.40 |
| 2 | opus-5-5 | **3.29** | 0.12 | 3.40 | 3.30 | 3.20 | 3.10 | 3.40 | 3.40 | 3.20 |
| 3 | grok-4-7 | **3.21** | 0.09 | 3.10 | 3.30 | 3.20 | 3.30 | 3.20 | 3.30 | 3.10 |
| 4 | deepseek-v4-pro | **3.19** | 0.32 | 3.20 | 3.20 | 2.90 | 3.00 | 2.80 | 3.50 | 3.70 |
| 5 | sonnet-5-5 | **3.19** | 0.12 | 3.40 | 3.20 | 3.10 | 3.20 | 3.00 | 3.20 | 3.20 |
| 6 | kimi-k3-1-pro | **3.17** | 0.28 | 3.10 | 3.40 | 2.90 | 2.80 | 3.30 | 3.10 | 3.60 |
| 7 | qwen-3-8-max-0902 | **3.13** | 0.43 | 3.30 | 2.90 | 3.20 | 2.90 | 4.00 | 2.80 | 2.80 |
| 8 | minimax-m3-1-flash | **3.06** | 0.30 | 3.40 | 2.80 | 2.80 | 2.80 | 3.50 | 3.20 | 2.90 |
| 9 | gemini-4-hydrogen | **3.00** | 0.28 | – | – | – | – | – | 3.20 | 2.80 |
| 10 | haiku-5-5 | **2.97** | 0.21 | 2.70 | 2.80 | 3.30 | 2.90 | 2.90 | 3.00 | 3.20 |
| 11 | glm-5-3 | **2.93** | 0.39 | 2.70 | 3.10 | 2.30 | 3.20 | 2.90 | 3.50 | 2.80 |
| 12 | fable-5-2 | **2.92** | 0.38 | – | – | 2.60 | 2.80 | 3.50 | 2.60 | 3.10 |
| 13 | fable-5-1 | **2.91** | 0.43 | 2.80 | 3.20 | 3.30 | 2.20 | 3.40 | 2.60 | 2.90 |
| 14 | gpt-6-astra | **2.87** | 0.46 | 2.20 | 2.70 | 3.60 | 3.00 | 2.50 | 2.90 | 3.20 |
| 15 | gpt-6-1-sol | **2.84** | 0.16 | 2.60 | 2.90 | 3.10 | 2.70 | 2.80 | 2.90 | 2.90 |
| 16 | gpt-6-luna | **2.69** | 0.36 | 2.70 | 2.50 | 3.30 | 2.50 | 3.00 | 2.20 | 2.60 |
| 17 | gemini-4-argon | **2.46** | 0.27 | 2.80 | 2.40 | 2.40 | 2.00 | 2.60 | 2.70 | 2.30 |
| 18 | gemini-4-carbon | **2.40** | 0.24 | – | – | – | 2.10 | 2.70 | 2.40 | 2.40 |
| 19 | gpt-6-1-terra | **2.33** | 0.21 | 2.00 | 2.20 | 2.30 | 2.40 | 2.70 | 2.40 | 2.30 |

**Most consistent:** grok-4-7 (0.09), opus-5-5 (0.12), sonnet-5-5 (0.12).
**Most volatile:** gpt-6-astra (0.46), qwen-3-8-max-0902 (0.43), fable-5-1 (0.43).
(Models with at least 3 days in the window.)

---

## About

Daily blind judging of each model's "AI Industry Pulse" summary from `daily-results/`. Maintained by Ogilvy.

- [SCORE-GRADERS.md](SCORE-GRADERS.md): which judge grades hardest and easiest.
- `daily/YYYY-MM-DD.md`: that day's ranking, per-judge scores, grader averages, self-preference check and judge notes.
- `json/YYYY-MM-DD.json`: the same data, machine-readable. The scripts use it to rebuild the leaderboard and to tell which days are already judged.
- [PROMPT.md](PROMPT.md): the exact judge prompt (v2, strict).
- [LEADERBOARD.md](LEADERBOARD.md): the same leaderboard as above, as its own file.

**Method.** Once a day's `token-costs/Usage-and-Cost-<date>.md` and `model-comparison/Model-Consensus-<date>.md` both exist, the Pulse section is extracted from each HTML file and model names are removed. Each judge (opus = anthropic/claude-opus-5-5, glm = openrouter_eich/z-ai/glm-5.3, astra = openai/gpt-6-astra, grok = openrouter_grok/x-ai/grok-4.7, dsflash = openrouter_flash/deepseek/deepseek-v4.1-flash-1017; a 5-judge panel since Nov 11, applied to every day) gets its own random label shuffle and scores every summary from 1 to 5 against fixed anchors. A grammar error caps a summary at 3, and repeated hedging caps it at 3.5. The judges never see model names or each other's scores. Each judge also competes as a model, so every report includes a self-preference check.
