from app.replay.storage import DummyReplayStorage
from app.replay.models import (
    DecisionReplayResult,
    ReplayConfig,
    ReplayScope,
    EventTimeline,
    PointInTimeSnapshot,
    ReproducibilityVerdict,
    ReplayabilityScore,
)
from app.replay.enums import SnapshotFidelity, ReproducibilityStatus, ReplayVerdict
from datetime import datetime, timezone


def test_replay_storage():
    storage = DummyReplayStorage()
    now = datetime.now(timezone.utc)
    config = ReplayConfig(scope=ReplayScope.TRADE, sources=[])
    res = DecisionReplayResult(
        run_id="r1",
        config=config,
        snapshot=PointInTimeSnapshot(timestamp=now, fidelity=SnapshotFidelity.HIGH),
        timeline=EventTimeline(),
        decision_path=[],
        diffs=[],
        reproducibility=ReproducibilityVerdict(
            status=ReproducibilityStatus.EXACT_MATCH, confidence=1.0, reasoning=""
        ),
        replayability_score=ReplayabilityScore(
            source_completeness=1,
            lineage_completeness=1,
            snapshot_fidelity=1,
            schema_compatibility=1,
            decision_path_coverage=1,
            diff_magnitude=0,
            deterministic_reproducibility=1,
            forensic_evidence_completeness=1,
            overall_score=1,
            verdict=ReplayVerdict.TRUSTED,
        ),
    )
    storage.save_run(res)
    assert storage.get_run("r1") is not None
    assert storage.get_run("r2") is None
    assert "r1" in storage.list_runs()
