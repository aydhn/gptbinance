
from app.control.models import ActionRequest, ApprovalRecord, OperatorIdentity
from app.control.enums import OperatorRole, PolicySeverity
from app.control.actions import registry as action_registry
from app.control.operators import is_self_approval, has_required_roles


class PolicyEngine:
    def __init__(self, severity: PolicySeverity = PolicySeverity.STRICT):
        self.severity = severity

    def evaluate_four_eyes(
        self, request: ActionRequest, record: ApprovalRecord
    ) -> bool:
        """Ensure four-eyes principle (requester cannot approve)."""
        for decision in record.decisions:
            if is_self_approval(request.requester, decision.approver):
                return False
        return True

    def evaluate_role_requirements(
        self, request: ActionRequest, record: ApprovalRecord
    ) -> bool:
        """Ensure required roles are met by approvers."""
        action = action_registry.get_action(request.action_type)
        if not action or not action.required_roles:
            return True

        # Check if at least one approver has the required role(s)
        # For simplicity, we require the combined roles of approvers to cover the required roles
        # or at least one approver to have one of the required roles depending on action definition.
        # Let's say we just need AT LEAST ONE approver to have the required role.
        for decision in record.decisions:
            if has_required_roles(decision.approver, action.required_roles):
                return True
        return False

    def check_duplicate_approvals(self, record: ApprovalRecord) -> bool:
        """Ensure an operator hasn't approved multiple times."""
        approver_ids = set()
        for decision in record.decisions:
            if decision.approver.id in approver_ids:
                return False
            approver_ids.add(decision.approver.id)
        return True

    def get_required_approval_count(self, request: ActionRequest) -> int:
        action = action_registry.get_action(request.action_type)
        if action:
            return action.min_approvals
        return 2  # default safe

    def evaluate(self, request: ActionRequest, record: ApprovalRecord) -> bool:
        if not self.check_duplicate_approvals(record):
            return False
        if not self.evaluate_four_eyes(request, record):
            return False
        if not self.evaluate_role_requirements(request, record):
            return False

        # Only approved decisions count
        approved_count = sum(1 for d in record.decisions if d.approved)
        required_count = self.get_required_approval_count(request)
        return approved_count >= required_count


engine = PolicyEngine()
