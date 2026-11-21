import unittest
from decimal import Decimal
from summary_metrics import *

def daily(day, values, judging='complete'):
    return {'schema_version':1,'calculation_version':1,'date':day,'judging':{'status':judging},'models':{m:{'metrics':dict.fromkeys(METRICS,None)|{'consensus_score':'50'}|v} for m,v in values.items()}}

class MetricsTests(unittest.TestCase):
    def test_sample_sd(self):
        s=stats(['2','4','4','4','5','5','7','9']);self.assertEqual(s['n'],8)
        self.assertEqual(number(s['avg']),5);self.assertEqual(number(s['sd']), (Decimal(32)/7).sqrt())
        self.assertIsNone(stats(['4'])['sd']);self.assertEqual(number(stats(['4','4'])['sd']),0)
    def test_calendar_boundaries(self):
        self.assertEqual(window('2026-11-22','weekly'),('2026-11-22','2026-11-22'))
        self.assertEqual(window('2026-11-21','weekly'),('2026-11-15','2026-11-21'))
        self.assertEqual(window('2024-03-01','rolling-7-day')[0],'2024-02-24')
        self.assertEqual(window('2027-01-01','monthly')[0],'2027-01-01')
    def test_missing_days_and_pooled_ecpts(self):
        ds={'2026-11-01':daily('2026-11-01',{'a':{'api_cost':'1','total_tokens':'10','ecpts':'10000000'}}),
            '2026-11-07':daily('2026-11-07',{'a':{'api_cost':'9','total_tokens':'90','ecpts':'10000000'}}),
            '2026-10-31':daily('2026-10-31',{'a':{'api_cost':'999','total_tokens':'1','ecpts':'99900000000'}})}
        result=aggregate(ds,'2026-11-01','2026-11-07');self.assertEqual(result['ecpts']['a']['n'],2)
        self.assertEqual(number(result['ecpts']['a']['avg']),10000000)
        for key in ('api_cost','total_tokens','ecpts'):self.assertIsNone(result[key]['a']['sd'])
    def test_invalid_numbers(self):
        for v in ('NaN','Infinity','-1',True):
            with self.assertRaises(ValueError):number(v)
    def test_reader_visible_extraction(self):
        html='<div id="pulse"><h2>Not counted</h2><p>A&amp;B <a href="https://not-counted">visible words</a> — 🦾 <span hidden>invisible</span>你好</p></div><div id="stories">'
        html+=''.join('<p><strong><a href="x">Title excluded</a></strong></p><p>Two words</p>' for _ in range(5))+'</div>'
        result=extract_words(html);self.assertEqual(result['pulse_words'],4);self.assertEqual(result['story_words'],10)
        with self.assertRaises(ValueError):extract_words(html.replace('id="stories"','id="other"'))
    def test_missing_story_rejected(self):
        with self.assertRaises(ValueError):extract_words('<div id="pulse"><p>Text</p></div><div id="stories"><p>One only</p></div>')
if __name__=='__main__':unittest.main()
