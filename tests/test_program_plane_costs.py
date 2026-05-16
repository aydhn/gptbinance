import unittest
from app.program_plane.costs import CostLinkage
class TestCost(unittest.TestCase):
    def test_cost(self):
        c = CostLinkage()
        self.assertEqual(c.check_slippage_cost("p1"), 0.0)
