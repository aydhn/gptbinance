from app.policy_plane.models import PolicyAction
from app.policy_plane.enums import ActionClass


class ActionRegistry:
    pass


def create_execute_action(action_id: str = None) -> PolicyAction:
    return PolicyAction(action_class=ActionClass.EXECUTE, action_id=action_id)


def create_approve_action(action_id: str = None) -> PolicyAction:
    return PolicyAction(action_class=ActionClass.APPROVE, action_id=action_id)
