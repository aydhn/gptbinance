from datetime import datetime
from typing import Optional
from app.risk.enums import DrawdownState
from app.risk.models import DrawdownStateModel, KillSwitchState


class RiskStateManager:
    def __init__(self):
        self.drawdown_state = DrawdownStateModel(last_updated=datetime.now())
        self.kill_switch_state = KillSwitchState()
        self.last_veto_time: Optional[datetime] = None

    def update_drawdown(self, new_state: DrawdownStateModel):
        self.drawdown_state = new_state

    def update_kill_switch(self, new_state: KillSwitchState):
        self.kill_switch_state = new_state

    def record_veto(self, timestamp: datetime):
        self.last_veto_time = timestamp
