from app.risk_plane.margins import calculate_margin_state
from app.risk_plane.enums import MarginClass


def test_calculate_margin():
    # 800 locked, 200 usable -> 1000 total. Usage ratio: 80%
    state = calculate_margin_state(
        usable_collateral=200.0, locked_margin=800.0, evidence_refs=[]
    )
    assert state.margin_usage_ratio == 0.8
    assert state.margin_class == MarginClass.PRESSURE
