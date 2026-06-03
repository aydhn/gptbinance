from enum import Enum

class ResilienceClass(str, Enum):
    LIQUIDITY_RESILIENCE = "liquidity_resilience"
    EXECUTION_RESILIENCE = "execution_resilience"
    DATA_INTEGRITY_RESILIENCE = "data_integrity_resilience"
    AUTONOMY_FAILURE_RESILIENCE = "autonomy_failure_resilience"
    ORCHESTRATION_BREAKDOWN_RESILIENCE = "orchestration_breakdown_resilience"
    ASSURANCE_DEGRADE_RESILIENCE = "assurance_degrade_resilience"
    IMMUNITY_MUTATION_RESILIENCE = "immunity_mutation_resilience"
    ADAPTATION_BACKLOG_RESILIENCE = "adaptation_backlog_resilience"
    DRIFT_BREACH_RESILIENCE = "drift_breach_resilience"
    BENEFICIARY_PROTECTION_RESILIENCE = "beneficiary_protection_resilience"
    FEDERATED_DISCONNECT_RESILIENCE = "federated_disconnect_resilience"
    CROSS_PLANE_COMPOUND_SHOCK_RESILIENCE = "cross_plane_compound_shock_resilience"

class ShockClass(str, Enum):
    ISOLATED = "isolated"
    SYSTEMIC = "systemic"
    TRANSIENT = "transient"
    PERSISTENT = "persistent"

class DegradationClass(str, Enum):
    GRACEFUL = "graceful"
    SHARP = "sharp"
    DECEPTIVE = "deceptive"
    BENEFICIARY_COSTLY = "beneficiary_costly"

class ContainmentClass(str, Enum):
    BOUNDED = "bounded"
    LEAKING = "leaking"
    DELAYED = "delayed"
    FALSE = "false"

class FallbackClass(str, Enum):
    VIABLE = "viable"
    PARTIAL = "partial"
    FAKE = "fake"
    STALE = "stale"

class ReserveClass(str, Enum):
    USABLE = "usable"
    THIN = "thin"
    RESTRICTED = "restricted"
    PHANTOM = "phantom"

class RecoveryClass(str, Enum):
    HEALTHY = "healthy"
    STRAINED = "strained"
    WEAK = "weak"
    FAKE = "fake"

class ExhaustionClass(str, Enum):
    NEAR = "near"
    ACTIVE = "active"
    DELAYED = "delayed"
    HIDDEN = "hidden"

class LoadClass(str, Enum):
    SUSTAINABLE = "sustainable"
    STRESSED = "stressed"
    OVERLOAD = "overload"
    HIDDEN = "hidden"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
