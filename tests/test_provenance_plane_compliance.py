import pytest
from app.compliance_plane.findings import check_compliance_provenance

def test_regulated_field_provenance_gaps_finding():
    assert "FINDING" in check_compliance_provenance("comp-1", True)
    assert "TRUSTED" in check_compliance_provenance("comp-2", False)
