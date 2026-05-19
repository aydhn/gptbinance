import pytest
from app.learning_plane.registry import CanonicalLearningRegistry
from app.learning_plane.equivalence import EquivalenceAnalyzer
from app.learning_plane.models import LearningObject
from app.learning_plane.enums import LearningClass, EquivalenceVerdict

def test_equivalence_equivalent():
    registry = CanonicalLearningRegistry()
    analyzer = EquivalenceAnalyzer()

    obj1 = LearningObject(
        learning_id="base1",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        signal_ids=["sig1"],
        lesson_ids=["lesson1"],
        action_ids=["action1"],
        validation_posture="none"
    )
    obj2 = LearningObject(
        learning_id="compare1",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org2",
        signal_ids=["sig1"],
        lesson_ids=["lesson1"],
        action_ids=["action1"],
        validation_posture="none"
    )
    registry.register_object(obj1)
    registry.register_object(obj2)

    report = analyzer.compare_environments("base1", "compare1")
    assert report.verdict == EquivalenceVerdict.EQUIVALENT
    assert len(report.blockers) == 0

def test_equivalence_divergent():
    registry = CanonicalLearningRegistry()
    analyzer = EquivalenceAnalyzer()

    obj1 = LearningObject(
        learning_id="base2",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        signal_ids=["sig1"],
        lesson_ids=["lesson1"],
        action_ids=["action1"],
        validation_posture="none"
    )
    obj2 = LearningObject(
        learning_id="compare2",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org2",
        signal_ids=["sig1"],
        lesson_ids=["lesson2"], # Different
        action_ids=["action1"],
        validation_posture="none"
    )
    registry.register_object(obj1)
    registry.register_object(obj2)

    report = analyzer.compare_environments("base2", "compare2")
    assert report.verdict == EquivalenceVerdict.DIVERGENT
    assert "Lesson extraction divergence detected." in report.blockers
