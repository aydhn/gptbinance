from enum import Enum

class ReleaseClass(str, Enum):
    DATA_FEATURE_MODEL_BUNDLE = "data_feature_model_bundle"
    STRATEGY_BUNDLE = "strategy_bundle"
    ALLOCATION_EXECUTION_BUNDLE = "allocation_execution_bundle"
    RISK_CONTROL_BUNDLE = "risk_control_bundle"
    WORKFLOW_ORCHESTRATION_BUNDLE = "workflow_orchestration_bundle"
    ENVIRONMENT_PATCH_BUNDLE = "environment_patch_bundle"

class CandidateClass(str, Enum):
    RELEASE_TRAIN_CANDIDATE = "release_train_candidate"
    PROBATIONARY_RELEASE = "probationary_release"
    CANARY_RELEASE = "canary_release"
    EMERGENCY_HOTFIX_RELEASE = "emergency_hotfix_release"

class BundleClass(str, Enum):
    STANDARD = "standard"
    EXPERIMENTAL = "experimental"
    EMERGENCY = "emergency"

class EnvironmentClass(str, Enum):
    REPLAY = "replay"
    PAPER = "paper"
    PROBATION = "probation"
    LIVE_CANARY = "live_canary"
    LIVE_FULL = "live_full"
    TEST = "test"

class RolloutClass(str, Enum):
    STAGED = "staged"
    DIRECT = "direct"
    GRADUAL = "gradual"
    EMERGENCY = "emergency"

class CanaryClass(str, Enum):
    TRAFFIC_SPLIT = "traffic_split"
    USER_SUBSET = "user_subset"
    ISOLATED_VENUE = "isolated_venue"
    FEATURE_FLAG = "feature_flag"

class RollbackClass(str, Enum):
    IMMEDIATE_REVERT = "immediate_revert"
    GRACEFUL_FALLBACK = "graceful_fallback"
    DATA_MIGRATION_REVERT = "data_migration_revert"

class HotfixClass(str, Enum):
    TEMPORARY_PATCH = "temporary_patch"
    PERMANENT_FIX = "permanent_fix"
    CONFIGURATION_OVERRIDE = "configuration_override"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    INCOMPARABLE = "incomparable"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
