# Same News. Different Editorial Decisions.

Give multiple AI models the same starting news evidence and ask each to build a daily briefing. What do they agree matters most? Where do their choices diverge—and what does each model notice that the others leave out?

This directory documents those decisions for Max’s AI Brief. It compares the headlines, stories, and social posts selected by different models, making their editorial choices visible rather than reducing every result to a single score.

## What you’ll find

- **Daily consensus reports** — model rankings, headline agreement, story and post vote counts, and individual model selections.
- **Focused comparisons** — analyses of production versus test editions, writing length, and selected execution routes.
- **JSON audits** — machine-readable supporting data in `json/`, for verification and further analysis.

Start with the most recent `Model-Consensus-*.md`. Read the overall ranking for orientation, then explore the vote tables and individual selections to understand why the scores differ.

## How the consensus score works

Each eligible edition contributes to a shared reference consensus. Stories about the same event are grouped even when models cite different URLs; social posts are matched by their numeric X status IDs.

| Component | Points | Basis |
|---|---:|---|
| Headline | 5 | Agreement with the headline consensus |
| Five stories | 45 | 9 points per matching story |
| Ten posts | 50 | 5 points per matching post |
| **Total** | **100** | **Selection agreement** |

All ties at the fifth-story and tenth-post cutoffs receive credit. Equal scores share ranks; speed does not break ties.

**Consensus is agreement—not ground truth.** Each model contributes to the reference against which it is scored. A high score means its choices closely match the group; it does not establish factual accuracy, writing quality, or superior general intelligence. A low-consensus selection may be a distraction—or a valuable discovery.

## What makes the comparison informative

The daily tests use saved starting evidence, allowing readers to inspect different selections from a shared news pool. That does not make the entire execution identical: sessions, runtime instructions, and follow-up research can differ. Individual reports document their cohort, evidence provenance, timing, and limitations.

Versioned model names distinguish releases. Elapsed time covers the broader workflow, including research, tool use, and validation—not just text generation.

For the economics behind these choices, see [token costs](../token-costs/). For patterns across days, see [summary](../summary/).
