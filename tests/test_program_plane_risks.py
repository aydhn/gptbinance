import unittest
from app.program_plane.risks import DeliveryRiskManager
class TestRisk(unittest.TestCase):
    def test_risk(self):
        m = DeliveryRiskManager()
        r = m.evaluate_risks("p1")
        self.assertEqual(r.risk_type, "dependency_risk")
