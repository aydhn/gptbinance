import unittest
from app.resolution_plane.models import ResolutionObject, ResolutionRecord
from app.resolution_plane.enums import ResolutionClass, TransferClass, ContinuityClass
from pydantic import ValidationError

class TestResolutionPlaneObjects(unittest.TestCase):
    def test_valid_resolution_object(self):
        res = ResolutionObject(
            resolution_id="RES-001",
            resolution_class=ResolutionClass.CROSS_PLANE_ORDERLY_RESOLUTION,
            owner="admin",
            scope="global",
            transfer_posture=TransferClass.INCLUSIVE_PERIMETER,
            continuity_posture=ContinuityClass.VERIFIED_CONTINUITY
        )
        self.assertEqual(res.resolution_id, "RES-001")
        self.assertEqual(res.resolution_class, ResolutionClass.CROSS_PLANE_ORDERLY_RESOLUTION)

    def test_missing_fields_validation(self):
        with self.assertRaises(ValidationError):
            ResolutionObject(
                resolution_id="RES-002",
                # missing resolution_class
                owner="admin",
                scope="global",
                transfer_posture=TransferClass.INCLUSIVE_PERIMETER,
                continuity_posture=ContinuityClass.VERIFIED_CONTINUITY
            )

if __name__ == "__main__":
    unittest.main()
