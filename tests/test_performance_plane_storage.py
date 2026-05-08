from app.performance_plane.repository import PerformanceRepository
from app.performance_plane.manifests import ManifestBuilder
from app.performance_plane.windows import WindowManager
from app.performance_plane.enums import WindowClass
from datetime import datetime, timezone


def test_manifest_storage():
    w = WindowManager.create_window(
        WindowClass.SESSION, datetime(2024, 1, 1, tzinfo=timezone.utc)
    )
    m = ManifestBuilder.build(w, [])

    PerformanceRepository.save_manifest(m)
    loaded = PerformanceRepository.get_manifest(m.manifest_id)

    assert loaded is not None
    assert loaded.manifest_id == m.manifest_id
    assert loaded.hash_signature == m.hash_signature
