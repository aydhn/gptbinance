import unittest
from app.program_plane.slippage import SlippageHandler
class TestSlip(unittest.TestCase):
    def test_slip(self):
        s = SlippageHandler()
        r = s.register_slip("p1")
        self.assertFalse(r.cascading_slip)
