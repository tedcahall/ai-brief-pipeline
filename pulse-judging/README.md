# Pulse Judging

Daily blind judging of each model's "AI Industry Pulse" summary from `daily-results/`. Maintained by Ogilvy.

- [LEADERBOARD.md](LEADERBOARD.md): cumulative averages across all judged days.
- `daily/YYYY-MM-DD.md`: that day's ranking, per-judge scores, self-preference check and judge notes.
- `daily/YYYY-MM-DD.json`: the same data, machine-readable.
- [PROMPT.md](PROMPT.md): the exact judge prompt (v2, strict).

**Method.** Once a day's `token-costs/Usage-and-Cost-<date>.md` and `model-comparison/Model-Consensus-<date>.md` both exist, the Pulse section is extracted from each HTML file and model names are removed. Each judge (opus = anthropic/claude-opus-5-5, glm = openrouter_eich/z-ai/glm-5.3, astra = openai/gpt-6-astra) gets its own random label shuffle and scores every summary from 1 to 5 against fixed anchors. A grammar error caps a summary at 3, and repeated hedging caps it at 3.5. The judges never see model names or each other's scores. Each judge also competes as a model, so every report includes a self-preference check.
