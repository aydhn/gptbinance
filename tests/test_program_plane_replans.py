import unittest
from app.program_plane.replans import ReplanGovernance
from app.program_plane.models import ReplanRecord
class TestReplan(unittest.TestCase):
    def test_rep(self):
        g = ReplanGovernance()
        r = ReplanRecord(replan_id="r1", program_id="p1", scope_preserving=True, capacity_driven=False)
        g.register_replan(r)
