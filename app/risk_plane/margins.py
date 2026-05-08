from typing import List
from .models import MarginState
from .enums import MarginClass


def calculate_margin_state(
    usable_collateral: float, locked_margin: float, evidence_refs: List[str]
) -> MarginState:
    total_col = usable_collateral + locked_margin
    margin_usage_ratio = locked_margin / total_col if total_col > 0 else 1.0

    if margin_usage_ratio > 0.9:
        margin_class = MarginClass.CRITICAL
    elif margin_usage_ratio > 0.7:
        margin_class = MarginClass.PRESSURE
    elif margin_usage_ratio > 0.5:
        margin_class = MarginClass.ELEVATED
    else:
        margin_class = MarginClass.SAFE

    fragility = locked_margin / (usable_collateral + 1e-9)

    return MarginState(
        margin_class=margin_class,
        margin_usage_ratio=margin_usage_ratio,
        usable_collateral=usable_collateral,
        collateral_fragility_ratio=fragility,
        evidence_refs=evidence_refs,
        proof_notes=[
            f"Usage: {margin_usage_ratio*100:.1f}%, Usable: {usable_collateral}"
        ],
    )
