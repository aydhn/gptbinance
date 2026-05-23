from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime
from .enums import (
    AuthorityClass, MandateClass, DecisionRightClass, DelegationClass, OverrideClass,
    VetoClass, RatificationClass, EscalationClass, QuorumClass, LegitimacyClass,
    EquivalenceVerdict, TrustVerdict
)

@dataclass
class AuthorityPlaneConfig:
    strict_mode: bool = True

@dataclass
class AuthorityObjectRef:
    authority_id: str
    class_type: AuthorityClass

@dataclass
class AuthorityObject:
    authority_id: str
    class_type: AuthorityClass
    owner: str
    scope: List[str]
    mandate_posture: Dict[str, Any]
    legitimacy_posture: Dict[str, Any]

@dataclass
class AuthorityRecord:
    authority_id: str
    object: AuthorityObject
    status: str
    proof_notes: List[str]
    lineage_refs: List[str]

@dataclass
class MandateRecord:
    mandate_id: str
    authority_id: str
    class_type: MandateClass
    caveats: List[str]
    lineage_refs: List[str]

@dataclass
class DecisionRightRecord:
    right_id: str
    authority_id: str
    class_type: DecisionRightClass
    ambiguity_notes: List[str]
    lineage_refs: List[str]

@dataclass
class ApprovalAuthorityRecord:
    authority_id: str
    type: str # BINDING, SCOPED, QUORUM, DELEGATED
    mandate_refs: List[str]
    lineage_refs: List[str]

@dataclass
class AdvisoryAuthorityRecord:
    authority_id: str
    type: str # NON_BINDING, REQUIRED, TECHNICAL, RISK
    caveats: List[str]
    lineage_refs: List[str]

@dataclass
class ReviewAuthorityRecord:
    authority_id: str
    type: str # MANDATORY, OPTIONAL, REVIEW_ONLY
    sufficiency_notes: List[str]
    lineage_refs: List[str]

@dataclass
class VetoAuthorityRecord:
    authority_id: str
    class_type: VetoClass
    caveats: List[str]
    lineage_refs: List[str]

@dataclass
class OverrideAuthorityRecord:
    authority_id: str
    class_type: OverrideClass
    boundary_notes: List[str]
    lineage_refs: List[str]

@dataclass
class DelegationRecord:
    delegation_id: str
    from_authority: str
    to_authority: str
    class_type: DelegationClass
    warnings: List[str]
    lineage_refs: List[str]

@dataclass
class SubdelegationRecord:
    subdelegation_id: str
    delegation_id: str
    permitted: bool
    warnings: List[str]
    lineage_refs: List[str]

@dataclass
class RatificationRecord:
    ratification_id: str
    class_type: RatificationClass
    abuse_cautions: List[str]
    lineage_refs: List[str]

@dataclass
class EscalationRecord:
    escalation_id: str
    class_type: EscalationClass
    resolution_caveats: List[str]
    lineage_refs: List[str]

@dataclass
class QuorumRecord:
    quorum_id: str
    class_type: QuorumClass
    theater_warnings: List[str]
    lineage_refs: List[str]

@dataclass
class JointAuthorityRecord:
    joint_id: str
    type: str # DUAL, MULTI, CONCURRENT, SPLIT
    warnings: List[str]
    lineage_refs: List[str]

@dataclass
class SeparationOfDutiesRecord:
    sod_id: str
    type: str # MAKER_CHECKER, APPROVER_REVIEWER, FINANCIAL_CONTROL
    relaxation_notes: List[str]
    lineage_refs: List[str]

@dataclass
class TemporaryAuthorityRecord:
    authority_id: str
    type: str # TIME_BOUNDED, EVENT_BOUNDED, ACTING
    expired: bool
    lineage_refs: List[str]

@dataclass
class EmergencyAuthorityRecord:
    authority_id: str
    type: str # BREAK_GLASS, INCIDENT, CRISIS
    abuse_notes: List[str]
    lineage_refs: List[str]

@dataclass
class FederatedAuthorityRecord:
    authority_id: str
    type: str # PARTNER, SHARED, LOCAL_WITH_CONSENT
    reach_cautions: List[str]
    lineage_refs: List[str]

@dataclass
class ShadowAuthorityRecord:
    shadow_id: str
    type: str # INFORMAL, TITLE_MISMATCH, INFLUENCE
    findings: List[str]
    lineage_refs: List[str]

@dataclass
class LegitimacyGapRecord:
    gap_id: str
    type: str # NO_VALID, WRONG_SCOPE, EXPIRED, MISSING_RATIFICATION
    lineage_refs: List[str]

@dataclass
class AuthorityComparisonRecord:
    comparison_id: str
    type: str
    notes: List[str]
    lineage_refs: List[str]

@dataclass
class AuthorityObservationReport:
    report_id: str
    data: Dict[str, Any]

@dataclass
class AuthorityForecastReport:
    forecast_id: str
    forecasts: Dict[str, Any]
    uncertainty_classes: List[str]

@dataclass
class AuthorityDebtRecord:
    debt_id: str
    type: str
    severity: str
    lineage_refs: List[str]

@dataclass
class AuthorityEquivalenceReport:
    report_id: str
    verdict: EquivalenceVerdict
    blockers: List[str]

@dataclass
class AuthorityDivergenceReport:
    report_id: str
    divergences: Dict[str, Any]
    severity: str

@dataclass
class AuthorityTrustVerdict:
    verdict: TrustVerdict
    factors: Dict[str, Any]
    blockers: List[str]

@dataclass
class AuthorityAuditRecord:
    audit_id: str
    timestamp: datetime
    action: str
    details: Dict[str, Any]

@dataclass
class AuthorityArtifactManifest:
    manifest_id: str
    refs: Dict[str, List[str]]
    hashes: Dict[str, str]
