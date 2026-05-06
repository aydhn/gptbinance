import unittest
from app.reviews.history import HistoryEngine


class TestReviewHistory(unittest.TestCase):
    def test_record_event(self):
        engine = HistoryEngine()
        event = engine.record_event("item1", "assigned", "user1")
        self.assertEqual(event.event_type, "assigned")
