import unittest
from app.reviews.storage import InMemoryReviewStorage
from app.reviews.repository import ReviewRepository
from app.reviews.requests import ReviewRequestFactory
from app.reviews.enums import ReviewClass
from app.reviews.models import ReviewScope
from app.reviews.queues import QueueEngine


class TestReviewStorage(unittest.TestCase):
    def test_storage(self):
        store = InMemoryReviewStorage()
        repo = ReviewRepository(store)

        req = ReviewRequestFactory.create_request(
            ReviewClass.POLICY_CONFLICT, ReviewScope(workspace_id="ws"), "rat", "p1"
        )
        q = QueueEngine()
        item = q.enqueue(req)

        repo.save_item(item)

        items = repo.get_pending_items()
        self.assertEqual(len(items), 1)
