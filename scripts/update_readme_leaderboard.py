#!/usr/bin/env python3
"""Render the approved five-batch README leaderboard from published audits."""
import argparse
from datetime import date
import json
import math
from pathlib import Path
import re
import statistics as st

START = '<!-- MODEL-LEADERBOARD:START -->'
END = '<!-- MODEL-LEADERBOARD:END -->'
NAMES = {
 'deepseek-v4-1-flash-1017':'DeepSeek V4.1 Flash 1017',
 'deepseek-v4-pro':'DeepSeek V4 Pro', 'sonnet-5-5':'Sonnet 5.5',
 'gpt-6-1-terra':'GPT-6.1 Terra', 'gpt-6-luna':'GPT-6 Luna',
 'qwen-3-8-max-0902':'Qwen 3.8 Max 0902', 'fable-5-1':'Fable 5.1',
 'fable-5-2':'Fable 5.2', 'glm-5-3':'GLM-5.3',
 'minimax-m3-1-flash':'MiniMax M3.1 Flash', 'opus-5-5':'Opus 5.5',
 'grok-4-7':'Grok 4.7', 'gpt-6-astra':'GPT-6 Astra',
 'gemini-4-argon':'Gemini 4 Argon', 'gemini-4-carbon':'Gemini 4 Carbon',
 'gpt-6-1-sol':'GPT-6.1 Sol', 'kimi-k3-1-pro':'Kimi K3.1 Pro',
 'haiku-5-5':'Haiku 5.5',
}
class Waiting(Exception):
    pass

def number(v):
    n=float(v)
    if not math.isfinite(n) or n < 0:
        raise ValueError(f'Invalid measurement: {v!r}')
    return n

def aggregate(data, days):
    series={}
    for d in days:
        for m,v in data.get(d,{}).items():
            if v is not None:
                series.setdefault(m,[]).append(number(v))
    return {m:(st.mean(v),len(v)) for m,v in series.items() if len(v)>=3}

def render(root):
    files=sorted((root/'summary/json').glob('Model-Summary-????-??-??.audit.json'))
    if not files:
        raise Waiting('No summary audit yet')
    source=files[-1]
    batch=source.name.removeprefix('Model-Summary-').removesuffix('.audit.json')
    date.fromisoformat(batch)
    a=json.loads(source.read_text())
    days=sorted(d for d in a['scores'] if d<=batch)[-5:]
    if len(days)!=5 or days[-1]!=batch:
        raise Waiting('Five batches including the latest summary are required')
    pulse={}
    for d in days:
        for group,template in [('model-comparison','Model-Consensus'),('token-costs','Usage-and-Cost'),('summary','Model-Summary')]:
            if not (root/group/f'{template}-{d}.md').is_file():
                raise Waiting(f'Missing {group} report for {d}')
        for key in ('scores','times','costs','tokens'):
            if d not in a[key]:
                raise Waiting(f'Missing {key} batch {d}')
        path=root/f'pulse-judging/json/{d}.json'
        if not path.is_file():
            raise Waiting(f'Pulse judging not yet published for {d}')
        j=json.loads(path.read_text())
        models=set(j['models'])
        expected={m for m,v in a['scores'][d].items() if v is not None}
        if j['date']!=d or models!=expected:
            raise Waiting(f'Pulse/summary cohort mismatch for {d}')
        if not j['judges'] or set(j['judges'])!=set(j['scores']):
            raise Waiting(f'Incomplete judge panel for {d}')
        for scores in j['scores'].values():
            if set(scores)!=models:
                raise Waiting(f'Incomplete judge coverage for {d}')
            if any(not 1<=number(v)<=5 for v in scores.values()):
                raise ValueError(f'Invalid Pulse score for {d}')
        pulse[d]={m:st.mean(number(s[m]) for s in j['scores'].values()) for m in models}
    pv={}
    for scores in pulse.values():
        for m,v in scores.items():
            pv.setdefault(m,[]).append(v)
    sd={m:(st.stdev(v),len(v)) for m,v in pv.items() if len(v)>=3}
    duration=lambda v:f'{round(v)//60}m {round(v)%60:02d}s'
    metrics=[
      ('Ed Selection',aggregate(a['scores'],days),True,lambda v:f'{v:.1f}/100'),
      ('Editorial Score',aggregate(pulse,days),True,lambda v:f'{v:.2f}/5'),
      ('Lowest Cost',aggregate(a['costs'],days),False,lambda v:f'${v:.4f}'),
      ('Completion Time',aggregate(a['times'],days),False,duration),
      ('Ed Consistency',sd,False,lambda v:f'SD {v:.3f}'),
      ('Token Usage',aggregate(a['tokens'],days),False,lambda v:f'{v:,.0f}'),
    ]
    first,last=map(date.fromisoformat,(days[0],days[-1]))
    if (first.year,first.month)==(last.year,last.month):
        window=f'{first:%B} {first.day}-{last.day}, {last.year}'
    else:
        window=f'{first:%B} {first.day}, {first.year} - {last:%B} {last.day}, {last.year}'
    out=f'# Model Performance Leaders\n\n**Five-batch moving averages | {window} | Minimum 3 observed runs**\n\n'
    for leader in (True,False):
        out+='## '+('🏆 Leaders' if leader else '⚠️ Laggards')+'\n\n'
        out+='| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |\n|---|---|---:|---:|---:|---:|---:|\n'
        for label,values,higher,fmt in metrics:
            if not values:
                raise Waiting(f'No eligible models for {label}')
            vals=[v[0] for v in values.values()]
            extreme=(max if higher==leader else min)(vals)
            winners=sorted(m for m,(v,n) in values.items() if v==extreme)
            names='; '.join(NAMES.get(m,m).replace(' ','\u00a0') for m in winners)
            counts={values[m][1] for m in winners}
            runs=str(next(iter(counts))) if len(counts)==1 else '; '.join(f'{NAMES.get(m,m)}: {values[m][1]}' for m in winners)
            if not leader and label=='Lowest Cost': label='Highest Cost'
            out+=f'| {label} | {names} | **{fmt(extreme)}** | {fmt(st.mean(vals))} | {fmt(min(vals))} | {fmt(max(vals))} | {runs} |\n'
        out+='\n'
    return out

def update(readme, sample):
    # Nest section headings under the repository's existing title.
    block=sample.replace('# Model Performance Leaders','## Model Performance Leaders',1)
    block=block.replace('## 🏆 Leaders','### 🏆 Leaders').replace('## ⚠️ Laggards','### ⚠️ Laggards')
    managed=START+'\n'+block.rstrip()+'\n'+END+'\n\n'
    if START in readme or END in readme:
        if readme.count(START)!=1 or readme.count(END)!=1:
            raise ValueError('Malformed README leaderboard markers')
        start=readme.index(START);end=readme.index(END)+len(END)
        if end<start: raise ValueError('Reversed README markers')
        return readme[:start]+managed+readme[end:].lstrip('\n')
    anchor=re.search(r'^## Explore the results\s*$',readme,re.M|re.I)
    if not anchor: raise ValueError('Explore the results heading missing')
    return readme[:anchor.start()]+managed+readme[anchor.start():]

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--if-ready',action='store_true',help='Leave README unchanged when inputs are pending')
    parser.add_argument('--output',type=Path,help='Write standalone Markdown instead of updating README')
    args=parser.parse_args()
    try: sample=render(args.repo)
    except Waiting as e:
        print(f'WAITING: {e}; prior README snapshot retained')
        return 0 if args.if_ready else 2
    if args.output:
        args.output.write_text(sample);return 0
    p=args.repo/'README.md';old=p.read_text();new=update(old,sample)
    if old!=new: p.write_text(new)
    print('README updated' if old!=new else 'README unchanged')
    return 0
if __name__=='__main__':
    raise SystemExit(main())
