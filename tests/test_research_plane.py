import pytest
import datetime
import os
import shutil
from app.research_plane.models import (
    ResearchItem,
    ResearchQuestion,
    ResearchScope,
    ResearchObservation,
    ResearchHypothesis,
    EvidenceBundle,
    EvidenceBundleEntry,
    ContradictionRecord,
    ConfidenceAssessment,
    ResearchReadinessRecord,
    ResearchInvalidationRecord,
)
from app.research_plane.enums import (
    ResearchClass,
    QuestionClass,
    EvidenceClass,
    ContradictionClass,
    ConfidenceClass,
    ReadinessClass,
    InvalidationClass,
    OverlapSeverity,
    TrustVerdict,
)
from app.research_plane.repository import ResearchRepository
from app.research_plane.exceptions import (
    InvalidResearchItemError,
    ConfidenceViolationError,
    InvalidHypothesisError,
)
from app.research_plane.questions import QuestionValidator
from app.research_plane.hypotheses import HypothesisContractValidator
from app.research_plane.confidence import ConfidenceLadderManager
from app.research_plane.readiness import ReadinessEvaluator
from app.research_plane.overlap import OverlapDetector
from app.research_plane.trust import TrustVerdictEngine


@pytest.fixture
def test_repo():
    test_path = "test_research_registry"
    if os.path.exists(test_path):
        shutil.rmtree(test_path)
    repo = ResearchRepository(storage_path=test_path)
    yield repo
    if os.path.exists(test_path):
        shutil.rmtree(test_path)


def test_research_registry_integrity(test_repo):
    scope = ResearchScope(symbols=["BTCUSDT"])
    q = ResearchQuestion(
        question_id="q1",
        text="Does volume precede price?",
        question_class=QuestionClass.CAUSAL,
        independent_variables=["volume"],
        dependent_variables=["price"],
        falsifiable=True,
        scope=scope,
    )
    item = ResearchItem(
        research_id="r1",
        title="Vol-Price",
        research_class=ResearchClass.SIGNAL_IDEA,
        question=q,
    )
    test_repo.save(item)

    loaded = test_repo.get("r1")
    assert loaded is not None
    assert loaded.title == "Vol-Price"


def test_falsifiable_question_validation():
    scope = ResearchScope(symbols=["BTCUSDT"])
    q = ResearchQuestion(
        question_id="q1",
        text="Volume is good?",
        question_class=QuestionClass.DESCRIPTIVE,
        independent_variables=["vol"],
        dependent_variables=["good"],
        falsifiable=False,
        scope=scope,
    )
    validator = QuestionValidator()
    with pytest.raises(InvalidResearchItemError):
        validator.validate(q)


def test_hypothesis_mechanism_clarity():
    hyp = ResearchHypothesis(
        hypothesis_id="h1",
        question_ref="q1",
        claimed_effect="Up",
        expected_mechanism="",
        expected_favorable_regimes=["trend"],
        expected_invalidation_triggers=["chop"],
        benchmark_expectation="BuyHold",
        dependency_assumptions=[],
    )
    validator = HypothesisContractValidator()
    with pytest.raises(InvalidHypothesisError):
        validator.validate(hyp)


def test_unjustified_confidence_jump():
    manager = ConfidenceLadderManager()
    bundle = EvidenceBundle(bundle_id="b1", hypothesis_ref="h1", entries=[])

    with pytest.raises(ConfidenceViolationError):
        manager.evaluate_transition(
            ConfidenceClass.SPECULATIVE, ConfidenceClass.EXPERIMENT_READY, bundle, []
        )


def test_experiment_readiness():
    scope = ResearchScope()
    q = ResearchQuestion(
        question_id="q1",
        text="Test?",
        question_class=QuestionClass.CAUSAL,
        independent_variables=["a"],
        dependent_variables=["b"],
        falsifiable=True,
        scope=scope,
    )
    item = ResearchItem(
        research_id="r1",
        title="Test",
        research_class=ResearchClass.SIGNAL_IDEA,
        question=q,
    )

    evaluator = ReadinessEvaluator()
    res = evaluator.evaluate(item)
    assert res.readiness_class == ReadinessClass.NOT_READY
    assert "No hypotheses defined." in res.blockers


def test_duplicate_research_detection():
    scope = ResearchScope()
    q1 = ResearchQuestion(
        question_id="q1",
        text="Same Question",
        question_class=QuestionClass.CAUSAL,
        independent_variables=["a"],
        dependent_variables=["b"],
        falsifiable=True,
        scope=scope,
    )
    item1 = ResearchItem(
        research_id="r1",
        title="Test1",
        research_class=ResearchClass.SIGNAL_IDEA,
        question=q1,
    )

    q2 = ResearchQuestion(
        question_id="q2",
        text="Same Question",
        question_class=QuestionClass.CAUSAL,
        independent_variables=["a"],
        dependent_variables=["b"],
        falsifiable=True,
        scope=scope,
    )
    item2 = ResearchItem(
        research_id="r2",
        title="Test2",
        research_class=ResearchClass.SIGNAL_IDEA,
        question=q2,
    )

    detector = OverlapDetector()
    res = detector.detect_overlap(item1, [item1, item2])
    assert res.severity == OverlapSeverity.CRITICAL


def test_trust_verdict():
    scope = ResearchScope()
    q = ResearchQuestion(
        question_id="q1",
        text="Test?",
        question_class=QuestionClass.CAUSAL,
        independent_variables=["a"],
        dependent_variables=["b"],
        falsifiable=True,
        scope=scope,
    )
    item = ResearchItem(
        research_id="r1",
        title="Test",
        research_class=ResearchClass.SIGNAL_IDEA,
        question=q,
    )

    engine = TrustVerdictEngine()
    verdict = engine.evaluate(item)
    assert (
        verdict.verdict == TrustVerdict.DEGRADED
    )  # Degraded because missing hypotheses and benchmark expectation

    # Add hypothesis and contradiction
    item.hypotheses.append(
        ResearchHypothesis(
            hypothesis_id="h1",
            question_ref="q1",
            claimed_effect="Up",
            expected_mechanism="Mech",
            expected_favorable_regimes=["trend"],
            expected_invalidation_triggers=["chop"],
            benchmark_expectation="BuyHold",
            dependency_assumptions=[],
        )
    )

    item.contradictions.append(
        ContradictionRecord(
            contradiction_id="c1",
            hypothesis_ref="h1",
            contradiction_class=ContradictionClass.DIRECT,
            description="Fails in chop",
            unresolved_burden=True,
        )
    )

    verdict2 = engine.evaluate(item)
    assert verdict2.verdict == TrustVerdict.CAUTION  # Has unresolved contradiction
    assert "Unresolved contradictions: 1" in verdict2.caveats
