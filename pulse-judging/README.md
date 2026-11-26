# Pulse Judging

## Leaderboard

Moving average of the last 7 judged run(s) (window: up to 7), 11-20 to 11-26. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-20 | 11-21 | 11-22 | 11-23 | 11-24 | 11-25 | 11-26 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | gpt-6-2-astra | **3.51** | 0.22 | 3.20 | 3.40 | 3.40 | 3.70 | 3.70 | 3.40 | 3.80 |
| 2 | deepseek-v4-1-flash-1017 | **3.50** | 0.50 | 4.30 | 3.60 | 3.10 | 3.80 | 3.00 | 3.20 | – |
| 3 | gpt-6-2-sol | **3.46** | 0.36 | 3.20 | 3.00 | 4.10 | 3.50 | 3.60 | 3.20 | 3.60 |
| 4 | fable-5-2 | **3.41** | 0.15 | 3.60 | 3.40 | 3.40 | 3.40 | 3.20 | 3.30 | 3.60 |
| 5 | gemini-4-neon | **3.27** | 0.24 | 3.60 | 3.00 | 3.30 | 3.10 | 3.10 | 3.60 | 3.20 |
| 6 | sonnet-5-5 | **3.23** | 0.15 | 3.30 | 3.10 | 3.10 | 3.20 | 3.10 | 3.50 | 3.30 |
| 7 | qwen-4-max | **3.19** | 0.29 | 3.50 | 3.40 | 3.20 | 2.60 | 3.20 | 3.10 | 3.30 |
| 8 | qwen-3-8-max-0902 | **3.16** | 0.38 | 3.10 | 3.60 | 3.00 | 3.10 | 3.70 | 2.60 | 3.00 |
| 9 | opus-5-5 | **3.11** | 0.27 | 3.50 | 3.20 | 2.60 | 3.10 | 3.20 | 3.10 | 3.10 |
| 10 | grok-4-7 | **3.06** | 0.24 | 3.00 | 3.00 | 2.80 | 3.20 | 3.10 | 2.80 | 3.50 |
| 11 | fable-5-1 | **3.00** | 0.23 | 3.00 | 3.00 | 3.20 | 3.20 | 2.80 | 2.60 | 3.20 |
| 12 | gpt-6-1-sol | **2.99** | 0.32 | 3.00 | 3.40 | 3.30 | 2.50 | 3.10 | 2.90 | 2.70 |
| 13 | deepseek-v4-pro | **2.94** | 0.50 | 2.10 | 2.70 | 2.70 | 3.30 | 3.50 | 2.90 | 3.40 |
| 14 | kimi-k3-1-pro | **2.91** | 0.30 | 3.00 | 2.70 | 3.00 | 3.50 | 2.70 | 2.60 | 2.90 |
| 15 | gemini-4-hydrogen | **2.90** | 0.32 | 3.00 | 2.50 | 3.30 | 2.70 | 2.90 | 3.30 | 2.60 |
| 16 | haiku-5-5 | **2.86** | 0.45 | 2.50 | 2.50 | 3.00 | 3.20 | 2.20 | 3.40 | 3.20 |
| 17 | glm-5-3 | **2.80** | 0.38 | 2.90 | 2.70 | 2.50 | 3.20 | 3.40 | 2.50 | 2.40 |
| 18 | minimax-m3-1-flash | **2.80** | 0.22 | 3.10 | 2.90 | 3.00 | 2.60 | 2.80 | 2.70 | 2.50 |
| 19 | gpt-6-luna | **2.79** | 0.23 | 2.70 | 2.80 | 2.80 | 2.50 | 2.90 | 2.60 | 3.20 |
| 20 | gpt-6-astra | **2.64** | 0.30 | 2.80 | 2.70 | 2.10 | 2.50 | 2.90 | 2.50 | 3.00 |
| 21 | gemini-4-carbon | **2.59** | 0.34 | 2.20 | 2.40 | 2.80 | 3.10 | 2.80 | 2.60 | 2.20 |
| 22 | gemini-4-argon | **2.47** | 0.20 | 2.20 | 2.30 | 2.60 | 2.60 | 2.70 | 2.30 | 2.60 |
| 23 | gpt-6-1-terra | **2.34** | 0.22 | 2.30 | 2.80 | 2.20 | 2.30 | 2.30 | 2.40 | 2.10 |

**Most consistent:** fable-5-2 (0.15), sonnet-5-5 (0.15), gemini-4-argon (0.20).
**Most volatile:** deepseek-v4-1-flash-1017 (0.50), deepseek-v4-pro (0.50), haiku-5-5 (0.45).
(Models with at least 3 days in the window.)

---

## About

Daily blind judging of each model's "AI Industry Pulse" summary from `daily-results/`. Maintained by Ogilvy.

- [SCORE-GRADERS.md](SCORE-GRADERS.md): which judge grades hardest and easiest.
- `daily/YYYY-MM-DD.md`: that day's ranking, per-judge scores, grader averages, self-preference check and judge notes.
- `json/YYYY-MM-DD.json`: the same data, machine-readable. The scripts use it to rebuild the leaderboard and to tell which days are already judged.
- [PROMPT.md](PROMPT.md): the exact judge prompt (v2, strict).
- [LEADERBOARD.md](LEADERBOARD.md): the same leaderboard as above, as its own file.

**Method.** Once a day's `token-costs/Usage-and-Cost-<date>.md` and `model-comparison/daily/Model-Consensus-<date>.md` both exist, the Pulse section is extracted from each HTML file and model names are removed. Each judge (opus = anthropic/claude-opus-5-5, glm = openrouter_eich/z-ai/glm-5.3, astra = openai/gpt-6-astra, grok = openrouter_grok/x-ai/grok-4.7, dsflash = openrouter_flash/deepseek/deepseek-v4.1-flash-1017; a 5-judge panel since Nov 11, applied to every day) gets its own random label shuffle and scores every summary from 1 to 5 against fixed anchors. A grammar error caps a summary at 3, and repeated hedging caps it at 3.5. The judges never see model names or each other's scores. Each judge also competes as a model, so every report includes a self-preference check.
