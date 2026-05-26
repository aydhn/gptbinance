from enum import Enum

class RecoveryClass(str, Enum):
    SETTLEMENT_DEFAULT = "settlement_default"
    PERFORMANCE_SECURITY = "performance_security"
    LIABILITY_CONTRIBUTION = "liability_contribution"
    REMEDY_EXECUTION = "remedy_execution"
    CONTRACT_CURE = "contract_cure"
    CUSTOMER_COMPENSATION = "customer_compensation"
    ENFORCEMENT_REVERSAL = "enforcement_reversal"
    COMPLIANCE_FOLLOWTHROUGH = "compliance_followthrough"
    MIGRATION_LOSS = "migration_loss"
    RELEASE_REGRESSION = "release_regression"
    FEDERATED_PARTNER = "federated_partner"
    CROSS_PLANE_REALIZATION = "cross_plane_realization"

class ClaimClass(str, Enum):
    DIRECT = "direct"
    CONTINGENT = "contingent"
    DISPUTED = "disputed"
    EXTINGUISHED = "extinguished"

class SourceClass(str, Enum):
    SECURITY = "security"
    SETTLEMENT = "settlement"
    CONTRIBUTION = "contribution"
    OFFSET = "offset"

class SecuredClass(str, Enum):
    FIRST_PRIORITY = "first_priority"
    SHARED = "shared"
    EXHAUSTED = "exhausted"
    UNDER_SECURED = "under_secured"

class WaterfallClass(str, Enum):
    SIMPLE = "simple"
    TIERED = "tiered"
    PRO_RATA = "pro_rata"
    CONDITIONAL = "conditional"

class PriorityClass(str, Enum):
    FIRST_TIER = "first_tier"
    PARI_PASSU = "pari_passu"
    SUBORDINATED = "subordinated"
    CONTESTED = "contested"

class DistributionClass(str, Enum):
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    WITHHELD = "withheld"
    DISPUTED = "disputed"

class ShortfallClass(str, Enum):
    QUANTIFIED = "quantified"
    TEMPORARY = "temporary"
    STRUCTURAL = "structural"
    HIDDEN = "hidden"

class DeficiencyClass(str, Enum):
    SECURED = "secured"
    UNSECURED = "unsecured"
    POST_WATERFALL = "post_waterfall"
    STALE = "stale"

class ClawbackClass(str, Enum):
    RECOVERABLE_BACK = "recoverable_back"
    SETTLEMENT = "settlement"
    DISTRIBUTION_EXPOSURE = "distribution_exposure"
    HIDDEN = "hidden"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    PARTIAL = "partial"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
