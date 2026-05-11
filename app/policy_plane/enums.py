from enum import Enum, auto


class PolicyClass(Enum):
    MANDATORY = auto()
    ADVISORY = auto()
    TEMPORARY = auto()
    CANARY_ONLY = auto()
    MAINTENANCE_ONLY = auto()


class RuleClass(Enum):
    ALLOW = auto()
    DENY = auto()
    REQUIRE_REVIEW = auto()
    REQUIRE_EVIDENCE = auto()
    REQUIRE_APPROVAL = auto()
    ALLOW_WITH_EXCEPTION = auto()


class InvariantClass(Enum):
    NON_BYPASSABLE = auto()
    ENVIRONMENT_SEPARATION = auto()
    NO_RELEASE_LESS_ACTIVATION = auto()
    NO_HIDDEN_MANUAL_INTERVENTION = auto()
    NO_UNVERIFIED_RECOVERY = auto()


class ObligationClass(Enum):
    MUST_ATTACH_EVIDENCE = auto()
    MUST_WAIT_FOR_REVIEW = auto()
    MUST_WAIT_FOR_APPROVAL = auto()
    MUST_USE_RELEASE_MANIFEST = auto()
    MUST_HAVE_CLEAN_READINESS = auto()
    MUST_RECORD_EXCEPTION_RECEIPT = auto()
    MUST_VERIFY_REMEDIATION = auto()


class SubjectClass(Enum):
    HUMAN_OPERATOR = auto()
    WORKFLOW_JOB = auto()
    RELEASE_CANDIDATE = auto()
    ACTIVATION_STAGE = auto()
    STRATEGY = auto()
    EXPERIMENT_ARM = auto()
    MODEL_MANIFEST = auto()
    DATA_SNAPSHOT = auto()
    SYSTEM_ACTOR = auto()


class ActionClass(Enum):
    ACTIVATE = auto()
    ROLLOUT = auto()
    ALLOCATE = auto()
    EXECUTE = auto()
    FREEZE = auto()
    UNFREEZE = auto()
    RERUN = auto()
    BACKFILL = auto()
    APPROVE = auto()
    ROLLBACK = auto()
    PROMOTE_CANDIDATE = auto()
    CLOSE_INCIDENT = auto()
    CLOSE_POSTMORTEM = auto()


class ResourceClass(Enum):
    SYMBOL = auto()
    SLEEVE = auto()
    STRATEGY = auto()
    WORKFLOW = auto()
    RELEASE_BUNDLE = auto()
    ENVIRONMENT = auto()
    MODEL = auto()
    DATA_SNAPSHOT = auto()
    INCIDENT = auto()
    POSTMORTEM = auto()
    ACCOUNT_PROFILE_WORKSPACE = auto()


class VerdictClass(Enum):
    ALLOW = auto()
    DENY = auto()
    ALLOW_WITH_REVIEW = auto()
    ALLOW_WITH_EVIDENCE = auto()
    ALLOW_WITH_APPROVAL = auto()
    ALLOW_WITH_EXCEPTION = auto()
    BLOCKED_PENDING_CONTEXT = auto()
    REVIEW_REQUIRED = auto()


class ExceptionClass(Enum):
    SCOPED = auto()
    TTL_BOUND = auto()
    INCIDENT_LINKED = auto()
    CONTROL_PLANE_SOURCED = auto()


class EquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    DIVERGENT = auto()
    PARTIALLY_EQUIVALENT = auto()


class TrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()


class ConflictSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()
