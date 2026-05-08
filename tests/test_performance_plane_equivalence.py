from datetime import datetime, timezone
from app.performance_plane.equivalence import EquivalenceChecker
from app.performance_plane.enums import WindowClass, EquivalenceVerdict
from app.performance_plane.windows import WindowManager
from app.performance_plane.manifests import ManifestBuilder
from app.performance_plane.models import PerformanceManifestEntry


def test_replay_paper_runtime_live_equivalence():
    start_t = datetime(2024, 1, 1, tzinfo=timezone.utc)
    end_t = datetime(2024, 1, 2, tzinfo=timezone.utc)
    w = WindowManager.create_window(WindowClass.SESSION, start_t, end_t)

    e1 = PerformanceManifestEntry(entry_id="1", entry_type="return", reference_id="r1")
    e2 = PerformanceManifestEntry(entry_id="2", entry_type="return", reference_id="r2")

    m_live = ManifestBuilder.build(w, [e1])
    m_replay = ManifestBuilder.build(w, [e2])  # Diff ref -> diff hash -> diff

    report = EquivalenceChecker.check(m_live, m_replay)
    assert report.verdict == EquivalenceVerdict.MINOR_DIVERGENCE
    assert "signatures differ" in report.divergence_sources[0]
