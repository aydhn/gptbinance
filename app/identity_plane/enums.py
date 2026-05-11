from enum import Enum

class PrincipalClass(str, Enum):
    HUMAN_OPERATOR = "human_operator"
    REVIEWER = "reviewer"
    APPROVER = "approver"
    SERVICE_RUNTIME = "service_runtime"
    WORKFLOW_ACTOR = "workflow_actor"
    RELEASE_ACTOR = "release_actor"
    INCIDENT_RESPONDER = "incident_responder"
    AUTOMATION_BOT = "automation_bot"
    MIGRATION_ACTOR = "migration_actor"
    POLICY_ADMIN = "policy_admin"
    READ_ONLY_OBSERVER = "read_only_observer"
    BREAK_GLASS_ACTOR = "break_glass_actor"
    SYSTEM_ACTOR = "system_actor"

class LifecycleState(str, Enum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    REVOKED = "revoked"
    PENDING_APPROVAL = "pending_approval"

class CapabilityRiskClass(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class SessionClass(str, Enum):
    INTERACTIVE = "interactive"
    API = "api"
    WORKFLOW_RUN = "workflow_run"
    EPHEMERAL = "ephemeral"

class DelegationClass(str, Enum):
    HUMAN_TO_SERVICE = "human_to_service"
    WORKFLOW_DELEGATION = "workflow_delegation"

class ImpersonationClass(str, Enum):
    INCIDENT_ONLY = "incident_only"
    APPROVED_ADMIN = "approved_admin"

class ElevationClass(str, Enum):
    JUST_IN_TIME = "just_in_time"
    MIGRATION_CUTOVER = "migration_cutover"
    INCIDENT_PERIOD = "incident_period"

class RevocationClass(str, Enum):
    IMMEDIATE_KILL = "immediate_kill"
    PARTIAL = "partial"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
