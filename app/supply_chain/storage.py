from typing import Dict, Any, Optional
from app.supply_chain.models import (
    SourceSnapshot,
    DependencySnapshot,
    BuildOutputManifest,
    AttestationRecord,
    ReproducibilityRun,
    RuntimeEquivalenceReport,
)


class SupplyChainStorage:
    def __init__(self):
        self.sources: Dict[str, SourceSnapshot] = {}
        self.deps: Dict[str, DependencySnapshot] = {}
        self.builds: Dict[str, BuildOutputManifest] = {}
        self.attestations: Dict[str, list[AttestationRecord]] = {}
        self.reproducibility: Dict[str, ReproducibilityRun] = {}
        self.runtime_eq: Dict[str, RuntimeEquivalenceReport] = {}

    def save_source(self, s: SourceSnapshot):
        self.sources[s.id] = s

    def get_source(self, id: str) -> Optional[SourceSnapshot]:
        return self.sources.get(id)

    def save_dependency(self, d: DependencySnapshot):
        self.deps[d.id] = d

    def get_dependency(self, id: str) -> Optional[DependencySnapshot]:
        return self.deps.get(id)

    def save_build(self, b: BuildOutputManifest):
        self.builds[b.id] = b

    def get_build(self, id: str) -> Optional[BuildOutputManifest]:
        return self.builds.get(id)

    def save_attestation(self, a: AttestationRecord):
        if a.build_id not in self.attestations:
            self.attestations[a.build_id] = []
        self.attestations[a.build_id].append(a)

    def get_attestations(self, build_id: str) -> list[AttestationRecord]:
        return self.attestations.get(build_id, [])

    def save_reproducibility(self, r: ReproducibilityRun):
        self.reproducibility[r.id] = r

    def get_reproducibility(self, id: str) -> Optional[ReproducibilityRun]:
        return self.reproducibility.get(id)

    def save_runtime_eq(self, r: RuntimeEquivalenceReport):
        self.runtime_eq[r.id] = r

    def get_runtime_eq(self, id: str) -> Optional[RuntimeEquivalenceReport]:
        return self.runtime_eq.get(id)
