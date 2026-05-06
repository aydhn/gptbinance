import unittest
from app.reviews.models import ReviewScope
from app.reviews.enums import ReviewClass, ReviewPriority
from app.reviews.requests import ReviewRequestFactory
from app.reviews.queues import QueueEngine


class TestReviewQueues(unittest.TestCase):
    def test_queue_enqueue(self):
        engine = QueueEngine()
        req = ReviewRequestFactory.create_request(
            ReviewClass.BOARD_CONTRADICTION,
            ReviewScope(workspace_id="ws-1"),
            "test",
            "prod-1",
        )
        item = engine.enqueue(req)
        self.assertIsNotNone(item)
        self.assertEqual(item.priority, ReviewPriority.HIGH)

        items = engine.get_pending_items()
        self.assertEqual(len(items), 1)
