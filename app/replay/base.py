import abc
from typing import Dict, Any, List

from app.replay.models import (
    ReplayConfig,
    PointInTimeSnapshot,
    EventTimeline,
    DecisionPathSnapshot,
    ReplayDiff,
    ForensicBundle,
)


class ReplaySourceResolverBase(abc.ABC):
    @abc.abstractmethod
    def resolve_sources(self, config: ReplayConfig) -> List[Dict[str, Any]]:
        pass


class TimelineBuilderBase(abc.ABC):
    @abc.abstractmethod
    def build_timeline(
        self, sources: List[Dict[str, Any]], config: ReplayConfig
    ) -> EventTimeline:
        pass


class SnapshotLoaderBase(abc.ABC):
    @abc.abstractmethod
    def load_snapshot(
        self, config: ReplayConfig, timeline: EventTimeline
    ) -> PointInTimeSnapshot:
        pass


class DiffEngineBase(abc.ABC):
    @abc.abstractmethod
    def compute_diff(
        self,
        original_path: List[DecisionPathSnapshot],
        replayed_path: List[DecisionPathSnapshot],
    ) -> List[ReplayDiff]:
        pass


class ForensicCollectorBase(abc.ABC):
    @abc.abstractmethod
    def collect_forensics(
        self,
        timeline: EventTimeline,
        decision_path: List[DecisionPathSnapshot],
        diffs: List[ReplayDiff],
        config: ReplayConfig,
    ) -> ForensicBundle:
        pass


class ReplayEngineBase(abc.ABC):
    @abc.abstractmethod
    def run_replay(self, config: ReplayConfig) -> Any:
        pass
