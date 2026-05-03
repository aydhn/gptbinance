from app.replay.counterfactuals import DummyCounterfactualEngine
from app.replay.models import (
    CounterfactualSpec,
    ReplayConfig,
    ReplayScope,
    EventTimeline,
    PointInTimeSnapshot,
)
from app.replay.enums import CounterfactualType, SnapshotFidelity
from datetime import datetime, timezone


def test_counterfactual_engine():
    engine = DummyCounterfactualEngine()
    specs = [
        CounterfactualSpec(
            type=CounterfactualType.ML_DISABLED, description="disable ML"
        )
    ]
    config = ReplayConfig(scope=ReplayScope.TRADE, sources=[])
    timeline = EventTimeline()
    snapshot = PointInTimeSnapshot(
        timestamp=datetime.now(timezone.utc), fidelity=SnapshotFidelity.HIGH
    )

    results = engine.run_counterfactuals(specs, config, timeline, snapshot)
    assert len(results) == 1
    assert results[0].historical_outcome["status"] == "executed"
    assert results[0].counterfactual_outcome["status"] == "blocked"
