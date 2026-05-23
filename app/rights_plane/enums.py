from enum import Enum

class RightClass(Enum):
    ACCESS = "access"
    USE = "use"
    NOTICE = "notice"
    REMEDY = "remedy"
    CHALLENGE = "challenge"
    PORTABILITY = "portability"
    INALIENABLE = "inalienable"

class EntitlementClass(Enum):
    DIRECT = "direct"
    CONTINGENT = "contingent"
    CONDITIONAL = "conditional"
    DERIVED = "derived"

class ClaimClass(Enum):
    ASSERTED = "asserted"
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"

class StandingClass(Enum):
    DIRECT = "direct"
    REPRESENTATIVE = "representative"
    DELEGATED = "delegated"
    NONE = "none"

class ConsentClass(Enum):
    EXPLICIT = "explicit"
    SCOPED = "scoped"
    CONDITIONAL = "conditional"
    DEGRADED = "degraded"
    PSEUDO = "pseudo"

class WaiverClass(Enum):
    SCOPED = "scoped"
    TEMPORARY = "temporary"
    INFORMED = "informed"
    INVALID = "invalid"

class RevocationClass(Enum):
    HOLDER = "holder"
    SYSTEM = "system"
    DOWNSTREAM = "downstream"

class BeneficiaryClass(Enum):
    DIRECT = "direct"
    DOWNSTREAM = "downstream"
    FEDERATED = "federated"
    HARMED = "harmed"

class ExhaustionClass(Enum):
    EXHAUSTED = "exhausted"
    PARTIAL = "partial"
    NOT_EXHAUSTED = "not_exhausted"
    FALSELY_EXHAUSTED = "falsely_exhausted"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    PARTIAL = "partial"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
