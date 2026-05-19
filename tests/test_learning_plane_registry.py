import pytest
from app.learning_plane.registry import CanonicalLearningRegistry
from app.learning_plane.models import LearningObject, LearningPlaneConfig
from app.learning_plane.enums import LearningClass
from app.learning_plane.exceptions import InvalidLearningObject

def test_registry_requires_id():
    registry = CanonicalLearningRegistry()
    obj = LearningObject(
        learning_id="",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        validation_posture="none"
    )
    with pytest.raises(InvalidLearningObject):
        registry.register_object(obj)

def test_registry_requires_origin_in_strict_mode():
    config = LearningPlaneConfig(enforce_strict_lineage=True)
    registry = CanonicalLearningRegistry(config=config)
    obj = LearningObject(
        learning_id="lrn1",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="",
        validation_posture="none"
    )
    with pytest.raises(InvalidLearningObject):
        registry.register_object(obj)

def test_registry_successful_registration():
    registry = CanonicalLearningRegistry()
    obj = LearningObject(
        learning_id="lrn1",
        learning_class=LearningClass.INCIDENT_LEARNING,
        owner="user",
        scope="global",
        origin_id="org1",
        validation_posture="none"
    )
    registry.register_object(obj)
    retrieved = registry.get_object("lrn1")
    assert retrieved.learning_id == "lrn1"
