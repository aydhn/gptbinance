from app.cost_plane.compliance import ComplianceLinkage
def test_compliance_linkage():
    linkage = ComplianceLinkage()
    assert linkage.calculate_audit_cost()["attestation_overhead"] == 1000
