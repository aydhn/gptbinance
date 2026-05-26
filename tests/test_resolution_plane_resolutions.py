import unittest
from app.resolution_plane.models import ResolutionRecord

class TestResolutionPlaneResolutions(unittest.TestCase):
    def test_resolution_record(self):
        rec = ResolutionRecord(
            id="REC-001",
            resolution_id="RES-001",
            state="initiated",
            proof_notes="Tested transition",
            lineage_refs=["L-01", "L-02"]
        )
        self.assertEqual(rec.id, "REC-001")
        self.assertEqual(rec.resolution_id, "RES-001")
        self.assertEqual(rec.state, "initiated")
        self.assertEqual(rec.proof_notes, "Tested transition")
        self.assertIn("L-01", rec.lineage_refs)

if __name__ == "__main__":
    unittest.main()
