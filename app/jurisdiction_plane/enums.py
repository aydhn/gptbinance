from enum import Enum

class JurisdictionClassEnum(Enum):
    STANDARD = "standard"

class ScopeClassEnum(Enum):
    ACTOR = "actor"
    DOMAIN = "domain"

class SubjectClassEnum(Enum):
    HUMAN = "human"

class RegimeClassEnum(Enum):
    CONSTITUTIONAL = "constitutional"

class GoverningSourceEnum(Enum):
    AUTHORITATIVE = "authoritative"

class ApplicabilityClassEnum(Enum):
    FULLY_APPLICABLE = "fully_applicable"

class ExclusionClassEnum(Enum):
    ACTOR_EXCLUSION = "actor_exclusion"

class ExemptionClassEnum(Enum):
    POLICY_EXEMPTION = "policy_exemption"

class WaiverClassEnum(Enum):
    TEMPORARY_WAIVER = "temporary_waiver"

class PrecedenceClassEnum(Enum):
    CONSTITUTIONAL_PRECEDENCE = "constitutional_precedence"

class ReachClassEnum(Enum):
    ACTOR_REACH = "actor_reach"

class PortabilityClassEnum(Enum):
    PORTABLE = "portable"

class EquivalenceVerdictEnum(Enum):
    EQUIVALENT = "equivalent"

class TrustVerdictEnum(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
