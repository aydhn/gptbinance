import unittest
from app.program_plane.acceptance import AcceptanceManager
from app.program_plane.models import AcceptanceRecord
class TestAcceptance(unittest.TestCase):
    def test_acc(self):
        a = AcceptanceManager()
        rec = AcceptanceRecord(acceptance_id="a1", deliverable_id="d1", state="accepted")
        a.record_acceptance(rec)
        self.assertTrue(a.is_accepted("d1"))
