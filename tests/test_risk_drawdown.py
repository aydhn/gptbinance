from datetime import datetime
from app.risk.drawdown import DrawdownTracker
from app.risk.models import RiskConfig
from app.risk.enums import DrawdownState


def test_drawdown_tracking():
    config = RiskConfig(
        max_account_drawdown_pct=20.0,
        reduce_drawdown_pct=15.0,
        caution_drawdown_pct=10.0,
    )
    tracker = DrawdownTracker(config)

    # New peak
    state = tracker.update(10000.0, datetime.now())
    assert state.peak_equity == 10000.0
    assert state.current_state == DrawdownState.NORMAL

    # 5% DD
    state = tracker.update(9500.0, datetime.now())
    assert state.drawdown_pct == 5.0
    assert state.current_state == DrawdownState.NORMAL

    # 12% DD
    state = tracker.update(8800.0, datetime.now())
    assert state.drawdown_pct == 12.0
    assert state.current_state == DrawdownState.CAUTION

    # 16% DD
    state = tracker.update(8400.0, datetime.now())
    assert state.drawdown_pct == 16.0
    assert state.current_state == DrawdownState.REDUCE

    # 25% DD
    state = tracker.update(7500.0, datetime.now())
    assert state.drawdown_pct == 25.0
    assert state.current_state == DrawdownState.HARD_STOP
