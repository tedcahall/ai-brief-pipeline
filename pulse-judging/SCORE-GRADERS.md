# Score Graders

Which judge grades hardest and which grades easiest. Each number is the average score a judge gave across all models that day; lower means a harder grader.

## Overall (19 judged days, 10-28 to 11-21)

| Rank (hardest first) | Judge | Avg grade | Days hardest | Days easiest |
|---|---|---|---|---|
| 1 | astra | **2.72** | 12 | 0 |
| 2 | dsflash | **2.82** | 5 | 0 |
| 3 | grok | **2.95** | 0 | 0 |
| 4 | opus | **3.00** | 2 | 1 |
| 5 | glm | **3.40** | 0 | 18 |

## By day

| Date | opus | glm | astra | grok | dsflash | Hardest | Easiest | Spread |
|---|---|---|---|---|---|---|---|---|
| 11-21 | 3.00 | 3.43 | 2.76 | 2.96 | 2.65 | dsflash | glm | 0.78 |
| 11-20 | 2.96 | 3.30 | 2.85 | 2.89 | 3.02 | astra | glm | 0.45 |
| 11-19 | 3.04 | 3.37 | 2.80 | 3.02 | 2.78 | dsflash | glm | 0.59 |
| 11-18 | 3.20 | 3.39 | 2.75 | 3.23 | 2.95 | astra | glm | 0.64 |
| 11-17 | 3.02 | 3.65 | 2.90 | 2.88 | 2.73 | dsflash | glm | 0.92 |
| 11-16 | 2.85 | 3.33 | 2.65 | 2.95 | 2.67 | astra | glm | 0.68 |
| 11-15 | 3.08 | 3.29 | 2.71 | 2.82 | 2.87 | astra | glm | 0.58 |
| 11-14 | 3.26 | 3.21 | 2.74 | 2.82 | 2.82 | astra | opus | 0.52 |
| 11-13 | 2.76 | 3.34 | 2.76 | 3.00 | 2.87 | opus | glm | 0.58 |
| 11-12 | 3.03 | 3.83 | 2.72 | 2.89 | 2.92 | astra | glm | 1.11 |
| 11-11 | 2.94 | 3.33 | 2.50 | 2.64 | 2.78 | astra | glm | 0.83 |
| 11-10 | 3.09 | 3.38 | 2.62 | 3.06 | 2.97 | astra | glm | 0.76 |
| 11-9 | 3.19 | 3.34 | 2.72 | 2.91 | 2.72 | astra | glm | 0.62 |
| 11-8 | 2.91 | 3.19 | 2.69 | 3.16 | 2.62 | dsflash | glm | 0.57 |
| 11-7 | 2.92 | 3.29 | 2.58 | 3.04 | 2.96 | astra | glm | 0.71 |
| 10-31 | 2.83 | 3.38 | 2.88 | 2.96 | 2.92 | opus | glm | 0.55 |
| 10-30 | 2.92 | 3.46 | 2.67 | 3.00 | 2.83 | astra | glm | 0.79 |
| 10-29 | 2.96 | 3.54 | 2.79 | 2.92 | 2.75 | dsflash | glm | 0.79 |
| 10-28 | 3.04 | 3.58 | 2.58 | 2.83 | 2.83 | astra | glm | 1.00 |

Judges: opus = anthropic/claude-opus-5-5, glm = openrouter_eich/z-ai/glm-5.3, astra = openai/gpt-6-astra, grok = openrouter_grok/x-ai/grok-4.7, dsflash = openrouter_flash/deepseek/deepseek-v4.1-flash-1017. Per-day detail is in each [daily](daily/) report under "Grader averages".
