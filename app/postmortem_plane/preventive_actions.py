from typing import List
from datetime import datetime
from app.postmortem_plane.models import PreventiveAction
from app.postmortem_plane.exceptions import InvalidRemediationActionError

class PreventiveActionRegistry:
    @staticmethod
    def register_action(action_id: str, desc: str, owner: str, due: datetime, scope: str, objective: str, blocking: bool = False, deps: List[str] = None) -> PreventiveAction:
        if not owner:
            raise InvalidRemediationActionError("Owner is required")
        if not objective:
             raise InvalidRemediationActionError("Recurrence prevention objective is required")

        return PreventiveAction(
            action_id=action_id,
            description=desc,
            owner=owner,
            due_date=due,
            target_scope=scope,
            recurrence_prevention_objective=objective,
            is_blocking=blocking,
            dependency_refs=deps or []
        )
