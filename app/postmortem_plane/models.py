from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime

from app.postmortem_plane.enums import (
    PostmortemClass,
    CauseClass,
    ContributorClass,
    ActionClass,
    VerificationClass,
    EffectivenessClass,
    DebtClass,
    DebtInterestClass,
    RecurrenceClass,
    RecurrenceEscalationClass,
    ClosureClass,
    EquivalenceVerdict,
    TrustVerdict,
)

class PostmortemPlaneConfig(BaseModel):
    strict_mode: bool = True
    require_evidence: bool = True

class SourceIncidentBundle(BaseModel):
    incident_ids: List[str]
    incident_family: Optional[str] = None
    severity_carryover: str
    blast_radius: str

class EvidenceReviewRecord(BaseModel):
    evidence_id: str
    evidence_type: str
    freshness: str
    sufficiency_notes: str
    contradictory_evidence_refs: List[str] = Field(default_factory=list)

class CausalNode(BaseModel):
    node_id: str
    cause_class: CauseClass
    description: str
    evidence_refs: List[str] = Field(default_factory=list)
    parent_node_ids: List[str] = Field(default_factory=list)

class CausalChain(BaseModel):
    chain_id: str
    nodes: List[CausalNode]
    completeness_notes: str
    proof_notes: str

class ContributorRecord(BaseModel):
    contributor_id: str
    contributor_class: ContributorClass
    description: str
    severity: str
    role: str

class RootCauseRecord(BaseModel):
    root_cause_id: str
    description: str
    causal_node_refs: List[str]
    is_multi_root: bool
    evidence_threshold_met: bool
    proof_notes: str

class ProximateCauseRecord(BaseModel):
    proximate_cause_id: str
    description: str
    causal_node_refs: List[str]
    lineage_refs: List[str]

class ActionVerificationRecord(BaseModel):
    verification_id: str
    verification_class: VerificationClass
    effectiveness: Optional[EffectivenessClass] = None
    proof_notes: str
    verified_at: Optional[datetime] = None
    verified_by: Optional[str] = None

class RemediationAction(BaseModel):
    action_id: str
    action_class: ActionClass
    description: str
    owner: str
    due_date: datetime
    target_scope: str
    is_blocking: bool = False
    dependency_refs: List[str] = Field(default_factory=list)
    verification_records: List[ActionVerificationRecord] = Field(default_factory=list)

class CorrectiveAction(RemediationAction):
    action_class: ActionClass = ActionClass.CORRECTIVE

class PreventiveAction(RemediationAction):
    action_class: ActionClass = ActionClass.PREVENTIVE
    recurrence_prevention_objective: str

class RemediationDebtRecord(BaseModel):
    debt_id: str
    action_ref: str
    debt_class: DebtClass
    interest_class: DebtInterestClass
    lineage_refs: List[str] = Field(default_factory=list)

class RecurrenceRecord(BaseModel):
    recurrence_id: str
    recurrence_class: RecurrenceClass
    previous_incident_family: str
    interval_days: int
    escalation_class: RecurrenceEscalationClass
    comparison_notes: str

class LearningNote(BaseModel):
    note_id: str
    category: str
    description: str
    scope_transferability: str
    lineage_refs: List[str] = Field(default_factory=list)

class PostmortemClosureRecord(BaseModel):
    closure_status: ClosureClass
    closure_rationale: str
    unresolved_blockers: List[str] = Field(default_factory=list)
    closed_at: Optional[datetime] = None
    closed_by: Optional[str] = None

class PostmortemEquivalenceReport(BaseModel):
    report_id: str
    environments_compared: List[str]
    verdict: EquivalenceVerdict
    action_path_equivalence: bool
    verification_equivalence: bool
    proof_notes: str

class PostmortemDivergenceReport(BaseModel):
    report_id: str
    environments_compared: List[str]
    cause_disagreement: bool
    action_mismatch: bool
    verification_mismatch: bool
    debt_classification_drift: bool
    divergence_severity: str

class PostmortemTrustVerdict(BaseModel):
    verdict: TrustVerdict
    evidence_completeness: bool
    causal_chain_quality: bool
    contributor_coverage: bool
    action_quality: bool
    verification_integrity: bool
    debt_visibility: bool
    recurrence_handling: bool
    policy_posture: bool
    breakdown_notes: str

class PostmortemDefinition(BaseModel):
    postmortem_id: str
    postmortem_class: PostmortemClass
    source_incidents: SourceIncidentBundle
    severity_class: str
    affected_scopes: List[str]
    evidence_reviews: List[EvidenceReviewRecord] = Field(default_factory=list)
    causal_chain: Optional[CausalChain] = None
    contributors: List[ContributorRecord] = Field(default_factory=list)
    root_causes: List[RootCauseRecord] = Field(default_factory=list)
    proximate_causes: List[ProximateCauseRecord] = Field(default_factory=list)
    corrective_actions: List[CorrectiveAction] = Field(default_factory=list)
    preventive_actions: List[PreventiveAction] = Field(default_factory=list)
    debt_records: List[RemediationDebtRecord] = Field(default_factory=list)
    recurrence_records: List[RecurrenceRecord] = Field(default_factory=list)
    learning_notes: List[LearningNote] = Field(default_factory=list)
    closure_record: Optional[PostmortemClosureRecord] = None
    trust_verdict: Optional[PostmortemTrustVerdict] = None
    created_at: datetime
    updated_at: datetime

class PostmortemRef(BaseModel):
    postmortem_id: str
    postmortem_class: PostmortemClass
    status: str

class PostmortemAuditRecord(BaseModel):
    audit_id: str
    postmortem_id: str
    action: str
    timestamp: datetime
    actor: str
    details: Dict[str, Any]

class PostmortemArtifactManifest(BaseModel):
    manifest_id: str
    postmortem_id: str
    incident_refs: List[str]
    evidence_refs: List[str]
    cause_refs: List[str]
    contributor_refs: List[str]
    action_refs: List[str]
    verification_refs: List[str]
    debt_refs: List[str]
    closure_refs: List[str]
    hashes: Dict[str, str]
