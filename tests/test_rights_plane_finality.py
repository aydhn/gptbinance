
def test_settlement_under_surviving_challenge_blocked():
    from app.finality_plane.settlement import verify_settlement_closure_rights
    from app.rights_plane.registry import CanonicalRightsRegistry
    class MockRegistry(CanonicalRightsRegistry):
        def is_right_surviving(self, r_id):
            return True

    res = verify_settlement_closure_rights("S-001", ["R-001"], MockRegistry())
    assert "settled label under surviving beneficiary right" in res
