import pytest
import os
from datetime import datetime, timezone
from app.execution.paper.storage import PaperStorage
from app.execution.paper.models import (
    PaperSessionConfig,
    PaperRuntimeSummary,
    PaperArtifactManifest,
    SessionStopReason,
    PaperEquitySnapshot,
    SessionHealthSnapshot,
    SessionHealth,
)


@pytest.fixture
def storage():
    db_path = "test_paper_storage.db"
    if os.path.exists(db_path):
        os.remove(db_path)
    store = PaperStorage(db_path)
    yield store
    if os.path.exists(db_path):
        os.remove(db_path)


def test_manifest_storage(storage):
    config = PaperSessionConfig(symbols=["BTCUSDT"], stream_types=["kline"])
    summary = PaperRuntimeSummary(
        run_id="run1",
        start_time=datetime.now(timezone.utc),
        total_orders=10,
        total_fills=5,
        final_equity=10500.0,
        max_drawdown_pct=0.05,
        risk_veto_count=2,
        stop_reason=SessionStopReason.MANUAL,
    )
    manifest = PaperArtifactManifest(run_id="run1", config=config, summary=summary)

    storage.save_manifest(manifest)

    loaded = storage.get_manifest("run1")
    assert loaded is not None
    assert loaded.run_id == "run1"
    assert loaded.config.symbols == ["BTCUSDT"]
    assert loaded.summary.total_orders == 10


def test_snapshot_storage(storage):
    equity = PaperEquitySnapshot(equity=10500.0, drawdown_pct=0.01)
    health = SessionHealthSnapshot(
        health=SessionHealth.HEALTHY,
        uptime_seconds=10.0,
        stream_freshness_ms=50.0,
        feature_lag_ms=10.0,
        error_count=0,
        open_positions=1,
        current_drawdown_pct=0.01,
    )

    storage.save_snapshot("run1", equity, health)

    snaps = storage.get_snapshots("run1")
    assert len(snaps) == 1
    assert snaps[0]["equity"] == 10500.0
    assert snaps[0]["health"] == "healthy"
