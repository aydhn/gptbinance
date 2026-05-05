from app.replay.models import (
    ReplayConfig,
    ReplayScope,
    ReplaySourceRef,
    ReplaySourceType,
)
from app.replay.timeline import DummyTimelineBuilder


def test_timeline_builder():
    builder = DummyTimelineBuilder()
    config = ReplayConfig(
        scope=ReplayScope.TRADE,
        sources=[
            ReplaySourceRef(source_type=ReplaySourceType.PAPER_SESSION, ref_id="s1")
        ],
    )
    sources = [{"ref_id": "s1"}]
    timeline = builder.build_timeline(sources, config)
    assert len(timeline.events) == 1
    assert timeline.events[0].component_ref == "s1"
    assert not timeline.gaps_detected
