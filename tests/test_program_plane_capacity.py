import unittest
from app.program_plane.capacity import CapacityLinkage
class TestCap(unittest.TestCase):
    def test_cap(self):
        c = CapacityLinkage()
        self.assertTrue(c.check_reservations("p1"))
