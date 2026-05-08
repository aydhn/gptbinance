from datetime import datetime, timezone
from typing import List, Optional
from .models import (
    RiskState,
    DrawdownState,
    LossState,
    ConcentrationState,
    MarginState,
    LiquidationProximityState,
)
from .enums import RiskDomain


class CanonicalRiskStateBuilder:
    def __init__(self):
        pass

    def build_risk_state(
        self,
        state_id: str,
        domain: RiskDomain,
        target_id: str,
        authoritative: bool,
        source_position_refs: List[str],
        source_ledger_refs: List[str],
        source_market_truth_refs: List[str],
        drawdown: Optional[DrawdownState] = None,
        loss: Optional[LossState] = None,
        concentration: Optional[ConcentrationState] = None,
        margin: Optional[MarginState] = None,
        liquidation: Optional[LiquidationProximityState] = None,
    ) -> RiskState:
        summary_parts = []
        if drawdown:
            summary_parts.append("Drawdown")
        if loss:
            summary_parts.append("Loss")
        if concentration:
            summary_parts.append("Concentration")
        if margin:
            summary_parts.append("Margin")
        if liquidation:
            summary_parts.append("Liquidation")

        completeness = (
            "FULL" if len(summary_parts) == 5 else f"PARTIAL: {','.join(summary_parts)}"
        )

        return RiskState(
            state_id=state_id,
            domain=domain,
            target_id=target_id,
            timestamp=datetime.now(timezone.utc),
            authoritative=authoritative,
            source_position_refs=source_position_refs,
            source_ledger_refs=source_ledger_refs,
            source_market_truth_refs=source_market_truth_refs,
            drawdown=drawdown,
            loss=loss,
            concentration=concentration,
            margin=margin,
            liquidation=liquidation,
            completeness_summary=completeness,
        )
