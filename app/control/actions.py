from typing import Dict, Optional
from app.control.enums import SensitiveActionType, ActionCriticality, OperatorRole
from app.control.models import SensitiveAction


class ActionRegistry:
    def __init__(self):
        self._actions: Dict[SensitiveActionType, SensitiveAction] = {}
        self._register_defaults()

    def _register_defaults(self):
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.START_LIVE_SESSION,
                criticality=ActionCriticality.HIGH,
                required_roles=[OperatorRole.OPS],
                min_approvals=2,
                ttl_seconds=3600,
                allow_break_glass=True,
                description="Start a live trading session",
                recommended_knowledge_refs=["SOP-LIVE-001"],
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.FLATTEN_LIVE_SESSION,
                criticality=ActionCriticality.CRITICAL,
                required_roles=[OperatorRole.OPS, OperatorRole.RISK],
                min_approvals=2,
                ttl_seconds=1800,
                allow_break_glass=True,
                description="Flatten all positions in a live session",
                recommended_knowledge_refs=["RB-FLATTEN-001"],
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.ROLLBACK_LIVE_SESSION,
                criticality=ActionCriticality.CRITICAL,
                required_roles=[OperatorRole.OPS, OperatorRole.RELEASE],
                min_approvals=2,
                ttl_seconds=1800,
                allow_break_glass=True,
                description="Rollback a live session",
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.APPLY_UPGRADE,
                criticality=ActionCriticality.HIGH,
                required_roles=[OperatorRole.RELEASE],
                min_approvals=2,
                ttl_seconds=7200,
                allow_break_glass=False,
                description="Apply a system upgrade",
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.APPLY_ROLLBACK,
                criticality=ActionCriticality.HIGH,
                required_roles=[OperatorRole.RELEASE, OperatorRole.OPS],
                min_approvals=2,
                ttl_seconds=3600,
                allow_break_glass=True,
                description="Apply a system rollback",
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.APPLY_RESTORE,
                criticality=ActionCriticality.CRITICAL,
                required_roles=[OperatorRole.SECURITY, OperatorRole.OPS],
                min_approvals=2,
                ttl_seconds=3600,
                allow_break_glass=False,
                description="Apply a state restore",
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.APPLY_ROTATION,
                criticality=ActionCriticality.HIGH,
                required_roles=[OperatorRole.SECURITY],
                min_approvals=2,
                ttl_seconds=3600,
                allow_break_glass=False,
                description="Apply credential rotation",
            )
        )
        self.register(
            SensitiveAction(
                action_type=SensitiveActionType.DESTRUCTIVE_RETENTION_CLEANUP,
                criticality=ActionCriticality.CRITICAL,
                required_roles=[OperatorRole.ADMIN],
                min_approvals=2,
                ttl_seconds=1800,
                allow_break_glass=False,
                description="Perform destructive data cleanup",
            )
        )

        # Add more defaults as needed...

    def register(self, action: SensitiveAction):
        self._actions[action.action_type] = action

    def get_action(self, action_type: SensitiveActionType) -> Optional[SensitiveAction]:
        return self._actions.get(action_type)


registry = ActionRegistry()


# Phase 43
def request_shadow_reconcile_review(self):
    pass


def request_shadow_remediation_review(self):
    pass


def request_account_mode_truth_review(self):
    pass
