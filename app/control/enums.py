from enum import Enum


class SensitiveActionType(str, Enum):
    ARM_MAINNET_EXECUTION = "arm_mainnet_execution"
    START_LIVE_SESSION = "start_live_session"
    SWITCH_LIVE_ROLLOUT_MODE = "switch_live_rollout_mode"
    FLATTEN_LIVE_SESSION = "flatten_live_session"
    ROLLBACK_LIVE_SESSION = "rollback_live_session"
    DISARM_LIVE_EXECUTION = "disarm_live_execution"
    APPLY_UPGRADE = "apply_upgrade"
    APPLY_ROLLBACK = "apply_rollback"
    APPLY_RESTORE = "apply_restore"
    APPLY_ROTATION = "apply_rotation"
    DESTRUCTIVE_RETENTION_CLEANUP = "destructive_retention_cleanup"
    MANUAL_CLEAR_KILL_SWITCH = "manual_clear_kill_switch"
    FORCE_RESUME_AFTER_INCIDENT = "force_resume_after_incident"
    FORCE_SKIP_MAINTENANCE_BLOCK = "force_skip_maintenance_block"
    FORCE_RECONCILIATION_OVERRIDE = "force_reconciliation_override"
    ARBITRARY_ACTION = "arbitrary_action"


class ActionCriticality(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ApprovalStatus(str, Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"
    REVOKED = "revoked"
    EXPIRED = "expired"
    SUPERSEDED = "superseded"


class AuthorizationVerdict(str, Enum):
    APPROVED = "approved"
    DENIED = "denied"
    REQUIRE_MORE_APPROVALS = "require_more_approvals"
    STALE = "stale"


class OperatorRole(str, Enum):
    OPS = "ops"
    RISK = "risk"
    SECURITY = "security"
    RELEASE = "release"
    ADMIN = "admin"


class ApprovalMode(str, Enum):
    SINGLE = "single"
    DUAL = "dual"
    MULTI = "multi"


class RevocationReason(str, Enum):
    CONTEXT_CHANGED = "context_changed"
    EMERGENCY = "emergency"
    MANUAL_CANCEL = "manual_cancel"
    ERROR_IN_REQUEST = "error_in_request"


class BreakGlassSeverity(str, Enum):
    INCIDENT_RECOVERY = "incident_recovery"
    SYSTEM_DOWN = "system_down"
    CRITICAL_RISK = "critical_risk"


class CommandStatus(str, Enum):
    REQUESTED = "requested"
    AUTHORIZED = "authorized"
    EXECUTED = "executed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class PolicySeverity(str, Enum):
    STRICT = "strict"
    RELAXED = "relaxed"
