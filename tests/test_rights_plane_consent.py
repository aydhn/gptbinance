
def test_blanket_consent_generates_caution():
    from app.rights_plane.consent import evaluate_consent
    from app.rights_plane.models import ConsentRecord, ConsentScopeRecord
    from app.rights_plane.enums import ConsentClass

    scope = ConsentScopeRecord(scope_id="S1", purpose="All", duration="Forever", is_blanket=True)
    consent = ConsentRecord(consent_id="C1", holder_ref="H1", scope_ref="S1", consent_class=ConsentClass.EXPLICIT)

    res = evaluate_consent(consent, scope)
    assert "caution" in res
