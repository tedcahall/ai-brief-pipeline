# Score Graders

Which judge grades hardest and which grades easiest. Each number is the average score a judge gave across all models that day; lower means a harder grader.

## Overall (5 judged days, 11-7 to 11-11)

| Rank (hardest first) | Judge | Avg grade | Days hardest | Days easiest |
|---|---|---|---|---|
| 1 | astra | **2.62** | 5 | 0 |
| 2 | opus | **3.01** | 0 | 0 |
| 3 | glm | **3.31** | 0 | 5 |

## By day

| Date | opus | glm | astra | Hardest | Easiest | Spread |
|---|---|---|---|---|---|---|
| 11-11 | 2.94 | 3.33 | 2.50 | astra | glm | 0.83 |
| 11-10 | 3.09 | 3.38 | 2.62 | astra | glm | 0.76 |
| 11-9 | 3.19 | 3.34 | 2.72 | astra | glm | 0.62 |
| 11-8 | 2.91 | 3.19 | 2.69 | astra | glm | 0.50 |
| 11-7 | 2.92 | 3.29 | 2.58 | astra | glm | 0.71 |

Judges: opus = anthropic/claude-opus-5-5, glm = openrouter_eich/z-ai/glm-5.3, astra = openai/gpt-6-astra. Per-day detail is in each [daily](daily/) report under "Grader averages".
