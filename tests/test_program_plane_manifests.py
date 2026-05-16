import unittest
from app.program_plane.manifests import ProgramManifestBuilder
class TestMan(unittest.TestCase):
    def test_man(self):
        b = ProgramManifestBuilder()
        r = b.build("p1")
        self.assertEqual(r.artifact_hash, "hash123")
