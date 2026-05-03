from app.replay.engine import DefaultReplayEngine
from app.replay.models import (
    ReplayConfig,
    ReplayScope,
    ReplaySourceRef,
    ReplaySourceType,
)


def test_replay_engine_run():
    engine = DefaultReplayEngine()
    sources = [
        ReplaySourceRef(source_type=ReplaySourceType.PAPER_SESSION, ref_id="test1")
    ]
    config = ReplayConfig(scope=ReplayScope.TRADE, sources=sources)

    result = engine.run_replay(config)
    assert result.run_id is not None
    # the dummy diff engine returns empty list if paths are identical
    assert result.reproducibility.status.value == "exact_match"
    assert len(result.diffs) == 0
