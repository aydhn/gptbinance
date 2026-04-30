import pytest
from datetime import datetime, timezone
from app.portfolio.models import (
    PortfolioContext,
    PortfolioConfig,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    SymbolSleeve,
    StrategySleeve,
)
from app.portfolio.concentration import ConcentrationEvaluator
from app.portfolio.enums import ConcentrationSeverity


def test_evaluate_concentration():
    config = PortfolioConfig(
        total_budget=1000.0,
        max_symbol_weight=0.30,
        max_strategy_sleeve_weight=0.50,
        max_correlated_cluster_weight=0.60,
    )
    evaluator = ConcentrationEvaluator(config)

    timestamp = datetime.now(timezone.utc)
    context = PortfolioContext(
        timestamp=timestamp,
        budget=PortfolioBudgetSnapshot(
            timestamp=timestamp,
            total_capital=1000.0,
            reserved_capital=0,
            available_capital=1000.0,
            pending_allocations_notional=0.0,
        ),
        exposure=PortfolioExposureSnapshot(
            timestamp=timestamp, total_exposure=0, long_exposure=0, short_exposure=0
        ),
        correlation=CorrelationSnapshot(timestamp=timestamp),
        concentration=ConcentrationSnapshot(timestamp=timestamp),
    )

    # 1. Normal
    context.symbol_sleeves["BTCUSDT"] = SymbolSleeve(
        symbol="BTCUSDT", budget_notional=1000, used_notional=100
    )  # 10%
    snap1 = evaluator.evaluate(context, timestamp)
    assert snap1.severity == ConcentrationSeverity.NORMAL

    # 2. Caution
    context.symbol_sleeves["BTCUSDT"].used_notional = 250  # 25% > 0.8 * 30% (24%)
    snap2 = evaluator.evaluate(context, timestamp)
    assert snap2.severity == ConcentrationSeverity.CAUTION

    # 3. Breach
    context.symbol_sleeves["BTCUSDT"].used_notional = 350  # 35% > 30%
    snap3 = evaluator.evaluate(context, timestamp)
    assert snap3.severity == ConcentrationSeverity.BREACH
    assert "Symbol BTCUSDT weight 0.35 > 0.30" in snap3.breaches[0]
