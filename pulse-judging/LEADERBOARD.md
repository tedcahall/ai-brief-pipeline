# Pulse Judging Leaderboard

Moving average of the last 7 judged run(s) (window: up to 7), 11-7 to 11-13. Each date column is that day's panel average for the model (all judges); a dash means the model did not run that day. Avg is the mean of the days the model ran. SD is the standard deviation of those days: low means consistent, high means it swings.

| Rank | Model | Avg | SD | 11-7 | 11-8 | 11-9 | 11-10 | 11-11 | 11-12 | 11-13 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | deepseek-v4-1-flash-1017 | **3.47** | 0.46 | 3.00 | 3.20 | 3.70 | 3.90 | 4.20 | 3.20 | 3.10 |
| 2 | opus-5-5 | **3.33** | 0.14 | 3.50 | 3.40 | 3.30 | 3.20 | 3.10 | 3.40 | 3.40 |
| 3 | gemini-4-hydrogen | **3.20** | – | – | – | – | – | – | – | 3.20 |
| 4 | grok-4-7 | **3.20** | 0.12 | 3.00 | 3.10 | 3.30 | 3.20 | 3.30 | 3.20 | 3.30 |
| 5 | qwen-3-8-max-0902 | **3.20** | 0.41 | 3.30 | 3.30 | 2.90 | 3.20 | 2.90 | 4.00 | 2.80 |
| 6 | sonnet-5-5 | **3.18** | 0.13 | – | 3.40 | 3.20 | 3.10 | 3.20 | 3.00 | 3.20 |
| 7 | kimi-k3-1-pro | **3.11** | 0.21 | 3.20 | 3.10 | 3.40 | 2.90 | 2.80 | 3.30 | 3.10 |
| 8 | deepseek-v4-pro | **3.07** | 0.24 | 2.90 | 3.20 | 3.20 | 2.90 | 3.00 | 2.80 | 3.50 |
| 9 | glm-5-3 | **3.06** | 0.48 | 3.70 | 2.70 | 3.10 | 2.30 | 3.20 | 2.90 | 3.50 |
| 10 | minimax-m3-1-flash | **3.00** | 0.37 | 2.50 | 3.40 | 2.80 | 2.80 | 2.80 | 3.50 | 3.20 |
| 11 | haiku-5-5 | **2.93** | 0.21 | – | 2.70 | 2.80 | 3.30 | 2.90 | 2.90 | 3.00 |
| 12 | fable-5-1 | **2.92** | 0.47 | – | 2.80 | 3.20 | 3.30 | 2.20 | 3.40 | 2.60 |
| 13 | fable-5-2 | **2.88** | 0.43 | – | – | – | 2.60 | 2.80 | 3.50 | 2.60 |
| 14 | gpt-6-1-sol | **2.84** | 0.16 | 2.90 | 2.60 | 2.90 | 3.10 | 2.70 | 2.80 | 2.90 |
| 15 | gpt-6-astra | **2.80** | 0.44 | 2.70 | 2.20 | 2.70 | 3.60 | 3.00 | 2.50 | 2.90 |
| 16 | gpt-6-luna | **2.67** | 0.37 | 2.50 | 2.70 | 2.50 | 3.30 | 2.50 | 3.00 | 2.20 |
| 17 | gemini-4-argon | **2.48** | 0.29 | – | 2.80 | 2.40 | 2.40 | 2.00 | 2.60 | 2.70 |
| 18 | gemini-4-carbon | **2.40** | 0.30 | – | – | – | – | 2.10 | 2.70 | 2.40 |
| 19 | gpt-6-1-terra | **2.33** | 0.21 | 2.30 | 2.00 | 2.20 | 2.30 | 2.40 | 2.70 | 2.40 |

**Most consistent:** grok-4-7 (0.12), sonnet-5-5 (0.13), opus-5-5 (0.14).
**Most volatile:** glm-5-3 (0.48), fable-5-1 (0.47), deepseek-v4-1-flash-1017 (0.46).
(Models with at least 3 days in the window.)

Daily reports, with each judge's scores and notes: [daily/](daily/)
