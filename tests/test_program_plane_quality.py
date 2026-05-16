import unittest
from app.program_plane.quality import ProgramQualityChecker
class TestQual(unittest.TestCase):
    def test_qual(self):
        c = ProgramQualityChecker()
        self.assertEqual(c.check("p1"), "high_quality")
