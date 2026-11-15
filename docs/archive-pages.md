# Daily model archive

The archive begins at [daily-results](../daily-results/index.html), with dates newest first in a responsive grid. Each date has a comparison viewer adapted from Dennis’s original tool. Mobile shows model links first, with comparison optional.

## Automatic updates

The `Build archive and deploy Pages` workflow runs on each main-branch push and can be dispatched manually. It checks out current main, discovers actual `daily-results/YYYY-MM-DD/model/*.html` reports, writes all daily indexes plus the archive index and manifest, commits changed indexes, and deploys that exact revision to GitHub Pages. Serialized runs and bounded push retries protect against overlapping publishers. No cron or inference calls are involved.

Pages uses **GitHub Actions** as its build source. Deployment is explicit in this workflow: it does not depend on a bot-generated commit triggering another Pages build. Existing report URLs and files remain unchanged. The artifact contains tracked repository files, preserving existing static paths.

## Local generation

Install Python 3, GNU date, and `beautifulsoup4==4.14.3`, then run:

```sh
python scripts/brief_archive/build.py
```

An optional positional argument selects a different daily-results directory. The generator discovers legacy `brief.html` filenames as well as dated filenames. Empty day directories are not listed. Counts are available reports, not performance or success scores. All generated navigation uses relative paths for compatibility with the repository’s Pages prefix.

- Generator: `scripts/brief_archive/build.py`
- Dennis source template: `scripts/brief_archive/reference/dennis-original.html`
- Adapted viewer logic: `scripts/brief_archive/reference/viewer.js`
- Design assets: `daily-results/assets/`

Newer/older navigation carries stable model IDs, not dated filenames. Unavailable selections temporarily fall back with a notice, retaining the request for subsequent day navigation. Existing full-path comparison hashes remain supported. Reports are sandboxed without script execution within comparison panes.

Artwork is the existing Max’s AI Brief homepage artwork, resized for the archive. Original tool supplied by Dennis; archive styling and layout integration by Max.

## Deferred

Add the actual published newsletter as a clearly labeled reference edition for each day. Do not infer that any alternate-model test output is the published edition. This enhancement was explicitly deferred by Ted.
