from datetime import datetime
from typing import List
from app.postmortem_plane.models import PostmortemClosureRecord, PostmortemDefinition
from app.postmortem_plane.enums import ClosureClass
from app.postmortem_plane.exceptions import ClosureViolationError

class PostmortemClosureGovernance:
    @staticmethod
    def evaluate_readiness(postmortem: PostmortemDefinition) -> PostmortemClosureRecord:
        blockers = []

        # Check action debt
        for action in postmortem.corrective_actions + postmortem.preventive_actions:
            if not action.verification_records:
                blockers.append(f"Action {action.action_id} lacks verification")

        if blockers:
            return PostmortemClosureRecord(
                closure_status=ClosureClass.BLOCKED_VERIFICATION,
                closure_rationale="Unresolved verifications",
                unresolved_blockers=blockers
            )

        return PostmortemClosureRecord(
            closure_status=ClosureClass.READY,
            closure_rationale="All actions verified",
            unresolved_blockers=[]
        )

    @staticmethod
    def close(postmortem: PostmortemDefinition, by: str) -> PostmortemClosureRecord:
        readiness = PostmortemClosureGovernance.evaluate_readiness(postmortem)
        if readiness.closure_status != ClosureClass.READY:
             raise ClosureViolationError(f"Cannot close: {readiness.unresolved_blockers}")

        readiness.closure_status = ClosureClass.CLOSED
        readiness.closed_at = datetime.now()
        readiness.closed_by = by
        return readiness
