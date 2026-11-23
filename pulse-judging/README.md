# Pulse Judging

## Leaderboard

Moving average of the last 7 judged run(s) (window: up to 7), 11-17 to 11-23. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-17 | 11-18 | 11-19 | 11-20 | 11-21 | 11-22 | 11-23 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | deepseek-v4-1-flash-1017 | **3.67** | 0.42 | 3.40 | 4.10 | 3.40 | 4.30 | 3.60 | 3.10 | 3.80 |
| 2 | gpt-6-2-astra | **3.60** | 0.33 | – | 3.80 | 4.10 | 3.20 | 3.40 | 3.40 | 3.70 |
| 3 | gpt-6-2-sol | **3.42** | 0.38 | – | 3.40 | 3.30 | 3.20 | 3.00 | 4.10 | 3.50 |
| 4 | sonnet-5-5 | **3.39** | 0.30 | 3.80 | 3.40 | 3.80 | 3.30 | 3.10 | 3.10 | 3.20 |
| 5 | fable-5-2 | **3.24** | 0.29 | 3.20 | 2.80 | 2.90 | 3.60 | 3.40 | 3.40 | 3.40 |
| 6 | qwen-3-8-max-0902 | **3.24** | 0.25 | 3.50 | 3.00 | 3.40 | 3.10 | 3.60 | 3.00 | 3.10 |
| 7 | qwen-4-max | **3.24** | 0.37 | 3.50 | 2.90 | 3.60 | 3.50 | 3.40 | 3.20 | 2.60 |
| 8 | opus-5-5 | **3.19** | 0.29 | 3.30 | 3.40 | 3.20 | 3.50 | 3.20 | 2.60 | 3.10 |
| 9 | fable-5-1 | **3.16** | 0.11 | 3.30 | 3.20 | 3.20 | 3.00 | 3.00 | 3.20 | 3.20 |
| 10 | kimi-k3-1-pro | **3.09** | 0.24 | 3.10 | 3.10 | 3.20 | 3.00 | 2.70 | 3.00 | 3.50 |
| 11 | gemini-4-neon | **3.06** | 0.48 | – | – | 2.30 | 3.60 | 3.00 | 3.30 | 3.10 |
| 12 | minimax-m3-1-flash | **2.97** | 0.19 | 3.00 | 3.20 | 3.00 | 3.10 | 2.90 | 3.00 | 2.60 |
| 13 | gemini-4-hydrogen | **2.94** | 0.26 | 3.00 | 3.00 | 3.10 | 3.00 | 2.50 | 3.30 | 2.70 |
| 14 | grok-4-7 | **2.91** | 0.19 | 2.70 | 2.70 | 3.00 | 3.00 | 3.00 | 2.80 | 3.20 |
| 15 | haiku-5-5 | **2.91** | 0.31 | 2.90 | 3.30 | 3.00 | 2.50 | 2.50 | 3.00 | 3.20 |
| 16 | gpt-6-1-sol | **2.89** | 0.35 | 2.70 | 2.60 | 2.70 | 3.00 | 3.40 | 3.30 | 2.50 |
| 17 | glm-5-3 | **2.84** | 0.28 | 3.10 | 3.00 | 2.50 | 2.90 | 2.70 | 2.50 | 3.20 |
| 18 | deepseek-v4-pro | **2.79** | 0.37 | 2.80 | 3.00 | 2.90 | 2.10 | 2.70 | 2.70 | 3.30 |
| 19 | gpt-6-luna | **2.74** | 0.13 | 2.80 | 2.90 | 2.70 | 2.70 | 2.80 | 2.80 | 2.50 |
| 20 | gemini-4-carbon | **2.66** | 0.42 | 3.00 | 3.00 | 2.10 | 2.20 | 2.40 | 2.80 | 3.10 |
| 21 | gpt-6-astra | **2.66** | 0.31 | 2.60 | 3.10 | 2.80 | 2.80 | 2.70 | 2.10 | 2.50 |
| 22 | gemini-4-argon | **2.53** | 0.29 | 2.50 | 3.10 | 2.40 | 2.20 | 2.30 | 2.60 | 2.60 |
| 23 | gpt-6-1-terra | **2.41** | 0.20 | 2.50 | 2.30 | 2.50 | 2.30 | 2.80 | 2.20 | 2.30 |

**Most consistent:** fable-5-1 (0.11), gpt-6-luna (0.13), grok-4-7 (0.19).
**Most volatile:** gemini-4-neon (0.48), deepseek-v4-1-flash-1017 (0.42), gemini-4-carbon (0.42).
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
