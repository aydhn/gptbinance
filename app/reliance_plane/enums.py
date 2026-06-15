from enum import Enum

class RelianceClass(str, Enum):
    ATTESTED_STATE = "attested_state"
    COMPLIANCE_CERTIFICATE = "compliance_certificate"
    EFFECTUATION_COMPLETION = "effectuation_completion"
    RELEASE_READINESS = "release_readiness"
    MIGRATION_CUTOVER = "migration_cutover"
    SUCCESSOR_CLEAN_STATE = "successor_clean_state"
    SUNSET_RETIRED_STATE = "sunset_retired_state"
    RIGHTS_RESTORATION = "rights_restoration"
    FEDERATED_CERTIFICATE = "federated_certificate"
    COMPENSATING_REVIEW = "compensating_review"
    CROSS_PLANE_DECISION_USE = "cross_plane_decision_use"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
