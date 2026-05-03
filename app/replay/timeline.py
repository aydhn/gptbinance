import logging
from typing import List, Dict, Any

from app.replay.models import ReplayConfig, EventTimeline, TimelineEvent
from app.replay.base import TimelineBuilderBase
from app.replay.enums import TimelineEventType
from datetime import datetime, timezone


logger = logging.getLogger(__name__)


class DummyTimelineBuilder(TimelineBuilderBase):
    def build_timeline(
        self, sources: List[Dict[str, Any]], config: ReplayConfig
    ) -> EventTimeline:
        logger.info("Building dummy timeline from sources")
        events = []
        now = datetime.now(timezone.utc)
        for i, src in enumerate(sources):
            events.append(
                TimelineEvent(
                    event_id=f"evt_{i}",
                    timestamp=now,
                    sequence_id=i,
                    event_type=TimelineEventType.SIGNAL,
                    component_ref=src["ref_id"],
                    payload={"mock": "payload"},
                )
            )

        return EventTimeline(
            events=events,
            gaps_detected=False,
            suspicious_overlaps=False,
            missing_refs=[],
            source_coverage=1.0,
        )
