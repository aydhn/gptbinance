from enum import Enum


class ConfigDomain(str, Enum):
    STRATEGY = "strategy"
    RISK = "risk"
    EVENT_RISK = "event-risk"
    MARKET_TRUTH = "market-truth"
    ORDER_INTENT = "order-intent"
    LIFECYCLE = "lifecycle"
    SHADOW_STATE = "shadow-state"
    CAPITAL = "capital"
    CROSS_BOOK = "cross-book"
    POLICY_READINESS = "policy-readiness"
    ACTIVATION = "activation"
    INCIDENTS = "incidents"
    REMEDIATION = "remediation"
    MIGRATIONS = "migrations"
    EXPERIMENTS = "experiments"
    RELIABILITY = "reliability"
    RELEASE_RUNTIME = "release-runtime"


class ParameterClass(str, Enum):
    NUMERIC = "numeric"
    BOOLEAN = "boolean"
    STRING = "string"
    LIST = "list"
    DICT = "dict"


class LayerClass(str, Enum):
    BASE_DEFAULTS = "base_defaults"
    WORKSPACE_DEFAULTS = "workspace_defaults"
    PROFILE_DEFAULTS = "profile_defaults"
    SYMBOL_OVERRIDES = "symbol_overrides"
    CANDIDATE_BUNDLE = "candidate_bundle"
    ACTIVATION_SCOPE_OVERLAY = "activation_scope_overlay"
    DEGRADED_MODE_OVERLAY = "degraded_mode_overlay"
    INCIDENT_CONTAINMENT_OVERLAY = "incident_containment_overlay"
    EXPERIMENT_CANDIDATE_OVERLAY = "experiment_candidate_overlay"
    REMEDIATION_RECOVERY_OVERLAY = "remediation_recovery_overlay"
    RUNTIME_SAFE_PATCH_INTENT = "runtime_safe_patch_intent"


class MutabilityClass(str, Enum):
    IMMUTABLE = "immutable"
    RELEASE_ONLY = "release_only"
    REVIEW_ONLY = "review_only"
    RUNTIME_SAFE = "runtime_safe"
    EMERGENCY_OVERLAY_ONLY = "emergency_overlay_only"
    EXPERIMENT_ONLY = "experiment_only"
    SECRET_ADJACENT = "secret_adjacent"


class ScopeClass(str, Enum):
    GLOBAL = "global"
    WORKSPACE = "workspace"
    PROFILE = "profile"
    SYMBOL = "symbol"
    SESSION = "session"
    STAGE = "stage"


class DiffSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class DriftSeverity(str, Enum):
    MINOR = "minor"
    MAJOR = "major"
    CRITICAL = "critical"


class EquivalenceVerdict(str, Enum):
    CLEAN = "clean"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class ConfigVerdict(str, Enum):
    VALID = "valid"
    INVALID = "invalid"
    UNKNOWN = "unknown"


class SecretVisibility(str, Enum):
    METADATA_ONLY = "metadata_only"
    REDACTED = "redacted"
    CLEAR = "clear"  # Only in isolated memory, never exported
