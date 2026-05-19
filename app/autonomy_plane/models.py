from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.autonomy_plane.enums import (
    AutonomyClass, AgentClass, TaskClass, IntentClass, CapabilityClass,
    PermissionClass, DelegationClass, ApprovalClass, GuardrailClass,
    InterventionClass, HaltClass, TrustVerdict, EquivalenceVerdict
)

@dataclass
class AutonomyPlaneConfig:
    is_active: bool = True

@dataclass
class AutonomyObjectRef:
    ref_id: str

@dataclass
class AgentRecord:
    agent_id: str
    agent_class: AgentClass
    criticality_notes: str = ""
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class TaskRecord:
    task_id: str
    task_class: TaskClass
    scope: str
    proof_notes: str = ""
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class GoalRecord:
    goal_id: str
    scope_notes: str = ""
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class IntentRecord:
    intent_id: str
    intent_class: IntentClass
    ambiguity_warnings: str = ""
    lineage_refs: List[str] = field(default_factory=list)

@dataclass
class ScopeRecord:
    scope_id: str
    object_scope: str
    domain_scope: str
    tenant_scope: str
    environment_scope: str
    time_bounded_scope: str
    ambiguity_warnings: str = ""

@dataclass
class CapabilityRecord:
    capability_id: str
    capability_class: CapabilityClass
    proof_notes: str = ""

@dataclass
class PermissionRecord:
    permission_id: str
    permission_class: PermissionClass
    proof_notes: str = ""

@dataclass
class DelegationRecord:
    delegation_id: str
    delegation_class: DelegationClass
    expiry_time: Optional[datetime] = None
    stale_warning: str = ""

@dataclass
class ApprovalRecord:
    approval_id: str
    approval_class: ApprovalClass
    freshness_notes: str = ""

@dataclass
class GuardrailRecord:
    guardrail_id: str
    guardrail_class: GuardrailClass
    enforcement_notes: str = ""

@dataclass
class ConstraintRecord:
    constraint_id: str
    hidden_constraint_cautions: str = ""

@dataclass
class BudgetRecord:
    budget_id: str
    retry_budget: int = 0
    time_budget: int = 0
    cost_budget: float = 0.0

@dataclass
class PlanRecord:
    plan_id: str
    completeness_notes: str = ""

@dataclass
class RationaleRecord:
    rationale_id: str
    evidence_backed: bool = True
    assumption_aware: bool = True

@dataclass
class ConfidenceRecord:
    confidence_id: str
    model_confidence: float = 0.0
    action_confidence: float = 0.0
    outcome_confidence: float = 0.0

@dataclass
class UncertaintyRecord:
    uncertainty_id: str
    hidden_uncertainty_warnings: str = ""

@dataclass
class SelfCheckRecord:
    self_check_id: str
    trigger: str = ""
    missing_warnings: str = ""

@dataclass
class VerificationRecord:
    verification_id: str
    scope_caveats: str = ""

@dataclass
class SandboxRecord:
    sandbox_id: str
    portability_caveats: str = ""

@dataclass
class AutonomousExecutionRecord:
    execution_id: str
    receipts: List[str] = field(default_factory=list)

@dataclass
class HumanInterventionRecord:
    intervention_id: str
    intervention_class: InterventionClass
    burden_notes: str = ""

@dataclass
class EscalationRecord:
    escalation_id: str
    avoidance_warnings: str = ""

@dataclass
class OverrideRecord:
    override_id: str
    residual_risk_notes: str = ""

@dataclass
class HaltRecord:
    halt_id: str
    halt_class: HaltClass
    release_conditions: str = ""

@dataclass
class RevocationRecord:
    revocation_id: str
    stale_caveats: str = ""

@dataclass
class RollbackRecord:
    rollback_id: str
    credibility_notes: str = ""

@dataclass
class AutonomyObservationRecord:
    observation_id: str
    sufficiency_notes: str = ""

@dataclass
class AutonomyDebtRecord:
    debt_id: str
    stale_delegation_debt: int = 0
    self_approval_debt: int = 0

@dataclass
class AutonomyForecastReport:
    forecast_id: str
    delegation_decay: float = 0.0

@dataclass
class AutonomyEquivalenceReport:
    equivalence_id: str
    verdict: EquivalenceVerdict

@dataclass
class AutonomyDivergenceReport:
    divergence_id: str
    divergence_notes: str = ""

@dataclass
class AutonomyTrustVerdict:
    verdict_id: str
    verdict: TrustVerdict
    blockers: List[str] = field(default_factory=list)
    caveats: List[str] = field(default_factory=list)

@dataclass
class AutonomyAuditRecord:
    audit_id: str
    audit_notes: str = ""

@dataclass
class AutonomyArtifactManifest:
    manifest_id: str
    artifacts: List[str] = field(default_factory=list)

@dataclass
class AutonomyObject:
    autonomy_id: str
    agent_id: str
    autonomy_class: AutonomyClass
    owner: str
    delegation_id: Optional[str] = None
    authorization_posture: str = "unverified"
    intervention_posture: str = "unknown"
