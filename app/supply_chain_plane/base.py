from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from app.supply_chain_plane.models import (
    ComponentDefinition,
    ComponentRef,
    SourceOriginRecord,
    DependencyTree,
    BuildProvenanceRecord,
    SbomRecord,
    SignatureRecord,
    LicenseRecord,
    RuntimeLineageRecord,
    SupplyChainTrustVerdict,
    DriftRecord,
)


class ComponentRegistryBase(ABC):
    @abstractmethod
    def register_component(self, component: ComponentDefinition) -> None:
        pass

    @abstractmethod
    def get_component(self, component_id: str) -> Optional[ComponentDefinition]:
        pass


class ProvenanceEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_provenance(self, component_ref: ComponentRef) -> BuildProvenanceRecord:
        pass


class DriftEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_drift(
        self, component_ref: ComponentRef, environment: str
    ) -> List[DriftRecord]:
        pass


class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate_trust(self, component_ref: ComponentRef) -> SupplyChainTrustVerdict:
        pass
