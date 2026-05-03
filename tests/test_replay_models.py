from app.replay.models import (
    ReplayConfig,
    ReplayScope,
    ReplaySourceRef,
    ReplaySourceType,
)


def test_replay_config_creation():
    sources = [
        ReplaySourceRef(source_type=ReplaySourceType.PAPER_SESSION, ref_id="test1")
    ]
    config = ReplayConfig(scope=ReplayScope.TRADE, sources=sources)
    assert config.scope == ReplayScope.TRADE
    assert len(config.sources) == 1
    assert config.sources[0].ref_id == "test1"
