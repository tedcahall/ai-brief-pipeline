#!/usr/bin/env python3
"""Generate static archive indexes from actual HTML files; never change reports."""
import argparse, html, json, re, subprocess
from pathlib import Path
from bs4 import BeautifulSoup
BASE=Path(__file__).resolve().parent

def build(root):
 days={}
 for f in sorted(root.glob('*/*/*.html')):
  day,model,name=f.relative_to(root).parts
  if not re.fullmatch(r'\d{4}-\d{2}-\d{2}',day):continue
  days.setdefault(day,[]).append((model,f'{model}/{name}'))
 ordered=sorted(days,reverse=True)
 def label(day,fmt):return subprocess.check_output(['date','-d',day,'+'+fmt],text=True).strip()
 for i,day in enumerate(ordered):
  rows=days[day];s=BeautifulSoup((BASE/'reference/dennis-original.html').read_text(),'html.parser')
  s.title.string=f"Max’s AI Brief · {day} · Compare models"
  s.h1.string=label(day,'%B %-d, %Y')
  s.select_one('header p').string=f'{len(rows)} archived reports. Choose two models and explore their work side by side.'
  s.select_one('.eyebrow').string="MAX’S AI BRIEF / MODEL COMPARISON"
  for sel in s.select('select'):
   sel.clear()
   for model,path in rows:
    o=s.new_tag('option',value=path);o.string=model;sel.append(o)
  ul=s.select_one('.archive');ul.clear()
  for model,path in rows:
   li=s.new_tag('li');a=s.new_tag('a',href=path);a.string=model;li.append(a);ul.append(li)
  s.select_one('#archive h2').string=f'All {len(rows)} reports'
  s.select_one('nav a').string='← All dates'
  for j,title in [(i+1,'Older day →'),(i-1,'← Newer day')]:
   if 0<=j<len(ordered):
    a=s.new_tag('a',href=f'../{ordered[j]}/');a.string=title;a['data-day']=f'../{ordered[j]}/';a['style']='margin-left:24px';s.nav.append(a)
  style=s.new_tag('link',rel='stylesheet',href='../assets/archive.css');s.head.append(style)
  s.body['class']='daily'
  toggle=s.new_tag('button',id='mobile-compare',type='button')
  toggle['aria-expanded']='false';toggle['aria-controls']='compare';toggle.string='Compare models (optional)'
  s.select_one('#compare').insert_before(toggle)
  mobile=s.new_tag('script');mobile.string="""document.getElementById('mobile-compare').addEventListener('click',function(){const open=document.body.classList.toggle('mobile-comparing');this.setAttribute('aria-expanded',String(open));this.textContent=open?'Hide comparison':'Compare models (optional)';});"""
  s.body.append(mobile)
  # Preserve Dennis’s behavior, replacing only default preferences and frame labels.
  script=s.find('script');script.string=(BASE/'reference/viewer.js').read_text()
  (root/day/'index.html').write_text(str(s))
 months={}
 for day in ordered:months.setdefault(day[:7],[]).append(day)
 sections=''
 for month,ds in months.items():
  cards=''.join(f'<a class="date-card" href="{d}/"><span class="weekday">{label(d,"%a")}</span><strong>{label(d,"%-d")}</strong><span>{label(d,"%b %Y")}</span><small>{len(days[d])} reports <b>↗</b></small></a>' for d in ds)
  sections+=f'<section class="month"><div class="section-title"><h2>{label(ds[0],"%B %Y")}</h2><span>{len(ds)} days</span></div><div class="dates">{cards}</div></section>'
 latest=ordered[0] if ordered else None
 cta=f'<a class="cta" href="{latest}/">Compare the latest models <span>↗</span></a>' if latest else ''
 page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Max’s AI Brief · Model Archive</title><link rel="stylesheet" href="assets/archive.css"></head><body><a class="skip" href="#dates">Skip to archive</a><main class="home"><nav class="brand"><a href="https://maxsaibrief.com">MAX’S AI BRIEF<span>THE MORNING SIGNAL</span></a><a class="website" href="https://maxsaibrief.com">Read the daily brief ↗</a></nav><header class="hero"><div class="hero-copy"><div class="eyebrow">THE MODEL ARCHIVE</div><h1>One day.<br>Many perspectives.</h1><p>Explore the AI Brief across models.<br>Pick a day. Choose two models. See how they compare.</p>{cta}</div><img src="assets/max-first-light.jpg" alt="Max’s AI Brief — The Morning Signal. Orange sunrise over blue mountains with circuit details."></header><div class="summary"><span><b>{len(days)}</b> archived days</span><span><b>{sum(map(len,days.values()))}</b> model reports</span><span class="summary-note">Newest first · Original reports preserved</span></div><div id="dates">{sections}</div><footer><strong>Max’s AI Brief</strong><span>A daily AI dispatch. A growing record of how models tell the story.</span><a href="https://github.com/tedcahall/ai-brief-pipeline">Explore the pipeline ↗</a></footer></main></body></html>'''
 (root/'index.html').write_text(page)
 (root/'manifest.json').write_text(json.dumps(days,indent=2))
 print(f'Generated {len(days)} daily indexes, {sum(map(len,days.values()))} report links, and archive index.')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('root',type=Path,nargs='?',default=BASE.parents[1]/'daily-results');build(p.parse_args().root)
