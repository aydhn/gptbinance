from app.control.actions import registry
from app.control.enums import SensitiveActionType, ActionCriticality


def test_action_registry_defaults():
    action = registry.get_action(SensitiveActionType.START_LIVE_SESSION)
    assert action is not None
    assert action.criticality == ActionCriticality.HIGH
    assert action.min_approvals == 2
    assert action.allow_break_glass is True

    action = registry.get_action(SensitiveActionType.DESTRUCTIVE_RETENTION_CLEANUP)
    assert action is not None
    assert action.criticality == ActionCriticality.CRITICAL
    assert action.allow_break_glass is False
