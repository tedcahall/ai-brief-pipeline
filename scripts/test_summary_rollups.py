import tempfile
import unittest
from pathlib import Path
from summary_metrics import *
from build_summary_rollups import generate, make_rollup
from test_summary_metrics import daily

class RollupTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def save(self,day,score='50',judge=None):
        obj=daily(day,{'a':{'consensus_score':score,'pulse_judge_score':judge}},'complete' if judge else 'pending')
        atomic_write(self.root/f'summary/daily/json/Model-Data-{day}.json',dumps(obj))
    def test_idempotence_and_immutable_history(self):
        self.save('2026-11-21');generate(self.root,['2026-11-21'])
        first={str(p):sha(p) for p in self.root.rglob('*') if p.is_file()}
        generate(self.root,['2026-11-21']);self.assertEqual(first,{str(p):sha(p) for p in self.root.rglob('*') if p.is_file()})
        self.save('2026-11-21','60')
        with self.assertRaises(ValueError):generate(self.root,['2026-11-21'])
    def test_late_judging_enrichment_only(self):
        self.save('2026-11-20');self.save('2026-11-21');generate(self.root,['2026-11-20','2026-11-21'])
        self.save('2026-11-20',judge='3.5');generate(self.root,[],enrich_date='2026-11-20')
        obj=read_json(self.root/'summary/json/rollups/rolling-7-day/Model-Summary-2026-11-21.json')
        self.assertEqual(obj['metrics']['pulse_judge_score']['a']['avg'],'3.5');self.assertEqual(obj['revisions'][-1]['reason'],'source-completion')
    def test_newest_first_full_window(self):
        obj=make_rollup({'2026-11-21':daily('2026-11-21',{'a':{}})},'2026-11-21','rolling-30-day')
        self.assertEqual(len(obj['dates']),30);self.assertEqual(obj['dates'][0],'2026-11-21')
if __name__=='__main__':unittest.main()
