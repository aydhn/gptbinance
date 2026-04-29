from app.risk.regime_adjustments import RegimeAdjuster
from app.risk.enums import RegimeRiskMode


def test_regime_adjuster():
    adj = RegimeAdjuster()
    assert adj.get_multiplier(RegimeRiskMode.NORMAL) == 1.0
    assert adj.get_multiplier(RegimeRiskMode.CAUTION) == 0.5
    assert adj.get_multiplier(RegimeRiskMode.RESTRICTIVE) == 0.25
