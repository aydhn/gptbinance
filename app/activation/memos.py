from app.activation.models import ActivationIntent, ActivationMemo


class MemoBuilder:
    @staticmethod
    def build(intent: ActivationIntent) -> ActivationMemo:
        return ActivationMemo(
            intent_id=intent.intent_id,
            rationale=f"Activation authorized by board decision {intent.board_decision_ref}",
            constraints=[
                f"Class: {intent.activation_class.value}",
                f"Forbidden expansions: {intent.forbidden_expansions}",
            ],
            next_checks=["Market Truth Health", "Shadow Cleanliness"],
        )
