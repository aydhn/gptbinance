from abc import ABC, abstractmethod
from app.supply_chain.models import (
    SourceSnapshot,
    DependencySnapshot,
    BuildOutputManifest,
    AttestationRecord,
)


class SourceSnapshotterBase(ABC):
    @abstractmethod
    def create_snapshot(self, path: str) -> SourceSnapshot:
        pass


class DependencyInventoryBase(ABC):
    @abstractmethod
    def create_snapshot(self, path: str) -> DependencySnapshot:
        pass


class BuildProvenanceBuilderBase(ABC):
    @abstractmethod
    def build_manifest(
        self, source_id: str, deps_id: str, env: dict, outputs: list
    ) -> BuildOutputManifest:
        pass


class AttestationVerifierBase(ABC):
    @abstractmethod
    def verify(self, record: AttestationRecord) -> bool:
        pass
