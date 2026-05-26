import unittest
from app.resolution_plane.registry import CanonicalResolutionRegistry
from app.resolution_plane.models import ResolutionObject
from app.resolution_plane.enums import ResolutionClass, TransferClass, ContinuityClass
from app.resolution_plane.exceptions import InvalidResolutionObjectError

class TestCanonicalResolutionRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = CanonicalResolutionRegistry()

    def test_register_and_get_resolution(self):
        res = ResolutionObject(
            resolution_id="RES-001",
            resolution_class=ResolutionClass.CROSS_PLANE_ORDERLY_RESOLUTION,
            owner="admin",
            scope="global",
            transfer_posture=TransferClass.INCLUSIVE_PERIMETER,
            continuity_posture=ContinuityClass.VERIFIED_CONTINUITY
        )
        self.registry.register_resolution(res)
        fetched = self.registry.get_resolution("RES-001")
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.resolution_id, "RES-001")

    def test_duplicate_registration_fails(self):
        res = ResolutionObject(
            resolution_id="RES-001",
            resolution_class=ResolutionClass.CROSS_PLANE_ORDERLY_RESOLUTION,
            owner="admin",
            scope="global",
            transfer_posture=TransferClass.INCLUSIVE_PERIMETER,
            continuity_posture=ContinuityClass.VERIFIED_CONTINUITY
        )
        self.registry.register_resolution(res)
        with self.assertRaises(InvalidResolutionObjectError):
            self.registry.register_resolution(res)

if __name__ == "__main__":
    unittest.main()
