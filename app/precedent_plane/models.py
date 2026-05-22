from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.precedent_plane.enums import *

class PrecedentObjectRef(BaseModel):
    precedent_id: str
    version: int

class RationaleRecord(BaseModel):
    rationale_id: str
    precedent_id: str
    rationale_class: RationaleClass
    description: str
    caveats: str
    lineage_refs: List[str]

class ControllingFactorRecord(BaseModel):
    factor_id: str
    precedent_id: str
    factor_class: FactorClass
    description: str
    ambiguity_notes: str
    lineage_refs: List[str]

class HoldingRecord(BaseModel):
    holding_id: str
    precedent_id: str
    holding_class: HoldingClass
    description: str
    proof_notes: str
    lineage_refs: List[str]
    rationales: List[RationaleRecord] = []
    controlling_factors: List[ControllingFactorRecord] = []

class CaseRecord(BaseModel):
    case_id: str
    precedent_id: str
    case_class: CaseClass
    description: str
    proof_notes: str
    lineage_refs: List[str]
    holdings: List[HoldingRecord] = []

class PrecedentObject(BaseModel):
    precedent_id: str
    precedent_class: PrecedentClass
    owner: str
    scope: str
    authority_posture: AuthorityClass
    applicability_posture: ApplicabilityClass
    cases: List[CaseRecord] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    version: int = 1

class ApplicabilityRecord(BaseModel):
    precedent_id: str
    target_id: str
    applicability_class: ApplicabilityClass
    proof_notes: str
    lineage_refs: List[str]

class BindingAuthorityRecord(BaseModel):
    precedent_id: str
    authority_class: AuthorityClass
    proof_notes: str

class PersuasiveAuthorityRecord(BaseModel):
    precedent_id: str
    authority_class: AuthorityClass
    caveats: str

class AnalogyRecord(BaseModel):
    analogy_id: str
    source_precedent_id: str
    target_case_id: str
    analogy_class: AnalogyClass
    insufficiency_notes: str
    lineage_refs: List[str]

class DistinctionRecord(BaseModel):
    distinction_id: str
    source_precedent_id: str
    target_case_id: str
    distinction_class: DistinctionClass
    key_difference_notes: str
    lineage_refs: List[str]

class CarveOutRecord(BaseModel):
    carve_out_id: str
    precedent_id: str
    carve_out_class: CarveoutClass
    inflation_warnings: str
    lineage_refs: List[str]

class ExceptionLineRecord(BaseModel):
    exception_id: str
    precedent_id: str
    exception_class: ExceptionClass
    proof_notes: str
    lineage_refs: List[str]

class ConflictRecord(BaseModel):
    conflict_id: str
    precedent_id_a: str
    precedent_id_b: str
    conflict_class: ConflictClass
    proof_notes: str
    resolved: bool = False

class HierarchyRecord(BaseModel):
    hierarchy_id: str
    dominant_precedent_id: str
    subordinate_precedent_id: str
    hierarchy_class: HierarchyClass
    proof_notes: str

class OverrideRecord(BaseModel):
    override_id: str
    precedent_id: str
    target_id: str
    override_type: str
    abuse_notes: str
    lineage_refs: List[str]

class OverruleRecord(BaseModel):
    overrule_id: str
    overruling_precedent_id: str
    overruled_precedent_id: str
    overrule_type: str
    caveats: str
    lineage_refs: List[str]

class SupersessionRecord(BaseModel):
    supersession_id: str
    superseding_id: str
    superseded_id: str
    scope_notes: str
    lineage_refs: List[str]

class ConsistencyRecord(BaseModel):
    record_id: str
    case_ids: List[str]
    consistency_class: ConsistencyClass
    convergence_notes: str
    lineage_refs: List[str]

class PrecedentComparisonRecord(BaseModel):
    comparison_id: str
    precedent_a: str
    precedent_b: str
    details: str
    lineage_refs: List[str]

class PrecedentForecastReport(BaseModel):
    conflict_growth: str
    exception_inflation: str
    carveout_sprawl: str
    analogy_misuse: str
    consistency_erosion: str
    uncertainty_classes: List[str]

class PrecedentDebtRecord(BaseModel):
    debt_id: str
    cherry_picked_debt: float
    rationale_loss_debt: float
    unresolved_conflict_debt: float
    exception_inflation_debt: float
    silent_override_debt: float
    severity: str

class PrecedentEquivalenceReport(BaseModel):
    precedent_id: str
    replay_hash: str
    paper_hash: str
    probation_hash: str
    live_hash: str
    verdict: PrecedentEquivalenceVerdict
    is_equivalent: bool
    proof_notes: str

class PrecedentDivergenceReport(BaseModel):
    precedent_id: str
    holding_divergence: bool
    rationale_divergence: bool
    applicability_divergence: bool
    severity: str

class PrecedentTrustVerdictReport(BaseModel):
    precedent_id: str
    verdict: PrecedentTrustVerdict
    factors: Dict[str, str]
    breakdown: str

class PrecedentAuditRecord(BaseModel):
    audit_id: str
    action: str
    actor: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class PrecedentArtifactManifest(BaseModel):
    manifest_id: str
    precedent_refs: List[str]
    hash: str

class PrecedentObservationReport(BaseModel):
    report_id: str
    details: str
