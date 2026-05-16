import unittest
from app.program_plane.milestones import MilestoneRegistry
from app.program_plane.models import MilestoneRecord
from app.program_plane.enums import MilestoneClass
class TestMilestones(unittest.TestCase):
    def test_milestone(self):
        r = MilestoneRegistry()
        rec = MilestoneRecord(milestone_id="m1", program_id="p1", milestone_class=MilestoneClass.DESIGN, completion_criteria="c1")
        r.register(rec)
        self.assertEqual(len(r.list_by_program("p1")), 1)
