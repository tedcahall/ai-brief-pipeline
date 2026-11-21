# Daily measurement and rollup contract

The finalizer admits one successful selected run per canonical model and edition date. Failed and replaced attempts do not become daily rows. Existing consensus and usage audits remain authoritative, with exact attempt/session checks where recorded. Historical cost estimates are never repriced. Cost ranges retain the published upper-estimate convention.

Daily files are `summary/daily/Model-Data-YYYY-MM-DD.md` and `summary/daily/json/Model-Data-YYYY-MM-DD.json`. JSON measurements are unrounded decimal strings or null, with per-measurement missing reasons and source hashes. Public provenance uses repository-relative paths. Unknown is never zero.

Eight metrics: Selection Score /100, API Cost (USD equivalent), Elapsed Time (seconds), Total Tokens including cache, ECPTS, Pulse Words, Story Words, Pulse Judge Score /5. ECPTS is cost / tokens × 100,000,000; period averages pool cost and tokens over the same positive-token paired days.

Sample SD (n-1) is present only for Selection Score, Elapsed Time, Pulse Words, Story Words and Pulse Judge Score. Fewer than two measurements gives unavailable SD. Original published reports and SDs are preserved in the legacy archive.

Word counts use the reader-visible archived HTML, never rewritten canonical text. The versioned section adapter identifies `#pulse` paragraphs and five `#stories` title/body pairs. Exclude titles, hidden text, script/style content and link attributes; include visible link text and decoded entities. A word is a whitespace-delimited unit containing a Unicode alphanumeric character. Extraction ambiguity produces unavailable with a reason. Source HTML is unchanged.

Rolling windows are seven/thirty calendar days ending at the as-of edition date, America/New_York. Weeks start Sunday; months are calendar months. Daily columns are newest first. Missing days are blank and do not pull older observations into the window. Open periods stop at the current as-of date. Rollup input is exclusively daily JSON. Completed snapshots are protected; changing source measurements requires an explicit `--revision` reason. Late judging uses `--enrich-date`, records source-completion revisions and touches only affected snapshots. Open weekly/monthly periods extend as new days arrive.

## Reusable commands

After copying accepted consensus, token-cost audits and HTML into their repository locations:

```sh
python3 scripts/build_daily_model_data.py --repo "$R" --date "$EDITION_DATE" --manifest "$WORK/daily-outputs.json"
python3 scripts/build_summary_rollups.py --repo "$R" --as-of "$EDITION_DATE" --manifest "$WORK/rollup-outputs.json"
python3 scripts/update_readme_leaderboard.py --repo "$R" --if-ready
```

Never copy or adapt a dated `build_summary.py` or `build.py`. New days select data, not code. Both builders accept `--from` and `--to` for a range. Daily base rebuilding of historical fallback-only data is not the backfill path; use the migration CLI.

Consensus Markdown belongs in `model-comparison/daily/`, focused comparisons in `model-comparison/comparisons/`, consensus audits in `model-comparison/json/`. Token-cost reports remain at their existing paths. Summary builders return explicit output manifests; stage only reviewed listed paths, plus the admitted input reports and managed README. Do not use `git add -A`.

## Judging write-back

Only an authorized publisher invokes the shared code in its own clone. This does not grant publishing permission. After complete Pulse JSON is ready:

```sh
python3 scripts/build_daily_model_data.py --repo "$R" --date "$EDITION_DATE" --enrich --manifest "$WORK/daily-outputs.json"
python3 scripts/build_summary_rollups.py --repo "$R" --as-of "$LATEST_EDITION_DATE" --enrich-date "$EDITION_DATE" --manifest "$WORK/rollup-outputs.json"
```

The latest edition date must come from the maximum existing daily JSON date, not the wall clock. The unrounded panel mean is calculated from `scores`, not the rounded `average` field. Full judge coverage and identical accepted-model cohort are required. Mismatch clears stale judge values to pending. A re-judge explicitly re-enriches, even if model membership is unchanged. Same inputs are byte-identical. A finalizer base rebuild revalidates the available panel against the accepted cohort.

Before publication, fetch and fast-forward a clean clone. Compute all outputs, verify the manifest allowlist, test, commit and push. On concurrent upstream changes, recompute from fresh upstream state, at most three attempts; never publish stale rebased calculations or force-push. A publisher failure must leave committed/recoverable local evidence and report a retryable error, not a dirty unattended checkout. Integration into Ogilvy's publisher is a separate coordinated activation step.
