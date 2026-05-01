import pytest
from datetime import datetime, timezone
from app.portfolio.models import (
    PortfolioConfig,
    PortfolioContext,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    SymbolSleeve,
    StrategySleeve,
)
from app.portfolio.policies import PortfolioPolicyManager


def test_max_symbol_weight():
    config = PortfolioConfig(total_budget=1000.0, max_symbol_weight=0.20)
    manager = PortfolioPolicyManager(config)

    context = PortfolioContext(
        timestamp=datetime.now(timezone.utc),
        budget=PortfolioBudgetSnapshot(
            timestamp=datetime.now(timezone.utc),
            total_capital=1000.0,
            reserved_capital=0,
            available_capital=1000.0,
            pending_allocations_notional=0.0,
        ),
        exposure=PortfolioExposureSnapshot(
            timestamp=datetime.now(timezone.utc),
            total_exposure=0,
            long_exposure=0,
            short_exposure=0,
        ),
        correlation=CorrelationSnapshot(timestamp=datetime.now(timezone.utc)),
        concentration=ConcentrationSnapshot(timestamp=datetime.now(timezone.utc)),
    )
    context.symbol_sleeves["BTCUSDT"] = SymbolSleeve(
        symbol="BTCUSDT", budget_notional=200, used_notional=100
    )

    # 100 + 50 = 150 -> 15% <= 20%
    err = manager.check_max_symbol_weight("BTCUSDT", 50.0, context)
    assert err is None

    # 100 + 150 = 250 -> 25% > 20%
    err = manager.check_max_symbol_weight("BTCUSDT", 150.0, context)
    assert err is not None
    assert "Max symbol weight exceeded" in err


def test_reserve_cash_ratio():
    config = PortfolioConfig(
        total_budget=1000.0, reserve_cash_ratio=0.10
    )  # 100 reserved
    manager = PortfolioPolicyManager(config)

    context = PortfolioContext(
        timestamp=datetime.now(timezone.utc),
        budget=PortfolioBudgetSnapshot(
            timestamp=datetime.now(timezone.utc),
            total_capital=1000.0,
            reserved_capital=100.0,
            available_capital=200.0,  # only 200 available right now
            pending_allocations_notional=0.0,
        ),
        exposure=PortfolioExposureSnapshot(
            timestamp=datetime.now(timezone.utc),
            total_exposure=0,
            long_exposure=0,
            short_exposure=0,
        ),
        correlation=CorrelationSnapshot(timestamp=datetime.now(timezone.utc)),
        concentration=ConcentrationSnapshot(timestamp=datetime.now(timezone.utc)),
    )

    # allocate 50 -> avail becomes 150. 150 >= 100 (reserved) -> OK
    err = manager.check_reserve_cash(50.0, context)
    assert err is None

    # allocate 150 -> avail becomes 50. 50 < 100 (reserved) -> Error
    err = manager.check_reserve_cash(150.0, context)
    assert err is not None
    assert "Reserve cash ratio breached" in err
