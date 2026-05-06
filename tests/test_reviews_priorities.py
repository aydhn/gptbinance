import unittest
from app.reviews.models import ReviewRequest, ReviewScope
from app.reviews.enums import ReviewClass, ReviewPriority
from app.reviews.requests import ReviewRequestFactory
from app.reviews.priorities import calculate_priority


class TestReviewPriorities(unittest.TestCase):
    def test_critical_priority(self):
        req = ReviewRequestFactory.create_request(
            ReviewClass.INCIDENT_CONTAINMENT,
            ReviewScope(incident_id="inc-1"),
            "test",
            "prod1",
        )
        p = calculate_priority(req)
        self.assertEqual(p, ReviewPriority.CRITICAL)

    def test_high_risk_override(self):
        req = ReviewRequestFactory.create_request(
            ReviewClass.EVIDENCE_PACK,
            ReviewScope(workspace_id="ws-1"),
            "test",
            "prod1",
            is_high_risk=True,
        )
        p = calculate_priority(req)
        self.assertEqual(p, ReviewPriority.CRITICAL)
