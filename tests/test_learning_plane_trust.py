import pytest
from app.learning_plane.registry import CanonicalLearningRegistry
from app.learning_plane.trust import TrustedLearningVerdictEngine
from app.learning_plane.models import LearningObject
from app.learning_plane.enums import LearningClass, TrustVerdict

def test_trust_engine_degraded_no_signals():
    registry = CanonicalLearningRegistry()
    engine = TrustedLearningVerdictEngine(registry)

    obj = LearningObject(
        learning_id="lrn_trust_1",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        validation_posture="none",
        # no signal_ids
    )
    registry.register_object(obj)

    verdict = engine.evaluate_trust("lrn_trust_1")
    assert verdict.verdict in [TrustVerdict.DEGRADED, TrustVerdict.BLOCKED]

def test_trust_engine_blocked_no_lessons():
    registry = CanonicalLearningRegistry()
    engine = TrustedLearningVerdictEngine(registry)

    obj = LearningObject(
        learning_id="lrn_trust_2",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        signal_ids=["sig1"],
        finding_ids=["fnd1"],
        cause_ids=["cause1"],
        # no lesson_ids
        validation_posture="none"
    )
    registry.register_object(obj)

    verdict = engine.evaluate_trust("lrn_trust_2")
    assert verdict.verdict == TrustVerdict.BLOCKED

def test_trust_engine_trusted():
    registry = CanonicalLearningRegistry()
    engine = TrustedLearningVerdictEngine(registry)

    obj = LearningObject(
        learning_id="lrn_trust_3",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        signal_ids=["sig1"],
        finding_ids=["fnd1"],
        hypothesis_ids=["hyp1"],
        cause_ids=["cause1"],
        lesson_ids=["lesson1"],
        target_ids=["target1"],
        action_ids=["action1"],
        validation_ids=["val1"],
        validation_posture="validated"
    )
    registry.register_object(obj)

    verdict = engine.evaluate_trust("lrn_trust_3")
    assert verdict.verdict == TrustVerdict.TRUSTED
