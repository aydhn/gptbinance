import unittest
from app.program_plane.decision import DecisionQualityLinkage
class TestDec(unittest.TestCase):
    def test_dec(self):
        d = DecisionQualityLinkage()
        self.assertTrue(d.require_rationale("p1"))
