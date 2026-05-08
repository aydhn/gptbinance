from decimal import Decimal
from app.performance_plane.cohorts import CohortAnalyzer
from app.performance_plane.enums import CohortClass
from app.performance_plane.contributions import ContributionAggregator


def test_contribution_rollups():
    c1 = CohortAnalyzer.create_contribution(
        CohortClass.SYMBOL, "BTCUSDT", Decimal("10.0"), "USD"
    )
    c2 = CohortAnalyzer.create_contribution(
        CohortClass.SYMBOL, "ETHUSDT", Decimal("5.0"), "USD"
    )
    c3 = CohortAnalyzer.create_contribution(
        CohortClass.SYMBOL, "BTCUSDT", Decimal("2.5"), "USD"
    )

    # Intentionally mix classes to test filtering
    c4 = CohortAnalyzer.create_contribution(
        CohortClass.STRATEGY, "Strat_A", Decimal("100.0"), "USD"
    )

    summary = ContributionAggregator.rollup([c1, c2, c3, c4], CohortClass.SYMBOL)

    assert summary["BTCUSDT"] == 12.5
    assert summary["ETHUSDT"] == 5.0
    assert "Strat_A" not in summary
