import tempfile
import unittest
from pathlib import Path
from summary_metrics import *
from build_summary_rollups import generate
from update_readme_leaderboard import render, update, START, END
from test_summary_metrics import daily

class ReadmeTests(unittest.TestCase):
    def test_independent_eligibility_and_pending_judging(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for day in dates('2026-11-18','2026-11-21'):
                obj=daily(day,{'a':{'consensus_score':'80','pulse_words':'100' if day!='2026-11-18' else None}},'pending')
                atomic_write(root/f'summary/daily/json/Model-Data-{day}.json',dumps(obj))
            generate(root,['2026-11-21']);text=render(root)
            self.assertIn('| Ed Selection | a | **80.0/100**',text)
            self.assertIn('| Pulse Words | unavailable |',text)
            self.assertIn('Judging update pending',text)
    def test_exact_ties_and_markers(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            for day in dates('2026-11-18','2026-11-21'):
                obj=daily(day,{'a':{},'b':{}})
                atomic_write(root/f'summary/daily/json/Model-Data-{day}.json',dumps(obj))
            generate(root,['2026-11-21']);text=render(root);self.assertIn('| Ed Selection | a; b |',text)
            base='# Repo\n\n## Explore the results\n\nunchanged\n';result=update(base,text)
            self.assertEqual(update(result,text),result);self.assertTrue(result.endswith('unchanged\n'))
    def test_malformed_markers(self):
        with self.assertRaises(ValueError):update(START,'test')
if __name__=='__main__':unittest.main()
