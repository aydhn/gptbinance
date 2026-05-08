from app.risk_plane.drawdowns import calculate_drawdown_state
from app.risk_plane.enums import RiskDomain, DrawdownClass


def test_calculate_drawdown():
    dd = calculate_drawdown_state(
        domain=RiskDomain.ACCOUNT,
        target_id="MAIN",
        peak_value=1000.0,
        current_value=800.0,
        realized_dd=50.0,
        drawdown_class=DrawdownClass.ACCOUNT,
    )
    assert dd.unrealized_drawdown == 200.0
    assert dd.realized_drawdown == 50.0
