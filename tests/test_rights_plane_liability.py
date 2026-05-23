
def test_harmed_party_retains_claim():
    from app.liability_plane.residual_exposure import check_harmed_party_rights
    from app.rights_plane.registry import CanonicalRightsRegistry
    class MockRegistry(CanonicalRightsRegistry):
        def get_active_claims_for_beneficiary(self, b_id):
            return ["C-001"]

    res = check_harmed_party_rights("B-001", MockRegistry())
    assert "liability capped but beneficiary rights still open" in res
