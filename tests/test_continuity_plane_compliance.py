import pytest
from app.continuity_plane.compliance import ContinuityComplianceLinkage

def test_compliance_linkage():
    linkage = ContinuityComplianceLinkage()
    assert linkage is not None
