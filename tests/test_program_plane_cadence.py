import unittest
from app.program_plane.cadence import CadenceManager
class TestCadence(unittest.TestCase):
    def test_cadence(self):
        c = CadenceManager()
        r = c.track("p1")
        self.assertEqual(r.misses, 0)
