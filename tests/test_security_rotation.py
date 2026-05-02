from app.security.rotation import RotationReadiness


def test_rotation():
    rr = RotationReadiness()
    rep = rr.get_report()
    assert rep.readiness_score > 0
    assert len(rep.impacted_modules) > 0
