from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from app.obligation_plane.enums import (ObligationClass, DutyClass, RequirementClass,
                                        ProhibitionClass, TriggerClass, DeadlineClass,
                                        RecurrenceClass, BreachClass, DischargeClass,
                                        ExcuseClass, ObligationEquivalenceVerdict,
                                        ObligationTrustVerdict)

class ObligationPlaneConfig(BaseModel):
    enabled: bool = True
    strict_mode: bool = True

class ObligationObjectRef(BaseModel):
    obligation_id: str
    owner: str

class ObligationObject(BaseModel):
    obligation_id: str
    obligation_class: ObligationClass
    owner: str
    scope: str
    trigger_posture: str
    discharge_posture: str

class ObligationRecord(BaseModel):
    id: str
    state: str = "ACTIVE"
    proof_notes: str = ""

class DutyRecord(BaseModel):
    duty_class: DutyClass
    lineage_refs: List[str]

class RequirementRecord(BaseModel):
    requirement_class: RequirementClass
    lineage_refs: List[str]

class ProhibitionRecord(BaseModel):
    prohibition_class: ProhibitionClass
    lineage_refs: List[str]

class ForbearanceRecord(BaseModel):
    forbearance_type: str
    scope: str
    lineage_refs: List[str]

class TriggerRecord(BaseModel):
    trigger_class: TriggerClass
    opacity_caution: bool = False
    lineage_refs: List[str]

class TriggerConditionRecord(BaseModel):
    condition_type: str
    validity_notes: str = ""

class TriggerActivationRecord(BaseModel):
    activation_state: str
    lineage_refs: List[str]

class DeadlineRecord(BaseModel):
    deadline_class: DeadlineClass
    theater_caution: bool = False
    lineage_refs: List[str]

class DueWindowRecord(BaseModel):
    window_type: str
    caveats: str = ""
    lineage_refs: List[str]

class RecurrenceRecord(BaseModel):
    recurrence_class: RecurrenceClass
    collapse_warning: bool = False
    lineage_refs: List[str]

class EscalationDutyRecord(BaseModel):
    escalation_type: str
    notes: str = ""
    lineage_refs: List[str]

class NonWaivableDutyRecord(BaseModel):
    duty_type: str
    lineage_refs: List[str]

class SuspensionRecord(BaseModel):
    suspension_type: str
    warnings: str = ""
    lineage_refs: List[str]

class WaiverRecord(BaseModel):
    waiver_type: str
    residual_duty_notes: str = ""
    lineage_refs: List[str]

class ExcuseRecord(BaseModel):
    excuse_class: ExcuseClass
    caveats: str = ""
    lineage_refs: List[str]

class ImpossibilityRecord(BaseModel):
    impossibility_state: str
    lineage_refs: List[str]

class SubstitutePerformanceRecord(BaseModel):
    substitute_type: str
    laundering_caution: bool = False
    lineage_refs: List[str]

class BreachRecord(BaseModel):
    breach_class: BreachClass
    lineage_refs: List[str]

class OverdueRecord(BaseModel):
    overdue_type: str
    notes: str = ""
    lineage_refs: List[str]

class DischargeRecord(BaseModel):
    discharge_class: DischargeClass
    integrity_notes: str = ""
    lineage_refs: List[str]

class ResidualDutyRecord(BaseModel):
    surviving_duty_type: str
    hidden_residual_caution: bool = False
    lineage_refs: List[str]

class BeneficiarySafeCompletionRecord(BaseModel):
    completion_type: str
    notes: str = ""
    lineage_refs: List[str]

class ObligationComparisonRecord(BaseModel):
    comparison_type: str
    lineage_refs: List[str]

class ObligationObservationReport(BaseModel):
    summary: str

class ObligationForecastReport(BaseModel):
    overdue_growth: float = 0.0
    recurrence_miss_prob: float = 0.0

class ObligationDebtRecord(BaseModel):
    debt_type: str
    severity: int
    lineage_refs: List[str]

class ObligationEquivalenceReport(BaseModel):
    verdict: ObligationEquivalenceVerdict
    blockers: List[str]

class ObligationDivergenceReport(BaseModel):
    divergence_type: str
    severity: int
    blast_radius: str

class ObligationTrustVerdict(BaseModel):
    verdict: ObligationTrustVerdict
    blockers: List[str]
    caveats: List[str]

class ObligationAuditRecord(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    action: str

class ObligationArtifactManifest(BaseModel):
    manifest_id: str
    hashes: Dict[str, str]
