import unittest
from app.program_plane.variance import ProgramVarianceAnalyzer
class TestVar(unittest.TestCase):
    def test_var(self):
        v = ProgramVarianceAnalyzer()
        r = v.analyze("p1")
        self.assertEqual(r.plan_vs_actual_days, 2)
