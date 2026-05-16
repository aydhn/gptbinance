import unittest
from app.program_plane.blockers import BlockerHandler
from app.program_plane.models import BlockerRecord
from app.program_plane.enums import BlockerClass
class TestBlocker(unittest.TestCase):
    def test_blocker(self):
        b = BlockerHandler()
        rec = BlockerRecord(blocker_id="b1", program_id="p1", blocker_class=BlockerClass.HARD, severity="high")
        b.register(rec)
        self.assertEqual(len(b.list_active("p1")), 1)
