from typing import Dict, List, Optional
from app.strategy_plane.models import (
    StrategyDefinition,
    StrategyHypothesis,
    StrategyThesis,
    StrategyLifecycleRecord,
    StrategyManifest,
    StrategyFitReport,
    StrategyDecayReport,
    StrategyOverlapReport,
    StrategyEquivalenceReport,
    StrategyTrustVerdict,
)


class StrategyPlaneStorage:
    def __init__(self):
        self.definitions: Dict[str, StrategyDefinition] = {}
        self.hypotheses: Dict[str, StrategyHypothesis] = {}
        self.theses: Dict[str, StrategyThesis] = {}
        self.lifecycle_records: Dict[str, List[StrategyLifecycleRecord]] = {}
        self.manifests: Dict[str, StrategyManifest] = {}
        self.fit_reports: Dict[str, StrategyFitReport] = {}
        self.decay_reports: Dict[str, StrategyDecayReport] = {}
        self.overlap_reports: Dict[str, StrategyOverlapReport] = {}
        self.equivalence_reports: Dict[str, StrategyEquivalenceReport] = {}
        self.trust_verdicts: Dict[str, StrategyTrustVerdict] = {}

    def save_definition(self, definition: StrategyDefinition):
        self.definitions[definition.strategy_id] = definition

    def save_hypothesis(self, hypothesis: StrategyHypothesis):
        self.hypotheses[hypothesis.hypothesis_id] = hypothesis

    def save_thesis(self, thesis: StrategyThesis):
        self.theses[thesis.thesis_id] = thesis

    def save_manifest(self, manifest: StrategyManifest):
        self.manifests[manifest.strategy_id] = manifest

    def save_lifecycle_record(self, record: StrategyLifecycleRecord):
        if record.strategy_id not in self.lifecycle_records:
            self.lifecycle_records[record.strategy_id] = []
        self.lifecycle_records[record.strategy_id].append(record)
