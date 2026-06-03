from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime
from app.resilience_plane.enums import *

class ResilienceObjectRef(BaseModel):
    resilience_id: str

class ResilienceObject(BaseModel):
    resilience_id: str
    resilience_class: ResilienceClass
    owner: str
    scope: str
    shock_posture: str
    recovery_posture: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ResilienceRecord(BaseModel):
    record_id: str
    resilience_id: str
    state: str
    proof_notes: str
    lineage_refs: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ShockClassRecord(BaseModel):
    shock_id: str
    resilience_id: str
    shock_class: ShockClass
    lineage_refs: List[str]

class CompoundShockRecord(BaseModel):
    compound_shock_id: str
    constituent_shocks: List[str]
    is_hidden: bool
    lineage_refs: List[str]

class AbsorptionMarginRecord(BaseModel):
    margin_id: str
    resilience_id: str
    margin_type: str # healthy, thin, exhausted, fake
    lineage_refs: List[str]

class DegradationLaneRecord(BaseModel):
    lane_id: str
    resilience_id: str
    degradation_class: DegradationClass
    lineage_refs: List[str]

class GracefulDegradationRecord(BaseModel):
    graceful_id: str
    resilience_id: str
    is_false_claim: bool
    lineage_refs: List[str]

class ContainmentBoundaryRecord(BaseModel):
    boundary_id: str
    resilience_id: str
    containment_class: ContainmentClass
    lineage_refs: List[str]

class BlastRadiusRecord(BaseModel):
    radius_id: str
    resilience_id: str
    is_bounded: bool
    is_hidden: bool
    lineage_refs: List[str]

class FallbackCapacityRecord(BaseModel):
    fallback_id: str
    resilience_id: str
    fallback_class: FallbackClass
    lineage_refs: List[str]

class SubstitutionPathRecord(BaseModel):
    path_id: str
    resilience_id: str
    is_safe: bool
    lineage_refs: List[str]

class ReserveRecord(BaseModel):
    reserve_id: str
    resilience_id: str
    reserve_class: ReserveClass
    lineage_refs: List[str]

class ReserveConsumptionRecord(BaseModel):
    consumption_id: str
    reserve_id: str
    is_hidden: bool
    lineage_refs: List[str]

class ExhaustionPointRecord(BaseModel):
    exhaustion_id: str
    resilience_id: str
    exhaustion_class: ExhaustionClass
    lineage_refs: List[str]

class RecoveryCapacityRecord(BaseModel):
    recovery_id: str
    resilience_id: str
    recovery_class: RecoveryClass
    lineage_refs: List[str]

class RecoveryLagRecord(BaseModel):
    lag_id: str
    resilience_id: str
    is_acceptable: bool
    is_hidden: bool
    lineage_refs: List[str]

class OperatorLoadRecord(BaseModel):
    load_id: str
    resilience_id: str
    load_class: LoadClass
    lineage_refs: List[str]

class CoordinationLoadRecord(BaseModel):
    coord_id: str
    resilience_id: str
    load_class: LoadClass
    lineage_refs: List[str]

class BeneficiaryImpactSurgeRecord(BaseModel):
    surge_id: str
    resilience_id: str
    is_bounded: bool
    is_hidden: bool
    lineage_refs: List[str]

class HiddenFragilityRecord(BaseModel):
    fragility_id: str
    resilience_id: str
    description: str
    lineage_refs: List[str]

class ResilienceComparisonRecord(BaseModel):
    comparison_id: str
    source_id: str
    target_id: str
    notes: str

class ResilienceDebtRecord(BaseModel):
    debt_id: str
    resilience_id: str
    debt_type: str
    severity: str

class ResilienceReadinessRecord(BaseModel):
    readiness_id: str
    resilience_id: str
    readiness_class: str
    proof_notes: str

class ResilienceTrustVerdict(BaseModel):
    verdict_id: str
    resilience_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ResilienceObservationReport(BaseModel):
    report_id: str
    resilience_id: str
    observations: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ResilienceForecastReport(BaseModel):
    forecast_id: str
    resilience_id: str
    predictions: List[str]
    uncertainty_level: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

class ResilienceArtifactManifest(BaseModel):
    manifest_id: str
    resilience_id: str
    artifacts: List[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
