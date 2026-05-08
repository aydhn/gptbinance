from typing import List
from .models import LossState
from .enums import RiskDomain


def calculate_loss_state(
    domain: RiskDomain,
    target_id: str,
    realized_loss: float,
    open_loss: float,
    evidence_refs: List[str],
) -> LossState:
    session_loss = realized_loss + open_loss

    caveats = []
    if open_loss > 0:
        caveats.append("Significant open loss burden present.")

    return LossState(
        domain=domain,
        target_id=target_id,
        realized_loss=realized_loss,
        open_loss_burden=open_loss,
        session_loss=session_loss,
        evidence_refs=evidence_refs,
        caveats=caveats,
    )
