from datetime import datetime
from app.research.regime.mtf_context import build_mtf_context
from app.research.regime.models import (
    RegimeContext,
    RegimeSuitabilityMap,
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)
from app.research.regime.enums import RegimeFamily, ContextQuality


def create_context(interval, trend_name):
    evals = {
        RegimeFamily.TREND: RegimeEvaluationResult(
            timestamp=datetime.now(),
            label=RegimeLabel(family=RegimeFamily.TREND, name=trend_name),
            score=RegimeScore(score=0.8, confidence=0.8),
            quality=RegimeQualityReport(
                quality=ContextQuality.HIGH, stability_score=1.0
            ),
            rationale="test",
        )
    }
    return RegimeContext(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval=interval,
        evaluations=evals,
        transitions={},
        suitability=RegimeSuitabilityMap(
            timestamp=datetime.now(),
            symbol="BTCUSDT",
            interval=interval,
            compatibilities={},
        ),
        overall_quality=ContextQuality.HIGH,
    )


def test_mtf_context_consistency():
    base = create_context("15m", "STRONG_UPTREND")
    higher = {"1h": create_context("1h", "STRONG_UPTREND")}

    mtf = build_mtf_context(base, higher)
    assert mtf.consistency_score == 1.0
    assert not mtf.contradiction_warnings


def test_mtf_context_contradiction():
    base = create_context("15m", "STRONG_UPTREND")
    higher = {"1h": create_context("1h", "STRONG_DOWNTREND")}

    mtf = build_mtf_context(base, higher)
    assert mtf.consistency_score < 1.0
    assert mtf.contradiction_warnings
