import unittest
from app.resolution_plane.registry import CanonicalResolutionRegistry
from app.resolution_plane.trust import TrustedResolutionVerdictEngine
from app.resolution_plane.models import ResolutionObject
from app.resolution_plane.enums import ResolutionClass, TransferClass, ContinuityClass, TrustVerdict

class TestTrustedResolutionVerdictEngine(unittest.TestCase):
    def setUp(self):
        self.registry = CanonicalResolutionRegistry()
        self.engine = TrustedResolutionVerdictEngine(self.registry)

    def test_trusted_verdict(self):
        res = ResolutionObject(
            resolution_id="RES-001",
            resolution_class=ResolutionClass.CROSS_PLANE_ORDERLY_RESOLUTION,
            owner="admin",
            scope="global",
            transfer_posture=TransferClass.INCLUSIVE_PERIMETER,
            continuity_posture=ContinuityClass.VERIFIED_CONTINUITY
        )
        self.registry.register_resolution(res)
        verdict = self.engine.evaluate_trust("RES-001")
        self.assertEqual(verdict.verdict, TrustVerdict.TRUSTED)
        self.assertEqual(len(verdict.caveats), 0)

    def test_blocked_verdict_on_broken_continuity(self):
        res = ResolutionObject(
            resolution_id="RES-002",
            resolution_class=ResolutionClass.BRIDGE_RESOLUTION,
            owner="admin",
            scope="global",
            transfer_posture=TransferClass.INCLUSIVE_PERIMETER,
            continuity_posture=ContinuityClass.BROKEN_CONTINUITY
        )
        self.registry.register_resolution(res)
        verdict = self.engine.evaluate_trust("RES-002")
        self.assertEqual(verdict.verdict, TrustVerdict.BLOCKED)
        self.assertIn("Broken continuity detected", verdict.caveats)

if __name__ == "__main__":
    unittest.main()
