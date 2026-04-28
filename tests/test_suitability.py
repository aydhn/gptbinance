from datetime import datetime
from app.research.regime.suitability import calculate_suitability
from app.research.regime.models import (
    RegimeContext,
    RegimeSuitabilityMap,
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)
from app.research.regime.enums import RegimeFamily, ContextQuality, SuitabilityVerdict


def create_context_for_suit(trend_name, vol_name):
    evals = {
        RegimeFamily.TREND: RegimeEvaluationResult(
            timestamp=datetime.now(),
            label=RegimeLabel(family=RegimeFamily.TREND, name=trend_name),
            score=RegimeScore(score=0.8, confidence=0.8),
            quality=RegimeQualityReport(
                quality=ContextQuality.HIGH, stability_score=1.0
            ),
            rationale="test",
        ),
        RegimeFamily.VOLATILITY: RegimeEvaluationResult(
            timestamp=datetime.now(),
            label=RegimeLabel(family=RegimeFamily.VOLATILITY, name=vol_name),
            score=RegimeScore(score=0.8, confidence=0.8),
            quality=RegimeQualityReport(
                quality=ContextQuality.HIGH, stability_score=1.0
            ),
            rationale="test",
        ),
    }
    return RegimeContext(
        timestamp=datetime.now(),
        symbol="BTCUSDT",
        interval="15m",
        evaluations=evals,
        transitions={},
        suitability=RegimeSuitabilityMap(
            timestamp=datetime.now(),
            symbol="BTCUSDT",
            interval="15m",
            compatibilities={},
        ),
        overall_quality=ContextQuality.HIGH,
    )


def test_suitability_trend():
    ctx = create_context_for_suit("STRONG_UPTREND", "NORMAL")
    suit = calculate_suitability(ctx)

    tf = suit.compatibilities["trend_following_core"]
    assert tf.verdict == SuitabilityVerdict.OPTIMAL

    mr = suit.compatibilities["mean_reversion_core"]
    assert mr.verdict == SuitabilityVerdict.AVOID


def test_suitability_mr():
    ctx = create_context_for_suit("NO_TREND", "LOW_ENERGY")
    suit = calculate_suitability(ctx)

    tf = suit.compatibilities["trend_following_core"]
    assert tf.verdict == SuitabilityVerdict.AVOID

    mr = suit.compatibilities["mean_reversion_core"]
    assert mr.verdict == SuitabilityVerdict.ALLOW
