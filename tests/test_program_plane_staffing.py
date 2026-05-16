import unittest
from app.program_plane.staffing import StaffingManager
class TestStaffing(unittest.TestCase):
    def test_staff(self):
        s = StaffingManager()
        r = s.evaluate("p1")
        self.assertTrue(r.staffing_drift)
