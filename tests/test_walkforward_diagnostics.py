import pytest
from app.backtest.walkforward.diagnostics import DiagnosticAnalyzer
from app.backtest.walkforward.models import (
    WalkForwardSegmentResult,
    WalkForwardWindow,
    WindowDiagnostic,
)
from app.backtest.walkforward.enums import SegmentStatus


def _make_segment(
    index: int, decay: float, oos_exp: float, trades: int
) -> WalkForwardSegmentResult:
    win = WalkForwardWindow(
        segment_index=index,
        is_start=0,
        is_end=10,
        oos_start=10,
        oos_end=20,
        is_length=10,
        oos_length=10,
        is_valid=True,
    )
    diag = WindowDiagnostic(
        is_expectancy=1.0,
        oos_expectancy=oos_exp,
        expectancy_decay=decay,
        is_trade_count=10,
        oos_trade_count=trades,
        oos_max_drawdown=0.1,
    )
    return WalkForwardSegmentResult(
        segment_index=index,
        window=win,
        status=SegmentStatus.COMPLETED,
        diagnostics=diag,
    )


def test_diagnostics():
    segments = [
        _make_segment(1, decay=0.8, oos_exp=-0.1, trades=1),
        _make_segment(2, decay=0.6, oos_exp=-0.2, trades=5),
        _make_segment(3, decay=0.0, oos_exp=1.0, trades=10),
    ]

    analyzer = DiagnosticAnalyzer()
    res = analyzer.analyze(segments)

    # avg decay = (0.8 + 0.6 + 0.0) / 3 = 0.46 (>0.3)
    # negative oos = 2 / 3 (>50%)
    # low trades = 1 segment

    assert len(res) == 3
    assert any("High average OOS decay" in d for d in res)
    assert any("More than half of OOS segments" in d for d in res)
    assert any("trade drought" in d for d in res)
