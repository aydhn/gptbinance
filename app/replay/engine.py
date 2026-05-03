import logging
import uuid

from app.replay.models import ReplayConfig, DecisionReplayResult, ReproducibilityVerdict
from app.replay.enums import ReproducibilityStatus
from app.replay.base import ReplayEngineBase
from app.replay.sources import DummyReplaySourceResolver
from app.replay.timeline import DummyTimelineBuilder
from app.replay.snapshots import DummySnapshotLoader
from app.replay.decision_path import DummyDecisionPathBuilder
from app.replay.diff import DummyDiffEngine
from app.replay.counterfactuals import DummyCounterfactualEngine
from app.replay.forensics import DummyForensicCollector
from app.replay.scoring import DummyScorer


logger = logging.getLogger(__name__)


class DefaultReplayEngine(ReplayEngineBase):
    def __init__(self):
        self.source_resolver = DummyReplaySourceResolver()
        self.timeline_builder = DummyTimelineBuilder()
        self.snapshot_loader = DummySnapshotLoader()
        self.path_builder = DummyDecisionPathBuilder()
        self.diff_engine = DummyDiffEngine()
        self.counterfactual_engine = DummyCounterfactualEngine()
        self.forensic_collector = DummyForensicCollector()
        self.scorer = DummyScorer()

    def run_replay(self, config: ReplayConfig) -> DecisionReplayResult:
        logger.info(f"Starting replay run for scope: {config.scope}")

        run_id = f"replay_{uuid.uuid4().hex[:8]}"

        # 1. Resolve sources
        sources = self.source_resolver.resolve_sources(config)

        # 2. Build timeline
        timeline = self.timeline_builder.build_timeline(sources, config)

        # 3. Load snapshot
        snapshot = self.snapshot_loader.load_snapshot(config, timeline)

        # 4. Reconstruct decision path (dummy)
        decision_path = self.path_builder.build_dummy_path()
        original_path = decision_path  # Assuming perfectly identical for dummy

        # 5. Compute diff
        diffs = self.diff_engine.compute_diff(original_path, decision_path)

        # 6. Counterfactuals
        counterfactual_results = self.counterfactual_engine.run_counterfactuals(
            config.counterfactual_specs, config, timeline, snapshot
        )

        # 7. Forensics
        forensic_bundle = None
        if config.include_forensics:
            forensic_bundle = self.forensic_collector.collect_forensics(
                timeline, decision_path, diffs, config
            )

        # 8. Score
        score = self.scorer.score()

        reproducibility = ReproducibilityVerdict(
            status=ReproducibilityStatus.EXACT_MATCH
            if not diffs
            else ReproducibilityStatus.CRITICAL_MISMATCH,
            confidence=1.0,
            reasoning="Dummy run",
        )

        return DecisionReplayResult(
            run_id=run_id,
            config=config,
            snapshot=snapshot,
            timeline=timeline,
            decision_path=decision_path,
            diffs=diffs,
            reproducibility=reproducibility,
            counterfactual_results=counterfactual_results,
            forensic_bundle=forensic_bundle,
            replayability_score=score,
        )
