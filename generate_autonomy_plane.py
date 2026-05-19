import os

def create_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

# Enums
create_file("app/autonomy_plane/enums.py", """from enum import Enum

class AutonomyClass(str, Enum):
    RECOMMENDATION = "recommendation"
    APPROVAL_BOUND = "approval_bound"
    SUPERVISED = "supervised"
    BOUNDED = "bounded"
    EMERGENCY = "emergency"

class AgentClass(str, Enum):
    SYSTEM = "system"
    OPERATOR_ASSIST = "operator_assist"
    DOMAIN = "domain"
    FEDERATED = "federated"

class TaskClass(str, Enum):
    READ_ONLY = "read_only"
    WRITE = "write"
    HIGH_RISK = "high_risk"
    CROSS_DOMAIN = "cross_domain"

class IntentClass(str, Enum):
    PROPOSE = "propose"
    ACT = "act"
    RECOVER = "recover"
    HALT = "halt"

class CapabilityClass(str, Enum):
    INSPECT = "inspect"
    PROPOSE = "propose"
    EXECUTE = "execute"
    RECOVER = "recover"
    REVOKE = "revoke"

class PermissionClass(str, Enum):
    PER_TASK = "per_task"
    PER_DOMAIN = "per_domain"
    ENVIRONMENT_BOUND = "environment_bound"
    TEMPORARY = "temporary"

class DelegationClass(str, Enum):
    BOUNDED = "bounded"
    ONE_SHOT = "one_shot"
    TIME_WINDOW = "time_window"
    FEDERATED = "federated"

class ApprovalClass(str, Enum):
    PER_ACTION = "per_action"
    PLAN = "plan"
    BATCH = "batch"
    EMERGENCY = "emergency"

class GuardrailClass(str, Enum):
    ACTION = "action"
    SCOPE = "scope"
    VALUE = "value"
    COMPLIANCE = "compliance"
    CONSTITUTIONAL = "constitutional"

class InterventionClass(str, Enum):
    APPROVE = "approve"
    PAUSE = "pause"
    REDIRECT = "redirect"
    NARROW_SCOPE = "narrow_scope"

class HaltClass(str, Enum):
    SOFT = "soft"
    HARD = "hard"
    EMERGENCY = "emergency"
    DEADMAN = "deadman"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"
""")

# Exceptions
create_file("app/autonomy_plane/exceptions.py", """class AutonomyPlaneError(Exception):
    pass

class InvalidAutonomyObject(AutonomyPlaneError):
    pass

class InvalidAgentRecord(AutonomyPlaneError):
    pass

class InvalidTaskScope(AutonomyPlaneError):
    pass

class InvalidCapability(AutonomyPlaneError):
    pass

class InvalidPermissionGrant(AutonomyPlaneError):
    pass

class InvalidDelegation(AutonomyPlaneError):
    pass

class InvalidApproval(AutonomyPlaneError):
    pass

class GuardrailViolation(AutonomyPlaneError):
    pass

class HaltViolation(AutonomyPlaneError):
    pass

class AutonomyStorageError(AutonomyPlaneError):
    pass
""")

# Models
create_file("app/autonomy_plane/models.py", """from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any
from datetime import datetime
from app.autonomy_plane.enums import *

class AutonomyPlaneConfig(BaseModel):
    is_active: bool = True

class AutonomyObjectRef(BaseModel):
    ref_id: str

class AgentRecord(BaseModel):
    agent_id: str
    agent_class: AgentClass
    criticality_notes: str = ""
    lineage_refs: List[str] = Field(default_factory=list)

class TaskRecord(BaseModel):
    task_id: str
    task_class: TaskClass
    scope: str
    proof_notes: str = ""
    lineage_refs: List[str] = Field(default_factory=list)

class GoalRecord(BaseModel):
    goal_id: str
    scope_notes: str = ""
    lineage_refs: List[str] = Field(default_factory=list)

class IntentRecord(BaseModel):
    intent_id: str
    intent_class: IntentClass
    ambiguity_warnings: str = ""
    lineage_refs: List[str] = Field(default_factory=list)

class ScopeRecord(BaseModel):
    scope_id: str
    object_scope: str
    domain_scope: str
    tenant_scope: str
    environment_scope: str
    time_bounded_scope: str
    ambiguity_warnings: str = ""

class CapabilityRecord(BaseModel):
    capability_id: str
    capability_class: CapabilityClass
    proof_notes: str = ""

class PermissionRecord(BaseModel):
    permission_id: str
    permission_class: PermissionClass
    proof_notes: str = ""

class DelegationRecord(BaseModel):
    delegation_id: str
    delegation_class: DelegationClass
    expiry_time: Optional[datetime] = None
    stale_warning: str = ""

class ApprovalRecord(BaseModel):
    approval_id: str
    approval_class: ApprovalClass
    freshness_notes: str = ""

class GuardrailRecord(BaseModel):
    guardrail_id: str
    guardrail_class: GuardrailClass
    enforcement_notes: str = ""

class ConstraintRecord(BaseModel):
    constraint_id: str
    hidden_constraint_cautions: str = ""

class BudgetRecord(BaseModel):
    budget_id: str
    retry_budget: int = 0
    time_budget: int = 0
    cost_budget: float = 0.0

class PlanRecord(BaseModel):
    plan_id: str
    completeness_notes: str = ""

class RationaleRecord(BaseModel):
    rationale_id: str
    evidence_backed: bool = True
    assumption_aware: bool = True

class ConfidenceRecord(BaseModel):
    confidence_id: str
    model_confidence: float = 0.0
    action_confidence: float = 0.0
    outcome_confidence: float = 0.0

class UncertaintyRecord(BaseModel):
    uncertainty_id: str
    hidden_uncertainty_warnings: str = ""

class SelfCheckRecord(BaseModel):
    self_check_id: str
    trigger: str = ""
    missing_warnings: str = ""

class VerificationRecord(BaseModel):
    verification_id: str
    scope_caveats: str = ""

class SandboxRecord(BaseModel):
    sandbox_id: str
    portability_caveats: str = ""

class AutonomousExecutionRecord(BaseModel):
    execution_id: str
    receipts: List[str] = Field(default_factory=list)

class HumanInterventionRecord(BaseModel):
    intervention_id: str
    intervention_class: InterventionClass
    burden_notes: str = ""

class EscalationRecord(BaseModel):
    escalation_id: str
    avoidance_warnings: str = ""

class OverrideRecord(BaseModel):
    override_id: str
    residual_risk_notes: str = ""

class HaltRecord(BaseModel):
    halt_id: str
    halt_class: HaltClass
    release_conditions: str = ""

class RevocationRecord(BaseModel):
    revocation_id: str
    stale_caveats: str = ""

class RollbackRecord(BaseModel):
    rollback_id: str
    credibility_notes: str = ""

class AutonomyObservationRecord(BaseModel):
    observation_id: str
    sufficiency_notes: str = ""

class AutonomyDebtRecord(BaseModel):
    debt_id: str
    stale_delegation_debt: int = 0
    self_approval_debt: int = 0

class AutonomyForecastReport(BaseModel):
    forecast_id: str
    delegation_decay: float = 0.0

class AutonomyEquivalenceReport(BaseModel):
    equivalence_id: str
    verdict: EquivalenceVerdict

class AutonomyDivergenceReport(BaseModel):
    divergence_id: str
    divergence_notes: str = ""

class AutonomyTrustVerdict(BaseModel):
    verdict_id: str
    verdict: TrustVerdict
    blockers: List[str] = Field(default_factory=list)
    caveats: List[str] = Field(default_factory=list)

class AutonomyAuditRecord(BaseModel):
    audit_id: str
    audit_notes: str = ""

class AutonomyArtifactManifest(BaseModel):
    manifest_id: str
    artifacts: List[str] = Field(default_factory=list)

class AutonomyObject(BaseModel):
    autonomy_id: str
    agent_id: str
    delegation_id: Optional[str] = None
    autonomy_class: AutonomyClass
    owner: str
    authorization_posture: str
    intervention_posture: str
""")

# Base
create_file("app/autonomy_plane/base.py", """class AutonomyRegistryBase:
    pass

class AuthorizationEvaluatorBase:
    pass

class InterventionEvaluatorBase:
    pass

class TrustEvaluatorBase:
    pass
""")

# Create many stub files
files = [
    "registry", "objects", "taxonomy", "agents", "tasks", "goals", "intents", "scopes",
    "capabilities", "permissions", "delegation", "approvals", "guardrails", "constraints",
    "budgets", "plans", "rationale", "confidence", "uncertainty", "self_checks",
    "verification", "sandboxes", "execution", "interventions", "escalations", "overrides",
    "halts", "revocations", "rollbacks", "observations", "human_review", "incidents",
    "recovery", "environment", "changes", "contracts", "state", "constitution", "security",
    "compliance", "federation", "learning", "scenario", "quality", "trust", "manifests",
    "reporting", "storage", "repository", "__init__"
]
for f in files:
    create_file(f"app/autonomy_plane/{f}.py", f"# {f} module\n")

# README
create_file("app/autonomy_plane/README.md", """# Autonomy Plane

Provides typed, bounded autonomy governance.
- agents/tasks -> permissions/delegations -> guardrails/self-checks -> execution/intervention -> halt/trust.
- capability != permission != autonomy.
- no self-approval / no silent autonomy.
""")
