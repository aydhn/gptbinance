import unittest
from app.program_plane.handoffs import HandoffGovernance
from app.program_plane.models import HandoffRecord
from app.program_plane.enums import HandoffClass
class TestHandoff(unittest.TestCase):
    def test_handoff(self):
        h = HandoffGovernance()
        rec = HandoffRecord(handoff_id="h1", source_program_id="p1", target_program_id="p2", handoff_class=HandoffClass.REQUESTED)
        h.register(rec)
        h.accept_handoff("h1")
        self.assertEqual(h._handoffs["h1"].state, "accepted")
