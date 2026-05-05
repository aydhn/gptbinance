import json
import os
from typing import Dict, Any, List, Optional

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

STORAGE_DIR = ".activation_data"


def _get_file_path(entity_type: str, intent_id: str) -> str:
    os.makedirs(STORAGE_DIR, exist_ok=True)
    return os.path.join(STORAGE_DIR, f"{entity_type}_{intent_id}.json")


def _save_model(model: Any, entity_type: str, intent_id: str):
    path = _get_file_path(entity_type, intent_id)
    with open(path, "w") as f:
        f.write(model.model_dump_json(indent=2))


def _load_model(model_cls, entity_type: str, intent_id: str) -> Optional[Any]:
    path = _get_file_path(entity_type, intent_id)
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        return model_cls.model_validate_json(f.read())


class ActivationStorage:
    @staticmethod
    def save_intent(intent: ActivationIntent):
        _save_model(intent, "intent", intent.intent_id)

    @staticmethod
    def load_intent(intent_id: str) -> Optional[ActivationIntent]:
        return _load_model(ActivationIntent, "intent", intent_id)

    @staticmethod
    def save_plan(plan: ActivationPlan):
        _save_model(plan, "plan", plan.intent_id)

    @staticmethod
    def load_plan(intent_id: str) -> Optional[ActivationPlan]:
        return _load_model(ActivationPlan, "plan", intent_id)

    @staticmethod
    def save_snapshot(snapshot: ActiveSetSnapshot):
        _save_model(snapshot, "snapshot", snapshot.snapshot_id)

    @staticmethod
    def load_snapshot(snapshot_id: str) -> Optional[ActiveSetSnapshot]:
        return _load_model(ActiveSetSnapshot, "snapshot", snapshot_id)

    @staticmethod
    def save_probation_status(status: ProbationStatus):
        _save_model(status, "probation", status.intent_id)

    @staticmethod
    def load_probation_status(intent_id: str) -> Optional[ProbationStatus]:
        return _load_model(ProbationStatus, "probation", intent_id)

    @staticmethod
    def save_halt_decision(decision: HaltDecision):
        _save_model(decision, "halt", decision.intent_id)

    @staticmethod
    def load_halt_decision(intent_id: str) -> Optional[HaltDecision]:
        return _load_model(HaltDecision, "halt", intent_id)

    @staticmethod
    def save_revert_plan(plan: RevertPlan):
        _save_model(plan, "revert", plan.intent_id)

    @staticmethod
    def load_revert_plan(intent_id: str) -> Optional[RevertPlan]:
        return _load_model(RevertPlan, "revert", intent_id)

    @staticmethod
    def save_memo(memo: ActivationMemo):
        _save_model(memo, "memo", memo.intent_id)

    @staticmethod
    def load_memo(intent_id: str) -> Optional[ActivationMemo]:
        return _load_model(ActivationMemo, "memo", intent_id)

    @staticmethod
    def append_history(record: ActivationHistoryRecord):
        # Simplistic append: load all, append, save
        os.makedirs(STORAGE_DIR, exist_ok=True)
        path = os.path.join(STORAGE_DIR, f"history_{record.intent_id}.json")
        records = []
        if os.path.exists(path):
            with open(path, "r") as f:
                records = [
                    ActivationHistoryRecord.model_validate(r) for r in json.load(f)
                ]
        records.append(record)
        with open(path, "w") as f:
            json.dump([r.model_dump(mode="json") for r in records], f, indent=2)

    @staticmethod
    def load_history(intent_id: str) -> List[ActivationHistoryRecord]:
        path = os.path.join(STORAGE_DIR, f"history_{intent_id}.json")
        if not os.path.exists(path):
            return []
        with open(path, "r") as f:
            return [ActivationHistoryRecord.model_validate(r) for r in json.load(f)]
