#!/usr/bin/env python3
"""One-time history conversion. Dry-run by default, against a disposable copy."""
import argparse
import shutil
import tempfile
from collections import Counter
from build_daily_model_data import build, write_daily, HIST_NAMES, BASE_KEYS
from build_summary_rollups import generate
from summary_metrics import *

COMPARISON_METHOD = '## How the consensus score works\n\nEach eligible edition contributes to a shared reference consensus. Stories about the same event are grouped even when models cite different URLs; social posts are matched by their numeric X status IDs.\n\n| Component | Points | Basis |\n|---|---:|---|\n| Headline | 5 | Agreement with the headline consensus |\n| Five stories | 45 | 9 points per matching story |\n| Ten posts | 50 | 5 points per matching post |\n| **Total** | **100** | **Selection agreement** |\n\nAll ties at the fifth-story and tenth-post cutoffs receive credit. Equal scores share ranks; speed does not break ties.\n\n**Consensus is agreement; not ground truth.** Each model contributes to the reference against which it is scored. A high score means its choices closely match the group; it does not establish factual accuracy, writing quality, or superior general intelligence. A low-consensus selection may be a distraction; or a valuable discovery.\n\n## What makes the comparison informative\n\nThe daily tests use saved starting evidence, allowing readers to inspect different selections from a shared news pool. That does not make the entire execution identical: sessions, runtime instructions, and follow-up research can differ. Individual reports document their cohort, evidence provenance, timing, and limitations.\n\nVersioned model names distinguish releases. Elapsed time covers the broader workflow, including research, tool use, and validation; not just text generation.\n\nFor the economics behind these choices, see [token costs](../token-costs/). For patterns across days, see [summary](../summary/).\n'

def migrate(root):
    archive=root/'summary/daily/z-original-data'
    legacy_files=sorted((root/'summary/json').glob('Model-Summary-*.audit.json'))
    if not legacy_files:legacy_files=sorted((archive/'json').glob('Model-Summary-*.audit.json'))
    if not legacy_files:raise ValueError('No preserved legacy audits to migrate')
    baseline=legacy_files[-1]
    legacy=read_json(baseline)
    days=sorted(legacy['scores'])
    moves={}
    for p in sorted((root/'summary').glob('Model-Summary-*.md')):moves[p]=archive/p.name
    for p in legacy_files:
        if p.parent!=archive/'json':moves[p]=archive/'json'/p.name
    for p in sorted((root/'model-comparison').glob('*.md')):
        if p.name!='README.md':moves[p]=p.parent/('daily' if p.name.startswith('Model-Consensus-') else 'comparisons')/p.name
    previous=root/'summary/json/migration-manifest.json'
    manifest=read_json(previous).get('originals',[]) if previous.exists() else []
    for old,new in moves.items():
        manifest.append({'original':str(old.relative_to(root)),'destination':str(new.relative_to(root)),'sha256':sha(old)})
        if new.exists() and sha(new)!=sha(old):raise ValueError(f'Archive collision: {new}')
    for old,new in moves.items():
        new.parent.mkdir(parents=True,exist_ok=True);old.rename(new)
    baseline=moves.get(baseline,baseline)
    outputs=[];coverage=[];conflicts=[]
    for day in days:
        obj=build(root,day,baseline)
        if day<max(days) and not (root/f'pulse-judging/json/{day}.json').exists():
            obj['judging']={'status':'unavailable','reason':'historical panel was not collected; no new judging requested'}
            for row in obj['models'].values():row['missing']['pulse_judge_score']='historical panel unavailable'
        outputs+=write_daily(root,obj);conflicts+=obj['conflicts']
        for model,row in obj['models'].items():
            coverage.append({'date':day,'model':model,'available':[k for k,v in row['metrics'].items() if v is not None], 'missing':row['missing'],'provenance':row['provenance']})
    outputs+=generate(root,days,revision='initial historical migration')
    for entry in manifest:
        if sha(root/entry['destination'])!=entry['sha256']:raise ValueError('Archive verification failed')
    # Record disagreements among cumulative snapshots, without silently selecting the newest by mtime.
    changes=[];seen={}
    for p in sorted((archive/'json').glob('*.audit.json')):
        obj=read_json(p)
        for key in BASE_KEYS.values():
            for day,rows in obj.get(key,{}).items():
                for model,value in rows.items():
                    ident=(key,day,HIST_NAMES.get(model,model));v=numeric(value)
                    if ident in seen and seen[ident][0]!=v:
                        changes.append({'metric':key,'date':day,'model':ident[2],'before':seen[ident][0],'after':v,'source':str(p.relative_to(root))})
                    seen[ident]=(v,str(p.relative_to(root)))
    totals=Counter(k for row in coverage for k in row['available'])
    html_dates=sorted(p.name for p in (root/'daily-results').iterdir() if p.is_dir() and re.fullmatch(r'\d{4}-\d{2}-\d{2}',p.name))
    report={'schema_version':1,'baseline':source_entry(root,baseline),'days':days,'daily_rows':len(coverage),'available_by_metric':dict(totals),
       'coverage':coverage,'daily_vs_cumulative_conflicts':conflicts,'cumulative_revision_history':changes,
       'html_dates_without_consensus_measurements':sorted(set(html_dates)-set(days)),
       'missing_calendar_dates':sorted(set(dates(days[0],days[-1]))-set(days)), 'originals':manifest,
       'outputs':sorted(set(outputs)), 'status':'review_required' if conflicts or changes else 'staged'}
    public={'schema_version':1,'baseline':report['baseline'],'days':days,'daily_rows':len(coverage),'available_by_metric':dict(totals),'originals':manifest,
       'daily_vs_cumulative_conflicts':conflicts,'cumulative_revision_history':changes,'missing_calendar_dates':report['missing_calendar_dates']}
    atomic_write(root/'summary/json/migration-manifest.json',dumps(public))
    latest=max(days)
    atomic_write(root/'model-comparison/README.md',f'# Model comparison\n\n[Latest daily report](daily/Model-Consensus-{latest}.md)\n\n- [Daily reports](daily/)\n- [Focused comparisons](comparisons/)\n- [Audits](json/)\n- [Summaries](../summary/)\n- [Token costs](../token-costs/)\n\nScores measure agreement with the daily cohort, not factual accuracy. Historical reports are preserved byte-for-byte.\n\n'+COMPARISON_METHOD)
    return report

def source_entry(root,p):return {'path':str(p.relative_to(root)),'sha256':sha(p)}
def report_text(r):
    lines=['# Migration coverage checkpoint','',f"Status: {r['status']}. {len(r['days'])} daily files; {r['daily_rows']} accepted model/day rows.",'','| Metric | Available rows |','|---|---:|']
    lines += [f'| {k} | {r["available_by_metric"].get(k,0)} |' for k in METRICS]
    lines += ['',f"Daily audit versus cumulative conflicts: {len(r['daily_vs_cumulative_conflicts'])}.",f"Changes across historical cumulative snapshots: {len(r['cumulative_revision_history'])}.",f"Hash-verified moved originals: {len(r['originals'])}.",f"Missing calendar dates: {', '.join(r['missing_calendar_dates'])}.",f"HTML dates without accepted consensus measurements: {', '.join(r['html_dates_without_consensus_measurements'])}.",'','No missing measurements were invented. No model or judge calls were made. Detailed per-date/model provenance and gaps are in coverage.json. Production activation and downstream publishing remain unverified.']
    return '\n'.join(lines)+'\n'
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--apply',action='store_true');p.add_argument('--report-dir',type=Path,required=True);a=p.parse_args()
    if a.apply:r=migrate(a.repo)
    else:
        with tempfile.TemporaryDirectory(prefix='summary-migration-dry-') as tmp:
            root=Path(tmp)/'repo';shutil.copytree(a.repo,root,ignore=shutil.ignore_patterns('.git','__pycache__'));r=migrate(root)
    a.report_dir.mkdir(parents=True,exist_ok=True);atomic_write(a.report_dir/'coverage.json',dumps(r));atomic_write(a.report_dir/'coverage.md',report_text(r));print(report_text(r))
if __name__=='__main__':main()
