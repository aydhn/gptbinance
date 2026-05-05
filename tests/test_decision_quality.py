from datetime import datetime, timezone
from app.decision_quality.models import (
    DecisionFunnelRecord,
    FunnelStageRecord,
    DecisionOutcomeWindow,
    DecisionQualityConfig,
)
from app.decision_quality.enums import (
    FunnelStage,
    DecisionClass,
    BlockReasonClass,
    OutcomeWindow,
    DecisionQualityVerdict,
    EvidenceConfidence,
    FrictionClass,
)
from app.decision_quality.opportunities import OpportunityCapture
from app.decision_quality.funnel import SignalToActionFunnel
from app.decision_quality.block_reasons import BlockReasonTaxonomy

from app.decision_quality.hindsight import HindsightSafeguard
from app.decision_quality.outcomes import OutcomeEvaluator
from app.decision_quality.friction import FrictionAnalyzer


from app.decision_quality.storage import DecisionQualityStore
from app.decision_quality.repository import DecisionQualityRepository


def test_opportunity_capture():
    capture = OpportunityCapture()
    candidate = capture.capture_candidate(
        symbol="BTCUSDT",
        regime="trend",
        strategy_family="momentum",
        timeframe="15m",
        profile="live",
        signal_strength=0.8,
        market_truth_posture="healthy",
        event_risk_context="none",
        universe_eligibility_context="eligible",
    )
    assert candidate.symbol == "BTCUSDT"
    assert candidate.regime == "trend"
    assert candidate.signal_strength == 0.8


def test_funnel():
    capture = OpportunityCapture()
    candidate = capture.capture_candidate(
        symbol="BTCUSDT",
        regime="trend",
        strategy_family="momentum",
        timeframe="15m",
        profile="live",
        signal_strength=0.8,
        market_truth_posture="healthy",
        event_risk_context="none",
        universe_eligibility_context="eligible",
    )

    funnel = SignalToActionFunnel()
    funnel.start_funnel(candidate)

    funnel.record_stage(
        opportunity_id=candidate.id,
        stage=FunnelStage.SIGNAL_GENERATED,
        passed=True,
        entered_at=datetime.now(timezone.utc),
    )

    final_record = funnel.finalize_funnel(candidate.id, DecisionClass.EXECUTED)
    assert final_record.final_class == DecisionClass.EXECUTED
    assert len(final_record.stages) == 1


def test_block_reasons():
    taxonomy = BlockReasonTaxonomy()
    reason = taxonomy.create_block_reason(
        opportunity_id="test_id",
        reason_class=BlockReasonClass.MARKET_TRUTH_STALE,
        description="Data is stale",
        is_primary=True,
    )
    assert reason.reason_class == BlockReasonClass.MARKET_TRUTH_STALE
    assert reason.is_primary is True

    resolved = taxonomy.resolve_primary_reason([reason])
    assert resolved == reason


def test_friction_analyzer():
    analyzer = FrictionAnalyzer()

    # Mock a funnel record that failed at POLICY_EVALUATED
    record = DecisionFunnelRecord(
        opportunity_id="test_id",
        final_class=DecisionClass.BLOCKED,
        created_at=datetime.now(timezone.utc),
        stages=[
            FunnelStageRecord(
                id="test_id_stage1",
                opportunity_id="test_id",
                stage=FunnelStage.POLICY_EVALUATED,
                entered_at=datetime.now(timezone.utc),
                passed=False,
            )
        ],
    )

    frictions = analyzer.analyze_friction(record)
    assert len(frictions) == 1
    assert frictions[0].friction_class == FrictionClass.POLICY_HARD_BLOCK


def test_hindsight_safeguard():
    safeguard = HindsightSafeguard()

    conf = safeguard.evaluate_confidence(
        is_market_truth_stale=True, is_event_window=False, evidence_refs=[]
    )
    assert conf == EvidenceConfidence.UNSAFE_TO_JUDGE

    conf = safeguard.evaluate_confidence(
        is_market_truth_stale=False, is_event_window=True, evidence_refs=[]
    )
    assert conf == EvidenceConfidence.WEAK

    conf = safeguard.evaluate_confidence(
        is_market_truth_stale=False, is_event_window=False, evidence_refs=["proof"]
    )
    assert conf == EvidenceConfidence.STRONG


def test_outcome_evaluator():
    evaluator = OutcomeEvaluator()
    window = DecisionOutcomeWindow(
        window_type=OutcomeWindow.SHORT,
        start_time=datetime.now(timezone.utc),
        end_time=datetime.now(timezone.utc),
    )

    # Test Executed Well
    outcome = evaluator.evaluate_executed(
        opportunity_id="test_id",
        window=window,
        realized_pnl=10.0,
        is_stale=False,
        is_event=False,
        evidence=["ref1"],
    )
    assert outcome.verdict == DecisionQualityVerdict.EXECUTED_WELL

    # Test Blocked and Likely Saved Loss
    outcome = evaluator.evaluate_blocked(
        opportunity_id="test_id",
        window=window,
        simulated_pnl=-5.0,
        is_stale=False,
        is_event=False,
        evidence=["ref1"],
    )
    assert outcome.verdict == DecisionQualityVerdict.BLOCKED_AND_LIKELY_SAVED_LOSS


def test_storage(tmp_path):
    db_path = tmp_path / "test_decision_quality.db"
    config = DecisionQualityConfig(storage_path=str(db_path))
    store = DecisionQualityStore(config)
    repo = DecisionQualityRepository(store)

    capture = OpportunityCapture()
    candidate = capture.capture_candidate(
        symbol="BTCUSDT",
        regime="trend",
        strategy_family="momentum",
        timeframe="15m",
        profile="live",
        signal_strength=0.8,
        market_truth_posture="healthy",
        event_risk_context="none",
        universe_eligibility_context="eligible",
    )

    repo.save_opportunity(candidate)

    loaded = repo.get_opportunity(candidate.id)
    assert loaded is not None
    assert loaded.id == candidate.id
    assert loaded.symbol == "BTCUSDT"
