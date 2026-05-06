import unittest
from app.reviews.enums import AssignmentClass
from app.reviews.assignments import AssignmentEngine
from app.reviews.models import QueueItem, ReviewRequest, ReviewScope
from app.reviews.requests import ReviewRequestFactory
from app.reviews.enums import ReviewClass, ReviewPriority
from app.reviews.queues import QueueEngine


class TestReviewAssignments(unittest.TestCase):
    def test_assignment(self):
        engine = AssignmentEngine()
        q_engine = QueueEngine()
        req = ReviewRequestFactory.create_request(
            ReviewClass.EVIDENCE_PACK, ReviewScope(workspace_id="ws"), "test", "prod"
        )
        item = q_engine.enqueue(req)

        assign = engine.assign(item, "user-1", AssignmentClass.REVIEWER)
        self.assertEqual(assign.assignee_id, "user-1")
        self.assertEqual(assign.assignment_class, AssignmentClass.REVIEWER)

        assigns = engine.get_assignments_for_item(item.item_id)
        self.assertEqual(len(assigns), 1)
