# Model summaries

All newly generated model summaries must be saved and committed to this repository under `summary/Model-Summary-YYYY-MM-DD.md`. Keep prior dated summaries. Avoid numbered download suffixes.

Preserve the established five-table layout: consensus score, API-equivalent cost, elapsed time, total tokens including cache, and effective cost per token scaled by 100,000,000. Append available new run days without inventing missing days or repricing historical columns. Tables come first; methodology follows.

Use latest corrected consensus reports and final selected-run usage audits, excluding superseded attempts. Include all 12 models. Use the conservative Qwen upper estimate. Means use available daily values; effective cost/token average is total costs divided by total tokens, then scaled, not an average of daily ratios. Sort score descending and all other tables ascending.

Verify source hashes, unchanged historical values, averages, sort order, table widths, and a lightweight rendered preview before committing and pushing. Verify the remote commit after push. No scheduled automation is enabled by these instructions.

## Audit-file layout

Keep readable Markdown reports at the top of `model-comparison/`, `token-costs/`, and `summary/`. Publish their JSON audit files in each directory’s `json/` subdirectory. Local working audits remain on disk at their existing generation paths; use the repository `json/` paths when reading published audits. Preserve report content and audit data when moving files.
