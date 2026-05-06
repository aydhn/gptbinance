import unittest
from app.reviews.adjudication import AdjudicationEngine
from app.reviews.enums import AdjudicationVerdict, ReviewClass
from app.reviews.requests import ReviewRequestFactory
from app.reviews.queues import QueueEngine
from app.reviews.models import ReviewScope


class TestReviewAdjudication(unittest.TestCase):
    def test_adjudication(self):
        engine = AdjudicationEngine()
        req = ReviewRequestFactory.create_request(
            ReviewClass.BOARD_CONTRADICTION,
            ReviewScope(workspace_id="ws-1"),
            "test",
            "prod-1",
        )
        queue_engine = QueueEngine()
        item = queue_engine.enqueue(req)

        decision = engine.adjudicate(
            item, "adj-1", AdjudicationVerdict.APPROVE_FOR_NEXT_STEP, "looks good"
        )
        self.assertEqual(
            decision.adjudication.verdict, AdjudicationVerdict.APPROVE_FOR_NEXT_STEP
        )
        self.assertEqual(decision.adjudication.rationale, "looks good")
