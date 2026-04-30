import pytest
from datetime import datetime, timezone
from app.backtest.enums import OrderSide
from app.portfolio.models import (
    PortfolioCandidate,
    PortfolioContext,
    CorrelationSnapshot,
    ConcentrationSnapshot,
    PortfolioBudgetSnapshot,
    PortfolioExposureSnapshot,
    SymbolSleeve,
)
from app.portfolio.overlap import OverlapEstimator
from app.portfolio.enums import OverlapType


class DummyIntent:
    def __init__(self, sym):
        self.symbol = sym
        self.side = OrderSide.BUY
        self.quantity = 1.0


def test_estimate_overlap():
    estimator = OverlapEstimator()

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

    # 1. Test no overlap
    cand1 = PortfolioCandidate(intent=DummyIntent("BTCUSDT"))
    rep1 = estimator.estimate_overlap(cand1, context)
    assert rep1.overlap_type == OverlapType.NONE

    # 2. Test same symbol same dir
    context.symbol_sleeves["BTCUSDT"] = SymbolSleeve(
        symbol="BTCUSDT", budget_notional=100.0, used_notional=50.0
    )
    rep2 = estimator.estimate_overlap(cand1, context)
    assert rep2.overlap_type == OverlapType.SAME_SYMBOL_SAME_DIR
    assert "BTCUSDT" in rep2.overlapping_symbols
    assert rep2.overlap_severity_score == 5.0

    # 3. Test high correlation same dir
    context.correlation.clusters["USDT_QUOTE"] = ["ETHUSDT", "SOLUSDT"]
    context.symbol_sleeves["SOLUSDT"] = SymbolSleeve(
        symbol="SOLUSDT", budget_notional=100.0, used_notional=50.0
    )

    cand3 = PortfolioCandidate(intent=DummyIntent("ETHUSDT"))
    rep3 = estimator.estimate_overlap(cand3, context)

    assert rep3.overlap_type == OverlapType.HIGH_CORR_SAME_DIR
    assert "SOLUSDT" in rep3.overlapping_symbols
    assert rep3.overlap_severity_score == 3.0
