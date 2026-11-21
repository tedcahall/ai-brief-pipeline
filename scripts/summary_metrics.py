"""Shared, deterministic measurements. Decimal strings are the JSON numeric contract."""
import calendar
from datetime import date, timedelta
from decimal import Decimal, localcontext
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import tempfile

VERSION = 1
METRICS = {
 'consensus_score': ('Selection Score', True, True),
 'api_cost': ('API Cost', False, False),
 'elapsed_seconds': ('Elapsed Time', False, True),
 'total_tokens': ('Total Tokens', False, False),
 'ecpts': ('ECPTS', False, False),
 'pulse_words': ('Pulse Words', True, True),
 'story_words': ('Story Words', True, True),
 'pulse_judge_score': ('Pulse Judge Score', True, True),
}

def number(value):
    if value is None: return None
    if isinstance(value, bool): raise ValueError('Boolean is not a measurement')
    result = Decimal(str(value))
    if not result.is_finite() or result < 0: raise ValueError(f'Invalid measurement {value!r}')
    return result

def numeric(value):
    return None if value is None else str(number(value))

def sha(path): return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def dumps(obj): return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + '\n'
def read_json(path): return json.loads(Path(path).read_text(), parse_float=Decimal)
def digest(obj): return hashlib.sha256(dumps(obj).encode()).hexdigest()

def atomic_write(path, content):
    path = Path(path)
    if path.exists() and path.read_text() == content: return False
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix='.'+path.name+'.')
    try:
        with os.fdopen(fd, 'w') as f:
            f.write(content); f.flush(); os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)
    return True

def dates(start, end):
    start, end = date.fromisoformat(str(start)), date.fromisoformat(str(end))
    if end < start: raise ValueError('Reversed range')
    return [(start+timedelta(days=i)).isoformat() for i in range((end-start).days+1)]

def window(day, family):
    d = date.fromisoformat(day)
    if family == 'rolling-7-day': start = d-timedelta(days=6)
    elif family == 'rolling-30-day': start = d-timedelta(days=29)
    elif family == 'weekly': start = d-timedelta(days=(d.weekday()+1)%7)
    elif family == 'monthly': start = d.replace(day=1)
    else: raise ValueError(family)
    return start.isoformat(), d.isoformat()

def stats(values, sd=True):
    values = [number(v) for v in values if v is not None]
    n = len(values)
    mean = sum(values)/n if n else None
    # Same sample-SD convention as the previously published editorial calculation.
    deviation = (sum((v-mean)**2 for v in values)/(n-1)).sqrt() if sd and n>1 else None
    return {'n':n, 'avg':numeric(mean), 'sd':numeric(deviation),
            'low':numeric(min(values)) if n else None, 'high':numeric(max(values)) if n else None}

def validate_daily(obj):
    if obj['schema_version'] != VERSION: raise ValueError('Unsupported daily schema')
    date.fromisoformat(obj['date'])
    if not isinstance(obj['models'], dict): raise ValueError('models must be keyed by canonical slug')
    for model, row in obj['models'].items():
        if not re.fullmatch(r'[a-z0-9][a-z0-9-]*', model): raise ValueError('Invalid canonical slug')
        for metric in METRICS: number(row['metrics'][metric])
        for key in ('total_tokens','pulse_words','story_words'):
            value=number(row['metrics'][key])
            if value is not None and value!=value.to_integral_value():raise ValueError('Count must be integral')
        score = number(row['metrics']['consensus_score'])
        if score is None or score>100: raise ValueError('Accepted row requires a consensus score /100')
        judge = number(row['metrics']['pulse_judge_score'])
        if judge is not None and not 1<=judge<=5: raise ValueError('Invalid panel mean')
    return obj

def aggregate(daily, start, end):
    selected = {d:validate_daily(v) for d,v in daily.items() if start<=d<=end}
    result = {}
    models = sorted({m for obj in selected.values() for m in obj['models']})
    for metric, (_, _, has_sd) in METRICS.items():
        result[metric] = {}
        for model in models:
            series = {d:obj['models'][model]['metrics'][metric] for d,obj in sorted(selected.items()) if model in obj['models']}
            summary = stats(series.values(), has_sd)
            if metric == 'ecpts':
                pairs = [(number(o['models'][model]['metrics']['api_cost']),number(o['models'][model]['metrics']['total_tokens'])) for o in selected.values() if model in o['models']]
                pairs = [(c,t) for c,t in pairs if c is not None and t is not None and t>0]
                summary['avg'] = numeric(sum(c for c,t in pairs)/sum(t for c,t in pairs)*10**8) if pairs else None
                summary['n'] = len(pairs)
            result[metric][model] = dict(summary, days=series)
    return result

class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag=tag; self.attrs=dict(attrs); self.parent=parent; self.children=[]
    def all(self, tag=None):
        for c in self.children:
            if isinstance(c,Node):
                if tag is None or c.tag==tag: yield c
                yield from c.all(tag)
    def hidden(self):
        style=re.sub(r'\s','',self.attrs.get('style','').lower())
        return self.tag in ('script','style','template','head') or 'hidden' in self.attrs or 'display:none' in style or 'visibility:hidden' in style
    def text(self):
        if self.hidden(): return ''
        return ''.join(c.text() if isinstance(c,Node) else c for c in self.children)

class Tree(HTMLParser):
    VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self, html):
        super().__init__(convert_charrefs=True); self.root=Node(); self.node=self.root; self.feed(html)
    def handle_starttag(self, tag, attrs):
        node=Node(tag,attrs,self.node); self.node.children.append(node)
        if tag in ('br','hr'): node.children.append(' ')
        if tag not in self.VOID:self.node=node
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag,attrs)
        if tag not in self.VOID:self.handle_endtag(tag)
    def handle_endtag(self, tag):
        node=self.node
        while node.parent is not None:
            if node.tag==tag:self.node=node.parent;return
            node=node.parent
    def handle_data(self, data):self.node.children.append(data)

def word_count(text): return sum(any(c.isalnum() for c in word) for word in text.split())

def extract_words(html):
    tree=Tree(html).root
    sections={}
    for name in ('pulse','stories'):
        found=[n for n in tree.all() if n.attrs.get('id')==name]
        if len(found)!=1: raise ValueError(f'Expected one #{name} section')
        sections[name]=found[0]
    def visible(n):
        while n is not None:
            if n.hidden():return False
            n=n.parent
        return True
    pulse=[n.text() for n in sections['pulse'].all('p') if visible(n)]
    # Known archived template: five alternating title and body paragraphs.
    ps=[n for n in sections['stories'].all('p') if visible(n)]
    if len(ps)!=10: raise ValueError(f'Expected ten story title/body paragraphs, got {len(ps)}')
    stories=[]
    for title, body in zip(ps[::2], ps[1::2]):
        if not list(title.all('strong')) or not list(title.all('a')): raise ValueError('Unrecognized story title structure')
        if not body.text().strip(): raise ValueError('Empty story summary')
        stories.append(body.text())
    if not pulse or not all(p.strip() for p in pulse):raise ValueError('Empty Pulse paragraphs')
    return {'pulse_words':word_count(' '.join(pulse)), 'story_words':sum(map(word_count,stories)),
            'per_story_words':list(map(word_count,stories)), 'adapter':'archived-id-paragraphs-v1'}

def display(metric, value):
    if value is None:return 'unavailable'
    v=number(value)
    if metric=='api_cost':return f'${v:.4f}'
    if metric=='elapsed_seconds':return f'{v:.1f}'
    if metric in ('total_tokens','pulse_words','story_words'):return f'{v:,.1f}' if v%1 else f'{v:,.0f}'
    return f'{v:.3f}'
