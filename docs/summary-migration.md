# Summary migration staging record

Baseline: `b46257ce9af64eeae7db271a97a581fed28cc431`. Migration code is date-neutral and uses preserved accepted sources, not model reruns or historical repricing.

## Preserved originals and recovery

`summary/json/migration-manifest.json` records every original path, destination and SHA-256. Cumulative Markdown and audit files live under `summary/daily/z-original-data/`. Consensus Markdown moved to `model-comparison/daily/`; focused comparisons moved to `model-comparison/comparisons/`. Old external direct URLs may break. The original reports, pricing, Pulse results and model HTML remain unchanged.

The latest published cumulative audit is the explicit historical baseline. Daily consensus/selected-usage audits are preferred and reconciled against it, cell by cell. Where those audits do not exist or omit a historical measurement, preserve the published cumulative value with fallback provenance. Any conflicting numeric measurement is reported for review, not averaged or silently corrected.

The staged backfill recovers 22 edition dates and 369 accepted model/day rows. All 369 have Pulse and five-story counts, independently recounted with a second HTML parser. API cost, tokens and ECPTS have 345 values; elapsed has 368; Pulse panel means have 285. Earlier HTML-only dates without accepted consensus evidence are reported separately, not promoted into admitted measurements. Historical absent panels are unavailable, not pending future judging. No-data days are not zero-valued observations.

Run a non-mutating source dry run:

```sh
python3 scripts/migrate_summary_history.py --repo /path/to/isolated-clone --report-dir /tmp/migration-review
```

It copies the checkout into a temporary directory, then performs the entire migration there. Only the specified review directory is written outside that copy. `--apply` performs the same work in the selected checkout and must be used only in the isolated staging clone until cutover is authorized. Review coverage.json for per-model gaps, conflicts and provenance. Historical labels with no original HTML hash are explicitly identified as published-edition-path binding rather than hash-proven attempt binding.

## Verification and limits

Staging verification includes original hash preservation, exact legacy numeric parity, independent HTML recounts, independent sample-SD calculations, deterministic reruns, Markdown table widths, archive-index regeneration parity, and representative local browser previews. The original archive/Pages generator was not changed. Real GitHub Actions execution, public rendering and the first daily finalizer-plus-judging sequence are separate post-cutover checks. Do not dispatch the production workflows against a staging branch: they intentionally check out main and can push to main.

A proposed finalizer diff lives outside this repository for Ken's review. It is not installed by this migration. Ogilvy's completion hook and explicit publisher staging integration must be coordinated separately; repository code alone does not activate write-back. No schedule, model, judge prompt, production newsletter or pricing job was changed.

## Rollback

Retain the baseline commit, finalizer baseline hash and migration manifest. Revert migration-owned commits on top of current main, preserving intervening pricing, report, judging and bot commits; never reset or force-push shared main. Restore the prior finalizer only after restoring its legacy inputs. If a new edition arrived in the new format, rebuild its legacy view from preserved daily JSON before re-enabling the old reader. Keep new daily measurements and private coverage evidence for repair. A local staging clone is not authority to publish.
