import pytest
from app.provenance_plane.objects import BaseProvenanceObject
from pydantic import ValidationError

def test_provenance_object_creation():
    obj = BaseProvenanceObject(
        provenance_id="id-1",
        class_type="source",
        owner="test-owner",
        scope="global",
        source_authority="trusted",
        custody_posture="secure"
    )
    assert obj.provenance_id == "id-1"

def test_provenance_object_validation():
    with pytest.raises(ValidationError):
        BaseProvenanceObject(provenance_id="id-1")
