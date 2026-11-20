# Pulse Judging

## Leaderboard

Moving average of the last 7 judged run(s) (window: up to 7), 11-14 to 11-20. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-14 | 11-15 | 11-16 | 11-17 | 11-18 | 11-19 | 11-20 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | gpt-6-2-astra | **3.70** | 0.46 | – | – | – | – | 3.80 | 4.10 | 3.20 |
| 2 | deepseek-v4-1-flash-1017 | **3.63** | 0.43 | 3.40 | 3.10 | 3.70 | 3.40 | 4.10 | 3.40 | 4.30 |
| 3 | qwen-4-max | **3.40** | 0.28 | – | – | 3.50 | 3.50 | 2.90 | 3.60 | 3.50 |
| 4 | sonnet-5-5 | **3.39** | 0.35 | 3.20 | 3.40 | 2.80 | 3.80 | 3.40 | 3.80 | 3.30 |
| 5 | gpt-6-2-sol | **3.30** | 0.10 | – | – | – | – | 3.40 | 3.30 | 3.20 |
| 6 | kimi-k3-1-pro | **3.29** | 0.33 | 3.60 | 3.90 | 3.10 | 3.10 | 3.10 | 3.20 | 3.00 |
| 7 | opus-5-5 | **3.20** | 0.26 | 3.20 | 3.10 | 2.70 | 3.30 | 3.40 | 3.20 | 3.50 |
| 8 | fable-5-2 | **3.11** | 0.26 | 3.10 | 3.00 | 3.20 | 3.20 | 2.80 | 2.90 | 3.60 |
| 9 | qwen-3-8-max-0902 | **3.10** | 0.26 | 2.80 | 3.00 | 2.90 | 3.50 | 3.00 | 3.40 | 3.10 |
| 10 | fable-5-1 | **3.09** | 0.16 | 2.90 | 3.10 | 2.90 | 3.30 | 3.20 | 3.20 | 3.00 |
| 11 | glm-5-3 | **3.06** | 0.46 | 2.80 | 3.10 | 4.00 | 3.10 | 3.00 | 2.50 | 2.90 |
| 12 | deepseek-v4-pro | **3.04** | 0.55 | 3.70 | 3.10 | 3.70 | 2.80 | 3.00 | 2.90 | 2.10 |
| 13 | minimax-m3-1-flash | **3.01** | 0.18 | 2.90 | 3.20 | 2.70 | 3.00 | 3.20 | 3.00 | 3.10 |
| 14 | gemini-4-hydrogen | **3.00** | 0.10 | 2.80 | 3.10 | 3.00 | 3.00 | 3.00 | 3.10 | 3.00 |
| 15 | haiku-5-5 | **2.96** | 0.31 | 3.20 | 3.20 | 2.60 | 2.90 | 3.30 | 3.00 | 2.50 |
| 16 | gemini-4-neon | **2.95** | 0.92 | – | – | – | – | – | 2.30 | 3.60 |
| 17 | grok-4-7 | **2.91** | 0.18 | 3.10 | 2.80 | 3.10 | 2.70 | 2.70 | 3.00 | 3.00 |
| 18 | gpt-6-astra | **2.81** | 0.27 | 3.20 | 2.80 | 2.40 | 2.60 | 3.10 | 2.80 | 2.80 |
| 19 | gpt-6-1-sol | **2.73** | 0.28 | 2.90 | 3.00 | 2.20 | 2.70 | 2.60 | 2.70 | 3.00 |
| 20 | gpt-6-luna | **2.59** | 0.36 | 2.60 | 1.80 | 2.60 | 2.80 | 2.90 | 2.70 | 2.70 |
| 21 | gemini-4-carbon | **2.53** | 0.37 | 2.40 | 2.70 | 2.30 | 3.00 | 3.00 | 2.10 | 2.20 |
| 22 | gemini-4-argon | **2.47** | 0.30 | 2.30 | 2.50 | 2.30 | 2.50 | 3.10 | 2.40 | 2.20 |
| 23 | gpt-6-1-terra | **2.31** | 0.15 | 2.30 | 2.20 | 2.10 | 2.50 | 2.30 | 2.50 | 2.30 |

**Most consistent:** gpt-6-2-sol (0.10), gemini-4-hydrogen (0.10), gpt-6-1-terra (0.15).
**Most volatile:** deepseek-v4-pro (0.55), glm-5-3 (0.46), gpt-6-2-astra (0.46).
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
