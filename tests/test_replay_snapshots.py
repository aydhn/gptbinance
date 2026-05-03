from app.replay.models import ReplayConfig, ReplayScope, EventTimeline
from app.replay.snapshots import DummySnapshotLoader
from app.replay.enums import SnapshotFidelity


def test_snapshot_loader():
    loader = DummySnapshotLoader()
    config = ReplayConfig(scope=ReplayScope.TRADE, sources=[])
    timeline = EventTimeline()
    snapshot = loader.load_snapshot(config, timeline)
    assert snapshot.fidelity == SnapshotFidelity.HIGH
    assert snapshot.timestamp is not None
