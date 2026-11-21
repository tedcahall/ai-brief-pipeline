# README leaderboard

Input is committed `summary/json/rollups/rolling-7-day/Model-Summary-YYYY-MM-DD.json`, never the legacy cumulative summaries. Use seven calendar days and at least four distinct observations per model/metric. All columns include only eligible models; ties use unrounded values. An unavailable metric renders its own unavailable row and does not hold the other rows.

Leaders prefer higher selection/judging/verbosity, lower cost/time/tokens and lower SD. Verbosity is length, not quality. SD rows use sample SD (n-1); the Mv Avg column is a window statistic, not a mean of daily SDs. Selection SD follows Ed Selection. Pulse and Story Verbosity each have mean and SD rows.

Publish non-judging rows immediately. While judging is pending, retain the latest complete judging snapshot with its actual as-of date and a pending label. Without a complete prior snapshot, judging rows are unavailable. Late write-back refreshes committed rollups, then this generator reads them.

Run `python3 scripts/update_readme_leaderboard.py --output /tmp/readme-preview.md` for a non-mutating standalone preview. Without `--output`, only the managed README block changes. GitHub Actions writes only README, recomputing from current main after a push race. A GITHUB_TOKEN commit does not trigger Pages, so its README copy may lag until the next ordinary push.
