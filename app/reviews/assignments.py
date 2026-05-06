from app.reviews.models import ReviewAssignment, QueueItem
from app.reviews.enums import AssignmentClass, ReviewState
from app.reviews.exceptions import InvalidAssignmentError
import uuid


class AssignmentEngine:
    def __init__(self):
        self._assignments = {}

    def assign(
        self, item: QueueItem, assignee_id: str, role: AssignmentClass
    ) -> ReviewAssignment:
        if item.state not in [ReviewState.PENDING, ReviewState.ASSIGNED]:
            raise InvalidAssignmentError("Can only assign pending or assigned items.")

        assignment = ReviewAssignment(
            assignment_id=str(uuid.uuid4()),
            item_id=item.item_id,
            assignee_id=assignee_id,
            assignment_class=role,
        )
        self._assignments[assignment.assignment_id] = assignment
        return assignment

    def get_assignments_for_item(self, item_id: str) -> list[ReviewAssignment]:
        return [
            a
            for a in self._assignments.values()
            if a.item_id == item_id and a.is_active
        ]
