import pytest
from datetime import datetime, timezone
from app.portfolio.models import (
    PortfolioContext,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    StrategySleeve,
    SymbolSleeve,
)
from app.portfolio.sleeves import SleeveManager


def test_sleeve_headroom():
    manager = SleeveManager()

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

    context.strategy_sleeves["core"] = StrategySleeve(
        strategy_family="core", budget_notional=500.0, used_notional=200.0
    )
    context.symbol_sleeves["BTCUSDT"] = SymbolSleeve(
        symbol="BTCUSDT", budget_notional=300.0, used_notional=250.0
    )

    headroom = manager.check_headroom(context)

    assert headroom["strategy_core"] == 300.0
    assert headroom["symbol_BTCUSDT"] == 50.0

    manager.update_usage(context, "core", "BTCUSDT", 40.0)

    assert context.strategy_sleeves["core"].used_notional == 240.0
    assert context.symbol_sleeves["BTCUSDT"].used_notional == 290.0
