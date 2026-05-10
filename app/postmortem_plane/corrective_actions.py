from typing import List
from datetime import datetime
from app.postmortem_plane.models import CorrectiveAction, ActionVerificationRecord
from app.postmortem_plane.exceptions import InvalidRemediationActionError

class CorrectiveActionRegistry:
    @staticmethod
    def register_action(action_id: str, desc: str, owner: str, due: datetime, scope: str, blocking: bool = False, deps: List[str] = None) -> CorrectiveAction:
        if not owner:
            raise InvalidRemediationActionError("Owner is required")
        if "monitor" in desc.lower() and len(desc) < 20:
             raise InvalidRemediationActionError("Vague monitor actions not allowed")

        return CorrectiveAction(
            action_id=action_id,
            description=desc,
            owner=owner,
            due_date=due,
            target_scope=scope,
            is_blocking=blocking,
            dependency_refs=deps or []
        )
