from enum import Enum


class ConfigDomain(str, Enum):
    STRATEGY = "strategy"
    RISK = "risk"
    EVENT_RISK = "event_risk"
    MARKET_TRUTH = "market_truth"
    ORDER_INTENT = "order_intent"
    LIFECYCLE = "lifecycle"
    SHADOW_STATE = "shadow_state"
    CAPITAL = "capital"
    CROSS_BOOK = "cross_book"
    POLICY = "policy"
    READINESS = "readiness"
    ACTIVATION = "activation"
    INCIDENTS = "incidents"
    REMEDIATION = "remediation"
    MIGRATIONS = "migrations"
    EXPERIMENTS = "experiments"
    RELIABILITY = "reliability"
    RELEASE = "release"
    RUNTIME = "runtime"


class MutabilityClass(str, Enum):
    IMMUTABLE = "immutable"
    RELEASE_ONLY = "release_only"
    REVIEW_ONLY = "review_only"
    RUNTIME_SAFE = "runtime_safe"
    EMERGENCY_OVERLAY_ONLY = "emergency_overlay_only"
    EXPERIMENT_ONLY = "experiment_only"


class ParameterClass(str, Enum):
    STANDARD = "standard"
    SECRET_ADJACENT = "secret_adjacent"


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


class ScopeClass(str, Enum):
    GLOBAL = "global"
    WORKSPACE = "workspace"
    PROFILE = "profile"
    SYMBOL = "symbol"
    SESSION = "session"
    CANDIDATE = "candidate"
    ACTIVATION_STAGE = "activation_stage"
    CAPITAL_TIER = "capital_tier"


class DiffSeverity(str, Enum):
    MINOR = "minor"
    MODERATE = "moderate"
    CRITICAL = "critical"


class DriftSeverity(str, Enum):
    NEGLIGIBLE = "negligible"
    MODERATE = "moderate"
    SEVERE = "severe"
    CRITICAL_BLOCKER = "critical_blocker"


class EquivalenceVerdict(str, Enum):
    CLEAN = "clean"
    CAUTION = "caution"
    DEGRADED = "degraded"
    REVIEW_REQUIRED = "review_required"
    BLOCKED = "blocked"


class ConfigVerdict(str, Enum):
    VALID = "valid"
    INVALID = "invalid"


class SecretVisibility(str, Enum):
    REDACTED = "redacted"
    METADATA_ONLY = "metadata_only"
    VISIBLE = "visible"  # extremely rare, internal use only
