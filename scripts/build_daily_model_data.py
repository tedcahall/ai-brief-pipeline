#!/usr/bin/env python3
"""Build admitted daily measurements or enrich existing measurements with a complete panel."""
import argparse
from pathlib import Path
from summary_metrics import *

HIST_NAMES=dict(zip(['DeepSeek Pro','Flash','GLM','Astra','Luna','Sol','Terra','Grok','Kimi','MiniMax','Opus','Qwen','Fable','Sonnet','Haiku','Argon'],['deepseek-v4-pro','deepseek-v4-1-flash-1017','glm-5-3','gpt-6-astra','gpt-6-luna','gpt-6-1-sol','gpt-6-1-terra','grok-4-7','kimi-k3-1-pro','minimax-m3-1-flash','opus-5-5','qwen-3-8-max-0902','fable-5-1','sonnet-5-5','haiku-5-5','gemini-4-argon']))
BASE_KEYS={'consensus_score':'scores','elapsed_seconds':'times','api_cost':'costs','total_tokens':'tokens'}

def source(root, path):return {'path':str(path.relative_to(root)), 'sha256':sha(path)}

def enrich(root, obj):
    if not obj['models']:
        obj['judging']={'status':'complete','reason':'no accepted models to judge'}
        return obj
    p=root/f"pulse-judging/json/{obj['date']}.json"
    historic_unavailable=obj.get('judging',{}).get('status')=='unavailable'
    obj['judging']={'status':'unavailable' if historic_unavailable else 'pending','reason':'historical panel unavailable' if historic_unavailable else 'judging not published'}
    for row in obj['models'].values():
        row['metrics']['pulse_judge_score']=None
        row['missing']['pulse_judge_score']='historical panel unavailable' if historic_unavailable else 'judging pending'
    if not p.exists():return obj
    panel=read_json(p); models=set(obj['models']); judges=set(panel.get('judges',{}))
    reason=None
    if panel.get('date')!=obj['date'] or set(panel.get('models',[]))!=models:reason='panel/cohort mismatch'
    elif not judges or judges!=set(panel.get('scores',{})):reason='incomplete panel'
    elif any(set(scores)!=models for scores in panel['scores'].values()):reason='incomplete panel coverage'
    if reason:
        obj['judging']={'status':'pending','reason':reason,'source':source(root,p)};return obj
    for scores in panel['scores'].values():
        if any(not 1<=number(v)<=5 for v in scores.values()):raise ValueError('Invalid judge score')
    for model,row in obj['models'].items():
        row['metrics']['pulse_judge_score']=numeric(sum(number(s[model]) for s in panel['scores'].values())/len(judges))
        row['missing'].pop('pulse_judge_score',None)
    obj['judging']={'status':'complete','source':source(root,p),'method':'unrounded arithmetic panel mean from scores'}
    return obj

def build(root, day, legacy_path=None):
    root=Path(root); date.fromisoformat(day)
    cp=root/f'model-comparison/json/Model-Consensus-{day}.audit.json'
    up=root/f'token-costs/json/Usage-and-Cost-{day}.audit.json'
    legacy=read_json(legacy_path) if legacy_path else None
    c=read_json(cp) if cp.exists() else None
    if not c and not legacy:raise ValueError(f'No accepted consensus audit for {day}')
    if c and c.get('date',c.get('edition'))!=day:raise ValueError('Consensus date mismatch')
    models={}
    conflicts=[]
    if c:
        for row in c['models']:
            model=row.get('slug') or HIST_NAMES.get(row['name'],row['name'])
            if not isinstance(model,str) or not re.fullmatch(r'[a-z0-9][a-z0-9-]*',model):raise ValueError('Invalid canonical model slug')
            if model in models:raise ValueError('Duplicate accepted model')
            if row.get('score') is None:continue
            if row.get('status','').startswith(('failed','incomplete')):continue
            models[model]=row
    elif legacy:
        models={HIST_NAMES.get(m,m):{'score':v} for m,v in legacy['scores'].get(day,{}).items() if v is not None}
    if not models and not c:raise ValueError(f'No accepted measurements for {day}')
    usages={}
    if up.exists():
        for u in read_json(up)['selected']:
            model=u.get('slug') or HIST_NAMES.get(u.get('display_name'),u.get('display_name'))
            if model in usages:raise ValueError('Duplicate selected usage')
            usages[model]=u
    obj={'schema_version':VERSION,'calculation_version':VERSION,'date':day,'status':'accepted' if models else 'finalized-no-successful-runs',
         'models':{},'sources':[], 'conflicts':conflicts}
    for p in (cp,up):
        if p.exists():obj['sources'].append(source(root,p))
    for model,row in sorted(models.items()):
        m={key:None for key in METRICS}; missing={}; provenance={}
        m['consensus_score']=numeric(row['score'])
        m['elapsed_seconds']=numeric(row.get('elapsed_seconds',row.get('elapsed')))
        u=usages.get(model)
        if u:
            if row.get('session') and u.get('session_id') and row['session']!=u['session_id']:raise ValueError(f'Attempt mismatch {day}/{model}')
            bounds=u.get('api_equivalent_range_usd')
            m['api_cost']=numeric(bounds['high'] if bounds else u.get('api_equivalent_usd'))
            counters=u.get('usage')
            if counters and all(counters.get(k) is not None for k in ('input_uncached','output','cache_read','cache_write')):
                m['total_tokens']=numeric(sum(number(counters[k]) for k in ('input_uncached','output','cache_read','cache_write')))
            provenance['cost_method']='historical selected API-equivalent estimate, upper bound when ranged'
        if legacy:
            for metric,key in BASE_KEYS.items():
                vals={HIST_NAMES.get(n,n):v for n,v in legacy.get(key,{}).get(day,{}).items()}
                val=numeric(vals.get(model))
                if m[metric] is not None and val is not None and number(m[metric])!=number(val):
                    conflicts.append({'date':day,'model':model,'metric':metric,'daily_audit':m[metric],'legacy':val})
                if m[metric] is None and val is not None:
                    m[metric]=val;provenance[metric]='published cumulative historical fallback'
        if m['api_cost'] is not None and number(m['total_tokens']) not in (None,0):m['ecpts']=numeric(number(m['api_cost'])/number(m['total_tokens'])*10**8)
        hp=root/f'daily-results/{day}/{model}/{day}.html'
        if hp.exists():
            expected=(c or {}).get('source_hashes',{}).get(f'{day}/{model}/{day}.html')
            if expected and expected!=sha(hp):
                missing['pulse_words']=missing['story_words']='HTML hash differs from accepted consensus source'
            else:
                try:
                    words=extract_words(hp.read_text())
                    m['pulse_words']=str(words['pulse_words']);m['story_words']=str(words['story_words'])
                    provenance['verbosity']=dict(words,source=source(root,hp),binding='consensus source hash' if expected else 'published edition path; no original HTML hash in historical audit')
                except ValueError as e:missing['pulse_words']=missing['story_words']=str(e)
        else:missing['pulse_words']=missing['story_words']='accepted archived HTML unavailable'
        for key,val in m.items():
            if val is None:missing.setdefault(key,'measurement unavailable in accepted source')
        obj['models'][model]={'metrics':m,'missing':missing,'provenance':provenance,
          'attempt':{k:str(row[k]) for k in ('run_id',) if row.get(k)}}
    if legacy_path and any('published cumulative historical fallback' in r['provenance'].values() for r in obj['models'].values()):
        obj['sources'].append(source(root,Path(legacy_path)))
    return validate_daily(enrich(root,obj))

def render(obj):
    names=['Model','Consensus Score','API Cost','Elapsed Time','Total Tokens','ECPTS','Pulse Words','Story Words','Pulse Judge Score']
    out=[f"# Model Data: {obj['date']}",'', 'USD API-equivalent estimates; elapsed seconds; tokens include cache. ECPTS = cost / tokens × 100,000,000. Successful accepted runs only.', '',f"Judging: {obj['judging']['status']}.",'','| '+' | '.join(names)+' |','|---|'+'---:|'*8]
    for model,row in obj['models'].items():out.append('| '+model+' | '+' | '.join(display(k,row['metrics'][k]) for k in METRICS)+' |')
    return '\n'.join(out)+'\n'

def write_daily(root,obj):
    paths=[root/f"summary/daily/json/Model-Data-{obj['date']}.json",root/f"summary/daily/Model-Data-{obj['date']}.md"]
    atomic_write(paths[0],dumps(obj));atomic_write(paths[1],render(obj))
    return [str(p.relative_to(root)) for p in paths]

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1]);p.add_argument('--date');p.add_argument('--from',dest='start');p.add_argument('--to',dest='end');p.add_argument('--enrich',action='store_true');p.add_argument('--manifest',type=Path,required=True)
    a=p.parse_args(); days=[a.date] if a.date else dates(a.start,a.end); outputs=[]
    # Compute and validate all requested inputs before writing any output.
    objects=[]
    for day in days:
        path=a.repo/f'summary/daily/json/Model-Data-{day}.json'
        obj=enrich(a.repo,read_json(path)) if a.enrich else build(a.repo,day)
        objects.append(validate_daily(obj))
    for obj in objects:outputs+=write_daily(a.repo,obj)
    atomic_write(a.manifest,dumps({'schema_version':1,'outputs':sorted(outputs),'dates':days,'mode':'enrich' if a.enrich else 'base','judging':{obj['date']:obj['judging']['status'] for obj in objects}}))
    print(f'{len(objects)} daily datasets; {len(outputs)} outputs')
if __name__=='__main__':main()
