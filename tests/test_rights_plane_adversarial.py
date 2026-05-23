
def test_pseudo_consent_detected():
    from app.adversarial_plane.confirmations import detect_adversarial_consent
    from app.rights_plane.registry import CanonicalRightsRegistry
    class MockRegistry(CanonicalRightsRegistry):
        def has_adversarial_manipulation(self, chain):
            return True

    res = detect_adversarial_consent(["Consent1"], MockRegistry())
    assert "compliant consent chain under adversarial manipulation" in res
