import unittest
from app.program_plane.trust import TrustedProgramVerdictEngine
from app.program_plane.enums import TrustVerdict
class TestTrust(unittest.TestCase):
    def test_trust(self):
        e = TrustedProgramVerdictEngine()
        r = e.evaluate("p1")
        self.assertEqual(r.verdict, TrustVerdict.TRUSTED)
