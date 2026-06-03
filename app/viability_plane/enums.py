from enum import Enum

class ViabilityClass(str, Enum):
    OPERATING = "operating_viability"
    BENEFICIARY_AFFORDABILITY = "beneficiary_affordability_viability"
    GOVERNANCE_BURDEN = "governance_burden_viability"
    RESILIENCE_CARRY = "resilience_carry_viability"

class RunwayClass(str, Enum):
    HEALTHY = "healthy"
    THINNING = "thinning"
    UNSTABLE = "unstable"
    FALSE_RUNWAY = "false_runway"

class BurdenClass(str, Enum):
    DIRECT = "direct_burden"
    INDIRECT = "indirect_burden"
    CROSS_PLANE = "cross_plane_burden"
    HIDDEN = "hidden_burden"

class SubsidyClass(str, Enum):
    TRANSPARENT = "transparent_subsidy"
    TEMPORARY = "temporary_subsidy"
    DEPENDENCY = "dependency_subsidy"
    HIDDEN = "hidden_subsidy"

class AffordabilityClass(str, Enum):
    AFFORDABLE = "affordable"
    STRAINED = "strained"
    COLLAPSING = "collapsing"
    FAKE = "fake_affordability"

class SustainabilityClass(str, Enum):
    SUSTAINABLE = "sustainable"
    DEFERRED_MAINTENANCE = "deferred_maintenance"
    OPERATOR_BURN = "operator_burn"
    PHANTOM_PROFITABLE = "phantom_profitable"

class LeakageClass(str, Enum):
    CONTAINED = "contained"
    GROWING = "growing"
    SYSTEMIC = "systemic"
    HIDDEN = "hidden_leakage"

class DebtClass(str, Enum):
    HIDDEN_SUBSIDY_DEBT = "hidden_subsidy_debt"
    DEFERRED_MAINTENANCE_DEBT = "deferred_maintenance_debt"
    OPERATOR_BURN_DEBT = "operator_burn_debt"
    AFFORDABILITY_DEBT = "affordability_debt"
    GOVERNANCE_OVERHEAD_DEBT = "governance_overhead_debt"

class DriftClass(str, Enum):
    MARGIN_DRIFT = "margin_drift"
    AFFORDABILITY_DRIFT = "affordability_drift"
    SUBSIDY_DRIFT = "subsidy_drift"
    HIDDEN_DRIFT = "hidden_viability_drift"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial_equivalence"
    DIVERGED = "diverged"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
