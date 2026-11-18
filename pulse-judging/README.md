# Pulse Judging

## Leaderboard

Moving average of the last 7 judged run(s) (window: up to 7), 11-12 to 11-18. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-12 | 11-13 | 11-14 | 11-15 | 11-16 | 11-17 | 11-18 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | gpt-6-2-astra | **3.80** | – | – | – | – | – | – | – | 3.80 |
| 2 | deepseek-v4-1-flash-1017 | **3.43** | 0.36 | 3.20 | 3.10 | 3.40 | 3.10 | 3.70 | 3.40 | 4.10 |
| 3 | gpt-6-2-sol | **3.40** | – | – | – | – | – | – | – | 3.40 |
| 4 | kimi-k3-1-pro | **3.31** | 0.32 | 3.30 | 3.10 | 3.60 | 3.90 | 3.10 | 3.10 | 3.10 |
| 5 | qwen-4-max | **3.30** | 0.35 | – | – | – | – | 3.50 | 3.50 | 2.90 |
| 6 | sonnet-5-5 | **3.26** | 0.32 | 3.00 | 3.20 | 3.20 | 3.40 | 2.80 | 3.80 | 3.40 |
| 7 | deepseek-v4-pro | **3.23** | 0.40 | 2.80 | 3.50 | 3.70 | 3.10 | 3.70 | 2.80 | 3.00 |
| 8 | opus-5-5 | **3.21** | 0.25 | 3.40 | 3.40 | 3.20 | 3.10 | 2.70 | 3.30 | 3.40 |
| 9 | glm-5-3 | **3.20** | 0.42 | 2.90 | 3.50 | 2.80 | 3.10 | 4.00 | 3.10 | 3.00 |
| 10 | qwen-3-8-max-0902 | **3.14** | 0.45 | 4.00 | 2.80 | 2.80 | 3.00 | 2.90 | 3.50 | 3.00 |
| 11 | minimax-m3-1-flash | **3.10** | 0.26 | 3.50 | 3.20 | 2.90 | 3.20 | 2.70 | 3.00 | 3.20 |
| 12 | fable-5-1 | **3.06** | 0.28 | 3.40 | 2.60 | 2.90 | 3.10 | 2.90 | 3.30 | 3.20 |
| 13 | fable-5-2 | **3.06** | 0.29 | 3.50 | 2.60 | 3.10 | 3.00 | 3.20 | 3.20 | 2.80 |
| 14 | gemini-4-hydrogen | **3.02** | 0.13 | – | 3.20 | 2.80 | 3.10 | 3.00 | 3.00 | 3.00 |
| 15 | haiku-5-5 | **3.01** | 0.24 | 2.90 | 3.00 | 3.20 | 3.20 | 2.60 | 2.90 | 3.30 |
| 16 | grok-4-7 | **2.99** | 0.25 | 3.20 | 3.30 | 3.10 | 2.80 | 3.10 | 2.70 | 2.70 |
| 17 | gpt-6-astra | **2.79** | 0.30 | 2.50 | 2.90 | 3.20 | 2.80 | 2.40 | 2.60 | 3.10 |
| 18 | gpt-6-1-sol | **2.73** | 0.27 | 2.80 | 2.90 | 2.90 | 3.00 | 2.20 | 2.70 | 2.60 |
| 19 | gemini-4-carbon | **2.64** | 0.29 | 2.70 | 2.40 | 2.40 | 2.70 | 2.30 | 3.00 | 3.00 |
| 20 | gemini-4-argon | **2.57** | 0.28 | 2.60 | 2.70 | 2.30 | 2.50 | 2.30 | 2.50 | 3.10 |
| 21 | gpt-6-luna | **2.56** | 0.42 | 3.00 | 2.20 | 2.60 | 1.80 | 2.60 | 2.80 | 2.90 |
| 22 | gpt-6-1-terra | **2.36** | 0.20 | 2.70 | 2.40 | 2.30 | 2.20 | 2.10 | 2.50 | 2.30 |

**Most consistent:** gemini-4-hydrogen (0.13), gpt-6-1-terra (0.20), haiku-5-5 (0.24).
**Most volatile:** qwen-3-8-max-0902 (0.45), gpt-6-luna (0.42), glm-5-3 (0.42).
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
