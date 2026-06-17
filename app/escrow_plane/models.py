from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class EscrowPlaneConfig:
    strict_neutrality_enforcement: bool = True
    require_dispute_awareness: bool = True
    prevent_fake_segregation: bool = True

@dataclass
class EscrowObjectRef:
    escrow_id: str
    class_type: str

@dataclass
class EscrowSubjectRecord:
    subject_id: str
    is_direct: bool = True
    is_composite: bool = False
    is_federated: bool = False
    has_opacity_gap: bool = False

@dataclass
class DepositedAssetRecord:
    asset_id: str
    asset_class: str
    is_disguised_deposit: bool = False
    has_opacity: bool = False

@dataclass
class DepositorRecord:
    depositor_id: str
    depositor_type: str
    has_blur_risk: bool = False

@dataclass
class BeneficiaryRecord:
    beneficiary_id: str
    beneficiary_type: str
    has_opacity_gap: bool = False

@dataclass
class EscrowAgentRecord:
    agent_id: str
    agent_type: str
    has_blur_risk: bool = False

@dataclass
class AgentAuthorityRecord:
    authority_id: str
    authority_state: str
    has_overreach_risk: bool = False

@dataclass
class AgentNeutralityRecord:
    neutrality_id: str
    neutrality_state: str
    has_theater_risk: bool = False

@dataclass
class EscrowCapacityRecord:
    capacity_id: str
    capacity_state: str
    has_illusion_risk: bool = False

@dataclass
class SegregationRecord:
    segregation_id: str
    segregation_state: str
    has_burial_risk: bool = False

@dataclass
class ComminglingRecord:
    commingling_id: str
    commingling_state: str
    has_denial_risk: bool = False

@dataclass
class CustodyRecord:
    custody_id: str
    custody_state: str
    has_opacity_risk: bool = False

@dataclass
class HoldConditionRecord:
    condition_id: str
    condition_type: str
    has_opacity_risk: bool = False

@dataclass
class ConditionEvidenceRecord:
    evidence_id: str
    evidence_state: str
    has_theater_risk: bool = False

@dataclass
class MilestoneReleaseRecord:
    milestone_id: str
    milestone_state: str
    has_laundering_risk: bool = False

@dataclass
class DocumentaryReleaseRecord:
    documentary_id: str
    documentary_state: str
    has_opacity_risk: bool = False

@dataclass
class AdjudicatedReleaseRecord:
    adjudicated_id: str
    adjudicated_state: str
    has_theater_risk: bool = False

@dataclass
class DualConsentReleaseRecord:
    dual_consent_id: str
    consent_state: str
    has_laundering_risk: bool = False

@dataclass
class UnilateralReleaseProhibitionRecord:
    prohibition_id: str
    prohibition_state: str
    has_opacity_risk: bool = False

@dataclass
class InstructionRecord:
    instruction_id: str
    instruction_state: str
    has_theater_risk: bool = False

@dataclass
class InstructionValidationRecord:
    validation_id: str
    validation_state: str
    has_laundering_risk: bool = False

@dataclass
class DisputeHoldRecord:
    dispute_id: str
    dispute_state: str
    has_burial_risk: bool = False

@dataclass
class ReservedPortionRecord:
    reserved_id: str
    reserved_state: str
    has_opacity_risk: bool = False

@dataclass
class PartialReleaseRecord:
    partial_id: str
    partial_state: str
    has_comfort_risk: bool = False

@dataclass
class WrongBeneficiaryReleaseRecord:
    wrong_id: str
    wrong_state: str
    has_burial_risk: bool = False

@dataclass
class ReleaseActionRecord:
    release_id: str
    release_state: str
    has_comfort_risk: bool = False

@dataclass
class ReleaseReversalRecord:
    reversal_id: str
    reversal_state: str
    has_theater_risk: bool = False

@dataclass
class ClawbackStyleRecoveryRecord:
    recovery_id: str
    recovery_state: str
    has_opacity_risk: bool = False

@dataclass
class EscrowExpiryRecord:
    expiry_id: str
    expiry_state: str
    has_laundering_risk: bool = False

@dataclass
class AbandonmentRecord:
    abandonment_id: str
    abandonment_state: str
    has_opacity_risk: bool = False

@dataclass
class DisposalPathRecord:
    disposal_id: str
    disposal_state: str
    has_laundering_risk: bool = False

@dataclass
class YieldRecord:
    yield_id: str
    yield_state: str
    has_opacity_risk: bool = False

@dataclass
class NegativeCarryRecord:
    carry_id: str
    carry_state: str
    has_burial_risk: bool = False

@dataclass
class EscrowDebtRecord:
    debt_id: str
    debt_type: str
    severity: str
    has_burial_risk: bool = False

@dataclass
class EscrowDriftRecord:
    drift_id: str
    drift_state: str

@dataclass
class EscrowComparisonRecord:
    comparison_id: str
    comparison_type: str
    has_apples_to_oranges_risk: bool = False

@dataclass
class EscrowObservationReport:
    report_id: str
    escrow_id: str
    observations: List[str] = field(default_factory=list)

@dataclass
class EscrowForecastReport:
    forecast_id: str
    escrow_id: str
    forecast_type: str
    has_fake_certainty: bool = False

@dataclass
class EscrowEquivalenceReport:
    report_id: str
    equivalence_class: str
    divergence_sources: List[str] = field(default_factory=list)

@dataclass
class EscrowDivergenceReport:
    report_id: str
    divergence_class: str
    severity: str

@dataclass
class EscrowTrustVerdict:
    escrow_id: str
    verdict: str
    factors: Dict[str, Any] = field(default_factory=dict)
    breakdown_mandatory: bool = True

@dataclass
class EscrowAuditRecord:
    audit_id: str
    escrow_id: str
    audit_type: str

@dataclass
class EscrowArtifactManifest:
    manifest_id: str
    escrow_id: str
    refs: List[str] = field(default_factory=list)

@dataclass
class EscrowObject:
    escrow_id: str
    escrow_class: str
    owner: str
    scope: str
    hold_posture: str
    release_posture: str
    subject: Optional[EscrowSubjectRecord] = None
    asset: Optional[DepositedAssetRecord] = None
    depositor: Optional[DepositorRecord] = None
    beneficiary: Optional[BeneficiaryRecord] = None
    agent: Optional[EscrowAgentRecord] = None
    condition: Optional[HoldConditionRecord] = None

@dataclass
class EscrowRecord:
    record_id: str
    escrow_object: EscrowObject
    status: str
