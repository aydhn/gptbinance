import pytest
from app.learning_plane.registry import CanonicalLearningRegistry
from app.learning_plane.trust import TrustedLearningVerdictEngine
from app.learning_plane.equivalence import EquivalenceAnalyzer
from app.learning_plane.models import LearningObject, RecurrenceRecord
from app.learning_plane.enums import LearningClass, RecurrenceClass, TrustVerdict
from app.learning_plane.storage import storage

def test_integration_recurrence_blocks_readiness():
    # Simulate Readiness checking trust verdict when recurrence exists
    registry = CanonicalLearningRegistry()
    engine = TrustedLearningVerdictEngine(registry)

    obj = LearningObject(
        learning_id="lrn_int_1",
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
        recurrence_ids=["rec1"], # RECURRENCE!
        validation_posture="validated"
    )
    registry.register_object(obj)

    rec = RecurrenceRecord(
        recurrence_id="rec1",
        recurrence_class=RecurrenceClass.SAME_FAILURE,
        description="Same failure happened again",
        severity="high",
        interval="1 day",
        proof_notes="Observed in logs"
    )
    storage.save_recurrence(rec)

    verdict = engine.evaluate_trust("lrn_int_1")
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert "Failed" in verdict.factors["recurrence_control"]
