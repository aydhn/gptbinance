import unittest
from app.program_plane.deliverables import DeliverableRegistry
from app.program_plane.models import DeliverableRecord
from app.program_plane.enums import DeliverableClass
class TestDeliverables(unittest.TestCase):
    def test_del(self):
        r = DeliverableRegistry()
        rec = DeliverableRecord(deliverable_id="d1", milestone_id="m1", deliverable_class=DeliverableClass.CODE, acceptance_criteria="ac")
        r.register(rec)
        self.assertEqual(len(r.list_by_milestone("m1")), 1)
