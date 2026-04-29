from datetime import datetime
from app.risk.enums import DrawdownState
from app.risk.models import DrawdownStateModel, RiskConfig


class DrawdownTracker:
    def __init__(self, config: RiskConfig):
        self.config = config
        self.peak_equity = 0.0
        self.current_drawdown_pct = 0.0

    def update(self, current_equity: float, timestamp: datetime) -> DrawdownStateModel:
        if current_equity > self.peak_equity:
            self.peak_equity = current_equity

        if self.peak_equity > 0:
            self.current_drawdown_pct = (
                (self.peak_equity - current_equity) / self.peak_equity
            ) * 100
        else:
            self.current_drawdown_pct = 0.0

        state = DrawdownState.NORMAL
        if self.current_drawdown_pct >= self.config.max_account_drawdown_pct:
            state = DrawdownState.HARD_STOP
        elif self.current_drawdown_pct >= self.config.reduce_drawdown_pct:
            state = DrawdownState.REDUCE
        elif self.current_drawdown_pct >= self.config.caution_drawdown_pct:
            state = DrawdownState.CAUTION

        return DrawdownStateModel(
            current_state=state,
            peak_equity=self.peak_equity,
            current_equity=current_equity,
            drawdown_pct=self.current_drawdown_pct,
            last_updated=timestamp,
        )
