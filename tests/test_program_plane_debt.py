import unittest
from app.program_plane.debt import ProgramDebtTracker
class TestDebt(unittest.TestCase):
    def test_debt(self):
        t = ProgramDebtTracker()
        r = t.evaluate("p1")
        self.assertFalse(r.stale_blocker_debt)
