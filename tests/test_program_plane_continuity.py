import unittest
from app.program_plane.continuity import ContinuityLinkage
class TestCont(unittest.TestCase):
    def test_cont(self):
        c = ContinuityLinkage()
        self.assertTrue(c.check_dr_readiness("p1"))
