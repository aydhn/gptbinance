import unittest
from app.program_plane.commitments import CommitmentManager
class TestCommitment(unittest.TestCase):
    def test_com(self):
        c = CommitmentManager()
        r = c.create_commitment("p1")
        self.assertFalse(r.is_rebaselined)
