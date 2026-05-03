from app.stressrisk.enums import ShockType
from app.stressrisk.models import ShockVector
from app.stressrisk.shocks import ShockEngine


def test_shock_engine():
    engine = ShockEngine()
    shocks = [ShockVector(shock_type=ShockType.PRICE, value_multiplier=0.8)]
    state = {"price": 100.0}
    shocked_state = engine.apply_shocks(state, shocks)
    assert shocked_state["price"] == 80.0
