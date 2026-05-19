from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

from app.learning_plane.enums import (
    LearningClass, SignalClass, OriginClass, OutcomeClass, FailureClass,
    FindingClass, LessonClass, HardeningClass, ValidationClass, RecurrenceClass,
    EquivalenceVerdict, TrustVerdict, ReadinessClass, UncertaintyClass, AdoptionStatus
)

class LearningObjectRef(BaseModel):
    learning_id: str
    description: str

class LearningSignalRecord(BaseModel):
    signal_id: str
    signal_class: SignalClass
    description: str
    confidence_notes: str
    detected_at: datetime
    learning_ref: Optional[str] = None

class LearningOriginRecord(BaseModel):
    origin_id: str
    origin_class: OriginClass
    description: str
    proof_notes: str
    learning_ref: Optional[str] = None

class OutcomeRecord(BaseModel):
    outcome_id: str
    outcome_class: OutcomeClass
    description: str
    evidence_notes: str

class FailureClassRecord(BaseModel):
    failure_class_id: str
    failure_class: FailureClass
    description: str

class NearMissRecord(BaseModel):
    near_miss_id: str
    description: str
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class AvoidedFailureRecord(BaseModel):
    avoided_failure_id: str
    description: str
    learning_notes: str

class FindingRecord(BaseModel):
    finding_id: str
    finding_class: FindingClass
    description: str
    confidence_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class CausalHypothesisRecord(BaseModel):
    hypothesis_id: str
    description: str
    is_primary: bool
    uncertainty_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class ValidatedCauseRecord(BaseModel):
    cause_id: str
    hypothesis_id: str
    description: str
    evidence: str
    sufficiency_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class LessonRecord(BaseModel):
    lesson_id: str
    lesson_class: LessonClass
    description: str
    clarity_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class ScopeOfLessonRecord(BaseModel):
    scope_id: str
    lesson_id: str
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class HardeningActionRecord(BaseModel):
    action_id: str
    hardening_class: HardeningClass
    description: str
    burden_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class UpdateTargetRecord(BaseModel):
    target_id: str
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class AdoptionRecord(BaseModel):
    adoption_id: str
    status: AdoptionStatus
    description: str
    stale_warnings: str
    lineage_refs: List[str] = Field(default_factory=list)

class ValidationRecord(BaseModel):
    validation_id: str
    validation_class: ValidationClass
    description: str
    sufficiency_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class RecurrenceRecord(BaseModel):
    recurrence_id: str
    recurrence_class: RecurrenceClass
    description: str
    severity: str
    interval: str
    proof_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class PrecedentLearningRecord(BaseModel):
    precedent_id: str
    description: str
    is_dangerous: bool
    caution_notes: str
    lineage_refs: List[str] = Field(default_factory=list)

class LearningComparisonRecord(BaseModel):
    comparison_id: str
    description: str
    lineage_refs: List[str] = Field(default_factory=list)

class LearningForecastReport(BaseModel):
    forecast_id: str
    recurrence_likelihood: str
    lesson_decay: str
    uncertainty: UncertaintyClass

class LearningDebtRecord(BaseModel):
    debt_id: str
    description: str
    severity: str
    interest: str

class LearningEquivalenceReport(BaseModel):
    report_id: str
    verdict: EquivalenceVerdict
    blockers: List[str] = Field(default_factory=list)
    proof_notes: str

class LearningDivergenceReport(BaseModel):
    report_id: str
    divergence_type: str
    severity: str
    description: str

class LearningTrustVerdict(BaseModel):
    verdict: TrustVerdict
    factors: Dict[str, str]
    caveats: List[str] = Field(default_factory=list)

class LearningArtifactManifest(BaseModel):
    manifest_id: str
    learning_id: str
    hashes: Dict[str, str]

class LearningObject(BaseModel):
    learning_id: str
    learning_class: LearningClass
    owner: str
    scope: str
    origin_id: str
    signal_ids: List[str] = Field(default_factory=list)
    outcome_ids: List[str] = Field(default_factory=list)
    failure_class_ids: List[str] = Field(default_factory=list)
    near_miss_ids: List[str] = Field(default_factory=list)
    avoided_failure_ids: List[str] = Field(default_factory=list)
    finding_ids: List[str] = Field(default_factory=list)
    hypothesis_ids: List[str] = Field(default_factory=list)
    cause_ids: List[str] = Field(default_factory=list)
    lesson_ids: List[str] = Field(default_factory=list)
    scope_ids: List[str] = Field(default_factory=list)
    action_ids: List[str] = Field(default_factory=list)
    target_ids: List[str] = Field(default_factory=list)
    adoption_ids: List[str] = Field(default_factory=list)
    validation_ids: List[str] = Field(default_factory=list)
    recurrence_ids: List[str] = Field(default_factory=list)
    precedent_ids: List[str] = Field(default_factory=list)
    validation_posture: str
    state: str = "active"

class LearningPlaneConfig(BaseModel):
    require_validation: bool = True
    enforce_strict_lineage: bool = True
