from typing import Optional, List
from app.activation.storage import ActivationStorage
from app.activation.models import (
    ActivationIntent,
    ActivationPlan,
    ActiveSetSnapshot,
    ProbationStatus,
    HaltDecision,
    RevertPlan,
    ActivationMemo,
    ActivationHistoryRecord,
)


class ActivationRepository:
    def __init__(self):
        self.storage = ActivationStorage()

    def get_intent(self, intent_id: str) -> Optional[ActivationIntent]:
        return self.storage.load_intent(intent_id)

    def save_intent(self, intent: ActivationIntent):
        self.storage.save_intent(intent)

    def get_plan(self, intent_id: str) -> Optional[ActivationPlan]:
        return self.storage.load_plan(intent_id)

    def save_plan(self, plan: ActivationPlan):
        self.storage.save_plan(plan)

    def save_snapshot(self, snapshot: ActiveSetSnapshot):
        self.storage.save_snapshot(snapshot)

    def get_snapshot(self, snapshot_id: str) -> Optional[ActiveSetSnapshot]:
        return self.storage.load_snapshot(snapshot_id)

    def get_probation_status(self, intent_id: str) -> Optional[ProbationStatus]:
        return self.storage.load_probation_status(intent_id)

    def save_probation_status(self, status: ProbationStatus):
        self.storage.save_probation_status(status)

    def save_halt_decision(self, decision: HaltDecision):
        self.storage.save_halt_decision(decision)

    def get_halt_decision(self, intent_id: str) -> Optional[HaltDecision]:
        return self.storage.load_halt_decision(intent_id)

    def get_revert_plan(self, intent_id: str) -> Optional[RevertPlan]:
        return self.storage.load_revert_plan(intent_id)

    def save_revert_plan(self, plan: RevertPlan):
        self.storage.save_revert_plan(plan)

    def get_memo(self, intent_id: str) -> Optional[ActivationMemo]:
        return self.storage.load_memo(intent_id)

    def save_memo(self, memo: ActivationMemo):
        self.storage.save_memo(memo)

    def append_history(self, record: ActivationHistoryRecord):
        self.storage.append_history(record)

    def get_history(self, intent_id: str) -> List[ActivationHistoryRecord]:
        return self.storage.load_history(intent_id)


activation_repo = ActivationRepository()
