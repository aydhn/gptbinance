import unittest
from app.program_plane.critical_path import CriticalPathEngine
class TestCP(unittest.TestCase):
    def test_cp(self):
        e = CriticalPathEngine()
        rep = e.evaluate("p1", ["m1", "m2"])
        self.assertEqual(rep.path_confidence, 1.0)
