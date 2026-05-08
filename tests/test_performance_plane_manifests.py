from datetime import datetime, timezone
from app.performance_plane.manifests import ManifestBuilder
from app.performance_plane.models import PerformanceManifestEntry
from app.performance_plane.windows import WindowManager
from app.performance_plane.enums import WindowClass


def test_manifest_building():
    w = WindowManager.create_window(
        WindowClass.SESSION, datetime(2024, 1, 1, tzinfo=timezone.utc)
    )
    e1 = PerformanceManifestEntry(
        entry_id="1", entry_type="return", reference_id="ret_123"
    )
    m = ManifestBuilder.build(w, [e1])

    assert m.hash_signature is not None
    assert len(m.entries) == 1
