# Pulse Judging

## Leaderboard

Moving average of the last 5 judged run(s) (window: up to 7), 11-7 to 11-11. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-7 | 11-8 | 11-9 | 11-10 | 11-11 |
|---|---|---|---|---|---|---|---|---|
| 1 | deepseek-v4-1-flash-1017 | **3.60** | 0.49 | 3.00 | 3.20 | 3.70 | 3.90 | 4.20 |
| 2 | opus-5-5 | **3.30** | 0.16 | 3.50 | 3.40 | 3.30 | 3.20 | 3.10 |
| 3 | sonnet-5-5 | **3.23** | 0.13 | – | 3.40 | 3.20 | 3.10 | 3.20 |
| 4 | grok-4-7 | **3.18** | 0.13 | 3.00 | 3.10 | 3.30 | 3.20 | 3.30 |
| 5 | qwen-3-8-max-0902 | **3.12** | 0.20 | 3.30 | 3.30 | 2.90 | 3.20 | 2.90 |
| 6 | kimi-k3-1-pro | **3.08** | 0.24 | 3.20 | 3.10 | 3.40 | 2.90 | 2.80 |
| 7 | deepseek-v4-pro | **3.04** | 0.15 | 2.90 | 3.20 | 3.20 | 2.90 | 3.00 |
| 8 | glm-5-3 | **3.00** | 0.53 | 3.70 | 2.70 | 3.10 | 2.30 | 3.20 |
| 9 | haiku-5-5 | **2.92** | 0.26 | – | 2.70 | 2.80 | 3.30 | 2.90 |
| 10 | fable-5-1 | **2.88** | 0.50 | – | 2.80 | 3.20 | 3.30 | 2.20 |
| 11 | minimax-m3-1-flash | **2.86** | 0.33 | 2.50 | 3.40 | 2.80 | 2.80 | 2.80 |
| 12 | gpt-6-astra | **2.84** | 0.51 | 2.70 | 2.20 | 2.70 | 3.60 | 3.00 |
| 13 | gpt-6-1-sol | **2.84** | 0.19 | 2.90 | 2.60 | 2.90 | 3.10 | 2.70 |
| 14 | gpt-6-luna | **2.70** | 0.35 | 2.50 | 2.70 | 2.50 | 3.30 | 2.50 |
| 15 | fable-5-2 | **2.70** | 0.14 | – | – | – | 2.60 | 2.80 |
| 16 | gemini-4-argon | **2.40** | 0.33 | – | 2.80 | 2.40 | 2.40 | 2.00 |
| 17 | gpt-6-1-terra | **2.24** | 0.15 | 2.30 | 2.00 | 2.20 | 2.30 | 2.40 |
| 18 | gemini-4-carbon | **2.10** | – | – | – | – | – | 2.10 |

**Most consistent:** sonnet-5-5 (0.13), grok-4-7 (0.13), gpt-6-1-terra (0.15).
**Most volatile:** glm-5-3 (0.53), gpt-6-astra (0.51), fable-5-1 (0.50).
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
