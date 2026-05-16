import unittest
from app.program_plane.releases import ReleaseLinkage
class TestRelease(unittest.TestCase):
    def test_rel(self):
        r = ReleaseLinkage()
        self.assertTrue(r.check_release_ready("p1"))
