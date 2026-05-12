from datetime import datetime
from typing import Dict, List, Optional

from .exceptions import InvalidBudgetPolicy
from .models import ErrorBudgetPolicy, ErrorBudgetSnapshot


class ErrorBudgetManager:
    def __init__(self):
        self._policies: Dict[str, ErrorBudgetPolicy] = {}
        self._snapshots: Dict[str, List[ErrorBudgetSnapshot]] = {}

    def register_policy(self, policy: ErrorBudgetPolicy) -> None:
        if not policy.policy_id:
            raise InvalidBudgetPolicy("Policy ID cannot be empty.")
        if policy.freeze_threshold < policy.depletion_threshold_alert:
            raise InvalidBudgetPolicy(
                "Freeze threshold must be >= depletion threshold alert."
            )
        self._policies[policy.policy_id] = policy

    def get_policy(self, policy_id: str) -> Optional[ErrorBudgetPolicy]:
        return self._policies.get(policy_id)

    def list_policies(self) -> List[ErrorBudgetPolicy]:
        return list(self._policies.values())

    def record_snapshot(self, snapshot: ErrorBudgetSnapshot) -> None:
        if snapshot.policy_id not in self._policies:
            raise InvalidBudgetPolicy(f"Unknown policy_id: {snapshot.policy_id}")
        if snapshot.policy_id not in self._snapshots:
            self._snapshots[snapshot.policy_id] = []
        self._snapshots[snapshot.policy_id].append(snapshot)

    def get_latest_snapshot(self, policy_id: str) -> Optional[ErrorBudgetSnapshot]:
        snapshots = self._snapshots.get(policy_id, [])
        if not snapshots:
            return None
        return sorted(snapshots, key=lambda s: s.timestamp)[-1]

    def list_snapshots(self, policy_id: str) -> List[ErrorBudgetSnapshot]:
        return sorted(self._snapshots.get(policy_id, []), key=lambda s: s.timestamp)
