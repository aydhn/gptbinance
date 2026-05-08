from decimal import Decimal
from app.performance_plane.cohorts import CohortAnalyzer
from app.performance_plane.enums import CohortClass


def test_symbol_sleeve_strategy_model_regime_cohorts():
    c = CohortAnalyzer.create_contribution(
        cohort_class=CohortClass.SYMBOL,
        cohort_id="BTCUSDT",
        value=Decimal("12.5"),
        currency="USD",
    )
    assert c.cohort_class == CohortClass.SYMBOL
    assert c.cohort_id == "BTCUSDT"
    assert c.contribution_value == Decimal("12.5")
