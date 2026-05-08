from typing import List
from .models import ConcentrationState
from .enums import RiskDomain


def calculate_concentration(
    domain: RiskDomain,
    target_id: str,
    target_value: float,
    total_value: float,
    lineage_refs: List[str],
) -> ConcentrationState:
    ratio = target_value / total_value if total_value > 0 else 0.0
    clipping_reason = "High Concentration" if ratio > 0.5 else None

    return ConcentrationState(
        domain=domain,
        target_id=target_id,
        concentration_ratio=ratio,
        clipping_reason=clipping_reason,
        lineage_refs=lineage_refs,
    )
