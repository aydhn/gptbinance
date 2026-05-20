import pytest
from app.assurance_plane.evidence import check_assurance_evidence_provenance

def test_assurance_evidence_lowers_confidence():
    assert "CAUTION" in check_assurance_evidence_provenance("assur-1", True)
    assert "TRUSTED" in check_assurance_evidence_provenance("assur-2", False)
