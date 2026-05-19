from enum import Enum

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
