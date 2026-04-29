from typing import List, Optional
from datetime import datetime
from app.risk.models import KillSwitchState, RiskContext, RiskConfig
from app.risk.enums import KillSwitchType, DrawdownState


class KillSwitchEvaluator:
    def __init__(self, config: RiskConfig):
        self.config = config
        self.state = KillSwitchState()

    def evaluate(self, context: RiskContext, timestamp: datetime) -> KillSwitchState:
        triggers: List[KillSwitchType] = []
        rationales: List[str] = []

        # 1. Drawdown Breach
        if context.drawdown_state.current_state == DrawdownState.HARD_STOP:
            triggers.append(KillSwitchType.DRAWDOWN_BREACH)
            rationales.append(
                f"Drawdown reached hard stop level: {context.drawdown_state.drawdown_pct:.2f}%"
            )

        # 2. Exposure Explosion (Simple hardcoded guard for now)
        if (
            context.exposure_snapshot.total_gross_exposure
            > context.exposure_snapshot.total_equity * 5.0
        ):  # Arbitrary hardcode for sanity
            triggers.append(KillSwitchType.EXPOSURE_EXPLOSION)
            rationales.append("Gross exposure exceeds 5x equity limit.")

        is_active = len(triggers) > 0
        if is_active and not self.state.is_active:
            self.state.last_triggered_at = timestamp

        self.state.is_active = is_active
        self.state.active_triggers = triggers
        self.state.rationale = " | ".join(rationales)

        return self.state
