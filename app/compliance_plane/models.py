from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any, Set
from datetime import datetime
from uuid import UUID

from app.compliance_plane.enums import (
    RequirementClass,
    ControlClass,
    EvidenceClass,
    AttestationClass,
    CertificationClass,
    ExceptionClass,
    RetentionClass,
    AuditReadinessClass,
    EquivalenceVerdict,
    TrustVerdict,
)


class ComplianceRequirementRef(BaseModel):
    requirement_id: str


class ControlObjectiveRef(BaseModel):
    control_id: str


class EvidenceBundleRef(BaseModel):
    bundle_id: str


class RetentionPolicy(BaseModel):
    retention_id: str
    retention_class: RetentionClass
    retention_window_days: int
    is_immutable: bool
    purge_eligible: bool
    proof_note: Optional[str] = None


class ComplianceRequirement(BaseModel):
    requirement_id: str
    requirement_class: RequirementClass
    scope: Dict[str, Any]
    owner_id: str
    satisfaction_criteria: str
    review_cadence_days: int
    failure_severity: str
    lineage_refs: List[str]
    is_mandatory: bool


class ControlObjective(BaseModel):
    control_id: str
    control_class: ControlClass
    owner_id: str
    cadence_days: int
    is_automated: bool
    is_preventive: bool
    is_detective: bool
    is_corrective: bool
    is_compensating: bool


class ControlMapping(BaseModel):
    mapping_id: str
    requirement_refs: List[ComplianceRequirementRef]
    control_ref: ControlObjectiveRef
    evidence_classes_required: List[EvidenceClass]
    mapping_proof_note: Optional[str] = None


class EvidenceRequirement(BaseModel):
    evidence_req_id: str
    control_ref: ControlObjectiveRef
    mandatory_evidence_classes: List[EvidenceClass]
    freshness_window_days: int
    completeness_checks: List[str]
    evidence_provenance: str


class AttestationRecord(BaseModel):
    attestation_id: str
    attestation_class: AttestationClass
    target_ref: str  # requirement_id or control_id
    attester_id: str
    attested_at: datetime
    expires_at: datetime
    is_stale: bool


class CertificationRecord(BaseModel):
    certification_id: str
    certification_class: CertificationClass
    scope: Dict[str, Any]
    certifier_id: str
    certified_at: datetime
    expires_at: datetime
    dependencies: List[str]
    proof_note: Optional[str] = None


class ControlEffectivenessReview(BaseModel):
    review_id: str
    control_ref: ControlObjectiveRef
    reviewer_id: str
    reviewed_at: datetime
    design_effective: bool
    operating_effective: bool
    partial_effectiveness_note: Optional[str] = None
    ineffective_reason: Optional[str] = None


class ExceptionAcceptanceRecord(BaseModel):
    exception_id: str
    exception_class: ExceptionClass
    target_ref: str  # requirement_id or control_id
    scope: Dict[str, Any]
    reason: str
    approver_ids: List[str]
    accepted_at: datetime
    expires_at: datetime
    residual_risk_note: str
    is_stale: bool


class CompensatingControlRecord(BaseModel):
    compensating_id: str
    target_control_ref: ControlObjectiveRef
    substitute_control_ref: ControlObjectiveRef
    residual_risk_estimation: str
    expires_at: datetime
    proof_note: Optional[str] = None


class AuditReadinessReport(BaseModel):
    report_id: str
    readiness_class: AuditReadinessClass
    requirement_satisfaction_score: float
    evidence_freshness_score: float
    attestation_coverage: float
    certification_coverage: float
    exception_burden_score: float
    proof_note: Optional[str] = None


class AuditFinding(BaseModel):
    finding_id: str
    target_ref: str
    finding_type: str  # evidence_gap, stale_control, exception_misuse, ineffective_control, retention_breach
    severity: str
    description: str
    discovered_at: datetime


class ComplianceRemediation(BaseModel):
    remediation_id: str
    finding_ref: str
    owner_id: str
    due_at: datetime
    verification_required: bool
    is_blocking: bool
    is_overdue: bool
    lineage_refs: List[str]


class ComplianceDebtRecord(BaseModel):
    debt_id: str
    debt_type: str  # stale_evidence, expired_attestation, stale_exception, compensating_control_cleanup, overdue_remediation
    severity: str
    target_ref: str
    incurred_at: datetime


class ComplianceRecurrenceRecord(BaseModel):
    recurrence_id: str
    recurrence_type: str  # repeated_finding, repeated_stale_attestation, repeated_exception_misuse, repeated_evidence_gap
    target_ref: str
    escalation_class: str
    lineage_refs: List[str]


class ComplianceEquivalenceReport(BaseModel):
    report_id: str
    target_requirement_ref: ComplianceRequirementRef
    verdict: EquivalenceVerdict
    replay_posture: Dict[str, Any]
    paper_posture: Dict[str, Any]
    probation_posture: Dict[str, Any]
    live_posture: Dict[str, Any]
    proof_note: Optional[str] = None


class ComplianceDivergenceReport(BaseModel):
    report_id: str
    divergence_type: str  # environment_specific, stale_evidence, attestation_mismatch, exception_burden, control_effectiveness_drift
    severity: str
    blast_radius: str
    description: str


class ComplianceTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    factors: Dict[str, str]
    breakdown: Dict[str, Any]
    evaluated_at: datetime


class ComplianceAuditRecord(BaseModel):
    audit_id: str
    event_type: str
    target_ref: str
    actor_id: str
    timestamp: datetime
    metadata: Dict[str, Any]


class ComplianceArtifactManifest(BaseModel):
    manifest_id: str
    requirement_refs: List[str]
    control_refs: List[str]
    evidence_refs: List[str]
    attestation_refs: List[str]
    exception_refs: List[str]
    finding_refs: List[str]
    debt_refs: List[str]
    hashes: Dict[str, str]
    lineage_refs: List[str]


class CompliancePlaneConfig(BaseModel):
    default_retention_days: int = 365
    strict_evidence_freshness: bool = True
    block_on_expired_attestation: bool = True
    allow_compensating_controls: bool = True
