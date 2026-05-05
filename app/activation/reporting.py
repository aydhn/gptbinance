import json
from app.activation.models import (
    ActivationIntent,
    ActivationPlan,
    ProbationStatus,
    ExpansionDecision,
    HaltDecision,
    RevertPlan,
    ActivationMemo,
    ActiveSetSnapshot,
)


class ActivationReporter:
    @staticmethod
    def format_intent(intent: ActivationIntent) -> str:
        return intent.model_dump_json(indent=2)

    @staticmethod
    def format_plan(plan: ActivationPlan) -> str:
        return plan.model_dump_json(indent=2)

    @staticmethod
    def format_probation(status: ProbationStatus) -> str:
        return status.model_dump_json(indent=2)

    @staticmethod
    def format_expansion(decision: ExpansionDecision) -> str:
        return decision.model_dump_json(indent=2)

    @staticmethod
    def format_halt(decision: HaltDecision) -> str:
        return decision.model_dump_json(indent=2)

    @staticmethod
    def format_revert(plan: RevertPlan) -> str:
        return plan.model_dump_json(indent=2)

    @staticmethod
    def format_memo(memo: ActivationMemo) -> str:
        return memo.model_dump_json(indent=2)

    @staticmethod
    def format_active_set(snapshot: ActiveSetSnapshot) -> str:
        return snapshot.model_dump_json(indent=2)
