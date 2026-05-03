from app.replay.diff import DummyDiffEngine
from app.replay.models import DecisionPathSnapshot
from app.replay.enums import DiffSeverity
from datetime import datetime, timezone


def test_diff_engine():
    engine = DummyDiffEngine()
    now = datetime.now(timezone.utc)
    path1 = [DecisionPathSnapshot(stage="s1", timestamp=now, inputs={}, decision={})]
    path2 = []

    diffs = engine.compute_diff(path1, path2)
    assert len(diffs) == 1
    assert diffs[0].severity == DiffSeverity.CRITICAL
    assert diffs[0].original_value == 1
    assert diffs[0].replayed_value == 0
