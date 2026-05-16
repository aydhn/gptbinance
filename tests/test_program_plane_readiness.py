import unittest
from app.program_plane.readiness import ProgramReadinessAggregator
class TestReadiness(unittest.TestCase):
    def test_readiness(self):
        a = ProgramReadinessAggregator()
        self.assertEqual(a.aggregate("p1"), "ready")
