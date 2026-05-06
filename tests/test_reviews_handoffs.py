import unittest
from app.reviews.handoffs import HandoffEngine
from app.reviews.enums import HandoffClass


class TestReviewHandoffs(unittest.TestCase):
    def test_handoff(self):
        engine = HandoffEngine()
        ho = engine.handoff(
            "item1", HandoffClass.SHIFT_CHANGE, "user1", "user2", "shift end"
        )
        self.assertEqual(ho.to_assignee_id, "user2")
