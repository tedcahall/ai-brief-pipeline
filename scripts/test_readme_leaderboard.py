import json
from pathlib import Path
import tempfile
import unittest
from update_readme_leaderboard import render, update, Waiting

class LeaderboardTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name)
        self.days=[f'2026-11-{d:02d}' for d in range(7,12)]
        a={k:{} for k in ('scores','times','costs','tokens')}
        for i,d in enumerate(self.days):
            for k in a:a[k][d]={'a':10+i,'b':20+i}
            # A two-day newcomer must not displace eligible leaders.
            if i>=3:
                for k in a:a[k][d]['new']=100
            models=list(a['scores'][d])
            judges={j:{m:(2 if m=='a' else 4) for m in models} for j in ('j1','j2')}
            self.write(f'pulse-judging/json/{d}.json',{'date':d,'models':models,'judges':{'j1':'j1','j2':'j2'},'scores':judges})
            for directory,prefix in [('summary','Model-Summary'),('model-comparison','Model-Consensus'),('token-costs','Usage-and-Cost')]:
                p=self.root/directory/f'{prefix}-{d}.md';p.parent.mkdir(parents=True,exist_ok=True);p.write_text('report')
        self.write(f'summary/json/Model-Summary-{self.days[-1]}.audit.json',a)
    def write(self,path,value):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(value))
    def test_values_eligibility_and_ties(self):
        s=render(self.root)
        self.assertIn('| Selection Agreement | b | **22.0/100** | 17.0/100 | 12.0/100 | 22.0/100 | 5 |',s)
        self.assertIn('| Lowest Cost | a | **$12.0000**',s)
        self.assertIn('| Editorial Consistency | a; b | **SD 0.000**',s)
        self.assertNotIn('| new |',s)
    def test_missing_panel_retains_readme(self):
        (self.root/f'pulse-judging/json/{self.days[-1]}.json').unlink()
        with self.assertRaises(Waiting):render(self.root)
    def test_cohort_revision_blocks_stale_judging(self):
        p=self.root/f'pulse-judging/json/{self.days[-1]}.json'
        j=json.loads(p.read_text());del j['scores']['j1']['b'];p.write_text(json.dumps(j))
        with self.assertRaises(Waiting):render(self.root)
    def test_managed_block_idempotence(self):
        original='# Repo\n\nIntro\n\n## Explore the results\n\nKeep me\n'
        once=update(original,render(self.root))
        self.assertEqual(once,update(once,render(self.root)))
        self.assertTrue(once.endswith('## Explore the results\n\nKeep me\n'))
        self.assertTrue(once.startswith('# Repo\n\nIntro\n\n'))

if __name__=='__main__':unittest.main()
