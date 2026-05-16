import unittest
from app.program_plane.equivalence import ProgramEquivalenceAnalyzer
from app.program_plane.enums import EquivalenceVerdict
class TestEq(unittest.TestCase):
    def test_eq(self):
        a = ProgramEquivalenceAnalyzer()
        r = a.analyze("p1")
        self.assertEqual(r.verdict, EquivalenceVerdict.EQUIVALENT)
