import unittest
from app.reviews.enums import ReviewClass, ReviewPriority
from app.reviews.models import ReviewScope
from app.reviews.requests import ReviewRequestFactory
from app.reviews.exceptions import InvalidReviewRequestError


class TestReviewRequests(unittest.TestCase):
    def test_request_creation(self):
        req = ReviewRequestFactory.create_request(
            ReviewClass.BOARD_CONTRADICTION,
            ReviewScope(workspace_id="ws-1"),
            "test rationale",
            "prod-1",
        )
        self.assertEqual(req.review_class, ReviewClass.BOARD_CONTRADICTION)
        self.assertEqual(req.rationale, "test rationale")
        self.assertEqual(req.producer_id, "prod-1")

    def test_invalid_request_scope(self):
        with self.assertRaises(InvalidReviewRequestError):
            ReviewRequestFactory.create_request(
                ReviewClass.EVIDENCE_PACK, ReviewScope(), "test", "p1"  # empty scope
            )
