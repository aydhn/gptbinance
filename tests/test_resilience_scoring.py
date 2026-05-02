from app.resilience.scoring import ResilienceScorer
from app.resilience.models import (
    ExperimentSummary,
    AssertionResult,
    RecoveryAssertion,
    ExperimentGateReport,
)
from app.resilience.enums import (
    AssertionVerdict,
    ExperimentStatus,
    SafeScope,
    GateVerdict,
)
from datetime import datetime, timezone


def test_resilience_scorer_all_pass():
    scorer = ResilienceScorer()

    summary = ExperimentSummary(
        run_id="test",
        definition_id="test",
        scope=SafeScope.PAPER,
        status=ExperimentStatus.COMPLETED,
        start_time=datetime.now(timezone.utc),
        gate_report=ExperimentGateReport(verdict=GateVerdict.ALLOW, reason="ok"),
        assertion_results=[
            AssertionResult(
                spec_id="a1",
                verdict=AssertionVerdict.PASS,
                message="ok",
                evaluated_at=datetime.now(timezone.utc),
            )
        ],
        recovery_results=[
            RecoveryAssertion(
                spec_id="r1",
                verdict=AssertionVerdict.PASS,
                message="ok",
                evaluated_at=datetime.now(timezone.utc),
            )
        ],
    )

    score = scorer.calculate_score(summary)
    assert score.overall_score == 100
    assert score.assertions_pass_rate == 1.0


def test_resilience_scorer_partial_fail():
    scorer = ResilienceScorer()

    summary = ExperimentSummary(
        run_id="test",
        definition_id="test",
        scope=SafeScope.PAPER,
        status=ExperimentStatus.COMPLETED,
        start_time=datetime.now(timezone.utc),
        gate_report=ExperimentGateReport(verdict=GateVerdict.ALLOW, reason="ok"),
        assertion_results=[
            AssertionResult(
                spec_id="a1",
                verdict=AssertionVerdict.PASS,
                message="ok",
                evaluated_at=datetime.now(timezone.utc),
            ),
            AssertionResult(
                spec_id="a2",
                verdict=AssertionVerdict.FAIL,
                message="fail",
                evaluated_at=datetime.now(timezone.utc),
            ),
        ],
        recovery_results=[
            RecoveryAssertion(
                spec_id="r1",
                verdict=AssertionVerdict.PASS,
                message="ok",
                evaluated_at=datetime.now(timezone.utc),
            )
        ],
    )

    score = scorer.calculate_score(summary)
    assert score.overall_score < 100
    assert score.assertions_pass_rate == 2 / 3
