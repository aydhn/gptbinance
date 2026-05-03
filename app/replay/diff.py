import logging
from typing import List

from app.replay.models import DecisionPathSnapshot, ReplayDiff
from app.replay.base import DiffEngineBase
from app.replay.enums import DiffSeverity

logger = logging.getLogger(__name__)


class DummyDiffEngine(DiffEngineBase):
    def compute_diff(
        self,
        original_path: List[DecisionPathSnapshot],
        replayed_path: List[DecisionPathSnapshot],
    ) -> List[ReplayDiff]:
        logger.info("Computing dummy diffs")
        diffs = []
        # Simulate a fake diff if requested for testing
        # or actually compare. Since we just returned identical paths in engine, length is same.
        # Let's force a benign diff so tests can check it, or an exact match.
        if len(original_path) != len(replayed_path):
            diffs.append(
                ReplayDiff(
                    stage="overall",
                    original_value=len(original_path),
                    replayed_value=len(replayed_path),
                    severity=DiffSeverity.CRITICAL,
                    description="Path length mismatch",
                )
            )
        return diffs
