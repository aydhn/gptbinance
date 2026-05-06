from enum import Enum, auto


class PrincipalType(Enum):
    HUMAN = auto()
    SERVICE = auto()
    SYSTEM = auto()


class PrincipalStatus(Enum):
    ACTIVE = auto()
    SUSPENDED = auto()
    PROBATIONARY = auto()
    REVIEW_ONLY = auto()


class RoleClass(Enum):
    READONLY_OBSERVER = auto()
    RUNTIME_OPERATOR = auto()
    REVIEW_OPERATOR = auto()
    FINAL_ADJUDICATOR = auto()
    INCIDENT_RESPONDER = auto()
    RELEASE_GATEKEEPER = auto()
    MIGRATION_REVIEWER = auto()
    REMEDIATION_REVIEWER = auto()
    EVIDENCE_READER = auto()
    RELIABILITY_REVIEWER = auto()


class CapabilityClass(Enum):
    READ_EVIDENCE_PACK = auto()
    BUILD_CASE_FILE = auto()
    REQUEST_REVIEW = auto()
    ADJUDICATE_REVIEW = auto()
    REQUEST_ACTIVATION_TRANSITION = auto()
    REVIEW_INCIDENT_CONTAINMENT = auto()
    REQUEST_MIGRATION_APPLY = auto()
    REVIEW_NON_REVERSIBLE_MIGRATION = auto()
    REVIEW_BREAKGLASS = auto()
    ACCESS_RESTRICTED_EVIDENCE_SUMMARY = auto()
    ACCESS_RUNTIME_POSTURE = auto()
    REQUEST_RELEASE_HOLD_REVIEW = auto()
    FINALIZE_POSTMORTEM = auto()
    REVIEW_CAPA_EFFECTIVENESS = auto()


class TrustZone(Enum):
    PUBLIC_READONLY = auto()
    OPERATIONAL_READONLY = auto()
    REVIEW_RESTRICTED = auto()
    RELEASE_CONTROLLED = auto()
    RUNTIME_SENSITIVE = auto()
    INCIDENT_SENSITIVE = auto()
    SECRET_ADJACENT = auto()
    BREAKGLASS_EMERGENCY = auto()


class SessionClass(Enum):
    REVIEW = auto()
    RUNTIME_SERVICE = auto()
    LIMITED_READ = auto()
    INCIDENT_EMERGENCY = auto()


class DelegationClass(Enum):
    STANDARD = auto()
    RESTRICTED = auto()


class ElevationClass(Enum):
    PURPOSE_BOUND = auto()
    TEMPORARY_ADMIN = auto()  # Note: strict TTL and review required


class BreakglassClass(Enum):
    INCIDENT_RECOVERY = auto()
    EMERGENCY_HALT = auto()
    CRITICAL_MIGRATION_FIX = auto()


class AuthorizationVerdict(Enum):
    ALLOW = auto()
    DENY = auto()
    HOLD = auto()
    NEEDS_REVIEW = auto()


class ScopeClaimClass(Enum):
    WORKSPACE = auto()
    PROFILE = auto()
    SYMBOL_SET = auto()
    SESSION_WINDOW = auto()
    CANDIDATE = auto()
    INCIDENT = auto()
    POSTMORTEM = auto()
    RELEASE = auto()
    CAPITAL_TIER = auto()
