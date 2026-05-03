import pytest
from app.replay.sources import DummyReplaySourceResolver
from app.replay.models import (
    ReplayConfig,
    ReplayScope,
    ReplaySourceRef,
    ReplaySourceType,
)
from app.replay.exceptions import MissingReplaySource


def test_source_resolver():
    resolver = DummyReplaySourceResolver()

    with pytest.raises(MissingReplaySource):
        resolver.resolve_sources(ReplayConfig(scope=ReplayScope.TRADE, sources=[]))

    config = ReplayConfig(
        scope=ReplayScope.TRADE,
        sources=[
            ReplaySourceRef(source_type=ReplaySourceType.PAPER_SESSION, ref_id="abc")
        ],
    )
    resolved = resolver.resolve_sources(config)
    assert len(resolved) == 1
    assert resolved[0]["ref_id"] == "abc"
