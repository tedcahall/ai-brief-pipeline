#!/usr/bin/env python3
"""Generate calendar rollups from daily data only. No legacy inputs or provider calls."""
import argparse
import copy
from summary_metrics import *

FAMILIES=('rolling-7-day','rolling-30-day','weekly','monthly')

def load_daily(root):
    result={}
    for path in sorted((root/'summary/daily/json').glob('Model-Data-*.json')):
        obj=validate_daily(read_json(path))
        if obj['date'] in result:raise ValueError('Duplicate daily date')
        result[obj['date']]=obj
    return result

def basename(day,family):
    if family=='weekly':return 'week-'+window(day,family)[0]
    if family=='monthly':return day[:7]
    return 'Model-Summary-'+day

def make_rollup(daily,day,family):
    start,end=window(day,family)
    chosen={d:o for d,o in daily.items() if start<=d<=end}
    nonjudge={d:{m:{k:v for k,v in r['metrics'].items() if k!='pulse_judge_score'} for m,r in o['models'].items()} for d,o in chosen.items()}
    return {'schema_version':VERSION,'calculation_version':VERSION,'family':family,'as_of':day,'start':start,'end':end,
      'dates':list(reversed(dates(start,end))), 'observed_dates':sorted(chosen),
      'inputs':{d:digest(o) for d,o in chosen.items()},'base_measurement_hash':digest(nonjudge),
      'judging_status':('pending' if any(o['judging']['status']=='pending' for o in chosen.values()) or not chosen else ('partial' if any(o['judging']['status']=='unavailable' for o in chosen.values()) else 'complete')),
      'pending_judging_dates':[d for d,o in chosen.items() if o['judging']['status']=='pending'],
      'unavailable_judging_dates':[d for d,o in chosen.items() if o['judging']['status']=='unavailable'],
      'metrics':aggregate(daily,start,end)}

def render(obj):
    out=[f"# Model Summary: {obj['family']}",'',f"Window: {obj['start']} through {obj['end']}. As of {obj['as_of']}. Judging: {obj['judging_status']}.",'',
       'Avg uses available readings only; SD is sample SD (n-1), unavailable below two readings. Elapsed Time is seconds. Cost is USD API-equivalent. Tokens include cache. ECPTS Avg pools costs/tokens on paired days and scales by 100,000,000. Missing days are not zeros. Historical backfill uses the preserved available evidence, not a claim of what was known then.','']
    for metric,(label,higher,has_sd) in METRICS.items():
        headers=['Model','Avg']+(['SD'] if has_sd else [])+[f'{int(d[5:7])}/{int(d[8:])}' for d in obj['dates']]
        out += [f'## {label}','','| '+' | '.join(headers)+' |','|---|'+'---:|'*(len(headers)-1)]
        def key(item):
            model,s=item;v=number(s['avg']);return (v is None,(-v if higher else v) if v is not None else 0,model)
        for model,s in sorted(obj['metrics'][metric].items(),key=key):
            cells=[model,display(metric,s['avg'])]+([display(metric,s['sd'])] if has_sd else [])+[display(metric,s['days'].get(d)) if s['days'].get(d) is not None else '' for d in obj['dates']]
            out.append('| '+' | '.join(cells)+' |')
        out.append('')
    return '\n'.join(out).rstrip()+'\n'

def generate(root,days,revision=None,enrich_date=None):
    daily=load_daily(root)
    if not daily:raise ValueError('No daily datasets')
    planned={}
    for day in sorted(days):
        for family in FAMILIES:
            name=basename(day,family);obj=make_rollup(daily,day,family)
            if not obj['observed_dates']:continue
            key=(family,name)
            planned[key]=obj
    if enrich_date:
        # Revisit only snapshots that actually include the enriched edition.
        for path in (root/'summary/json/rollups').glob('*/*.json'):
            old=read_json(path)
            if old['start']<=enrich_date<=old['end']:
                planned[(old['family'],path.stem)]=make_rollup(daily,old['as_of'],old['family'])
    payloads={}
    for (family,name),obj in planned.items():
        jp=root/f'summary/json/rollups/{family}/{name}.json';mp=root/f'summary/{family}/data/{name}.md'
        if jp.exists():
            old=read_json(jp)
            # Historical requests must never regress a more current open-period report.
            if old['as_of']>obj['as_of']:continue
            old_core={k:v for k,v in old.items() if k!='revisions'}
            if old_core==obj:obj=old
            else:
                changed_base=old['base_measurement_hash']!=obj['base_measurement_hash']
                advancing=old['as_of']<obj['as_of'] and family in ('weekly','monthly')
                completion=not changed_base and enrich_date is not None
                if not advancing and not completion and not revision:raise ValueError(f'Protected snapshot changed: {jp}; explicit revision required')
                obj['revisions']=old.get('revisions',[])+[{'reason':revision or ('source-completion' if completion else 'open-period extension'),'previous_sha256':sha(jp),'input_hash':digest(obj['inputs'])}]
        payloads[jp]=dumps(obj);payloads[mp]=render(obj)
    # All protection checks finish before any writes.
    for path,text in payloads.items():atomic_write(path,text)
    outputs=[str(p.relative_to(root)) for p in payloads]
    for family in FAMILIES:
        files=sorted((root/f'summary/json/rollups/{family}').glob('*.json'))
        if not files:continue
        latest=max(files,key=lambda p:read_json(p)['as_of']);obj=read_json(latest)
        intro=f'# {family}\n\n[Latest data](data/{latest.stem}.md) | [Summary home](../README.md)\n\n'
        text=intro+render(obj)+'\n## Archive\n\n'+'\n'.join(f'- [{p.stem}](data/{p.stem}.md)' for p in reversed(files))+'\n'
        path=root/f'summary/{family}/README.md';atomic_write(path,text);outputs.append(str(path.relative_to(root)))
    path=root/'summary/README.md';atomic_write(path,'# Model summaries\n\nDaily accepted measurements drive every view. No failed attempts or invented missing days.\n\n- [Daily measurements](daily/)\n'+'\n'.join(f'- [{f}]({f}/)' for f in FAMILIES)+'\n\n[Method](../docs/summary-procedure.md)\n');outputs.append(str(path.relative_to(root)))
    return sorted(set(outputs))

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--as-of','--date',dest='day');p.add_argument('--from',dest='start');p.add_argument('--to',dest='end');p.add_argument('--enrich-date');p.add_argument('--revision');p.add_argument('--manifest',type=Path,required=True)
    a=p.parse_args();days=[a.day] if a.day else dates(a.start,a.end)
    outputs=generate(a.repo,days,a.revision,a.enrich_date)
    atomic_write(a.manifest,dumps({'schema_version':1,'outputs':outputs}));print(f'{len(outputs)} rollup/navigation outputs')
if __name__=='__main__':main()
