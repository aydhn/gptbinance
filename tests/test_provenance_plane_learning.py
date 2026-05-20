import pytest
from app.learning_plane.validated_causes import check_validated_cause_provenance

def test_validated_cause_requires_attribution():
    assert "CAUTION" in check_validated_cause_provenance("cause-1", False)
    assert "TRUSTED" in check_validated_cause_provenance("cause-2", True)
