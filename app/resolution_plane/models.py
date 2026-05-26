from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from app.resolution_plane.enums import (
    ResolutionClass, TriggerClass, BridgeClass, TransferClass, ContinuityClass,
    RingFenceClass, WriteDownClass, ConversionClass, WindDownClass, PortabilityClass,
    EquivalenceVerdict, TrustVerdict
)

class ResolutionObjectRef(BaseModel):
    id: str

class ResolutionPlaneConfig(BaseModel):
    strict_continuity_checks: bool = True

class ResolutionObject(BaseModel):
    resolution_id: str
    resolution_class: ResolutionClass
    owner: str
    scope: str
    transfer_posture: TransferClass
    continuity_posture: ContinuityClass

class ResolutionRecord(BaseModel):
    id: str
    resolution_id: str
    state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ResolutionTriggerRecord(BaseModel):
    id: str
    trigger_class: TriggerClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class BridgeRecord(BaseModel):
    id: str
    bridge_class: BridgeClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class BridgeSupportRecord(BaseModel):
    id: str
    support_type: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TransferPerimeterRecord(BaseModel):
    id: str
    transfer_class: TransferClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TransferExecutionRecord(BaseModel):
    id: str
    execution_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class GoodEstateRecord(BaseModel):
    id: str
    estate_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class BadEstateRecord(BaseModel):
    id: str
    estate_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class CriticalFunctionRecord(BaseModel):
    id: str
    function_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ServiceContinuityRecord(BaseModel):
    id: str
    continuity_class: ContinuityClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ContinuityDependencyRecord(BaseModel):
    id: str
    dependency_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class RingFenceRecord(BaseModel):
    id: str
    ring_fence_class: RingFenceClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ClientAssetProtectionRecord(BaseModel):
    id: str
    protection_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class WriteDownRecord(BaseModel):
    id: str
    write_down_class: WriteDownClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ConversionRecord(BaseModel):
    id: str
    conversion_class: ConversionClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ClassTreatmentRecord(BaseModel):
    id: str
    treatment_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class NonTransferableRecord(BaseModel):
    id: str
    non_transferable_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class PortabilityRecord(BaseModel):
    id: str
    portability_class: PortabilityClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TemporarySupportRecord(BaseModel):
    id: str
    support_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class WindDownLaneRecord(BaseModel):
    id: str
    wind_down_class: WindDownClass
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class LiquidationFallbackRecord(BaseModel):
    id: str
    fallback_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ResolutionUnwindRecord(BaseModel):
    id: str
    unwind_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class PostResolutionDutyRecord(BaseModel):
    id: str
    duty_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ResidualContinuityGapRecord(BaseModel):
    id: str
    gap_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ResolutionComparisonRecord(BaseModel):
    id: str
    comparison_state: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ResolutionObservationReport(BaseModel):
    id: str
    observations: List[str]

class ResolutionForecastReport(BaseModel):
    id: str
    forecasts: List[str]

class ResolutionDebtRecord(BaseModel):
    id: str
    debt_type: str
    severity: str
    proof_notes: Optional[str] = None

class ResolutionEquivalenceReport(BaseModel):
    id: str
    verdict: EquivalenceVerdict
    blockers: List[str]

class ResolutionDivergenceReport(BaseModel):
    id: str
    divergences: List[str]

class ResolutionTrustVerdict(BaseModel):
    id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    caveats: List[str]

class ResolutionAuditRecord(BaseModel):
    id: str
    action: str
    details: Dict[str, Any]

class ResolutionArtifactManifest(BaseModel):
    id: str
    artifacts: List[str]
