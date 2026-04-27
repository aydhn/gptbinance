from typing import Optional, List
from app.research.regime.models import RegimeEvaluationResult, RegimeTransition
from app.research.regime.enums import TransitionType


def detect_transition(
    current_eval: RegimeEvaluationResult,
    previous_eval: Optional[RegimeEvaluationResult],
    history: List[RegimeEvaluationResult] = None,
) -> Optional[RegimeTransition]:
    """
    Detects if there has been a regime transition.
    Returns a RegimeTransition object if a transition occurred, else None.
    """
    if not previous_eval:
        return None

    if current_eval.label.name != previous_eval.label.name:
        # Detected a change
        # Logic to determine type (SUDDEN vs GRADUAL vs WHIPSAW) could be based on history
        # For simplicity in this iteration:

        transition_type = TransitionType.SUDDEN
        if history and len(history) >= 2:
            # Check for whipsaw (flip flop in last few bars)
            # recent_labels = last 2 from history + current
            recent_labels = [e.label.name for e in history[-2:]] + [
                current_eval.label.name
            ]
            # e.g., NO, STRONG, NO
            if (
                len(recent_labels) == 3
                and recent_labels[0] == recent_labels[2]
                and recent_labels[1] != recent_labels[0]
            ):
                transition_type = TransitionType.WHIPSAW
            elif (
                len(
                    set(
                        [e.label.name for e in history[-3:]] + [current_eval.label.name]
                    )
                )
                > 3
            ):
                transition_type = TransitionType.WHIPSAW

        return RegimeTransition(
            timestamp=current_eval.timestamp,
            from_label=previous_eval.label,
            to_label=current_eval.label,
            transition_type=transition_type,
            transition_strength=0.8,  # Placeholder logic
            rationale=f"Regime changed from {previous_eval.label.name} to {current_eval.label.name}",
        )

    return None
