from app.crossbook.reporting import CrossBookReporter
import logging
from typing import List

from app.replay.models import DecisionPathSnapshot

logger = logging.getLogger(__name__)


class DummyDecisionPathBuilder:
    def build_dummy_path(self) -> List[DecisionPathSnapshot]:
        now = "2024-01-01T00:00:00Z"  # Dummy timestamp is ok as string if model allows it or we import datetime
        from datetime import datetime, timezone

        now = datetime.now(timezone.utc)

        # Cross-book integration: record state in inputs
        reporter = CrossBookReporter()
        crossbook_summary = reporter.generate_summary()
        return [
            DecisionPathSnapshot(
                stage="signal",
                timestamp=now,
                inputs={"price": 100},
                decision={"signal": "buy"},
                evidence_refs=["ref1"],
            ),
            DecisionPathSnapshot(
                stage="risk",
                timestamp=now,
                inputs={"signal": "buy", "crossbook_state": crossbook_summary},
                decision={"approved": True},
                evidence_refs=["ref2"],
            ),
        ]
