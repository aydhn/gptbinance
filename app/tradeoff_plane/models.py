from datetime import datetime
from typing import Dict, List, Optional, Any, Set
from pydantic import BaseModel, Field
from uuid import UUID

from .enums import (
    TradeoffClass, ObjectiveClass, PriorityClass, UtilityClass,
    BurdenClass, SacrificeClass, ExternalityClass, DominanceClass,
    FrontierClass, FeasibilityClass, EquivalenceVerdict, TrustVerdict
)

class TradeoffPlaneConfig(BaseModel):
    strict_dominance: bool = True
    require_explicit_sacrifices: bool = True
    enforce_non_compensable_boundaries: bool = True
    track_burden_shifts: bool = True

class TradeoffObjectRef(BaseModel):
    tradeoff_id: str
    version: str
    hash: Optional[str] = None

class ObjectiveRecord(BaseModel):
    objective_id: str
    name: str
    description: str
    objective_class: ObjectiveClass
    scope: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ObjectiveSetRecord(BaseModel):
    set_id: str
    objectives: List[ObjectiveRecord]
    completeness_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class PreferenceRecord(BaseModel):
    preference_id: str
    description: str
    is_temporary: bool = False
    conditional_context: Optional[str] = None
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class PriorityRecord(BaseModel):
    priority_id: str
    priority_class: PriorityClass
    rationale: str
    change_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class UtilityRecord(BaseModel):
    utility_id: str
    utility_class: UtilityClass
    semantics: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class BenefitRecord(BaseModel):
    benefit_id: str
    description: str
    is_direct: bool
    is_local: bool
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class BurdenRecord(BaseModel):
    burden_id: str
    burden_class: BurdenClass
    description: str
    is_transferred: bool = False
    is_hidden: bool = False
    visibility_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class ExternalityRecord(BaseModel):
    externality_id: str
    externality_class: ExternalityClass
    description: str
    target_scope: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class OpportunityCostRecord(BaseModel):
    cost_id: str
    description: str
    foregone_value_type: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class SacrificeRecord(BaseModel):
    sacrifice_id: str
    sacrifice_class: SacrificeClass
    description: str
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class NonCompensableConstraintRecord(BaseModel):
    constraint_id: str
    description: str
    boundary_type: str
    violation_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class FeasibilityRecord(BaseModel):
    feasibility_id: str
    feasibility_class: FeasibilityClass
    description: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class DominanceRecord(BaseModel):
    dominance_id: str
    dominance_class: DominanceClass
    compared_options: List[str]
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class FrontierRecord(BaseModel):
    frontier_id: str
    frontier_class: FrontierClass
    description: str
    caveats: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class MarginalChangeRecord(BaseModel):
    marginal_id: str
    description: str
    gain: str
    burden_increase: str
    is_negative_trade: bool = False
    proof_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TradeoffComparisonRecord(BaseModel):
    comparison_id: str
    description: str
    options: List[str]
    comparison_type: str
    lineage_refs: List[str] = Field(default_factory=list)

class TradeoffJustificationRecord(BaseModel):
    justification_id: str
    description: str
    is_emergency: bool = False
    evidence_backed: bool = True
    burden_explicit: bool = True
    sufficiency_notes: Optional[str] = None
    lineage_refs: List[str] = Field(default_factory=list)

class TradeoffObservationReport(BaseModel):
    report_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    observations: List[str]

class TradeoffForecastReport(BaseModel):
    forecast_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    burden_accumulation: str
    resilience_erosion: str
    cost_externalization: str
    uncertainty_class: str

class TradeoffDebtRecord(BaseModel):
    debt_id: str
    debt_type: str
    description: str
    severity: str

class TradeoffEquivalenceReport(BaseModel):
    report_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    divergence_sources: List[str]

class TradeoffDivergenceReport(BaseModel):
    report_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    divergence_type: str
    description: str
    severity: str

class TradeoffTrustVerdict(BaseModel):
    verdict_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tradeoff_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]

class TradeoffAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tradeoff_id: str
    action: str
    details: str

class TradeoffArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tradeoff_id: str
    components: Dict[str, str]

class TradeoffObject(BaseModel):
    tradeoff_id: str
    tradeoff_class: TradeoffClass
    owner: str
    scope: str
    objective_set: ObjectiveSetRecord
    burden_posture: List[BurdenRecord]
    sacrifices: List[SacrificeRecord] = Field(default_factory=list)
    state: str = "active"
    created_at: datetime = Field(default_factory=datetime.utcnow)
