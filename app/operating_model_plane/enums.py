from enum import Enum

class OperatingObjectClass(str, Enum):
    PORTFOLIO = "portfolio"
    PROGRAM = "program"
    RELEASE = "release"
    INCIDENT = "incident"
    SECURITY = "security"
    COMPLIANCE = "compliance"
    CONTINUITY = "continuity"
    WORKFLOW = "workflow"
    DECISION = "decision"
    SYSTEM_SURFACE = "system_surface"

class RoleClass(str, Enum):
    ACCOUNTABLE_OWNER = "accountable_owner"
    RESPONSIBLE_EXECUTOR = "responsible_executor"
    REVIEWER = "reviewer"
    APPROVER = "approver"
    BACKUP = "backup"
    ESCALATION_RECEIVER = "escalation_receiver"

class OwnershipClass(str, Enum):
    PRIMARY = "primary"
    SHARED_WITH_DRI = "shared_with_dri"
    TEMPORARY = "temporary"

class CoverageClass(str, Enum):
    BUSINESS_HOURS_ONLY = "business_hours_only"
    FOLLOW_THE_SUN = "follow_the_sun"
    ON_CALL_24_7 = "on_call_24_7"
    NO_COVERAGE = "no_coverage"

class IndependenceClass(str, Enum):
    FULLY_INDEPENDENT = "fully_independent"
    DOMAIN_PEER = "domain_peer"
    SAME_CHAIN_CONFLICT = "same_chain_conflict"
    SELF_REVIEW = "self_review"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGED_ACCOUNTABILITY = "diverged_accountability"
    DIVERGED_COVERAGE = "diverged_coverage"
    DIVERGED_INDEPENDENCE = "diverged_independence"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
