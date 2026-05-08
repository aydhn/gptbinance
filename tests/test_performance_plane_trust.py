from datetime import datetime, timezone
from app.performance_plane.trust import TrustEngine
from app.performance_plane.enums import WindowClass, TrustVerdict
from app.performance_plane.windows import WindowManager
from app.performance_plane.manifests import ManifestBuilder


def test_trust_verdict_synthesis():
    w_incomplete = WindowManager.create_window(
        WindowClass.SESSION, datetime(2024, 1, 1, tzinfo=timezone.utc)
    )
    m_incomplete = ManifestBuilder.build(w_incomplete, [])

    v1 = TrustEngine.evaluate(m_incomplete, [])
    assert v1.verdict == TrustVerdict.CAUTION
    assert "Incomplete window" in v1.blockers[0]

    w_complete = WindowManager.create_window(
        WindowClass.SESSION,
        datetime(2024, 1, 1, tzinfo=timezone.utc),
        datetime(2024, 1, 2, tzinfo=timezone.utc),
    )
    m_complete = ManifestBuilder.build(w_complete, [])

    v2 = TrustEngine.evaluate(m_complete, ["High unexplained residual value"])
    assert v2.verdict == TrustVerdict.DEGRADED
    assert "High unexplained" in v2.blockers[0]
