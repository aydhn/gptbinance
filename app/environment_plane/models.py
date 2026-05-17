from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timezone
from app.environment_plane.enums import (
    EnvironmentClass, TopologyClass, BoundaryClass, ParityClass,
    DivergenceClass, PromotionClass, IsolationClass, TenancyClass,
    ContaminationClass, ReadinessClass, EquivalenceVerdict, TrustVerdict
)

class EnvironmentObjectRef(BaseModel):
    environment_id: str
    version: str

class EnvironmentRecord(BaseModel):
    id: str
    environment_class: EnvironmentClass
    owner: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    description: str

class EnvironmentTopologyRecord(BaseModel):
    topology_class: TopologyClass
    proof_notes: str

class EnvironmentBoundaryRecord(BaseModel):
    boundary_class: BoundaryClass
    ambiguity_warnings: str

class EnvironmentCapabilityRecord(BaseModel):
    capabilities: List[str]
    caveats: str

class EnvironmentLimitationRecord(BaseModel):
    limitations: List[str]
    burden_notes: str

class ParityRecord(BaseModel):
    parity_class: ParityClass
    sufficiency_notes: str

class IntendedDivergenceRecord(BaseModel):
    divergence_class: DivergenceClass
    justification_notes: str

class DriftRecord(BaseModel):
    severity: str
    description: str

class PromotionPathRecord(BaseModel):
    promotion_class: PromotionClass
    proof_notes: str

class PromotionGateRecord(BaseModel):
    gate_name: str
    passed: bool
    lineage_refs: str

class IsolationRecord(BaseModel):
    isolation_class: IsolationClass
    proof_notes: str

class TenancyRecord(BaseModel):
    tenancy_class: TenancyClass
    reuse_warnings: str

class SecretScopeRecord(BaseModel):
    scope_description: str
    proof_notes: str

class DataScopeRecord(BaseModel):
    scope_description: str
    bleed_warnings: str

class NetworkScopeRecord(BaseModel):
    scope_description: str
    mismatch_cautions: str

class EnvironmentSeedRecord(BaseModel):
    seed_provenance: str
    stale_warnings: str

class EnvironmentResetRecord(BaseModel):
    reset_type: str
    drift_notes: str

class EnvironmentObservationRecord(BaseModel):
    observation_type: str
    sufficiency_notes: str

class EnvironmentReadinessReport(BaseModel):
    readiness_class: ReadinessClass
    proof_notes: str

class EnvironmentContaminationRecord(BaseModel):
    contamination_class: ContaminationClass
    severity: str
    blast_radius: str

class EnvironmentRotRecord(BaseModel):
    rot_description: str
    severity: str

class EnvironmentEquivalenceReport(BaseModel):
    verdict: EquivalenceVerdict
    proof_notes: str

class EnvironmentDivergenceReport(BaseModel):
    severity: str
    blast_radius: str

class EnvironmentTrustVerdict(BaseModel):
    verdict: TrustVerdict
    breakdown: Dict[str, str]

class EnvironmentAuditRecord(BaseModel):
    action: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    user: str

class EnvironmentArtifactManifest(BaseModel):
    artifact_hash: str
    lineage_refs: str

class EnvironmentObject(BaseModel):
    environment_id: str
    record: EnvironmentRecord
    topology: Optional[EnvironmentTopologyRecord] = None
    boundaries: List[EnvironmentBoundaryRecord] = []
    capabilities: Optional[EnvironmentCapabilityRecord] = None
    limitations: Optional[EnvironmentLimitationRecord] = None
    parity: Optional[ParityRecord] = None
    intended_divergence: Optional[IntendedDivergenceRecord] = None
    drifts: List[DriftRecord] = []
    promotion_paths: List[PromotionPathRecord] = []
    gates: List[PromotionGateRecord] = []
    isolations: List[IsolationRecord] = []
    tenancy: Optional[TenancyRecord] = None
    secrets: Optional[SecretScopeRecord] = None
    data_scope: Optional[DataScopeRecord] = None
    network_scope: Optional[NetworkScopeRecord] = None
    seeds: List[EnvironmentSeedRecord] = []
    resets: List[EnvironmentResetRecord] = []
    observations: List[EnvironmentObservationRecord] = []
    readiness: Optional[EnvironmentReadinessReport] = None
    contaminations: List[EnvironmentContaminationRecord] = []
    rot_records: List[EnvironmentRotRecord] = []
    trust_verdict: Optional[EnvironmentTrustVerdict] = None

class EnvironmentPlaneConfig(BaseModel):
    enforce_strict_isolation: bool = True
    block_on_contamination: bool = True
