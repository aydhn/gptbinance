
def test_precedent_cannot_generalize_across_mismatched_beneficiaries():
    from app.precedent_plane.applicability import check_precedent_rights_transfer
    from app.rights_plane.registry import CanonicalRightsRegistry
    class MockRegistry(CanonicalRightsRegistry):
        def verify_beneficiary_scope(self, p_id, scope):
            return False

    res = check_precedent_rights_transfer("P-001", "Global", MockRegistry())
    assert "precedent generalized across mismatched beneficiaries" in res
