
def test_non_authorized_representative_cannot_waive():
    from app.authority_plane.delegation import check_waiver_authority_rights
    from app.rights_plane.registry import CanonicalRightsRegistry
    class MockRegistry(CanonicalRightsRegistry):
        def is_standing_valid(self, s_id):
            return False

    res = check_waiver_authority_rights("WaiverAction", "S-001", MockRegistry())
    assert "waived right by non-authorized representative" in res
