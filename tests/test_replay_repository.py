from app.replay.repository import replay_repository
from app.replay.models import (
    ReplayConfig,
    ReplayScope,
    ReplaySourceRef,
    ReplaySourceType,
)


def test_replay_repository_save_and_get():
    sources = [
        ReplaySourceRef(source_type=ReplaySourceType.PAPER_SESSION, ref_id="test1")
    ]
    config = ReplayConfig(scope=ReplayScope.TRADE, sources=sources)

    result = replay_repository.run_and_save(config)

    retrieved = replay_repository.get_run(result.run_id)
    assert retrieved is not None
    assert retrieved.run_id == result.run_id
