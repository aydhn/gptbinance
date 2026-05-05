from typing import Dict, Any, List
import uuid
from app.activation.base import ActivationCompilerBase
from app.activation.models import ActivationIntent, ActivationScope
from app.activation.enums import ActivationClass
from app.activation.exceptions import InvalidActivationIntent


class IntentCompiler(ActivationCompilerBase):
    def compile_intent(self, board_decision: Dict[str, Any]) -> ActivationIntent:
        if (
            board_decision.get("decision") != "GO"
            and board_decision.get("decision") != "CONDITIONAL_GO"
        ):
            raise InvalidActivationIntent(
                "Cannot compile intent without a GO or CONDITIONAL_GO board decision."
            )

        candidate_id = board_decision.get("candidate_id")
        if not candidate_id:
            raise InvalidActivationIntent("Candidate ID missing in board decision.")

        # Resolve activation class from board decision terms
        act_class_str = board_decision.get("activation_class", "canary_limited").upper()
        try:
            act_class = ActivationClass[act_class_str]
        except KeyError:
            act_class = ActivationClass.CANARY_LIMITED

        scope_dict = board_decision.get("scope", {})
        scope = ActivationScope(
            allowed_symbols=scope_dict.get("allowed_symbols", []),
            allowed_profiles=scope_dict.get("allowed_profiles", []),
            allowed_sessions=scope_dict.get("allowed_sessions", []),
            allowed_capital_tiers=scope_dict.get("allowed_capital_tiers", []),
            ttl_seconds=scope_dict.get("ttl_seconds"),
            is_no_new_exposure=scope_dict.get("is_no_new_exposure", False),
        )

        intent_id = f"intent-{uuid.uuid4().hex[:8]}"

        intent = ActivationIntent(
            intent_id=intent_id,
            activation_class=act_class,
            board_decision_ref=board_decision.get("decision_id", "unknown"),
            candidate_id=candidate_id,
            scope=scope,
            forbidden_expansions=board_decision.get("forbidden_expansions", []),
            probation_requirements=board_decision.get("probation_requirements", {}),
        )
        return intent
