from app.policy_kernel.storage import (
    store_decision,
    get_decision,
    store_conflicts,
    get_conflicts,
)
from app.policy_kernel.rules import list_rules
from app.policy_kernel.invariants import list_invariants
from app.policy_kernel.drift import list_drifts
from app.policy_kernel.gaps import list_gaps


class PolicyRepository:
    def save_decision(self, decision):
        store_decision(decision)

    def fetch_decision(self, decision_id):
        return get_decision(decision_id)

    def save_conflicts(self, action_id, conflicts):
        store_conflicts(action_id, conflicts)

    def fetch_conflicts(self, action_id):
        return get_conflicts(action_id)

    def fetch_all_rules(self):
        return list_rules()

    def fetch_all_invariants(self):
        return list_invariants()

    def fetch_all_drifts(self):
        return list_drifts()

    def fetch_all_gaps(self):
        return list_gaps()
