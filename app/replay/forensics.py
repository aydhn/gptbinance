import logging
from typing import List

from app.replay.models import (
    EventTimeline,
    DecisionPathSnapshot,
    ReplayDiff,
    ReplayConfig,
    ForensicBundle,
)
from app.replay.base import ForensicCollectorBase

logger = logging.getLogger(__name__)


class DummyForensicCollector(ForensicCollectorBase):
    def collect_forensics(
        self,
        timeline: EventTimeline,
        decision_path: List[DecisionPathSnapshot],
        diffs: List[ReplayDiff],
        config: ReplayConfig,
    ) -> ForensicBundle:
        logger.info("Collecting dummy forensics")
        return ForensicBundle(
            incident_ref=None,
            timeline=timeline,
            decision_path=decision_path,
            findings=[],
            likely_root_causes=["None identified in dummy run"],
            next_investigation_steps=["Check logs"],
        )
