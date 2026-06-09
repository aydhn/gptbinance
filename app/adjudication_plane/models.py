from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime
from .enums import *

class AdjudicationPlaneConfig(BaseModel):
    require_dispositive_proof: bool = True
    enforce_panel_independence: bool = True
    prevent_predetermined_outcome: bool = True

class AdjudicationObject(BaseModel):
    adjudication_id: str
    class_type: AdjudicationClass
    owner: str
    scope: str
    determination_posture: str
    disposition_posture: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class AdjudicationRecord(BaseModel):
    adjudication_id: str
    state: str
    notes: List[str] = Field(default_factory=list)

class CaseRecord(BaseModel):
    case_id: str
    adjudication_id: str
    case_class: CaseClass
    clarity_score: float

class CaseIntakeRecord(BaseModel):
    intake_id: str
    case_id: str
    is_valid: bool
    jurisdiction_defective: bool

class IssueFrameRecord(BaseModel):
    frame_id: str
    case_id: str
    issue_class: IssueClass
    excluded_issues: List[str] = Field(default_factory=list)

class AdjudicatorRecord(BaseModel):
    adjudicator_id: str
    independence_score: float

class PanelRecord(BaseModel):
    panel_id: str
    adjudicators: List[str]
    panel_class: PanelClass

class RecusalRecord(BaseModel):
    recusal_id: str
    adjudicator_id: str
    is_valid: bool
    is_late: bool

class ConflictDisqualificationRecord(BaseModel):
    conflict_id: str
    adjudicator_id: str
    is_disqualifying: bool
    hidden_conflict_risk: bool

class AdmissibilityRecord(BaseModel):
    admissibility_id: str
    evidence_id: str
    admissibility_class: AdmissibilityClass

class EvidentiaryRecord(BaseModel):
    record_id: str
    case_id: str
    is_complete: bool
    is_contaminated: bool

class StandardOfProofRecord(BaseModel):
    proof_id: str
    proof_class: ProofClass
    is_laundered: bool

class BurdenAllocationRecord(BaseModel):
    allocation_id: str
    is_proper: bool
    is_shifted: bool
    hidden_shift: bool

class DeliberationRecord(BaseModel):
    deliberation_id: str
    is_genuine: bool
    is_predetermined: bool
    duration_seconds: int

class ExParteRiskRecord(BaseModel):
    risk_id: str
    active_contamination: bool
    hidden_influence: bool

class DeterminationRecord(BaseModel):
    determination_id: str
    deliberation_id: str
    determination_class: DeterminationClass

class ReasoningRecord(BaseModel):
    reasoning_id: str
    determination_id: str
    is_traceable: bool
    has_gap: bool
    is_decorative: bool

class DispositionRecord(BaseModel):
    disposition_id: str
    determination_id: str
    disposition_class: DispositionClass

class BindingEffectRecord(BaseModel):
    binding_id: str
    disposition_id: str
    is_binding: bool
    is_advisory: bool
    is_falsely_binding: bool

class LiabilityDeterminationRecord(BaseModel):
    liability_id: str
    determination_id: str
    is_full: bool
    is_partial: bool
    is_unsupported_inference: bool

class RemedyDispositionRecord(BaseModel):
    remedy_id: str
    disposition_id: str
    is_proportional: bool
    hidden_gap: bool

class DismissalRecord(BaseModel):
    dismissal_id: str
    is_justified: bool
    is_premature: bool
    silent_logic: bool

class AcquittalRecord(BaseModel):
    acquittal_id: str
    is_supported: bool
    is_false_signal: bool

class ConditionalDispositionRecord(BaseModel):
    conditional_id: str
    disposition_id: str
    is_bounded: bool
    has_hidden_burden: bool

class DeferredDispositionRecord(BaseModel):
    deferred_id: str
    disposition_id: str
    is_justified: bool
    is_endless: bool

class AdjudicationDebtRecord(BaseModel):
    debt_id: str
    adjudication_id: str
    debt_class: DebtClass
    severity: str

class AdjudicationDriftRecord(BaseModel):
    drift_id: str
    adjudication_id: str
    drift_notes: str

class AdjudicationComparisonRecord(BaseModel):
    comparison_id: str
    adjudication_id: str
    notes: str

class AdjudicationObservationReport(BaseModel):
    report_id: str
    adjudication_id: str
    observation: str

class AdjudicationForecastReport(BaseModel):
    forecast_id: str
    adjudication_id: str
    prediction: str

class AdjudicationEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict

class AdjudicationDivergenceReport(BaseModel):
    report_id: str
    divergence_sources: List[str]

class AdjudicationTrustVerdict(BaseModel):
    adjudication_id: str
    verdict: TrustVerdict
    breakdown: Dict[str, str]

class AdjudicationAuditRecord(BaseModel):
    audit_id: str
    target_id: str

class AdjudicationArtifactManifest(BaseModel):
    manifest_id: str
    refs: List[str]
