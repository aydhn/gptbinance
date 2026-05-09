from typing import List, Dict
from app.control_plane.models import (
    ApprovalDecision,
    ActionApprovalChain,
)


class ApprovalEngine:
    def __init__(self):
        self._decisions: Dict[str, List[ApprovalDecision]] = {}
        self._chains: Dict[str, ActionApprovalChain] = {}

    def init_chain(self, action_id: str, required_approvals: int = 1):
        self._chains[action_id] = ActionApprovalChain(
            action_id=action_id, required_approvals=required_approvals
        )
        self._decisions[action_id] = []

    def record_decision(self, decision: ApprovalDecision):
        if decision.action_id not in self._decisions:
            self._decisions[decision.action_id] = []
            self._chains[decision.action_id] = ActionApprovalChain(
                action_id=decision.action_id, required_approvals=1
            )

        self._decisions[decision.action_id].append(decision)
        if decision.is_approved:
            self._chains[decision.action_id].current_approvals += 1
            if decision.approver not in self._chains[decision.action_id].approvers:
                self._chains[decision.action_id].approvers.append(decision.approver)

    def is_approved(self, action_id: str) -> bool:
        chain = self._chains.get(action_id)
        if not chain:
            return False
        return chain.current_approvals >= chain.required_approvals

    def get_decisions(self, action_id: str) -> List[ApprovalDecision]:
        return self._decisions.get(action_id, [])
