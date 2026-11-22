#!/usr/bin/env python3
"""Render the rolling-seven-day README leaderboard from committed rollups."""
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
 # Display-only rule: omit the 1017 build suffix; preserve the source model ID.
 'deepseek-v4-1-flash-1017':'DeepSeek V4.1 Flash',
 'deepseek-v4-pro':'DeepSeek V4 Pro', 'sonnet-5-5':'Sonnet 5.5',
 'gpt-6-1-terra':'GPT-6.1 Terra', 'gpt-6-luna':'GPT-6 Luna',
 'qwen-3-8-max-0902':'Qwen 3.8 Max 0902', 'fable-5-1':'Fable 5.1',
 'fable-5-2':'Fable 5.2', 'glm-5-3':'GLM-5.3',
 'minimax-m3-1-flash':'MiniMax M3.1 Flash', 'opus-5-5':'Opus 5.5',
 'grok-4-7':'Grok 4.7', 'gpt-6-astra':'GPT-6 Astra',
 'gemini-4-argon':'Gemini 4 Argon', 'gemini-4-carbon':'Gemini 4 Carbon',
 'gpt-6-1-sol':'GPT-6.1 Sol', 'kimi-k3-1-pro':'Kimi K3.1 Pro',
 'haiku-5-5':'Haiku 5.5',
 'gemini-4-hydrogen':'Gemini 4 Hydrogen', 'gemini-4-neon':'Gemini 4 Neon',
 'gpt-6-2-astra':'GPT-6.2 Astra', 'gpt-6-2-sol':'GPT-6.2 Sol', 'qwen-4-max':'Qwen4 Max',
}
class Waiting(Exception):
    pass

def render(root):
    from summary_metrics import read_json, number, METRICS
    from decimal import Decimal
    files=sorted((root/'summary/json/rollups/rolling-7-day').glob('Model-Summary-*.json'))
    if not files: raise Waiting('No rolling-seven-day dataset yet')
    current=read_json(files[-1])
    judging=current
    pending=current['judging_status']=='pending'
    if pending:
        complete=[read_json(p) for p in files if p<files[-1] and read_json(p)['judging_status']=='complete']
        judging=complete[-1] if complete else None
    metrics=[
      ('Ed Selection','consensus_score','avg',True),
      ('Selection SD','consensus_score','sd',False),
      ('Editorial Score','pulse_judge_score','avg',True),
      ('Ed Score SD','pulse_judge_score','sd',False),
      ('Lowest Cost','api_cost','avg',False),
      ('Run Time','elapsed_seconds','avg',False),
      ('Token Usage','total_tokens','avg',False),
      ('Pulse Words','pulse_words','avg',True),
      ('Pulse SD','pulse_words','sd',False),
      ('Story Words','story_words','avg',True),
      ('Story SD','story_words','sd',False),
    ]
    def fmt(metric,stat,value):
        if stat=='sd':return f'{value:.1f}'
        if metric=='api_cost':return f'${value:.2f}'
        if metric=='consensus_score':return f'{value:.1f}/100'
        if metric=='pulse_judge_score':return f'{value:.2f}/5'
        if metric=='elapsed_seconds':return f'{round(value)//60}m {round(value)%60:02d}s'
        return f'{value:,.0f}'
    out=f"# Model Performance Leaders\n\n**Seven-calendar-day statistics | {current['start']} through {current['end']} | Minimum 4 observed days per metric**\n\n"
    if pending:
        out+=f"Judging update pending. Judging rows retain {judging['as_of'] if judging else 'no prior completed snapshot (unavailable)'}. Other rows are current.\n\n"
    else:out+=f"Judging as of {judging['as_of']}; status: {judging['judging_status']}.\n\n"
    for leader in (True,False):
        out+='## '+('🏆 Leaders' if leader else '⚠️ Laggards')+'\n\n'
        out+='| Category | Model | Mv Avg | All Avg | All Low | All High | Runs |\n|---|---|---:|---:|---:|---:|---:|\n'
        for label,metric,stat,higher in metrics:
            obj=judging if metric=='pulse_judge_score' else current
            values={m:(number(v[stat]),v['n']) for m,v in (obj['metrics'][metric] if obj else {}).items() if v['n']>=4 and v[stat] is not None}
            if not leader and label=='Lowest Cost':label='Highest Cost'
            if not values:
                out+=f'| {label} | unavailable | unavailable | unavailable | unavailable | unavailable | 0 |\n';continue
            vals=[v[0] for v in values.values()];extreme=(max if higher==leader else min)(vals)
            winners=sorted(m for m,(v,n) in values.items() if v==extreme)
            names='; '.join(NAMES.get(m,m).replace(' ','\u00a0') for m in winners)
            counts={values[m][1] for m in winners}
            runs=str(next(iter(counts))) if len(counts)==1 else '; '.join(f'{NAMES.get(m,m)}: {values[m][1]}' for m in winners)
            f=lambda v:fmt(metric,stat,v)
            out+=f'| {label} | {names} | **{f(extreme)}** | {f(sum(vals)/len(vals))} | {f(min(vals))} | {f(max(vals))} | {runs} |\n'
        out+='\n'
    out+='Mv Avg is the window mean for ordinary rows and sample SD for SD rows. All columns use only eligible models. Word counts rank length, not quality.\n'
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
