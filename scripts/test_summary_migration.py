import unittest
import tempfile
from pathlib import Path
from summary_metrics import *
from build_daily_model_data import enrich, build
from test_summary_metrics import daily

class IngestionTests(unittest.TestCase):
    def test_unrounded_panel_and_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);p=root/'pulse-judging/json/2026-11-21.json'
            panel={'date':'2026-11-21','models':['a'],'judges':{'x':'x','y':'y','z':'z'},'scores':{'x':{'a':1},'y':{'a':2},'z':{'a':2}},'average':{'a':1.67}}
            atomic_write(p,dumps(panel));obj=daily('2026-11-21',{'a':{}});obj['models']['a']['missing']={}
            obj=enrich(root,obj);self.assertEqual(number(obj['models']['a']['metrics']['pulse_judge_score']),Decimal(5)/3)
            panel['models'].append('b');atomic_write(p,dumps(panel));obj=enrich(root,obj)
            self.assertIsNone(obj['models']['a']['metrics']['pulse_judge_score']);self.assertEqual(obj['judging']['status'],'pending')
    def test_failed_attempt_excluded_and_session_binding(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);cp=root/'model-comparison/json/Model-Consensus-2026-11-21.audit.json';up=root/'token-costs/json/Usage-and-Cost-2026-11-21.audit.json'
            atomic_write(cp,dumps({'date':'2026-11-21','models':[{'name':'a','score':80,'session':'one'},{'name':'bad','score':0,'status':'failed'}]}))
            obj=build(root,'2026-11-21');self.assertEqual(set(obj['models']),{'a'})
            atomic_write(up,dumps({'selected':[{'slug':'a','session_id':'two','usage':{},'api_equivalent_usd':1}]}))
            with self.assertRaises(ValueError):build(root,'2026-11-21')
    def test_finalized_all_failed_has_no_observations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);cp=root/'model-comparison/json/Model-Consensus-2026-11-21.audit.json'
            atomic_write(cp,dumps({'date':'2026-11-21','models':[],'excluded_models':['bad']}))
            obj=build(root,'2026-11-21');self.assertEqual(obj['models'],{});self.assertEqual(obj['judging']['status'],'complete')
    def test_atomic_write_failure_preserves_original(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'data.json';p.write_text('original')
            with patch('summary_metrics.os.replace',side_effect=OSError('interrupted')):
                with self.assertRaises(OSError):atomic_write(p,'replacement')
            self.assertEqual(p.read_text(),'original');self.assertEqual(len(list(p.parent.iterdir())),1)
if __name__=='__main__':unittest.main()
