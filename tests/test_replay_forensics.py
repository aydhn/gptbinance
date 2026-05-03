from app.replay.forensics import DummyForensicCollector
from app.replay.models import EventTimeline, ReplayConfig, ReplayScope


def test_forensic_collector():
    collector = DummyForensicCollector()
    timeline = EventTimeline()
    config = ReplayConfig(scope=ReplayScope.INCIDENT, sources=[])

    bundle = collector.collect_forensics(timeline, [], [], config)
    assert bundle.incident_ref is None
    assert "Check logs" in bundle.next_investigation_steps
