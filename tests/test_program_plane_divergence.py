import unittest
from app.program_plane.divergence import ProgramDivergenceAnalyzer
class TestDiv(unittest.TestCase):
    def test_div(self):
        a = ProgramDivergenceAnalyzer()
        r = a.analyze("p1")
        self.assertEqual(r.blast_radius, "none")
