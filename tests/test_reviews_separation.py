import unittest
from app.reviews.separation import SeparationOfDutiesEngine
from app.reviews.models import ReviewScope
from app.reviews.enums import ReviewClass
from app.reviews.requests import ReviewRequestFactory
from app.reviews.queues import QueueEngine


class TestReviewSeparation(unittest.TestCase):
    def test_sod_dual_control(self):
        engine = SeparationOfDutiesEngine()
        req = ReviewRequestFactory.create_request(
            ReviewClass.MIGRATION_NON_REVERSIBLE,
            ReviewScope(workspace_id="ws-1"),
            "test",
            "prod-1",
            requires_dual_control=True,
        )
        queue_engine = QueueEngine()
        item = queue_engine.enqueue(req)

        check = engine.check_adjudication_eligibility(item, "prod-1")
        self.assertFalse(check.is_valid)

        check = engine.check_adjudication_eligibility(item, "other-adjudicator")
        self.assertTrue(check.is_valid)
