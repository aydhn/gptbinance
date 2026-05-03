import logging
from datetime import datetime, timezone

from app.replay.models import ReplayConfig, EventTimeline, PointInTimeSnapshot
from app.replay.enums import SnapshotFidelity
from app.replay.base import SnapshotLoaderBase


logger = logging.getLogger(__name__)


class DummySnapshotLoader(SnapshotLoaderBase):
    def load_snapshot(
        self, config: ReplayConfig, timeline: EventTimeline
    ) -> PointInTimeSnapshot:
        logger.info("Loading dummy snapshot")
        return PointInTimeSnapshot(
            timestamp=datetime.now(timezone.utc), fidelity=SnapshotFidelity.HIGH
        )
