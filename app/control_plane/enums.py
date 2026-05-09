from enum import Enum


class CommandClass(str, Enum):
    FREEZE_SYMBOL = "freeze_symbol"
    FREEZE_SLEEVE = "freeze_sleeve"
    FREEZE_STRATEGY = "freeze_strategy"
    NO_NEW_EXPOSURE_SCOPE = "no_new_exposure_scope"
    KILL_EXECUTION = "kill_execution"
    PAUSE_WORKFLOW = "pause_workflow"
    REQUEST_RERUN = "request_rerun"
    REQUEST_BACKFILL_REVIEW = "request_backfill_review"
    ROLLBACK_CANDIDATE_EXPANSION = "rollback_candidate_expansion"
    REVOKE_EXCEPTION_TOKEN = "revoke_exception_token"
    UNFREEZE_SCOPE = "unfreeze_scope"
    INCIDENT_HOLD = "incident_hold"
    GUARDED_RESUME = "guarded_resume"
    RISK_OVERRIDE_REQUEST = "risk_override_request"
    ACTIVATION_STOP_REQUEST = "activation_stop_request"


class ActionClass(str, Enum):
    IMMEDIATE = "immediate"
    DEFERRED = "deferred"
    REVIEW_REQUIRED = "review_required"


class PreviewClass(str, Enum):
    FULL_FIDELITY = "full_fidelity"
    PARTIAL = "partial"
    UNKNOWN = "unknown"


class ApprovalClass(str, Enum):
    SINGLE = "single"
    DUAL_CONTROL = "dual_control"
    QUORUM = "quorum"


class ExceptionClass(str, Enum):
    TIME_BOUND = "time_bound"
    SINGLE_USE = "single_use"
    MULTI_STEP = "multi_step"


class RollbackClass(str, Enum):
    REVERSIBLE = "reversible"
    IRREVERSIBLE = "irreversible"


class ScopeClass(str, Enum):
    GLOBAL = "global"
    ENVIRONMENT = "environment"
    WORKSPACE = "workspace"
    PROFILE = "profile"
    SESSION = "session"
    SYMBOL = "symbol"
    SLEEVE = "sleeve"
    STRATEGY = "strategy"
    ACCOUNT = "account"
    WORKFLOW = "workflow"


class KillSwitchClass(str, Enum):
    EXECUTION_GLOBAL = "execution_global"
    SYMBOL_KILL = "symbol_kill"
    WORKFLOW_HALT = "workflow_halt"
    ACTIVATION_HALT = "activation_halt"
    EMERGENCY_FREEZE = "emergency_freeze"


class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
