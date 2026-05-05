from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime, timezone
from app.policy_kernel.enums import (
    PolicyDomain,
    RuleClass,
    PolicyVerdict,
    EvidenceFreshness,
    ConflictClass,
    PrecedenceClass,
    DriftSeverity,
    GapSeverity,
)


class PolicyRuleVersion(BaseModel):
    version_id: str
    effective_from: datetime
    effective_to: Optional[datetime] = None


class PolicyRule(BaseModel):
    rule_id: str
    owner: str
    rationale: str
    domain: PolicyDomain
    severity: PolicyVerdict
    required_evidence: List[str] = Field(default_factory=list)
    is_waivable: bool = False
    effective_scope: List[str] = Field(default_factory=list)
    profile_constraints: List[str] = Field(default_factory=list)
    version: PolicyRuleVersion


class PolicyInvariant(PolicyRule):
    rule_class: RuleClass = RuleClass.INVARIANT
    is_waivable: bool = False  # Always False
    severity: PolicyVerdict = (
        PolicyVerdict.HARD_BLOCK
    )  # Invariants always result in HARD_BLOCK if violated


class PolicyContext(BaseModel):
    action_type: str
    workspace_id: str
    profile_id: str
    mode: str  # live, testnet, paper
    capital_posture: Dict[str, Any] = Field(default_factory=dict)
    event_overlay: Dict[str, Any] = Field(default_factory=dict)
    stress_overlay: Dict[str, Any] = Field(default_factory=dict)
    cross_book_posture: Dict[str, Any] = Field(default_factory=dict)
    qualification_status: Dict[str, Any] = Field(default_factory=dict)
    shadow_truthfulness: Dict[str, Any] = Field(default_factory=dict)
    lifecycle_health: Dict[str, Any] = Field(default_factory=dict)
    remediation_debt: Dict[str, Any] = Field(default_factory=dict)
    approvals: List[str] = Field(default_factory=list)


class PolicyEvidenceBundle(BaseModel):
    qualification_refs: Dict[str, Any] = Field(default_factory=dict)
    stress_refs: Dict[str, Any] = Field(default_factory=dict)
    ledger_refs: Dict[str, Any] = Field(default_factory=dict)
    shadow_refs: Dict[str, Any] = Field(default_factory=dict)
    event_refs: Dict[str, Any] = Field(default_factory=dict)
    workspace_refs: Dict[str, Any] = Field(default_factory=dict)
    lifecycle_refs: Dict[str, Any] = Field(default_factory=dict)
    control_refs: Dict[str, Any] = Field(default_factory=dict)
    capital_refs: Dict[str, Any] = Field(default_factory=dict)
    freshness: Dict[str, EvidenceFreshness] = Field(default_factory=dict)
    is_complete: bool = False


class PolicyDecisionNode(BaseModel):
    rule_id: str
    verdict: PolicyVerdict
    evidence_used: List[str]
    reasoning: str
    is_overridden: bool = False
    overridden_by: Optional[str] = None
    waiver_applied: Optional[str] = None


class PolicyDecisionGraph(BaseModel):
    nodes: List[PolicyDecisionNode] = Field(default_factory=list)
    root_verdict: PolicyVerdict


class PolicyDecision(BaseModel):
    decision_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    action_type: str
    context: PolicyContext
    evidence: PolicyEvidenceBundle
    graph: PolicyDecisionGraph
    final_verdict: PolicyVerdict
    winning_rules: List[str]
    reasoning: str


class PolicyConflict(BaseModel):
    conflict_id: str
    action_type: str
    rule_a_id: str
    rule_b_id: str
    conflict_class: ConflictClass
    resolution_notes: str


class PolicyPrecedenceRule(BaseModel):
    precedence_class: PrecedenceClass
    description: str


class PolicyWaiverRequest(BaseModel):
    waiver_id: str
    rule_id: str
    requester: str
    rationale: str
    scope: str
    ttl_seconds: int


class PolicyWaiverDecision(BaseModel):
    waiver_id: str
    rule_id: str
    approver: str
    is_approved: bool
    expires_at: datetime
    scope: str


class PolicyDriftRecord(BaseModel):
    drift_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    module_name: str
    declared_verdict: PolicyVerdict
    actual_verdict: PolicyVerdict
    action_type: str
    severity: DriftSeverity
    remediation_suggestion: str


class PolicyGapFinding(BaseModel):
    gap_id: str
    domain: PolicyDomain
    description: str
    severity: GapSeverity
    suggested_action: str


class PolicyAuditRecord(BaseModel):
    audit_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    decisions_reviewed: int
    drifts_found: int
    gaps_found: int
    summary: str


class PolicyArtifactManifest(BaseModel):
    manifest_id: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    artifacts_included: List[str]
