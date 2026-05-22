import pytest
from app.precedent_plane.models import PrecedentObject, AuthorityClass, ApplicabilityClass, PrecedentClass

def test_precedent_object_creation():
    obj = PrecedentObject(
        precedent_id="P-001",
        precedent_class=PrecedentClass.LOCAL,
        owner="test-owner",
        scope="global",
        authority_posture=AuthorityClass.LOCAL_PERSUASIVE,
        applicability_posture=ApplicabilityClass.DIRECTLY_APPLICABLE
    )
    assert obj.precedent_id == "P-001"
    assert obj.owner == "test-owner"
