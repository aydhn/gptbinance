import unittest
from app.reviews.evidence import EvidenceEngine


class TestReviewEvidence(unittest.TestCase):
    def test_assemble_pack(self):
        engine = EvidenceEngine()
        pack = engine.assemble_pack(["ref1", "ref2"])
        self.assertEqual(len(pack), 2)
        self.assertTrue(engine.verify_pack(pack))
