import unittest
from app.program_plane.reliability import ReliabilityLinkage
class TestRel(unittest.TestCase):
    def test_rel(self):
        r = ReliabilityLinkage()
        self.assertTrue(r.check_protective_work("p1"))
