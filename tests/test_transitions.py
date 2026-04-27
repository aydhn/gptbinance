from datetime import datetime
from app.research.regime.transitions import detect_transition
from app.research.regime.models import (
    RegimeEvaluationResult,
    RegimeLabel,
    RegimeScore,
    RegimeQualityReport,
)
from app.research.regime.enums import RegimeFamily, ContextQuality, TransitionType


def create_mock_eval(name):
    return RegimeEvaluationResult(
        timestamp=datetime.now(),
        label=RegimeLabel(family=RegimeFamily.TREND, name=name),
        score=RegimeScore(score=0.8, confidence=0.8),
        quality=RegimeQualityReport(quality=ContextQuality.HIGH, stability_score=1.0),
        rationale="test",
    )


def test_transition_sudden():
    prev = create_mock_eval("STRONG_UPTREND")
    curr = create_mock_eval("STRONG_DOWNTREND")

    t = detect_transition(curr, prev, [prev])
    assert t is not None
    assert t.transition_type == TransitionType.SUDDEN


def test_transition_whipsaw():
    e1 = create_mock_eval("STRONG_UPTREND")
    e2 = create_mock_eval("NO_TREND")
    e3 = create_mock_eval("STRONG_UPTREND")
    e4 = create_mock_eval("NO_TREND")

    t = detect_transition(e4, e3, [e1, e2, e3])
    assert t is not None
    assert t.transition_type == TransitionType.WHIPSAW
